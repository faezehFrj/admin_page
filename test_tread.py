##Program to demonstrate the if cancel() function cancels the start() function or the Timer object itself
import threading as th
## Creating a function
def prnt():
    print("EDU CBA \n")
T = th.Timer(3.0, prnt)
T.cancel()

T = th.Timer(3.0, prnt)
T.start()
print("Exit Program\n")