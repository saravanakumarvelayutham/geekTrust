import GlobalVariables
from Message import Message
from Conquest import Conquest

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
