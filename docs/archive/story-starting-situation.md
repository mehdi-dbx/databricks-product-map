# Story starting situation

> **Archived on 2026-10-17.** The Story follows the plan in `docs/feature-tree.md` (v2), which has no "Challenges" chapter: it opens with the platform architecture and goes straight to the features. This file describes chapter 1 of v1. No script reads it.

These are the instructions for rewriting the starting situation of the Story, chapter 1 "Challenges", as a complete synthesis of the pains that the Story solves, and then for updating the Story with it. Follow them exactly.

Today, chapter 1 states two problems: data spread across systems, and AI pilots blocked before production. That is too thin. The Story solves far more, and the opening must show all of it, so that each chapter then answers part of the situation.

- **The story:** that of any large organization that faces AI. It tells no specific case and invents no scene.
- **Audience:** tech C-level, architects, Heads of Data and AI. Use plain words.

## Conduct

- Act only on an explicit request.
- Before each step, say in French, in one line, what you are about to do.
- Write the Story in English, and talk in French.
- Do not ask about anything these instructions already settle.

## Step 1 — Inventory

List every chapter of the Story and every capsule that its points cite. Take the chapters and the `refs` from `app/src/story.json`, and the capsules from `app/src/ai-tree.json` and `app/src/ds-tree.json`.

Generate the list with a short script so that nothing is missed. Check the counts: 11 chapters, 40 points, 59 capsule references.

## Step 2 — Pains

For each capsule, list the pains it solves: the `problem` of each of its `solves` rows, word for word.

- If a capsule has no `solves` rows, mark it "no pains in the tree". Do not invent any.
- For each chapter, the pains are those of its capsules.

Write steps 1 and 2 to `docs/story-pains.md`, chapter by chapter and then capsule by capsule. Give the counts of capsules, of pains, and of capsules without pains.

## Step 3 — Synthesis

1. Group the pains into the challenges that a large organization faces with data and AI. For each group, say:
   - who has it: business users, data teams, developers, security, the organization;
   - what it costs.

   Use only the wording of the pains. Order the groups like the chapters that solve them, so that the opening announces the Story in order.
2. Write the new chapter 1, with one point per group:
   - **Title:** the challenge, in plain words. Keep it short and synthetic, with one idea and no list of notions. See the "Title" section of `docs/story-editorial-guide.md`: chapter 1 is its only exception, since its titles name no product.
     - The audience is technical. Write a label of two to four words that names the problem directly, such as "Fragmented data", "Model provider sprawl", "Unsafe agent access" or "Pilots stuck before production".
     - Write no sentence and no styled phrase. "AI pilots do not make it to Production", "Every model provider handled separately" and "Data spread across systems" are too long.
     - Use no relative clause, as in "Agents that cannot reach data and tools safely", and no vague verb, as in "Business users and developers held back".
   - **Text:** 2 to 5 short sentences that synthesize the group's pains, one fact each, with its key phrase in bold as `**…**`. Go straight to the problem: no setup sentence such as "Most companies already run analytics and have started with AI.", and keep each link sentence to one short line. Name no product in the text: the products come in the later chapters. The point cites, in its `refs`, the capsules whose pains its sentences rest on. Drop a capsule whose sentence was dropped.
   - Start from the two current points, 1.1 and 1.2. Keep their sentences unless the synthesis already says the same thing. List every sentence you drop or change.
   - Write a link sentence between consecutive points, as the other chapters do. It is the `lead` of the next point.
   - Keep the chapter's `title` and `handoff` word for word. Chapter 2 receives the handoff.
   - Repeat no lead and no bullet of a later chapter, even in other words. Chapter 1 announces each problem in its own words, and the later chapters give the detail. In the first run, a sentence of 1.2 copied the lead of 3.2 and had to be reworded.
3. Follow the same rules as the rest of the Story:
   - no scene, character or example company;
   - no number or fact that is not in the pains;
   - no exaggeration;
   - no slogans, taglines, refrains, or formulas such as "One set of rules: …";
   - no jargon that a C-level reader would not know, unless you explain it;
   - no term repeated from one sentence to the next, when a pronoun or another word would do;
   - one claim per sentence. Join two clauses only when the second follows from the first. A sentence of three clauses, such as "Token spend grows without warning, calls to outside models go unaudited, and relying on a single vendor creates lock-in.", is split;
   - no mirrored clauses, such as "nobody sees which step failed, and nobody measures its quality" or "the people who use data and AI every day, and those who build with it";
   - no setup line that contrasts two things, such as "A model on its own only answers.".

## Step 4 — Update the Story

1. Copy the file: `cp app/src/story.json /tmp/story.before.json`.
2. In `app/src/story.json`, chapter 1 (the first entry of `chapters`):
   - Replace its points. Each one has its `title`, its `lead` (the link sentence from the previous point, empty for 1.1), its `bullets` and its `refs`. Its `effect`, `challenge` and `pivot` stay empty.
   - Keep the chapter's `title` and `handoff` as they are.
3. In `docs/story-cement.md`, update the map from each point of chapter 1 to the chapters that answer it. Then the ending can close the loop.
4. Run `python3 scripts/story_check.py --diff /tmp/story.before.json`, then `python3 app/build.py`.
5. If the opening or the closing of the complete story no longer matches chapter 1, follow `docs/story-cement.md` to update them.

## Checks before showing it

- `docs/story-pains.md` has all 59 capsule references, and its counts are right.
- Every pain in `docs/story-pains.md` belongs to one group, and every group leads to at least one chapter.
- Every sentence of the new chapter 1 rests on pains of the capsules in its point's `refs`, as listed in `docs/story-pains.md`.
- Compare each sentence of the new chapter 1 with the leads and bullets of chapters 2–11, by script. Reword every sentence that comes too close.
- The diff of `story_check.py` lists changes in chapter 1 only (`story.chapters[0]`).
- The check and the build run without errors.

## Output

1. Show this in the chat:
   - the counts from steps 1 and 2;
   - the groups, with their pains and their chapters;
   - the new chapter 1, point by point, laid out as slides;
   - the dropped or changed sentences of points 1.1 and 1.2;
   - the link to the local `ai-tree-mindmap.html`, Story tab.
2. Wait for the verdict. For a rejected passage, rewrite only that passage, from the comment, then go back to step 4.
