class ParkingSystem:
    '''
    1603. Design Parking System
    '''
    def __init__(self, big: int, medium: int, small: int):
        self.cap = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if carType < 1 or carType > 3:
            return False
        if self.cap[carType] == 0:
            return False
        self.cap[carType] -= 1
        return True



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)