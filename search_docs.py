#!/usr/bin/env python3
import json

search_terms = {
    "2.1": ["delta lake", "transactions", "schema"],
    "2.2": ["lakeflow", "data ingestion", "dlt", "pipeline", "transformation"],
    "2.3": ["lakebase", "serverless postgres", "vector search"],
    "2.4": ["lakehouse rt", "real-time", "operational", "ltap"],
    "2.5": ["unity catalog", "data quality", "classification", "profiling", "anomaly detection"],
}

results = {k: [] for k in search_terms}

with open('/Users/mehdi.lamrani/code/Report/AmadeusAI/run/docs-inventory/pages.json') as f:
    for line in f:
        page = json.loads(line)
        path = page.get('path', '').lower()
        title = (page.get('title', '') or '').lower()
        label = (page.get('label', '') or '').lower()

        for point, terms in search_terms.items():
            for term in terms:
                if term in path or term in title or term in label:
                    if len(results[point]) < 5:  # Max 5 per point
                        results[point].append({
                            'path': page['path'],
                            'title': page['title'],
                            'area': page.get('area', ''),
                            'match_term': term,
                        })
                    break

# Print results
for point in sorted(results.keys()):
    print(f"\n=== POINT {point} ===")
    for page in results[point][:3]:
        print(f"  {page['title']}")
        print(f"    Path: docs.databricks.com/aws/en/{page['path']}")
        print(f"    Match: {page['match_term']}")
