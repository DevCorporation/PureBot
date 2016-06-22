from random import randint
from random import choice as randstr

# Command «/help»

def helps(commandsend):
 if commandsend == "/help":
  print("\n Список комманд:\n/help - Помощь по боту\n/random - Случайное число от 0 до 100\n/tf - Мини игра «True or False»\n/exit - Выйти из системы")

# Мини игра Правда или Лож

def trueorfalse(commandsend):
 if commandsend == "/tf":
  true = {0:"В Армении есть интернет?",1:"У русских «Медведь», а у амереканцев «Ястреб»?",2:"Питон - Так называют какой-то язык программирования?",
  3:"Существует ли такой сериал «ZKD»?",4:"Python - Это язык программирования, который назван в честь цирка Пайтона?"}
  false = {0:"Обама черный?",1:"ЯП - Это язык педиков? ",2:"Вафля - это еда и имя?",
  3:"ПК - Это пистолетная кончина?",4:"Создатель minecraft - Шоги?"}
  keys = {"true":true,"false":false}
  rint = randint(0,4)
  rstr1 = randstr([true,false])
  rstr2 = randstr([rstr1[rint]])
  print("\n",rstr2)
  result = input("\n«true» или «false»?\nВаш ответ: ")
  if true == keys[result]:
   if rstr2 == true[rint]:
    print("Правильный ответ и это - ПРАВДА")
   else:
    print("Неверно, ответ: ЛОЖ")
  elif false == keys[result]:
   if rstr2 == false[rint]:
    print("Правильный ответ и это - ЛОЖ")
   else:
    print("Неверно, ответ: ПРАВДА")
  else:
   print("Вы ввели другой сивмвол в ответе!") 
   
# TODO:
# Правила и информация об игре!
# Система случайного получения денег:  
# print("\nВаша награда: ",randmoney)
# Возможно экономика "БОТовая".

# Command «/random»
  
def random(commandsend):
 if commandsend == "/random":
  random = randint(0,100)
  print("\n Случайное число: ",random)
