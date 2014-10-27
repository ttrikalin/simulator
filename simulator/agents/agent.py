
from simulate import ureg
from organ_systems import cardiac_system

class Agent(object):

    def __init__(self, name='agent', sex='male', age = 0 * ureg('year')):
        self.name = name 
        self.sex = sex
        self.age = age

        # define systems 
        self.cardiacSystem = cardiac_system.CardiacSystem()
        self.cardiacSystem.agent = self 
