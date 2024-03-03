starting_numbers = input().split()
number_of_removes = int(input())
end_numbers = [int(nums) for nums in starting_numbers]

# remove min int in for cycle of (number_of_removes)
for number in range(number_of_removes):
    end_numbers.remove(min(end_numbers))

end_numbers = [str(nums) for nums in end_numbers]
print(", ".join(end_numbers))