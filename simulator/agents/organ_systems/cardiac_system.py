#import abc
from simulate import ureg

class OrganSystem(object):
    def __init__(self):
        self.name = 'organ system name'
        self.agent = 'agent'
#        self.setBiologicalData()
#
#    @classmethod 
#    def setBiologicalData(cls):
#        pass


class Organ(object): 
    def __init__(self):
        self.name = 'organ name'
        self.organSystem = 'organ system'
        self.agent = 'agent' 
#        self.setBiologicalData()
#
#    @classmethod 
#    def setBiologicalData(cls):
#        pass


class SubOrgan(object):
    def __init__(self):
        self.name = 'suborgan name'
        # this allows a handle to set the status 
        # of the organ if an event originates
        # in the suborgan
        self.parentOrgan = 'parent organ'
#        self.setBiologicalData()
#
#    @classmethod 
#    def setBiologicalData(cls):
#        pass


    

class HeartChamber(SubOrgan):
    def __init__(self, name):
        super(HeartChamber, self).__init__()
        self.name = name
        self.endDiastolicVolume = 0 *ureg.mL
        self.endSystolicVolume = 0 *ureg.mL
    

class Valve(SubOrgan):
    def __init__(self, name):
        super(Valve, self).__init__()
        self.name = name
        self.hasProlapse = False
        

class Septum(SubOrgan):
    def __init__(self, name):
        super(Septum, self).__init__()
        self.name = name
        self.hasDefect = False
        

class AtrioVentricularNode(SubOrgan): 
    def __init__(self, name):
        super(AtrioVentricularNode, self).__init__()
        self.name = name
        self.rate = 70 / ureg('min')
        self.hasArrythmia = False 



class Heart(Organ):

    def initializeLeftAtriumParameters(self):
        self.leftAtrium.endSystolicVolume = 20 * ureg.mL 
        self.leftAtrium.endDiastolicVolume = 45 * ureg.mL
        self.leftAtrium.parentOrgan = self

    def initializeRightAtriumParameters(self):
        self.rightAtrium.endSystolicVolume = 10 * ureg.mL 
        self.rightAtrium.endDiastolicVolume = 35 * ureg.mL
        self.rightAtrium.parentOrgan = self 

    def initializeLeftVentricleParameters(self):
        self.leftVentricle.endSystolicVolume = 80 * ureg.mL 
        self.leftVentricle.endDiastolicVolume = 120 * ureg.mL 
        self.leftVentricle.parentOrgan = self

    def initializeRightVentricleParameters(self):
        self.rightVentricle.endSystolicVolume = 50 * ureg.mL 
        self.rightVentricle.endDiastolicVolume = 80 * ureg.mL 
        self.rightVentricle.parentOrgan = self

    def __init__(self):
        super(Heart, self).__init__()

        self.name = 'Heart'
        self.organSystem = 'Cardiac System' # will be overwritten with the system object

        #define suborgans - chambers 
        self.leftAtrium = HeartChamber('Left Atrium')
        self.rightAtrium = HeartChamber('Right Atrium')
        self.leftVentricle = HeartChamber('Left Ventricle')
        self.rightVentricle = HeartChamber('Right Ventricle')

        self.initializeLeftAtriumParameters()
        self.initializeRightAtriumParameters()
        self.initializeLeftVentricleParameters()
        self.initializeRightVentricleParameters()

        #define suborgans - atrioventricular valves 
        self.biscupidValve = Valve('Biscupid Valve')
        self.triscupidValve = Valve('Triscupid Valve')

        #define suborgans - atrial septum 
        self.atrialSeptum = Septum('Atrial Septum')

        #define suborgans -- electrical impulse control 
        self.atrioVentricularNode = AtrioVentricularNode('Atrioventricular Node')




class Vessel(Organ):
    def __init__(self, name):
        super(Vessel, self).__init__()

        self.name = name
        self.organSystem = 'Cardiac System' # will be overwritten with the system object

        # define suborgans -- valves 
        self.valveList = []
        
        # define lesions 
        self.lesionList = []

        # define biological measurements 
        self.luminalDiameter = 3 * ureg('mm')

        # define children vessels of interest; 
        # instead model the whole tree and select a branch here 
        self.childrenVessels = []


class CardiacSystem(OrganSystem):

    def __init__(self): 
        super(CardiacSystem, self).__init__()

        # define heart and its suborgans:
        #    atrial septum
        #    biscupid (mitral, left AV) valve
        #    triscupid (right AV) valve 
        #    atrioventricular node
        self.heart = Heart()
        self.heart.organSystem = self 

        # define aorta and its suborgans 
        #    aortic valve
        #    left coronary artery 
        #    right coronary artery 
        aorticValve = Valve('Aortic Valve')
        rightCoronaryArtery = Vessel('Right Coronary Artery')
        rightCoronaryArtery.luminalDiameter = 2 * ureg('mm')

        leftCoronaryArtery = Vessel('Left Coronary Artery')
        leftCoronaryArtery.luminalDiameter = 3.5 * ureg('mm')

         
        self.aorta = Vessel('Aorta')
        self.aorta.organSystem = self
        self.aorta.luminalDiameter = 20 * ureg('mm')
        self.aorta.valveList = [aorticValve]
        self.aorta.childrenVessels = [leftCoronaryArtery, rightCoronaryArtery]





