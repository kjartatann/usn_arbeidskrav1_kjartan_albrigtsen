"""
Første oppgavekrav USN grunnleggende programmering i Python
Kjartan Albrigtsen
kjartis@hotmail.com
"""
#først setter jeg de variablene jeg har fått
insurance_electric = 5000 #kr per år
insurance_gas = 7500 #kr pr år
road_tax = 8.38 # kr per dag - norsk trafikkforsikringsavgift
power_electric = 0.2 # kWh per km med elbil
power_price = 2.00 # kr per kWh
cost_gas = 1.0 # kr pr km med bensinbil
toll_road_electric = 0.1 #kr per km med elbil
toll_road_gas = 0.3 #kr per km med bensinbil

#ber brukeren om input på hvor mye hen kjører per år
km_input = input("Hvor mange km planlegger du å kjøre hvert år?")
km = float(km_input)

#beregner kost som ikke er avhengig av kjøretøyet
road_tax_tot = road_tax * 365 #i skuddår vil dette bli 1 dag for lite, men jeg ser bort fra det i denne oppgaven

#beregner kost som gjelder for elbil
fuel_cost_el = power_electric * power_price * km
toll_road_el_tot = toll_road_electric * km

#beregner kost som gjelder for bensinbil
fuel_cost_gas = cost_gas * km
toll_road_gas_tot = toll_road_gas * km

#beregner totalkostnader
el_total_cost = insurance_electric + road_tax_tot + fuel_cost_el + toll_road_el_tot
gas_total_cost = insurance_gas + road_tax_tot + fuel_cost_gas + toll_road_gas_tot

#beregner differansen mellom kostnadene
cost_diff = gas_total_cost - el_total_cost


print ()
print (f"Under forutsetning av at du kjører {int(km)} km per år vil kostnadene være som vist nedenfor") #bruker int-funksjon for å unngå desimaltall
print ("Vi tar her ikke med kostnader til renter, verditap etc.")
print ("Svarene er avrundet til nærmeste heltall.")
print ()
print ("Oppsummering:")
print (f"Bensinbilen vil koste deg {int(gas_total_cost)} kr per år") #bruker int-funksjon for å unngå desimaltall
print (f"Elbilen vil koste deg {int(el_total_cost)} kr per år") #bruker int-funksjon for å unngå desimaltall
print ()

# skriver ut forskjellig tekst, avhengig av hvem som er dyrest
if cost_diff > 0:
    print(f"Bensinbilen er {int(cost_diff)} kr dyrere enn elbilen.")
elif cost_diff < 0:
    print(f"Elbilen er {int(-cost_diff)} kr dyrere enn bensinbilen.")
else:
    print("Kostnaden for å kjøre elbil og bensinbil er lik.")
