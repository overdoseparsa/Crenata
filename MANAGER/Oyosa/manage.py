#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from collections import UserDict # TODO یه کاکشن تایبی که بتونم کنترل کنم تای
get_or_replace_env_ = lambda get , replace_if_not  : os.environ.get(get  , replace_if_not)
ver_error = """
you dont have add Enviremen Variable PATH for external settings_logs 
to config you have two choice 
1)add export SETTINGS_PATH="your settings path" 
2)or change your config of TYPE_SETTINGS to defualt internal 
"""
def create_difrents(iter1:list,iter2:list)->list:
    """
    This is the temporary function to get the difrentes two list in a new list 
    """.title()

    resualt = []
    for va in iter2 : 
        if not (va in iter1) :
            resualt.append(va)
    return resualt 


def main():
    # settings is ceateed 
    """Run administrative tasks.""" # this is defualt  # defualt dict 
    def PACKING_PATH_SEETINGS():
        data_type_settings = {  # use lambda functions 
            "internal":True  , 
            "external":False , 

        }
        settings_log =  {
            'type':data_type_settings.get(get_or_replace_env_('TYPE_SETTINGS'  , "internal")) , 
            'Path':get_or_replace_env_('SETTINGS_PATH' ,None) # what im i do 
        }

        
        if settings_log['type']:
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Oyosa.settings') # settings is the file.py settings here


        else : 
            print(
                'we user external'.title() , settings_log['type']
            )
            Path_join:str = settings_log['Path'] # this is from path join 
            print(Path_join)

            if (not Path_join):
                from GUICONTROLL.settings import Gui  # this is start 
                PACKING_PATH_SEETINGS() #  تابع بازگشتی 
                

            else : 
                os.environ.setdefault('DJANGO_SETTINGS_MODULE' , '.'.join(create_difrents(os.getcwd().split('/')
                ,  Path_join.split('/')))[:-3])
                print('.'.join(create_difrents(os.getcwd().split('/')
                ,  Path_join.split('/')))) # this is for test 
    PACKING_PATH_SEETINGS() # CALL FUNCTIONS 

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
