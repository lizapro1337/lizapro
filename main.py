text = "Hello, Python!"
print (text[0]) 
print (text[0:5]) 
print (text[4:10])
print (text[0:14])
print (text[7:]) 
print (text[:5]) 
print (text[:]) 
print (text[-1]) 
print (text[-1:-14]) 
print (text[::2]) 
print (text[::-1]) 
print (text+"Nice to code you")
print (text[-1]) 

my_list =[True, 786, 3.14, 'text', 70.2]
second_list =[123, 'text']

print (my_list)
print (my_list[0])
print (my_list[1:3])
print (my_list[2:])
print (second_list *2)
print (my_list + second_list) 

my_typle =(True, 786, 3.14, 'text', 70.2)
second_tuple =(123, 'text')

print (my_typle)
print (my_typle[0])
print (second_tuple *2)
print (my_typle + second_tuple) 

my_dict = { }
my_dict["country"] = "Mexico"
print (my_dict["country"])

another_dict = {"number":23, 2: True, "my_list" :[1,2,3]}
print (another_dict.keys())
print (another_dict.values())

s = (set())

s = {"hi", "bye"}