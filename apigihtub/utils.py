import json

class Payload(object):
    def __init__(self, j):
        self.__dict__ = j

class PayloadDict(object):
    def __init__(self, j):
        json_obj = json.loads(j)
        self.__dict__ = json_obj
    
    def parse_user(self):
        data = {}
        for item in self.__dict__:
            if item == 'login':
                data['username'] = self.__dict__[item]
            elif item == 'id':
                data['user_id'] = self.__dict__[item]
            elif item == 'html_url':
                data['url'] = self.__dict__[item]
        return data

class PayloadList(object):
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
                elif key == 'html_url':
                    el[key] = item.html_url
                elif key == 'owner':
                    el[key] = item.owner['id']
                elif key == 'id':
                    el[key] = item.id
            if len(el) > 0:
                data.append(el)        
        return {"repos" : data}
    
    def parse_users(self):
        data = []
        for item in self.payloads:
            el = {}
            for key in item.__dict__:
                if key == 'login':
                    el[key] = item.login
                elif key == 'id':
                    el[key] = item.id
                elif key == 'html_url':
                    el[key] = item.html_url
            if len(el) > 0:
                data.append(el)        
        return {"users" : data}
        
            


