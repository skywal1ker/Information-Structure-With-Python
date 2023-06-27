class Table_Fan:
    def __init__(self, name, item, cost, condition):
        self.mname = name
        self.item = item
        self.cost = cost
        self.speed = 2
        self.status = True
        self.swingStatus = True
        self.condition = condition

    def getManufacturer(self):
        return self.mname

    def getModel(self):
        return self.item

    def getPrice(self):
        return self.cost

    def getCondition(self):
        return self.condition

    def switchOn(self):
        if self.status == True:
            print("Already Switched On")
            return
        self.status == True

    def switchOff(self):
        if self.speed == 0:
            self.status == False
            print("Already Switched off")
            return
        else:
            self.speed = 0
            print("Switching off the Fan")
            return
        self.status = False

    def toggleSwing(self):
        if self.status == False:
            self.status == True
        if self.swingStatus == False:
            self.swingStatus = True
            return
        if self.swingStatus == True:
            self.swingStatus = False

    def increaseSpeed(self):
        if self.status == False:
            self.status == True
        if (self.speed < 5):
            self.speed = self.speed + 1
            print("Speed increased by one and the current speed is " + str(self.speed))
        else:
            self.speed = 5
            print("current speed is " + str(self.speed) + " i.e. Maximum speed")

    def decreaseSpeed(self):
        if self.status == False:
            self.status == True
        if (self.speed > 0):
            self.speed = self.speed - 1
            print("Speed decreased by one and the current speed is " + str(self.speed))

        else:
            self.speed = 0
            print("Speed is " + str(self.speed) + " Hence switching off the Fan")


myfan = Table_Fan("USHA", "Elegence", "$30", "New")
print(myfan.getManufacturer())
print(myfan.getModel())
print(myfan.getPrice())
print(myfan.getCondition())
myfan.switchOn()
myfan.increaseSpeed()
myfan.toggleSwing()
myfan.decreaseSpeed()
myfan.increaseSpeed()
myfan.switchOff()