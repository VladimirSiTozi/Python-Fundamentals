import re


def base_function(string, matched_polindroms):
    matched_words = matching_initial_input(string)
    matched_polindroms_list = checking_for_pair(matched_words, matched_polindroms)
    return matched_words


def matching_initial_input(string):
    pattern = r'(@|\#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})'
    match = re.findall(pattern, string)
    return match

def checking_for_pair(matched_words, matched_polindroms):
    for pair in matched_words:
        if pair[1] == pair[2][::-1]:
            matched_polindroms.append(f'{pair[1]} <=> {pair[2]}')
    return matched_polindroms


matched_polindroms_list = []
text_string = input()
words = base_function(text_string, matched_polindroms_list)

if not words:
    print("No word pairs found!")
else:
    print(f"{len(words)} word pairs found!")

if not matched_polindroms_list:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(matched_polindroms_list))


# @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r
#
# #po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@
#
# #lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#