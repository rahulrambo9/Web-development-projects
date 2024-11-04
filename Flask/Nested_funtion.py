def outer_fun():
    print("I am outer fun")
    
    def inner_fun():
        print ("I am inner fun")
    return inner_fun    

in_fun = outer_fun()       
in_fun()