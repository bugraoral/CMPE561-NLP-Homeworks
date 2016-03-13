import json
import os
import re
import shutil
from collections import Counter

TOKENS_PATH_SUFFIX = "tokens"

token_regex = re.compile("\w+")


def get_article(file_name, f_encoding="windows-1254"):
    file = open(file_name, 'r', encoding=f_encoding)
    article = "\n".join(file.readlines()).strip()
    file.close()
    return article


def tokenize(article):
    article_tokens = re.findall(token_regex, article)
    return dict(Counter(article_tokens))


def write_tokens(filename, tokens, f_encoding='windows-1254'):
    with open(filename, 'w', encoding=f_encoding) as file:
        json.dump(tokens, file, ensure_ascii=False)

        # with open(filename, 'wb') as handle:
        #    pickle.dump(tokens, handle)


def read_tokens(filename, f_encoding='windows-1254'):
    with open(filename, 'r', encoding=f_encoding) as file:
        return json.load(file)

        # with open(filename, 'rb') as handle:
        #    return pickle.load(handle)


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

        write_tokens(tokens_path + "/" + artical, tokenize(get_article(path + "/" + artical)))


tokenize_path("training")
tokenize_path("test")


# tokens = tokenize(get_article("training/abbasGuclu_11.txt"))

# print(tokens)
# print("Length = " + str(len(tokens)))

# write_tokens("testing_token_write.txt", tokens)
# print(20 * "=")
# print(read_tokens("testing_token_write.txt"))
