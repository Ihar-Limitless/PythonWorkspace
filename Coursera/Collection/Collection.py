class Pet:
    def __init__(self, name, tooth):
        self.name = name
        self.tooth = tooth

pet_collect=dict()
for i in range(5):
    pn = input()
    pt = input()
    pet = Pet(pn, pt)
    pet_collect[pet.name]=pet.tooth

for key, value in pet_collect.items():
    print(f' у {key} - {value} зуба')


