
valid_rule = {
    "name":{
        "type":str,
        "max_len":100,
        "min_len":20
        },
    "age":{
        "type":int,
        "max_value":50,
        "min_value":16,
    }
}

data_dict = {"name":"Mero neupane ho","age":17}


def validate_string(key,data_dict, valid_rule):

    if valid_rule[key].get("min_len") and valid_rule[key].get("max_len"):
        if  valid_rule[key]["min_len"] < len(data_dict[key]) < valid_rule[key]["max_len"]:
            print("true")
        else:
            print("false")
    
    elif valid_rule[key].get("min_len"):
        if  valid_rule[key]["min_len"] < len(data_dict[key]):
            print("true")
        else:
            print("false")

    elif valid_rule[key].get("max_len"):
        if  valid_rule[key]["max_len"] > len(data_dict[key]):
            print("true")
        else:
            print("false")
    else:
        print("true")

def validate_int(key,data_dict, valid_rule):
    if valid_rule[key].get("max_value") and valid_rule[key].get("min_value"):
        if  valid_rule[key]["min_value"] < data_dict[key] < valid_rule[key]["max_value"]:
            print("true")
        else:
            print("false")
    
    elif valid_rule[key].get("max_value"):
        if  valid_rule[key]["max_value"] < data_dict[key]:
            print("true")
        else:
            print("false")

    elif valid_rule[key].get("max_value"):
        if  valid_rule[key]["max_value"] > data_dict[key]:
            print("true")
        else:
            print("false")
    else:
        print("true")

def validate_dict(data_dict, valid_rule):
    for key in data_dict:
        if valid_rule.get(key):
            if valid_rule[key]["type"] == type(data_dict[key]):
                if type(data_dict[key]) == str:
                    validate_string(key,data_dict, valid_rule)
                
                if type(data_dict[key]) == int:
                    validate_int(key,data_dict, valid_rule)
            else:
                print("false")


validate_dict(data_dict, valid_rule)


    
