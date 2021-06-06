import jsonlines
from datetime import datetime


TEST_COUNT = 5000

def getTrainingSessions():
    with jsonlines.open('data/sessions.jsonl') as reader:
        data = [[item["user_id"], item["product_id"], item["event_type"], _strToDate(item["timestamp"]), item['session_id']] for item in reader]
    return data[:-TEST_COUNT]

def getTestSessions():
    with jsonlines.open('data/sessions.jsonl') as reader:
        data = [[item["user_id"], item["product_id"], item["event_type"], _strToDate(item["timestamp"]), item['session_id']] for item in reader]
    return data[-TEST_COUNT:]

def getUserIds():
    with jsonlines.open('data/users.jsonl') as reader:
        data = [item["user_id"] for item in reader]
    return data

def getProductIds():
    with jsonlines.open('data/products.jsonl') as reader:
        data = [item["product_id"] for item in reader]
    return data

def getProductCategoryData():
    with jsonlines.open('data/products.jsonl') as reader:
        data = [[item["product_id"], item["category_path"]] for item in reader]
    return data



def _strToDate(date: str) -> datetime:
    result = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    return result
