# Return the count of a given substring from a string how many times substrings “Emma” appears in the given string.
# Give str_x = “Emma is good developer. Emma is a writer”.

str_x = "Emma is good developer. Emma is a writer."
list1 = str_x.split()
count = 0
for i in list1:
    if i == "Emma":
        count += 1

print(count)
