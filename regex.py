'''
Simple Regex examples

note: https://regex101.com/ is a handy regex tester
'''

import re

sample_text = """
tknk (41) -> ujml, padx, fwft
pbga (66)
"""

one_liner = "~tknk (41) -> ujml, padx, fwft"

pattern_1 = r'(?P<element>\w+)[ \t]+\(\d+\)[ \t]+->[ \t](?P<children>[\w, ]+)'
pattern_2 = r'(?P<element>\w+)[ \t]+\(\d+\)$'

# `match` returns a Match object if a string starts with the specified pattern and None otherwise
match_object = re.match(pattern_1, one_liner)

if match_object:
    element = match_object.groupdict()['element']
    children = match_object.groupdict()['children'].split(', ')
    print("element: {}, children: {}".format(element, children))

else:
    print("no match")

# `search` returns the first matching Match object if one is found in the string, and None otherwise
match_object_2 = re.search(pattern_1, sample_text)

if match_object_2:
    element = match_object_2.groupdict()['element']
    children = match_object_2.groupdict()['children'].split(', ')
    print("element: {}, children: {}".format(element, children))

else:
    print("no match")

