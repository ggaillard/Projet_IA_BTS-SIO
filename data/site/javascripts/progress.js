// Configuration des sections par module
const moduleConfig = {
    module1: {
        sections: [
            'module1-intro-pratique',
            'module1-concepts-fondamentaux',
            'module1-mini-projet',
            'module1-auto-evaluation'
        ],
        totalActivities: 10
    },
    module2: {
        sections: [
            'module2-reseaux-convolutifs',
            'module2-reseaux-recurrents',
            'module2-challenge-amelioration'
        ],
        totalActivities: 10
    },
    module3: {
        sections: [
            'module3-frameworks',
            'module3-integration',
            'module3-preparation-projet'
        ],
        totalActivities: 9
    },
    module4: {
        sections: [
            'module4-developpement',
            'module4-finalisation',
            'module4-presentation'
        ],
        totalActivities: 10
    }
};

// Définition des badges
const badgesList = [
    {
        id: 'explorateur',
        icon: '🔍',
        name: 'Explorateur',
        description: 'A complété toutes les démonstrations pratiques',
        condition: ['module1-intro-pratique']
    },
    {
        id: 'neurone',
        icon: '🧠',
        name: 'Neurone activé',
        description: 'A compris les fondamentaux des réseaux de neurones',
        condition: ['module1-concepts-fondamentaux']
    },
    {
        id: 'experimentateur',
        icon: '🔬',
        name: 'Expérimentateur',
        description: 'A réalisé le mini-projet avec succès',
        condition: ['module1-mini-projet']
    },
    {
        id: 'data-scientist',
        icon: '🧪',
        name: 'Data Scientist',
        description: 'A comparé ML classique et Deep Learning',
        condition: ['module1-intro-pratique', 'module1-concepts-fondamentaux', 'module1-mini-projet', 'module1-auto-evaluation']
    },
    {
        id: 'vision-ia',
        icon: '👁️',
        name: 'Vision IA',
        description: 'A implémenté un CNN fonctionnel',
        condition: ['module2-reseaux-convolutifs']
    },
    {
        id: 'nlp-apprenti',
        icon: '💬',
        name: 'NLP Apprenti',
        description: 'A travaillé avec des modèles de texte',
        condition: ['module2-reseaux-recurrents']
    },
    {
        id: 'optimiseur',
        icon: '🛠️',
        name: 'Optimiseur',
        description: 'A amélioré un modèle sous-optimal',
        condition: ['module2-challenge-amelioration']
    },
    {
        id: 'architecte-ia',
        icon: '🏆',
        name: 'Architecte IA',
        description: 'A maîtrisé différentes architectures de réseaux',
        condition: ['module2-reseaux-convolutifs', 'module2-reseaux-recurrents', 'module2-challenge-amelioration']
    },
    {
        id: 'integrateur',
        icon: '🔧',
        name: 'Intégrateur',
        description: 'A utilisé efficacement un framework ML',
        condition: ['module3-frameworks']
    },
    {
        id: 'performance',
        icon: '⚡',
        name: 'Optimiseur',
        description: 'A optimisé les performances d\'un modèle',
        condition: ['module3-integration']
    },
    {
        id: 'planificateur',
        icon: '📝',
        name: 'Planificateur',
        description: 'A conçu un plan de projet IA',
        condition: ['module3-preparation-projet']
    },
    {
        id: 'developpeur-ia',
        icon: '🚀',
        name: 'Développeur IA',
        description: 'A maîtrisé le développement d\'applications ML',
        condition: ['module3-frameworks', 'module3-integration', 'module3-preparation-projet']
    },
    {
        id: 'ui-designer',
        icon: '💻',
        name: 'UI Designer',
        description: 'A créé une interface conversationnelle',
        condition: ['module4-developpement']
    },
    {
        id: 'testeur',
        icon: '📊',
        name: 'Testeur',
        description: 'A effectué des tests rigoureux',
        condition: ['module4-finalisation']
    },
    {
        id: 'presentateur',
        icon: '🎯',
        name: 'Présentateur',
        description: 'A présenté avec succès le projet final',
        condition: ['module4-presentation']
    },
    {
        id: 'master-ia',
        icon: '🏅',
        name: 'Master IA',
        description: 'A terminé l\'ensemble de la formation',
        condition: [
            'module1-intro-pratique', 'module1-concepts-fondamentaux', 'module1-mini-projet', 'module1-auto-evaluation',
            'module2-reseaux-convolutifs', 'module2-reseaux-recurrents', 'module2-challenge-amelioration',
            'module3-frameworks', 'module3-integration', 'module3-preparation-projet',
            'module4-developpement', 'module4-finalisation', 'module4-presentation'
        ]
    }
];

// Fonction pour sauvegarder la progression d'une section
function saveProgress(section) {
    const checkbox = document.getElementById('section-completed');
    const dateInput = document.getElementById('date-completed');
    
    if (checkbox.checked && dateInput.value) {
        // Sauvegarder la progression dans localStorage
        const progress = JSON.parse(localStorage.getItem('dl-progress') || '{}');
        progress[section] = {
            completed: true,
            date: dateInput.value
        };
        localStorage.setItem('dl-progress', JSON.stringify(progress));
        
        alert(`Section "${section}" marquée comme terminée le ${dateInput.value}!`);
        
        // Mettre à jour les badges
        updateBadges();
    } else {
        alert('Veuillez cocher la case et sélectionner une date.');
    }
}

