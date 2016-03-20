import os
import shutil

import article_util
import file_util
import split_data
import tokenizer
from naive_bayes import NaiveBayes

TEST_PATH = "test"
TRAINING_PATH = "training"

RUN_DIRTY = False
VERBOSE = True


def clean_up():
    if os.path.exists(TRAINING_PATH):
        shutil.rmtree(TRAINING_PATH)
    if os.path.exists(TEST_PATH):
        shutil.rmtree(TEST_PATH)
    if os.path.exists(tokenizer.get_token_path(TRAINING_PATH)):
        shutil.rmtree(tokenizer.get_token_path(TRAINING_PATH))
    if os.path.exists(tokenizer.get_token_path(TEST_PATH)):
        shutil.rmtree(tokenizer.get_token_path(TEST_PATH))


if not RUN_DIRTY:
    clean_up()

if not RUN_DIRTY and not os.path.exists(TRAINING_PATH) and not os.path.exists(TEST_PATH):
    print("Splicing raw data")
    split_data.split_data("raw_texts")

training_labels_file = TRAINING_PATH + "/_label"
test_labels_file = TEST_PATH + "/_label"

print("Reading labels")
training_labels = file_util.read_line_list(training_labels_file)
test_labels = file_util.read_line_list(test_labels_file)

training_tokens_path = tokenizer.get_token_path(TRAINING_PATH)
test_tokens_path = tokenizer.get_token_path(TEST_PATH)

print("Tokenizing...")
if not os.path.exists(training_tokens_path):
    print("Tokenizing training set...")
    tokenizer.tokenize_path(TRAINING_PATH)
    print("Training set tokenization complete")

if not os.path.exists(test_tokens_path):
    print("Tokenizing test set...")
    tokenizer.tokenize_path(TEST_PATH)
    print("Test set tokenization complete")

print("Reading tokens")
training_set_tokens = article_util.load_tokenized_articals(training_tokens_path)
test_set_tokens = article_util.load_tokenized_articals(test_tokens_path)

print("Training naive bayes")
naive_bayes = NaiveBayes(training_set_tokens, training_labels)

print("Validating with training set")
correctClassification = 0
for i in range(len(training_set_tokens)):
    predictedClass = naive_bayes.classify(training_set_tokens[i])
    if VERBOSE:
        print("Predicted " + training_labels[i] + " as " + predictedClass)
    if predictedClass == training_labels[i]:
        correctClassification += 1

print("Number of correct classifications " + str(correctClassification))
print("Success Rate = %" + str((correctClassification / len(training_labels)) * 100))

print("*" * 50)

print("Validating with test set")
correctClassification = 0
for i in range(len(test_set_tokens)):
    predictedClass = naive_bayes.classify(test_set_tokens[i])
    if VERBOSE:
        print("Predicted " + test_labels[i] + " as " + predictedClass)
    if predictedClass == test_labels[i]:
        correctClassification += 1

print("Number of correct classifications " + str(correctClassification))
print("Success Rate = %" + str((correctClassification / len(test_labels)) * 100))
