'''
Created on 19-Aug-2016

@author: atif
'''
def word_density(fp_include,fp_exclude):
    unique_words=[]
    with open(fp_exclude,'r')as fp2:
        words_excluded=fp2.read().split()
    with open(fp_include,'r') as file:
        words_list=file.read().split()
        #print(words_list)
        for word in words_list:
            if word not in unique_words and word not in words_excluded:
                unique_words+=[word]
        word_frequencies=[]
        for word in unique_words:
            word_frequencies+=[float((words_list.count(word))/len(words_list))*100]
        for i in range(len(unique_words)):
            
            density_list=(str(unique_words[i]) + ": " +str( "%6.2f"%(word_frequencies[i])))
            yield density_list
            
            
        
x=list(word_density("word_file","exclude_file"))
print(x)

            
#word_density("word_file")           