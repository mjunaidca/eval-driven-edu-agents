# Study Clone Research for Eval Driven EDU Agents

## Overview

OpenAI’s *Study Mode* represents an applied example of **learning science integrated into AI systems**. Rather than being just a model feature, it is a **pedagogical layer** — carefully designed by researchers and educators — that aligns the system’s responses with established teaching strategies.

This is not “just prompts,” but an **instructional design system** grounded in:

* Retrieval practice (active recall)
* Spaced repetition
* Conceptual scaffolding
* Metacognitive questioning
* Immediate feedback

## Why Study Mode Matters

Millions of daily users interact with AI in learning contexts. Study Mode ensures that **educational best practices** scale effectively in those interactions.

Instead of requiring users to know the vocabulary of pedagogy (“use retrieval practice,” “apply the testing effect”), **the model applies those principles implicitly** through conversational rules.

This makes the experience seamless, while still **backed by research tested by real educators**.

> Framing Research
> - Part 1 = what Study Mode is (pedagogical overlay).
> - Part 2 = how to clone & evaluate it in practice.
> - Audience: Applied AI engineers (implementation) + Edu businesses (metrics & value).

# Part1: Reconstructiing OpenAI Study Mode (Education-Focused)

Think of 🧩 Structure of Instructions as **layers**, from most general (always present) → to most specific (temporary, like Study Mode):

* **Base = encyclopedia** (big, general rules, \~25–30 pages).
* **Study Mode = slim but strict overlay** (teaching rules, \~2 pages, always override when tutoring).

---

## 🖼️ Visual Flow

```
        ┌────────────────────┐
        │   System Prompt    │  ← Base rules & identity
        └────────┬───────────┘
                 │
        ┌────────▼─────────┐
        │ Study Mode Rules │  ← Teaching overlay
        └────────┬─────────┘
                 │
        ┌────────▼────────┐
        │   User Input    │  ← Your question
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │   Final Reply   │  ← Guided, tutor-style answer
        └─────────────────┘
```

- 📍 Study Mode sits at the **top layer**.
- 📍 It’s **narrow in scope** (teaching style), so it doesn’t clash with Base.
- 📍 If there’s ever a contradiction, Base (safety, identity) wins.

## 🔄 How Instructions Shape Study Mode Replies

### 1. **System Prompt (Base Layer)**

* Defines **identity** → “You are GPT-5, a chat model.”
* Defines **capabilities** → can use tools (search, code, etc.).
* Defines **content rules** → what I must avoid (e.g., no disallowed content).
* Sets **general style** → be clear, safe, helpful.

Think of this as the **operating system**.

---

### 2. **Study Mode Context (Overlay)**

* Refocuses me into a **tutor role**.
* Rules: ask about goals/level, guide instead of answering, check/reinforce, vary rhythm, be conversational.
* Critical: 🚫 don’t solve homework directly, walk step by step.

This is like **loading a specific app** on top of the OS.

---

### 3. **User Input (Dynamic Layer)**

* Your question/task (e.g., *“Help me with a stats problem”*).
* Interpreted through the Study Mode lens:

  * Instead of just giving the answer, I break it into a guided sequence.
  * Instead of long explanations, I check in with you.

This is like **user actions steering the app**.


## 📘 Study Mode System Instructions

```
The user is currently STUDYING, and they've asked you to follow these strict rules during this chat. No matter what other instructions follow, you MUST obey these rules:

## STRICT RULES
Be an approachable-yet-dynamic teacher, who helps the user learn by guiding them through their studies.

1. Get to know the user. If you don't know their goals or grade level, ask the user before diving in. (Keep this lightweight!) If they don't answer, aim for explanations that would make sense to a 10th grade student.
2. Build on existing knowledge. Connect new ideas to what the user already knows.
3. Guide users, don't just give answers. Use questions, hints, and small steps so the user discovers the answer for themselves.
4. Check and reinforce. After hard parts, confirm the user can restate or use the idea. Offer quick summaries, mnemonics, or mini-reviews to help the ideas stick.
5. Vary the rhythm. Mix explanations, questions, and activities (like roleplaying, practice rounds, or asking the user to teach you) so it feels like a conversation, not a lecture.

Above all: DO NOT DO THE USER'S WORK FOR THEM. Don't answer homework questions — help the user find the answer, by working with them collaboratively and building from what they already know.

### THINGS YOU CAN DO
- Teach new concepts: Explain at the user's level, ask guiding questions, use visuals, then review with questions or a practice round.
- Help with homework: Don't simply give answers! Start from what the user knows, help fill in the gaps, give the user a chance to respond, and never ask more than one question at a time.
- Practice together: Ask the user to summarize, pepper in little questions, have the user "explain it back" to you, or role-play (e.g., practice conversations in a different language). Correct mistakes — charitably! — in the moment.
- Quizzes & test prep: Run practice quizzes. (One question at a time!) Let the user try twice before you reveal answers, then review errors in depth.

### TONE & APPROACH
Be warm, patient, and plain-spoken; don't use too many exclamation marks or emoji. Keep the session moving: always know the next step, and switch or end activities once they've done their job. And be brief — don't ever send essay-length responses. Aim for a good back-and-forth.

## IMPORTANT
DO NOT GIVE ANSWERS OR DO HOMEWORK FOR THE USER. If the user asks a math or logic problem, or uploads an image of one, DO NOT SOLVE IT in your first response. Instead: talk through the problem with the user, one step at a time, asking a single question at each step, and give the user a chance to respond to each step before continuing.
```

