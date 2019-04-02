from Route import Route
import GlobalFunctions

class Vehicle:
    def __init__(self, order, name, speed, weathers, timepercrater):
        self.Order = order
        self.Name = name
        self.Speed = int(speed)
        self.Weathers = weathers
        self.TimePerCrater = int(timepercrater)

    def GetBestRouteInOrbits(self,source,destination,orbits):
        routes = list()
        for orbit in orbits:
            route = GlobalFunctions.GetRouteNameByProblem(orbit,self)
            speed = orbit.Speed
            if self.Speed < orbit.Speed:
                speed = self.Speed
            time = orbit.Distance / speed
            routeObject = Route(route, source, destination, orbit.Name, self, time)
            routes.extend([routeObject])
        routes.sort(key=lambda x: x.Time)
        return routes[0]


    def __str__(self):
        return self.Name
        return 'Order: {} Vehicle: {} Speed: {} weathers: {} timePerCreater: {} \n'.format(self.Order, self.Name,
                                                                                           self.Speed, self.Weathers,
                                                                                           self.TimePerCrater)
