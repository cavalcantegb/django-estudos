import json

class Payload(object):
    def __init__(self, j):
        self.__dict__ = j

class PayloadUser(object):
    def __init__(self, j):
        json_obj = json.loads(j)
        self.__dict__ = json_obj
    
    def parse_user(self):
        data = {}
        for item in self.__dict__:
            if item == 'full_name':
                data[item] = self.__dict__[item]
            elif item == 'name':
                data[item] = self.__dict__[item]
        return data

class PayloadRepo(object):
    payloads = []
    
    def __init__(self, j):
        json_obj = json.loads(j)
        for item in json_obj:
            self.payloads.append(Payload(item))
    
    def parse_repos(self):
        data = []
        for item in self.payloads:
            el = {}
            for key in item.__dict__:
                if key == 'name':
                    el[key] = item.name
                elif key == 'full_name':
                    el[key] = item.full_name
            if len(el) > 0:
                data.append(el)        
        return {"repos" : data}
        
            


