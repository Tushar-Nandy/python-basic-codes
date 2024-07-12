class Teacher():
    def __init__(self,name,time_alloated,lec1=None,lec2=None,lec3=None,lec4=None) -> None:
        self.name=name
        self.sub1=lec1
        self.sub2=lec2
        self.sub3=lec3
        self.sub4=lec4
        self.time=time_alloated
    def info(self):
        print(f"{self.name} teaches {self.sub1,self.sub2,self.sub3,self.sub4} for {self.time} hrs.")

