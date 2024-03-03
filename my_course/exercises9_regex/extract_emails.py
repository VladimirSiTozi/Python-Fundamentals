import re


def matching(line):
    pattern = r"\s(([a-z0-9]+[a-z0-9\.\_\-]*)@([a-z\-]+)(\.[a-z]+)+)\b"
    match = re.findall(pattern, line)
    return match


line_sentence = input()
result = matching(line_sentence)
for email in result:
    print(email[0])

# input
# Please contact us at: support@github.com.
#
# Just send email to s.miller@mit.edu and j.hopking@york.ac.uk
# for more information.
#
# Many users @ SoftUni confuse email addresses. We @
# Softuni.BG provide high-quality training @ home or @ class.
# –- steve.parker@softuni.de.
