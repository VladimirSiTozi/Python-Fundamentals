import re


def regex_test(regex, string):

    match = re.search(regex, string)

    if match:
        print('Match found:', match.group())
    else:
        print('No match found')


regex_test('\\bworld\\b', "Hello world!")
regex_test('\\d', '12345')
regex_test('\\d+', '12345')
regex_test('\\d+', '1234gosho5')