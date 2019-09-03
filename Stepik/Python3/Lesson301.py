d = {}
def update_dictionary(d, key, value):
    if(key in d):
        d[key] = d[key]+[value]
    elif(key not in d  and 2*key not in d):
        d[2*key] = [value]
    elif(key not in d  and 2*key in d):
        d[2*key] = d[2*key]+[value]
print(update_dictionary(d, 1, -1))  # None
print(d)
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)