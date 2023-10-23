import pandas

# Načti data do DataFrame, který si pojmenuj titanic.
titanic = pandas.read_csv("titanic.csv")
# Nech si zobrazit názvy sloupců, které jsou v souboru uloženy.
print(titanic.columns)
print(titanic.info())
# Podívej se, kolik má soubor řádků.
print(titanic.shape)
# Zjisti, jaký byl průměrný věk pasažérů.
print(titanic.info())
print(titanic["Age"].info())
# Kolik bylo nejstaršímu pasažérovi?
print(titanic["Age"].info())