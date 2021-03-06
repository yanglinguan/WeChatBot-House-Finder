from scraper import do_scrape, cloudAMQP_client

import traceback
import time
import sys


if __name__ == "__main__":
    
    SLEEP_TIME_BETWEEN_LOOP_IN_SECONDS = 10
    
    while True:
        print("{}: Starting scrape cycle".format(time.ctime()))

        try:
            do_scrape()
        except KeyboardInterrupt:
            print("Exiting Scrape...")
            sys.exit(1)
        except Exception as exc:
            print("Error with the scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished scraping".format(time.ctime()))
        cloudAMQP_client.sleep(SLEEP_TIME_BETWEEN_LOOP_IN_SECONDS)
