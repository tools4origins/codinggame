import sys
import math


def debug(*args, **kwargs):
    parts = [
                "{}".format(arg) for arg in args
            ] + [
                "{}={}".format(key, value) for key, value in kwargs.items()
            ]
    print("DEBUG: " + " -- ".join(parts), file=sys.stderr)


class O:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "O({})".format(
            ", ".join(
                "{}={}".format(key, getattr(self, key))
                for key in dir(self)
                if not key.startswith("_")
            )
        )
