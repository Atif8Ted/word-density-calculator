'''
Poject title : To find word density : Topic 7
'''
'''
Team Members: Atif Imam : U101113FCS194 :S3
              Ekta Tiwari : U101113FCS283 :S3
              Aakanksha Kapoor : U101113FCS267 :S5
              Tanya Ghumman : U101113FCS285 :S3

'''
'''
word_file : Contains all the words
exclude_file : contains words to be excluded
usage : python3 word_density.py word_file exclude_file 10
'''

import sys

class WordDensityCalc(object):
    def __init__(self):
        self.freq_dictionary={}

    #forms density dictionary based on frequency of usage
    def form_density_dictionary(self,word_file,exclude_file):
        words_excluded=self.read_file(exclude_file)
        words_excluded=self.lowercase(words_excluded)

        words_list=self.read_file(word_file)
        if len(words_list)==0:
            print("No data in file: {}".format(word_file))
            sys.exit()

        words_list=self.lowercase(words_list)

        unique_words=list(set(words_list)-set(words_excluded))

        self.freq_dictionary = {
            word: ("{:6.2f}".format(
                float((words_list.count(word)) / len(words_list)) * 100))
            for word in unique_words
            }

    def top_freq_calc(self,top_freq):
        return(sorted(self.freq_dictionary.items(),
        reverse=True,key=lambda x:x[1]))[:top_freq]

    def least_freq_calc(self,least_freq):
        return(sorted(self.freq_dictionary.items(),
        reverse=False,key=lambda x:x[1]))[:least_freq]

    #can be done using staticmethod
    def read_file(self,file_name):
        try:
            with open(file_name,'r') as file:
                data=file.read()
                return data.split()

        except IOError as e:
            print("Could not read file:{0.filename}".format(e))
            sys.exit()

    #can be done using staticmethod
    def lowercase(self,word_list):
        return [word.lower() for word in word_list]

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
    top=(s.top_freq_calc(int(freq)))
    least=(s.least_freq_calc(int(freq)))
    print()
    print("Top %d used words are :" %int(freq),end=" ")
    print(top)
    print()
    print("Least %d used words are :" %int(freq),end=" ")
    print(least)

if __name__=="__main__":
    main()
