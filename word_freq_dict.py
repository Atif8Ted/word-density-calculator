#!/usr/bin/python3
'''
Created on 19-Aug-2016

@author: atif

'''

import sys

'''class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg'''
        

        
def word_density(word_file,fp_exclude,top_freq): # word_file is for the file containing all the words , fp_exlude is for file containing words to be excluded
    unique_words=[] # list for containing unique words
    with open(fp_exclude,'r')as fp2:   
        words_excluded=fp2.read().split() #words to be excluded stored in a list
    with open(word_file,'r') as file:
        words_list=file.read().split() #All the words from main word file stored in word_list
        for word in words_list: #Adding all the unique word to list
            if word not in unique_words and word not in words_excluded:
                unique_words+=[word]
        freq_dictionary={}
        for word in unique_words:
            freq_dictionary[word] = ("%6.2f"%(float((words_list.count(word))/len(words_list))*100)) #calculating frequency of the words
    return(sorted(freq_dictionary.items(), reverse=True,key=lambda x:x[1]))[:top_freq] # returning top n items based on word density



if __name__=="__main__":
    user_args=sys.argv[1:]
    try:
        word_file,exclude_file,top_freq=user_args
    except ValueError:        
        print("Needed 3 arguments , supplied  %d" %len(user_args))
        print("Usage: python3 word_freq_dict.py word_file exclude_file 10")
        sys.exit()
            
    #main(sys.argv[1:])
    
    
    
    top_freq_words=word_density(word_file,exclude_file,int(top_freq))
    print(top_freq_words)
            
            
            
        

            
#word_density("word_file")           
