#!/bin/bash
#service redis start
#service mongod start

#pip install -r requirement.txt

#cd house_listing_pipeline
python ./scrape/scraper_loop.py &
python ./filter/house_listing_filter_loop.py &
python ./deduper/house_listing_deduper_loop.py &

echo "==============================================="
read -p "PRESS [ANY KEY] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)
