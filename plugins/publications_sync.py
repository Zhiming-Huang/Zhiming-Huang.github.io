"""
Publications Auto-Sync Plugin for Pelican

Uses Pelican's content processing signals to automatically sync publications
whenever publications.md is processed by Pelican.
"""

import os
import yaml
import json
from pathlib import Path
from pelican import signals

# Track the last modification time to avoid redundant syncs
_last_sync_mtime = {}

def sync_publications(pelican_settings):
    """Sync publications from MD to JSON"""
    try:
        # Paths
        content_path = pelican_settings.get('PATH', 'content')
        md_path = Path(content_path) / 'pages' / 'publications.md'
        
        theme_path = pelican_settings.get('THEME', 'themes/modern-academic')
        json_path = Path(theme_path) / 'static' / 'data' / 'publications.json'
        
        if not md_path.exists():
            return False
        
        # Check if file has been modified since last sync
        current_mtime = md_path.stat().st_mtime
        if _last_sync_mtime.get('publications') == current_mtime:
            return True  # Already synced this version
        
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find Publications section
        lines = content.split('\n')
        publications_start = -1
        
        for i, line in enumerate(lines):
            if line.strip() == 'Publications:':
                publications_start = i
                break
        
        if publications_start == -1:
            return False
        
        # Extract YAML from Publications: until we hit non-YAML content
        yaml_lines = []
        for i in range(publications_start, len(lines)):
            line = lines[i]
            # Stop when we hit a markdown header or non-indented content
            if line.strip().startswith('#') or (line.strip() and not line.startswith(' ') and not line.startswith('Publications:') and not line.strip() == ''):
                break
            yaml_lines.append(line)
        
        publications_yaml = '\n'.join(yaml_lines)
        metadata = yaml.safe_load(publications_yaml)
        publications = metadata.get('Publications', [])
        
        if not publications:
            return False
        
        # Ensure directory exists
        json_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write to JSON file
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(publications, f, indent=2, ensure_ascii=False)
        
        # Update last sync time
        _last_sync_mtime['publications'] = current_mtime
        
        print(f"✅ Synced {len(publications)} publications")
        return True
        
    except Exception as e:
        print(f"❌ Publications sync error: {e}")
        return False

def on_content_object_init(content_object):
    """Sync when publications.md is processed"""
    if hasattr(content_object, 'source_path'):
        source_path = str(content_object.source_path)
        if 'publications.md' in source_path:
            print(f"📝 Processing {Path(source_path).name}, syncing publications...")
            sync_publications(content_object.settings)

def on_pelican_init(pelican_obj):
    """Initial sync when Pelican starts"""
    print("📚 Publications sync plugin initialized")
    sync_publications(pelican_obj.settings)

def register():
    """Register the plugin with Pelican"""
    signals.initialized.connect(on_pelican_init)
    signals.content_object_init.connect(on_content_object_init)