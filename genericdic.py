
class DictValidation:

    def __init__(self, validation_values):
        self.valdation_rules = validation_values
    
    def validate(self, data_dict):
        self.data_dict = data_dict
        for keys in data_dict:
            print(data_dict[keys])
            print(self.valdation_rules[keys])
    
    def validate_string(self):
        ...


validation_values = DictValidation({
    "name":{
        "type":str,
        "max_len":40,
        "min_len":20,
    },
    "age":{
        "type":int,
        "<=":80,
        ">":16,
    }

})

data_dict = {
    "name":"Sagar Neupnae","age":25
}

validation_values.validate(data_dict)