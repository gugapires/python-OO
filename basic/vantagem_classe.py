# Vantagens de usar classes e instancias.
# Convencinou-se chamar de self, porém pode chama-la do que quiser.

class empregado:
    pass

    # É um método de inicialização, pode encara-la como um construtor
    # depois do self, podemos especificar os demais argumentos que queremos
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self):
        return '{} {}'.format(emp_1.first, emp_1.last)



# Passamos os paramentos para as duas instancias a baixo
emp_1= empregado('bunda','mole', 50)
emp_2= empregado('jon','nit', 70)

emp_1.fullname()
#
empregado.fullname(emp_1)
# quando passamos a classe, ela não sabe o que exatamente ira rodar
# logo, para rodar um metodo temos que passar uma instancia
