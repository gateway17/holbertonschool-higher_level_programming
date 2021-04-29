#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    my_list = dir(hidden_4)
    letter = "s"
    for word in my_list:
        if word[1] is not "_":
            print("{}".format(word))
