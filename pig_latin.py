#Program to print sentences in the pig latin language
#By Lalelani Eddie Nene
#29 April 



def constant(word):
    index = 0 
    while (word[index] not in ["a","e","i","o","u"]):
        index = index + 1
        
        
    return word[index:] + "a" +word[0:index] + "ay"

def vowel(word):
    return word + "way"

def main():
    text = input("Enter a sentence:\n")
    splitText = text.split(" ")
    pigLatinText = ""
    for word in splitText:
        if (word[0] in ["a","e","i","o","u"]):
            pigLatinText += vowel(word) + " "
            
        else:
            pigLatinText +=constant(word) + " "
    print(pigLatinText[:-1].lower())
    
if  __name__=="__main__":
    main()
