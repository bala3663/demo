"""num=153
num1=str(num)
sum=0
for i in num1:
    a=int(i)*int(i)*int(i)
    sum=sum+a
print(sum) 
if sum==num:
    print("armstrong number")   
"""

"""for num1 in range(2,51):
    for num2 in range(2,51):
        if num1%num2==0:
            break
    if num1==num2:
        print(num1,end=" ")    """

"""while True:
    num=int(input("enter number"))
    list=[]
    for digit in range(1,num+1):
        if num%digit==0:
            list.append(digit)
    print(list)    
    if (len(list))==2:
        print("prime number")
    else:
        print("not prime")    """


"""def fibonacci(num):
    if num<=0:
        return 0
    if num==1:
        return 0
    if num==2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(10))"""


"""s="z"
print(ord(s))"""


"""list=[4,9,2,6,1]
for dig1 in range(len(list)):
    for dig2 in range(len(list)):
        if list[dig1]<list[dig2]:
            list[dig1],list[dig2]=list[dig2],list[dig1]
print(list)  """ 

"""list=[10,2,7]
multiplication=1
for number in list:
    multiplication=multiplication*number
print(multiplication)  """ 

"""list=[1,2,3,4,5]
for i in list:
    if i in (1,2,3):
        pass
    else:
        print(i)"""

"""test_list = [5, 6, [], 3, [], [], 9]
for i in test_list:
    if i==[]:
        pass
    else:
        print((i)) """ 


"""num=231
sum=0
num1=str(num)
for digit in num1:
    sum=sum+int(digit)
print(sum)"""   



"""list=[12,22]
ans=[]
for dig in  list:
    sum=0
    for j in str(dig):
        #print(j)
        sum=sum+int(j)
    ans.append(sum)
print((ans))        
"""

"""list=[2,3,4,5,2,5,5]
count=0
for i in range (len(list)):
    if list[i]==5:
        count=count+1
print(count)  """

"""str="hello"
count={}
for i in str:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count) 

for i in count:
    if count[i]==2:
        print(i)"""


"""tuple=(1,23)
print(len(tuple))
""" 


"""x=10
y=50

x=x+y
y=x-y
x=x-y


print(x)
print(y)"""


"""
tuple=(1,"a")
print(tuple)"""


"""
import array as arr
a=arr.array("i",[1,2,3])
b=arr.array("i",[3,1,2])
print(a==b)
print(a)"""

"""sum=lambda x,y:x+y
print(sum(4,5))"""

"""str="123abcjw:, .@! eiw"
ans=""
for i in str:
    if i.isalpha() or i.isdigit():
        ans=ans+i
print(ans)  """      
        

"""
dict={'a': 100, 'b':200, 'c':300}
sum=0
for i in dict.values():
    sum=sum+i
print(sum)            
"""


"""list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print(sorted(list,key=lambda x:x['age']))"""

"""s="animal"

res=s.endswith(('a','e','i'))
print(res)  """    

"""def factorial(num):
    if num==0:
        return 1
    if num==1:
        return 1
    if num==2:
        return 2
    else:
        return num*factorial(num-1)
print(factorial(3))"""




"""def fibonacci(num):
    if num==0:
        return 0
    if num==1:
        return 1
    if num==2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(9))
"""



"""
list=[4,9,8,2]
for num1 in range (len(list)):
    for num2 in range(len(list)):
        if list[num1]<list[num2]:
            list[num1],list[num2]=list[num2],list[num1]
print(list[-1])
"""



"""list=[12, 15, 3, 10]
ans=[]
for num in list:
    if num not in (12,3):
        ans.append(num)
print(ans)  """      




"""list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
count={}
for num in list:
    if num in count:
        count[num]=count[num]+1
    else:
        count[num]=1
print(count)        
for ele in count:
    if count[ele]>=2:
        print(ele)"""


"""class Person:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2 
obj=Person(2,4) 
print(obj.add()) 

class Student(Person):
    pass"""


"""list=[1, 2, 3, 4, 5]
print(list[:-2])
list.pop()
print(list)"""



"""dict={2:"two",1:"one"}
dict1={}
d=sorted(dict.keys())

for i in d:
    dict1[i]=dict[i]
print(dict1) """   


"""dict={2:"two",1:"one"}
dict2={}
sorted_key=sorted(dict.keys())
for value in sorted_key:
    dict2[value]=dict[value]
print(dict2)"""

