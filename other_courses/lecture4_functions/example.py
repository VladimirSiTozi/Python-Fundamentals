def function_name(first_name):
    print(f"Hello, {first_name}")

name = (input("Enter your name:"))

function_name("vlado1")
function_name("Nora")
function_name(input("Enter your family name:"))

for i in range(1, 6):
    function_name(i)

for i in range(1, 6):
    function_name(input("Enter 5 names:"))

