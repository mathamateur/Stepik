def update_dictionary(d, key, value):
    a = []
    a.append(value)
    if key in d:
        d[key] += a
    elif 2*key in d:
        d[2*key] += a
    else:
        d[key*2] = a
d = {}
update_dictionary(d,1,-1)
update_dictionary(d,2,-2)
update_dictionary(d,1,-3)
print()