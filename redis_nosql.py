from redis import StrictRedis

if __name__ == '__main__':
    try:
        redis_1 = StrictRedis(host='localhost', port=6379, db=0)
        redis_1.set('name', 'majian')
        # print(redis_1.get('name').decode())
        # result=redis_1.delete('name')
        # result = redis_1.keys()
        redis_1.lpush('a1','he','heh','hehe')
        result=redis_1.lrange('a1',0,-1).decode()
        print(result)
    except Exception as e:
        print('错误在%s' % e)
