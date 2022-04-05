# 1. simple 
 # lang='python1'
# if lang=='python':
# 	print('The Language is python')
# elif lang=='java':
# 	print('The language is Java')
# else: 
# 	print('No match')



# 2. and, or, not 

lang='java'
level = 'high'

if lang=='java' and level=='high':
	print('Great')

#3. find id of a variable in memory 
print(id(level) is id(lang))
	
