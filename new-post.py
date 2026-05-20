#!/usr/bin/env python3
"""
Simple Post Generator for Jekyll Portfolio
Creates posts with proper front matter and handles images automatically.
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
import shutil

# Configuration
POSTS_DIR = Path("_posts")
IMAGES_DIR = Path("images")
BASE_DIR = Path(__file__).parent

def slugify(text):
    """Convert text to URL-friendly slug"""
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text

def get_user_input(prompt, default=None):
    """Get input from user with optional default"""
    if default:
        response = input(f"{prompt} [{default}]: ").strip()
        return response if response else default
    return input(f"{prompt}: ").strip()

def create_article_post(args):
    """Create a traditional article post"""
    print("\n📝 Creating Article Post\n")
    
    title = args.title or get_user_input("Post title")
    description = args.description or get_user_input("Description")
    tags = args.tags or get_user_input("Tags (comma-separated)", "").split(',')
    tags = [tag.strip() for tag in tags if tag.strip()]
    
    # Generate filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    
    # Create post folder (page bundle)
    post_dir = BASE_DIR / POSTS_DIR / f"{date_str}-{slug}"
    post_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = post_dir / "index.markdown"
    
    # Front matter - images now relative to post folder
    front_matter = f"""---
layout: post
title: {title}
description: {description}
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0300
image: thumbnail.jpg
tags: [{', '.join(tags)}]
type: article
---

Your content here...

![Image description](image1.jpg)

## Section Title

More content...

"""
    
    # Write file
    filepath.write_text(front_matter)
    
    print(f"✅ Created: {filepath}")
    print(f"📁 Post folder: {post_dir}")
    print(f"\n💡 Add your images directly to: {post_dir}/")
    print(f"   - thumbnail.jpg (for post preview)")
    print(f"   - Reference as: ![desc](image.jpg)")
    
    return filepath

def create_gallery_post(args):
    """Create a simple gallery post with multiple images"""
    print("\n🖼️  Creating Gallery Post\n")
    
    title = args.title or get_user_input("Gallery title")
    description = args.description or get_user_input("Short description", "")
    
    # Generate filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    
    # Create post folder (page bundle)
    post_dir = BASE_DIR / POSTS_DIR / f"{date_str}-{slug}"
    post_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = post_dir / "index.markdown"
    
    # If source directory provided, copy images
    if args.images_dir:
        source_dir = Path(args.images_dir)
        if source_dir.exists():
            print(f"📸 Copying images from {source_dir}...")
            image_files = []
            for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.webp']:
                image_files.extend(source_dir.glob(ext))
                image_files.extend(source_dir.glob(ext.upper()))
            
            for i, img_file in enumerate(sorted(image_files), 1):
                dest = post_dir / f"{i:02d}{img_file.suffix}"
                shutil.copy2(img_file, dest)
                print(f"  ✓ Copied {img_file.name} -> {dest.name}")
    
    # Get list of images
    image_files = sorted([f for f in post_dir.iterdir() if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']])
    
    # Generate image paths (relative to post folder)
    gallery_images = [img.name for img in image_files]
    
    # Front matter
    tags_str = ', '.join(args.tags) if args.tags else ''
    front_matter = f"""---
layout: post
title: {title}
description: {description}
date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} +0300
image: '{gallery_images[0] if gallery_images else "01.jpg"}'
tags: [{tags_str}]
type: gallery
gallery:
{chr(10).join(f'  - {img}' for img in gallery_images) if gallery_images else '  - 01.jpg'}
---

{description}
"""
    
    # Write file
    filepath.write_text(front_matter)
    
    print(f"\n✅ Created: {filepath}")
    print(f"📁 Post folder: {post_dir}")
    if not gallery_images:
        print(f"\n💡 Add your images directly to: {post_dir}/")
        print(f"   Name them: 01.jpg, 02.jpg, 03.jpg, etc.")
    else:
        print(f"📸 Added {len(gallery_images)} images to gallery")
    
    return filepath

def main():
    parser = argparse.ArgumentParser(description='Create new Jekyll posts easily')
    parser.add_argument('type', choices=['article', 'gallery'], 
                       help='Type of post to create')
    parser.add_argument('-t', '--title', help='Post title')
    parser.add_argument('-d', '--description', help='Post description')
    parser.add_argument('-g', '--tags', nargs='+', help='Tags for the post')
    parser.add_argument('-i', '--images-dir', help='Source directory with images (for gallery posts)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("  JEKYLL POST GENERATOR")
    print("=" * 60)
    
    if args.type == 'article':
        filepath = create_article_post(args)
    elif args.type == 'gallery':
        filepath = create_gallery_post(args)
    
    print("\n" + "=" * 60)
    print("🎉 Done! Edit your post and add images, then commit.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
