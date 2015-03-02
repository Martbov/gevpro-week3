#!usr/bin/python3.4

import sys
from collections import namedtuple
import json

def main(argv):
    """" Checks for same meaning of the word blood and die in languages"""
    if len(argv) > 2:
        print("Usage: python3.4 json-file", file=sys.stderr)
        exit(-1)
    else:
        jsonFile = open(argv[1], 'r')
        jsonData = json.load(jsonFile)
    
        JsonTuple = namedtuple('JsonTuple', 'language, classifier, blood, die')
        namedtupleList = [JsonTuple(line[0], line[1], line[2].split(', '), line[3].rstrip().split(', ')) for line in jsonData]    
        jsonFilterList = [line for line in namedtupleList if len(set(line.blood) & set(line.die)) > 0]

        for line in jsonFilterList:
            print(line.language, line.classifier, ', '.join(line.blood), ', '.join(line.die))

if __name__ == '__main__':
    main(sys.argv)