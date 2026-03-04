# Scout Setup Guide

## Step 1: Create Telegram Bot
1. Message @BotFather on Telegram
2. Send `/newbot`
3. Name: `ScoutIntelBot` (or similar)
4. Save the API token

## Step 2: Initialize OpenClaw Agent
```bash
mkdir -p ~/.openclaw/agents/scout
cd ~/.openclaw/agents/scout

# Copy this SOUL.md
cp /path/to/SOUL.md .

# Create AGENTS.md
echo "# Scout Agent Config
runtime: agent
model: nvidia-nim/moonshotai/kimi-k2.5
skills: web_search, browser, memory
" > AGENTS.md

# Start OpenClaw with this workspace
openclaw start --workspace ~/.openclaw/agents/scout
openclaw onboard
```

## Step 3: Connect to Coordination Repo
```bash
cd ~/.openclaw/agents/scout
git clone https://github.com/evan604/bot-coordination.git
cd bot-coordination
```

## Step 4: Daily Workflow
1. Morning: Research market
2. Write findings to `intel/MARKET-INTEL.md`
3. `git add . && git commit -m "Scout: $(date) intelligence"`
4. `git push origin master`

## Step 5: Coordination
- Check Telegram for commands from Crabby
- Automatic: Reads updates from GitHub
- Writes intel daily to shared repo

## First Run Test
Message your bot: "Run market sweep"
Expected: Research trending products, summarize, ask to commit