class ZombiePy : 
    def __init__ (self,name,height,hobby):
        self.name = name
        self.height = height
        self.hobby = hobby
    def greet (self) :
        print(f'Hello {self.name}')
obj = ZombiePy('Tyrant',1000000,'Killing Stupid People')
obj.greet()
        