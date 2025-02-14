import subprocess
import re
from pathlib import Path

def init():
    ...
    directory = Path(input('Directory (./): ') or './')
    ext = (input('Extension (mp3): ').replace('.', '')) or 'mp3'
    reg_ex = re.compile(input('File RegEx (.*): ') or '.*')

    files: list[Path] = sorted(directory.rglob(f'**/*.{ext}'))
    filtered: list[Path] = list(filter(lambda f: reg_ex.search(f.name), files))

    list_path = Path(directory, 'list.txt')
    name = directory.name

    if len(filtered) == 0:
        input('No files found')
        return

    with open(list_path, 'w') as file:
        file.write("\n".join([f"file '{file.relative_to(directory)}'" for file in filtered]))

    cmd = f'ffmpeg.exe -f concat -safe 0 -i "{list_path}" -c copy "{Path(directory, f'{name}.{ext}')}"'

    try:
        subprocess.run(cmd, check=True)

        input(f'Finished: {name}.{ext}')
    except subprocess.CalledProcessError as error:
        input('Error: ' + str(error))

if __name__ == '__main__':
    init()

