# Talking Management class
import datetime
class Talking():
    count=0
    def __init__(self,StartDate,EndDate,OneFhone,SecondFhone):
        Talking.count+=1
        self.__StartDate=StartDate
        self.__EndDate=EndDate
        self.__OneFhone=OneFhone
        self.__SecondFhone=SecondFhone

#property
    @property
    def TalkCode(self):
        return self.__TalkCode

    @TalkCode.setter
    def TalkCode(self, value):
           self.__TalkCode=value

    @property
    def StartDate(self):
        return self.__StartDate

    @StartDate.setter
    def StartDate(self, value):
           self.__StartDate=value

    @property
    def EndDate(self):
        return self.__EndDate

    @EndDate.setter
    def EndDate(self, value):
        self.__EndDate = value

    @property
    def OneFhone(self):
        return self.__OneFhone

    @OneFhone.setter
    def OneFhone(self, value):
        if(len(value)<=10):
            self.__OneFhone = value
    @property
    def SecondFhone(self):
        return self.__SecondFhone

    @SecondFhone.setter
    def SecondFhone(self, value):
        if(len(value)<=10):
            self.__SecondFhone = value

#class functions
    def __str__(self):
        return "StartDate : "+ str(self.StartDate)+ "  EndDate: "+  str(self.EndDate)+" FromPhone: "+str(self.OneFhone)+"  ToPhone: "+str(self.SecondFhone)
    def __eq__(self, other):
        if isinstance(self,Talking):
            if self.EndDate-self.StartDate==other.EndDate - other.StartDate:
                return True
            return False
        return True
    def __ne__(self, other):
        if isinstance(self,Talking):
            if self.EndDate-self.StartDate==other.EndDate - other.StartDate:
                return True
            return False
        return True
