#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author:  Çağıl Uluşahin Sönmez
# Created: 25 Feb 2016
# Last Updates: 11 March 2016

import argparse, re, os, sys, traceback
import enchant

dict = enchant.Dict("en_US")
ARTICLE = ""
VERBOSE = False


def get_article(filename="./raw_texts/gulseBirsel/1.txt", file_encoding="windows-1254"):
    """ Given a filename reads the content of the file into a string
    Args:
        filename (str): Full path to the file. Defaults to ./raw_texts/gulseBirsel/1.txt
        encoding (str): Encoding of the file. Defaults to "windows-1254" and alternative would be
                        "ISO-8859-1" or "utf-8"
    Returns:
        str: the text content in the given file

    Raises:
        FileNotFoundError: raises if there is no such file
        UnicodeDecodeError: raises when the given encoding is different than the original encoding of the file.

    Examples:

        >>> print(ps_week_04.get_article())
        Yıllardır restorandı, oteldi şuydu buydu tavsiye ettiğim yok. Memleketin hali ....

        >>> print(ps_week_04.get_article(filename = "./raw_texts/gulseBirsel/1.txt", file_encoding="windows-1254"))
        Yıllardır restorandı, oteldi şuydu buydu tavsiye ettiğim yok. Memleketin hali ....

        >>> print(ps_week_04.get_article(filename = "/Users/cgl/ex/raw_texts/gulseBirsel/1.txt", file_encoding="windows-1254"))
        Yıllardır restorandı, oteldi şuydu buydu tavsiye ettiğim yok. Memleketin hali ....
    """
    if ARTICLE:
        return ARTICLE
    with open(filename, encoding=file_encoding) as file:  #
        lines = file.readlines()
    article = "\n".join(lines).strip()
    return article


def regex_alternatives(article=get_article()):
    """ Some regex examples
    Args:
        article (str): The given text to process. Defaults to global variable ARTICLE
    Returns:
        list: calculates all the regex expressions and returns all answers as a list of list of str
    """
    return [re.findall(r'\w', article),
            re.findall(r's\w ', article),
            re.findall(r's\w+ ', article),
            re.findall(r'[ ,.]s\w+ ', article),
            re.findall(r'[ ,.](s\w+) ', article),  #
            re.findall(r'[ ,.]+([sS]\w+) ', article),
            re.findall(r'[ ,.]*([sS]\w+) ', article),
            re.findall(r'[ ,.]?([sS]\w+) ', article),
            re.findall(r'[ ,.]+(s\w+) ', article),  #
            re.findall(r'[ ,.](S\w+)[ ,]', article),  #
            re.findall(r'[ ,.](S\w+)[ ,](\w+)', article),
            re.findall(r'\b(s\w+)\b', article),
            re.findall(r'\b([s|S]\w+)\b', article),
            re.findall(r'(?:ben|sen)', article),
            ]


def print_hello(**kwargs):
    print("Hello")


def find_all_startswith_s(article=get_article(), **kwargs):  # exercise 1
    """ Given a text(str) finds and prints all the words in the text which starts with letter "s"
    Args:
        article (str): The given text to process. Defaults to global variable ARTICLE
        **kwargs: Arbitrary keyword arguments.
    """
    match = re.findall(r'[ ,.]+(s\w+) ', article)
    match = re.findall(r'\b(s\w+)\b', article)  # [ ,.!?]+
    for token in match: print(token)
    print("Total %d tokens" % len(match))


def find_all_startswith(article=get_article(), **kwargs):  # exercise 2
    """ Given a text(str) finds and prints all the words in the text which starts with given token.
    Args:
        article (str): The given text to process. Defaults to global variable ARTICLE
        token (str): The search token (letter(s)) to use in the search. Deafults to "s"
    Returns:
        list of str: the list of matching words, [] if None
    Examples:

      >>> print(ps_week_04.find_all_startswith())
      Found 40 tokens
      ['sebep', 'sokaklara', 'sebep', 'sevdiğim', 'stili', 'suşi', 'söylenen', 'sonra', 'siyah', 'sordum', 'santime', 'santim', 'siyah', 'sade', 'sipariş', 'satış', 'sipariş', 'sadece', 'sordum', 'sayıyla', 'ses', 'saniye', 'satış', 'sonra', 'sözkonusu', 'sokaklarına', 'sıralamak', 'sucuklu', 'salata', 'süsleri', 'sigara', 'senaryosunu', 'sinema', 'sokağının', 'salonundan', 'semtlerinin', 'sonra', 'sofrasını', 'sürükleyici', 'siyasi']

        >>> print(ps_week_04.find_all_startswith(token="ed"))
        Found 3 tokens
        ['edebiliriz', 'eden', 'edilebilir']

        >>> print(ps_week_04.find_all_startswith(token="en"))
        Found 5 tokens
        ['en', 'en', 'en', 'en', 'en']
    """
    search_token = kwargs['token']
    match = re.findall(r'[ ,.]+(%s\w*)' % search_token, article)
    # match = re.findall(r'\b(s\w*)\b',article) # [ ,.!?]+
    print("Found %d tokens" % len(match))
    if VERBOSE:
        for token in match: print(token)
    return match


