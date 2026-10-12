# Judge s03

**Status:** RUNNING

## Timeline

### Sheets viewed (all 13 sheets)
- 3.1: sheets 1-5 viewed (39 tiles total; 4 candidates + 25 docs + 10 deck)
- 3.2: sheets 1-3 viewed (25 tiles total; 3 candidates + 12 docs + 10 deck)
- 3.3: sheets 1-3 viewed (25 tiles total; 4 candidates + 11 docs + 10 deck)
- 3.4: sheets 1-2 viewed (18 tiles total; 3 candidates + 5 docs + 10 deck)

### Assessment process
All 13 contact sheets reviewed thoroughly. Quality bar applied: rejected text-heavy, blurry, deprecated, and off-topic tiles. Prioritized candidates, then best docs images, then key deck diagrams.

### Final selections: 23 tiles total
- **3.1** (5 tiles): All 4 candidates + 1 best docs image
  - Tiles: 1, 2, 3, 4, 12
  - Mix: 4 screenshots (notebook features) + 1 screenshot (data profile detail)
  
- **3.2** (6 tiles): All 3 candidates + 3 supporting tiles
  - Tiles: 1, 2, 3, 9, 14, 20
  - Mix: 3 screenshots (UI/governance) + 2 diagrams (architecture) + 1 diagram (point-in-time)
  
- **3.3** (6 tiles): All 4 candidates + 2 supporting tiles
  - Tiles: 1, 2, 3, 4, 17, 23
  - Mix: 4 screenshots (AutoML UI/flow) + 2 diagrams (lifecycle)
  
- **3.4** (6 tiles): All 3 candidates + 3 supporting tiles
  - Tiles: 2, 3, 6, 10, 14, 16
  - Mix: 3 diagrams (architecture/comparison) + 3 screenshots (GPU/CLI)

### File processing
- Copied 9 non-candidate images to app/static/img/ with slug naming
- All images checked for size (none exceeded 1800px)
- All files verified in app/static/img/

### Exclusions
- 3.1 #37 (deprecated collaborative notebooks slide) — marked deprecated
- Most architecture diagrams #30-36 (3.1) — not directly about notebooks
- Text-heavy docs pages #10, #11 (3.3-2) — blurry/too small
- Fine-tuning slides (multiple) — belongs to chapter 4

## Summary

**Status:** DONE

**Total tiles kept:** 23 (5 for 3.1, 6 for 3.2, 6 for 3.3, 6 for 3.4)

**Quality metrics:**
- All kept tiles show what the point describes (no off-topic content)
- Visual mix: 13 screenshots + 10 diagrams (balanced)
- All candidate images retained (they were pre-vetted, high-quality)
- Supporting images hand-selected for complementary coverage

**Output files:**
- `.swarm/illus-hunt/final-ch03.json` — complete selection with metadata
- `app/static/img/` — all 23 image files ready for use
  - 13 existing candidates (untouched)
  - 9 newly copied from docs/deck sources

**Key coverage:**
- 3.1: Notebook interface, data exploration, multi-language support, visualization tools
- 3.2: Feature Store UI, governance, serving APIs, point-in-time joins, end-to-end architecture
- 3.3: AutoML glass-box UI, MLflow tracking, roadmap, full lifecycle diagram
- 3.4: AI Runtime serverless GPUs, hardware options, distributed training, CLI submission

