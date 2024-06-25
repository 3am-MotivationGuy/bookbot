def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    words = file_contents.split()
    counts = count_chars(words)
    print(f"==== Start report on {path} ====")
    print(f"{len(words)} words were found in the document")
    listed_dict = listed(counts)
    newlist = sorted(listed_dict, reverse=True, key=lambda d: d["num"])
    for dict in newlist:
        char = dict["character"]
        num = dict["num"]
        print(f"The '{char}' character was used {num} times!")

    print("==== End of report ====")

        
        
#Counts the number of each character
def count_chars(words):
    total = {}
    for word in words:
        chars = {}
        for i in word.lower():
               if i not in chars:
                    chars[i] = word.count(i)


        for a in chars:
             if a not in total:
                  total[a] = chars[a]

             elif a in total:
                  total[a] = total[a] + chars[a]

    return total

#Turns the character dictionary into a list of dictionaries where each dictonary holds the character in the
#"character" keyword and the number in the "num" keyword    
def listed(dict):
    worded = []
    for chars in dict:
        char_dict = {}
        char_dict["character"] = chars
        char_dict["num"] = dict[chars]
        worded.append(char_dict)

    return worded




main()
