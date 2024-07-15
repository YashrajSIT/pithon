#defining a function frequency to count the frequncy of the word
def frequency(str):
    words=str.split()
    print(words)
    words_freq={}
    for word in words:
        if word in words_freq:
            words_freq[word]+=1
        else:
            words_freq[word]=1
    print(words_freq)
#taking input of a string
str=input("enter the string=")
#calling a function named frequency
frequency(str)
