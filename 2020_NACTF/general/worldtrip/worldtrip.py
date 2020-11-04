# https://github.com/che0/countries
import countries
cc = countries.CountryChecker('TM_WORLD_BORDERS-0.3.shp')

f = open('enc.txt').read().splitlines()


for i in f:
    word = i.split(", ")
    try:
        cCode = cc.getCountry(countries.Point(float(word[0]), float(word[1]))).iso
        print(cCode)
    except:
        print(word)