import os
import sys
# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))


NOTIFICATION_TASK_QUEUE_URL = "amqp://lmmocuap:DPdNdw03IT0laCvkNm66BzP_0iSY3GHk@elephant.rmq.cloudamqp.com/lmmocuap"
NOTIFICATION_TASK_QUEUE_NAME = "notification_task_queue"

notification_queue_client = CloudAMQPClient(DEDUP_TASK_QUEUE_URL, DEDUP_TASK_QUEUE_NAME)  

def handle_message(msg):

