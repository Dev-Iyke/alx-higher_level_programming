#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as te:
        print("Exception: {}".format(te), file=sys.stderr)
        return None
