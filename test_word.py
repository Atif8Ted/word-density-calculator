import sys
from collections import Counter

class WordDensityCalc(object):
    def form_density_dictionary(self, word_file, fp_exclude):
        success_msg = '*Read file succesfully : {filename}'
        fail_msg = '**Could not read file: {filename}: Please check filename'
        empty_file_msg = '*No data in file :{filename}:**'
        try:
           with open(fp_exclude, 'r') as fp2:
               words_excluded = (fp2.read().split())
               print(success_msg.format(filename= fp_exclude))
        except IOError:
            print(fail_msg.format(filename= fp_exclude))
            sys.exit()

        try:
            with open(word_file, 'r') as file:
                print(success_msg.format(filename= word_file))
                words_list = file.read()
                if not words_list:
                    print(empty_file_msg.format(filename= words_file))
                words = Counter([word.lower() for word in words_list.split()])
                unique_words = set(words) - set(words_excluded)
                self.freq_dictionary= {word:("%6.2f"%(float((words_list.count(word))/len(words_list))*100))  for word in unique_words}
                print(self.freq_dictionary)

        except IOError:
            print(fail_msg.format(filename= word_file))
            sys.exit()

    def top_freq(self,top_freq):
        return(sorted(self.freq_dictionary.items(), reverse=True,key=lambda x:x[1]))[:top_freq]


    def least_freq(self,least_freq):
        return(sorted(self.freq_dictionary.items(), reverse=False,key=lambda x:x[1]))[:least_freq]


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
