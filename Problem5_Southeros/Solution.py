import GlobalVariables
from Message import Message
from Conquest import Conquest
from Ballot import Ballot

class SoutherosSolution:
    def ExecuteProblem1(self,inputText):
        GlobalVariables.initalizeConstants()
        conquest = Conquest()
        for sentence in inputText.split('\n'):
            if 'Input:' not in sentence:
                continue
            splitSentence = sentence.split()
            sender = 'King Shan'
            receiver = splitSentence[1][:-1]
            text = r'{}'.format(' '.join(splitSentence[2:]))[1:-1]
            msg = Message(sender, receiver, text)
            conquest.Send(msg)
            del msg
        conquest.Conquer()
        conquest.GetResult()

    def ExecuteProblem2(self,inputText):
        GlobalVariables.initalizeConstants()
        for sentence in inputText.split('\n'):
            if 'Input:' not in sentence:
                continue
            splitSentence = sentence.split()
            contestants = splitSentence[1:]
        ballot = Ballot([kingdom for kingdom in GlobalVariables.kingdoms if kingdom.Name in contestants])
        ballot.Vote()
        ballot.CountVotes()
        ballot.GetBallotResult()


