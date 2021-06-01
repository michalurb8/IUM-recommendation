import jsonlines


def getSessionData():
    with jsonlines.open('sessions.jsonl') as reader:
        data = [[item["user_id"], item["product_id"], item["event_type"]] for item in reader]
    return data

def getUserIds():
    with jsonlines.open('users.jsonl') as reader:
        data = [item["user_id"] for item in reader]
    return data

def getProductIds():
    with jsonlines.open('products.jsonl') as reader:
        data = [item["product_id"] for item in reader]
    return data

def getProductCategoryData():
    with jsonlines.open('products.jsonl') as reader:
        data = [[item["product_id"], item["category_path"]] for item in reader]
    return data
