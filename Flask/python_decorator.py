import time

def delay_decorator(fun):
    def wrapper_decorator():
        time.sleep(2)
        fun()
    return wrapper_decorator

@delay_decorator
def hello_fun():
    print("Hello world")

def Bye_fun():
    print("Byeee")

@delay_decorator
def Food_fun():
    print("Food preparing...")    

hello_fun()    

