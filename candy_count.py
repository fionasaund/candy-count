# candy_count.py
# Counts my Halloween candy.

name = "Fiona"
chocolate = 10
gummies = 6
lollipops = 9
given_away = 5
sour_worms = 6

total = chocolate + gummies + lollipops + sour_worms
left = total - given_away

print("Candy report for", name)
print("Total pieces:", total)
print("Pieces left after sharing:", left)