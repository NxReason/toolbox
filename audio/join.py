import sys
import secrets
from pathlib import Path
from pydub import AudioSegment


class Params:
    def __init__(self, path: str = '.', silence: str = '1000'):
        self.path = path
        self.silence = int(silence)


def main():
    params = Params(*(sys.argv[1:]))

    files = read_dir(params.path)
    silence = AudioSegment.silent(duration=params.silence)

    playlist = AudioSegment.empty()
    for f in files:
        playlist += AudioSegment.from_file(f) + silence
    playlist.export(f"out_{secrets.token_hex(4)}.wav", format="wav")


def read_dir(path: str) -> list[str]:
    dir = Path(path)
    extensions = ('.mp3', '.wav')
    files = sorted([str(f)
                   for f in dir.iterdir() if f.suffix.lower() in extensions])
    return files


if __name__ == '__main__':
    main()
