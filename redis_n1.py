from rediscluster import *

if __name__ == '__main__':
    try:
        redis_nodes = [
            {'host': '192.168.48.128', 'port': '6001'},
            {'host': '192.168.48.128', 'port': '6002'},
            {'host': '192.168.48.128', 'port': '6003'},
            {'host': '192.168.48.128', 'port': '6004'},
            {'host': '192.168.48.128', 'port': '6005'},
            {'host': '192.168.48.128', 'port': '6006'},
        ]
        src=StrictRedisCluster(startup_nodes=redis_nodes,decode_responses=True)
        result=src.set('name','itchaoma')
        print(result)
        name=src.get('name')
        print(name)
    except Exception as e:
        print(e)

