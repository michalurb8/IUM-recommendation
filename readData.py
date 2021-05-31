import jsonlines


def getData():
    with jsonlines.open('sessions.jsonl') as reader:
        data = [[item["user_id"], item["product_id"], item["event_type"]] for item in reader]

    # for datum in data: # print all 183 561 lines
    #     print(datum)


    return data
