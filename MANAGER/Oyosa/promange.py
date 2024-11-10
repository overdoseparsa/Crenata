import sys 
import os
from pathlib import Path
from subprocess import check_call
BASE_DIR = Path(__file__).resolve().parent.parent
# This is work ok >
# the command of manage.py to the simple dict 
def append_path(manger)->list:
    ''' create the django syntax python3 manage.py input  '''
    return f"python3 manage.py {manger}".split(' ')
    
commands_manger = {
    'makestart':map(append_path, ['makemigrations'  , 'migrate' , 'runserver']) , 
    'migrate':[append_path('migrate')] ,

    # ...
}

    

def Apply_Managepy(arg)->None:
    """
    this function it's  when start the promanage.py 

    """
    print("closeing the port : 8000")
    os.system(
        'sudo fuser -k 8000/tcp'
    )
    print('that port was close')
    print("this is closed")
    for command in (commands_manger.get(arg)):
        check_call(command)
    

if __name__ =="__main__":
    print(
        sys.argv[1]
    )
    Apply_Managepy(
        sys.argv[1]
    )