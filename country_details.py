from countryinfo import CountryInfo

country = CountryInfo(input("Enter name of Country: "))

print("Country Name:", country.name())
print("Capital:", country.capital())
print("Population:", country.population())
print("Area (in kilometers):", country.area())
print("Region:", country.region())
print("Subregion:", country.subregion())
print("Demonym:", country.demonym())
print("Currency:", country.currencies())
print("Language:", country.languages())
print("Borders:", country.borders())