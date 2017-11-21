import os
import sys

import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client

from cloudAMQP_client import CloudAMQPClient

HOUSE_LISTING_TABLE_NAME = "house-listing"


DEDUP_TASK_QUEUE_URL = "amqp://qmkhhszp:tgEYKeeNuKfnKRiWLX6p9-Kuv8Zfl066@elephant.rmq.cloudamqp.com/qmkhhszp"
DEDUP_TASK_QUEUE_NAME = "dedup_task_queue"

NOTIFICATION_TASK_QUEUE_URL = "amqp://lmmocuap:DPdNdw03IT0laCvkNm66BzP_0iSY3GHk@elephant.rmq.cloudamqp.com/lmmocuap"
NOTIFICATION_TASK_QUEUE_NAME = "notification_task_queue"

cloudAMQP_client = CloudAMQPClient(DEDUP_TASK_QUEUE_URL, DEDUP_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        return

    task = msg
    
