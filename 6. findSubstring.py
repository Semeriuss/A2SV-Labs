#Takes a small string and looks for its permutation in a big string
def findSubString(small, big):

    #return if passed argument is reversed
    if len(small) > len(big):
        return -1

    #Create list of chars from small string
    #Create hashmap with key of chars from small string
    #and initial value of zero
    small_list = [char for char in small]
    small_dict = {char: 0 for char in small}

    #Create a copy of uninitialized hashmap
    compare_dict = small_dict.copy()

    #Update original hashmap value based on the list
    for char in small_list:
        if char in small_dict:
            small_dict[char] += 1

    #If char in big not in dict
    #or if len of leftover string slice 
    #is less than the starting indexer
    #reinitialize dict and counter 
    count = i = 0
    while(i < len(big)):
        if (big[i] not in compare_dict) or (i-count > len(big)-len(small)):
            i += 1
            count = 0
            compare_dict = {char: 0 for char in small}
            continue

        if big[i] in compare_dict:
            compare_dict[big[i]] += 1
            i += 1
            count += 1

        #check if loop traversed len small times
        #print result if substring found
        #reinitialize dict and len counter
        #left shift indexer to next string slice
        if count == len(small):
            if compare_dict == small_dict:
                print(f'From Index {i-count} to {i}')
            compare_dict = {char: 0 for char in small}
            i -= count-1
            count = 0
        
        
            
            

    
small = "abbc"
big = "abcbdbbcabadccbba"

s = "an"
b = """
A cognition is a bit of knowledge or belief. When it disagrees with another cognition in our head, theorized Prof. Leon Festinger of Stanford a half century ago, a nasty jangling occurs. To end this cognitive dissonance, or C.D., we change the weak cognition to conform to the stronger one.
Take Aesop's fox, who could not reach a lofty bunch of grapes no matter how high he jumped. One foxy cognition was that grapes were delicious; the other was that he couldn't get them. To resolve that cognitive dissonance, the fox persuaded himself that the grapes were sour -- and trotted off, his mind at ease.
"""

findSubString(s, b)
##findSubString(small, big)

