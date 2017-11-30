from house_listing_deduper import dedup_queue_client, dedup

import traceback
import time
import sys


if __name__ == "__main__":

    SLEEP_TIME_BETWEEN_LOOP_IN_SECONDS = 10

    while True:
        print("{}: Starting deduping cycle".format(time.ctime()))

        try:
            dedup()
        except KeyboardInterrupt:
            print("Exiting Deduping...")
            sys.exit(1)
        except Exception as exc:
            print("Error with the deduping:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print("{}: Successfully finished deduping".format(time.ctime()))
        dedup_queue_client.sleep(SLEEP_TIME_BETWEEN_LOOP_IN_SECONDS)

