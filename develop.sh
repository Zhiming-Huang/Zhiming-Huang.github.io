#!/bin/bash

# Development script for Pelican website

set -e

echo "🚀 Starting development environment..."

# Activate virtual environment
echo "📦 Activating virtual environment..."
source pelican-env/bin/activate

# Build the site
echo "🔨 Building site..."
pelican content

# Start development server with auto-reload
echo "🌍 Starting development server with auto-reload..."
echo "🔗 Visit: http://localhost:8000"
echo "📝 The site will automatically rebuild when you edit files"
echo "⏹️  Press Ctrl+C to stop"

pelican --listen --autoreload
