# Convert a full name to snake case. For Eg: str = "Zaheen Malik", output -> "zaheen_malik".
# First Method
def convert_snake_case(txt):
    s = txt.lower()
    return s.replace(' ', '_')


result = convert_snake_case("Zaheen Malik")
print(result)


# Second Method
def convert_snake_case(txt):
    return txt.lower().replace(' ', '_')


print(convert_snake_case("Zaheen Malik"))
