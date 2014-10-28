
from simulate import ureg
from organ_systems import cardiac_system
from organ_systems import lower_gastrointestinal_system

class Agent(object):

    def __init__(self, name='agent', sex='male', age = 0 * ureg('year')):
        self.name = name 
        self.sex = sex
        self.age = age

        # define systems 
        self.cardiacSystem = cardiac_system.CardiacSystem()
        self.cardiacSystem.agent = self


        self.lowerGastroIntestinalSystem = 
                lower_gastrointestinal_system.LowerGastroIntestinalSystem()
        self.lowerGastroIntestinalSystem._agent = self


