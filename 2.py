d3={'k1':5 , 'k2': [1,2,3,4] , 'k3' : {'a':1 , 'b':2 , 'c': [4,5,6]}}
print(d3.get('k3'))
print(d3.get('k3').get('c'))

#################################################################################

############################################################################

var='spam'
if var=='spam':
    print('spam')
var2='girl'
if var2=='girl':
    print("girl")
elif var=='boy':
    print("boy")

#############################################################################

var2='girl'
if var2=='girl':
    print("girl")
elif var=='boy':
    print("boy")
else:
    print("helllllllllllllllllllooooooooooooooooo")

############################################################################

numbers=range(0,10)
for number in numbers:
    if number<3:
        print(number)
    else:
        break
else:
    print("loop exited normally")

##############################################################################

number=5
while number>0:
    print(number)
    number-=1

##############################################################################

shopinglist=['eggs','ham','bacon']
try:
    print(shopinglist[3])
except IndexError as e:
    print('exception:' + str(e) + ' has occured')
else:
    print('no exceptions occured')
finally:
    print('I will always execute no matter what')

##############################################################################

shopinglist=['eggs','ham','bacon']
try:
    print(shopinglist[2])
except IndexError as e:
    print('exception:' + str(e) + ' has occured')
else:
    print('no exceptions occured')
finally:
    print('I will always execute no matter what')

###############################################################################

def myfunction(number):
    return number*number
print(myfunction(5))

################################################################################

def moreargument(*args):
    squared_args = []
    for item in args:
        squared_args.append(item * item)
    return squared_args
print(moreargument(1,2,3,4))

#################################################################################

def person_details(**kwargs):
    for key, value in kwargs.items():
        print(key, '----->' ,value)

person_details(Name='zahra gaasabei' , Alias='zarey' , job='student')

#################################################################################

numbers=range(5)
def recursive_squares(numbers):
    if not numbers:
        return []
    else:
        return [numbers[0]*numbers[0]] + recursive_squares(numbers[1:])

print(recursive_squares(numbers))

####################################################################################

numbers=range(9)
numbers
print(set(num%2 for num in numbers ))

#####################################################################################

numbers=range(9)
print(numbers)
print([num * num for num in numbers])

######################################################################################

numbers=range(9)
numbers

print({num: num * num for num in numbers})

######################################################################################

numbers=range(9)
numbers

print([{'Number' : num , 'Square':num*num , 'Type':'even' if num%2==0 else 'odd'} for num in numbers])

#######################################################################################

numbers=[1,2,3,4,5]
def generate_squares(numbers):
    for number in numbers:
        yield number * number
gen_obj=generate_squares(numbers)
gen_obj
for item in gen_obj:
    print(item)

#########################################################################################

csv_string='The, covid19 , is , most, hazardous , virus, thorough , the , life'
gen_obj=(item for item in csv_string.split(','))
student=' '.join(gen_obj)
print(student)

###########################################################################################

class ANIMAL(object):
    species='Animal'

    def __init__(self , name):
        self.name=name=name
        self.attributes=[]

    def add_atrutesib(self, attributes):
        self.attributes.extend(attributes)
        if type(attributes)==list:
            pass
        else:
            self.attributes.append(attributes)

    def __str__(self):
        return self.name+" is type of"+ self.species +"and has attributes:"+ str(self.attributes)

a1=ANIMAL('ZEBRA')
a1.add_atrutesib(['runs','eats','wild'])
print(str(a1))

#########################################################################################


