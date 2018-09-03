import argparse
from subprocess import run
from time import sleep
from os import listdir as ls
import sys

parser = argparse.ArgumentParser(
	description='Repeat commands'
)

parser.add_argument('command')
parser.add_argument('-d', '--delay', help='delay in seconds', type=float)
parser.add_argument('-l', '--ls', action='store_true', help='performs `for file in ls(".")`. Example: repeat.py "echo {file}" --ls')
parser.add_argument('-r', '--range', type=int, nargs=2)

args = parser.parse_args()

if sys.stdin:
	for line in sys.stdin:
		command = args.command.format(
			file=line
		)
		run(command)

if args.range:
	for number in range(args.range[0], args.range[1]):
		command = args.command.format(
			number=number
		)
		run(command)
		if args.delay:
			sleep(args.delay)
elif args.ls and '{file}' in args.command:
	autonumber = autonumber or 1
	for file in ls('.'):
		command = args.command.format(
			file=file,
			number=autonumber
		)
		run(command)
		if args.delay:
			sleep(args.delay)
		autonumber += 1
else:
	while True:
		run(args.command)
		if args.delay:
			sleep(args.delay)
