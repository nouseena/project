def fn_part(n): 
    for i in range(1, n+1): 
        for j in range(1,i+1): 
            print("*",end =" ") 
        print("\r")  
def display(request):
    n=int(input("enter number"))
    fn_part(n)            