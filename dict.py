# creating a dictonary
new_dict = {"trouble":"problem",
            "python":"computer language",
            "update":"a new change"
            }

# if input founds
try:
    # taking inputs from the user
    print("From now onwards give only the below mention words\n 1. trouble\n 2. python \n 3. update ")
    inp1 = input("word:")

    # making non-case sensitive
    lowerinput = inp1.lower()

    # giving output to user
    for keys in new_dict:
        resultskeys = keys.find(lowerinput)
        if resultskeys != -1:
            print(keys + " meaning is " + new_dict[keys])

# if input not founds
except:
    print("No found")