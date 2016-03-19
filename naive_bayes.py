import collections
import math
import operator
from collections import Counter


class NaiveBayes:
    def __init__(self, training_set, labels):

        assert len(training_set) == len(labels)

        self._classes = list(set(labels))
        self._p_c = dict()
        self._class_word_occurrence = collections.defaultdict(dict)

        counter = Counter(labels)

        for class_name in self._classes:
            class_probability = (counter.get(class_name) / len(labels))
            self._p_c[class_name] = class_probability

        for i in range(len(training_set)):
            article = training_set[i]
            article_class = labels[i]

            if isinstance(article, dict):
                for token in article.keys():
                    if token in self._class_word_occurrence[article_class]:
                        self._class_word_occurrence[article_class][token] += article.get(token)
                    else:
                        self._class_word_occurrence[article_class][token] = article.get(token)

        self._class_token_counts = dict()

        for article_class in self._class_word_occurrence.keys():
            self._class_token_counts[article_class] = sum(self._class_word_occurrence[article_class].values())

    def classify(self, document: dict):

        probabilities = dict()

        for article_class in self._classes:
            probabilities[article_class] = math.log10(self._p_c[article_class])

            for token in document.keys():
                token_in_class_count = 0
                if token in self._class_word_occurrence[article_class]:
                    token_in_class_count = self._class_word_occurrence[article_class][token]
                probabilities[article_class] += math.log10(
                    ((token_in_class_count + 1) / (self._class_token_counts[article_class] + len(document))) * document[
                        token])

        return max(probabilities, key=operator.itemgetter(1))[0]
