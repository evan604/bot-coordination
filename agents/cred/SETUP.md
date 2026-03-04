# Cred Setup Guide

## Step 1: Create LinkedIn Account
1. linkedin.com/signup (or use separate profile)
2. Name: "OpenClaw Insights" or similar professional name
3. Headline: "AI Productivity • Building autonomous agent teams"
4. Banner: Professional, minimal

## Step 2: Create Telegram Bot
1. @BotFather → `/newbot`
2. Name: `CredAuthorityBot`
3. Save token

## Step 3: Initialize Agent
```bash
mkdir -p ~/.openclaw/agents/cred
cd ~/.openclaw/agents/cred

cp /path/to/SOUL.md .

echo "# Cred Agent Config
runtime: agent
model: nvidia-nim/moonshotai/kimi-k2.5
skills: web_search
" > AGENTS.md

openclaw start --workspace ~/.openclaw/agents/cred
openclaw onboard
```

## Step 4: Connect to Coordination
```bash
cd ~/.openclaw/agents/cred
git clone https://github.com/evan604/bot-coordination.git
```

## Step 5: Daily Workflow
1. Read Scout's intel for professional angle
2. Write 1 LinkedIn post to `marketing/LINKEDIN-DRAFTS.md`
3. Format: Hook + Story + CTA
4. Commit: `git add . && git commit -m "Cred: LinkedIn $(date)"`
5. Push for Crabby approval

## Approval Process
- Cred writes drafts
- Crabby reviews (brand safety check)
- Publer schedules at 8-9 AM EST

## First Run
Message: "Draft today's LinkedIn post"
Expected: Professional post, story-based, soft product mention, ready for approval