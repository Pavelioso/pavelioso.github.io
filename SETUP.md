# 🚀 Setup Instructions - Page Bundles

Your site now supports **co-located posts and images**! Here's how to enable it:

## What Changed?

✅ **New structure:** Posts and images live together  
✅ **Simpler references:** `![](image.jpg)` instead of long paths  
✅ **GitHub Actions:** Custom Jekyll build with plugins  
✅ **Still free:** GitHub Pages hosting  

---

## Setup Steps (5 minutes)

### 1. Install Dependencies

```bash
bundle install
```

This installs the `jekyll-postfiles` plugin that makes co-located images work.

### 2. Test Locally (Optional)

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` and verify everything works.

### 3. Commit and Push

```bash
git add .
git commit -m "Enable page bundles with GitHub Actions"
git push
```

### 4. Enable GitHub Actions (One-Time)

1. Go to your repository settings:
   ```
   https://github.com/YOUR-USERNAME/pavelioso.github.io/settings/pages
   ```

2. Under **"Build and deployment"** section:
   - Change **Source** from "Deploy from a branch" 
   - To **"GitHub Actions"** ⚡

3. Click **Save**

4. That's it! The Actions workflow (`.github/workflows/jekyll.yml`) will run automatically.

---

## Verify It's Working

1. After pushing, go to the **Actions** tab in your repo
2. You should see a workflow running
3. Wait ~2 minutes for it to complete
4. Your site will be live with the new build system!

---

## Now You Can:

### Create New Posts
```bash
# Gallery with images
python3 new-post.py gallery -t "My Photos" -i ~/Pictures/photos

# Article post  
python3 new-post.py article -t "My Story"
```

### Everything Lives Together
```
_posts/
  2026-05-20-my-photos/
    index.markdown
    01.jpg    ← Drop images here!
    02.jpg
    03.jpg
```

### Simple References
```markdown
![Caption](01.jpg)    ← Just the filename!
```

---

## Troubleshooting

### If Actions Fail:
1. Check the Actions tab for error messages
2. Verify `bundle install` works locally
3. Make sure you selected "GitHub Actions" as the source

### If Images Don't Show:
1. Verify images are in the same folder as `index.markdown`
2. Check front matter has correct image filenames
3. Make sure `jekyll-postfiles` is in plugins list in `_config.yml`

---

## Migration Guide (Optional)

Want to migrate old posts to the new structure?

### Old Structure:
```
_posts/2023-01-01-my-post.markdown
images/my-post/photo.jpg
```

### New Structure:
```bash
# Create folder
mkdir -p _posts/2023-01-01-my-post

# Move post
mv _posts/2023-01-01-my-post.markdown _posts/2023-01-01-my-post/index.markdown

# Move images
mv images/my-post/* _posts/2023-01-01-my-post/

# Update front matter and references
# Change: image: '/images/my-post/photo.jpg'
# To:     image: 'photo.jpg'
```

---

## Questions?

Read [POST-MANAGEMENT.md](POST-MANAGEMENT.md) for complete documentation!

🎉 **Happy posting!**
