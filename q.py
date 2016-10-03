import sys


class WordDensityCalc:
    def __init__(self):
        self.freq_dictionary = {}

    def form_density_dictionary(self, word_file, exclude_file):
        words_excluded = self.read_words_list(exclude_file)
        words_excluded = self.lowercase(words_excluded)

        words_list = self.read_words_list(word_file)
        if len(words_list) == 0:
            print("** No data in file: {} **".format(word_file))
            sys.exit()

        words_list = self.lowercase(words_list)

        unique_words = list((set(words_list) - set(words_excluded)))

        self.freq_dictionary = {
            word: ("{:6.2f}".format(
                float((words_list.count(word)) / len(words_list)) * 100))
            for word in unique_words
            }

    @staticmethod
    def read_words_list(file_name):
        try:
            with open(file_name, 'r') as file:
                data = file.read()
                print("**  Read file successfully: {} **".format(file_name))
                return data.split()
        except IOError as e:
            print("** Could not read file: {0.filename} **".format(e))
            sys.exit()

    @staticmethod
    def lowercase(word_list):
        return [word.lower() for word in word_list]
