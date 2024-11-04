class User:
    def __init__(self, name):
        self.name = name 
        self.is_logged_in = False

#*args  --> called positional argument
# **kwargs --> called keyword argument
#

def is_authenticated_decorater(fun):
    def wrapper (*args, **kwargs):
        if args[0].is_logged_in == True:
           fun(args[0])
    return wrapper            

@is_authenticated_decorater
def user_blog(user):
    print(f"this is {user.name}'s blog post !!")

new_user = User("Rahul")
new_user.is_logged_in = True
user_blog(new_user)            