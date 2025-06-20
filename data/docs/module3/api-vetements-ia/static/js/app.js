/**
 * Application de recherche visuelle de vêtements - Frontend
 * 
 * Gère les interactions utilisateur, la capture d'image et les appels API
 */

document.addEventListener('DOMContentLoaded', function() {
    // Éléments DOM
    const imageInput = document.getElementById('image-input');
    const previewImage = document.getElementById('preview-image');
    const analyzeButton = document.getElementById('analyze-button');
    const cameraButton = document.getElementById('camera-button');
    const cameraContainer = document.getElementById('camera-container');
    const cameraFeed = document.getElementById('camera-feed');
    const captureButton = document.getElementById('capture-button');
    const cancelButton = document.getElementById('cancel-button');
    const resultsContainer = document.getElementById('results-container');
    const loadingIndicator = document.getElementById('loading-indicator');
    const predictionResults = document.getElementById('prediction-results');
    const processingTime = document.getElementById('processing-time');
    const exampleItems = document.querySelectorAll('.example-item');
    
    // Variables globales
    let mediaStream = null;
    
    // Prévisualisation de l'image sélectionnée
    imageInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                analyzeButton.disabled = false;
            }
            reader.readAsDataURL(this.files[0]);
            
            // Masquer les résultats précédents
            resultsContainer.style.display = 'none';
        }
    });
    
    // Activation de la caméra
    cameraButton.addEventListener('click', function() {
        cameraContainer.style.display = 'block';
        
        // Accéder à la caméra
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                mediaStream = stream;
                cameraFeed.srcObject = stream;
            })
            .catch(function(error) {
                console.error("Erreur d'accès à la caméra:", error);
                alert("Impossible d'accéder à la caméra. Veuillez vérifier les permissions.");
                cameraContainer.style.display = 'none';
            });
    });
    
    // Capture d'image depuis la caméra
    captureButton.addEventListener('click', function() {
        // Créer un canvas pour capturer l'image
        const canvas = document.createElement('canvas');
        canvas.width = cameraFeed.videoWidth;
        canvas.height = cameraFeed.videoHeight;
        
        // Dessiner l'image sur le canvas
        const context = canvas.getContext('2d');
        context.drawImage(cameraFeed, 0, 0, canvas.width, canvas.height);
        
        // Convertir en URL data
        const imageDataUrl = canvas.toDataURL('image/jpeg');
        
        // Afficher dans l'aperçu
        previewImage.src = imageDataUrl;
        
        // Arrêter la caméra
        stopCamera();
        
        // Masquer le conteneur de caméra
        cameraContainer.style.display = 'none';
        
        // Activer le bouton d'analyse
        analyzeButton.disabled = false;
    });
    
    // Annulation de la prise de photo
    cancelButton.addEventListener('click', function() {
        stopCamera();
        cameraContainer.style.display = 'none';
    });
    
    // Analyse de l'image
    analyzeButton.addEventListener('click', function() {
        // Afficher l'indicateur de chargement
        resultsContainer.style.display = 'block';
        loadingIndicator.style.display = 'block';
        predictionResults.style.display = 'none';
        
        // Récupérer l'image (du file input ou du data URL)
        let imageData;
        if (imageInput.files && imageInput.files[0]) {
            // Envoi du fichier via FormData
            const formData = new FormData();
            formData.append('image', imageInput.files[0]);
            
            // Appel API
            fetch('/api/predict', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(displayResults)
            .catch(handleError);
        } else if (previewImage.src && !previewImage.src.includes('placeholder.png')) {
            // Envoi de l'image en base64
            fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ image: previewImage.src })
            })
            .then(response => response.json())
            .then(displayResults)
            .catch(handleError);
        } else {
            alert("Veuillez sélectionner ou capturer une image");
            resultsContainer.style.display = 'none';
        }
    });
    
    // Utiliser les exemples
    exampleItems.forEach(item => {
        item.addEventListener('click', function() {
            const imagePath = this.getAttribute('data-image');
            previewImage.src = `/static/images/examples/${imagePath}`;
            analyzeButton.disabled = false;
            
            // Masquer les résultats précédents
            resultsContainer.style.display = 'none';
        });
    });
    
    // Fonctions utilitaires
    
    function stopCamera() {
        if (mediaStream) {
            mediaStream.getTracks().forEach(track => track.stop());
            mediaStream = null;
        }
    }
    
    function displayResults(data) {
        // Masquer l'indicateur de chargement
        loadingIndicator.style.display = 'none';
        predictionResults.style.display = 'block';
        
        // Vérifier s'il y a une erreur
        if (data.error) {
            predictionResults.innerHTML = `<div class="error-message">${data.error}</div>`;
            return;
        }
        
        // Afficher le temps de traitement
        processingTime.textContent = data.processing_time_ms || 0;
        
        // Générer le HTML pour les résultats
        let resultsHTML = '';
        
        data.results.forEach((result, index) => {
            const confidence = (result.confidence * 100).toFixed(1);
            const barWidth = confidence + '%';
            const isTopResult = index === 0;
            
            resultsHTML += `
                <div class="result-item ${isTopResult ? 'top-result' : ''}">
                    <div class="result-category">${result.category}</div>
                    <div class="result-confidence">
                        <div class="confidence-bar">
                            <div class="confidence-value" style="width: ${barWidth}"></div>
                        </div>
                        <div class="confidence-percentage">${confidence}%</div>
                    </div>
                </div>
            `;
        });
        
        // Ajouter un message pour le résultat principal
        if (data.results && data.results.length > 0) {
            const topResult = data.results[0];
            resultsHTML = `
                <div class="main-result">
                    <h3>Ce vêtement est probablement un(e) <span class="highlight">${topResult.category}</span></h3>
                </div>
            ` + resultsHTML;
        }
        
        // Insérer les résultats dans la page
        predictionResults.innerHTML = resultsHTML;
    }
    
    function handleError(error) {
        console.error('Erreur lors de l\'analyse:', error);
        loadingIndicator.style.display = 'none';
        predictionResults.style.display = 'block';
        
        predictionResults.innerHTML = `
            <div class="error-message">
                Une erreur est survenue lors de l'analyse de l'image. Veuillez réessayer.
            </div>
        `;
    }
});