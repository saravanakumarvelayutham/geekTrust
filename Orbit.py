class Orbit:
    def __init__(self, name, speed, source, destination, distance, numberofcraters):
        self.Name = name
        self.Speed = int(speed)
        self.Source = source
        self.Destination = destination
        self.Distance = int(distance)
        self.NumberOfCraters = numberofcraters

    def __str__(self):
        return 'Name: {} speed: {} source: {} destination: {} distance: {} numberofcraters: {} \n'.format(self.Name,
                                                                                                          self.Speed,
                                                                                                          self.Source,
                                                                                                          self.Destination,
                                                                                                          self.Distance,
                                                                                                          self.NumberOfCraters)
