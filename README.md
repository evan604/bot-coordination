# Bot Coordination Hub

Shared workspace for Crabby, Tazer, and Max.

## Structure
- `intel/` — Research and daily briefs
- `agents/` — Per-bot working directories
- `tasks/` — Shared task queue

## How It Works
1. Tazer writes research to `intel/DAILY.md`
2. Crabby reads, synthesizes, assigns tasks
3. Max turns intel into content
4. All bots sync via git

---
*Created: March 3, 2026*