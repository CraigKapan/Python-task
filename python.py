# pay = 10
# hours = 40

# class Student:

#     def __init__(self, name, surname, tel, mark):
#         self.name = name
#         self.surname = surname
#         self.tel = tel
#         self.mark = mark

#     def fullmarks(self):
#         return self.mark * 5

#     def fullname(self):
#         return '{} {}'.format(self.name, self.surname)

#     def prize(self):
#         if self.mark <= 3:
#             return 'small trophy'

#         else:
#             return 'big trophy'


# stu_1 = Student('John', 'Doe', 4852942743, 3)
# stu_2 = Student('Patric', 'Rover', 2743294485, 4)


# class Teacher:

#     def __init__(self, name, surname, tel, pay_per_week, hours_per_week, students):
#        self.name = name
#        self.surname = surname
#        self.tel = tel
#        self.pay_per_week = pay_per_week
#        self.hours_per_week = hours_per_week
#        self.students = students

#     def fullname(self):
#         return '{} {}'.format(self.name, self.surname)

#     def calulate_salary_over_time(self):

#         if self.hours_per_week > hours:
#             (hours_per_week - hours) * pay


# teac_1 = Teacher('Molly', 'Polly', 2987423843, 400, 45, 40)
# teac_2 = Teacher('Sally', 'Pally', 3483247892, 400, 42, 35)


# print('<=========-Sudents-=========>')
# print('')

# print('name: ' + stu_1.name)
# print('surname: ' + stu_1.surname)
# print('fullname: ' + stu_1.fullname())
# print('teacher: ' + teac_1.fullname())
# print('tel: ' + str(stu_1.tel))
# print('mark: ' + str(stu_1.mark))
# print('fullmarks: ' + str(stu_1.fullmarks()))
# print('prize: ' + stu_1.prize())

# print('')

# print('name: ' + stu_2.name)
# print('surname: ' + stu_2.surname)
# print('fullname: ' + stu_2.fullname())
# print('teacher: ' + teac_2.fullname())
# print('tel: ' + str(stu_2.tel))
# print('mark: ' + str(stu_2.mark))
# print('fullmarks: ' + str(stu_2.fullmarks()))
# print('prize: ' + stu_2.prize())

# print('')
# print('')

# print('<=========-Teachers-=========>')
# print('')

# print('name: ' + teac_1.name)
# print('surname: ' + teac_1.surname)
# print('fullname: ' + teac_1.fullname())
# print('students: ' + str(teac_1.students))
# print('tel: ' + str(teac_1.tel))
# print('pay per week: ' + str(teac_1.pay_per_week))
# print('avarage hours per week: ' + str(hours))
# print('hours per week: ' + str(teac_1.hours_per_week))
# print('hours over time: ' + str(teac_1.hours_per_week - hours))
# print('pay over time: ' + str((teac_1.hours_per_week - hours) * pay))
# print('total payment: ' + str((teac_1.hours_per_week - hours) * pay + teac_1.pay_per_week))

# print('')

# print('name: ' + teac_2.name)
# print('surname: ' + teac_2.surname)
# print('fullname: ' + teac_2.fullname())
# print('students: ' + str(teac_2.students))
# print('tel: ' + str(teac_2.tel))
# print('pay per week: ' + str(teac_2.pay_per_week))
# print('avarage hours per week: ' + str(hours))
# print('hours per week: ' + str(teac_2.hours_per_week))
# print('hours over time: ' + str(teac_2.hours_per_week - hours))
# print('pay over time: ' + str((teac_2.hours_per_week - hours) * pay))
# print('total payment: ' + str((teac_2.hours_per_week - hours) * pay + teac_2.pay_per_week))

# computer = {
#     "color": "black",
#     "price": "R1000",
#     "model": "windows 8",
#     "company": "lenovo",
#     "speed": "exellent"
# }

# def displayproperties():  
#     return computer

# def shutdown():
#     print('yes I am shutting down')

# def reboot():
#     print('yes I am rebotting')


# print(displayproperties())


class computer:

    def __init__(self, color, price, model, company, speed):
        self.color = color
        self.price = price
        self.model = model
        self.company = company
        self.speed = speed

    def displayproperties(self):
        return self.color, self.price, self.model, self.company, self.speed

    def shutdown(self):
        return self.company + ' is shutting down'

    def reboot(self):
        return self.company + ' is rebooting'

com_1 = computer('Blue', 2000, 'Window 10', 'Samsung', 'exellent')

print(com_1.displayproperties())
print(com_1.shutdown())
print(com_1.reboot())