# Rote Management class
class Croute():
    #constructor
    def __init__(self, RouteName ,RouteCost,MinitRouteHere,MinitRouteBroad):
        self.__RouteName=RouteName
        self.__RouteCost=RouteCost
        self.__MinitRouteHere=MinitRouteHere
        self.__MinitRouteBroad=MinitRouteBroad

#property
    @property
    def RouteName(self):
        return self.__RouteName

    @RouteName.setter
    def RouteName(self, value):
            self.RouteName = value
    @property
    def RouteCost(self):
        return self.__RouteCost

    @RouteCost.setter
    def RouteCost(self, value):
            self.__RouteCost = value

    @property
    def MinitRouteHere(self):
        return self.__MinitRouteHere

    @MinitRouteHere.setter
    def MinitRouteHere(self, value):
            self.__MinitRouteHere = value

    @property
    def MinitRouteBroad(self):
        return self.__MinitRouteBroad

    @MinitRouteBroad.setter
    def MinitRouteBroad(self, value):
            self.__MinitRouteBroad= value

#class functions

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __ne__(self, o: object) -> bool:
        return super().__ne__(o)

    def __str__(self):
        return "name: " +self.RouteName + " cost: " + str(self.RouteCost) + " minit here: " + str(self.MinitRouteHere) + " minit broad: " + str(self.MinitRouteBroad)







