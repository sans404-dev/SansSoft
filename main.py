import os
from sys import exit
from loguru import logger
from os import system
from rich.console import Console

try:
    from modules import test
except ImportError as ImportErr:
    logger.error(
        f"\n[X] Некоторые модули не были были загружены корректно!\nОШИБКА: {ImportErr}"
    )
    exit(1)

version = "альфа 0.2"
plugins_list = [file for file in os.listdir("modules") if file.endswith(".py")]

if len(plugins_list) == 1:
    index = 1
else:
    index = len(plugins_list) + 1
console = Console()


def menu():
    try:
        global menu
        menu = int(console.input("\n[bold yellow][?] Введите пункт из меню >>> "))
    except ValueError:
        menu()


console.print(
    f"""[bold blue] __             __      _    
(_   _   _   _ (_   _  (_ |_ 
__) (_| | ) _) __) (_) |  |_[/]\n\n[bold white]Версия:[/] [bold magenta]{version}[/]
\n[bold white]Кол-во модулей:[/] {len(plugins_list)}
\n[{index}][bold green] - {test.name}"""
)
menu()
if menu == 1:
    try:
        test.main()
    except Exception as moduleEXC:
        logger.critical(moduleEXC)
