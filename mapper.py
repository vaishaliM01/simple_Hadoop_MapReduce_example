#!/usr/bin/env python
import sys
import string

stopwords = set(['the', 'and', 'for', 'I', 'four'])
# checking all punctuation marks other than -
for line in sys.stdin:
    chars = [c for c in line if c not in string.punctuation.replace("-", "") ]
    line = ''.join(chars)
    tokens = line.split()
    # Splitting words based on -
    for token in tokens:
        words = token.split("-")
        # Checking for stopwords
        for word in words:
            if word not in stopwords:
                print '%s\t%s' % (word, "1")

