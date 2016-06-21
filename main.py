# coding: utf-8
# Импортирование модулей

from random import randint
from random import choice as randstr
import sl4a
import time
   
# Вывод на экран!

droid = sl4a.Android().makeToast
echo = droid
words = ["Привет, добро пожаловать в «PureBot»", "Если найдете баги, то пишите нам", "Приятной игры"]
for word in words:
 echo(word + "!")
 
# Глобальные переменные

global inp
global not_found
global prefix
global version

not_found = "Команда не найдена, введите «/help» для просмотра доступных комманд."
prefix = "\n[PureBot]"
version = "Версия: 0.5 - Бета"

# Начало программы

print("Запуск программы...\nПрограмма «PureBot» предназначена для лиц старше 14+  :D")
print("Разработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99\n\n",version)
print("-"*50,"\n")

# Command «/help»

def helps(commandsend):
 if commandsend == "/help":
  print("\n Список комманд:\n/help - Помощь по боту\n/random - Случайное число от 0 до 100\n/tf - Мини игра «True or False»\n/exit - Выйти из системы")

# Command «/random»
  
def random(commandsend):
 if commandsend == "/random":
  random = randint(0,100)
  print("\n Случайное число: ",random)

# Мини игра True or False

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

# Команда «/exit»

def exit(commandsend):
 while commandsend == "/exit":
  print("Хотите выйти из программы?\nДа или Нет?\n",)
  exit = input("Потвердите выход: ")
  exits = {"Да":"Да","да":"да","Нет":"Нет","нет":"нет"}
  if exit == exits[exit]:
   print("\nВыход из программы потвержден.")
   print("\n\nВыключение программы...."*2)
   break
  
# Функция ввода и вывода

def entry():
 commands = {"/help":helps,"/random":random,"/tf":trueorfalse}
 exits = {"Да":"Да","да":"да","Нет":"Нет","нет":"нет"}
 while True:
  print(prefix," Ожидайте появления ввода...")
  time.sleep(4)
  command = str(input("\nВведите комманду: "))  
  if command in commands:
   commands[command](command)
  elif command == "/exit":
   print("Хотите выйти из программы?\nДа или Нет?\n",)
   try:
    exit = input("Потвердите выход: ")
    exits = {"Да":"Да","да":"да","Нет":"Нет","нет":"нет"}
    if exit == exits[exit]:
     print("\nВыход из программы потвержден.")
     print("\n\nВыключение программы..")
     time.sleep(2)
     print("\n3..")
     time.sleep(2)
     print("\n2..")
     time.sleep(2)
     print("\n1..")
     time.sleep(1)
     print("\nСпасибо за внимание!!!")
     break
   except KeyError:
    print("Ошибка, ключ с данным именем не найден!\n"*3)
  else:
   print(not_found)
  continue
entry()

# Конец программы

print("\n\n©DevCorp")
