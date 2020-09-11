# Line Management class
class Line():
    def __init__(sel,CustomerCode,RouteCode,LineFone):
        self.__CustomerCode=CustomerCode
        self.__RouteCode=RouteCode
        self.__LineFone=LineFone
#proprty
    @property
    def LineCode(self):
            return self.__LineCode

    @LineCode.setter
    def LineCode(self, value):
           self.__LineCode=value

    @property
    def CustomerCode(self):
        return self.__CustomerCode

    @CustomerCode.setter
    def CustomerCode(self, value):
           self.__CustomerCode=value

    @property
    def RouteCode(self):
        return self.__RouteCode

    @RouteCode.setter
    def RouteCode(self, value):
        self.__RouteCode = value

    @property
    def LineFone(self):
        return self.__LineFone

    @LineFone.setter
    def LineFone(self, value):
        self.__LineFone = value

#class function
    def __str__(self):
        return "CustomerCode: " + str(self.CustomerCode) + " RouteCode: " + str(
            self.RouteCode) + " Phone: " + self.LineFone

