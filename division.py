#function definition
def div(a:int,b:int):
    if b==0:
        return ZeroDivisionError
    else:
        d=a//b
        return d
