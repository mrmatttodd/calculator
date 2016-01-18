""" Tokenizer """

import re

TOKEN_REGEX = '([\+)\-\*\/])+'

def tokenize_line(line):

    pattern = re.compile(r'\s+')
    line = re.sub(pattern, '', line)

    result = re.split(TOKEN_REGEX, line)

    return result