def find_all_pronouns(article=get_article(), **kwargs):  # exercise 3
    """ Given a text(str) finds and prints all the words in the text which starts with given tokens.
    Args:
        article (str): The given text to process. Defaults to global variable ARTICLE
        token (str): The search token (letter(s)) to use in the search
    Returns:
        list of str: the list of matching words, [] if None
    Examples:

        >>> print(ps_week_04.find_all_startswith(token="ed"))
        Found 3 tokens
        ['edebiliriz', 'eden', 'edilebilir']

        >>> print(ps_week_04.find_all_startswith(token="en"))
        Found 5 tokens
        ['en', 'en', 'en', 'en', 'en']
    """
    match = re.findall(r'(?:ben|sen)', article)
    print("Total %d tokens" % len(match))
    if VERBOSE:
        for token in match: print(token)
    return match


def normalize(**kwargs):  # exercise 4
    text = "I frgot to introdce myself"
    if kwargs['sentence'] != "":
        text = kwargs['sentence']
    candidates = re.findall(r'\b(\w?[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]{3}\w*)\b', text)
    print("Some normalization suggestions for '%s'" % text)
    for token in candidates:
        if not dict.check(token):
            print("---> You may want to spellcheck %s as %s" % (token, dict.suggest(token)[0] or ""))


def dive_into_folders(**kwargs):  # exercise 5
    path = "./raw_texts/gulseBirsel"
    if kwargs['path']:
        path = kwargs['path']
    file_encoding = kwargs['encoding']
    files = [filename for filename in os.listdir(path) if filename.endswith(".txt")]
    for filename in files[0:5]:
        with open(os.path.join(path, filename), encoding=file_encoding) as file:
            try:
                lines = file.readlines()
            except UnicodeDecodeError:
                sys.stderr.write("Error in file %s\n" % os.path.join(path, filename))
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
                continue
        outputfilename = "/tmp/myfile.html"
        with open(outputfilename, "wt", encoding=file_encoding) as outputfile:
            print("<html>" + "\n".join(lines[0:3]) + "</html>", file=outputfile)
            print("Converted %s/%s to html see: %s" % (path, filename, outputfilename))


def write_csv_file(**kwargs):  # exercise 6
    los = ["I", "am", "here"]
    los2 = ["She", "is", "there"]
    with open("/tmp/my_csv_file.csv", "wt") as my_file:
        print(",".join(los), file=my_file)
        print(",".join(los2), file=my_file)
        # cat /tmp/my_csv_file.csv


def list_all_files(**kwargs):  # exercise 7
    """ Lists all files in a folder with depth 2
        A better and efficient implementation can be found below in function alternative_list_all_files
    Args:
       path (str): Path of the folder. Defaults to "./raw_texts"

    Examples:

       >>> list_all_files()
       ./raw_texts
       ./raw_texts/.DS_Store
       ./raw_texts/abbasGuclu
       ./raw_texts/abbasGuclu/1.txt
       ./raw_texts/abbasGuclu/10.txt
       ...

       >>> list_all_files(path="/Users/cagil/brat/data/full_main/")
       /Users/cagil/Downloads/brat/data/full_main/
       /Users/cagil/Downloads/brat/data/full_main/.DS_Store
       /Users/cagil/Downloads/brat/data/full_main/.stats_cache
       /Users/cagil/Downloads/brat/data/full_main/0.ann
       /Users/cagil/Downloads/brat/data/full_main/0.txtprint
       ...
    """
    path = "./raw_texts" if not "path" in kwargs or not kwargs["path"] else kwargs["path"]
    folders = os.listdir(path)
    print(path)
    for folder_name in folders:
        print(os.path.join(path, folder_name))
        if os.path.isdir(os.path.join(path, folder_name)):
            for filename in os.listdir(os.path.join(path, folder_name)):
                print(os.path.join(path, folder_name, filename))


def alternative_list_all_files(path):  # exercise 7
    """
    Examples:
        >>> alternative_list_all_files("./raw_texts/")
        [['./raw_texts/abbasGuclu/1.txt',
          './raw_texts/abbasGuclu/10.txt',
          './raw_texts/abbasGuclu/11.txt',
        ...
    """
    return [[os.path.join(dirpath, filename) for filename in filenames if filename[-4:].lower() == ".txt"] for
            (dirpath, dirnames, filenames) in os.walk(path)]


# source: http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html
def example_generator(n):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    for i in range(n):
        yield i


def exercises(index, **kwargs):
    ex_dict = [print_hello,
               find_all_startswith_s,
               find_all_startswith,
               find_all_pronouns,  # 3
               normalize,  # 4
               dive_into_folders,
               write_csv_file,
               list_all_files,
               ]
    ex_dict[index](**kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--exercise', default=0, type=int, help='Number of exercise')
    parser.add_argument('-t', '--token', default="s", type=str, help='A token ex: -t hello ')
    parser.add_argument('-p', '--path', type=str, help='Path to something')
    parser.add_argument('-s', '--sentence', default="", type=str, help='A example sentence')
    parser.add_argument('-e', '--encoding', default="windows-1254", type=str, help='File encoding')
    parser.add_argument('-pl', '--pronoun_list', default="ben,sen", help='Comma separated list of words')
    opts = parser.parse_args()
    opts.exercise = int(opts.exercise)
    opts.pronoun_list = opts.pronoun_list.split(",")
    opts.encoding = opts.encoding
    ARTICLE = get_article()
    VERBOSE = True
    exercises(opts.exercise, path=opts.path, token=opts.token, sentence=opts.sentence, encoding=opts.encoding)
