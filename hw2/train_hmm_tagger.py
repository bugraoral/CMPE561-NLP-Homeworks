import argparse

TRAINING_PATH = None
TAGTYPE_POSTAG = None

START = "start"
END = "end"


def train():
    assert TRAINING_PATH is not None
    assert TAGTYPE_POSTAG is not None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('path', help='Re-split and tokenize')
    parser.add_argument('--postag', action="store_true",
                        help='uses cpostag by default input --postag to switcg')
    parser.add_argument('--cpostag', action="store_true",
                        help='uses cpostag by default input --postag to switcg')

    opts = parser.parse_args()

    TRAINING_PATH = opts.path
    TAGTYPE_POSTAG = opts.postag

    print(TRAINING_PATH + " " + str(TAGTYPE_POSTAG))

    train()
