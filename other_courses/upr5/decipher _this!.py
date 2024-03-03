def decipher_the_word(words):
    for word in words_decipher:
        for num in word:
            if num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                lst_nums.append(num)

            else:
                words_lst.append(num)

        letter_from_ascii = "".join(lst_nums)
        letter_from_ascii = chr(int(letter_from_ascii))
        words_lst.insert(0, letter_from_ascii)
        words_lst[1], words_lst[-1] = words_lst[-1], words_lst[1]
        final_word = "".join(words_lst)
        words_ready_to_display.append(final_word)
        lst_nums.clear()
        words_lst.clear()


words_decipher = input().split()
words_lst = []
lst_nums = []
words_ready_to_display = []

decipher_the_word(words_decipher)

print(" ".join(words_ready_to_display))

# test input
# 72olle 103doo 100ya
#
# 82yade 115te 103o
