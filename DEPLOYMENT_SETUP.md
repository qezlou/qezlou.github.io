# GitHub Pages Deployment Setup

## Problem
Your commits are not automatically deploying to GitHub Pages because the repository is still configured to use the old deployment method instead of GitHub Actions.

## Solution: Configure GitHub Pages to Use GitHub Actions

### Step 1: Go to Repository Settings
1. Visit: **https://github.com/qezlou/qezlou.github.io/settings/pages**
2. Or navigate: Repository → Settings → Pages (in left sidebar)

### Step 2: Change Build and Deployment Source
In the "Build and deployment" section:

1. **Source**: Click the dropdown (currently probably set to "Deploy from a branch")
2. **Select**: `GitHub Actions`
3. The page will update automatically - no need to click Save

### Step 3: Verify Workflow Permissions (if needed)
If the workflow still doesn't run after Step 2:

1. Go to: **https://github.com/qezlou/qezlou.github.io/settings/actions**
2. Under "Workflow permissions":
   - Select: **"Read and write permissions"**
   - Check: **"Allow GitHub Actions to create and approve pull requests"**
3. Click **Save**

### Step 4: Verify Deployment
After changing the settings:

1. Go to: **https://github.com/qezlou/qezlou.github.io/actions**
2. You should see the "Deploy to GitHub Pages" workflow running
3. Wait for it to complete (usually 1-2 minutes)
4. Your site will be live at: **https://qezlou.github.io/**

## How It Works After Setup

Once configured, every time you push to the `master` branch:
1. GitHub Actions automatically triggers
2. The workflow builds and deploys your site
3. Changes go live in 1-2 minutes

## Current Status

✅ Workflow file created: `.github/workflows/pages.yml`
✅ Latest commits pushed to GitHub
⏳ **PENDING**: GitHub Pages needs to be configured to use GitHub Actions (see steps above)

## Testing

After setup, test by making any small change:
```bash
git commit --allow-empty -m "Test deployment"
git push origin master
```

Then check: https://github.com/qezlou/qezlou.github.io/actions

You should see a new workflow run appear immediately!

## Troubleshooting

### Issue: Workflow doesn't appear in Actions tab
- **Solution**: Make sure you selected "GitHub Actions" as the source in Pages settings

### Issue: Workflow fails with permissions error
- **Solution**: Enable "Read and write permissions" in Actions settings (Step 3 above)

### Issue: Site shows old content after deployment
- **Solution**: Hard refresh your browser (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)
- Or wait 5-10 minutes for CDN cache to clear
- Or open in incognito/private mode

---

**Quick Link**: https://github.com/qezlou/qezlou.github.io/settings/pages
