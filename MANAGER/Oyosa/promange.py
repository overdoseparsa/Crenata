import sys 
import os
from pathlib import Path
from subprocess import check_call
BASE_DIR = Path(__file__).resolve().parent.parent

# the command of manage.py to the simple dict 
def append_path(manger)->list:
    return f"python3 manage.py {manger}".split(' ')
    
commands_manger = {
    'makestart':map(append_path, ['makemigrations'  , 'migrate' , 'runserver'])
    # ...
}

    

def Apply_Managepy(arg)->None:
    """
    this func start the promanage.py 
    """
    print("closeing 8000")
    os.system(
        'sudo fuser -k 8000/tcp'
    )
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