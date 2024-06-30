s: str = 'JAIST'
print(s[0])
print(s[1])

try:
    print(s[5])
except IndexError as e:
    print(e)

s1: str = 'Japan'
s2: str = 'Advanced'
s3: str = 'Institute'
s4: str = 'of'
s5: str = 'Science'
s6: str = 'and'
s7: str = 'Technology'
print(f'{s1} {s2} {s3} {s4} {s5} {s6} {s7}')
