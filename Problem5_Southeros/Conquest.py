class Conquest:
    def __init__(self,conqueror):
        self.Winner = None
        self.Allies = None
        self.Conqueror = conqueror

    def SendMessage(self,msg):
        msg.Send()

    def GetResult(self):
        if self.Conqueror.Support >= 3 :
            self.Winner = self.Conqueror
            self.Allies = ', '.join([kingdom.Name for kingdom in self.Conqueror.Allies])
        print('Who is the ruler of Southeros?')
        print(self.Winner)
        print('Allies of Ruler?')
        print(self.Allies)
