# sort_dict={"bijender":45,"deepak":60,"param":20,"anjali":30,"roshan":50}
#

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict) 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict) 




# a={
#     "a":"1",
#     "b":"2",
#     "c":"3",
#     "d":"4"
# }
# del a["a"]
# print(a)

# a={
#     "a":"a",
#     "b":"b",
#     "d":"d"
# }
# a.popitem()
# print(a)

# dic={"name":"Raju", "marks":56}
# user=input("enter the number")
# if user in dic:
#     print("exists")
# else:
#     print("not exists")




# my_dict = {
#     'data1':100,
#     'data2': -54,
#     'data3': 247
#     }  


# def returnSum(dict):
      
#      sum = 0
#      for i in dict.values():
#            sum = sum + i
       
#      return sum
  
# # Driver Function
# dict = {'a': 100, 'b':200, 'c':300}
# print("Sum :", returnSum(dict))     

dict={"a":100,"b":200,"c":300}
sum=0
for i in dict.values():
    sum=sum+i
print(sum)
