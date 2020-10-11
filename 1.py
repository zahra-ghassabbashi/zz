intnumber = 976123
print('your Integer number:', intnumber)
floatnumber = 989.45
print('your Real number:', floatnumber)
a = input("please enter a float number:")
b = input("please enter a second number:")
c = int(a) * int(b);
print(c)

#########################################################

a = input("please enter a float number:")
b = input("please enter a second number:")
c = int(a) * int(b);
print(c)
division = float(a)/int(b)
print(division)

############################################################

fname=input("your desired name:")
lname=input("your family name:")
print("full name :", fname+" "+lname)
specialchar="*"
print(specialchar*100)

##############################################################
num1=input("please enter a base number:")
pow=input("please enter a number for power:")
result=int(num1)**int(pow)
print("Result is:",result)

###############################################################

text="is there any professional programmer here?!"
print(text)
print(text[0])
print(text[0:5])
print(text[2:5])

################################################################

mylist=[1,2,99.6,[44,444],"hello"]
print(mylist)
print(len(mylist))
print(mylist[4])
print(mylist[2:4])
for item in mylist:
    print(item)

################################################################

mylist=[1,2,99.6,[44,444],"hello"]
print(mylist)
print(len(mylist))
print(mylist[4])
print(mylist[2:4])
print(mylist[3] [1])

##################################################################

mylist2=[3,2,99.6,[698,4244],"student"]
mylist2.append(99)
mylist2.insert(0,"helli")
print(mylist2)
mylist2.remove(99)
del(mylist2[0])
print(mylist2)

##################################################################

mylist2=[3,2,99.6,[698,4244],"student"]
print(mylist2)
mylist2.append(mylist2)
print(mylist2[5][5])

#################################################################

mylist2=[3,2,99.6,7,1,10]
mylist2.sort()
print(mylist2)
mylist2.reverse()
print(mylist2)

#################################################################
