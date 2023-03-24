class Transport():
    def __init__(self, speed, oil):
        self._speed = speed
        self._oil = oil

    def setSpeed(self, speed):
        self._speed = speed

    def setOil(self, oil):
        self._oil = oil

    def getSpeed(self):
        return self._speed

    def getOil(self):
        return self._oil     

    speed = property(getSpeed, setSpeed)
    oil = property(getOil, setOil)

    def out(self):
        print(self.speed, self.oil)

# class Auto(Transport):

#     def __init__(self, speed, oil, color):
#         super().__init__(speed, oil)
#         self.__color = color

#     def getColor(self):
#         return self.__color

#     def setColor(self, color):
#         self.__color = color

#     color = property(getColor, setColor)

#     def out(self):
#         print(self.speed, self.oil, self.color)

# listTr = [Transport (50 , "92"), Auto (100, "95", "red"), Transport (120, "95"), Auto(200, "92", "green")]

# def out(transport):
#     for t in transport:
#         t.out()

# out(listTr)        


class LandTr(Transport):
    def __init__(self, speed, oil, mod):
        super().__init__(speed, oil)
        self._mod = mod

    def getMod(self):
        return self._mod
    def setMod(self, mod):
        self._mod = mod    

    mod = property(getMod, setMod)
    
    def out(self):
        print(self.speed, self.oil, self.mod)

# alfa = [Transport(100, "95"),LandTr(150, "100","Lamba")]
# def out(transport):
#     for t in transport:
#         t.out()
# out(alfa)


class AirTr(Transport):
    def __init__(self, speed, oil, mark):
        super().__init__(speed, oil,)
        self._mark = mark

    def getMark(self):
        return self._mark
    def setMark(self, mark):
        self._mark = mark

    mark = property(getMark, setMark)

    def out(self):
        print(self.speed, self.oil, self.mark)

# live = [Transport(400, "100", "air")]
# def out(airtrans):
#     for t in airtrans:
#         t.out()
# out(live)

class WTr(Transport):
    def __init__(self, speed, oil, tan):
        super().__init__(speed, oil)
        self._tan = tan

    def getTan(self):
        return self._tan
    def setTan(self, tan):
        self._tan = tan

    tan = property(getTan, setTan)

    def out(self):
        print(self.speed, self.oil, self.tan)

class Auto(LandTr):
    def __init__(self, speed, oil, mod, color):
        super().__init__(speed, oil, mod)
        self._color = color

    def getColor(self):
        return self._color
    def setColor(self, color):
        self._color = color

    color = property(getColor, setColor)

    def out(self):
        print(self.speed, self.oil, self, self.mod, self.color)


class Airplane(AirTr):
    def __init__(self, speed, oil, mark, ps):
        super().__init__(speed, oil, mark)
        self._ps = ps

    def getPs(self):
        return self._ps
    def setPs(self, ps):
        self._ps = ps

    ps = property(getPs, setPs)

    def out(self):
        print(self.speed, self.oil, self.mark, self.ps)


class Ship(WTr):
    def __init__(self, speed, oil, tan, type):
        super().__init__(speed, oil, tan)
        self._type = type

    def getType(self):
        return self._type
    def setType(self, type):
        self._type = type

    type = property(getType, setType)

    def out(self):
        print(self.speed, self.oil, self.tan, self.type)


ListT = [Transport(100,"92"),LandTr(150, "100", "Lamba"), Auto(150,"100","Huracan"), AirTr(300, "100", "MARK"), WTr(100, "100", "TAN")]
