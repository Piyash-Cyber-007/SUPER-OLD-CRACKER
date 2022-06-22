import os, sys
try:
    __import__("k").menu()
except Exception as e:
    exit(str(e))