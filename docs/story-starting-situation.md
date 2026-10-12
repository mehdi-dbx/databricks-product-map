# Story starting situation

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
   - **Title:** the challenge, in plain words.
   - **Text:** 2 to 4 sentences that synthesize the group's pains. Name no product: the products come in the later chapters. The point cites no capsule.
   - Start from the two current points, 1.1 and 1.2. Keep their sentences unless the synthesis already says the same thing. List every sentence you drop or change.
   - Write a link sentence between consecutive points, as the other chapters do, with `↳ **Link 1.k → 1.k+1 (reason).**`.
   - Keep the chapter's title and its "Hands off" line word for word. Chapter 2 receives it.
   - Repeat no lead and no bullet of a later chapter, even in other words. Chapter 1 announces each problem in its own words, and the later chapters give the detail. In the first run, a sentence of 1.2 copied the lead of 3.2 and had to be reworded.
3. Follow the same rules as the rest of the Story:
   - no scene, character or example company;
   - no number or fact that is not in the pains;
   - no exaggeration;
   - no slogans, taglines, refrains, or formulas such as "One set of rules: …";
   - no jargon that a C-level reader would not know, unless you explain it.

## Step 4 — Update the Story

1. Copy the notes: `cp docs/story-notes.md /tmp/story-notes.before.md`.
2. In `docs/story-notes.md`, section `## M1 — Chapter 1. Challenges`:
   - Replace the points and their links with the new ones.
   - Keep the "Receives" and "Hands off" lines as they are.
   - Rewrite the Check M1 block. For each point, give the chapters that answer its group and the pains that its sentences rest on, by capsule. Then the ending can close the loop.
3. Run `python3 scripts/story_extract.py`, then `python3 app/build.py`.
4. Update `docs/story-cement.md`. It relies on "the four obstacles of point 1.2" in its inputs, its opening, its closing and its checks. Make it rely on the points of the new chapter 1 and on the mapping in Check M1.

## Checks before showing it

- `docs/story-pains.md` has all 59 capsule references, and its counts are right.
- Every pain in `docs/story-pains.md` belongs to one group, and every group leads to at least one chapter.
- Every sentence of the new chapter 1 rests on pains listed in Check M1.
- Compare each sentence of the new chapter 1 with the leads and bullets of chapters 2–11, by script. Reword every sentence that comes too close.
- Outside section M1, `diff /tmp/story-notes.before.md docs/story-notes.md` shows no change.
- The extractor and the build run without errors.

## Output

1. Show this in the chat:
   - the counts from steps 1 and 2;
   - the groups, with their pains and their chapters;
   - the new chapter 1, point by point, laid out as slides;
   - the dropped or changed sentences of points 1.1 and 1.2;
   - the link to the local `ai-tree-mindmap.html`, Story tab.
2. Wait for the verdict. For a rejected passage, rewrite only that passage, from the comment, then go back to step 4.
