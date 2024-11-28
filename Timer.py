import time

#function definition
def countdown_timer(seconds):
    while seconds>0:
       mins=int(seconds/60)
       secs=int(seconds%60)
       timer=f'{mins}:{secs}'
       print(timer)
       time.sleep(1)
       seconds-=1
    print("time is up")
seconds=input("Enter the time in seconds: ")
#function call
countdown_timer(int(seconds))
