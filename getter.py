from piazza_api import Piazza
import json
p = Piazza()
p.user_login()
eecs100 = p.network('hyq0br1u3kx7dg')
feed = eecs100.get_feed(limit=999999, offset=0)
cids = [post['id'] for post in feed["feed"]]

jsline = open('sample.jsonl','w')

def worker():
	while len(cids) != 0:
		print('Progress...',str(1- len(cids)/5004))
		res = eecs100.get_post(cids.pop())
		jsline.write(json.dumps(res))
		jsline.write('\n')
		jsline.flush()

import threading

threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
