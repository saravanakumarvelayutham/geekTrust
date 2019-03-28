class Route:
    def __init__(self, name, source, destination, orbit, vehicle, time):
        self.Name = name
        self.Vehicle = vehicle
        self.Time = time
        self.Source = source
        self.Destination = destination
        self.Orbit = orbit

    def __str__(self):
        return self.Name
