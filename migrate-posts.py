#!/usr/bin/env python3
"""
Migrate existing Jekyll posts to page bundle structure
Moves posts and their images into co-located folders
"""

import os
import re
import shutil
from pathlib import Path

BASE_DIR = Path("/Users/nonode/Projects/pavelioso.github.io")
POSTS_DIR = BASE_DIR / "_posts"
IMAGES_DIR = BASE_DIR / "images"

def extract_image_folder(content):
    """Extract the image folder path from post content"""
    # Look for image paths like /images/fortnite/ or {{site.baseurl}}/images/ez/
    patterns = [
        r"['\"]?/images/([^/'\"]+)/",
        r"\{\{site\.baseurl\}\}/images/([^/'\"]+)/",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.group(1)
    return None

def update_image_references(content, image_folder):
    """Update image references to be relative to post folder"""
    if not image_folder:
        return content
    
    # Replace various image path formats
    replacements = [
        (rf"['\"]?/images/{image_folder}/", ""),
        (rf"\{{\{{site\.baseurl\}}\}}/images/{image_folder}/", ""),
        (rf"'/images/{image_folder}/", "'"),
        (rf'"/images/{image_folder}/', '"'),
    ]
    
    for old, new in replacements:
        content = re.sub(old, new, content)
    
    return content

def migrate_post(post_file):
    """Migrate a single post to page bundle structure"""
    if post_file.is_dir():
        print(f"⏭️  Skipping {post_file.name} (already a folder)")
        return
    
    if not post_file.suffix == '.markdown':
        print(f"⏭️  Skipping {post_file.name} (not a markdown file)")
        return
    
    # Skip hidden/trash files
    if post_file.name.startswith('.') or 'trash' in str(post_file):
        print(f"⏭️  Skipping {post_file.name} (hidden/trash)")
        return
    
    print(f"\n📄 Processing: {post_file.name}")
    
    # Read post content
    content = post_file.read_text(encoding='utf-8')
    
    # Extract image folder from content
    image_folder = extract_image_folder(content)
    
    if image_folder:
        print(f"   Found images folder: {image_folder}")
    else:
        print(f"   No images folder detected")
    
    # Create new post folder (remove .markdown extension)
    post_slug = post_file.stem
    new_post_dir = POSTS_DIR / post_slug
    
    if new_post_dir.exists():
        print(f"   ⚠️  Folder already exists: {new_post_dir}")
        return
    
    new_post_dir.mkdir(parents=True, exist_ok=True)
    print(f"   ✅ Created folder: {post_slug}/")
    
    # Update image references in content
    if image_folder:
        updated_content = update_image_references(content, image_folder)
    else:
        updated_content = content
    
    # Write index.markdown
    index_file = new_post_dir / "index.markdown"
    index_file.write_text(updated_content, encoding='utf-8')
    print(f"   ✅ Created: index.markdown")
    
    # Move images if folder exists
    if image_folder:
        source_images = IMAGES_DIR / image_folder
        if source_images.exists() and source_images.is_dir():
            image_files = list(source_images.glob('*'))
            image_files = [f for f in image_files if f.is_file() and not f.name.startswith('.')]
            
            if image_files:
                print(f"   📸 Moving {len(image_files)} images...")
                for img_file in image_files:
                    dest = new_post_dir / img_file.name
                    shutil.copy2(img_file, dest)
                    print(f"      ✓ {img_file.name}")
            else:
                print(f"   ℹ️  No images found in {source_images}")
        else:
            print(f"   ⚠️  Image folder not found: {source_images}")
    
    # Remove original markdown file
    post_file.unlink()
    print(f"   🗑️  Removed original: {post_file.name}")
    
    print(f"   ✅ Migration complete!")

def main():
    print("=" * 70)
    print("  JEKYLL PAGE BUNDLE MIGRATION")
    print("=" * 70)
    print(f"\nPosts directory: {POSTS_DIR}")
    print(f"Images directory: {IMAGES_DIR}")
    print("\n" + "=" * 70)
    
    # Get all markdown files
    post_files = sorted(POSTS_DIR.glob('*.markdown'))
    
    if not post_files:
        print("\n✅ No posts to migrate!")
        return
    
    print(f"\nFound {len(post_files)} posts to migrate\n")
    
    # Migrate each post
    migrated = 0
    skipped = 0
    
    for post_file in post_files:
        try:
            migrate_post(post_file)
            migrated += 1
        except Exception as e:
            print(f"   ❌ Error: {e}")
            skipped += 1
    
    print("\n" + "=" * 70)
    print(f"✅ Migration Complete!")
    print(f"   Migrated: {migrated} posts")
    if skipped > 0:
        print(f"   Skipped: {skipped} posts")
    print("=" * 70)
    
    print("\n📝 Next steps:")
    print("   1. Review migrated posts")
    print("   2. Test locally: bundle exec jekyll serve")
    print("   3. Commit: git add . && git commit -m 'Migrate to page bundles'")
    print("   4. Push: git push")
    print("\n")

if __name__ == "__main__":
    main()
