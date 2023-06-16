"""
Ismail Shaikh
CS 100 Section 015
HW 10 November 18, 2022
"""
#Problem 1
def initialLetterCount(wordlist):
    iLetter={}
    for word in wordlist:
        if word[0] in iLetter:
            iLetter[word[0]]+=1
        else:
            iLetter[word[0]]=1
    return iLetter
wordlist=["Hello","pine","Pie","Care","Birthday"]
print(initialLetterCount(wordlist))
#Problem 2
def initialLetters(wordlist):
    dict={}
    for word in wordlist:
        if word not in dict:
            dict[word[0]]= [word]
        else:
            dict[word[0]].append(word)
    return dict
wordlist=["Pine","list","school","Mine","Sign"]
print(initialLetters(wordlist))
#Problem 3
def shareOneLetter(wordList):
    oneL={}
    for word in wordList:
        lst=[]
        if word not in oneL:
            oneL[word]=lst
            for letter in word:
                for oneWord in wordList:
                    if letter in oneWord:
                        if oneWord not in lst:
                            lst.append(oneWord)
    return oneL
wordlist=["Line","Spine","signal","pine","burger","Pizza"]
print(shareOneLetter(wordlist))
