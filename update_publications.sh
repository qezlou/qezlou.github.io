#!/bin/bash
# Quick script to update publications and deploy

echo "======================================"
echo "Publication Update & Deploy Script"
echo "======================================"
echo

# Check if ADS_API_TOKEN is set
if [ -z "$ADS_API_TOKEN" ]; then
    echo "ERROR: ADS_API_TOKEN not set!"
    echo 
    echo "Please set your ADS API token:"
    echo "  export ADS_API_TOKEN='your-token-here'"
    echo
    echo "Get your token from:"
    echo "  https://ui.adsabs.harvard.edu/user/settings/token"
    exit 1
fi

# Fetch publications
echo "Fetching publications from ADS..."
python3 fetch_publications.py

# Check if fetch was successful
if [ $? -ne 0 ]; then
    echo
    echo "ERROR: Failed to fetch publications"
    exit 1
fi

echo
echo "Publications updated successfully!"
echo

# Ask user if they want to commit and push
read -p "Commit and push to GitHub? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git add publications.json
    git commit -m "Update publications - $(date '+%Y-%m-%d')"
    git push
    echo
    echo "✓ Changes pushed to GitHub"
    echo "✓ Your website will update automatically"
else
    echo
    echo "Changes saved locally but not committed"
    echo "Run 'git add publications.json && git commit && git push' when ready"
fi

echo
echo "Done!"
