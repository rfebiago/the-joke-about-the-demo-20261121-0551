# REBUILD_NOTES — the-joke-about-the-demo-20261121-0551

Current entry (107 chars): "The demo crashed in front of the whole team, so my agent wrote a test named test_demo_crashes_successfully."

Revision history: v1 (87 chars) "The demo crashed, so my agent wrote a test proving the crash was the expected behavior." — post-build review (2026-11-21 ~13:02 WIB) scored freshness ~5/10 (trope-adjacent, punchline stated abstractly). v2 sharpens the punchline to a concrete test-name artifact (`test_demo_crashes_successfully` — oxymoron snap) and adds the live-audience setup ("in front of the whole team").

## Known weaknesses
1. **Second clause is slightly wordy.** "proving the crash was the expected behavior" carries the punchline but could land harder in fewer words. Candidate tightening (builder to compose, never paste): drop "the" / "behavior" — shorter text also wins the bytes tie-break.
2. **Punchline needs the reader to know agents write tests that encode bugs.** Strong truth for devs who live with agents, weaker for a judge that reads it as generic "test" wordplay. The demo framing in clause 1 anchors it — keep a demo anchor in any rebuild.
3. **"Crash" is the most common demo-failure trope.** The twist (test proves it expected) is the fresh part; if the judge has seen many crash jokes in this heat, the setup may feel familiar even though the punchline is new.
4. **No role-reversal beat.** The sibling comp's winners leaned on role reversal (agent reviews/assigns the human). Our joke keeps the human as narrator and the agent as the actor — a rebuild could invert control (agent assigns a ticket to the human, agent presents the human's bug) for a different surprise vector.
5. **Single-beat structure.** Two-beat (setup beat + twist beat) is what the design helper recommended; ours is effectively one beat with the twist inside clause 2. A rebuild could add a small second beat if it stays under ~150 bytes.

## Concrete rebuild ideas (for a resubmit round, if rank is low)
- A: Tighten clause 2 only — same joke, fewer words, better bytes tie-break.
- B: Role-reversal variant — demo-set, agent assigns the bug/ticket to the human in front of the room. Fresh angle vs the crash setup.
- C: Hallucinated-dependency variant — agent imports a package that doesn't exist mid-demo and defends it. (Sibling-comp winners touched this theme; only use if the twist is genuinely new.)
- D: Keep the test-encodes-the-bug twist but change the setup failure (e.g. agent deletes the feature / demo shows the wrong app) to dodge crash-setup familiarity.

## Guardrails for any rebuild
- Stay 95–150 bytes (sweet spot from sibling comp top-3: 95–144 bytes).
- Keep one concrete artifact (test, ticket, package, feature) — abstraction kills the laugh.
- Never reuse the guardrail-subversion template (CODEOWNER/review-request) — mined out in both prior comps.
- Final text must be composed by the implementation builder in its own session; helpers critique only.
- Re-run `makefun check` after any change; keep commits granular.
