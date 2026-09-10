# Easy Post Management System ✨

This portfolio now supports **two types of posts** with **images and posts living together**!

## 🎯 What's New?

### ✅ Images Live With Posts!
```
_posts/
  2026-05-20-my-awesome-post/
    index.markdown      ← Your post
    01.jpg             ← Images right here!
    02.jpg
    thumbnail.jpg
```

No more separate `images/` folder hunting! Everything in one place.

### ✅ Simple References
```markdown
![My photo](01.jpg)          ← Just the filename!
![Another](thumbnail.jpg)    ← No paths needed!
```

---

## 🎯 Post Types

### 1. **Gallery Posts** (Simple Image Tiles)
- Perfect for quick photo dumps
- Images shown directly in grid
- Click to view in lightbox
- No separate post page needed
- Visually distinct with "📸 Gallery" badge

### 2. **Article Posts** (Traditional Blog Posts)
- Full blog post with content
- Thumbnail in grid
- Click opens detailed post page
- Current format you're used to

---

## 🚀 Quick Start

### Create a Gallery Post

```bash
# Interactive mode
python3 new-post.py gallery

# Quick mode with all options
python3 new-post.py gallery -t "Beach Day" -d "Beautiful sunset at the beach" --tags photography travel

# With images from a folder
python3 new-post.py gallery -t "Beach Day" -d "Beautiful sunset" --tags photography -i ~/Pictures/beach-photos
```

### Create an Article Post

```bash
# Interactive mode
python3 new-post.py article

# Quick mode
python3 new-post.py article -t "Building a Game in Unity" -d "My journey creating an indie game" --tags gamedev programming
```

---

## 📸 Adding Images

### The New Way (Everything Together!)
1. Run the script - creates `_posts/2026-05-20-your-post/`
2. Drop images directly into that folder
3. Reference as just `![desc](image.jpg)`

### For Gallery Posts
```bash
# Copy images automatically from a folder
python3 new-post.py gallery -t "Beach Day" -i ~/Pictures/beach-pics

# Images copied to _posts/2026-05-20-beach-day/
# Front matter auto-generated
# Done!
```

### For Article Posts
1. Script creates the post folder
2. Add `thumbnail.jpg` (for preview)
3. Add other images as needed
4. Reference: `![Caption](photo.jpg)` - that's it!

---

## 🎨 How Gallery Posts Look

Gallery posts appear in the main feed with:
- ✅ Images visible directly (no clicking needed)
- ✅ Lighter background with border
- ✅ "📸 Gallery" badge in corner
- ✅ Smart grid layout (1-6 images shown)
- ✅ Click any image to view fullscreen
- ✅ "+N" indicator if more than 6 images

They're visually distinct from article posts so users know they're different!

---

## 📋 Front Matter Examples

### Gallery Post
```yaml
---
layout: post
title: Weekend Adventures
description: Photos from hiking and exploring
date: 2026-05-20 15:01:35 +0300
image: '01.jpg'              # ← Just filename!
tags: [photography, travel]
type: gallery
gallery:
  - 01.jpg                   # ← Relative to post folder
  - 02.jpg
  - 03.jpg
---
```

### Article Post
```yaml
---
layout: post
title: How I Built This Feature
description: Deep dive into the implementation
date: 2026-05-20 15:01:35 +0300
image: 'thumbnail.jpg'       # ← Just filename!
tags: [programming, tutorial]
type: article
---

Your content here...

![Screenshot](screenshot.jpg)   # ← Simple references!
```

---

## 🛠️ Script Options

```
python3 new-post.py <type> [options]

Types:
  gallery     Simple image gallery post
  article     Full blog article post

Options:
  -t, --title         Post title
  -d, --description   Short description
  --tags              Space-separated tags
  -i, --images-dir    Source directory for images (gallery only)
```

---

## 💡 Workflow Examples

### Scenario 1: Quick Instagram-style Post
```bash
# Take some photos on your phone
# AirDrop to ~/Downloads/today

python3 new-post.py gallery -t "Coffee Shop Vibes" -d "Morning coffee" --tags life -i ~/Downloads/today

# Done! Commit and push
git add .
git commit -m "Add coffee shop photos"
git push
```

### Scenario 2: Detailed Project Write-up
```bash
python3 new-post.py article -t "Building My VR Game" -d "Complete postmortem" --tags gamedev VR

# Opens _posts/2026-05-20-building-my-vr-game.markdown
# Write your content
# Add images to images/building-my-vr-game/
# Commit when ready
```

---

## 🎯 Industry Standard Approach

This implements a **mixed content feed** similar to:
- **Instagram**: Gallery posts = photo dumps, Articles = carousel posts
- **Tumblr**: Different post types with distinct styling
- **Pinterest**: Mixed content with visual weight differences

Users can instantly tell the difference:
- **Gallery = Quick visual content** (no commitment needed)
- **Article = In-depth content** (requires reading)

---

## 🔧 Technical Details

### Files Modified/Added
- ✅ `new-post.py` - Post generator (now creates page bundles)
- ✅ `_includes/article-content.html` - Handles both post types
- ✅ `_sass/3-modules/_gallery-posts.scss` - Gallery styling + lightbox
- ✅ `.github/workflows/jekyll.yml` - GitHub Actions workflow
- ✅ `Gemfile` - Added jekyll-postfiles plugin
- ✅ `_config.yml` - Added plugin configuration

### How It Works
1. Script creates `_posts/YYYY-MM-DD-slug/` folder structure
2. Images go directly in post folder
3. `jekyll-postfiles` plugin makes images available
4. Jekyll template checks `post.type`
5. Gallery posts render inline with lightbox
6. Article posts work as before
7. CSS provides visual distinction

### Structure Comparison

**Old Way:**
```
_posts/2026-05-20-my-post.markdown
images/my-post/01.jpg
images/my-post/02.jpg
```
Reference: `![]({{site.baseurl}}/images/my-post/01.jpg)` 😫

**New Way:**
```
_posts/2026-05-20-my-post/
  index.markdown
  01.jpg
  02.jpg
```
Reference: `![](01.jpg)` 😊

---

## 🚀 Deployment

### One-Time Setup (GitHub Actions)

To enable the new structure, you need to configure GitHub Pages to use Actions:

1. **Push these changes** first:
   ```bash
   bundle install  # Install jekyll-postfiles plugin
   git add .
   git commit -m "Add page bundles and GitHub Actions"
   git push
   ```

2. **Enable GitHub Actions** (one-time):
   - Go to your repo: `https://github.com/YOUR-USERNAME/YOUR-REPO/settings/pages`
   - Under "Build and deployment"
   - Change **Source** from "Deploy from a branch" to **"GitHub Actions"**
   - Save

3. **That's it!** Your site will now build with Actions and support the new structure.

### Regular Deployment (After Setup)

Just commit and push as usual:
```bash
git add .
git commit -m "Add new posts"
git push
```

GitHub Actions builds and deploys automatically in ~2 minutes.

---

## 📝 Tips

1. **Gallery posts** should have 1-10 images (6 shown in grid)
2. **Keep descriptions short** for galleries (one sentence)
3. **Use tags** to help users filter content
4. **Image naming**: 01.jpg, 02.jpg for easy ordering
5. **Optimize images** before adding (use ImageOptim or similar)

---

## Questions?

The script will guide you through creating posts interactively if you don't provide options. Just run:

```bash
python3 new-post.py gallery
# or
python3 new-post.py article
```

Happy posting! 🎉
