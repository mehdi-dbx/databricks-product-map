#!/bin/bash
cd /Users/mehdi.lamrani/code/Report/AmadeusAI/.swarm/illus-hunt

# Fetch documentation pages and extract images
echo "Fetching docs pages..."

# 2.2: Lakeflow pipelines fan-in-fan-out
curl -sL "https://docs.databricks.com/aws/en/data-engineering/fan-in-fan-out" -o /tmp/doc_2_2.html
grep -oE '/aws/en/assets/images/[^" >]+' /tmp/doc_2_2.html | head -3 > /tmp/imgs_2_2.txt
echo "Found $(wc -l < /tmp/imgs_2_2.txt) images in Lakeflow doc"

# 2.3: Lakebase documentation
curl -sL "https://docs.databricks.com/aws/en/admin/system-tables/lakebase" -o /tmp/doc_2_3.html
grep -oE '/aws/en/assets/images/[^" >]+' /tmp/doc_2_3.html | head -3 > /tmp/imgs_2_3.txt
echo "Found $(wc -l < /tmp/imgs_2_3.txt) images in Lakebase doc"

# 2.4: Real-time analytics
curl -sL "https://docs.databricks.com/aws/en/compute/sql-warehouse/real-time" -o /tmp/doc_2_4.html
grep -oE '/aws/en/assets/images/[^" >]+' /tmp/doc_2_4.html | head -3 > /tmp/imgs_2_4.txt
echo "Found $(wc -l < /tmp/imgs_2_4.txt) images in Real-time doc"

# 2.5: Data quality  
curl -sL "https://docs.databricks.com/aws/en/admin/system-tables/data-quality-monitoring" -o /tmp/doc_2_5.html
grep -oE '/aws/en/assets/images/[^" >]+' /tmp/doc_2_5.html | head -3 > /tmp/imgs_2_5.txt
echo "Found $(wc -l < /tmp/imgs_2_5.txt) images in Data quality doc"

# Download images
echo ""
echo "Downloading images from docs..."

i=1
while read img_path; do
  url="https://docs.databricks.com$img_path"
  filename="docs_2_2_$i.png"
  echo "Downloading: $url → $filename"
  curl -sL "$url" -o "dl-ch02/$filename" &
  sleep 1
  i=$((i+1))
done < /tmp/imgs_2_2.txt

# Similar for other points...
wait

echo "Done!"