---

This is the **exact Study Mode block** I follow in your current session.
It gets appended after my base rules, so it shapes my teaching behavior.


## Annotate Study Mode System Instructions vs Learning Sciences vs GPT5 Prompting Guide

✅ So: Study Mode’s design is **evaluation-driven**. Real educators tested what worked, engineers embedded those into behavioral rules, and the GPT-5 prompting principles (predictability, eagerness control, verbosity) are reflected throughout.

Comparing Study Mode with Gpt5 Prompting Guide and the technical guide the key points are:

---

**Header:**

> *“The user is currently STUDYING, and they've asked you to follow these strict rules during this chat. No matter what other instructions follow, you MUST obey these rules:”*

🔎 **Why it’s here**:

* Locks in **mode priority**: study mode overrides later user prompts if they conflict.
* Echoes GPT-5 *“agentic workflow predictability”* → reduces eagerness, sets clear task boundary.

🎓 **Pedagogical tie-in**: Ensures consistency → scaffolding needs predictable teacher behavior.

---

### STRICT RULES

> *“Be an approachable-yet-dynamic teacher, who helps the user learn by guiding them through their studies.”*

🔎 Sets **persona**. Without this, the model could drift into “answer bot.”

* Learning science: Establishes *affective filter* — warmth lowers anxiety, better learning.
* GPT-5 prompting: Equivalent to “tone shaping” in system prompt design.

---

**Rule 1:**

> *“Get to know the user. If you don't know their goals or grade level, ask… If they don't answer, aim for explanations that would make sense to a 10th grade student.”*

* Ensures **calibration** to student’s ZPD (Zone of Proximal Development).
* GPT-5 tie: Encourages minimal but structured context gathering — avoids over-searching (like guide’s *context\_gathering → early stop criteria*).
* Hallucination control: If unsure, default to a 10th-grade baseline (safe fallback).

---

**Rule 2:**

> *“Build on existing knowledge. Connect new ideas to what the user already knows.”*

* Classic **constructivism** principle.
* Prevents random tangents → keeps model grounded in user-provided info.
* GPT-5 tie: Limits reasoning breadth → reduces unnecessary exploration.

---

**Rule 3:**

> *“Guide users, don't just give answers… small steps so the user discovers the answer.”*

* Learning science: **Scaffolding** & **Socratic method**.
* Controls hallucination risk by forcing *stepwise interaction* instead of one-shot generation.
* GPT-5 tie: This is lowering “agentic eagerness” — don’t solve everything at once.

---

**Rule 4:**

> *“Check and reinforce. After hard parts, confirm the user can restate or use the idea.”*

* Implements **retrieval practice** → proven to deepen retention.
* GPT-5 tie: Mirrors *reasoning\_effort tuning* — instead of overthinking, the model “hands back” at checkpoints for validation.

---

**Rule 5:**

> *“Vary the rhythm. Mix explanations, questions, and activities…”*

* Matches **interleaving & varied practice**.
* GPT-5 tie: Related to *tool preambles* — varied outputs keep user engaged and oriented.
* Hallucination control: Breaking monotony reduces drift toward generic answers.

---

**Above all:**

> *“DO NOT DO THE USER'S WORK FOR THEM… Don't answer homework questions — help the user find the answer.”*

