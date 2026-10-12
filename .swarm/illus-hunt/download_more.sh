#!/bin/bash
cd /Users/mehdi.lamrani/code/Report/AmadeusAI/.swarm/illus-hunt

# More slides for 2.3: Lakebase and Vector Search
echo "Downloading more Point 2.3 (Lakebase & Vector Search)..."
python3 gslides.py thumb 1zYbz4UnikZ1yFgBPWZzfwEaQG3hSKpR8UjbhS3cmaBM 26 dl-ch02/p2.3-vector-search.png || true
sleep 2

python3 gslides.py thumb 1zYbz4UnikZ1yFgBPWZzfwEaQG3hSKpR8UjbhS3cmaBM 85 dl-ch02/p2.3-embedding.png || true
sleep 2

# More slides for 2.4: Real-time analytics
echo "Downloading more Point 2.4 (Real-time)..."
python3 gslides.py thumb 1luYXYZXzb5ut1ebZIMtf6r8h8a9m7AVDTEl4FbIApSY 3 dl-ch02/p2.4-operational.png || true
sleep 2

# More slides for 2.2: Lakeflow/Pipelines
echo "Downloading more Point 2.2 (Lakeflow pipelines)..."
python3 gslides.py thumb 1zYbz4UnikZ1yFgBPWZzfwEaQG3hSKpR8UjbhS3cmaBM 81 dl-ch02/p2.2-lakeflow-ingest.png || true
sleep 2

# Additional architecture diagrams
python3 gslides.py thumb 1p-lb7UxBJLcrAIqQ6sIxsyI5-li-Fpy4hqYDUkHCoBI 12 dl-ch02/p2.4-mosaic-arch.png || true
sleep 2

echo "Done!"
