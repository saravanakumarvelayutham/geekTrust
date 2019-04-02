from Route import Route
import GlobalVariables
import GlobalFunctions


class Routes:
    def __init__(self, source,intermediate, destination, weather):
        self.Source = source
        self.Destination = destination
        self.Intermediate = intermediate
        self.Orbits = list()
        self.Routes = list()
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
                route = GlobalFunctions.GetRouteNameByProblem(orbit,vehicle)
                speed = orbit.Speed
                if vehicle.Speed < orbit.Speed:
                    speed = vehicle.Speed
                time = orbit.Distance / speed
                routeObject = Route(route, self.Source, self.Destination, orbit.Name, vehicle, time)
                self.Routes.extend([routeObject])
        self.Routes.sort(key=lambda x: x.Time)
        return self.Routes[0]

    def GetPossibleorbits(self,source,destination):
        return list([orbit for orbit in self.Orbits if
              ((orbit.Source == source and orbit.Destination == destination) or
               (orbit.Destination == source and orbit.Source == destination))])

    def GetBestRouteForProblem2(self):
        routeCombinations = list()

        for vehicle in GlobalVariables.vehicleswithWeather:
            if self.Weather not in vehicle.Weathers:
                continue

            orbits = self.GetPossibleorbits(self.Source,self.Destination)
            route_source_to_destination = vehicle.GetBestRouteInOrbits(self.Source,self.Destination,orbits)

            orbits = self.GetPossibleorbits(self.Source,self.Intermediate)
            route_source_to_intermediate = vehicle.GetBestRouteInOrbits(self.Source,self.Intermediate,orbits)

            orbits = self.GetPossibleorbits(self.Intermediate,GlobalVariables.Destination)
            route_intermediate_to_destination = vehicle.GetBestRouteInOrbits(self.Intermediate,self.Destination,orbits)

            orbits = self.GetPossibleorbits(self.Destination,self.Intermediate)
            route_destination_to_intermediate =vehicle.GetBestRouteInOrbits(self.Destination,self.Intermediate,orbits)

            smallestRoutes = self.GetBestRouteFrom([route_source_to_intermediate, route_intermediate_to_destination],[route_source_to_destination, route_destination_to_intermediate])
            routeObj = self.CreateRouteObject(smallestRoutes,vehicle)
            routeCombinations.extend([routeObj])
        routeCombinations.sort(key=lambda x: (x.Time, x.Vehicle.Order))
        return routeCombinations[0]

    def GetBestRouteFrom(self,FirstRoute, SecondRoute):
        firstRouteTotalTime = sum(
            [route.Time for route in FirstRoute])
        secondRouteTotalTime = sum(
            [route.Time for route in SecondRoute])

        if firstRouteTotalTime > secondRouteTotalTime:
            smallestRoutes = SecondRoute
        else:
            smallestRoutes = FirstRoute
        return smallestRoutes

    def CreateRouteObject(self,smallestRoutes,vehicle):
        routeName = None
        previousDestination = None
        for route in smallestRoutes:
            currentDestination = route.Destination
            if routeName is None:
                routeName = route.Name
                previousDestination = route.Destination
            else:
                if previousDestination == currentDestination:
                    currentDestination = route.Source
                routeName = routeName + ' and ' + currentDestination + ' via ' + route.Orbit
        return Route(routeName, self.Source, self.Destination, '', vehicle, route.Time)