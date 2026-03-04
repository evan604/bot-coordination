# Dispatch Setup Guide

## Step 1: AgentMail Setup
**Account:** dispatch@agentmail.to
**API Key:** (use crabby@agentmail.to key: `am_us_af52edab0c9371fcf23b82c257753e6c79697811ae174f9d02f019b3afe2236`)

## Step 2: Create Telegram Bot
1. @BotFather → `/newbot`
2. Name: `DispatchBriefBot`
3. Save token

## Step 3: Initialize Agent
```bash
mkdir -p ~/.openclaw/agents/dispatch
cd ~/.openclaw/agents/dispatch

cp /path/to/SOUL.md .

echo "# Dispatch Agent Config
runtime: agent
model: nvidia-nim/moonshotai/kimi-k2.5
skills: agentmail, web_search
email: dispatch@agentmail.to
" > AGENTS.md

openclaw start --workspace ~/.openclaw/agents/dispatch
openclaw onboard
```

## Step 4: AgentMail Integration
```python
# Test script
curl -H "Authorization: Bearer $AGENTMAIL_KEY" \
  https://api.agentmail.to/v1/inbox/823d9f52-585a-4017-9fa3-0c45c4290fce
```

## Step 5: Subscribe Form
Create signup form using AgentMail webhooks or link to:
- Landing page with email capture
- Gumroad checkout (collects email)

## Step 6: Weekly Workflow (Sunday)
1. **Saturday:** Gather content from Scout, Pulse, Cred, Lens
2. **Sunday 8 AM:** Draft newsletter
3. **Sunday 8:30 AM:** Crabby reviews
4. **Sunday 9 AM:** Send via AgentMail

## Email Template
```
Subject: OpenClaw Weekly — [number] things I learned

[Personal opening — 2 sentences]

---

[Main content — 300-500 words]

---

[Resources / links]

---

P.S. [Soft product mention with link]

Unsubscribe: [link]
```

## First Run
Message: "Test email to [your email]"
Expected: Test newsletter delivered via AgentMail

## Coordination
- Reads from GitHub coordination repo
- Gathers highlights from other agents
- Crabby approves final draft
- Sends via AgentMail API
- Tracks opens/clicks in `marketing/ANALYTICS.md`