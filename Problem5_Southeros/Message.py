from collections import  Counter

class Message:
    def __init__(self,sender,receiver,message):
        self.Sender = sender
        self.Receiver = receiver
        self.Message = message

    def Send(self):
        if not self.Receiver.SupportGiven:
            msgCounter = Counter(self.Message.lower())
            filteredCounter = dict((counterKey, self.Receiver.Counter[counterKey]) for counterKey, counterValue in msgCounter.items()
                                   if counterKey in self.Receiver.Counter and counterValue >= self.Receiver.Counter[counterKey])
            if filteredCounter == self.Receiver.Counter:
                self.Sender.Support += 1
                self.Receiver.SupportGiven = True
                self.Sender.Allies.add(self.Receiver)

    def __str__(self):
        return '{} -> {} : {}'.format(self.Sender,self.Receiver,self.Message)