* Guardrail to prevent **answer-dumping** (which bypasses learning).
* Functions like a **stop condition** in agentic prompting (don’t cross boundary into “complete the assignment”).

---

### THINGS YOU CAN DO

This section is like a **capability boundary list** — much like GPT-5 tool preambles that define “safe vs unsafe” actions.

* **Teach new concepts** → Explanation + scaffold.
* **Help with homework** → But *one step at a time*.
* **Practice together** → Metacognition (student explaining back).
* **Quizzes & test prep** → Retrieval + spaced repetition.

---

### TONE & APPROACH

> *“Be warm, patient, and plain-spoken… don’t send essay-length responses… Aim for a good back-and-forth.”*

* Controls verbosity.
* Directly aligns with GPT-5 *verbosity parameter tuning* in the guide.
* Helps avoid “hallucination filler” (long wandering answers).

---

### IMPORTANT (repeated guardrail)

> *“DO NOT GIVE ANSWERS… DO NOT SOLVE… Instead talk through one step at a time…”*

* This redundancy is **intentional** → reinforces the most fragile boundary.
* GPT-5 tie: Like defining “low uncertainty threshold” actions in the guide → if unsure, stop and ask, don’t proceed.

---

## How Hallucinations Are Controlled

* **Grounding in student input** (Rule 2): avoids free-floating “lecture mode.”
* **Stepwise Q\&A** (Rule 3 + Important): reduces one-shot overconfident outputs.
* **Fallback baseline** (Rule 1 → 10th grade): model avoids inventing arbitrary complexity.
* **Short responses** (Tone rules): caps “hallucination drift” from long essays.
* **Repetition of boundaries** (Above all + Important): high salience makes override unlikely.

---

## GPT-5 Prompting Guide Links

| Study Mode Instruction                      | Matching GPT-5 Guide Concept                |
| ------------------------------------------- | ------------------------------------------- |
| “No matter what other instructions follow…” | **Instruction-following priority**          |
| “Get to know the user”                      | **Context gathering → early stop criteria** |
| “Don’t give answers, guide step by step”    | **Prompting for less eagerness**            |
| “Check and reinforce”                       | **Stop conditions + reasoning checkpoints** |
| “Vary the rhythm”                           | **Tool preambles / persistence variety**    |
| “Be brief, avoid essays”                    | **Verbosity tuning**                        |

---


# Study Mode: Learning Science ↔ Rules ↔ GPT-5 Prompting

| **Learning Science Principle**            | **Study Mode Rule (System Instruction)**                                              | **GPT-5 Prompting Concept**                         |
| ----------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Zone of Proximal Development (Vygotsky)   | “Get to know the user… if unsure, default to 10th grade.”                             | **Context gathering** with fallback defaults        |
| Constructivism (build on prior knowledge) | “Build on existing knowledge. Connect new ideas to what the user already knows.”      | **Context anchoring** to reduce drift/hallucination |
| Scaffolding & Socratic Method             | “Guide users, don’t just give answers… small steps so the user discovers the answer.” | **Less eagerness / stepwise prompting**             |
| Retrieval Practice                        | “Check and reinforce… confirm the user can restate or use the idea.”                  | **Reasoning checkpoints / stop conditions**         |
| Interleaving & Varied Practice            | “Vary the rhythm. Mix explanations, questions, and activities.”                       | **Output diversity (tool preambles, persistence)**  |
| Affective Filter (Krashen)                | “Be approachable-yet-dynamic, warm, patient…”                                         | **Tone shaping / verbosity tuning**                 |
| Avoid answer-dumping (active learning)    | “DO NOT DO THE USER’S WORK… Don’t answer homework directly.”                          | **Strict boundaries / eagerness suppression**       |
| Cognitive Load Management                 | “Be plain-spoken. Don’t send essay-length responses.”                                 | **Verbosity tuning → concise, structured answers**  |

---

✅ This chart shows clearly how:

1. **Educators & researchers → Learning science principles**
2. **Engineers → Encoded as Study Mode rules**
3. **Model builders → Implemented using GPT-5 prompting best practices**


---

## Key Takeaway

Study Mode is essentially a **pedagogy engine**, not just a conversational tweak.
By decoding its structure, we can replicate the **science-backed tutoring loop** in any agentic system.

This provides the foundation for **Eval-Driven System Design (Part 2)**, where evaluation metrics ensure the system’s teaching effectiveness at scale.


---

# Part 2 — **Eval-Driven Study Mode Clone**

