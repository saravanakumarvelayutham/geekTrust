from collections import  Counter
import GlobalVariables


class Conquest:
    Winner = None
    Allies = None
    def Send(self,msg):
        msgCounter = Counter(msg.Message.lower())
        for kingdom in GlobalVariables.kingdoms:
            filteredCounter = dict((counterKey, kingdom.Counter[counterKey]) for counterKey, counterValue in msgCounter.items()
                                   if counterKey in kingdom.Counter and counterValue >= kingdom.Counter[counterKey])

            if filteredCounter == kingdom.Counter:
                kingdom.Support += 1

    def Conquer(self):
        allies = [kingdom.Name for kingdom in GlobalVariables.kingdoms if kingdom.Support > 0]
        if(len(allies) >= 3):
            self.Winner = 'King Shan'
            self.Allies = ', '.join(allies)

    def GetResult(self):
        print('Who is the ruler of Southeros?')
        print(self.Winner)
        print('Allies of Ruler?')
        print(self.Allies)
