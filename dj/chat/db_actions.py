import redis
from datetime import datetime

r = redis.Redis(host='localhost', port=6379, db=0)

def set_values(key, value):
    r.set(key, value)

def get_values(key):
    return r.get(key)

def get_all_keys():
    return r.keys()
    

def hset_values(fields={}):
    now = datetime.now()
    key = 'expense_db'+'-'+str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'-'+str(now.hour)+'-'+str(now.minute)
    r.hset(key,mapping=fields)

def hgetall_values():
    data_array = []
    get_keys = r.keys('expense_db*')
    for i in get_keys:
        data_array.append(convert_byte_string(r.hgetall(i)))
    
    return data_array


def convert_byte_string(con):
    return { key.decode(): val.decode() for key, val in con.items() }