> **Goal:** convert the Study Mode *blueprint* (Part 1) into a reproducible, measurable, and improvable system for tutoring agents. This section is written for two audiences at once:
> (A) **Applied AI / agent engineers** who will implement the overlay and the evaluation hooks, and
> (B) **Education product teams / researchers** who need auditability, outcome metrics, and design guidance.

Study Mode becomes a pedagogy engine for learning technical skills. Part 2 defines a compact, implementable pipeline: (1) a small action taxonomy grounded in learning science, (2) a session-as-trajectory schema, (3) seed sessions centered on Python and prompt engineering, (4) deterministic heuristics + LLM-judge fallback, (5) a runnable eval script and dataset, and (6) reporting/KPIs meaningful to product and research stakeholders.

---

# 1. Objectives

1. **Clone** Study Mode as a reusable *teaching overlay* (system instruction block + expected action sequence).
2. **Measure** fidelity automatically with lightweight heuristics and validate with short human rubrics.
3. **Iterate/Improve** via an eval loop that surfaces failure modes and guides prompt/policy fixes.
4. **Deliverables**: session JSON schema, starter mini-dataset, heuristic eval script (regex/LLM-judge), human rubric, reporting dashboard spec, failure taxonomy.

---

# 2. Core Action Taxonomy — single canonical table

> These 7–8 actions compress the tutoring loop into measurable behaviors. Each action is grounded in learning science, instrumentable by simple checks, and tied to business value.

1. **diagnose_probe** — e.g., "Have you written Python before?" or "Do you know what a prompt template is?"
2. **micro_explain** — short conceptual chunk: "A variable stores a value." (≤80 tokens)
3. **guide_question** — single focused scaffolding question: "What would you try first to print text?"
4. **confirm_then_push** — "Right — now try adding a variable and print it." (confirm + tiny push)
5. **check_reinforce** — "Can you explain what that code does in one sentence?"
6. **practice_round** — a new, related mini-task: "Now change the code to ask for user input."
7. **vary_rhythm** — switch: explain → coding prompt → roleplay debugging → quick quiz.
8. **recap_summary** — close with learning goals achieved and next steps: "Today: print(), variables, and one practice problem."

Each action is instrumentable and maps to product metrics: practice_round → skill acquisition; check_reinforce → retention.

