# ###
# try:
#     # Code that might raise an exception
# except:
#     # Code to handle all exceptions
# except SomeException as e
#     # Code to handle particular exceptions
# else:
#     # Code If no exception is raised
# finally:
#     # Code which always runs
# ###

# WORKS FOR BOTH RUNTIME AND COMPILE TIME ERRORS

a = 1   # a = [1,2,3,4]
b = 0   # No var 'b'
c = "c"
d = "10"

try:                            # Code we want to run that might raise an exception
    # print(a/b)
    print(int(c))
    print(int(d))       # Does not Run as it goes from above stm to Exception block then directly to Finally Block

# Can also mix 2 or more errors in one block
# except (ValueError,ZeroDivisionError):
# print("")

except ValueError:
    print("This is ValueError")
except ZeroDivisionError:
    print("This is Zero Division Error")      # Outputs when b = 0
except Exception as e:
    print("Try block has error: ", e)       # Outputs when we try to print 'b'
else:
    print("Try block has no error")         # Outputs when we try to print 'a'
finally:
    print("End of Exception handling")      # Always prints