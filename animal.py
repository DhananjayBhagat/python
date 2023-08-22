

class Animals:
    def _init_(self):
        self.legs=4
        self.domestic= True
        self.tail= True
        self.mammals= True
        
    def ismammals(self):
        if self.mammals:
            print("It is Mammals")
            
    def isdomestic(self):
        if self.domestic:
            print("Is is Domestic")
            
class Dogs(Animals):
    def _init_(self):
        super()._init_()
        
    def ismamm(self):
        super().ismammals()
        
        
class Horses(Animals):
    def _init_(self):
        super()._init_()
        
    def hasTailandLegs(self):
        if self.tail and self.legs==4:
            print("Has legs and Tails")
            
Tom=Dogs()
Tom.ismamm()
Tom.isdomestic()

Bruno=Horses()
Bruno.hasTailandLegs()
