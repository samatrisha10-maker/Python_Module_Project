import json

def convert_to_json(data):
    result = json.dumps(data)
    return result
print(convert_to_json({"name" :"ravi","age" :22}))