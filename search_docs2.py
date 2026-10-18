#!/usr/bin/env python3
import json

search_terms = {
    "2.1": ["delta", "lakehouse", "transaction"],
    "2.2": ["lakeflow", "ingestion", "pipeline", "dlt"],
    "2.3": ["lakebase", "postgres", "vector", "search"],
    "2.4": ["lakehouse rt", "real-time", "operational"],
    "2.5": ["unity catalog", "data quality", "classification", "anomaly"],
}

with open('/Users/mehdi.lamrani/code/AIFeatureMap/run/docs-inventory/pages.json') as f:
    full_data = json.load(f)

pages = full_data.get('pages', [])

results = {k: [] for k in search_terms}

for page in pages:
    path = page.get('path', '').lower()
    title = (page.get('title', '') or '').lower()

    for point, terms in search_terms.items():
        for term in terms:
            if term in path or term in title:
                if len(results[point]) < 4:
                    results[point].append({
                        'path': page['path'],
                        'title': page['title'],
                        'area': page.get('area', ''),
                    })
                break

# Print results
for point in sorted(results.keys()):
    print(f"\n=== POINT {point} ===")
    for page in results[point]:
        print(f"  {page['title']}")
        print(f"    {page['path'][:60]}")
