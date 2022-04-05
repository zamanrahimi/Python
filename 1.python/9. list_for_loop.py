list1 = ["Ahmad", "Karim", "Ali"]

# A. print only elements 
# for li in list1:

# 	print(li)

# B. print index + elements 

for index, li in enumerate(list1, start=1):
	print(index, li)
