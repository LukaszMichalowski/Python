countries_information={}
countries_information["Polska"] = ("Warszawa", 40.43)
countries_information["Niemcy"] = ("Berlin", 32.43)
countries_information["Słowacja"] = ("Bratyslawa", 43.54)


def  show_country(country):
    country_information= countries_information.get(country)

    print()
    print(country)
    print("-------")
    print("Stolica:" + country_information[0])
    print("Liczba mieszkańców:" + str(country_information[1]))

for country in countries_information:
    print(country)

country=input("O jakim kraju chcesz wyświetlić informacje?")
show_country(country)