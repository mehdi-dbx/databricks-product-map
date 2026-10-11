# Agent Apps Deploy Log

**Mission:** Publish existing single-file HTML (`ai-tree-mindmap.html`) as a Databricks App. Scaffold minimal static-serving app, do read-only deploy prep, STOP before any provisioning/publish.
**Start:** 2026-10-07 09:30:57 CEST

---

[step 1 | 09:30:57] ATTEMPT: get timestamp + stat source HTML — cmd=date, ls, wc
[step 1 | 09:30:57] RESULT: ok — source exists, 25814 bytes, 404 lines

[step 2 | 09:31] ATTEMPT: inspect HTML — tool=Read ai-tree-mindmap.html
[step 2 | 09:31] RESULT: ok — self-contained static HTML/CSS/JS; only ext dep = Google Fonts CDN + inline data-URI favicon; no build needed
[step 3 | 09:31] ATTEMPT: scaffold app dir, copy HTML to static/index.html — tool=mkdir/cp
[step 3 | 09:31] RESULT: ok — /app/static/index.html (25814 bytes)
[step 4 | 09:31] ATTEMPT: check CLI version + auth profiles — cmd=databricks --version / auth profiles
[step 4 | 09:31] RESULT: ok — CLI v1.18.0; most profiles Valid=NO (expired); Valid=YES: ug-oauth(ai_devtools), latecoere, fevm-databricks-cursor; amadeus/airops profiles expired
[step 5 | 09:32] ATTEMPT: write scaffold files app.yaml/app.py/requirements.txt/.gitignore — tool=Write
[step 5 | 09:32] RESULT: ok — 4 files written

[step 6 | 09:33] ATTEMPT: verify identity on valid profiles — cmd=databricks current-user me -p {latecoere,fevm-databricks-cursor}
[step 6 | 09:33] RESULT: ok — both active as mehdi.lamrani@databricks.com
[step 7 | 09:33] ATTEMPT: confirm Apps enabled — cmd=databricks apps list -p {fevm-databricks-cursor,latecoere}
[step 7 | 09:33] RESULT: ok — both workspaces host apps (fevm-databricks-cursor wsid 7474658581896078; latecoere wsid 2865348338307293)

--- STOP POINT REACHED (no create/deploy/sync executed, per instructions) ---

RECOMMENDED DEPLOY TARGET: profile=fevm-databricks-cursor (clean FE workspace), app=ai-tree-mindmap
Deploy plan (NOT executed):
  P=fevm-databricks-cursor
  databricks sync /Users/mehdi.lamrani/code/Report/AmadeusAI/app /Workspace/Users/mehdi.lamrani@databricks.com/ai-tree-mindmap -p $P
  databricks apps create ai-tree-mindmap -p $P
  databricks apps deploy ai-tree-mindmap --source-code-path /Workspace/Users/mehdi.lamrani@databricks.com/ai-tree-mindmap -p $P

Blocker: intended "amadeus/airops" workspaces are expired. To target one, run:
  databricks auth login -p airops   (host https://fevm-amadeus-airops.cloud.databricks.com)
End: $(date "+%H:%M:%S %Z")
