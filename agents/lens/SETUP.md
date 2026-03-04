# Lens Setup Guide

## Step 1: Create Instagram Account
1. instagram.com/signup
2. Username: @openclawlens (check availability)
3. Name: "OpenClaw | AI Agent Teams"
4. Bio: "Building autonomous agent teams. Visual guide to OpenClaw"

## Step 2: Create Telegram Bot
1. @BotFather → `/newbot`
2. Name: `LensFrameBot`
3. Save token

## Step 3: Initialize Agent
```bash
mkdir -p ~/.openclaw/agents/lens
cd ~/.openclaw/agents/lens

cp /path/to/SOUL.md .

echo "# Lens Agent Config
runtime: agent
model: nvidia-nim/moonshotai/kimi-k2.5
skills: web_search, browser
" > AGENTS.md

openclaw start --workspace ~/.openclaw/agents/lens
openclaw onboard
```

## Step 4: Design Tools
**Required:**
- Canva Pro (Evan's account)
- Figma (free tier)
- Phone camera for BTS content

**Design System:**
- Colors: [TBD — minimal, modern]
- Fonts: [TBD — clean sans-serif]
- Templates: [TBD — create reusable]

## Step 5: Content Creation
```bash
# Daily workflow
cd ~/.openclaw/agents/lens/bot-coordination

# Read Pulse/Cred for content ideas
cat marketing/X-DRAFTS.md
cat marketing/LINKEDIN-DRAFTS.md

# Create visual assets
# Upload to: marketing/INSTAGRAM-ASSETS/
# Name: YYYY-MM-DD-content-type.png

# Write caption
# Save to: marketing/INSTAGRAM-DRAFTS.md
```

## Step 6: Commit and Push
```bash
git add marketing/INSTAGRAM-ASSETS/
git add marketing/INSTAGRAM-DRAFTS.md
git commit -m "Lens: Visual assets $(date)"
git push origin master
```

## Approval Process
- Lens creates assets
- Crabby reviews for brand consistency
- Publer schedules (1x/day, 12 PM or 6 PM EST)

## Content Types (Daily Rotation)
- Monday: Quote card (from Pulse/Cred)
- Tuesday: Carousel (tips/tutorial)
- Wednesday: Behind-the-scenes
- Thursday: Product mockup
- Friday: Quote card
- Saturday: BTS/Reel
- Sunday: Carousel

## First Run
Message: "Create today's Instagram post"
Expected: Quote card + caption, saved to assets/, ready for approval

## Tools
- Canva: `open -a "Canva"`
- Figma: Browser automation
- Google Images: For inspiration (not copying)

**Remember: Visuals should be shareable.**