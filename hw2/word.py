class Word:
    def __init__(self, token_line):
        self._data = token_line.split("\t")

    def get_lemma(self):
        return self._data[2]

    def get_form(self):
        return self._data[1]
