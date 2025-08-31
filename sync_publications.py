#!/usr/bin/env python3
"""
Script to sync publications from publications.md to publications.json
This ensures the website always reflects the current state of publications.md
"""

import yaml
import json
import os

def sync_publications():
    """Read publications.md and update publications.json"""
    
    # Paths
    md_path = 'content/pages/publications.md'
    json_path = 'themes/modern-academic/static/data/publications.json'
    
    # Check if markdown file exists
    if not os.path.exists(md_path):
        print(f"Error: {md_path} not found")
        return False
    
    try:
        # Read the markdown file
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where the Publications section starts
        lines = content.split('\n')
        publications_start = -1
        
        for i, line in enumerate(lines):
            if line.strip() == 'Publications:':
                publications_start = i
                break
        
        if publications_start == -1:
            print("Error: No 'Publications:' section found")
            return False
        
        # Extract YAML from Publications: until we hit non-YAML content
        yaml_lines = []
        for i in range(publications_start, len(lines)):
            line = lines[i]
            # Stop when we hit a markdown header or non-indented content that's not part of YAML
            if line.strip().startswith('#') or (line.strip() and not line.startswith(' ') and not line.startswith('Publications:') and not line.strip() == ''):
                break
            yaml_lines.append(line)
        
        publications_yaml = '\n'.join(yaml_lines)
        
        # Parse just the publications YAML
        metadata = yaml.safe_load(publications_yaml)
        
        # Extract publications
        publications = metadata.get('Publications', [])
        
        if not publications:
            print("Warning: No publications found in metadata")
            print("Available keys:", list(metadata.keys()) if metadata else "None")
            return False
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        
        # Write to JSON file
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(publications, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Successfully synced {len(publications)} publications from {md_path} to {json_path}")
        return True
            
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    success = sync_publications()
    exit(0 if success else 1)
