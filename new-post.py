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
    
    filepath = post_dir / f"{date_str}-{slug}.markdown"
    
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

def main():
    parser = argparse.ArgumentParser(description='Create new Jekyll posts easily')
    parser.add_argument('type', choices=['article'], 
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
    print("\n" + "=" * 60)
    print("🎉 Done! Edit your post and add images, then commit.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
