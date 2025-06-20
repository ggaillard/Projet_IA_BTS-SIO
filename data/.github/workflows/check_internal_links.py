import os
import re
import sys

def get_all_md_files(docs_dir):
    md_files = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def check_internal_md_links(md_files, docs_dir):
    # Modèle pour capturer les liens Markdown
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    # Liste de tous les fichiers Markdown disponibles (chemins normalisés)
    available_files = [os.path.normpath(f) for f in md_files]
    
    # Dictionnaire pour stocker les liens cassés par fichier
    broken_links = {}
    
    for file_path in md_files:
        file_broken_links = []
        file_dir = os.path.dirname(file_path)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Trouver tous les liens
        matches = link_pattern.findall(content)
        
        for text, link in matches:
            # Ignorer les liens externes et les ancres seules
            if link.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            
            # Séparer le lien et l'ancre si présente
            if '#' in link:
                link_path, anchor = link.split('#', 1)
            else:
                link_path, anchor = link, ''
            
            # Ignorer les liens vides (ancres seulement)
            if not link_path:
                continue
                
            # Gérer les liens relatifs à la séance
            if link_path.startswith(('seance1/', 'seance2/', 'seance3/', 'seance4/')):
                target_path = os.path.normpath(os.path.join(docs_dir, link_path))
                if not os.path.exists(target_path):
                    file_broken_links.append((text, link, f"Fichier non trouvé: {link_path}"))
                continue
            
            # Gérer les liens relatifs au fichier actuel
            if not link_path.startswith('/'):
                target_path = os.path.normpath(os.path.join(file_dir, link_path))
            else:
                # Liens absolus par rapport à la racine docs
                target_path = os.path.normpath(os.path.join(docs_dir, link_path.lstrip('/')))
            
            if not os.path.exists(target_path):
                file_broken_links.append((text, link, f"Fichier non trouvé: {target_path}"))
        
        if file_broken_links:
            broken_links[file_path] = file_broken_links
    
    return broken_links

def main():
    docs_dir = 'docs'  # Ajustez si nécessaire
    md_files = get_all_md_files(docs_dir)
    
    broken_links = check_internal_md_links(md_files, docs_dir)
    
    if broken_links:
        print("## Liens internes cassés dans les fichiers Markdown\n")
        for file, links in broken_links.items():
            print(f"### {os.path.relpath(file, docs_dir)}\n")
            for text, link, error in links:
                print(f"- [❌] [{text}]({link}) - {error}")
            print("\n")
        return 1
    else:
        print("## Liens internes dans les fichiers Markdown\n")
        print("✅ Tous les liens internes sont valides\n")
        return 0

if __name__ == "__main__":
    sys.exit(main())
