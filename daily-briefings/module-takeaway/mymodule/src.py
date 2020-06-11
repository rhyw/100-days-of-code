import sys
import datetime

version = "1.0"
__all__ = ['today', 'echo_date', 'echo_time']


today = datetime.datetime.now()

def echo_date():
    print(today.strftime('%Y-%m-%d'))


def echo_time():
    print(today.strftime('%H:%M:%S'))
    
