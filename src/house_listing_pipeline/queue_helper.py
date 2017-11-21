import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

FILTER_TASK_QUEUE_URL = "amqp://ymcsvgqv:ulM5Xwupq5lJdQ3L0HBy_-xO74CRtGh7@mosquito.rmq.cloudamqp.com/ymcsvgqv"
FILTER_TASK_QUEUE_NAME = "filter_task_queue"

DEDUP_TASK_QUEUE_URL = "amqp://qmkhhszp:tgEYKeeNuKfnKRiWLX6p9-Kuv8Zfl066@elephant.rmq.cloudamqp.com/qmkhhszp"
DEDUP_TASK_QUEUE_NAME = "dedup_task_queue"

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
