import agents.organ_systems.organ_abstract_classes as oac 
from simulate import ureg


class LargeIntestine(oac.Organ):


    _name = None
    _organSystem = 'Lower Gastro Intestinal System'
    _agent = 'agent'
    _lesionList = []
    _proximalOrgan = []
    _distalOrgan = []

    def __init__(self, name):
        self._name = name
        #self.setBelongsRelations(_organSystem, _agent,
        #                        _proximalOrgan, _distalOrgan)
        #self.setBiologicalData(_lesionList)

    def setBelongsRelations(self, organSystem, agent,
                            proximalOrgan, distalOrgan):
        self._organSystem = organSystem
        self._agent = agent
        self._proximalOrgan = proximalOrgan
        self._distalOrgan = distalOrgan
        
    def setBiologicalData(self, lesionList):
        self.lesionList = lesionList





class LowerGastroIntestinalSystem(oac.OrganSystem):

    _name = None
    _agent = 'agent'

    def __init__(self, name):
        self._name = name 
        #self.setBelongsRelations(self, name, _agent) 
        self.setBiologicalData()

    def setBelongsRelations(self, name, agent):
        self._name = name
        self._agent = agent
        
    def setBiologicalData(self):
        self.ascendingColon = LargeIntestine('Ascending Colon')
        self.appendix = LargeIntestine('Appendix')
        self.transverseColon = LargeIntestine('Transverse Colon')
        self.descendingColon = LargeIntestine('Descending Colon')
        self.sigmoidColon = LargeIntestine('Sigmoid Colon')
        self.rectum = LargeIntestine('Rectum')

        self.ascendingColon.setBelongsRelations(self, self._agent,
                            [], [self.appendix, self.transverseColon])
        self.appendix.setBelongsRelations(self, sel_agent,
                            [self.ascendingColon], [])
        self.transverseColon.setBelongsRelations(self, self._agent,
                            [self.ascendingColon], [self.descendingColon])
        self.descendingColon.setBelongsRelations(self, self._agent,
                            [self.transverseColon], [self.sigmoidColon])
        self.sigmoidColon.setBelongsRelations(self, self._agent,
                            [self.descendingColon], [self.rectum])
        self.rectum.setBelongsRelations(self, self._agent,
                            [self.sigmoidColon], [])
        








