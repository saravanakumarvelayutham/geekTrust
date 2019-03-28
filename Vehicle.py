class Vehicle:
    def __init__(self, order, name, speed, weathers, timepercrater):
        self.Order = order
        self.Name = name
        self.Speed = int(speed)
        self.Weathers = weathers
        self.TimePerCrater = int(timepercrater)

    def __str__(self):
        return 'Order: {} Vehicle: {} Speed: {} weathers: {} timePerCreater: {} \n'.format(self.Order, self.Name,
                                                                                           self.Speed, self.Weathers,
                                                                                           self.TimePerCrater)
