from Route import Route
import GlobalVariables


class Routes:
    def __init__(self, source, destination, sample, weather):
        self.Source = source
        self.Destination = destination
        self.Orbits = list()
        self.Routes = list()
        self.Sample = sample
        self.Weather = weather

    def AddOrbit(self, orbit):
        self.Orbits.extend([orbit])

    def GetBestRoute(self):
        self.Routes.clear()
        orbits = list([orbit for orbit in self.Orbits if
                       ((orbit.Source == self.Source and orbit.Destination == self.Destination) or
                        (orbit.Destination == self.Source and orbit.Source == self.Destination))])
        for orbit in orbits:
            for vehicle in GlobalVariables.vehicleswithWeather:
                if self.Weather not in vehicle.Weathers:
                    continue
                if self.Sample == 1:
                    route = 'Vehicle {} on {}'.format(vehicle.Name, orbit.Name)
                else:
                    route = 'Vehicle {} to {} via {}'.format(vehicle.Name, orbit.Destination, orbit.Name)
                speed = orbit.Speed
                if vehicle.Speed < orbit.Speed:
                    speed = vehicle.Speed
                time = orbit.Distance / speed
                routeObject = Route(route, self.Source, self.Destination, orbit.Name, vehicle, time)
                self.Routes.extend([routeObject])
        self.Routes.sort(key=lambda x: x.Time)
        return self.Routes[0]

    def GetBestRouteByVehicle(self, vehicle):
        self.Routes.clear()
        orbits = list([orbit for orbit in self.Orbits if
                       ((orbit.Source == self.Source and orbit.Destination == self.Destination) or
                        (orbit.Destination == self.Source and orbit.Source == self.Destination))])
        for orbit in orbits:
            if self.Weather not in vehicle.Weathers:
                continue
            if self.Sample == 1:
                route = 'Vehicle {} on {}'.format(vehicle.Name, orbit.Name)
            else:
                route = 'Vehicle {} to {} via {}'.format(vehicle.Name, orbit.Destination, orbit.Name)
            speed = orbit.Speed
            if vehicle.Speed < orbit.Speed:
                speed = vehicle.Speed
            time = orbit.Distance / speed
            routeObject = Route(route, self.Source, self.Destination, orbit.Name, vehicle, time)
            self.Routes.extend([routeObject])
        self.Routes.sort(key=lambda x: x.Time)
        return self.Routes[0]