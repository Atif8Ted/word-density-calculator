import sys
from collections import Counter
class WordDensityCalc(object):




    def form_density_dictionary(self, word_file, fp_exclude):
        success_msg = '*Read file succesfully : {filename}'
        fail_msg = '**Could not read file: {filename}: Please check filename'
        empty_file_msg = '*No data in file :{filename}:**'
        exclude_read = self.open_file(fp_exclude, success_msg, fail_msg, '')
        exclude = Counter([word.lower() for word in exclude_read.split()])
        word_file_read = self.open_file(word_file, success_msg, fail_msg, empty_file_msg)
        words = Counter([word.lower() for word in word_file_read.split()])
        unique_words = words - excluded
        self.freq_dictionary = {word: '{.2f}'.format(count / len(unique_words))
                            for word, count in unique_words.items()}

    def open_file(self, filename, success_msg, fails_msg, empty_file_msg):
        try:
           with open(filename, 'r') as file:
               if success_msg:
                   print(success_msg.format(filename= filename))
               data = file.read()
               if empty_file_msg:
                   print(empty_file_msg.format(filename= filename))
               return data
        except IOError:
               if fail_msg:
                   print(fail_msg.format(filename= filename))
               sys.exit()

    def top_freq(self,top_freq):
        return(sorted(self.freq_dictionary.items(),
        reverse=True,key=lambda x:x[1]))[:top_freq]

    def least_freq(self,least_freq):
        return(sorted(self.freq_dictionary.items(),
        reverse=False,key=lambda x:x[1]))[:least_freq]


def main():
    user_args=sys.argv[1:]
    try:
        word_file,exclude_file,freq=user_args

    except ValueError:
        print("Needed 3 arguments , supplied  %d" %len(user_args))
        print("Usage: python3 word_freq_dict.py word_file exclude_file 10")
        sys.exit()
    s=WordDensityCalc()
    s.form_density_dictionary(word_file,exclude_file)
    top=(s.top_freq(int(freq)))
    least=(s.least_freq(int(freq)))
    print()
    print("Top %d used words are :" %int(freq),end=" ")
    print(top)
    print()
    print("Least %d used words are :" %int(freq),end=" ")
    print(least)

if __name__=="__main__":
    main()
