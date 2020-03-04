class Jumble():

    def __init__(self, path_file, four_words):
        self.path_file = path_file
        self.four_words = four_words
        self.actual_words = []
        self.sorted_four_words = [] # ['eisst', 'horsu', 'dlo', 'aert']


        for word in self.four_words:
            word = "".join(sorted(word))
            self.sorted_four_words.append(word)

        with open(self.path_file) as file:
            for line in file:
                word = line.strip().split()[0] # eht
                if "".join(sorted(word)) in self.sorted_four_words:
                    self.actual_words.append(word)
    
    def arrange_words(self):
        new_actual_words = []
        for w in self.sorted_four_words:
            for inner_w in self.actual_words:
                if sorted(w) == sorted(inner_w):
                    new_actual_words.append(inner_w)
        return new_actual_words

    def is_four_words_in_text(self):
        # return len(self.sorted_four_words) == len(self.actual_words)
        return self.sorted_four_words, self.arrange_words()
                

if __name__ == "__main__":
    path = "words.txt"
    four_words = ["tefon", "sokik", "niumem", "siconu"]
    j = Jumble(path, four_words)
    j.arrange_words()
    print(j.is_four_words_in_text())