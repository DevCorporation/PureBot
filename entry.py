import time
from commands import helps
from commands import random
from commands import trueorfalse
# Глобальные переменные
global not_found
global prefix

not_found = "Команда не найдена, введите «/help» для просмотра доступных комманд."
prefix = "\n[PureBot]"
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
