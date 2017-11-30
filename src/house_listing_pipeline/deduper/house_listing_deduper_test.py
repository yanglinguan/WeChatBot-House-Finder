from house_listing_deduper import handle_message, notification_queue_client, HOUSE_LISTING_TABLE_NAME
import os
import sys
# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import mongodb_client


def test_handle_message():
    msg = {'url': 'https://toronto.craigslist.ca/tor/apa/d/amazing-2-bedroom-condo-in/6396181487.html', "id": 1}

    task = handle_message(msg)

    db = mongodb_client.get_db()

    db_listing = list(db[HOUSE_LISTING_TABLE_NAME].find({'id': 1}))

    db[HOUSE_LISTING_TABLE_NAME].remove({'id': 1})
    queue_listing = notification_queue_client.getMessage()

    assert task['url'] == db_listing[0]['url']
    assert task['id'] == db_listing[0]['id']
    assert task['img_id_hash'] == db_listing[0]['img_id_hash']
    assert task == queue_listing
    print 'pass'

if __name__ == "__main__":
    test_handle_message()

