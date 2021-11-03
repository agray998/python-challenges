# These challenges are intended to provide practice in basic python skills such as string manipulation, iteration, use of collection types and conditionals

# Challenge 1: Write a function which:
# - Takes a string as an argument
# - returns the string in all upper case if its' length is even, and all lower case if its' length is odd. Any non-alphabetic characters should not be changed
# - stretch goal: try to implement this both with and without the .upper()/.lower() methods

def func_1_methods(string):
    if len(string) % 2 == 0:
        return string.upper()
    else:
        return string.lower()

def func_1_no_methods(string):
    upper_case_dict = {
        "A":"a",
        "B":"b",
        "C":"c",
        "D":"d",
        "E":"e",
        "F":"f",
        "G":"g",
        "H":"h",
        "I":"i",
        "J":"j",
        "K":"k",
        "L":"l",
        "M":"m",
        "N":"n",
        "O":"o",
        "P":"p",
        "Q":"q",
        "R":"r",
        "S":"s",
        "T":"t",
        "U":"u",
        "V":"v",
        "W":"w",
        "X":"x",
        "Y":"y",
        "Z":"z"
    }
    lower_case_dict = {
        "a":"A",
        "b":"B",
        "c":"C",
        "d":"D",
        "e":"E",
        "f":"F",
        "g":"G",
        "h":"H",
        "i":"I",
        "j":"J",
        "k":"K",
        "l":"L",
        "m":"M",
        "n":"N",
        "o":"O",
        "p":"P",
        "q":"Q",
        "r":"R",
        "s":"S",
        "t":"T",
        "u":"U",
        "v":"V",
        "w":"W",
        "x":"X",
        "y":"Y",
        "z":"Z"
    }
    if len(string) % 2 == 0:
        return ''.join([lower_case_dict.get(char, char) for char in string])
    else:
        return ''.join([upper_case_dict.get(char, char) for char in string])

# Challenge 2: write a function which:
# - takes a word and a list of words as input
# - returns a new list containing only the words from the given list which differ from the given word in exactly one position
# You should ignore case

def func_2(string, list):
    newlist = []
    for word in list:
        if len(word) != len(string):
            continue
        else:
            diffs = 0
            for i in range(len(word)):
                if word.lower()[i] == string.lower()[i]:
                    continue
                else:
                    diffs += 1
            if diffs == 1:
                newlist.append(word)
            else:
                continue
    return newlist

# Challenge 3: write a function which:
# - takes two ints and a list of ints as arguments
# - returns a list of bools where the ith element is True if list[i] has the two given ints as factors and false otherwise

def func_3(int1, int2, intlist):
    return [(int % int1 == 0 and int % int2 == 0) for int in intlist]

# Challenge 4: write a function which:
# - takes a string as an argument
# - returns a new string containing only the letters from the original string which are at an even-numbered position in the alphabet (letting a = 1, b = 2, ...)
# - the returned string should only contain letter characters. All chars in the returned string should be lower case

def func_4(string):
    return ''.join([char for char in string.lower() if 97 <= ord(char) <= 122 and ord(char) % 2 == 0])

# Challenge 5: write a function which:
# - takes a list of integers as argument
# - for each int, creates a list of the factors of the number, including 1 but excluding the number itself
# - converts these lists to strings and writes them out to a csv file called factors.csv, each on a new line
# - Note: this function should be a void (i.e return nothing)

def func_5(list):
    factorlists = [','.join([str(num) for num in range(1, int) if int % num == 0]) for int in list]
    outfile = '\n'.join(factorlists)
    with open('factors.csv', 'w') as f:
        f.write(outfile)