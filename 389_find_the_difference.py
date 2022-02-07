s = "a"
t = "aa"

''' it wont return if there is 2 similar letter
for i in t:
	if i not in s:
		return(i)
'''

'''  https://realpython.com/python-counter/
s_lettercount = {}
t_lettercount = {}

for s_letter in s:
	s_lettercount[s_letter] = s_lettercount.get(s_letter, 0) + 1

for t_letter in t:
	t_lettercount[t_letter] = t_lettercount.get(t_letter, 0) + 1

for letter in t:
	if s_lettercount[letter] != t_lettercount[letter]:
		print(letter)
'''

'''
for tletter in t:
	if tletter not in lettercount or lettercount.get(letter) > 1:
		print(tletter)
	print(lettercount)
'''

# https://www.w3schools.com/python/ref_string_count.asp
for i in t:
	if s.count(i) != t.count(i):
		print(i)