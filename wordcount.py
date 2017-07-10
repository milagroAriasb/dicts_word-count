# put your code here.

poem_file = open("test.txt")

def poem(poem_file):
 
    for line in poem_file:
        line = line.rstrip()
        word = line.split(" ")
       
        print word
    
    poem_file.close()
 



def word_count(words):
    word_count_in_poem = {}

    for word in words:
        word_count_in_poem [word] = word_count_in_poem.get(word,0) + 1

    return word_count_in_poem

    


poem(poem_file)