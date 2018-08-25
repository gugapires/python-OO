# Aqui vamos falar um pouco de classes e instancias

class empregado:
    pass


emp_1= empregado()
emp_2= empregado()

print(emp_1)
print(emp_2)


emp_1.first = "bunda"
emp_1.last = "mole"
emp_1.email = "bunda.mole@gmail.com"
emp_1.pay = 50


emp_2.first = "jon"
emp_2.last = "nit"
emp_2.email = "jon.nit@gmail.com"
emp_2.pay = 70

print(emp_1.email)
print(emp_2.email)
