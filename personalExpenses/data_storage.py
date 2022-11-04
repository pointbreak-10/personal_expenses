import json



def jsonDB(obj):
    with open('data.json','a') as f:
        json.dump(obj, f, ensure_ascii=True, indent=4)
        
