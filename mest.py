import csv


class School:
    def __init__(self, Eits, Fellows):
        self.Eits = Eits
        self.Fellows = Fellows


class Eit(School):
    def __init__(self, ename, country, tech_funfact):
        self.ename = ename
        self.country = country
        self.tech_funfact = tech_funfact
        try:
            with open("eit2018.csv", "w") as csvInit:
                csvWriter = csv.writer(csvInit)
                headers = ['Name', 'Nationality', 'Funfact']
                csvWriter.writerow(headers)
        except:
            pass

    def getname(self):
        return self.ename
    
    def getnationality(self):
        return self.country

    def getfunfact(self):
        return self.tech_funfact

    def writeNametoCsv(self, name):
        with open("eit2018.csv", "a+") as csvFile:
            csvWriter = csv.writer(csvFile)
            dataRow = [name.ename, name.country, name.tech_funfact]
            csvWriter.writerow(dataRow)
            print("details exported to csv")


insert = input("please give a name: ")
country = input("please give nationality: ")
funfact = input("please indicate fun fact: ")

neit = Eit(ename=insert, country=country, tech_funfact=funfact)
eit_name = neit.getname()
eit_nation = neit.getnationality()
eit_funfact = neit.getfunfact()

neit.writeNametoCsv(Eit(ename=insert, country=country, tech_funfact=funfact))

print("{} comes from {} and loves {}".format(eit_name, eit_nation, eit_funfact))


class Fellow(School):
    fellow_hired = 0

    def __init__(self, ename, country, happiness_level=15):
        if Fellow.fellow_hired == 4:
            raise Exception("{} cannot be hired".format(ename))
        Fellow.fellow_hired += 1

        self.ename = ename
        self.country = country
        self.happiness_level = happiness_level

    def getfname(self):
        return self.ename

    def getfnationality(self):
        return self.country

    def is_eating(self):
        self.happiness_level += 1
        return self.happiness_level

    def is_teaching(self):
        self.happiness_level -= 1
        return self.happiness_level

    def __repr__(self):
        return "{} comes from {} and my happiness level is {}".format(self.ename, self.country, self.happiness_level)


class Person:
    
    def __init__(self, ename, country):
        self.ename = ename
        self.country = country


class Eit(Person):
    
    def __init__(self, ename, country, tech_funfact):
        super().__init__(ename, country)
        self.tech_funfact = tech_funfact


class fellow(Person):
    
    def __init__(self, ename, country, happiness_level):
        super().__init__(ename, country)
        self.happiness_level = happiness_level


with open("eit2018.csv", "r") as file_handler:
    country = ["Kenya", "Nigeria", "Ivory Coast", "South Africa", "Ghana", "Zimbambwe"]

    current = 0
    for detail in file_handler:
        if current == 0:
            current += 1
            continue
        neit = detail.split(',')
        if neit[1] in country:
            print(neit)
        else:
            raise ValueError("Wrong country")


fellow1 = Fellow('Andrew', 'USA')
fellow1.is_eating()
print(fellow1)

fellow2 = Fellow('Edem', 'Ghana')
fellow2.is_teaching()
print(fellow2)

fellow3 = Fellow('Simphiwe', 'South Africa')
print(fellow3)

fellow4 = Fellow('Kerry', 'USA')
print(fellow4)

fellow5 = Fellow('Miishe', 'USA')
print(fellow5)




    





