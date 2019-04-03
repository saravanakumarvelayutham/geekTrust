from collections import Counter
from Message import Message
import random
import GlobalVariables


class Kingdom:
    def __init__(self,name,emblem,support):
        self.Name = name
        self.Emblem = emblem
        self.Support = support
        self.Counter = Counter(emblem.lower())
        self.SupportGiven = False
        self.Allies = set()

    def ClearAlliesAndSupport(self):
        self.Allies = set()
        self.Support = 0
        self.SupportGiven = False

    def PrepareMessagesFor(self,otherKingdoms):
        for kingdom in otherKingdoms:
            randomIndex = random.randint(0, len(GlobalVariables.messagesForSelection) - 1)
            selectedMessage = GlobalVariables.messagesForSelection[randomIndex]
            message = Message(self, kingdom, selectedMessage)
            yield message

    def __str__(self):
        return '{} with {} of support {}'.format(self.Name,self.Emblem,self.Support)
