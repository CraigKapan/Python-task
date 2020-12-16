class Computer:
    def __init__(self, color, size, weight, performance, model, company):
        self.color = color
        self.size = size
        self.weight = weight
        self.performance = performance
        self.model = model
        self.company = company

    def shutdown(self):
        return self.company + ' is shutting down'

    def restart(self):
        return self.company + ' is restarting'

class Server(Computer):
    def __init__(self, color, size, weight, performance, model, company, clients):
        self.clients = clients

    def connect(self):
        return self.company + ' is connecting to another client'

class Laptop(Computer):
    def __init__(self, color, size, weight, performance, model, company, portable):
        self.portable = portable

class Mobile(Computer):
    def call(self):
        return self.company + ' is calling someone'
    
class Tablet(Mobile):
    def __init__(self, color, size, weight, performance, model, company, tel):
        self.tel = tel

class Phone(Mobile):
    def __init__(self, color, size, weight, performance, model, company, tel):
        self.tel = tel

    def sendsms(self, message):
        print(str(self.tel) + ' sending a message: ' + message)

    def makeacall(self, num):
        print(str(self.tel) + ' is calling: ' + str(num))


mobile = Phone("black", 20, 10, "good", "S20", "samsung", 822252885)

# print(mobile)

mobile.sendsms('hello')
mobile.makeacall(718181630)

