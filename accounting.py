import json
import numbers

def accounting(path):
    '''
    Function returns total amount of numeric values in json file
    '''
    with open(path) as json_data:
        json_file = json.load(json_data)
    
    def countNumbers(json_data):
        if type(json_data) is dict:
            return(sum([countNumbers(i) for i in json_data.values()]))
        elif type(json_data) is list:
            return(sum([countNumbers(i) for i in json_data]))
        elif isinstance(json_data, numbers.Number):
            return json_data
        else:
            return 0
    
    return countNumbers(json_file)

print("Total Amount:", accounting('accounting_input.json'))
input("Press any key to exit")
