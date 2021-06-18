from typing import List

def parse_id(id_) -> List[int]:
    id = id_.replace("-", " ", 2)
    id = id.split()
    return [int(x) for x in id] # convert to int
    
def format_json(json: dict) -> List:
    json.pop("requestId")
    return json