import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def set_values(key, value):
    r.set(key, value)

def get_values(key):
    return r.get(key)

def get_all_keys():
    return r.keys()