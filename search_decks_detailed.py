#!/usr/bin/env python3
import json

# More specific search terms per point
point_queries = {
    "2.1": [
        ("Delta Lake", ["delta", "transaction", "acidity", "acid", "version control"]),
        ("Lakehouse", ["lakehouse", "open format"]),
    ],
    "2.2": [
        ("Lakeflow/DLT", ["lakeflow", "dlt", "pipeline", "ingestion", "declarative"]),
        ("Predictive Optimization", ["predictive optim"]),
    ],
    "2.3": [
        ("Lakebase", ["lakebase", "serverless postgres", "sql database"]),
        ("Vector Search", ["vector search", "lakebase search", "embedding"]),
    ],
    "2.4": [
        ("Lakehouse//RT", ["lakehouse rt", "real-time", "millisecond", "operational", "ltap"]),
    ],
    "2.5": [
        ("Unity Catalog", ["unity catalog", "uc integration"]),
        ("Data Quality", ["data quality", "profiling", "classification", "anomaly", "pii", "monitoring"]),
    ],
}

results_by_point = {k: {} for k in point_queries.keys()}

with open('/Users/mehdi.lamrani/code/Report/AmadeusAI/.swarm/illus-hunt/deck-index.jsonl') as f:
    for line in f:
        slide = json.loads(line)
        text = (slide.get('text', '') or '').lower()

        if slide.get('images', 0) == 0 or slide.get('deprecated', False):
            continue

        # Match against queries
        for point, queries in point_queries.items():
            for query_name, terms in queries:
                for term in terms:
                    if term.lower() in text:
                        key = query_name
                        if key not in results_by_point[point]:
                            results_by_point[point][key] = []

                        if len(results_by_point[point][key]) < 3:  # Max 3 per query
                            results_by_point[point][key].append({
                                'deck': slide['deck'],
                                'deck_id': slide['deck_id'],
                                'slide': slide['slide'],
                                'images': slide['images'],
                                'text_preview': text[:150],
                                'match_term': term,
                            })
                        break

# Print results
for point in sorted(results_by_point.keys()):
    print(f"\n=== POINT {point} ===")
    for query_name, slides in results_by_point[point].items():
        print(f"\n  {query_name}: {len(slides)} slides")
        for s in slides[:2]:
            print(f"    - {s['deck']} / slide {s['slide']} ({s['images']} images)")
            print(f"      deck_id={s['deck_id']}, match: {s['match_term']}")
            print(f"      {s['text_preview'][:80]}...")
