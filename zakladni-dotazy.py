import pandas

#----------------------Jmena 2 -----------------------------------#
jmena = pandas.read_csv("jmena.csv")
# Vypiš všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
print(jmena[jmena["věk"] > 60])
# Vypiš pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
print(jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)])
# Vypiš jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
vybrana_jmena = jmena[jmena["původ"].isin(["slovanský","hebrejský"])]
print(vybrana_jmena["četnost"])
# Vypiš všechna jména, která mají svátek první 3 dny v prosinci.
jmena_prosinec = jmena[jmena["svátek"].isin(["1.12","2.12","3.12"])]
print(jmena_prosinec.shape)
print(jmena_prosinec)
