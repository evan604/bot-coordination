# Pulse Setup Guide

## Step 1: Create X Account
1. Go to x.com/signup
2. Username: @ScoutPulse (or similar — check availability)
3. Profile: "Real-time AI & productivity intel"
4. Bio: "The signal. Product drops, AI insights, weekly newsletter"

## Step 2: Create Telegram Bot
1. @BotFather → `/newbot`
2. Name: `PulseSignalBot`
3. Save token

## Step 3: Initialize Agent
```bash
mkdir -p ~/.openclaw/agents/pulse
cd ~/.openclaw/agents/pulse

cp /path/to/SOUL.md .

echo "# Pulse Agent Config
runtime: agent
model: nvidia-nim/moonshotai/kimi-k2.5
skills: web_search
" > AGENTS.md

openclaw start --workspace ~/.openclaw/agents/pulse
openclaw onboard
```

## Step 4: Connect to Coordination
```bash
cd ~/.openclaw/agents/pulse
git clone https://github.com/evan604/bot-coordination.git
```

## Step 5: Daily Workflow
1. Read `intel/MARKET-INTEL.md` from Scout
2. Write 2-3 tweets to `marketing/X-DRAFTS.md`
3. Commit: `git add . && git commit -m "Pulse: X drafts $(date)"`
4. Push: `git push origin master`
5. Crabby reviews → schedules via Publer

## Approval Process
**IMPORTANT: Pulse cannot post directly**
- Writes drafts
- Crabby reviews and approves
- Publer posts at optimal times
- This prevents brand-damaging mistakes

## Content Templates (Built-in)
See `marketing/X-DRAFTS.md` for templates

## First Run
Message: "Draft today's tweets"
Expected: 3 tweet drafts based on Scout's intel, waiting approval