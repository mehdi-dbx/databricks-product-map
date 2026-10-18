#!/usr/bin/env python3
import json
import sys

# Search terms for each point
searches = {
    "2.1": ["Delta Lake", "delta", "open table", "lakehouse storage", "transactions", "schema"],
    "2.2": ["Lakeflow", "DLT", "Data Lifecycle", "ingestion", "transformation", "connector", "predictive optimization"],
    "2.3": ["Lakebase", "serverless postgres", "vector search", "AI Search"],
    "2.4": ["Lakehouse//RT", "real-time", "LTAP", "millisecond", "serving", "operational data"],
    "2.5": ["Unity Catalog", "classification", "profiling", "monitoring", "anomaly detection", "data quality", "PII"],
}

# Read and search the deck index
results = {k: [] for k in searches.keys()}

with open('/Users/mehdi.lamrani/code/AIFeatureMap/.swarm/illus-hunt/deck-index.jsonl') as f:
    for line in f:
        slide = json.loads(line)
        text = (slide.get('text', '') or '').lower()
        deck = slide.get('deck', '')

        # Skip if no images
        if slide.get('images', 0) == 0:
            continue

        # Skip deprecated slides for now
        if slide.get('deprecated', False):
            continue

        # Match against each point's search terms
        for point, terms in searches.items():
            for term in terms:
                if term.lower() in text:
                    results[point].append({
                        'deck': deck,
                        'deck_id': slide['deck_id'],
                        'slide': slide['slide'],
                        'object_id': slide['object_id'],
                        'images': slide['images'],
                        'text': text[:200],
                        'match': term
                    })
                    break  # One match per slide per point

# Print results
for point, slides in results.items():
    print(f"\n=== POINT {point} ({len(slides)} slides) ===")
    for i, s in enumerate(slides[:6]):  # Top 6 per point
        print(f"  {i+1}. {s['deck']} / slide {s['slide']} ({s['images']} images) - match: {s['match']}")
        print(f"     deck_id={s['deck_id']}, object_id={s['object_id']}")
        print(f"     text: {s['text'][:100]}...")
