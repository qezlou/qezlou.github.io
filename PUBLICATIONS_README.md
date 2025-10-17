# Dynamic Publications System

This system automatically loads your publications from a JSON file that can be updated via the ADS API.

## How It Works

1. **JavaScript on the webpage** (`astrophysics.html`) reads `publications.json`
2. **Python script** (`fetch_publications.py`) fetches fresh data from ADS API
3. Publications are displayed automatically when the page loads

## Setup Instructions

### First Time Setup

1. **Get your ADS API token:**
   - Visit: https://ui.adsabs.harvard.edu/user/settings/token
   - Create a token (it's free!)
   - Copy your token

2. **Install Python dependencies:**
   ```bash
   pip install requests
   ```

3. **Set your API token:**
   ```bash
   export ADS_API_TOKEN="your-token-here"
   ```

4. **Run the fetch script:**
   ```bash
   cd /Users/mq3595/Documents/qezlou.github.io
   python3 fetch_publications.py
   ```

5. **Commit and deploy:**
   ```bash
   git add publications.json
   git commit -m "Update publications"
   git push
   ```

## Updating Publications

Whenever you want to refresh your publication list:

```bash
export ADS_API_TOKEN="your-token-here"
python3 fetch_publications.py
git add publications.json
git commit -m "Update publications"
git push
```

## Automation Options

### Option 1: GitHub Actions (Recommended)

Create `.github/workflows/update-publications.yml`:

```yaml
name: Update Publications

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:  # Manual trigger

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      
      - name: Install dependencies
        run: pip install requests
      
      - name: Fetch publications
        env:
          ADS_API_TOKEN: ${{ secrets.ADS_API_TOKEN }}
        run: python3 fetch_publications.py
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add publications.json
          git diff --quiet && git diff --staged --quiet || git commit -m "Auto-update publications"
          git push
```

Then add your `ADS_API_TOKEN` as a GitHub secret:
- Go to your repo → Settings → Secrets → New repository secret
- Name: `ADS_API_TOKEN`
- Value: Your ADS token

### Option 2: Local Cron Job

Add to your crontab (`crontab -e`):

```bash
0 0 * * 0 cd /Users/mq3595/Documents/qezlou.github.io && /usr/local/bin/python3 fetch_publications.py && git add publications.json && git commit -m "Auto-update publications" && git push
```

## Files

- `astrophysics.html` - Your page with embedded JavaScript to load publications
- `publications.json` - JSON file with publication data (auto-generated)
- `fetch_publications.py` - Python script to fetch from ADS
- `PUBLICATIONS_README.md` - This file

## Troubleshooting

**"ADS_API_TOKEN not set" error:**
- Make sure you exported the token: `export ADS_API_TOKEN="your-token"`
- Check it's set: `echo $ADS_API_TOKEN`

**"No publications found" error:**
- Verify your library ID is correct
- Check the library is public
- Ensure your token has the right permissions

**Publications not showing on website:**
- Check browser console for errors (F12)
- Verify `publications.json` exists and is valid JSON
- Make sure you deployed the updated file

## Manual Fallback

If the automated system fails, the page will show a link to view publications directly on ADS. Users can always access your full publication list at:

https://ui.adsabs.harvard.edu/public-libraries/MK-no7fnQfiXyzaHTA_azg
