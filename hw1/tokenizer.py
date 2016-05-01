import os
import re
import shutil
from collections import Counter

import file_util

import article_util

TOKENS_PATH_SUFFIX = "tokens"

token_regex = re.compile("\w\w+")


def tokenize(article):
    article_tokens = re.findall(token_regex, article)
    article_tokens = map(str.lower, article_tokens)
    article_tokens = dict(Counter(article_tokens))

    article_tokens['NOfWords'] = len(re.findall(token_regex, article))
    article_tokens['NOfCommas'] = len(re.findall(',', article))
    return article_tokens


def get_token_path(path):
    return path + "_" + TOKENS_PATH_SUFFIX


def tokenize_path(path):
    tokens_path = get_token_path(path)

    if os.path.exists(tokens_path):
        shutil.rmtree(tokens_path)

    os.mkdir(tokens_path)

    articals = os.listdir(path)

    for artical in articals:
        if artical.startswith("_"):
            continue

        file_util.write_dic(tokens_path + "/" + artical, tokenize(article_util.get_article(path + "/" + artical)))

    return tokens_path

# tokens = tokenize(article_util.get_article("training/abbasGuclu_12.txt"))

# print(tokens)
# print("Length = " + str(len(tokens)))

# file_util.write_dic("testing_token_write.txt", tokens)
# print(20 * "=")
# print(file_util.read_dic("testing_token_write.txt"))
