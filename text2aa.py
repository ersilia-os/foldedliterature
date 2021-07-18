import os
import collections
import random

AA = "ARNDCQEGHILKMFPSTWYV"

def text2aa(text):
    char_counts = collections.defaultdict(int)
    seq = ""
    for char in text:
        if char.isalpha():
            char = char.upper()
            char_counts[char] += 1
            seq += char
    all_chars = set([x for x in char_counts.keys()])
    aa_chars = set([x for x in AA])
    literal_chars = all_chars.intersection(aa_chars)
    missing_chars = all_chars.difference(aa_chars)
    free_chars = aa_chars.difference(all_chars)
    nm = len(missing_chars)
    nf = len(free_chars)
    if nm > nf:
        ns = nm-nf
        free_chars_ = set([x[0] for x in sorted(char_counts.items(), key=lambda x: x[1])][:ns])
        free_chars.update(free_chars_)
    else:
        free_chars = random.sample(list(free_chars), nm)
    missing_chars = sorted(missing_chars)
    free_chars = sorted(free_chars)
    code = {}
    for c in list(literal_chars):
        code[c] = c
    for x,y in zip(missing_chars, free_chars):
        code[x] = y
    seq = [code[c] for c in seq]
    return "".join(seq)


def textfile2aa(prefix):
    file_name = prefix+".txt"
    with open(os.path.join("data", file_name), "r") as f:
        text = f.read()
    return text2aa(text)