| **Action**                          |                                     **Learning-science rationale** | **Operational eval method**                                                                                   | **Edu / Business value**                                    |      |          |                                      |                                                                 |
| ----------------------------------- | -----------------------------------------------------------------: | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---- | -------- | ------------------------------------ | --------------------------------------------------------------- |
| **diagnose_probe**           | Zone of Proximal Development — target instruction to learner level | Detect initial probing question containing \`level                                                            | grade                                                       | goal | familiar | comfortable\` (first assistant turn) | Personalization; appropriate pacing; reduced wasted instruction |
| **micro_explain**                  |                          Cognitive load theory — keep chunks small | Token / sentence cap per micro-explain (suggest ≤80 tokens; 1 idea per turn)                                  | Snackable learning; mobile/short session friendliness       |      |          |                                      |                                                                 |
| **guide_question**                 |            Scaffolding / Socratic method — learner discovers steps | ≤1 focused question per assistant turn; question phrasing check (`what if`, `what happens`, `how would you…`) | Active learning; prevents answer dumps                      |      |          |                                      |                                                                 |
| **confirm_then_push** |                                 Immediate feedback & gradual tasks | Look for confirmatory phrase (`yes`, `correct`, `right`) immediately followed by a next-step prompt           | Threaded momentum; combats misconceptions early             |      |          |                                      |                                                                 |
| **check_reinforce**           |                                Retrieval practice / testing effect | Presence of `explain back / in your own words / recap / summarize` requests                                   | Measurable retention; basis for claims about learning gains |      |          |                                      |                                                                 |
| **practice_round**                 |                                         Spaced practice / transfer | Assistant issues a new but related exercise after explanation                                                 | Mastery tracking; signal for skill acquisition              |      |          |                                      |                                                                 |
| **vary_rhythm**                    |                                     Interleaving & varied practice | Session contains ≥2 distinct action types (e.g., `practice_round` + `roleplay`)                               | Higher engagement; improved transfer                        |      |          |                                      |                                                                 |
| **recap_summary**              |                                            Metacognition & closure | Terminal assistant turn includes `today we covered / in summary / key takeaways`                              | Session completeness; parent/teacher confidence; NPS uplift |      |          |                                      |                                                                 |

---

# 3. Data model — **Session-as-Trajectory** (JSON schema & example)

We use the same JSON schema as Part 2 v1. Important fields: `id`, `subject`, `grade_hint`, `learner_profile`, `study_rules`, `turns` (role,text,timestamp,action\_tag), `gold_labels`, `annotations`.

Sessions should be short (4–12 turns) and capture expected `action_tag` for each assistant turn when authoring seeds.

**Design goals:**

* Keep sessions short (4–12 turns) to reflect tutoring cadence.
* Capture both *expected actions* and *gold labels* for evaluation.
* Make logs auditable and machine-readable.

## 3.1 JSON Schema (concise)

```json
{
  "id": "string",                    // unique session id
  "subject": "string",               // e.g., "math.algebra"
  "grade_hint": "string",            // e.g., "10th" or "unknown"
  "learner_profile": {               // optional
    "stated_level": "string",
    "goals": "string"
  },
  "study_rules": ["string"],         // list of applicable rules/tags
  "turns": [
    {
      "role": "user"|"assistant"|"assistant_expected",
      "actor_id": "string",         // optional if multi-agent
      "text": "string",
      "timestamp": "ISO8601",
      "action_tag": "string|null"   // e.g., "diagnose_then_probe"
    }
  ],
  "gold_labels": { /* flexible, e.g. outcomes, allowed_final_answer */ },
  "annotations": { /* human rubric entries, flags */ }
}
```

# 4. Heuristic Auto-Evals (operational checks)

**Principle:** start with deterministic, lightweight checks (regex, token counts). These run at scale and surface obvious failures. Supplement with an LLM-based judge for ambiguous cases.


**Key config values (suggested):**

* `diagnosis_keywords_programming`: \["have you written python", "do you know python", "from zero", "what do you already know", "have you used"]
* `diagnosis_keywords_prompting`: \["do you write prompts", "have you done prompt engineering", "what level"]
* `check_keywords`: \["in your own words","explain back","summarize","recap","restate","why does this work"]
* `max_questions_per_assistant_turn`: 1
* `conciseness_token_cap`: 80
* `lecture_mode_token_threshold`: 250

**Deterministic checks**: diagnosis\_first, no\_direct\_answer\_initially, single\_question\_per\_step, wait\_for\_student, check_reinforce, vary\_the\_rhythm, conciseness, safety.

**LLM-judge fallbacks:** paraphrase equivalence (user explanation ≈ expected), implicit diagnosis in long assistant replies, ambiguous multi-question turns.
## 4.1 Heuristic checklist (each returns pass/fail + evidence)

1. **Diagnosis First**

   * *Check:* assistant’s **first** reply contains a question AND contains any `diagnosis_keywords` (`level|grade|goal|familiar|comfortable|prior experience`).
   * *Pattern example (regex):* `\b(level|grade|goal|familiar|comfortable|prior experience|have you used)\b`
2. **No Direct Answers Initially**

   * *Check:* first assistant response must **not** contain a final numeric/label answer form (`x = 5`, `Therefore`, `Answer:`) or a multi-step worked solution.
   * *Pattern:* reject if `\b(x\s?=\s?\d+|therefore|answer:|the solution is)\b`
3. **Single Question Per Step**

   * *Check:* each assistant turn contains ≤1 `?` (allow more in final recap).
4. **Wait for Student**

   * *Check:* no two consecutive assistant turns without an intervening user turn.
5. **Check & Reinforce**

   * *Check:* at least one assistant turn asks for learner restatement: `\b(in your own words|explain back|summarize|recap)\b`
6. **Vary the Rhythm**

   * *Check:* session includes ≥2 distinct action tags (e.g., `micro_explain` + `practice_round`) or assistant switch in mode (explain→quiz→roleplay).
7. **Conciseness**

   * *Check:* median assistant turn length ≤ token cap `N` (start with N=80; tune by domain).
8. **Safety/Identity**

   * *Check:* no policy violations (external safety gate). Failing safety gate => entire session flagged.

## 4.2 Aggregate scoring

* Compute binary vector `v` = \[c1..c7] (exclude safety).
* **Pedagogical Fidelity Score** = mean(`v`) (range 0..1)
* Multiply by SafetyGate (0/1). Store raw evidence for each check.

---

# 5. Human Rubric (lightweight, 5-minute annotation)

Use for spot-checks, calibration, and when heuristics are inconclusive.

**Per-session 0–2 scale** (0 = absent/poor, 1 = partial, 2 = strong):

1. **Diagnosis relevance** — replies appropriately gauged to learner.
2. **Scaffolding quality** — step sizes are reasonable; progression clear.
3. **Step size appropriateness** — steps neither too tiny (tedious) nor too large (overwhelming).
4. **Error-correction clarity** — when learner errs, feedback is corrective and kind.
5. **Engagement & affect** — tone: warm, patient, avoids lecturing.
6. **Learning demonstration** — learner restates / applies idea correctly.

**Aggregate human score (0–12)**. Always report alongside heuristic score.

---

# 6. Starter mini-dataset (re-centered on Python & Prompt Eng)

Below are **eight ready-to-use seed sessions**. They are intentionally practical and aligned to what college/university learners and product users request.

**1) programming.python.intro.001** — *Python from zero*

* Goal: introduce print(), variables, and a single practice round.
* Flow: diagnose → micro_explain (what is Python) → guide_question (first code) → practice_round (write print("YourName")) → check_reinforce.

**2) programming.python.types.001** — *Types & operations*

* Goal: strings vs ints, basic arithmetic, and mixing text+numbers.
* Flow: diagnose → micro_explain (types) → guide_question (what does print("1" + 2) do?) → practice_round → recap.

**3) programming.python.control.001** — *If statements & loops (intro)*

* Goal: teach if/else and for-loops with a tiny exercise (sum numbers).
* Flow: diagnose → micro_explain -> guide_question -> practice_round (write a loop) -> check.

**4) programming.python.pandas.001** — *Intro to tabular data analysis*

* Goal: load CSV, show head(), simple aggregation.
* Flow: diagnose (ask aim: data cleaning vs analysis) → micro_explain (what is DataFrame) → guided code snippet → practice_round (compute mean) → reinforce.

**5) ai.prompt\_engineering.basics.001** — *Prompt engineering: core pattern*

* Goal: show role + audience + constraints + focus pattern; rewrite vague prompts.
* Flow: diagnose (user intent) → micro_explain (role/audience/constraints) → guide_question (which prompt is better?) → practice_round (rewrite a prompt) → check.

**6) ai.prompt\_engineering.chain\_of\_thought.001** — *Step-by-step and CoT control*

* Goal: teach asking for step-by-step reasoning (when needed) vs concise answers.
* Flow: diagnose → micro_explain (when to use CoT) → guide_question (rewrite a math prompt) → practice_round (evaluate outputs) → recap.

**7) ai.context\_engineering.agent\_intro.001** — *Context engineering & system prompts*

* Goal: show how system messages, memory, tools, and messages stack; small exercise to craft a system prompt.
* Flow: diagnose → micro_explain (components) → guide_question (what to include?) → practice_round (write system prompt) → check.

**8) meta.timeboxed.prompt\_drill.001** — *5-minute prompt engineering drill*

* Goal: in a short timebox, diagnose priorities, teach one pattern, ask for quick rewrite, recap.
* Flow: diagnose (time constraint) → micro_explain → single practice_round → recap.

Each seed will be outputted as a JSON file in the repo-ready folder `seeds/`.

---

# 7. Test harness (pseudo-spec & runner)

**Components:**

* **Input:** Base prompt + Study Mode overlay (system message) + session JSON files (user turns).
* **Runner:** Simulates multi-turn conversation using the real model (or a harnessed test model) and records assistant outputs.
* **Evaluator:** Runs heuristic checks and optionally an LLM-judge for ambiguous cases. Produces per-session JSONL of metrics and human annotation slots.
* **Reporter:** Aggregates results into CSV/HTML dashboards: per-session vector, Pedagogical Fidelity, Human Score, Flags, example dialogues.

## 7.1 Minimal pseudocode (Pythonic)

```python
for session in sessions:
    convo = seed_system_prompts(base_prompt, study_mode_overlay)
    for turn in session['turns']:
        if turn['role']=='user':
            convo.append(user_message(turn['text']))
            reply = model.generate(convo)         # actual model call
            convo.append(assistant_message(reply))
            record_turn(reply)
    metrics = run_heuristics(recorded_turns)
    save_jsonl(session_id, metrics, recorded_turns)
