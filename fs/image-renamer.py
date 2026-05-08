from pathlib import Path
import secrets

IMAGE_EXTS = ['.png', '.jpg', '.jpeg', '.webp', '.gif']


def main():
    files = [f for f in Path('.').iterdir() if f.is_file()]
    images = [f for f in files if f.suffix in IMAGE_EXTS]
    for img in images:
        new_name = secrets.token_hex(16)
        ext = img.suffix
        img.rename('./' + new_name + ext)


if __name__ == '__main__':
    main()
