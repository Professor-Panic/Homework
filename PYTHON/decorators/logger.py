import time
from datetime import datetime,date
def logger(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        today=date.today()
        duration=round((end_time-start_time)*1000,2)
        timestamp=datetime.now().isoformat()
        with open(f"{today}.txt","a") as f:
            f.write(f"{timestamp} : function:{func.__name__}  duration:{duration}.ms\n")
    return wrapper
@logger
def hello():
    print("hello")
@logger
def big_count():
    for i in range(100000):
        print(i)
        pass
big_count()