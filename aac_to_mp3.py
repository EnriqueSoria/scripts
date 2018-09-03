from os import listdir as ls
from os.path import abspath
from subprocess import run

FFMPEG = r"C:\Another_apps\ffmpeg\bin\ffmpeg.exe"
command = '{program} -i "{inp}" -acodec libmp3lame "{out}"'
file_extension = '.aac'

for file in ls('.'):
	if file.endswith(file_extension):
		file = file.replace(file_extension, '')
		run(
			command.format(
				program = FFMPEG,
				inp = abspath('./' + file + file_extension),
				out = abspath('./' + file + '.mp3')
			)
		)