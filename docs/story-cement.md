# Story cement

These are the instructions for writing the complete story that holds the 11 chapters of the Story tab together. Follow them exactly.

The slides carry the detail of each product. This text carries what the slides cannot: why each chapter comes after the previous one, and how the whole thing forms one story.

- **The story:** that of any large organization that faces AI. It tells no specific case and invents no scene.
- **The products are the core.** Each chapter paragraph names its products as the answer to the challenge of that stage.
- **Audience:** tech C-level, architects, Heads of Data and AI. Use plain words.

## Conduct

- Act only on an explicit request.
- Before each step, say in French, in one line, what you are about to do.
- Write the story in English, and talk in French.
- Do not ask about anything these instructions already settle.

## Inputs

Read these before writing:

1. `docs/story-notes.md`:
   - the M0 Spine, which gives the thread of the whole story and the chain of questions between chapters;
   - for each chapter, its "Receives" and "Hands off" lines;
   - the points of chapter 1 and the Check M1 block, which maps each point to the chapters that answer it. This map is the loop that the ending closes.
2. `app/src/story.json`: the chapters in order, their titles, their points and the handoff of each chapter.
3. For each chapter, the names of the capsules its points cite. This is how the products are named.

## Keep exactly as it is

- the chapters, their order and their titles
- the question that closes each chapter: the last sentence of its handoff in `story.json`, word for word

## Structure

**Title.** One line.

**Opening.** It covers chapter 1 in one paragraph:

- the starting situation of any large organization, as a synthesis of the points of chapter 1, in their order. Each point is one group of pains, and the groups follow the chapters that answer them.

It ends with the question of chapter 1's handoff.

**One paragraph per chapter, from 2 to 11.** Put the chapter number and title before each paragraph, for example **2. Data and AI foundation**. Each paragraph has 4 or 5 sentences, in this order:

1. Pick up the question the previous paragraph ended on. Do not repeat it word for word.
2. State the challenge the organization faces at this stage.
3. Name the chapter's products as the answer. Give no detail: the slides carry it.
4. Say what this changes for the organization.
5. End on the question of the chapter's handoff, word for word. Chapter 11 has no handoff, so its paragraph leads into the closing.

**Closing.** One paragraph that goes back to the situation of the opening. For each point of chapter 1, it names the chapter that answers it, using the map in Check M1.

**Length.** About 1,000 words, which takes about 6 minutes to tell. Name the products that carry each chapter's answer, not all of them. The first run named four to six products per chapter and came to 1,104 words.

## Do not write

- a scene, a character or an example company
- a number or a fact that is not in `docs/story-notes.md`, `app/src/story.json` or the capsules
- a product that the chapter's points do not cite
- exaggeration
- slogans, taglines, refrains, or formulas such as "One set of rules: …"
- jargon a C-level reader would not know, unless you explain it

## Checks before showing it

- Run the next two checks with a script, not by eye.
- Every chapter from 2 to 11 has its paragraph, in order, under its current title.
- Every paragraph ends on its handoff question, word for word. Chapter 11 is the exception.
- Every product named in a paragraph is cited by one of that chapter's points.
- The closing goes back to every point of chapter 1, each with its chapter from the Check M1 map.
- Read the text straight through. Each paragraph follows from the one before.
- Check each sentence against "Do not write".

## Output

1. Show the full text in the chat for review.
2. Wait for the verdict. For a rejected passage, rewrite only that passage, from the comment.
3. Add it at the end of `docs/story-notes.md` as section `## M15 — The complete story`, in four kinds of blocks: `**Title:** …`, `**Opening.**`, `**Chapter N.**` for chapters 2 to 11, and `**Closing.**`, each followed by its paragraph.
   - `scripts/story_extract.py` reads the section into `app/src/story.json`: `thread` gets the title, opening and closing, and each chapter gets its `intro`.
   - The Story tab shows the title and the opening at the top, each chapter's paragraph under the chapter's heading, and the closing after chapter 11, with a "Closing" entry in the chapter list. The Story search covers all of them.
   - Run `python3 scripts/story_extract.py`, then `python3 app/build.py`.
