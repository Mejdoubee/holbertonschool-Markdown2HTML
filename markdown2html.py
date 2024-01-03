#!/usr/bin/python3
'''
Markdown to HTML Module 
'''
import os
import sys

def main():
	if len(sys.argv) < 3:
		print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
		exit(1)

	try:
		with open(sys.argv[1], 'r') as f:
			pass
	except FileNotFoundError:
		print(f'Missing {sys.argv[1]}', file=sys.stderr)
		exit(1)

	exit(0)

if __name__ == "__main__":
    main()
