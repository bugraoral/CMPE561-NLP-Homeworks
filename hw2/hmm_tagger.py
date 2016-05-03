import argparse
import shutil

import hw2.conllxi_reader as conllxi_reader
import hw2.file_util as file_util

START = "_start"


def tag(data_file, output_file):
    assert data_file is not None
    assert output_file is not None

    tag_transition_prob = file_util.read_dic(".transition_prob")
    word_tag_prob = file_util.read_dic(".word_prob")

    shutil.rmtree(output)

    sentences = conllxi_reader.read_conllxi(data_file)

    for sentence in sentences:
        tokens = sentence.get_valid_tokens()

        get_tags(tokens, tag_transition_prob, word_tag_prob)


def get_tags(tokens, tag_transition_prob, word_tag_prob):
    viterbi = dict(dict())
    viterbi[0] = dict()

    backpointer = dict(dict())
    backpointer[0] = dict()
    for tag in tag_transition_prob:
        if tag == START:
            continue
        viterbi[0][tag] = tag_transition_prob[START][tag] * word_tag_prob[tokens[0].get_representation()]

    for token in tokens[1:]:
        for tag in tag_transition_prob:



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('path', help='Path of test data')
    parser.add_argument('output', help='output file')

    opts = parser.parse_args()

    data = opts.path
    output = opts.output

    tag(data, output)

tag("metu_sabanci_cmpe_561_v2/test/turkish_metu_sabanci_test_blind_sample.conll", "blind_test_results.txt")
