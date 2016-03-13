import os

import file_util


def get_article(file_name, f_encoding="windows-1254"):
    file = open(file_name, 'r', encoding=f_encoding)
    article = "\n".join(file.readlines()).strip()
    file.close()
    return article


def load_tokenized_articals(tokens_path):
    token_files = os.listdir(tokens_path)

    articles_tokens = []

    for file in token_files:
        article_tokens = file_util.read_dic(tokens_path + "/" + file)
        print(article_tokens)
        articles_tokens.append(article_tokens)

    return articles_tokens
