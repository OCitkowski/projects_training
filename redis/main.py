import redis

r = redis.Redis(host='localhost', port=6379, db=0)

if '__name__' == '__main__':
    r.set('foo', 'bar')
    print('foofttt')
    print(r.get('foo'))
