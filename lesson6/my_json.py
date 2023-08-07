import json

data_to_write = {
    "name": "Alex",
    "age": 35,
    "isMarried": False,
    "friends": [
        {

            "name": "Bob",
            "age": 25,
            "isMarried": False
        },
        {
            "name": "John",
            "age": 25,
            "isMarried": False
        }
    ]
}

with open('Hello', 'w') as f:
    json.dump(data_to_write, f)

with open('Hello', 'r') as f:
    printlines = f.read()
    result = json.loads(printlines)
    print(result)
