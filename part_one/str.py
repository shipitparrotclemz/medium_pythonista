parrot_name: str = "boban"
print(parrot_name)

parrot_name = parrot_name + " boba"
parrot_name += " bobanana"
print(parrot_name)

"""
Traceback (most recent call last):
  File ".../medium/the_pythonista/part_one/str.py", line 8, in <module>
    parrot_name -= " boba bobanana"
TypeError: unsupported operand type(s) for -=: 'str' and 'str'

We can't use - or -= with strings
"""
# parrot_name -= " boba bobanana"

parrot_first_name: str = parrot_name[0:5]
print(parrot_first_name)