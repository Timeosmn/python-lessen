planeet = "mars"

#we meten de zwaartekracht van een planeet in m/s^2

mars_gravitatieconstante = 3.7

gewicht_aarde = float(input("hoeveel weeg je op aarde (kg)? "))

#gewicht is massa * zwaartekracht

aarde_gravitatieconstante = 9.81

massa = gewicht_aarde / aarde_gravitatieconstante

nieuw_gewicht = massa * mars_gravitatieconstante

print("De persoon zou " + str(nieuw_gewicht,2) + " kg wegen op " + planeet + ".")