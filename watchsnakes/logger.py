import uuid
from datetime import datetime
from pathlib import Path
from contextlib import contextmanager

class Logger:
    def __init__(self, filename: str = ''):
        if filename == '':
            filename = str(uuid.uuid4())
        self.path = Path('./logs/' + filename + '.txt')
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.file = open(self.path, 'a', encoding='utf-8')

    def log(self, msg: str):
        self.file.write(f'{self.gettimef()} {msg}\n')

    def close(self):
        self.file.close()

    def gettimef(self) -> str:
        return datetime.now().strftime("[%H:%M:%S]")


@contextmanager
def logger_context(filename: str = ''):
    logger = Logger(filename)
    yield logger
    logger.close()


if __name__ == '__main__':
    with logger_context() as logger:
        dt = datetime.now()
        logger.log(f'test {dt}')
