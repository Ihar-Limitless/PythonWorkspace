str = input().split()
dict = {'mile':1609, 'yard':0.9144, 'foot':0.3048, 'inch':0.0254, 'km':1000, 'cm':0.01, 'mm':0.001, 'm':1.0}
x = float(str[0]) * dict[str[1]] / dict[str[3]]
print('{:.2e}'.format(x))
