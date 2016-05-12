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
        self._vocabulary = dict()

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
                    if token in self._vocabulary:
                        self._vocabulary[token] += article.get(token)
                    else:
                        self._vocabulary[token] = article.get(token)

        self._class_token_counts = dict()

        for article_class in self._class_word_occurrence.keys():
            self._class_token_counts[article_class] = sum(self._class_word_occurrence[article_class].values())

        self._class_word_count = dict()
        for article_class in self._classes:
            self._class_word_count[article_class] = 0
            for token in self._vocabulary:
                if token in self._class_word_occurrence[article_class]:
                    self._class_word_count[article_class] += self._class_word_occurrence[article_class][token]

    def classify(self, document: dict, n_of_words, n_of_commas):

        probabilities = dict()

        for article_class in self._classes:

            probabilities[article_class] = math.log1p(self._p_c[article_class])

            for token in document.keys():
                '''
                Extra features
                '''
                if token == 'NOfWords' and n_of_words:
                    continue

                if token == 'NOfCommas' and n_of_commas:
                    continue

                word_in_class_count = 0
                if token in self._class_word_occurrence[article_class]:
                    word_in_class_count = self._class_word_occurrence[article_class][token]

                word_in_class_count += 0.01
                probabilities[article_class] += math.log1p(
                    (word_in_class_count / (self._class_word_count[article_class] + 0.01 * len(self._vocabulary))))

        author = max(probabilities.items(), key=operator.itemgetter(1))[0]
        # print("Author Prob : " + str(probabilities[author]))
        return author
