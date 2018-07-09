# string methods
# --------------
# isalpha()
'hello'.isalpha()       # True
'hello world'.isalpha() # False

# isalnum()
'k9'.isalnum()          # True
'k-9'.isalnum()         # False

# isdecimal()
# (contains only numeric characters)
'1'.isdecimal()         # True
'1.1'.isdecimal()       # False

# isspace()
' '.isspace()           # True
'\t'.isspace()          # True
'\n'.isspace()          # True
'hello world'.isspace() # False

# startswith()
'hello world'.startswith('hello') # True
'hello world'.startswith('world') # False

# endswith()
'hello world'.endswith('hello') # False
'hello world'.endswith('world') # True

rjust()
ljust()
center()
