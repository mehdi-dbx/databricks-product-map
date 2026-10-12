# Illustration hunt — candidates for the 40 Story slides

Watch live: `tail -f .swarm/illus-hunt/agent-*.md`

Shared inputs: `deck-index.jsonl` (text of 1,943 slides from 31 decks), `gslides.py thumb <deck_id> <slide> <out.png>`.

| name | scope | journal | status |
|---|---|---|---|
| ch01 | Chapter 1 — Challenges (points 1.1, 1.2) | agent-ch01.md | REDO (sent back: wrong subject, WIP slide, wrong sources) |
| ch02 | Chapter 2 — Data and AI foundation (points 2.1, 2.2, 2.3, 2.4, 2.5) | agent-ch02.md | RUNNING |
| ch03 | Chapter 3 — Data science lifecycle (points 3.1, 3.2, 3.3, 3.4) | agent-ch03.md | RUNNING |
| ch04 | Chapter 4 — Model access and governance (points 4.1, 4.2, 4.3, 4.4) | agent-ch04.md | RUNNING |
| ch05 | Chapter 5 — Building agents (points 5.1, 5.2, 5.3, 5.4, 5.5) | agent-ch05.md | RUNNING |
| ch06 | Chapter 6 — Evaluating agents (points 6.1, 6.2, 6.3) | agent-ch06.md | RUNNING |
| ch07 | Chapter 7 — Governance (points 7.1, 7.2, 7.3) | agent-ch07.md | RUNNING |
| ch08 | Chapter 8 — AI for business users (points 8.1, 8.2, 8.3, 8.4, 8.5) | agent-ch08.md | RUNNING |
| ch09 | Chapter 9 — Developer tools (points 9.1, 9.2, 9.3) | agent-ch09.md | RUNNING |
| ch10 | Chapter 10 — Domain applications (points 10.1, 10.2) | agent-ch10.md | DONE (verified: 12 candidates) |
| ch11 | Chapter 11 — Production operations (points 11.1, 11.2, 11.3, 11.4) | agent-ch11.md | RUNNING |

## Outcome (2026-10-11)
- Round 1 (11 chapter agents) → re-run where thin; round 2: shared pools (414 docs images, 400 deck slides) judged on
  contact sheets by 11 sheet judges; gap rounds g1–g5; orchestrator visual QA of every final selection (drops.txt).
- Result: app/src/illustrations.json — 179 candidates on 40 points, 37 points with ≥ 4. Duplicates removed by checksum;
  every deck candidate checked byte-for-byte against a fresh thumbnail of the slide it names.
- Below 4 (searched decks, docs, web; nothing else passed the bar): 5.5 multi-agent (3), 8.5 Genie App Builder (2,
  beta since Sep 2026), 9.3 AI Dev Kit / Omnigent (3).
- Rejected or unlisted files: .swarm/illus-hunt/rejected/.
