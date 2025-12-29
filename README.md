# python-command-line-compressor
Python command line application that compresses specified files.

(.venv) ➜  clcomp git:(main) ✗ ./clcomp.py -h   
usage: clcomp.py [-h] [-v] files [files ...]

Compress files from the command line

positional arguments:
  files          File(s) to compress (supports wildcards like *.txt)

options:
  -h, --help     show this help message and exit
  -v, --verbose  Enable verbose output

Examples:
  clcomp.py file.txt
  clcomp.py *.txt
  clcomp.py file1.txt file2.txt
  clcomp.py data/*.log
