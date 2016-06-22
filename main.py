# coding: utf-8
# Импортирование модулей
from entry import entry
import sl4a  
# Вывод на экран!
droid = sl4a.Android().makeToast
echo = droid
words = ["Привет, добро пожаловать в «PureBot»", "Если найдете баги, то пишите нам", "Приятной игры"]
for word in words:
 echo(word + "!")
# Глобальные переменные
#global version
#version = "Версия: 0.5 - Бета"
#print("Запуск программы...\nПрограмма «PureBot» предназначена для лиц старше 14+  :D")
#print("Разработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99\n\n",version)
#print("-"*50,"\n")
entry()
