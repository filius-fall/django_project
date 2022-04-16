import redis

r=redis.Redis(host='localhost',port=6379,db=0)

# r.set('name1','test')
# r.set('message1','test message')
# r.set('name2','test2')
# r.set('message2','test message2')
# r.set('name3','test3')
# r.set('message3','test message3')
r.set('name5','test5')
r.set('message5','test message5')