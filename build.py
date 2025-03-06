from PyInstaller.__main__ import run

run([
    'main.py',
    '--onefile',
    '--name' ,
    'audio-combiner',
    '--icon',
    'icon.ico'
])