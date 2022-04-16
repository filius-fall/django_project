import redis,json
from datetime import datetime

r=redis.Redis(host='localhost',port=6379,db=0)

now = datetime.now()

# r.set('name1','test')
# r.set('message1','test message')
# r.set('name2','test2')
# r.set('message2','test message2')
# r.set('name3','test3')
# r.set('message3','test message3')
# r.set('name5','test5')
# r.set('message5','test message5')
# key = 'expense_db'+'-'+str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'-'+str(now.hour)+'-'+str(now.minute)

# details = {
#     'expense': 87777777,
#     'category': 'tes',
#     'descryption': 'test description'
# }
# print(type(json.dumps(details).encode('utf-8')))
# l = json.dumps(details)
# r.hset(key,mapping=details)
# for i in r.scan_iter('expense_db*'):
#     print(i)
#     print(r.hgetall(i))
#     print('\n')
# print(k)

# r.hset(key,details.digest())
r.flushall()