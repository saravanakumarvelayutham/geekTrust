import GlobalVariables
import random
import inflect
from Message import Message


class Ballot:
    Contestants = None
    Voters = None
    Messages = None
    p = inflect.engine()

    def __init__(self,contestants):
        self.Contestants = contestants
        self.Voters = [kingdom for kingdom in GlobalVariables.kingdoms if kingdom not in contestants]
        self.Messages = list()

    def VotingProcess(self):
        self.Vote()
        self.CountVotes()

    def UpdateContestants(self,contestants):
        self.Contestants = contestants
        self.ClearVotingResults()

    def ClearVotingResults(self):
        self.Messages.clear()
        for contestant in self.Contestants:
            contestant.ClearAlliesAndSupport()
        for voter in self.Voters:
            voter.ClearAlliesAndSupport()

    def PrepareMessages(self,contestant):
        for voter in self.Voters:
            randomIndex = random.randint(0,len(GlobalVariables.messagesForSelection)-1)
            selectedMessage = GlobalVariables.messagesForSelection[randomIndex]
            message = Message(contestant,voter,selectedMessage)
            self.Messages.extend([message])

    def HighPriestPickMessages(self):
        messageLen = len(self.Messages)
        selectMessages = set()
        while len(selectMessages) != 6:
            randomIndex = random.randint(0, messageLen - 1)
            selectedMessage = self.Messages[randomIndex]
            selectMessages.add(selectedMessage)
        self.Messages = list(selectMessages)

    def SendMessages(self):
        for message in self.Messages:
            message.Send()

    def Vote(self):
        for contestant in self.Contestants:
            messages = contestant.PrepareMessagesFor(self.Voters)
            self.Messages.extend(messages)
        self.HighPriestPickMessages()
        self.SendMessages()

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
            self.DecideReVote(topKingdoms)
            break
        GlobalVariables.Winner = topKingdoms[0]

    def DecideReVote(self,topKingdoms):
        while (len(topKingdoms) > 1):
            GlobalVariables.Round += 1
            self.UpdateContestants(topKingdoms)
            self.VotingProcess()
            break

    def GetBallotResult(self):
        print('Who is the ruler of Southeros?')
        print(GlobalVariables.Winner.Name)
        print('Allies of Ruler?')
        print(' '.join([ally.Name for ally in GlobalVariables.Winner.Allies]))
