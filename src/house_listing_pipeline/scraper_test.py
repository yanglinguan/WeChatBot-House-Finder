from scraper import scrape, do_scrape, redis_client, cloudAMQP_client

import pickle

def test_scrape():
    print "start test"
    city = "toronto"
    area = "tor"
    filters = {
            "max_price": 1500,
            "min_price": 500,
            "min_bedrooms": 1,
            "max_bedrooms": 1,
            "private_bath": True,
            }
    category = "apa"

    result = scrape(city, area, category, filters, "1")

    print result;

def test_do_scrape():
    redis_client.rpush("client_list", "1")

    client_request = {
            "city": "toronto",
            "area": ["tor"],
            "category": ["apa", "roo"],
            "max_price": 1500,
            "min_price": 500,
            "min_bedrooms": 1,
            "max_bedrooms": 1,
            "private_bath": True,
            "request_id": "1",
            "active": True,
            }

    client_request_table = {"1": client_request}
    redis_client.set("1", pickle.dumps(client_request_table))

    do_scrape()

    cloudAMQP_client.getMessage()



if __name__ == "__main__":
    #test_scrape()
    test_do_scrape()

