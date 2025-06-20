import yaml
import os
import sys

def load_mkdocs_config():
    with open('mkdocs.yml', 'r') as f:
        return yaml.safe_load(f)

def check_nav_item(item, docs_dir, prefix=''):
    issues = []
    
    if isinstance(item, dict):
        for title, link in item.items():
            if isinstance(link, str) and not link.startswith(('http://', 'https://')):
                file_path = os.path.join(docs_dir, link)
                if not os.path.exists(file_path):
                    issues.append(f"{prefix}{title}: {link} (fichier non trouvé)")
            elif isinstance(link, list):
                for sub_item in link:
                    sub_issues = check_nav_item(sub_item, docs_dir, prefix=f"{title} > ")
                    issues.extend(sub_issues)
    elif isinstance(item, list):
        for sub_item in item:
            sub_issues = check_nav_item(sub_item, docs_dir, prefix)
            issues.extend(sub_issues)
            
    return issues

def main():
    config = load_mkdocs_config()
    docs_dir = config.get('docs_dir', 'docs')
    nav = config.get('nav', [])
    
    all_issues = []
    for item in nav:
        issues = check_nav_item(item, docs_dir)
        all_issues.extend(issues)
    
    if all_issues:
        print("## Problèmes de navigation MkDocs\n")
        for issue in all_issues:
            print(f"- [❌] {issue}")
        print("\n")
        return 1
    else:
        print("## Navigation MkDocs\n")
        print("✅ Tous les liens de navigation sont valides\n")
        return 0

if __name__ == "__main__":
    sys.exit(main())
