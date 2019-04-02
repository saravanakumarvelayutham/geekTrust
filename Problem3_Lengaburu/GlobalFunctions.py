import GlobalVariables

def GetRouteNameByProblem(orbit, vehicle):
    if GlobalVariables.ProblemNumber == 1:
        return 'Vehicle {} on {}'.format(vehicle.Name, orbit.Name)
    else:
        return 'Vehicle {} to {} via {}'.format(vehicle.Name, orbit.Destination, orbit.Name)