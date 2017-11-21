from house_listing_filter import filter_queue, filter_queue_client

import traceback
import time
import sys


if __name__ == "__main__":

    SLEEP_TIME_BETWEEN_LOOP_IN_SECONDS = 60 * 10

    while True:
        print("{}: Starting filtering cycle".format(time.ctime()))

        try:
            filter_queue()
        except KeyboardInterrupt:
            print("Exiting Filtering...")
            sys.exit(1)
        except Exception as exc:
            print("Error with the filtering:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished filtering".format(time.ctime()))
        filter_queue_client(SLEEP_TIME_BETWEEN_LOOP_IN_SECONDS)

