#Exceptions in Python:
#NameError,ZeroDivisionError,SyntaxError,IndexError,
#KeyError,IOError,AttributeError......

#Detecting and handling Exceptions:
try:
    try_suite
except Exception[,reason]:
    except_suite

def safe_float(obj):
   try:
       retval=float(obj)
   except ValueError:
       retval='Could not convert non-number to float'
   return(retval)
   
#Multiple except Statements:   
#except statement with mutipile Exceptions:
except (ValueError，TypeError)：

#Catching All Exceptions：
except Exception:
# class Exception(BaseException)- Common base class for all non-exit exceptions.  

#else Clause

#finally Clause:try-except-else-finally


#with Statement:
with context_expr [as var]:
    with_suite
