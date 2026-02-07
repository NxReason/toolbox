from typing import Any
import sys
import os

class Menu:
    def __init__(self, options: dict[str, Any]):
        self.options = options
        self.selection = 0
        self.is_open = True

    def draw(self) -> None:
        options_str = list(map(lambda o: f'   {o}', self.options.keys()))
        if self.selection is not None:
            selected = options_str[self.selection]
            options_str[self.selection] = selected[:2] + '>' + selected[3:]
        print('\n'.join(options_str), flush=True)
        try:
            key = input(f'Enter a choice (1-{len(self.options)}): ')
            self._process_key(key)
        except (KeyboardInterrupt, EOFError):
            print()
            self.is_open = False

    def _clear(self, n: int | None = None) -> None:
        n_lines_clear = len(self.options) if not n else n

        if os.name == 'nt': # windows
            print('\b' * 100, end='', flush=True)
        else:
            sys.stdout.write(f'\033[{n_lines_clear}A') # move up n lines
            sys.stdout.write(f'\033[2K') # clear entire line
            sys.stdout.flush()

    def _process_key(self, key: str):
        if key == 'q': self.is_open = False
        try:
            option = int(key)
            if option < 1 or option > len(self.options): raise ValueError('invalid option')
            self.selection = option - 1
            self._process_option()
        except Exception as exc:
            print(exc)

    def _process_option(self):
        keys = list(self.options.keys())
        selected_key = keys[self.selection]
        self.options[selected_key]()

    @classmethod
    def close(_cls, instance: Menu):
        instance.is_open = False
