import time
from pathlib import Path

def print_tree(path: Path, pad: int = 0, *, show_hidden: bool = False):
    for sub in path.iterdir():
        if not show_hidden and sub.name.startswith('.'):
            continue
        print(f'{' ' * pad}{sub.name}')
        if sub.is_dir():
            print_tree(sub, pad + 4, show_hidden=show_hidden)

class FileSnap:
    def __init__(self, name: str, m_time: float, contents: list[FileSnap] | None = None):
        self.name = name
        self.m_time = m_time
        self.contents = contents

    def __repr__(self) -> str:
        return self._rec_repr(0)

    def _rec_repr(self, pad: int=0) -> str:
        t = 'Dir' if self.contents is not None else 'File'
        result = f'{' ' * pad}{t}: {self.name} ({self.m_time})\n'
        if not self.contents:
            return result
        for sub in self.contents:
            result += sub._rec_repr(pad + 4)
        return result

    @classmethod
    def diff(cls, left: list[FileSnap], right: list[FileSnap]):
        left_dict = { snap.name: snap.m_time for snap in left }
        right_dict = { snap.name: snap.m_time for snap in right }
        intersect = right_dict.keys() & left_dict.keys()
        updated = set()
        for key in intersect:
            if left_dict[key] != right_dict[key]: updated.add(key)
        return {
                'added': right_dict.keys() - left_dict.keys(),
                'removed': left_dict.keys() - right_dict.keys(),
                'updated': updated
                }

def snapshot(path: Path, track_hidden: bool=False) -> FileSnap:
    result = FileSnap(path.name, path.stat().st_mtime)
    if path.is_file():
        return result

    result.contents = []
    for sub in path.iterdir():
        if not track_hidden and sub.name.startswith('.'):
            continue
        contents_snap = snapshot(sub, track_hidden)
        result.contents.append(contents_snap)

    return result


def diff(prev: FileSnap, curr: FileSnap):
    if prev.contents and curr.contents:
        print(FileSnap.diff(prev.contents, curr.contents))

if __name__ == '__main__':
    p = Path().resolve()
    prev = snapshot(p)
    while True:
        time.sleep(.3)
        curr = snapshot(p)
        diff(prev, curr)
        prev = curr

