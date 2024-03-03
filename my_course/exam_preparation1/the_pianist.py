def create_composer(number_of_pieces):
    composer_list = {}
    for n in range(n_number_of_pieces):
        piece, composer, key = input().split("|")
        composer_list[piece] = [composer, key]
    return composer_list


def modifying_data_function(composer_list):

    while True:
        command, *params = input().split('|')
        if command == 'Stop':
            return composer_list

        elif command == 'Add':
            piece, composer, key = params
            if piece in composer_list:
                print(f"{piece} is already in the collection!")
            else:
                composer_list[piece] = [composer, key]
                print(f"{piece} by {composer} in {key} added to the collection!")

        elif command == 'Remove':
            piece = params[0]
            if piece in composer_list:
                del composer_list[piece]
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

        elif command == 'ChangeKey':
            piece, new_key = params[0], params[1]
            if piece in composer_list:
                composer_list[piece][1] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")


def base_function(number_of_pieces):
    composer_dict = create_composer(number_of_pieces)
    modifying_dict = modifying_data_function(composer_dict)

    for piece, data in modifying_dict.items():
        composer, key = data[0], data[1]
        print(f"{piece} -> Composer: {composer}, Key: {key}")


n_number_of_pieces = int(input())
base_function(n_number_of_pieces)