"""str="hello_world"
str1=str.split("_")
print(str1)
str2=".".join(str1)
print(str2)  """ 


"""list=[2,4,6,6]
list.sort()
print(list)"""

"""for num in list:
    if list.count(num)==2:
        print(num)
        break"""


"""]"""

"""list1=[2,3,4]
list2=[3,5,7]
sum=map(lambda x,y:x+y,list1,list2)
print(list(sum))"""

"""list1=[2,3,4]
list2=[3,5,7]
ans=[]
for i in list1:
    sum=0
    for j in list2:
        sum=i+j
    ans.append(sum)
print(ans)       """ 





"""#perfect number
num=7
sum=0
ans=[]
for i in range(1,num):
    if num%i==0:
        ans.append(i)
print(ans) 
for i in ans:
    sum=sum+i
if num==sum:
    print("perfect number")
else:
    print("not perfect")"""



"""#ANAGRAM
str1="hello"
str2="ollekh"
if sorted(str1)==sorted(str2):
    print("anagram")
else:
    print("not anagram")
    """

#find missings
"""arr=[1,2,4,5]
for i in range(1,6):
    if i not in  arr:
        print(i)"""

"""#reverse array
arr=[1,2,4,5,8,9,8,9]
for i in range(len(arr)-1,-1,-1):
    print(arr[i])"""

"""    #remove number at index
list=[0,1,2,3,4]
ans=[]
for i in range(len(list)):
    if i!=1:
        ans.append(list[i])
print(ans)  
"""

#hcf
"""num1=8
num2=2
if num1>num2:
    mini=num1
else:
    mini=num2
for i in range(1,mini+1):
    if num1%i==0 and num2%i==0:
        hcf=i
print(hcf)  """



#lcm
"""num1=9
num2=18
if num1>num2:
    maxi=num1
else:
    maxi=num2
for i in range(1,maxi+1):
    if maxi%num1==0 and maxi%num2==0:
        lcm=i
print(lcm)  """      
    

"""num1= 8
num2=2
if num1>num2:
    mini=num2
else:
    mini=num1
for i in range(1,mini+1):
    if num1%i==0 and num2%i==0:
        hcf=i
print(hcf) """           

"""num1=9
num2=18
if num1>num2:
    maxi=num1
else:
    maxi=num2
while True:

    if maxi%num1==0 and maxi%num2==0:
        lcm=maxi
        break
print(lcm) """    

"""def fibonacci(num):
    if num==0:
        return 0
    if num==1:
        return 1
    if num==2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(9))"""
    
"""def factorial(num):
    if num==0:
        return 1
    if num==1:
        return 1
    if num==2:
        return 2
    else:
        return(num*factorial(num-1))
print(factorial(3))    """



"""num1=7
num2=0
try:
    ans=num1/num2
except ZeroDivisionError:
    print("can not divide by zero") """ 



"""file=open("text.txt","r")
print(file.read())"""

"""
list1=[4,6,7]
#list2=[9,3,5]
ans=list(filter(lambda y:y%2==0,list1))
print(ans)"""


"""dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict1.update(dict2)
print(dict1)"""


"""def merge(dict1,dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1    

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(merge(dict1,dict2))"""


"""str="geeksforgeeeks"
count={}
for i in str:
    if i not in count:
        count[i]=1
        
    else:
        count[i]=count[i]+1
print(count)   
for i in count:
    if count[i]==2:
        print(i)         
"""

"""test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}
test_dict1=test_dict.pop('Mani')
print(test_dict1)"""



"""dicts = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]
print(sorted(dicts,key=lambda x:x['age']))"""




"""
def longest_common_prefix(strings):
    small_word=min(strings,key=len)
    #print(small_word)
    for i,ch in enumerate(small_word):
        #print(i,ch)
        for words in strings:
            #print(words)
            if words[i]!=ch:
                return small_word[:i]
    return small_word        
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))"""





"""strings = ["hello", "world", "apple", "banana", "cat", "dog"]
vowel_count=[]
vowels="aeiou"
for words in strings:
    print(words)
    count=0
    for ch in words:
        if ch in vowels:
            count+=1
    vowel_count.append([words,count])
print(vowel_count)   
print(sorted(vowel_count,key=lambda x:x[1]))  """  





