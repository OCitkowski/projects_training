import os
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

redis_host = os.environ.get('REDIS_HOST', 'localhost')
# Channel layer definitions
# http://channels.readthedocs.org/en/latest/deploying.html#setting-up-a-channel-backend
CHANNEL_LAYERS = {
    "default": {
        # This example app uses the Redis channel layer implementation asgi_redis
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(redis_host, 6379)],
        },
        "ROUTING": "multichat.routing.channel_routing",
    },
}


if __name__ == '__main__':
    print(r.ping())

    rr = r.set('foo', 'bar', ex=10)
    r.set('foo2', 'bar2')
    r.set('qfoo2', 'qbar2')
    print(redis_host)
    print(r.get('foo'))
    print(r.dbsize)

    print(r.info('foo'))
    print(r.keys())
    print(r.info())

    r.close()

