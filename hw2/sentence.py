from word import Word


class Sentence:
    def __init__(self, sentence_block):
        self._tokens = []
        for item in sentence_block:
            self._tokens.append(Word(item))

    def get_human_sentence(self):
        sentence = ""

        for token in self._tokens:
            form = token.get_form()
            if form != "_":
                sentence += " " + form

        return sentence

    def get_tokens(self):
        return self._tokens
