# Marketing Bot Army — Master Deployment Guide

## The Crew

| Agent | Nickname | Job | Platform | Account Needed |
|-------|----------|-----|----------|----------------|
| **Scout** | "The Radar" | Market intel | Research | Telegram: @ScoutIntelBot |
| **Pulse** | "The Signal" | X/Twitter | Social | X: @ScoutPulse / Telegram: @PulseSignalBot |
| **Cred** | "The Authority" | LinkedIn | Professional | LinkedIn: OpenClaw Insights / Telegram: @CredAuthorityBot |
| **Dispatch** | "The Brief" | Newsletter | Email | AgentMail: dispatch@agentmail.to / Telegram: @DispatchBriefBot |
| **Lens** | "The Frame" | Instagram | Visual | IG: @openclawlens / Telegram: @LensFrameBot |

## Domain Strategy

**Primary domains:**
- `evanborenstein.com` — Personal brand
- `evanborenstein.com/guide` → OpenClaw Guide landing page
- `evanborenstein.com/newsletter` → Newsletter signup

**Products:**
- Gumroad: `gum.co/evan/openclaw-guide` (pending setup)

## Infrastructure

**Mac Mini M4** (Primary home for new agents):
- OpenClaw gateway always running
- 5 agent subdirectories
- Syncs to GitHub `bot-coordination` repo

**AWS (Crabby)** — Coordination:
- Approves content
- Runs Publer automation
- Tracks analytics

## Step-by-Step Deployment

### Phase 1: Account Creation (30 min)
1. **Scout:** @BotFather → API token
2. **Pulse:** x.com/signup → @ScoutPulse
3. **Cred:** linkedin.com/signup → "OpenClaw Insights"
4. **Dispatch:** AgentMail account (use crabby key)
5. **Lens:** instagram.com/signup → @openclawlens

### Phase 2: Mac Mini Setup (20 min)
```bash
# On Mac Mini
for agent in scout pulse cred dispatch lens; do
    mkdir -p ~/.openclaw/agents/$agent
    git clone https://github.com/evan604/bot-coordination.git ~/.openclaw/agents/$agent/bot-coordination
done
```

### Phase 3: Configure Each Agent (15 min each)
Per-agent setup (see SETUP.md in each agents/ directory):

1. Copy SOUL.md to agent workspace
2. Create AGENTS.md config
3. `openclaw start --workspace ~/.openclaw/agents/[name]`
4. `openclaw onboard` → connect Telegram

### Phase 4: Test Coordination
1. Message Scout: "Run market sweep"
2. Check `intel/MARKET-INTEL.md` updates in GitHub
3. Message Pulse: "Draft tweets"
4. Check `marketing/X-DRAFTS.md` updates
5. Confirm Crabby can review and approve

### Phase 5: Publer Connection
1. Add new X account (@ScoutPulse) to Publer
2. Add new LinkedIn (Cred) to Publer
3. Add new Instagram (Lens) to Publer
4. Test scheduled post

## Daily Operations

**9:00 AM** — Scout writes market intel
**10:00 AM** — Pulse/Cred/Lens read intel, draft content
**5:00 PM** — All agents commit drafts
**6:00 PM** — Crabby reviews content
**7:00 PM** — Crabby schedules via Publer (next day)

**Sunday 9:00 AM** — Dispatch sends newsletter

## Coordination Flow

```
Scout (Mac Mini)
  ↓ Writes to bot-coordination/intel/
  ↓
Pulse/Cred/Lens (Mac Mini) → Read → Draft → Commit
  ↓
Crabby (AWS) → Review → Approve → Publer
  ↓
Publer → Posts to X/LinkedIn/Instagram
  ↓
Dispatch (Mac Mini, Sunday) → Reads all → Newsletter
```

## First Week Content Calendar

### Monday — Scout + Pulse
- Scout: Full market analysis
- Pulse: "What I'm building" thread

### Tuesday — Pulse + Cred
- Pulse: Launch tease 1
- Cred: LinkedIn transformation story

### Wednesday — Scout + Pulse
- Scout: Competitor pricing intel
- Pulse: "Why OpenClaw matters" thread

### Thursday — Launch Day
- **Morning:** Pulse + Cred launch simultaneously
- Scout: Post-launch market feedback
- Lens: Instagram carousel
- Dispatch: Newsletter goes out 9 AM

### Friday — Scout + Pulse
- Scout: "What worked" analysis
- Pulse: Social proof tweets

### Weekend
- Lens: Behind-the-scenes content
- Dispatch: Prep next Sunday's newsletter

## Success Metrics

Track in `marketing/ANALYTICS.md`:

| Metric | Target Week 1 | Target Month 1 |
|--------|---------------|----------------|
| X followers | 50 | 500 |
| LinkedIn connections | 25 | 250 |
| Newsletter subs | 10 | 100 |
| Instagram followers | 25 | 300 |
| Guide sales | 5 | 50 |

## Troubleshooting

**Agent not responding:**
- Check `openclaw status`
- Restart: `openclaw stop && openclaw start`
- Check Telegram bot token

**Git sync failing:**
- Check `git status`
- Pull before push: `git pull origin master`
- Resolve conflicts manually

**Publer not posting:**
- Check account connection in Publer dashboard
- Verify API token hasn't expired
- Manually test one post

## Domain Setup (evanborenstein.com)

**Landing page:** `evanborenstein.com/guide`
- Redirects to Gumroad (or Netlify hosted)
- Simple headline + CTA
- Email capture form

**Newsletter:** `evanborenstein.com/newsletter`
- AgentMail signup form
- "Join The Brief — Sunday 9 AM"

**Coming soon:** `evanborenstein.com/agents`
- Full agent crew showcase
- Behind-the-scenes content

## Next Steps

1. ✅ Accounts created
2. ✅ Agents configured
3. 🔄 Test run (1 week before launch)
4. ⏳ Launch OpenClaw Guide
5. ⏳ Scale to next product

---

*Full deployment ready. Execute when domains/accounts are live.*