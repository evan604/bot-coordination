#!/usr/bin/env python3
"""Publer Auto-Scheduler for Marketing Content

Reads approved content from marketing/ directory
and schedules via Publer API.

Run: python3 PUBLER-AUTO.py
"""

import requests
import json
import re
from datetime import datetime, timedelta

PUBLER_API = "https://app.publer.com/api/v1"
API_TOKEN = "d71526169b3d69139beca4c5037ccbc46575065128e1dbf0"
WORKSPACE = "69a5c09673e957e8eeed2805"

HEADERS = {
    "Authorization": f"Bearer-API {API_TOKEN}",
    "Publer-Workspace-Id": WORKSPACE,
    "Content-Type": "application/json"
}

ACCOUNTS = {
    "twitter": "<twitter_account_id>",
    "linkedin": "<linkedin_account_id>",
    "instagram": "<instagram_account_id>"
}

def load_content(filepath):
    """Load approved content from marketing/"""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

def extract_posts(content):
    """Extract posts marked for scheduling"""
    posts = []
    # Format: ## 2026-03-04\n- [ ] Platform: Content...
    pattern = r'## (\d{4}-\d{2}-\d{2})\n(?:.*\n)*?- \[ \] ([^:]+): (.+?)(?=\n-|\n##|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    for date_str, platform, text in matches:
        posts.append({
            'date': date_str,
            'platform': platform.strip().lower(),
            'text': text.strip()
        })
    return posts

def schedule_post(text, platform, scheduled_at):
    """Schedule via Publer API"""
    account_id = ACCOUNTS.get(platform)
    if not account_id:
        print(f"❌ Unknown platform: {platform}")
        return None
    
    payload = {
        "bulk": {
            "posts": [{
                "content": text,
                "accounts": [account_id],
                "scheduled_at": scheduled_at
            }]
        }
    }
    
    try:
        resp = requests.post(
            f"{PUBLER_API}/posts",
            headers=HEADERS,
            json=payload,
            timeout=30
        )
        if resp.status_code in [200, 201, 202]:
            data = resp.json()
            print(f"✅ Scheduled for {platform}: {data.get('job_id')}")
            return data.get('job_id')
        else:
            print(f"❌ Error {resp.status_code}: {resp.text[:200]}")
            return None
    except Exception as e:
        print(f"❌ Exception: {e}")
        return None

def main():
    """Main scheduling loop"""
    print("Publer Auto-Scheduler")
    print("=" * 40)
    
    # Load approved content
    x_content = load_content("marketing/X-DRAFTS.md")
    li_content = load_content("marketing/LINKEDIN-DRAFTS.md")
    ig_content = load_content("marketing/INSTAGRAM-DRAFTS.md")
    
    all_posts = []
    
    for content, platform in [(x_content, "twitter"), 
                                (li_content, "linkedin"), 
                                (ig_content, "instagram")]:
        if content:
            posts = extract_posts(content)
            for post in posts:
                post['platform'] = platform
                all_posts.append(post)
    
    if not all_posts:
        print("No posts to schedule")
        return
    
    # Schedule for next week
    for i, post in enumerate(all_posts[:10]):  # Max 10 per run
        # Space posts 3 hours apart
        schedule_time = datetime.now() + timedelta(days=1, hours=i*3)
        iso_time = schedule_time.strftime("%Y-%m-%dT%H:%M:%S-05:00")
        
        schedule_post(post['text'], post['platform'], iso_time)
    
    print(f"\n✅ Scheduled {min(10, len(all_posts))} posts")

if __name__ == "__main__":
    main()