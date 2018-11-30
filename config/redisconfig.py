import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

r.set('one', '一')
r.set('two', '二')
print(r.get('one'))
print(r.get('two'))
