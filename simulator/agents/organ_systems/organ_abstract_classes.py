from abc import ABCMeta, abstractmethod, abstractproperty



class OrganSystem(metaclass=ABCMeta):

    
    @classmethod
    @abstractmethod 
    def setBelongsRelations(cls):
        #name = None 
        #agent = None 
        pass
    
    @classmethod
    @abstractmethod 
    def setBiologicalData(cls):
        pass


class Organ(metaclass=ABCMeta):


    @classmethod
    @abstractmethod 
    def setBelongsRelations(cls):
        #name = None 
        #organSystem = None 
        #agent = None 
        pass

    @classmethod
    @abstractmethod 
    def setBiologicalData(cls):
        pass


class SubOrgan(metaclass=ABCMeta):


    @classmethod
    @abstractmethod 
    def setBelongsRelations(cls):
        #name = None 
        #parentOrgan = None 
        pass

    @classmethod
    @abstractmethod 
    def setBiologicalData(cls):
        pass

