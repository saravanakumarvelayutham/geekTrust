from collections import  Counter
import GlobalVariables
import random
import inflect


class Ballot:
    Contestants = None
    Messages = None
    p = inflect.engine()
    def __init__(self,contestants):
        for contestant in contestants:
            contestant.ClearAlliesAndSupport()
        self.Contestants = contestants

    def ChooseRandom(self):
        self.Messages = list()
        messageLen = len(GlobalVariables.messagesForSelection)
        for index in [random.randint(0, messageLen - 1) for _ in range(6)]:
            selectedMessage = GlobalVariables.messagesForSelection[index]
            self.Messages.extend([selectedMessage])

    def Vote(self):
        for contestant in self.Contestants:
            self.ChooseRandom()
            for message in self.Messages:
                for kingdom in GlobalVariables.kingdoms:
                    if kingdom == contestant:
                        continue
                    msgCounter = Counter(message.lower())
                    filteredCounter = dict((counterKey, kingdom.Counter[counterKey]) for counterKey, counterValue in msgCounter.items()
                                           if counterKey in kingdom.Counter and counterValue >= kingdom.Counter[counterKey])
                    if filteredCounter == kingdom.Counter:
                        if kingdom not in contestant.Allies:
                            contestant.Support += 1
                            contestant.Allies.add(kingdom)


    def CountVotes(self):
        while True:
            maxSupport = max([kingdom.Support for kingdom in self.Contestants])
            topKingdoms = [kingdom for kingdom in self.Contestants if kingdom.Support == maxSupport]
            topKingdoms.sort(key=lambda x: x.Support)
            contestants = self.Contestants
            roundNumber = self.p.number_to_words(GlobalVariables.Round)
            print('Results after round {} ballot count'.format(roundNumber))
            for contestant in contestants:
                print('Allies for {} : {}'.format(contestant.Name, contestant.Support))
            while(len(topKingdoms) > 1):
                GlobalVariables.Round+=1
                ballot = Ballot(topKingdoms)
                ballot.Vote()
                ballot.CountVotes()
                break
            print('Who is the ruler of Southeros?')
            print(topKingdoms[0].Name)
            print('Allies of Ruler?')
            print(' '.join([ally.Name for ally in topKingdoms[0].Allies]))
            break
