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
    def __init__(self, color, size, weight, performance, model, company, tel)
    self.tel = tel

class Phone(Mobile):
    def __init__(self, color, size, weight, performance, model, company, tel, sms):
        self.tel = tel
        self.sms = sms

    def sms(self):
        return self.company + ' is smsing somebody'
