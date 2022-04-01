import os
from os import system
from rich.console import Console
from plugins import test

version = "альфа 0.1"
plugins_list = [file for file in os.listdir("plugins") if file.endswith(".py")]

if len(plugins_list) == 1:
	index = 1
else:
	index = len(plugins_list)+1
console = Console()


def menu():
	try:
		global menu
		menu = int(console.input("\n[bold yellow][?] Введите пункт из меню >>> "))
	except ValueError:
		menu()
try:
	console.print(f"""[bold blue] __             __      _    
(_   _   _   _ (_   _  (_ |_ 
__) (_| | ) _) __) (_) |  |_[/]\n\n[bold white]Версия:[/] [bold magenta]{version}[/]
\n[bold white]Кол-во плагинов:[/] {len(plugins_list)}
\n[{index}][bold green] - {test.name}""")
except NameError as NameErr:
	console.print(f"[bold red][X] Некоторые плагины не были были загружены корректно!\n\nОШИБКА: {NameErr}")
else:
	menu()
	if menu == 1:
		test.main()