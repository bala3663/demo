"""list=[12,34]
ans=[]
for ele in list:
    sum=0
    for dig in str(ele):
        sum=sum+int(dig)
    ans.append(sum)
print(ans)        
"""



"""class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
width=int(input("width"))  
height=int(input("height"))    
obj=Rectangle(width,height)
print(obj.area())        

"""






"""class Cal:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return("addition",self.num1+self.num2)
    def div(self):
        return("division",self.num1/self.num2) 
object=Cal(2,3)
print(object.add())  
print(object.div())       """

"""
def facy
factorial(10)
"""
















"""x=10
y=20
x=x+y
y=x-y
x=x-y
print(x)
print(y)
"""











"""list=[2,2,3,2]
count=0
for i in list:
    if i==2:
        count=count+1
print(count)              
"""










"""
list=[1,2,3]
for i in range(len(list)):
    for j in range(len(list)):
        for k in range(len(list)):
            if list[i]!=list[j] and list[j]!=list[k] and list[k]!=list[i]:
                print(list[i],list[j],list[k])

"""
















"""str =" geeks quiz practice code"
list=[]
str1=str.split()
print(str1)
for word in str1:
    list.append(str1[::-1])

print(list)
str2=" ".join(str1) 
print(str2)"""   





"""str="hello"
str1=""
num=2
for i in range (len(str)):
    if i!=num:
        str1=str1+str[i]
print(str1)  """      

"""
str="hello"
ans=str.replace("l",'$')
print(ans)
"""

"""list=[2,3,4,2]
for num in list:
    if list.count(num)==2:
        print(num)

def add(list):
    sum=0
    for i in list:
        sum=sum+i
    print(sum)    
list=[1,2]
add(list)"""















"""x=1
y=0
try:
    result=x/y
except ZeroDivisionError:
    print("can not divide by zero")"""






"""file=open("text.txt","a")
file.write("123")"""




"""def removeDuplicates(str):
    s=set(str)
    print(s)
    s="".join(s)
    print(s)
    t=""
    for i in str:
        if (i in t):
            pass
        else:
            t=t+i
    print(t)

str ="hello world"
removeDuplicates(str)"""



"""def sum(dict):
    list=[]
    for i in dict:
        list.append(dict[i])
    print(list) 
    sum=0
    for i in list:
        sum=sum+i
    print(sum)       

dict={'a': 100, 'b':200, 'c':300}
sum(dict)"""


"""dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict2.update(dict1)
print(dict2)"""









"""class Person:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+self.b)
class Student(Person):
    
    
    def mul(self):
        return(self.a*self.b)
obj=Person(2,3)
print(obj.add())
obj1=Student(7,9)
print(obj1.mul())
print(obj1.add())"""


"""file=open("text.txt","r")
print(file.read())"""
    




"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print({self.name},{self.age})
class student(Person):
    
    def info(self):
        print({self.name},{self.age})
        
        
obj=Person("john",21)
obj1=student("sam",22)

