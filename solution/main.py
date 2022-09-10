import json


def load_json(path:str) -> dict:
    try:
        with open(path) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = {}
    except FileNotFoundError:
        return None
        
    return data  


def get_proper_schema_type_name(schema_type: str) -> str:
    """Get the proper schema type name"""
    if schema_type == "bool":
        return "boolean"
    elif schema_type in {"int", "float"}:
        return "integer"
    elif schema_type == "str":
        return "string"
    elif schema_type == "list":
        return "enum"
    else:
        return schema_type


def generate_schema(data:dict) -> dict:
    """Generate a schema from a JSON object"""
    
    schema = {}
    
    if not data or type(data) != dict:
        return schema
    
    
    padding = {
            "tag": "",
            "description": "",
            "required" : False,
    }
    
    for key, value in data.items():
        if type(value) == dict:
            schema[key] = {
                "type": "array",
                # crawl the nested objects by recursion
                "properties": generate_schema(value)
            } | padding
            
        else:
            
            # get the type of the value if it is not a nested object
            schema[key] =  {
                        "type":get_proper_schema_type_name(type(value).__name__)
                    
                    } | padding
            
    return schema


def write_json(data: dict, file_name: str) -> None:
    """Write JSON to a file"""
    if not data or not file_name:
        return

    if type(data) != dict or type(file_name) != str:
        print('Invalid data or file name')
        return
  
    try:
        path = f"./data/output/{file_name}.json"
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"File saved to {path}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    file_name = input("Enter the name of the JSON file [1], [2]: ")
    data = load_json(f'./data/input/{file_name}.json')
    work_data = data["message"] 
    write_json(generate_schema(work_data), file_name)
    
    




