from collections import Counter


class Kingdom:
    def __init__(self,name,emblem,support):
        self.Name = name
        self.Emblem = emblem
        self.Support = support
        self.Counter = Counter(emblem.lower())
    def __str__(self):
        return '{} with {} of support {}'.format(self.Name,self.Emblem,self.Support)