print(obj.display())
print(obj1.info())
print(obj1.display())  """  

"""list=[]
n=int(input("enter"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)    
    """


"""
lst = [10, 11, 12, 13, 14, 15]
rev_list=[]
for i in lst:
    rev_list.insert(0,i)
print(rev_list)    """
   

"""lst = [10, 11, 12, 13, 14, 15]

l = [] 


for i in lst:
	
	l.insert(0, i)

print(l)"""


"""list=[]
sum=0
n=int(input("enter "))
for i in range (0,n):
    ele=int(input())
    list.append(ele)
print(list) 
for i in list:
    sum=sum+i
print(sum)   """  


"""str="hello welcome to world"
str_list=str.split()
length=[len(i) for i in str_list]
print(max(length))
    """
    
"""list=[]
n=int(input("enter"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)   """         

"""str="hello"
str_rev=str[::-1]
print(str_rev)"""

"""str=input("enter")
str_splt=str.split()
str_splt.sort()
print(str_splt)
"""
"""str=input("enter string")
str_splt=str.split()
upper_las=[i.upper() for i in str_splt]
print(upper_las)"""



"""list=[]
n=int(input("enter"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
ans=[]
for i in list:
    if i%2==0:
        ans.append(i)
print(ans)        """

"""str="hello world"
str_splt=str.split()
uppr_last=[i.upper() for i in str_splt]
print(uppr_last)"""


"""str="hello world"
str_splt=str.split()
rev_lst=[i[::-1] for i in str_splt]
print(rev_lst)"""


"""str="hello welcome to world"

for ch in str:
    if ch in ("a","e","i","o","u"):
        str=str.replace(ch,"*")
print(str)  """      




"""def longest_palindrome(s):
    n=len(s)
    longest=""
    for i in range(n):
        for j in range (i,n):
            substring=s[i:j+1]
            print(substring)
            if substring==substring[::-1]:
                if len(substring)>len(longest):
                    longest=substring
    print(longest)
    
s ="forgeeksskeegfor"
longest_palindrome(s)"""



"""def count_vowel(string):
    vowel="aeiou"
    count=0
    for char in string:
        if char in vowel:
            count=count+1
            return count
def sorted_by_vowel(string):
    return sorted(string,key=count_vowel) 
strings = ["hello", "world", "apple", "banana", "cat", "dog"]
sorted_strings = sorted_by_vowel(strings) 
print(sorted_strings)"""


"""def longest_palindrome(s):
    longest=""
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            substring=s[i:j+1]
            if substring==substring[::-1]:
                if len(substring)>len(longest):
                    longest=substring
    print(longest)                
s ="forgeeksskeegfor"
longest_palindrome(s)"""



"""def longest_common_prefix(strings):

    if not strings:

        return ""

    shortest_string = min(strings, key=len)

    for i, char in enumerate(shortest_string):

        for other_string in strings:

            if other_string[i] != char:

                return shortest_string[:i]

    return shortest_string
"""



"""def count_vowel(string):
    vowel="aeiou"
    count=0
    for i in string:
        if i in vowel:
            count=count+1
    return count
def sorted_by_vowel(string):
    return sorted(string,key=count_vowel)        

string = ["hello", "world", "apple", "banana", "cat", "dog"]
print(sorted_by_vowel(string))"""



"""def sorted_by_second(tuples):
    return sorted(tuples,key=lambda x:x[1])##select 0 or 1 acoording to key and value
tuples = [(1, "apple"), (3, "banana"), (2, "cat"), (5, "dog"), (4, "elephant")]
sorted_touple=sorted_by_second(tuples)
print(sorted_touple)"""



"""list=[1250,14,656,1]
len_list=[]
for i in list:
    len_list.append((len(str(i)),i))
    
    
print(len_list)

def sorted_tuple(len_list):

    return sorted(len_list,key=lambda x:x[0])
print(sorted_tuple(len_list))"""




"""def sort_by_key(dict,key):
    return sorted(dict,key=lambda x:x[key])

dicts = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]
print(sort_by_key(dicts, "age"))"""






"""def longest_common_prefix(strings):

   

    shortest_string = min(strings,key=len)
    #print(shortest_string)
   

    for i, char in enumerate(shortest_string):
        #print(i,char)
        

        for other_string in strings:
            #sprint(other_string)

            if other_string[i] != char:
                
                return shortest_string[:i]

    #return shortest_string

# Example usage:

strings = ["flower", "flow", "flight"]

prefix = longest_common_prefix(strings)

print(prefix)"""



"""
def most_common_character(string_splt):

    frequency = {}

    for char in string_splt:

        if char in frequency:

            frequency[char] += 1

        else:

            frequency[char] = 1

    return max(frequency,key=frequency.get)
string="hello world world"
string_splt=string.split()
print(most_common_character(string_splt))"""




"""test_set="abcdef"
for id,val in enumerate(test_set):
    print(id)"""


"""dict1={1:"one"}
dict2={2:"two"}
dict1.update(dict2) 
print(dict1)
"""

"""dict={}
num_dict=int(input("nuber of dictionary items"))
for i in range(num_dict):
    key=input("key")
    value=input("value")
    dict[key]=value
print(dict)    
"""


"""dict={'1': 'a', '2': 'b', '3': 'c'}
dict1={}
for val,key in (dict.items()):
    if val!='2':
        dict1[key]=val
print(dict1)""" 



"""dict1 = {'ravi': 10, 'rajnish': 9,'sanjeev': 15, 'yash': 2, 'suraj': 32}
dict2={}
d=sorted(dict1.keys())
for i in (d):
    dict2[i]=dict1[i]
print(dict2)    """


"""def longest_common_prefix(strings):
    if not strings:
        return ""
    shortest_string=min(strings,key=len)
    for i,char in enumerate(shortest_string):
        for other_string in strings:
            if other_string[i]!=char:
                return shortest_string[:i]
    return  shortest_string 

strings = ["flower", "flow", "flight"]

prefix = longest_common_prefix(strings)

print(prefix)  """  



"""str="hello world hello python"
str1=str.split()
print(str1)
count={}
for i in str1:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count) 
for substring, count in count.items():

    if count == max(count.keys()):

        print(count[substring])
 """




"""def longest_common_prefix(strings):
    small_word=min(strings,key=len)
    #print(small_word)
    for i,char in enumerate(small_word):
        for words in strings:
            if words[i]!=char:
                return small_word[:-i]
   

 

strings = ["flower", "flow", "flight"]

prefix = longest_common_prefix(strings)

print(prefix)"""


"""
def most_common_character(string):

    frequency = {}

    for char in string:

        if char in frequency:

            frequency[char] += 1

        else:

            frequency[char] = 1

    print(max(frequency, key=frequency.get))
string="hello world"
most_common_character(string)
 """


"""dict={}
n=int(input("enter"))
for i in range(n):
    key=int(input())
    value=input()
    dict[i]=value
print(dict)    """




"""def longest_palindrom(s):
    longest=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring=s[i:j+1]
            if substring==substring[::-1]:
                if len(substring)>len(longest):
                    longest=substring
    return longest                


s="forgeeksskeegfor"
a=longest_palindrom(s)
print(a)"""



"""def longest_common_prefix(strings):
    small_word=min(strings,key=len)

    for i,ch in enumerate(small_word):
        for word in strings:
            if word[i]!=ch:
                return small_word[:i]




strings = ["flower", "flow", "flight"]

prefix = longest_common_prefix(strings)

print(prefix)"""



"""def test(str):
    vowel_str=""
    consonent=""
    vovels="aeiou"
    for i in str:
        if i in vovels:
            vowel_str=vowel_str+i
        else:
            consonent=consonent+i 
    print(vowel_str)
    print(consonent)      
str="hello welcome to python programming"
test(str)"""


"""string="gee@1ks"
count=0
for i,a in enumerate(string):
    
    count+=1
print(count)"""    

"""test_str = 'geeksforgeeks is best for geeks'
target="best"
str=test_str.split()
for i in str:
    if target==i:
        print(str.index(i))
    #print(i)"""      

"""test_str = 'for geeksforgeeks is best best for geeks is '
str=test_str.split()
print(set(str))"""



"""str = 'ABC'
for i in range(len(str)):
    for j in range(len(str)):
        for k in range(len(str)):
            if str[i]!=str[j] and str[j]!=str[k] and str[k]!=str[i]:
                print(str[i],str[j],str[k])"""



"""A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
A=A.split()
B=B.split()
x=[]
for i in A:
    if i not in B:
        x.append(i)
for i in B:
    if i not in A:
        x.append(i)
print(list(set(x) )) """       


"""num=100101010
num1=set(str(num))
s={'0', '1'}
if s==num1:
    print("yes")
else:
    print("no") """   


"""
str="geeks"
for i in range(len(str)):
    print(i)
    if i==3:
        str=str.replace(str[i],"")
        break
print(str) """ 


"""test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
for i in range(len(test_list)-1,-1,-1):
    print(test_list[i])"""


"""suff = 'x'

res=[i for i in test_list if i.endswith(suff)]
print(res)"""

"""for word in test_list[:]:
    if word.endswith(suff):
        test_list.remove(word)
print(test_list)"""



"""
str = " Jan = January; Feb = February; Mar = March"
dictionary=dict(str.split("=") for str in str.split(";"))
print(dictionary)
"""



"""dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict1.update(dict2)
print(dict1)"""


"""
test_list = ['gfg', ' ', ' ', 'is', '         ', 'best']
 

print("The original list is : " + str(test_list))

res = []
for ele in test_list:
    if ele.strip():
        res.append(ele)
     

print("List after filtering non-empty strings : " + str(res))
"""


"""str="   hello world    "
print(str.strip())"""

"""
import re
test_str = 'GFGaBste4oCS'
result=re.split('a|e|i|u',test_str)
print(result)"""



"""test_str = 'GFGaBste4oCS'
trans_table = str.maketrans('aeiouAEIOU', ' '*10)
res = test_str.translate(trans_table).split()
print("The splitted string : " + str(res))
"""

"""def distinct_anagrams(lst):
    anagram=set()
    for word in lst:
        sorted_word=''.join(sorted(word))
        anagram.add(sorted_word)
        return len(anagram)"""



"""try:
    my_list = []
  
    while True:
        my_list.append(int(input()))

except:
    print(my_list)"""

"""initial_set = set([12, 10, 13, 15, 8, 9])
initial_set.pop()
print(initial_set)"""



"""r=5
for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1)) """

"""r=5
for x in range(r):
    print(' '*(r-x-1)+'*'*(2*x+1))"""

"""list1 = [  2, 4, 6, 1, 8, 5, 3 ]
max_num=max(list1)
print(list1.index(max_num))   """    

"""list=[12, 33, 10, 20, 25]
num_lst=[i for i in list if i<=21]
print(num_lst)"""


"""list = ["Geeks", "For", "Geeks"]
list=list[:-2]
print(list)"""


"""data=[1,2,3,4,5,6,7]
result=[i*i for i in data if i%2!=0]
print(result)"""
# list=[]
# for i in range(1,21):
#     list.append(i)
# print(list)    
# for i in list:
#     if i%3==0:
#         print(i,"three")
#         break
# def test(num):
#     for i in range(1,num+1):
#         if i%3==0 and i%5==0:
#             print("threefive")
#         elif i%3==0:
#             print("three")   
#         elif i%5==0:
#             print("five")    
#         else:
#             print(i)  
# test(20)
# 
   



"""class Square:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def num(self):
        c=5
        print(self.a*self.b*c)
     
new = Square(2,3)
new.num()"""
"""
strings = ["flower", "flow", "flight"]
print(strings.index("flow"))"""


"""file=open("text.txt","r")
print(file.read())"""


"""list=[1,2,3,5]
for i in range(1,list[-1]):
    if i not in list:
        print("missing lalue is",i)"""



"""import sys
set={"a",1,"b",2,"c",3}
print(sys.getsizeof(set),"bytes")  """




"""def longest_palindrom(s):
    longest=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring=s[i:j+1]
            if substring==substring[::-1]:
                if len(substring)>len(longest):
                    longest=substring
    return longest                


s="forgeeksskeegfor"
a=longest_palindrom(s)
print(a)"""





"""def long_pal(str):
    longest=""
    for i in range(len(str)):
        for j in range(i,len(str)):
            string=str[i:j+1]
            if string==string[::-1]:
                if len(string)>len(longest):
                    longest=string
    print(longest)            
str="forgeeksskeegfor"
long_pal(str)"""


"""list=input("enter string ").split()
print(list)
len_lst=[len(i) for i in list]
print(max(len_lst))"""


"""list=input("enter").split()
print(list)
len_lst=[int(i) for i in list]
max_len=(max(len_lst))
print(max_len)"""



"""str="hello"
rev_str=""
for i in range (len(str)-1,-1,-1):
    rev_str=rev_str+str[i]
print(rev_str) """  
  
"""str_lst=input("entre ").split()
print(str_lst)
str_lst.sort()
print(str_lst)"""



"""list_num=input("enter ").split()
print(list_num)
list_num=[int(i) for i in list_num]
list_num.sort()
print(list_num)"""


"""str1=input("str1")
str2=input("str2")
str3=str1+" "+str2
print(str3)"""

"""
def vowel_count(str):
    count=0
    vowel="aeiouAEIOU"
    for i in str:
        if i in vowel:
            count+=1
    print(count) 
          
vowel_count("hello world")
"""


"""num_lst=input("enter").split()
print(num_lst)
num_lst=[int(i) for i in num_lst]
num_lst=[i for i in num_lst if i%2==0]
sum_even_lst=sum(num_lst)
print(sum_even_lst)"""



"""str_lst=input("enter").split()
print(str_lst)
str_lst=[i.upper() for i in str_lst]
print(str_lst)"""


"""num_lst=input("enter num ").split()
num_lst=[int(i) for i in num_lst]
num_lst_sum=[i for i in num_lst if i%3==0]
ans=sum(num_lst_sum)
print(ans)"""

"""
str=input("enter").split()
print(str)
len_str=len(str)
print(len_str)"""



"""str=input("entter ").split()
print(str)
str=[i[::-1] for i in str]
print(str)"""



"""list=input("enter").split()
print(list)
list=[int(i) for i in list]
even_lst=[i for i in list if i%2==0]
print(even_lst)"""

"""str="hello world"
vowel="aeiouAEIOU"
for i in str:
    if i in vowel:
        str=str.replace(i,"*")
print(str) """ 



"""list=input('eneter').split()
print(list)
list=(int(i) for i in list)
new_last=[i for i in list if i>10]
print(new_last)"""

"""string=input("enter string")
string=string.replace(" ","")
print(string)"""


"""
def count_vowel(strings):
    vowels="aeiouAEIOU"
    count=0
    for char in strings:
        if char in vowels:
            count+=1
    return count
def sort_by_vowel(strings):
    return sorted(strings,key=count_vowel)



strings = ["hello", "world", "apple", "banana", "cat", "dog"]
print(sort_by_vowel(strings))"""

"""def count_vowel(strings):
    dict={}
    vowel="aeiouAEIOU"
    for word in strings:
        count=0
        for ch in word:
            if ch in vowel:
                
                count+=1
                dict[ch]=count
            print(dict)            


strings = ["hello", "world", "apple", "banana", "cat", "dog"]
print(count_vowel(strings))"""




"""def len_num(list):
    return len(str(list))

def ln_lst(list):
    return sorted(list,key=len_num)  


list=[123, 45, 6789, 0,1, 555]
print(ln_lst(list))"""


"""def sorted_touple(touples):
    return sorted(tuples,key=lambda x:x[1])
tuples = [(1, "apple"), (3, "banana"), (2, "cat"), (5, "dog"), (4, "elephant")]
print(sorted_touple(tuples))"""


"""
def sorted_toupl(touples):
    return sorted(touples,key=lambda x:x[1])
tuples = [(1, "apple"), (3, "banana"), (2, "cat"), (5, "dog"), (4, "elephant")]
print(sorted_toupl(tuples))"""



"""def sort_by_key(dicts,key):
    return sorted(dicts,key=lambda x:x["age"])
dicts = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]
print(sort_by_key(dicts,"age"))"""

"""
def longest_common_prefix(strings):
    small_word=min(strings,key=len)
    print(small_word)
    for i,ch in  enumerate(small_word):
        print(i,ch)
        for words in strings:
            if words[i]!=ch:
                return small_word[:i]
    return small_word    

     
strings = ["flower", "flow", "flight"]
print( longest_common_prefix(strings))"""




"""
def longest_common_prefix(strings):
    small_word=min(strings,key=len)
    #print(small_word)
    for index,char in enumerate(small_word):
        #print(index,char)
        for words in strings:
            #print(words)
            if words[index]!=char:
                return small_word[:index]

     
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))
"""


"""def most_common_character(str):
    freq={}
    for i in str:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    return max(freq,key=freq.get)           

print(most_common_character("hello"))"""


"""dict={
    2:"two",
    1:"one",
    4:"four"
    3:"three"
}

dict1={}

d=sorted(dict.keys())
for i in d:
    dict1[i]=dict[i]
print(dict1)    """












"""string="hello welcome to world"
ans_lst=[]
str_lst=string.split()
print(str_lst)
for i in str_lst:
    ans_lst.append([i,len(i)])
print(ans_lst)  
sorted_len_lst=sorted(ans_lst,key=lambda x:x[1]) 
print(sorted_len_lst[0])
"""


"""nums = [123, 45, 6789, 1, 0, 555]
nums_len=[]
for i in nums:
    nums_len.append([i,len(str(i))])
print(nums_len)   
ans=sorted(nums_len,key=lambda x:x[1]) 
print("biggest,word",ans[-1])
print("small,num",ans[0])
"""

"""
tuples = [(1, "apple"), (3, "banana"), (2, "cat"), (5, "dog"), (4, "elephant")]
print(sorted(tuples,key=lambda x:x[0]))"""










































