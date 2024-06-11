'''
Создайте класс «Дробь». Необходимо хранить в полях
класса: числитель и знаменатель. Реализуйтеметодыкласса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса. Также создайте
методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление, и т.д.).

p.s по желанию добавьте целую часть в дробь, возможность её сокращения
'''

class Fraction():
  def __init__(self, numenator:int, denominator:int):
    self.numenator = numenator
    while denominator == 0:
      print("Делитель не может быть равен нулю")
    self.denominator = denominator

  def set_numenator(self, numenator:int) -> None:
    self.numenator = numenator
  def set_denominator(self, denominator:int) -> None:
    self.denominator = denominator

  def get_numenator(self)->int:
    return self.numenator
  def get_denominator(self)->int:
    return self.denominator

  def fraction_summ(self, fraction):
    if self.denominator == fraction.denominator:
      print(f"{self.numenator + fraction.numenator}/{self.denominator}")
    else:
      print(f"{self.numenator * fraction.denominator + fraction.numenator * self.denominator}/{self.denominator * fraction.denominator}")

  def fraction_subtraction(self, fraction):
    if self.denominator == fraction.denominator:
      print(f"{self.numenator - fraction.numenator}/{self.denominator}")
    else:
      print(f"{self.numenator * fraction.denominator - fraction.numenator * self.denominator}/{self.denominator * fraction.denominator}")

  def fraction_multiplication(self, fraction):
    print(f"{self.numenator * fraction.numenator}/{self.denominator * fraction.denominator}")

  def fraction_division(self, fraction):
    print(f"{self.numenator * fraction.denominator}/{self.denominator * fraction.numenator}")

  def fraction_simplification(self):
    for i in range (1,9):
      if self.numenator % i == 0 and self.denominator % i == 0:
        self.numenator = self.numenator // i
        self.denominator = self.denominator // i
    print(f"{self.numenator}/{self.denominator}")

  def fraction_wholenumber(self):
    wholenumber = round(self.numenator / self.denominator)
    self.numenator = self.numenator % self.denominator
    print(f"{wholenumber}, {self.numenator}/{self.denominator}")

fraction0 = Fraction(17,22)
fraction1 = Fraction(2,3)
fraction2 = Fraction(3,4)
fraction1.fraction_summ(fraction2)
fraction1.fraction_simplification()


