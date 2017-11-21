from scraper import scrape, do_scrape, redis_client

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
            }
    redis_client.set("1", pickle.dumps(client_request))

    do_scrape()



if __name__ == "__main__":
    #test_scrape()
    test_do_scrape()

