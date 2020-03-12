from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
print('heloo baabtra')


def fn_myfun(**amounts):
    print(amounts)
def fn_fact(num):
    
    if num == 0:
        return 1
    else:
        return num*fn_fact(num-1)    

def app(request):
    fn_myfun(amount1=100,amount2=200,amount3=300)
    num = int(input("Enter a number: "))
    fact=fn_fact(num)
    print (fact)
    return HttpResponse('welcome to programming')


def fn_sample(request):
    my_name = input('enter your name: ')
    print(my_name)
    print(type(my_name))
    return HttpResponse(my_name)
def fn_add(request):
    a=int(input("enter 1st number: "))
    b=int(input("enter 2nd number: "))
    c=a+b
    return HttpResponse(c)
def fn_number(request):
    my_data = input("enter sring:")
    print(my_data)
    print(len(my_data))
    print(my_data[0])
    print(my_data[0:3])
    print(my_data[3:])
def fn_list(request):
    my_list=[10,25,'baabtra']
    my_list.append('ramya')
    my_list.insert(0,'hari')
    print(my_list)
    my_tuple=(100,9,'gg')
    print(my_tuple)
def fn_dict(request):
    my_dict={"name":"nouse","age":23,"place":"calicut"}
    # print(my_dict["place"])
    # for data in my_dict.values():
    #     print(data)
    for data1,data2 in my_dict.items():
        print(data1,':',data2)
def fn_data(request):
    my_list=['data1','data2','data3']
    for data in range(0,len(my_list),1):
        print(my_list[data])    
        print(data)
def fn_num(request):
    n=int(input("enter number")) 
    # if(n%2==0):
    #     print("even")
    # else:print("odd") 
def fn_week(request):
    n=int(input("enter number"))
    if(n==1):
        print("sundy")
    elif(n==2):
        print("mondy")
    elif(n==2):
        print("tues")
    elif(n==2):
        print("wedn")
    else:
        print("wrong value")
def fn_and(request): 
    n=int(input("enter number"))
    if(n%2==0 and n<20):
        print("valid")
    else:
        print("invalid")
def fn_prime(request):
    n=int(input("enter the number:")
    if n>1:
        for i in range(2,n):
        if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",n//i,"is",n)
           break
        else:
            print(n,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")
           
 





