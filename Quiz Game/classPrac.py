class User:
    """Takes two values, name,userId. 
    Used to create a new user"""
    #__init__() function is clled as soon as we make an object, it mainly contains attributes
    def __init__(self,name,id) -> None:
        self.id=id
        self.name=name
        self.followers=0
        self.following=0

        print(f"Created a new user {name}")
    def follow(self,user):
        self.following+=1
        user.followers+=1

user_1=User("Jake","001")
print(user_1.id)
user_2=User("Queen","002")
print(user_2.name)
print(user_1.followers,user_2.followers)
user_1.follow(user_2)
print(user_1.followers,user_1.following)
print(user_2.followers,user_2.following)