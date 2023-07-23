def to_string(n, base):
    convert_string = '01'
    if n < base:
        return convert_string[n]
    else:
        return to_string(n//base, base) + convert_string[n%base]

print(to_string(11,2))


