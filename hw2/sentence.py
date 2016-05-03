from word import Word


class Sentence:
    def __init__(self, sentence_block):
        self._tokens = []
        for item in sentence_block:
            self._tokens.append(Word(item))

    def get_tokens(self):
        return self._tokens

    def get_valid_tokens(self):
        valids = []

        for item in self._tokens:
            if item.get_form() != "_":
                valids.append(item)

        return valids

    def get_human_sentence(self):
        sentence = ""

        for token in self.get_valid_tokens():
            sentence += " " + token.get_form()

        return sentence
