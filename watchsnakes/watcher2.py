import os
import time

def snapshot(path):
    return {
            f: os.stat(os.path.join(path, f)).st_mtime for f in os.listdir(path)
            }

def watch(path: str = '.'):
    before = snapshot(path)
    print(before)
    while True:
        time.sleep(1)
        after = snapshot(path)
        added = after.keys() - before.keys()
        removed = before.keys() - after.keys()
        modified = {f for f in after.keys() & before.keys()
                    if after[f] != before[f]}

        for f in added:
            print('Added:', f)
        for f in removed:
            print('Removed:', f)
        for f in modified:
            print('Modified:', f)

        before = after


if __name__ == '__main__':
    watch('/home/nxr/Dev/toolbox')
