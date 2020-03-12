class employee:
    def __init__(self,name,age,username,password):
        self.name   = name
        self.age    = age
        self.uname  = username
        self.pasword= password
    def fn_display(self):
        print('name:'+self.name)
        print('age:',self.age)

employee1=employee('nouseena',23,'nouseena@gmail.com','123##')
employee1.fn_display()
