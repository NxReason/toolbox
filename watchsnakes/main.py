from watchers import show, add
from cli_menu import Menu

opt_cmd = {
        'show watchers': show,
        'add watcher': add,
        }

menu = Menu(opt_cmd)

while menu.is_open:
    menu.draw()
