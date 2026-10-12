#!/bin/bash
cd /Users/mehdi.lamrani/code/Report/AmadeusAI/.swarm/illus-hunt

# Point 2.1: Delta Lake architecture
echo "Downloading Point 2.1 slides..."
python3 gslides.py thumb 1p-lb7UxBJLcrAIqQ6sIxsyI5-li-Fpy4hqYDUkHCoBI 8 dl-ch02/p2.1-slide1.png || true
sleep 2

# Point 2.2: Lakeflow and transformations  
echo "Downloading Point 2.2 slides..."
python3 gslides.py thumb 1zYbz4UnikZ1yFgBPWZzfwEaQG3hSKpR8UjbhS3cmaBM 70 dl-ch02/p2.2-slide1.png || true
sleep 2

# Point 2.3: Lakebase (Agent Bricks has good diagrams)
echo "Downloading Point 2.3 slides..."
python3 gslides.py thumb 1yHFQN3ZD7PWDnpEInf8nhiToChVn_g5XfTlY98Ls58U 14 dl-ch02/p2.3-slide1.png || true
sleep 2

# Point 2.4: Real-time serving
echo "Downloading Point 2.4 slides..."
python3 gslides.py thumb 1yHFQN3ZD7PWDnpEInf8nhiToChVn_g5XfTlY98Ls58U 19 dl-ch02/p2.4-slide1.png || true
sleep 2
python3 gslides.py thumb 1yHFQN3ZD7PWDnpEInf8nhiToChVn_g5XfTlY98Ls58U 20 dl-ch02/p2.4-slide2.png || true
sleep 2

# Point 2.5: Unity Catalog & Governance
echo "Downloading Point 2.5 slides..."
python3 gslides.py thumb 1yHFQN3ZD7PWDnpEInf8nhiToChVn_g5XfTlY98Ls58U 13 dl-ch02/p2.5-slide1.png || true
sleep 2
python3 gslides.py thumb 1yHFQN3ZD7PWDnpEInf8nhiToChVn_g5XfTlY98Ls58U 50 dl-ch02/p2.5-slide2.png || true

echo "Done!"
