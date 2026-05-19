def my_calulator(a,b, instruction="sum"):
    if instruction == "sum":
        return a+b
    elif instruction == "sub":
        return a-b
    elif instruction == "mul":
        return a*b
    elif instruction == "div":
        return a/b
    else:
        return "invalid operation"
    
print(my_calulator(5,3,"sum"))
print(my_calulator(5,3,"sub"))
print(my_calulator(5,3,"mul"))
print(my_calulator(5,3,"sum"))
print(my_calulator(5,3,"mod"))
