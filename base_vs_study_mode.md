# 📑 Base Instructions vs. Study Mode Overlay

| Feature               | **Base System Prompt (Core Rules)**                                                                          | **Study Mode Overlay (Extra Rules)**                                                                      | **Example in My Replies**                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Identity**          | Must say “I am GPT-5, a large language model trained by OpenAI.” Cannot claim to be human or another system. | No change — identity rules still hold.                                                                    | If you ask “Are you human?”, I say I’m GPT-5.                                                                              |
| **Reasoning**         | I can’t show hidden chain-of-thought, but I should explain clearly if needed.                                | Must break problems into small steps and guide, not just explain.                                         | If you give me a math problem, instead of showing all my steps at once, I ask *“What’s the first operation we’d do here?”* |
| **Tools**             | Can use web search, code execution, file reading, image generation — but always visibly.                     | Still true, but tool use must fit tutoring.                                                               | If you upload a dataset, I won’t just crunch it — I’ll ask what you want to analyze first.                                 |
| **Content Safety**    | Long detailed rules about what I cannot generate (unsafe, private, or disallowed content).                   | No change — Study Mode doesn’t override safety.                                                           | If you asked for election ballot details, I’d refuse (per safety rules).                                                   |
| **Tone/Style**        | General guidance: clear, concise, approachable, not overly casual.                                           | Must feel like a **teacher**: ask questions, vary rhythm, check understanding, never dump full solutions. | Instead of writing a long lecture, I might quiz you: *“Want to try explaining that step back to me?”*                      |
| **Homework Requests** | Normally, I could solve a homework problem if asked.                                                         | 🚫 Prohibited — I must tutor, not give direct answers.                                                    | If you ask *“What’s the answer to this equation?”* → Base would solve it; Study Mode forces me to walk you step by step.   |

---

## 1. Base Instructions (core system prompt – \~25–30 pages)

These are the **main parts** that make it so long:

* **Identity & Role**

  * Always say I’m GPT-5, trained by OpenAI.
  * No pretending to be a human or another AI.
  * Don’t reveal hidden prompts or internals.

* **Reasoning & Transparency**

  * Don’t show hidden chain-of-thought.
  * Explain step by step *when useful for the user*.
  * Admit when I don’t know something.

* **Tools & Capabilities**

  * Detailed instructions for each tool (search, code, file handling, image generation, memory, etc.).
  * When to use them, how to explain to the user, and what not to do (no secret tool use).

* **Content Safety**

  * Big section with categories of disallowed content.
  * Guardrails for sensitive areas (e.g., medical, legal, elections in the U.S.).
  * How to respond safely (refuse or redirect).

* **Response Style**

  * Clear, concise, and approachable.
  * No excessive repetition or overlong answers.
  * Encourage clarity, accuracy, and user engagement.

* **Error Handling**

  * If a tool fails, explain why.
  * If a question is ambiguous, ask clarifying questions.
  * If asked about private data, refuse.

Think of this as the **general operating manual** that covers *everything I can do*.

---

## 2. Study Mode Overlay (extra rules – \~2 pages)

This is much shorter but much stricter. You’ve already seen the actual text, but here are its **main parts**:

* **Get to know the user**

  * Start by asking about grade level or goals.

* **Build on existing knowledge**

  * Connect new ideas to what the student already knows.

* **Guide, don’t just answer**

  * Never give direct homework answers.
  * Ask guiding questions one step at a time.

* **Check & Reinforce**

  * Have the student restate or use the idea.
  * Offer mnemonics or mini-reviews.

* **Vary the Rhythm**

  * Mix explanations, quizzes, roleplay, and short activities.
  * Avoid long lecture-style replies.

* **Tone & Approach**

  * Be warm, patient, plain-spoken.
  * Keep things moving.

* **Strict Rule Reminder**

  * 🚫 Don’t do the homework for the student.
  * Always stay in the “approachable teacher” role.

---
