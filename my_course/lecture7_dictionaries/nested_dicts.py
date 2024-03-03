c

print(students)
print(f"Gosho - {students['Gosho']}")
print(f"Gosho - Math - {students['Gosho']['Math']}")
students['Gosho']['Math'] += 1
print(f"Gosho - Math - {students['Gosho']['Math']}")