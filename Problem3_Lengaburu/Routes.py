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

    def GetBestRouteForSample2(self):
        routeCombinations = list()

        for vehicle in GlobalVariables.vehicleswithWeather:
            self.Source = GlobalVariables.Source
            self.Destination = GlobalVariables.Destination

            if self.Weather not in vehicle.Weathers:
                continue

            route_source_to_destination = self.GetBestRouteByVehicle(vehicle)

            self.Destination = GlobalVariables.Intermediate
            route_source_to_intermediate = self.GetBestRouteByVehicle(vehicle)

            self.Source = GlobalVariables.Intermediate
            self.Destination = GlobalVariables.Destination
            route_intermediate_to_destination = self.GetBestRouteByVehicle(vehicle)

            self.Source = GlobalVariables.Destination
            self.Destination = GlobalVariables.Intermediate
            route_destination_to_intermediate = self.GetBestRouteByVehicle(vehicle)

            source_intermediate_destination = [route_source_to_intermediate, route_intermediate_to_destination]
            source_destination_intermediate = [route_source_to_destination, route_destination_to_intermediate]

            source_intermediate_destination_totalDistance = sum(
                [route.Time for route in source_intermediate_destination])
            source_destination_intermediate_totalDistance = sum(
                [route.Time for route in source_destination_intermediate])

            if source_intermediate_destination_totalDistance > source_destination_intermediate_totalDistance:
                smallestRoutes = source_destination_intermediate
                time = source_destination_intermediate_totalDistance
            else:
                smallestRoutes = source_intermediate_destination
                time = source_intermediate_destination_totalDistance
            routeName = None
            previousDestination = None
            for route in smallestRoutes:
                currentDestination = route.Destination
                if routeName is None:
                    routeName = route.Name
                    previousDestination = route.Destination
                else:
                    if previousDestination == currentDestination :
                        currentDestination = route.Source
                    routeName = routeName + ' and ' + currentDestination + ' via ' + route.Orbit
            routeObj = Route(routeName, self.Source, self.Destination, '', vehicle, route.Time)
            routeCombinations.extend([routeObj])

        routeCombinations.sort(key=lambda x: (x.Time,x.Vehicle.Order))
        return routeCombinations[0]