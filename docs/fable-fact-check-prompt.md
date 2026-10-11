# Prompt — fact check against official Databricks documentation

Attach `app/src/ai-tree.json`, `app/src/ds-tree.json` and `app/src/story.json`, then
paste the prompt below.

---

These three files hold the content of an internal Databricks field app. Field engineers
use it to present Databricks data science and AI capabilities to customers.

- `ai-tree.json` and `ds-tree.json` are trees of products and features. Each node has a
  name (`n`), a one-sentence description (`note`), a status (`s`: GA, PuP = public
  preview, Beta, PrivPreview, Announced, Legacy), and on some nodes `solves` rows
  (problem → solution) and doc links.
- `story.json` is a narrative of 11 chapters. Its slides have a title, a lead sentence
  and bullets, and they reference tree nodes by path.

I only want one thing checked: whether the facts are true according to Databricks'
official public documentation. That means docs.databricks.com, release notes, and
databricks.com product pages and blog. Ignore style, structure and wording unless the
wording makes a statement false.

Use your judgment on what to check and how. Product names, statuses, capabilities,
figures and dates are the likely places for errors. Many facts here are recent
(September and October 2026). Some come from internal or preview material that public
docs may not cover yet.

**HARD RULE: WEB SEARCH IS MANDATORY. YOU MUST SEARCH THE WEB AND OPEN THE OFFICIAL
PAGES TO CHECK EVERY CLAIM. THIS RULE IS ABSOLUTE.**

**ANY USE OF MEMORY WITHOUT A SOURCE IS PROHIBITED.** Every verdict must rest on a public
source that you cite. If you find no public source that confirms or refutes a claim,
mark it `unverifiable`.

## Output

Return one JSON array, and nothing else after it. Each item is one claim you checked:
claims you confirmed as correct, and claims that are wrong, outdated, or that you could
not confirm.

```json
{
  "file": "ai-tree.json | ds-tree.json | story.json",
  "path": ["Databricks AI", "Governance for AI", "Unity Gateway"],
  "story": {"chapter": 7, "point": "7.2", "part": "title | lead | bullet", "bullet": 0},
  "field": "n | note | s | solves[2].solution | docs | ...",
  "current": "exact current text",
  "verdict": "correct | wrong | outdated | unverifiable",
  "correct": "exact replacement text; empty when the verdict is correct or the right value is unknown",
  "source": "URL of the public page that supports the verdict (empty only for unverifiable)",
  "why": "one sentence"
}
```

- For a tree node, use `path`, the list of names from the root to the node, exactly as
  in the file. Omit `story`.
- For a Story slide, use `story` and omit `path`. `point` is the slide `id`. `bullet` is
  the 0-based index in `bullets`.
- `current` must be copied exactly from the file. I use it to find and replace the text.
