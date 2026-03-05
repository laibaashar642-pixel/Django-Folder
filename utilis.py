#so ye aik random si file hum nai bnayi aur hum django kai shell kai through run kry gai iskokun kai ye python ki file direct run nai ho skti that why kun kai ye django kai diifernet cheezon ko use krti hai
from home.models import Student
def runthisfunction():
    print("Hello ! I run through shell") # so it gives me error
    import time
    time.sleep(1)#means itny second kai baad ye chly
    print("I am running after this")
"""     Use exit() or Ctrl-Z plus Return to exit
>>> from home.utilis import *
>>> runthisfunction()
Hello ! I run through shell
I am running after this
>>>  """