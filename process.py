import psutil
import time
import os
while True:
    pro_dict = {}
    monitor_name = {'nginx'}
    monitor_map = {
        'nginx','service nginx start'
    }
    pro_name = set()
    for p in psutil.process_iter(attrs=['pid','name']):
        pro_dict[p.info['pid']] = p.info['name']
        pro_name.add(p.info['name'])
    pro_stop = monitor_name - pro_name
    if pro_stop:
        print('%s已经停止' % pro_stop)
    else:
        print('一切正常')
    time.sleep(2)