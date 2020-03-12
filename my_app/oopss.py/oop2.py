class Admin:
    def __init__(self,name,age,username,password):
        self.name   = name
        self.age    = age
        self.uname  = username
        self.pasword= password
    def fn_display(self):
        print('name:'+self.name)
        print('username:'+self.uname)
class Student(Admin):
    def __init__(self,name,age,username,password,batch):
        Admin. __init__(self,name,age,username,password)
        self.batch = batch
    def displayStudent(self):
        print('student detailsss')
        self.fn_display()
        print(self.batch)


admin = Admin('nouseena',23,'nouseena@gmail.com','123##')
admin.fn_display()
stud = Student('nouse',23,'nouseena@gmail.com','123345','python')
stud.displayStudent()
