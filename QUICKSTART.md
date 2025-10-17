# Quick Start Guide - Dynamic Publications

## ✅ What's Already Set Up

Your website now **automatically loads publications** from `publications.json` every time someone visits `astrophysics.html`.

## 🚀 Quick Update (3 Steps)

1. **Set your ADS token** (one time only):
   ```bash
   export ADS_API_TOKEN="your-ads-token-here"
   ```
   Get token from: https://ui.adsabs.harvard.edu/user/settings/token

2. **Run the update script:**
   ```bash
   ./update_publications.sh
   ```

3. **Done!** Your website now shows updated publications.

## 📁 Files Created

- ✅ `astrophysics.html` - Updated with dynamic loading JavaScript
- ✅ `publications.json` - Sample data (4 publications)
- ✅ `fetch_publications.py` - Python script to fetch from ADS
- ✅ `update_publications.sh` - One-command update script
- ✅ `PUBLICATIONS_README.md` - Full documentation

## 🧪 Test It Now

Visit: http://localhost:8000/astrophysics.html

Scroll to the bottom - you should see "All Publications" section loading your papers!

## 🔄 When to Update

Run `./update_publications.sh` whenever you:
- Publish a new paper
- Want to refresh citation counts
- Add papers to your ADS library

## 🤖 Automate It (Optional)

See `PUBLICATIONS_README.md` for:
- GitHub Actions (auto-update weekly)
- Cron job setup (auto-update locally)

## ❓ Troubleshooting

**Publications not showing?**
- Check browser console (F12) for errors
- Verify `publications.json` exists
- Make sure your local server is running

**Need to update token?**
```bash
export ADS_API_TOKEN="new-token"
./update_publications.sh
```

**Want to add specific papers manually?**
Edit `publications.json` directly - same format as existing entries.

---

**Ready to deploy?** Just push to GitHub:
```bash
git add .
git commit -m "Add dynamic publications system"
git push
```

Your GitHub Pages site will automatically show the updated publications! 🎉
