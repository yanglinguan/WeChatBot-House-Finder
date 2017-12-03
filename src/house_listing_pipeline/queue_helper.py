import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient
config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config", "config.json")
with open(config_path) as config_file:
    json_config = json.load(config_file)

queue_config = json_config["rabbit_mq"]
FILTER_TASK_QUEUE_URL = queue_config["FILTER_TASK_QUEUE_URL"]
FILTER_TASK_QUEUE_NAME = queue_config["FILTER_TASK_QUEUE_NAME"]

DEDUP_TASK_QUEUE_URL = queue_config["DEDUP_TASK_QUEUE_URL"]
DEDUP_TASK_QUEUE_NAME = queue_config["DEDUP_TASK_QUEUE_NAME"]


def clearQueue(queue_url, queue_name):
    
    queue_client = CloudAMQPClient(queue_url, queue_name)
    num_of_messages = 0

    while True:
        if queue_client is not None:
            msg = queue_client.getMessage()
            if msg is None:
                print "Cleared %d messages." % num_of_messages
                return
            num_of_messages += 1

if __name__ == "__main__":
    clearQueue(FILTER_TASK_QUEUE_URL, FILTER_TASK_QUEUE_NAME)
    clearQueue(DEDUP_TASK_QUEUE_URL, DEDUP_TASK_QUEUE_NAME)
