import re
import threading
from piazza_api import Piazza
import json

p = Piazza()
p.user_login()
eecs100 = p.network('hyq0br1u3kx7dg')


file = open('all.jsonl','r')
all_uids = set()
lines = file.readlines()
for i, line in enumerate(lines):
	print(str(i), '/', str(5004), 'lines read...')
	uids = set(re.findall(r'"uid": "(.*?)"',line))
	all_uids.update(uids)


print('Total Users')
print(len(all_uids))

all_uids = list(all_uids)

jsline = open('all_users.jsonl','w')

def worker():
	while len(all_uids) != 0:
		print('Progress...',str(1- len(all_uids)/5004))
		res = eecs100.get_users([all_uids.pop()])[0]
		jsline.write(json.dumps(res))
		jsline.write('\n')
		jsline.flush()

threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
