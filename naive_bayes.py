from collections import Counter


class NaiveBayes:
    def __init__(self, training_set, labels):
        self._classes = list(set(labels))
        self._p_c = dict()

        counter = Counter(labels)

        for class_name in self._classes:
            class_probability = (counter.get(class_name) / len(labels))
            self._p_c[class_name] = class_probability

    def classify(self, document):
        pass
