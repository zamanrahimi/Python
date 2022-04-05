#1. simple concatenation

greeting="hello"
name="John"

print(greeting + " , "+ name)

#2. complicated 
message = "{} ,{}"
print(message.format(greeting, name))

#3. using f format 

message1 = f'{greeting}, {name.lower()}'
print(message1 + "" +" "+"Welcome")

