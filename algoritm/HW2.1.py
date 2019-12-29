def main(my_greeting):
    longest_word = ''
    longest_size = 0
    for word in my_greeting.split():
        if len(word) > longest_size:
            longest_size = len(word)
            longest_word = word
    return longest_word

# remove spaces
my_gift = "  Wellcom to     Portland    "
new_my_gift = ''.join(my_gift).split()
concatenate = ' '.join(new_my_gift)


#def unite_gift(*args):
   # new_string = []
    #for arg in args:
        #new_string += arg
    #return new_string

def unite_gift(s):
    new_string = ""
    for arg in s:
        new_string += arg
    return new_string


if __name__ == "__main__":
    print(main(my_greeting="Oleg_Morozov is the best men"))
    print(new_my_gift)
    #print(unite_gift(new_my_gift))
    print(concatenate)
