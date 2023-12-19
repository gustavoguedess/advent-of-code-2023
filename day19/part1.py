import sys
import re

def parse_input(data):

    _workflows, points = data.split('\n\n')

    workflows = {}
    for line in _workflows.split('\n'):
        key, var, op, num, accept, reject = re.findall(r'(\w+)\{(\w)([\<\>])(\d+):(\w+),(.+)\}', line)[0]
        workflows[key] = {
            'variable': var,
            'operator': op,
            'number': int(num),
            'accept': accept,
            'reject': reject
        }
    
    ratings = []
    for line in points.split('\n'):
        points = points.replace('{', '').replace('}', '')
        print(line)
        rat = {k: int(v) for k, v in re.findall(r'(\w)=(\d+)', line)}
        ratings.append(rat)
    return workflows, ratings

def calc(workflows, ratigns):
    
    return sum(map())
    
############## MAIN #################
    
data = sys.stdin.read()
workflows, ratings = parse_input(data)
print(ratings)