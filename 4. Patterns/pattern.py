# Pattern Questions

# Pattern1: Print a square.
string = ""
n = 5
for i in range(n):
    for j in range(n):
        string += ' * '
    string += '\n'
print(string)

# Pattern2: Print a left-Triangle
string = ""
n = 5
for i in range(n):
    for j in range(i+1):
        string += ' * '
    string += '\n'
print(string)

# Pattern3: Print a left-Triangle with numbers.
string = ""
n = 6
for i in range(1, n):
    for j in range(1, i+1):
        string += f" { j } "
    string += '\n'
print(string)

# Pattern4: Print a left-Triangle with same number in each row.
string = ""
n = 6
for i in range(1, n):
    for j in range(1, i+1):
        string += f" { i } "
    string += '\n'
print(string)

# Pattern5: Print a reverse left-Triangle.
string = ""
n = 6
for i in range(1, n):
    for j in range(i, n):
        string += ' * '
    string += '\n'
print(string)

# Pattern6: Print a reverse left-Triangle with numbers.
string = ""
n = 6
for i in range(1, n):
    for j in range(1, n+1-i):
        string += f' { j } '
    string += '\n'
print(string)

#pattern7: Print a triangle with stars.
string = ""
n = 5
for i in range(0, n):
    for j in range(0, n-i-1): #Adds space to string.
        string += " "
    for j in range (0, 2*i+1): #Adds star to string.
        string += "*"
    for j in range(0, n-i-1): #Adds space to string.
        string += " "
    string += '\n'
print(string)

#pattern8: Print a reverse triangle.
string = ""
n = 5
for i in range(0, n):
    for j in range(0, i): #Adds space to string.
        string += " "
    for j in range (0, 2*n -(2*i +1)): #Adds star to string.
        string += "*"
    for j in range(0, i): #Adds space to string.
        string += " "
    string += '\n'
print(string)

#pattern9: Print a normal and reverse triangle joined with each other.
string = ""
n = 5
for i in range(0, n):
    for j in range(0, i): #Adds space to string.
        string += " "
    for j in range (0, 2*n -(2*i +1)): #Adds star to string.
        string += "*"
    for j in range(0, i): #Adds space to string.
        string += " "
    string += '\n'
print(string)