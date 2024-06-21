import json
from pypinyin import pinyin, lazy_pinyin, Style
from pypinyin_dict.pinyin_data import ktghz2013
from pypinyin.contrib.tone_convert import to_normal, to_tone, to_initials, to_finals
from tqdm import tqdm
import numpy as np
import Levenshtein


def levenshtein_similarity(py1, py2):
    py1, py2 = to_normal(py1), to_normal(py2)
    return Levenshtein.ratio(py1, py2)


def calculate(char1, char2):
    py1 = pinyin(char1, style=Style.TONE3, heteronym=True)[0]
    py2 = pinyin(char2, style=Style.TONE3, heteronym=True)[0]
    similarity_max = 0
    for i in py1:
        for j in py2:
            similarity = levenshtein_similarity(i, j)
            if similarity > similarity_max:
                similarity_max = similarity
    return similarity_max


if __name__ == '__main__':
    char1 = "未"
    char2 = "维"
    print(calculate(char1, char2))

