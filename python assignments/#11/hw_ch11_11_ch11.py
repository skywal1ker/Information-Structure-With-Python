class Sentence:
    def __init__(self, Sentencestr):
        self.s_array = Sentencestr.split()
    def get_first_word(self):
        return self.s_array[0]
    def get_all_words(self):
        return self.s_array
    def replace(self, index, n_word):
        if 0 <= index <= len(self.s_array):
            self.s_array[index] = n_word

a = Sentence("I am going back")
print(a.get_first_word())
print(a.get_all_words())
a.replace(3, "Home")
print(a.get_all_words())
