'''
Created on 19-Aug-2016

@author: atif

'''
class spam:
    
    def word_density(self): # word_file is for the file containing all the words , fp_exlude is for file containing words to be excluded
        unique_words=[]
        self.freq_dictionary={}
        # list for containing unique words
        words_list=['Atif', 'Atif', 'git', 'git', 'linux', 'github', '.', '"', '"', ',', '}', 'repository', 'echo', 'init', 'push', 'pull', 'black', 'hole', 'theory', 'import', 'code', 'another', 'online', 'offline', 'initialize', 'add', 'origin', 'readme', ',', 'licence', ',', 'Imam', ',', 'Imam,', 'University', ',', 'Attendence', ',', 'Independence', 'day', ',', 'republic', 'day', 'Python', 'fun', '.', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'linux', 'linux', 'linux', 'linux', 'linux', 'repository', 'repository', 'repository', 'initialize', 'initialize', 'initialize', 'licence', 'licence', 'licence', 'licence', 'hole', 'theory', 'hole', 'theory', 'hole', 'theory', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'Atif', 'init', 'init', 'init', 'init', 'bash', 'bash', 'bash', 'bash', 'bash']
        words_excluded=['.', ',', 'is', 'was', ';', '"', "'", 'offline', 'black']   
        
        for word in words_list:#Adding all the unique word to list
            if word not in unique_words and word not in words_excluded:
                unique_words+=[word]
                #freq_dictionary={}
        for word in unique_words:
            self.freq_dictionary[word] = ("%6.2f"%(float((words_list.count(word))/len(words_list))*100)) #calculating frequency of the words
        # returning top n items based on word density
    def top_freq(self,top_freq):
        return(sorted(self.freq_dictionary.items(), reverse=True,key=lambda x:x[1]))[:top_freq]
    def least_freq(self,least_freq):
        return(sorted(self.freq_dictionary.items(), reverse=False,key=lambda x:x[1]))[:least_freq]
        
        



if __name__=="__main__":
    #top_freq_words=word_density(10)
    #print(top_freq_words)
    #print(words_list)
    s=spam()
    z=s.word_density()
    top=s.top_freq(10)
    least=s.least_freq(10)
    
    print(top)
    print(least)
    
    
            
            
            
        

            
#word_density("word_file")           