# Agent Standard Best Practices (2026)

Synthesized from the agentskills.io spec, GitHub's 2,500+ AGENTS.md study, the ETH context-file study, and leading skill repos (Anthropic, VoltAgent, wshobson, obra/superpowers).

---

## 1. Skills (SKILL.md)

### Frontmatter is the contract
- **`name`** — lowercase, hyphens only, ≤64 chars, must match the parent directory. **Never add namespace prefixes** (e.g. `team:foo`) — causes silent discovery failure.
- **`description`** — ≤1024 chars; the single biggest lever for whether a skill triggers. Must answer **what** + **when**. Be "pushy": list explicit verbs and synonyms ("write, draft, scope, spec a PRD"). Vague descriptions = dead skills.

### Progressive disclosure (three tiers)
1. **Discovery** (~100 tokens) — only `name` + `description` loaded into every session.
2. **Activation** — full SKILL.md loaded when triggered. Target **<5,000 tokens**. Lean body, link to references.
3. **Execution** — references, scripts, assets loaded on demand from the skill folder.

### Structure that wins
- **One skill = one job.** Single-responsibility. If you can't name it in a verb, split it.
- **Short SKILL.md, fat references folder.** Keep prose minimal in SKILL.md; push templates, examples, and long process detail into sibling files (`references/`, `scripts/`, `assets/`).
- **Show, don't tell.** A real example beats three paragraphs of description.
- **`evals.json` with `should_trigger` / `should_not_trigger`** (≥5 each). Prevents over- and under-triggering as your library grows.

### Security hygiene
- Skills can execute arbitrary code. Install only from trusted sources. Review SKILL.md and any scripts before adding to a project.
- Beware skills that fetch external URLs at runtime — they bypass the audit trail.

### Storage layering
- `~/.claude/skills/` (personal) and `.claude/skills/` (project, git-shared) for Claude Code.
- Equivalent paths for Codex (`.codex/skills/`), OpenClaw, etc.
- **Project-level overrides personal-level** — use this to pin a team's version.

---

## 2. Instructions (AGENTS.md / CLAUDE.md)

GitHub's analysis of 2,500+ repos found the best AGENTS.md files share six traits.

### Six core areas to cover
1. **Commands** (executable, with versions: `npm run docs:build`, not "build the docs")
2. **Testing** (exact invocation, not philosophy)
3. **Project structure** (kept current — see anti-pattern below)
4. **Code style** (one real snippet beats prose)
5. **Git workflow** (branch naming, commit format, PR rules)
6. **Boundaries** (the three-tier rule — see below)

### Three-tier boundaries
- **Allowed without prompt** — read files, run a single test, lint, format
- **Ask first** — install packages, push, delete files, run full suites
- **Never** — secrets, prod configs, vendor dirs

"Never commit secrets" was the **single most common helpful constraint** across the 2,500 repos studied.

### Length: ≤150 lines (ideally less)
- AGENTS.md is read at the start of every session. Long files **slow the agent and bury signal**. Critical rules go first.
- Claude Code best practice for CLAUDE.md is **<60 lines** — point at AGENTS.md, don't duplicate.

### Layering
- **Nested AGENTS.md** for monorepos — agents read the nearest one. OpenAI's main repo has 88. Codex concatenates root-down, with the nearest file taking precedence.
- **Personal overrides** — `~/.codex/AGENTS.override.md` for temporary global rules without touching shared instructions.

### Iterative, not upfront
- Best AGENTS.md files grow through trial and error. When the agent makes a mistake, codify the fix as a rule.
- When you comment on an agent's PR, mirror the comment into AGENTS.md.

---

## 3. Anti-patterns (the ETH study)

A 2025 ETH study tested LLM-generated context files vs. hand-written ones:

- **LLM-generated AGENTS.md hurt performance in 5 of 8 settings.** +2.45–3.92 steps per task, +20–23% inference cost.
- **Stale structural references actively mislead.** Architectural overviews increase cost and encourage broader (worse) file traversal without improving success.
- **"Lost in the middle"** — long context files cause silent rule dropout; agents quietly stop following CLAUDE.md mid-session.
- **Checks are advisory.** Agents may skip programmatic checks they judge unnecessary. Don't assume mechanical enforcement.

**Implication**: hand-write your instructions, keep them short, and don't document repo structure in prose — let the file tree speak.

---

## 4. Best-in-class repo patterns

From the leading skill collections, common architectural moves:

- **`anthropics/skills`** — canonical reference. Notable: `skill-creator` (a meta-skill that scaffolds new skills), `webapp-testing`, `mcp-builder`. Document skills (`docx`, `pdf`, `pptx`, `xlsx`) ship in production.
- **`obra/superpowers`** — battle-tested PM/eng patterns: TDD loops, debugging rituals, collaboration handshakes. Cited as the highest-quality community library.
- **`wshobson/agents`** — 184 specialized agents + 150 skills + 16 orchestrators, organized into **78 single-purpose plugins**. Demonstrates that scale comes from narrow scope per unit, not bigger units.
- **`VoltAgent/awesome-agent-skills`** — curated, official-team-first (Anthropic, Vercel, Stripe, Cloudflare, Sentry). Filters out AI-bulk-generated noise.
- **`mcollina/skills`** — Matteo Collina's 11 personal skills (Node/Fastify/TypeScript). Proof that **a small, opinionated set beats a big generic one**.

Cross-cutting patterns:
- **Plugin marketplaces** (`/plugin install document-skills@anthropic-agent-skills`) are emerging as the distribution standard.
- **Verification badges** (✅ in `karanb192/awesome-claude-skills`) signal community review — useful when curating.
- **Cross-tool compatibility** is now table stakes: top repos work in Claude Code, Codex, Cursor, Gemini CLI, Antigravity simultaneously.

---

## 5. Validation & CI

- Most mature repos run a **schema validator on every PR** (frontmatter shape, naming rules, evals presence).
- **Linters that run the agent against fixtures** (your `evals.json`) are becoming the next bar — measure activation, not just syntax.
- The `skills-ref` library (community) provides reference cases for validating SKILL.md compliance.

---

## Sources

**Spec & canonical**
- [agentskills.io/specification](https://agentskills.io/specification)
- [agents.md](https://agents.md/)
- [Claude Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills)
- [Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md)
- [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/agents/skills)

**Industry analysis**
- [GitHub: How to write a great agents.md (2,500+ repos)](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [Augment Code: Build Your AGENTS.md (2026)](https://www.augmentcode.com/guides/how-to-build-agents-md)
- [Builder.io: Improve AI output with AGENTS.md](https://www.builder.io/blog/agents-md)
- [Marmelab: Agent Experience best practices](https://marmelab.com/blog/2026/01/21/agent-experience.html)

**Best-in-class repos**
- [anthropics/skills](https://github.com/anthropics/skills)
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- [wshobson/agents](https://github.com/wshobson/agents)
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills)
- [skill-creator (Anthropic)](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)

**Articles**
- [Bibek Poudel — The SKILL.md Pattern](https://bibek-poudel.medium.com/the-skill-md-pattern-how-to-write-ai-agent-skills-that-actually-work-72a3169dd7ee)
- [Fungies.io — AI Agent Skills 2026 Guide](https://fungies.io/ai-agent-skills-skill-md-guide-2026/)
- [Spring AI — Generic Agent Skills](https://spring.io/blog/2026/01/13/spring-ai-generic-agent-skills/)
- [Tim De Schryver — Keep Agentic AI Simple](https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development)
