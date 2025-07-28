# Compress a string using character counts.
# Input: "aabbbcc" → Output: "a2b3c2"
# s="aabbbcc"
# x=""
# y=""
# for i in range(len(s)-1):
#     if s[i] not in y:
#         y+=s[i]
#         x+=s[i]
#         x+=str(s.count(s[i]))
# print(x)
  

# Convert a string to title case without using .title().
#  Input: "python is fun" → Output: "Python Is Fun

# s="python is fun"
# y=""
# z="" 
# y+=s[0].capitalize()
# for i in range(len(s)):
#     if s[i]== " ":
#         y+=" "
#         y+=s[i+1].capitalize()
#     else:
#         y+=s[i]
# print(y)
# z+=y[0]
# for j in range(len(y)-1):
#     m=ord(y[j])+32
#     n=chr(m)
#     if y[j+1]!=n:
#         z+=y[j+1]
# print(z)


# Check whether two strings are anagrams of each other.
# s="gum"
# t="mug"
# x="false"
# for i in s:
#     if i in t and len(s)==len(t):
#         x="true"
#     else:
#         false
#         break
# print(x)

# Convert a string "1a2b3c" to "abc123".

# s="1a2b3c"
# x=""
# y=""
# for i in range(len(s)):
#     if s[i].isdigit():
#         x+=s[i]
#     else:
#         y+=s[i]
# print(y+x)

# Extract all numbers from a string and calculate their sum.
#  "abc12xyz34" → Output: 46
# s="abc12xyz34"
# sum=0
# for i in range(len(s)-1):
#      if s[i].isalpha():
#           continue
#      else:
#           if s[i].isdigit() and s[i+1].isdigit():
#                sum+=int(s[i]+s[i+1])
# print(sum)
               
# Sort a list in ascending and descending order with out using sort?
# ascending
# l1=[7,22,9,776,12,8,54]
# l2=[]
# for i in range(len(l1)-1):
#         for j in range(i+1,len(l1)):
#              if l1[i]>=l1[j]:
#                     l1[i],l1[j]=l1[j],l1[i]
            
# print(l1)

# descending
# l1=[7,22,9,776,12,8,54]
# l2=[]
# for i in range(len(l1)-1):
#         for j in range(i+1,len(l1)):
#              if l1[i]<=l1[j]:
#                     l1[i],l1[j]=l1[j],l1[i]
            
# print(l1)

# Find the second largest number in a list
# l1=[7,2,99,77,12,82,54]
# smax=0
# l1.sort()
# print(l1)
# smax=l1[len(l1)-2]
# print(smax)

#  Find the intersection and union of two lists.
# l1=[7,12,99,77,82,54]
# l2=[77,22,9,7,12,8,54]
# print(l1+l2)     # unioun
# for i in l1:
#     if i in l2:
#         print(i) # intersection

# Print all prime numbers from a list.
# l1=[77,22,9,7,12,8,54]
# l2=[]
# ct=0
# for i in range(len(l1)):
#     for j in range(2,l1[i]):
#         if l1[i]%j==0:
#             ct=1
#             break
#         else:
#             ct=0
#     if ct<1:
#        l2.append(l1[i])
# print(l2)

# . Find if a number is Armstrong or not.
# n=153
# m=n
# temp=n
# ct=0
# sum=0
# while n>0:
#     ct+=1
#     digit=n%10 
#     n=n//10
# while m>0:
#     digit=m%10
#     m=m//10
#     sum+=digit**ct
# if sum==temp:
#   print("is armstrong")
# else:
#    print("not a armstrong")

#. Count number of vowels in a string using while.\

# s="anfdie ytulsn"
# ct=0
# for i in s:
#     if i in "AEIOUaeiou":
#         ct+=1
# print(ct)

#Print multiplication table in reverse order.
# n=5
# for i in range(10,0,-1):
#     print(n,"*",i,"=",(n*i))

# Count how many times digit 7 appears between 1 to 100 --->
# ct=1
# for i in range(1,100):
#     if i==7:
#         ct+=1
#     elif i== 
# print(ct)

#Replace all negative numbers in a list with 0. Using list comprehention?  ---->
# l1=[34,-23,-6,5,8,-99]
# res=[i  if i>0  else 0 for i in l1]
# print(res)


# Write Function to check if a list is sorted or not.
# def fun(l1):
#     for i in range(len(l1)-1):
#         for j in range(i+1,len(l1)):
#              if l1[i]>=l1[j]:
#                     l1[i],l1[j]=l1[j],l1[i]
#     return l1
# x=fun([92,33,4,53,72])
# l2=[4,33,53,72,92]
# if l2 == x:
#      print("is sorted")
# else:
#      print("not sorted")


#Store student names and marks in a dictionary and print each student’s result.
# d={'nave':{'telugu':23,'Hindi':56,'Eng':67,'math':98,'science':35},
#    'suni':{'telugu':23,'Hindi':56,'Eng':67,'math':98,'science':35}}
# for x in d.items():
#      print(x)

# 17. Sort a dictionary by values
# d={'a':100,'b':34,'c':98,'d':45}
# d1={}
# for i,j in d.items():
#       d1=sorted(d.values())
# print(d1)


#. Write a lambda function that takes two numbers and returns a tuple containing:
# i. Their sum.    # ii. Their product.   # iii. Their difference
    

# x1=lambda x,y :x+y
# x2=lambda x,y :x*y
# x3=lambda x,y :x-y
# x=(x1(10,20),x2(30,20),x3(60,30))
# print(x)

  