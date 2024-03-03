def adding(current_command, my_books):
    title = current_command[1]
    if title not in my_books:
        my_books.insert(0, title)
    return my_books


def taking(current_command, my_books):
    title = current_command[1]
    if title in my_books:
        my_books.remove(title)
    return my_books


def swapping(current_command, my_books):
    title_one, title_two = current_command[1], current_command[2]
    if title_one in my_books and title_two in my_books:
        index_one = my_books.index(title_one)
        index_two = my_books.index(title_two)
        my_books[index_one], my_books[index_two] = my_books[index_two], my_books [index_one]
    return my_books


def inserting(current_command, my_books):
    title = current_command[1]
    if title not in my_books:
        my_books.append(title)
    return my_books

def checking(current_command, my_books):
    index = int(current_command[1])
    if 0 <= index <= len(my_books):
        title = my_books[index]
        print(title)



books = [book for book in input().split("&")]

while True:
    breaking_command = input()
    if breaking_command == "Done":
        break
    command = breaking_command.split(" | ")

    if command[0] == "Add Book":
        books = adding(command, books)

    elif command[0] == "Take Book":
        books = taking(command, books)

    elif command[0] == "Swap Books":
        books = swapping(command, books)

    elif command[0] == "Insert Book":
        books = inserting(command, books)

    elif command[0] == "Check Book":
        checking(command, books)

print(', '.join(books))