import json

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)
        
    def parse_user(self):
        data = {}
        for item in self.__dict__:
            if item == 'url':
                data[item] = self.__dict__[item]
            elif item == 'name':
                data[item] = self.__dict__[item]
        return data


