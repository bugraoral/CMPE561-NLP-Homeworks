import os

import article_util
import file_util
import tokenizer
from naive_bayes import NaiveBayes

training_labels = "training/_label"
test_labels = "training/_label"

labels = file_util.read_line_list(training_labels)
print(labels)

training_tokens_path = tokenizer.get_token_path("training")

if not os.path.exists(training_tokens_path):
    tokenizer.tokenize_path(training_tokens_path)

training_set_tokens = article_util.load_tokenized_articals(training_tokens_path)

naive_bayes = NaiveBayes(training_set_tokens, test_labels)
