import json 
from collections import UserDict
import os 
from abc import abstractmethod

"""
TODO 
1 :) create a type for name file 
'''
class nameos():...

'''
TODO MABY DONE 
2 :) thinking about what the comman attrbuite and appening mixin 
''' it will use in a mult classes maby '''

STEP : 
create the json and wirtie files 

TODO it is not bad thinkings 
3 :)
create a class for open and close json file 

TODO MAYBY DONE 
4 :)  

append add to virtual  json  

"""
class MixinJsonMangerFile():
    @abstractmethod 
    def __init__(self , json_file) -> None: # if have json 
        ''

class jsonManagerFile(MixinJsonMangerFile): # this manager from connector json dict style 
    
    def __init__(self , json_file , **kwargs) -> None:
        self.file_name = json_file
        super().__init__(json_file)



    @staticmethod
    def open_file(nameFile  , Type):
        pass
    def Json_open(self):
        with open(self.file_name , 'r') as JSONFILE :
            self.open_file
            static_json = json.loads(JSONFILE.read()) # this is return dict sytle 
        
        JSONFILE.close()
        return static_json
    def Json_add(self , values):# it will be to create wihout overlodings add to the futuer TODO 
        '''  adding wihout overlodings  '''

    def Json_OverLoad(self , values:UserDict): # this is just overlode and write overloded json 
        self.open_file # TODO add this open file manager 
        with open(self.file_name, 'w+') as JSONFILE : 
            JSONFILE.write(json.dumps(values))
            JSONFILE.close()
        

    


 

class MixinJsonModels():
    @staticmethod
    def add_json_dict_file():...
    @staticmethod
    def add_dict_to_dict():...
    @staticmethod
    def extends_dicts(*args)->dict:
        ''' This is The simple dict extender without deplicate keys '''
        new_dict = {}
        for d in args : 
            for key in d : 
                if key not in new_dict: 
                    new_dict[key] = d[key]
                else : 
                    continue

        return new_dict
        

    def __init__(self , name:str, *args , **kwargs) -> None:
        self._virtutlated_json = kwargs.get('base_json') or {} # we retrive from json and alter to dict  # this is cahce dict dumpit 
        self.combine_name =  kwargs.get('combine') or 'CombinJson'
        self.name = name
    def add(self ,tree_name, **kwargs):
        """ This is the simple adding """
        self._virtutlated_json[tree_name] = kwargs
    

    def retrive(self , *args , **kwargs):
        pass # when i wanted toretivre open it when i want want rto witre no need else 

    def remove(self , treename):
        del self._virtutlated_json[treename]

    def save(self):
        # alter dict_venv to the json file python 
        pass # this is append to the dabase 
    def update(self , save = True):
        pass
    def append(self , treename , **kwargs):
        pass


    def __add__(self , jsclass):
        
        return MixinJsonModels(
            self.name + '<->' + jsclass.name , base_json = self.__class__.extends_dicts(self.virtutlated_json , jsclass.virtutlated_json) 
        )
    def __radd__(self , jsclass): 
        return self.__add__(jsclass)


    def __str__(self) -> str:
        return json.dumps(self._virtutlated_json)
    def __repr__(self) -> str: # create dattime error 
        return f'{self.__class__.__name__}(name = {self.name!r} ,**{dict(base_json = self._virtutlated_json)!r})'
    
    
class JsonModels(MixinJsonModels): 
    def __init__(self , name , **kwargs) -> None: # we overload all things 
        self.json_manager = jsonManagerFile(name) 
        super().__init__(name , **kwargs)

    def add(self, tree_name, **kwargs):
        return super().add(tree_name, **kwargs)

    def save(self): # that is done 
        self.json_manager.Json_OverLoad(self._virtutlated_json)
        return super().save()

    def append(self, treename, **kwargs):
        """this is when using we use """
        self.cache_j_v = self.virtutlated_json[treename]
        print('8'*20)
        print(kwargs)
        for key  in kwargs : 
            assert key in self.cache_j_v  , f'we havend this columns from {treename}'

            self.cache_j_v[key].extend(kwargs[key])
        print('this is cache' , self.cache_j_v)

        self._virtutlated_json[treename] = self.cache_j_v
        self.save()
        # this is the simple append 
        return super().append(treename, **kwargs)


    @property 
    def virtutlated_json(self):
        self.save() # alter dict  

        return self.json_manager.Json_open()
    @virtutlated_json.setter
    def virtutlated_json(self , jsonDict): # this is update virtual json 
        
        self._virtutlated_json = jsonDict
        self.save()

from pprint import pprint
import datetime
now = lambda : str(datetime.datetime.now())
def main_Test_from_mixin():
    test = MixinJsonModels(
        'testTable' , 
    )
    test2 = MixinJsonModels(
        'newtable'
    )


    pprint(test)
    test.add(
        'ParsaTable' , posts = [
        {
         'title':'hello this is test'  , 
         'test.virtutlated_json(time':   now() , 
         'text' : 'this is simple text'
        } , 


        ]
    )

    test2.add(
        tree_name='SepehrTable' , posts = [
                    {
                    'title':'1'  , 
                    'time':   now() , 
                    'text' : 'dont care about timme'
                    } 
                    
        ]
    )
    print(
        test.virtutlated_json
    )

    print('----------------')
    print(test2.virtutlated_json)
    print('*'*20)




    test3 = test + test2
    print(
        test3.virtutlated_json
    )




def main_test_two():
    parsa = JsonModels(
        'parsa.json' 
    )
    #print(parsa , repr(parsa))
    #repr_test_object = JsonModels(name = 'parsa.json' , **{'base_json': {}})
    
    
    post_data = [
        {
            'title':'hello' , 
            'body' : 'hello to every one' , 
            'time':now()
        } , 
        {
         'title':'hello this is test'  , 
         'test.virtutlated_json(time':   now() , 
         'text' : 'this is simple text'
        } , 
        {
         'title':'asdsadst'  , 
         'test.virtutlated_json(time':   now() , 
         'text' : 'this is simple text'
        } , 
    ]
    parsa.add( tree_name='parsa_khakiy' , 
        post = post_data
    )
    parsa.save()

    parsa.append(
        'parsa_khakiy' , post = [{'title':'afdsafaffascsaasdasdada'}]
        
    )
    print('*'*20)
    print('this is saved append' , parsa)
if __name__ =="__main__":
    main_test_two()

