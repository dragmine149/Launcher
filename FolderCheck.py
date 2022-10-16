import os
import argparse
import re

def CheckFiles(folder):
    return False


def parserFunc():
    parser = argparse.ArgumentParser(description="Readme updater info")
    parser.add_argument("-fc", default="")

    return vars(parser.parse_args())


args = parserFunc()

print(args["fc"])

if str(args["fc"]).find("-fc") == -1:
    CheckFiles("w")
