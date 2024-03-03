import re


def generate_products_function(n_line_of_products):
    pattern = r'(\@{1}\#{1,})([A-Z]{1}[A-Za-z0-9]{4,}[A-Z$])(\@{1}\#{1,})'
    for n in range(n_line_of_products):
        product = input()
        match = re.search(pattern, product)
        group_string = ''
        if match:
            match = match.group(2)
            for symbol in match:
                if symbol.isdigit():
                    group_string += symbol
            if not group_string:
                group_string = '00'
            print(f'Product group: {group_string}')
        group_string = ''

        if match == None:
            print("Invalid barcode")


n_line_of_products = int(input())
match_products = generate_products_function(n_line_of_products)
