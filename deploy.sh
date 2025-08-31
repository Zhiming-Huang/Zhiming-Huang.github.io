#!/bin/bash

# Deploy script for Pelican website

set -e

echo "🚀 Starting deployment process..."

# Activate virtual environment
echo "📦 Activating virtual environment..."
source pelican-env/bin/activate

# Build the site with production settings
echo "🔨 Building site with production settings..."
pelican content -s publishconf.py

# Check if output directory exists
if [ ! -d "output" ]; then
    echo "❌ Error: Output directory not found!"
    exit 1
fi

echo "✅ Site built successfully!"
echo "📁 Generated files are in the 'output' directory"

# Option to start local server for testing
read -p "🌐 Start local server to preview? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🌍 Starting local server at http://localhost:8000"
    echo "Press Ctrl+C to stop"
    cd output && python -m http.server 8000
fi

echo "🎉 Deployment process completed!"
echo "📝 Next steps:"
echo "   1. Push changes to GitHub: git push origin main"
echo "   2. GitHub Actions will automatically deploy to GitHub Pages"
echo "   3. Visit your site at: https://zhiminghuang.me"
