class Coder:
  def __init__(self, a, b):
    self.__a=a
    self.__b=b
  def __resault(self):
    return self.__a+self.__b * 0.28
  def getresault(self):
    return self.__resault()
ia = int(input("Введите число а: "))
ib = int(input("Введите число b: "))
obj = Coder(ia, ib)
print("Ваш результат:", obj.getresault())