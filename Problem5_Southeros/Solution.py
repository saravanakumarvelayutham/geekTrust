import GlobalVariables
from Message import Message
from Conquest import Conquest
from Ballot import Ballot
from Kingdom import Kingdom


class SoutherosSolution:
    def ExecuteProblem1(self,inputText):
        GlobalVariables.initalizeConstants()
        sender = 'King Shan'
        senderKingdom = Kingdom(sender,'',0)
        conquest = Conquest(senderKingdom)
        for sentence in inputText.split('\n'):
            splitSentence = sentence.split()
            receiver = splitSentence[1][:-1]
            text = r'{}'.format(' '.join(splitSentence[2:]))[1:-1]
            receiverKingdom = next((kingdom for kingdom in GlobalVariables.kingdoms if kingdom.Name == receiver),None)
            msg = Message(senderKingdom, receiverKingdom, text)
            conquest.SendMessage(msg)
            del msg
        conquest.GetResult()

    def ExecuteProblem2(self,inputText):
        GlobalVariables.initalizeConstants()
        for sentence in inputText.split('\n'):
            if 'Input:' not in sentence:
                continue
            splitSentence = sentence.split()
            contestants = splitSentence[1:]
        ballot = Ballot([kingdom for kingdom in GlobalVariables.kingdoms if kingdom.Name in contestants])
        ballot.VotingProcess()
        ballot.GetBallotResult()


