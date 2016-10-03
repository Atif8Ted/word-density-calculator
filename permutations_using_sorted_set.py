'''
Created on 18-Aug-2016

@author: atif
'''
def permutations(word):
    '''
    Return perm
    '''
    if (len(word)==1):
        return [word]
    else:
        #get all permutations of length N-1
        perms=permutations(word[1:])
        char=word[0]
        result=[]
        #iterate over all permutations of length N-1
        for perm in perms:
            #insert the character into every possible location
            for i in range(len(perm)+1):
                result.append(perm[:i] + char + perm[i:])
        return type((result))

print(permutations("Atif"))

'''if __name__=='__main__':
    string=input("Enter the string: ")
    unique_permutations=sorted(set(permutations(string)))
    print(unique_permutations)
    '''


