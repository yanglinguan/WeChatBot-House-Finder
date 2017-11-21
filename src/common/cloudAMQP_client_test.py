from cloudAMQP_client import CloudAMQPClient

#CLOUDAMQP_URL = "amqp://jltoaaqa:sUWk_YUboQTE5k5LSRzfEyvVUZN2FPiT@rhino.rmq.cloudamqp.com/jltoaaqa"
#TEST_QUEUE_NAME = "test"
CLOUDAMQP_URL = "amqp://ymcsvgqv:ulM5Xwupq5lJdQ3L0HBy_-xO74CRtGh7@mosquito.rmq.cloudamqp.com/ymcsvgqv"
TEST_QUEUE_NAME = "filter_task_queue"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)
    sentMsg = {"test": "test"}
    #client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    #assert sentMsg == receivedMsg
    print "test_basic passed"

if __name__ == "__main__":
    test_basic()
