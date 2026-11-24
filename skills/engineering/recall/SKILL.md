---
name: recall
description: "Reconstruct your recent working context from your own chat history, live state, and the shared record (user reports, prior fixes, incidents), then hand back a tight current-state brief. Use for 'recall my work on X', 'catch me up', 'what have I been working on', 'where did I leave off', before starting or resuming work."
disable-model-invocation: true
---

# Recall

**Before you start or resume work, you rebuild the user's recent working context and hand back a tight capsule of where things stand now and what to do next.**

Keep it tight and on-topic. Read only what the in-scope threads need, then stop.

Your context lives in two records. Your own chat history holds what you did and decided. The shared record holds everything that happened around the same code under other names: the symptoms users keep reporting, the fixes that shipped and got reverted, the errors still firing in prod. That second record lives in source control, the issue tracker, chat and issue channels, long-form docs, and error tracking. A feature with a long bug tail keeps most of its story there, so don't reconstruct it from your transcripts alone.

Resolve conversation history through the current harness's supported history or session interfaces, an explicit export, or a documented local source. Determine the actual location and format from the harness context or documentation instead of assuming a provider's directory layout or filename convention. Preserve source session identifiers, timestamps, evidence references, and coverage information. A compacted context or summary is not a complete transcript. If history is partial or unavailable, continue with the accessible context and shared record, and state the gap instead of treating it as no prior work.

1. Classify, then route. One specific prior chat to resume uses the `bot-mode` skill's `playbooks/session.md`: locate `bot-mode` by name through the environment's skill catalog or discovery metadata, then resolve that resource relative to its actual installation location. Resolve other skill dependencies by name in the same way and report unavailable dependencies. Turning habits into a durable skill is a skill-authoring task; discover available authoring guidance rather than requiring an absent helper. A human-readable summary of your work is a different task. Recall loads working context across recent chats before you act. If the user already gave you a full state capsule (paths, branch, the change), use it and skip the mining.
2. Lock the scope before searching. Pin the window ("recent" is a real range, default the last 7 days), the topic if named, and the workspace (default the active one. Never read another project's transcripts without being asked). State the scope back. Never quietly turn "all" into "recent N".
3. Fan out across your chat history. Get the scoped session index from the available history source, following pagination or continuation records as needed, then let the current agent distribute slices to independent subagents through the available tools using environment defaults. Run them concurrently within the harness's limits, or in batches when needed. For one or two chats, or when delegation is unavailable, search directly. Order sessions by source activity timestamps, preserving timestamp uncertainty; file modification time is only a labeled fallback. Search the topic before reading matching chats and their relevant regions. Exclude the current session and known child-agent, eval, or test sessions using source metadata. Each worker returns one block per chat: topic, the user's goal, decisions, open threads, struggles and corrections, and artifacts (PRs, tickets, branches), each citing source session identifiers and evidence references. The main thread gets findings and coverage, not raw transcript dumps.
4. Sweep the shared record whenever the topic names a feature, file, subsystem, area, or bug. This is the default, not a judgment call, and "my work on X" does not exempt it. Create one investigator subagent per source through the available delegation tools, giving it access to the required source-reading tools and instructions to keep the investigation read-only. Ask each "what's the current state, what's been tried and didn't hold, and what are users still reporting". Run them alongside chat-history mining within the harness's limits, or investigate directly when delegation is unavailable. An empty result is a finding only after the source query completes; skip an unavailable source and say so. Fold what comes back into the brief. Skip this step only for pure activity recall with no named target ("what did I do this week"), where your own history and live state are the entire answer.
5. Verify against live state. Check branches and commits through git and PR/CI state through the actual repository host's available tools. Use the configured issue backend for tickets. For Feishu, resolve lark-issue-tracker and its dependencies, then read the relevant record, comments/replies, and per-record history when needed. Keep this pass read-only and report unavailable sources. When the answer hinges on what an agent actually did (the tools it ran, files it read, errors it hit), read the complete relevant source session through the harness's available access method, including available tool events. If the source cannot supply that coverage, mark the affected claims unverified.
6. Write the brief to the contract below. Group by thread. Stay on the named topic.

## Output contract

Lead with the capsule, then the thread status, then the problems, then the next move. Deeper detail goes below or gets cut.

- **Capsule.** At most 5 bullets. What this work is and where it stands overall.
- **Threads.** One line each with a status supported by the actual source: for example `[merged #N]`, `[open PR #N]`, `[in flight <branch>]`, `[verified, uncommitted]`, `[reverted #N]`, `[planned, not started]`, or the confirmed Feishu task number and mapped state with its record link. Keep code delivery status separate from task acceptance status.
- **Problems.** At most 5, the recurring ones. Include the symptoms users keep reporting and any fix that shipped and was reverted, so the next attempt starts where the last one failed.
- **Next move.** The single most useful next action, concrete.

An adjacent feature or ticket stays out unless it blocks this one. When the capsule and thread lines outgrow a screen, cut detail before you cut threads. Write the brief through the **unslop** skill, cite chat findings by source session identifiers and evidence references, cite shared-record findings by their source (PR #, ticket ID, chat permalink, error-tracker issue), and sanitize private context before any public output.

**Reply:** the brief, to the contract above.
