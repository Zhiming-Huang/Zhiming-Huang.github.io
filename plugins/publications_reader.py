"""
Publications Reader Plugin for Pelican

This plugin reads publications.md and makes the structured data available 
to templates, allowing Pelican's native file monitoring to work seamlessly.
"""

import yaml
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open

class PublicationsReader(BaseReader):
    """Custom reader for publications.md that parses YAML data"""
    
    enabled = True
    file_extensions = ['md']
    
    def read(self, filename):
        """Read and parse publications.md file"""
        with pelican_open(filename) as fp:
            text = fp.read()
        
        # Split content into metadata and body
        lines = text.splitlines()
        
        # Find the Publications section
        publications_start = -1
        for i, line in enumerate(lines):
            if line.strip() == 'Publications:':
                publications_start = i
                break
        
        if publications_start == -1:
            # Fallback: treat as regular markdown
            return super().read(filename)
        
        # Extract metadata (before Publications:)
        metadata_lines = lines[:publications_start]
        metadata_text = '\n'.join(metadata_lines)
        
        # Extract YAML from Publications: section
        yaml_lines = []
        for i in range(publications_start, len(lines)):
            line = lines[i]
            # Stop when we hit a markdown header or non-YAML content
            if line.strip().startswith('#') or (line.strip() and not line.startswith(' ') and not line.startswith('Publications:') and not line.strip() == ''):
                break
            yaml_lines.append(line)
        
        publications_yaml = '\n'.join(yaml_lines)
        
        try:
            # Parse the Publications YAML
            publications_data = yaml.safe_load(publications_yaml)
            publications = publications_data.get('Publications', [])
        except Exception as e:
            print(f"⚠️  Error parsing publications YAML: {e}")
            publications = []
        
        # Parse regular metadata
        metadata = {}
        for line in metadata_lines:
            if ':' in line and not line.startswith(' '):
                key, value = line.split(':', 1)
                metadata[key.strip().lower()] = value.strip()
        
        # Add publications data to metadata
        metadata['publications_data'] = publications
        
        # Content is everything after YAML
        content_start = len(yaml_lines) + publications_start
        content_lines = lines[content_start:] if content_start < len(lines) else []
        content = '\n'.join(content_lines)
        
        return content, metadata

def add_reader(readers):
    """Add the publications reader to Pelican"""
    # Store the original markdown reader
    original_md_reader = readers.reader_classes.get('md')
    
    class ConditionalPublicationsReader(PublicationsReader):
        def read(self, filename):
            # Only use custom reader for publications.md
            if 'publications.md' in str(filename):
                return super().read(filename)
            else:
                # Use original reader for other files
                if original_md_reader:
                    return original_md_reader(readers.settings).read(filename)
                else:
                    return super().read(filename)
    
    # Replace the markdown reader
    readers.reader_classes['md'] = ConditionalPublicationsReader

def register():
    """Register the plugin"""
    signals.readers_init.connect(add_reader)
