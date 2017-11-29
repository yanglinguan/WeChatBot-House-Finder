import datetime
import googlemaps
import os
import pickle
import redis
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SLEEP_TIME_IN_SECONDS = 10

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)

FILTER_TASK_QUEUE_URL = "amqp://ymcsvgqv:ulM5Xwupq5lJdQ3L0HBy_-xO74CRtGh7@mosquito.rmq.cloudamqp.com/ymcsvgqv"
FILTER_TASK_QUEUE_NAME = "filter_task_queue"

DEDUP_TASK_QUEUE_URL = "amqp://qmkhhszp:tgEYKeeNuKfnKRiWLX6p9-Kuv8Zfl066@elephant.rmq.cloudamqp.com/qmkhhszp"
DEDUP_TASK_QUEUE_NAME = "dedup_task_queue"


filter_queue_client = CloudAMQPClient(FILTER_TASK_QUEUE_URL, FILTER_TASK_QUEUE_NAME) 
dedup_queue_client = CloudAMQPClient(DEDUP_TASK_QUEUE_URL, DEDUP_TASK_QUEUE_NAME)

gmaps = googlemaps.Client(key='AIzaSyAf4ltA-FUcRxs52hR_EVqJbYFL7amwZJI')

WALKING_MODE = "WALKING"
DRIVING_MODE = "driving"
TRANSIT_MODE = "transit"


def getTimeToWork(house_addr, work_addr, t_mode, d_time):
    
    routes = directions_result = gmaps.directions(
            house_addr, 
            work_addr, 
            mode=t_mode, 
            departure_time=d_time)

    total_duration = routes[0]['legs'][0]['duration']['value']
    total_distance = routes[0]['legs'][0]['distance']['value']
    
    if t_mode == "transit":
        walking_duration = 0
        walking_distance = 0
        if routes[0]['legs'][0]['steps'][0]['travel_mode'] == WALKING_MODE:
            walking_duration = routes[0]['legs'][0]['steps'][0]['duration']['value']
            walking_distance = routes[0]['legs'][0]['steps'][0]['distance']['value']
        return total_duration, total_distance, walking_duration, walking_distance

    return total_duration, total_distance
        

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print 'message is broken'
        return

    task = msg
    client_request_table = pickle.loads(redis_client.get(msg["client_id"]))
    client_request = client_request_table[msg["request_id"]]

    work_addr = client_request["work_addr"]

    travel_mode = client_request["travel_mode"]

    house_addr = (msg["lat"], msg["lon"])

    departure_to_work_hour = client_request['departure_to_work_hour']
    departure_to_work_minute = client_request['departure_to_work_minute']


    nextday = datetime.datetime.now() + datetime.timedelta(days=1)

    d_time = nextday.replace(hour=int(departure_to_work_hour), minute=int(departure_to_work_minute), second=0, microsecond=0)

    print house_addr
    print work_addr
    print d_time

    transit_total_duration, transit_total_distance, walking_duration, walking_distance = getTimeToWork(house_addr, work_addr, TRANSIT_MODE, d_time)

    print transit_total_duration
    
    other_mode_duration = sys.maxint
    other_mode_distance = sys.maxint

    if travel_mode != TRANSIT_MODE:
        other_mode_duration, other_mode_distance = getTimeToWork(house_addr, work_addr, travel_mode, d_time)
        
    min_mode_duration = transit_total_duration
    min_mode_distance = transit_total_distance

    print travel_mode
    print other_mode_duration

    if min_mode_duration > other_mode_duration:
        min_mode_duration = other_mode_duration
        min_mode_distance = other_mode_distance

    time_to_work = int(client_request['time_to_work'])
    time_delta = 0
    # time_delta = int(client_request['time_to_work_delta'])
    print "time to wok:" + str(time_to_work)
    print "min: " + str(min_mode_duration)
    print min_mode_duration

    if min_mode_duration <= time_to_work + time_delta:
        task['transit_mode_duration'] = transit_total_duration
        task['transit_mode_distance'] = transit_total_distance
        if travel_mode != TRANSIT_MODE:
            task[travel_mode + "_duration"] = other_mode_duration
            task[travel_mode + "_distance"] = other_mode_distance

        dedup_queue_client.sendMessage(task)
        return task


def filter_queue():
    while True:
        if filter_queue_client is not None:
            msg = filter_queue_client.getMessage()
            if msg is not None:
                try: 
                    handle_message(msg)
                except Exception as e:
                    pass
            else:
                break
            filter_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
        else:
            print("filter task queue is none")
            break

