
"This program will suggest a pricing range for knit orders, based on pattern difficulty, size, and time estimated"

import time

print("Welcome to the Knit Price Calculator! " )

time.sleep(1.5)

print("Please answer the following questions about your knit order to get a price suggestion.")

time.sleep(2)

starting_rate = 400
work_amount = 0
sizes = ["XXS", "XS", "S", "M", "L", "XL"]
genders = ["male", "female", "baby"]
garments = ["Sweater", "Poncho", "T-shirt", "Singlet", "Scarf", "Hat", "Mittens"]
structure_difficulties = ["simple", "medium", "complex"]
colorwork_difficulties = ["simple", "medium", "complex"]
cable_difficulties = ["simple", "medium", "complex"]

material_cost = int(input("What is the total material cost: "))
gauge = int(input("What is the gauge (stitches per 10 cm): "))

cables = input("Are there cables? (Yes/No): ").lower() == "yes"
if cables:
    cable_difficulty = input("Are the cables simple, medium, or complex? (simple/medium/complex): ").lower()
    work_amount += [1.2, 2.5, 3.5][cable_difficulties.index(cable_difficulty)]

structure = input("Are there any significant texture/structural decorations? (Yes/No): ").lower() == "yes"
if structure:
    structure_difficulty = input("Is the structure simple, medium, or complex? (If the garment is mostly ribbing, select complex): ").lower()
    work_amount += [1, 1.5, 2.5][structure_difficulties.index(structure_difficulty)]

colorwork = input("Is there colorwork? (Yes/No): ").lower() == "yes"
if colorwork:
    colorwork_difficulty = input("Is the colorwork simple, medium, or complex? (simple/medium/complex): ").lower()
    work_amount += [1.2, 1.5, 2.5][colorwork_difficulties.index(colorwork_difficulty)]
    color_amount = int(input("How many colors are used? "))
    if color_amount > 2:
        work_amount += color_amount - 2


garment = input("Type of garment (Sweater, Poncho, T-shirt, Singlet, Scarf, Hat, Mittens): ").capitalize()
if garment not in ["Scarf", "Hat", "Mittens"]:
    gender = input("Is it for a male, female, or a baby?: ").lower()
    size = input("Size (XXS, XS, S, M, L, XL): ").upper()
    work_amount += [0.10, 0.15, 0.20, 0.35, 0.50, 0.60][sizes.index(size)]
    work_amount += [1.7, 1.3, -0.4][genders.index(gender)]
if garment in ["Scarf", "Hat", "Mittens"]:
    starting_rate = 300
if garment == "Scarf":
    scarf_length = int(input("Length of the scarf in cm: "))
    work_amount += scarf_length / 50 * (gauge/10)*0.3


work_amount += [1.8, 1.4, 1.2, 1.1, 0.8, 0.5, 1.5][garments.index(garment)]
gauge_time = gauge / 100 *(gauge/5)
work_amount += gauge_time

price = starting_rate * (1 + work_amount)
price_tot = material_cost + price

print(f'The time spent will be approximately {work_amount - 0.5:.0f} to {work_amount + 1:.0f} weeks')
time.sleep(1)
print(f'Your total price is {round(price_tot, -1)}kr, including the labor fee of {round(price, -1)}kr. The minimum fee is {starting_rate}kr.')
time.sleep(1)
print(f'This amounts to {round(price/price_tot*100, 2)}% of the total price. Around {round(price/work_amount, -1)}kr per week of knitting.')