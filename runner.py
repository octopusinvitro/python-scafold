import importlib
import sys

path = sys.argv[1][:-3].replace('/', '.')
script = importlib.import_module(path)

script.main()