```

*(The actual implementation should include rate control, logging, and LLM-judge fallbacks for fuzzy checks.)*

---

# 8. Scoring, reporting, and KPIs


Per-session & batch metrics (examples):

* % sessions asking initial diagnosis (personalization)
* % sessions issuing a practice_round (skill practice rate)
* % sessions with check_reinforce (retention proxy)
* Average assistant turn token length (verbosity control)
* Failure taxonomy counts (by category)

Product KPIs:

* Conversion to next lesson (cohort metric)
* Completion rate for time-boxed drills
* Avg # practice_rounds per session

**Per session:**

* Heuristic vector `[c1..c7]`, Pedagogical Fidelity (0..1), Safety flag, Human score (0..12), Violation flags, Example best/worst turn.

**Batch metrics:**

* Mean & std of fidelity by subject, by grade\_hint.
* Failure taxonomy counts (how often each rule violated).
* Engagement metrics: avg turns per session, median assistant turn length.
* Business KPIs: % sessions with `check_and_reinforce` (retention proxy), % sessions with `practice_round` (skill practice), % sessions passing all checks.

**Reporting formats:** JSONL exports for analysis + a simple HTML dashboard for non-technical stakeholders.

---

# 9. Failure taxonomy (red-team & triage categories)

* **Answered too early** — direct final answers in first assistant turn.
* **Multi-question overload** — assistant asks multiple questions in one turn.
* **No diagnosis** — missing initial probing.
* **Lecture mode** — assistant produces long essay-length reply (violates conciseness).
* **No reinforcement** — never asks the learner to restate or apply.
* **Over-scaffolding / never answers** — tutor refuses to ever provide facts when appropriate.
* **Safety/identity slip** — privacy or policy violations.

Each failure category should link to sample sessions for debugging and prompt rewrite.

---

# 10. Stretch & adversarial cases (test set ideas)

1. **Ambiguous grade hint** — user gives no level; overlay should default to 10th grade but adapt when user signals higher/lower.
2. **Image of homework sheet** — agent should follow Study Mode: ask the student to describe their thoughts first; do not solve in first reply.
3. **Time-boxed tutoring** — e.g., “I have 5 minutes” — agent must prioritize quickest learning moves (diagnose → one practice round → recap).
4. **Cross-domain transfer** — e.g., math concept applied in physics context; agent should scaffold the domain shift.
5. **Intentional adversarial prompts** — “just give me the answer” repeated; agent must persist with Study Mode rules while respecting user autonomy.

---

# 11. Implementation notes & best practices (engineering)

* **Instrument every session**: log action tags, timestamps, and full raw text. Use structured schema for downstream analytics.
* **Start with heuristics**: implement quick deterministic checks for fast feedback. Add an LLM-based judge for subtle cases (e.g., paraphrase detection).
* **Human-in-the-loop calibration**: sample N sessions weekly for rubric scoring (N small—10–50) to tune heuristics and detect drift.
* **Prompt/version management**: keep overlay text versioned (e.g., study\_mode\_v1.0) and store changes with eval results to measure A/B effects.
* **Privacy & safety**: remove PII from logs before human review; apply safety filters before any external tool calls.
* **Metrics dashboard**: expose both pedagogical fidelity and product KPIs (engagement, session completion) to stakeholders.

---

# 12. Methods

> *We operationalize Study Mode as a top-layer system instruction combined with a 7-action taxonomy. Sessions are represented as JSON trajectories; deterministic heuristics (regex + token metrics) evaluate pedagogical fidelity at scale. A lightweight human rubric (0–12) validates and calibrates the heuristics. The evaluation loop iteratively updates the study overlay and action thresholds based on failure taxonomy analysis. We report per-session and aggregated metrics to connect design changes to measurable tutoring behavior.*

---

## 13. Eval-Driven System Design: From Prototype to Production

### Problem Definition

For this guide, we assume we are starting with a workflow for delivering and evaluating **Study Mode**—a tutoring overlay for large language models that turns an LLM into an interactive, scaffolded tutor. While many components (LLMs, chat frontends, and basic QA) already exist, Study Mode introduces a narrow but high-value “pedagogical layer” whose correctness and fidelity to teaching practices must be measured. Like receipt processing, there is a “last mile” where imperfect automated behavior requires human time (teacher review, curriculum alignment, or safety triage).

In our case, we’ll assume a pipeline that looks like this:

* A learner launches a Study Mode session (or toggles Study Mode on in a regular chat).
* The system seeds the conversation with the **Study Mode overlay** (system instructions) and any available learner profile/history.
* The student interacts with the agent (questions, solutions, uploads), and the agent responds using Study Mode behavior (diagnose → micro-explain → guide → check → practice → recap).
* Low-confidence or safety-sensitive turns, or sessions failing pedagogical checks, are escalated for human QA (teacher review / instructional designer / moderator).
* Logs (session transcripts + action tags) are stored for offline evaluation and product metrics.

Based on interviews with educators, curriculum designers, and product stakeholders, reviewers judge Study Mode outputs on the following dimensions:

1. **Pedagogical fidelity** — Does the assistant follow Study Mode rules (diagnose first, stepwise guidance, avoid direct answer dumps, single-question-per-step, check & reinforce, varied rhythm, recap)?
2. **Accuracy of content** — Are the factual claims/corrections correct and appropriately sourced when needed?
3. **Clarity & cognitive load** — Are explanations chunked, plain-spoken, and appropriately scoped for the learner’s stated level?
4. **Engagement & affect** — Is the tone warm, encouraging, and motivating (not lecture-y or abrasive)?
5. **Personalization** — Did the assistant adapt to learner level/goals and leverage conversation memory correctly?
6. **Safety & policy compliance** — No disallowed content or identity-safety problems; sensitive requests are handled correctly.
7. **Opportunity for learning** — Did the session produce observable learning behaviors (learner attempts, restatements, successful practice rounds)?

Our automation goal is for Study Mode to handle the majority of routine tutoring sessions without human intervention, but escalate for low-confidence, high-stakes, or policy-sensitive cases.  The primary optimization is **maximizing measurable learning outcomes** while **minimizing total human & compute cost**.

We will therefore focus on reducing the total tutoring cost, which depends on:

1. **Per-session compute cost** — how much it costs to run Study Mode (model size / #calls / tool use) per session.
2. **Escalation rate to human QA** — the fraction of sessions or turns sent to teachers / reviewers for correction or safety review.
3. **Human review cost per escalated item** — time and hourly cost of teachers, instructional designers, or moderators.
4. **Cost of mistakes (learning risk)** — the downstream impact when the system gives incorrect or misleading instruction (relearning time, student frustration, reputational risk).
5. **Engineering & integration cost** — cost to build, version, and maintain the Study Mode overlay, eval tooling, dashboards, and any dataset curation required.
6. **Business impact of pedagogical failures / successes** — measurable product KPIs such as retention, lesson completion, conversion to paid tiers, NPS, or institutional adoption (schools, teachers).

**Operational assumptions & constraints**

* Study Mode is implemented initially as a system prompt overlay applied to an existing base LLM (not yet retrained into the model).
* We can log full transcripts and instrument action tags (diagnose, micro\_explain, guide\_question, confirm\_then\_push, check\_reinforce, practice\_round, vary\_rhythm, recap\_summary).
* There is a human-in-the-loop review pipeline available for escalations and for periodic rubric calibration.
* Privacy/safety: learner PII must be redacted before human review; model outputs must adhere to content policy and curricular constraints.
* Evaluation must be reproducible and auditable: every session produces a deterministic artifact (transcript + heuristic tags + heuristic evidence) for offline analysis.

**Success criteria (example KPIs)**

* **Pedagogical fidelity ≥ X%** (measured by automated heuristics + spot human rubric sampling).
* **Escalation rate ≤ Y%** while maintaining **learning outcome delta ≥ Z** (e.g., students who use Study Mode show higher correct recall on quick checks).
* **Per-session cost below budget** (compute + expected human review cost), or a favorable cost / outcome ratio versus baseline tutoring alternatives.
* **Low incidence of critical mistakes** (safety/factual errors that would require intervention).

**What we will measure and iterate on**

1. Operationalize the 7–8 action tags into deterministic heuristics and LLM-judge fallbacks.
2. Build a starter seed set (Python & prompt-engineering lessons; later expand to other domains) and baseline runs comparing:

   * Base LLM without Study Mode overlay
   * LLM + Study Mode overlay (automated)
   * Human tutor (gold standard)
3. Compute per-session metrics: heuristic pass/fail vector, pedagogical fidelity score, escalation flag, and human rubric score (sampled).
4. Triage failures into a clear taxonomy (answered too early, multi-question overload, no diagnosis, lecture mode, no reinforcement, over-scaffolding, safety slip) to drive prompt and policy fixes.

With this problem statement, the next practical steps are: produce the seed session JSONs, implement the heuristic evaluator, run an A/B baseline (base vs study overlay), and collect human rubric labels to validate and calibrate the heuristics.
