class Message:
    def __init__(self,sender,receiver,message):
        self.Sender = sender
        self.Receiver = receiver
        self.Message = message
    def __str__(self):
        return '{} -> {} : {}'.format(self.Sender,self.Receiver,self.Message)