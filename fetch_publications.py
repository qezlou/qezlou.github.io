#!/usr/bin/env python3
"""
Script to fetch publications from NASA ADS library and generate publications.json

Requirements:
    pip install requests

Usage:
    1. Get an ADS API token from https://ui.adsabs.harvard.edu/user/settings/token
    2. Set it as environment variable: export ADS_API_TOKEN="your-token-here"
    3. Run: python3 fetch_publications.py

This will create/update publications.json with your latest publications.
"""

import os
import json
import requests
from datetime import datetime

# ADS API configuration
ADS_API_TOKEN = os.environ.get('ADS_API_TOKEN', '')
ADS_API_URL = 'https://api.adsabs.harvard.edu/v1'
LIBRARY_ID = 'MK-no7fnQfiXyzaHTA_azg'

def fetch_ads_publications():
    """Fetch publications from ADS library"""
    
    if not ADS_API_TOKEN:
        print("ERROR: ADS_API_TOKEN not set!")
        print("Get your token from: https://ui.adsabs.harvard.edu/user/settings/token")
        print("Then run: export ADS_API_TOKEN='your-token-here'")
        return None
    
    headers = {
        'Authorization': f'Bearer {ADS_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    # Step 1: Get bibcodes from public library
    # Use the search endpoint with library filter
    print(f"Fetching library: {LIBRARY_ID}...")
    
    try:
        # Query for all papers in the public library
        search_url = f'{ADS_API_URL}/search/query'
        params = {
            'q': f'docs(library/{LIBRARY_ID})',
            'fl': 'bibcode',
            'rows': 2000,  # Max papers to fetch
            'sort': 'date desc'
        }
        
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_data = response.json()
        
        bibcodes = [doc['bibcode'] for doc in search_data.get('response', {}).get('docs', [])]
        print(f"Found {len(bibcodes)} publications in library")
        
        if not bibcodes:
            print("No publications found in library")
            return []
        
        # Step 2: Get detailed publication information
        print("Fetching publication details...")
        
        params = {
            'q': f'docs(library/{LIBRARY_ID})',
            'fl': 'bibcode,title,author,year,pub,citation_count,pubdate',
            'rows': len(bibcodes),
            'sort': 'date desc'
        }
        
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_data = response.json()
        
        publications = []
        for doc in search_data.get('response', {}).get('docs', []):
            pub = {
                'bibcode': doc.get('bibcode', ''),
                'title': doc.get('title', [''])[0] if doc.get('title') else '',
                'authors': doc.get('author', []),
                'year': doc.get('year', 'N/A'),
                'journal': doc.get('pub', 'Preprint'),
                'citation_count': doc.get('citation_count', 0),
                'pubdate': doc.get('pubdate', '')
            }
            publications.append(pub)
        
        print(f"Successfully fetched {len(publications)} publications")
        return publications
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response: {e.response.text if hasattr(e, 'response') else 'No response'}")
        return None
    except Exception as e:
        print(f"Error fetching publications: {e}")
        return None

def save_publications_json(publications):
    """Save publications to JSON file"""
    
    if publications is None:
        print("No publications to save")
        return False
    
    output_data = {
        'last_updated': datetime.now().isoformat(),
        'count': len(publications),
        'publications': publications
    }
    
    output_file = 'publications.json'
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Successfully saved {len(publications)} publications to {output_file}")
        print(f"  Last updated: {output_data['last_updated']}")
        return True
    except Exception as e:
        print(f"Error saving JSON file: {e}")
        return False

def main():
    print("=" * 60)
    print("ADS Publication Fetcher")
    print("=" * 60)
    print()
    
    publications = fetch_ads_publications()
    
    if publications:
        success = save_publications_json(publications)
        if success:
            print("\nNext steps:")
            print("1. Commit publications.json to your repository")
            print("2. Deploy your site - the publications will load automatically")
            print("\nTo update publications later, just run this script again!")
    else:
        print("\nFailed to fetch publications.")
        print("Please check your ADS_API_TOKEN and try again.")

if __name__ == '__main__':
    main()
