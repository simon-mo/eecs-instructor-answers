import html2text
import json
from json.decoder import JSONDecodeError

ins_ids = {'hck3jkt89tc5ot': 'Tsu-Jae King Liu', 'hc2jr3mqtgy7j5': 'Prasad Raghavendra', 'ixkvrxp4cro10j': 'John DeNero', 'giw1lvgzQSy': 'Satish Rao', 'gxkz7s1dqu77nq': 'Kris Pister', 'gro4nnkuub': 'Elad Alon', 'i1hzq2pfv2y4mu': 'Clark Nguyen', 'hkzv8x1xsup4d9': 'umesh vazirani', 'hqlw1f5vivi399': 'Vladimir Stojanovic', 'gxj8rtteeuaa9': 'Anant Sahai'}

def parse(x):
	return html2text.html2text(x)

ans = open('prof_answers.jsonl','r').readlines()

cleaned = []
for a in ans:
    if a[-1] == '\n':
        a = a[:-1]
    try:
		d = json.loads(a)
		cleaned.append(d)
	except JSONDecodeError:
		pass

non_note_results = []
for r in cleaned:
	if 'instructor-note' not in r['tags']:
		non_note_results.append(r)

non_note_results = non_note_results[::-1]

for test in non_note_results:
	post = test['history'][0]
	subject = parse(post['subject'])
	content = parse(post['content'])
	time = post['created']

	i_answer = [t for t in test['children'] if t['type'] == 'i_answer']
	if len(i_answer) != 0:
		i_answer = i_answer[0]
		i_answer_content = parse(i_answer['history'][0]['content'])
		i_answer_author = ins_ids.get(i_answer['history'][0]['uid'])

	print('##', subject[:-1])
	print(time[0:10])
	print(content[:-1])

	if i_answer_content:
		i_answer_content = i_answer_content[:-1]
		if i_answer_author is not None:
			print('###', i_answer_author+"\'s answer")
			print(i_answer_content)
		else:
			print('###', "Instructor answer")
			print(i_answer_content)
		
	follow_ups = [t for t in test['children'] if t['type'] == 'followup']
	for f in follow_ups:
		if f['children'] != []:
			print('### Followup:')
			f_subject = parse(f['subject'])
			f_children = f['children'][::-1]
			for c in f_children:
				c_subject = parse(c['subject'])
				c_author = c.get('uid')

				if c_author:
					c_author = ins_ids.get(c_author)
				
				if c_author is None:
					c_author = 'Student'

				print(c_author+':')
				print(c_subject[:-1])
			