// Fonction pour charger l'état de progression d'une section
function loadSectionProgress() {
    // Récupérer l'identifiant de la section à partir de l'URL ou d'un attribut data
    const sectionElement = document.querySelector('[data-section-id]');
    if (!sectionElement) return;
    
    const sectionName = sectionElement.getAttribute('data-section-id');
    const progress = JSON.parse(localStorage.getItem('dl-progress') || '{}');
    
    if (progress[sectionName]) {
        document.getElementById('section-completed').checked = progress[sectionName].completed;
        document.getElementById('date-completed').value = progress[sectionName].date;
    }
}

// Fonction pour calculer et afficher la progression globale
function updateProgressBars() {
    const progressBars = document.querySelectorAll('[id$="-progress"]');
    if (progressBars.length === 0) return; // Ne rien faire s'il n'y a pas de barres de progression
    
    const progress = JSON.parse(localStorage.getItem('dl-progress') || '{}');
    
    // Progression par module
    let totalCompleted = 0;
    let totalActivities = 0;
    
    Object.keys(moduleConfig).forEach(moduleId => {
        const module = moduleConfig[moduleId];
        let moduleCompleted = 0;
        
        // Compter les sections complétées dans ce module
        module.sections.forEach(section => {
            if (progress[section] && progress[section].completed) {
                moduleCompleted++;
            }
        });
        
        // Calculer le pourcentage pour ce module
        const modulePercentage = Math.round((moduleCompleted / module.totalActivities) * 100);
        
        // Mettre à jour la barre de progression du module
        const progressBar = document.getElementById(`${moduleId}-progress`);
        const progressText = document.getElementById(`${moduleId}-text`);
        
        if (progressBar && progressText) {
            progressBar.style.width = `${modulePercentage}%`;
            progressText.textContent = `${modulePercentage}%`;
        }
        
        // Mettre à jour les totaux pour la progression globale
        totalCompleted += moduleCompleted;
        totalActivities += module.totalActivities;
    });
    
    // Calculer et afficher la progression globale
    const globalPercentage = Math.round((totalCompleted / totalActivities) * 100);
    const globalProgressBar = document.getElementById('global-progress');
    const globalProgressText = document.getElementById('global-text');
    
    if (globalProgressBar && globalProgressText) {
        globalProgressBar.style.width = `${globalPercentage}%`;
        globalProgressText.textContent = `${globalPercentage}%`;
    }
}

// Fonction pour mettre à jour l'affichage des badges
function updateBadges() {
    const badgesContainer = document.getElementById('badges-container');
    if (!badgesContainer) return;
    
    const progress = JSON.parse(localStorage.getItem('dl-progress') || '{}');
    const unlockedBadges = JSON.parse(localStorage.getItem('dl-badges') || '[]');
    
    // Vérifier s'il n'y a aucun badge débloqué
    let hasUnlockedBadges = false;
    
    // Vider le container
    badgesContainer.innerHTML = '';
    
    // Vérifier les badges débloqués
    badgesList.forEach(badge => {
        const isUnlocked = badge.condition.every(section => progress[section] && progress[section].completed);
        
        // Si le badge est débloqué
        if (isUnlocked) {
            hasUnlockedBadges = true;
            
            // Vérifier s'il était déjà débloqué
            const isNew = !unlockedBadges.includes(badge.id);
            
            // Créer l'élément badge
            const badgeElement = document.createElement('div');
            badgeElement.className = `badge ${isNew ? 'badge-new' : ''}`;
            badgeElement.innerHTML = `
                <div class="badge-icon">${badge.icon}</div>
                <div class="badge-name">${badge.name}</div>
                <div class="badge-description">${badge.description}</div>
            `;
            badgesContainer.appendChild(badgeElement);
            
            // Ajouter à la liste des badges débloqués si c'est nouveau
            if (isNew) {
                unlockedBadges.push(badge.id);
            }
        } else {
            // Afficher le badge verrouillé en grisé
            const badgeElement = document.createElement('div');
            badgeElement.className = 'badge badge-locked';
            badgeElement.innerHTML = `
                <div class="badge-icon">${badge.icon}</div>
                <div class="badge-name">${badge.name}</div>
                <div class="badge-description">Non débloqué</div>
            `;
            badgesContainer.appendChild(badgeElement);
        }
    });
    
    // Afficher le message placeholder si aucun badge n'est débloqué
    if (!hasUnlockedBadges) {
        badgesContainer.innerHTML = '<div class="badge-placeholder">Complétez des sections pour débloquer des badges!</div>';
    }
    
    // Sauvegarder la liste des badges débloqués
    localStorage.setItem('dl-badges', JSON.stringify(unlockedBadges));
}

// Réinitialiser toute la progression
function resetProgress() {
    if (confirm('Êtes-vous sûr de vouloir réinitialiser toute votre progression ? Cette action est irréversible.')) {
        localStorage.removeItem('dl-progress');
        localStorage.removeItem('dl-badges');
        
        updateProgressBars();
        updateBadges();
        
        // Désélectionner les cases à cocher
        const checkbox = document.getElementById('section-completed');
        const dateInput = document.getElementById('date-completed');
        
        if (checkbox) checkbox.checked = false;
        if (dateInput) dateInput.value = '';
        
        alert('Votre progression a été réinitialisée.');
    }
}

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    // Charger l'état de progression de la section actuelle
    loadSectionProgress();
    
    // Mettre à jour les barres de progression si présentes
    updateProgressBars();
    
    // Mettre à jour les badges si présents
    updateBadges();
});