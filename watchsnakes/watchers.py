_watchers = []

def show():
    print('Watchers list')
    watchers_lines = [f'  👁  {w}' for w in _watchers]
    print('\n'.join(watchers_lines))
    print()

def add():
    path = input('Enter new path to watch: ')
    _watchers.append(path)
