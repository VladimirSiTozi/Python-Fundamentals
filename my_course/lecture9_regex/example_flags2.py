import re

text = """start one
start two"""
print(re.findall('^start', text))
# MultiLine - 
print(re.findall('^start', text, re.MULTILINE))