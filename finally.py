def asd():
    try:
        1-'kjllk'
    
    except:
        print('except')
        
    else:
        print('rtyui')
    
    finally:
        print('Hello, World')
    

print(asd())
print(type(None))

class MyError(Exception):
    pass
raise MyError('pass = pass')