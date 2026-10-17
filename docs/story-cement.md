# Story cement

These are the instructions for writing the text that sits between the slides of the Story tab: the intro of each chapter. Follow them exactly.

The plan, `docs/feature-tree.md`, sets the chapters, their order and their slides. It opens with the platform architecture and goes straight to the features. The order is the order of dependency: a chapter only uses what earlier chapters introduced.

- **Audience:** tech C-level, architects, Heads of Data and AI. Use plain words.
- **The products are the core.** An intro says what the chapter covers and what it builds on. The slides carry the detail.

## Conduct

- Act only on an explicit request.
- Before each step, say in French, in one line, what you are about to do.
- Write the Story in English, and talk in French.
- Do not ask about anything these instructions already settle.

## Inputs

1. `docs/feature-tree.md`: the chapters and their slides, in order.
2. `app/src/story.json`: for each chapter, the titles and the bullets of its slides.

## What to write

- **Intro of each chapter**, in its `intro`: two or three sentences, one per bullet. Name what the chapter covers, in the plan's order, and what it builds on from the earlier chapters.
- **Handoff:** none. Each chapter's `handoff` stays `""`. The v1 chain of questions between chapters is gone with the plan's v2.
- **Opening and closing:** none. `thread.opening` and `thread.closing` stay `[]`. The overview, the platform architecture, is the first slide, and the appendix, the capability map, is the last.

## Do not write

- a question, a hook or a pitch, such as "How do you get it into one place?"
- a problem framing of the kind the plan dropped, such as "Why AI stalls before production"
- a scene, a character or an example company
- a number or a fact that is not in the chapter's slides
- a product that the chapter's slides do not name
- slogans, taglines, refrains, or formulas such as "One set of rules: …"
- a sentence about the deck itself, such as "This section covers…"

## Output

1. Copy the file: `cp app/src/story.json /tmp/story.before.json`.
2. Write the intros into `app/src/story.json`.
3. Run `python3 scripts/story_check.py --diff /tmp/story.before.json`, then `python3 app/build.py` and `python3 scripts/story_pdf.py`.
4. Show the intros in the chat, chapter by chapter.
