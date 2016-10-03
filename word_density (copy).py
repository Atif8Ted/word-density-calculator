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

    #forms density dictionary based on frequency of usage
    def form_density_dictionary(self,word_file,fp_exclude):
        self.freq_dictionary={}
        try:
            with open(fp_exclude,'r')as fp2:
                words_excluded=fp2.read().split() #words to be excluded stored in a list
                print("**Read file successfully :" + fp_exclude + "**")
                words_excluded=[words.lower() for words in words_excluded] # converted to lowercase

        except IOError:
            print("**Could not read file:", fp_exclude, " :Please check file name**")
            sys.exit()

        try:
            with open(word_file,'r') as file:
                print("**Read file successfully :" + word_file + "**")
                words_list=file.read()
                if not words_list:
                    print("**No data in file:",word_file +":**")
                    sys.exit()
                words_list=words_list.split()
                words_list=[words.lower() for words in words_list] # lowercasing entire list
            unique_words=list((set(words_list)-set(words_excluded)))

            for word in unique_words:
                self.freq_dictionary[word] = ("%6.2f"%(float((words_list.count(word))/len(words_list))*100)) #frequency calculation
            '''self.freq_dictionary= {word:("%6.2f"%(float((words_list.count(word))/len(words_list))*100))  for word in unique_words}'''
            print((len(self.freq_dictionary)))
        except IOError:
            print("**Could not read file:", word_file, " :Please check file name**")
            sys.exit()


    #functions for top n most frequent words
    def top_freq(self,top_freq):
        return(sorted(self.freq_dictionary.items(), reverse=True,key=lambda x:x[1]))[:top_freq]

    #functions for least n used words
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
