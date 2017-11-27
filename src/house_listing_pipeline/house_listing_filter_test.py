from house_listing_filter import handle_message, getTimeToWork, filter_queue, redis_client, gmaps, dedup_queue_client

import pickle

def test_handle_message():
    redis_client.rpush("client_list", "1")

    msg = {"client_id": "1", "request_id": "1"}

    geocode = gmaps.geocode("N2T0A5")

    lat = geocode[0]['geometry']['bounds']['northeast']['lat']
    lon = geocode[0]['geometry']['bounds']['northeast']['lng']
    
    msg['lat'] = lat
    msg['lon'] = lon

    client_request = {
            "work_addr": "University of Waterloo",
            "transit_mode": "driving",
            "departure_to_work": 8,
            "time_to_work": 25 * 60,
            "time_to_work_delta": 5 * 60,
            }

    client_request_table = {"1": client_request}
    redis_client.set("1", pickle.dumps(client_request_table))

    task = handle_message(msg)

    getTask = dedup_queue_client.getMessage()

    print task
    print getTask
    assert task == getTask

    print "pass"


if __name__ == "__main__":
    test_handle_message()
    
