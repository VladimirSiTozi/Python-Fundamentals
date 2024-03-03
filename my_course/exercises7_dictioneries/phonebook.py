phonebook = {}

while True:
    entry = input()

    if entry.isdigit():
        entry = int(entry)
        break

    contact, number = entry.split("-")
    phonebook[contact] = number

for _ in range(entry):
    contact_to_search = input()
    if contact_to_search in phonebook:
        print(f'{contact_to_search} -> {phonebook[contact_to_search]}')
    else:
        print(f'Contact {contact_to_search} does not exist.')
