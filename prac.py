
"""def longest_palindrom(str):
    longest=""
    for i in range(len(str)):
        for j in range(i,len(str)):
            substring=str[i:j+1]
            if substring==substring[::-1]:
                if len(substring)>len(longest):
                    longest=substring
    return longest

str="forgeeksskeegfor"
print(longest_palindrom(str))"""




"""list=[2,4,5,6,7,8,9,5,10]
ans=[]
target=6
for i in range (len(list)):
    for j in range(i,len(list)):
        if list[i]+list[j]==target:
            ans.append([list[i],list[j]])
print(ans) """           


"""class Circle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area_of_circle(self):
        return 3.14*self.base*self.height
obj=Circle(12,8)
print(obj.area_of_circle())   """     