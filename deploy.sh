#!/bin/bash

# Deploy script for GitHub Pages
# This script builds the site and can be used for local testing

set -e  # Exit on any error

echo "🚀 Starting deployment process..."

# Activate virtual environment if it exists
if [ -d "pelican-env" ]; then
    echo "📦 Activating virtual environment..."
    source pelican-env/bin/activate
fi

# Clean output directory
echo "🧹 Cleaning output directory..."
rm -rf output

# Build the site using production configuration
echo "🏗️ Building site with production configuration..."
pelican content -s publishconf.py

# Check if build was successful
if [ -d "output" ] && [ "$(ls -A output)" ]; then
    echo "✅ Build completed successfully!"
    echo "📂 Generated files in output/ directory:"
    find output -type f -name "*.html" | head -10
    echo ""
    echo "🌐 To preview locally, you can serve the output directory:"
    echo "   cd output && python -m http.server 8080"
    echo ""
    echo "📤 To deploy to GitHub Pages, push your changes to the main/master branch"
else
    echo "❌ Build failed - output directory is empty or missing"
    exit 1
fi

echo "✨ Deployment preparation complete!"
