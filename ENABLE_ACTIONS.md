# Enable GitHub Actions - Quick Fix

## The Problem
You're seeing: **"GitHub Actions is disabled for this repo"**

This means Actions are turned off at the repository level, so the deployment workflow cannot run.

## Solution: Enable GitHub Actions

### Step 1: Enable Actions
1. Go to: **https://github.com/qezlou/qezlou.github.io/settings/actions**
2. Under **"Actions permissions"**, select:
   - ✅ **"Allow all actions and reusable workflows"**
   - Or at minimum: **"Allow actions created by GitHub"**
3. Click **Save**

### Step 2: Configure GitHub Pages Source
1. Go to: **https://github.com/qezlou/qezlou.github.io/settings/pages**
2. Under **"Build and deployment"**:
   - **Source**: Select **"GitHub Actions"** from the dropdown
3. The setting will auto-save

### Step 3: Verify It Works
1. Go to: **https://github.com/qezlou/qezlou.github.io/actions**
2. You should see "Deploy to GitHub Pages" workflow running
3. Wait 1-2 minutes for it to complete
4. Your site will be updated at: **https://qezlou.github.io/**

## Quick Links
- Enable Actions: https://github.com/qezlou/qezlou.github.io/settings/actions
- Configure Pages: https://github.com/qezlou/qezlou.github.io/settings/pages
- View Workflows: https://github.com/qezlou/qezlou.github.io/actions

---

## After Setup
Every commit to `master` will automatically deploy your site! 🚀
