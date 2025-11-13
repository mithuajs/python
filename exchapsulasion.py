class Employee :
    def __init__( self,name , salary, dept ):
        self .name = name 
        self .salary= salary
        self . dept = dept 
    def display (self):
        print ('name:', self . name, 'salary:', self. salary)
    def work (self):
        print (self.name, 'is working on', self.dept)
emp = Employee ('Mobasher' , 40000 ,'computer')
emp.display ()
emp.work()
