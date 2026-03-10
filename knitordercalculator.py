import streamlit as st

st.set_page_config(page_title="Knit Price Calculator", page_icon="🧶")

st.title("Welcome to the Knit Price Calculator!")
st.write("Please answer the following questions about your knit order to get a price suggestion.")

starting_rate = 400
work_amount = 0

sizes = ["XXS", "XS", "S", "M", "L", "XL"]
genders = ["male", "female", "baby"]
garments = ["Sweater", "Poncho", "T-shirt", "Singlet", "Scarf", "Hat", "Mittens"]
structure_difficulties = ["simple", "medium", "complex"]
colorwork_difficulties = ["simple", "medium", "complex"]
cable_difficulties = ["simple", "medium", "complex"]

material_cost = st.number_input("What is the total material cost:", min_value=0, step=50)
gauge = st.number_input("What is the gauge (stitches per 10 cm):", min_value=1, step=1)

cables = st.selectbox("Are there cables?", ["No", "Yes"]) == "Yes"
if cables:
    cable_difficulty = st.selectbox(
        "Are the cables simple, medium, or complex?",
        cable_difficulties
    )

structure = st.selectbox(
    "Are there any significant texture/structural decorations?",
    ["No", "Yes"]
) == "Yes"
if structure:
    structure_difficulty = st.selectbox(
        "Is the structure simple, medium, or complex? (If the garment is mostly ribbing, select complex):",
        structure_difficulties
    )

colorwork = st.selectbox("Is there colorwork?", ["No", "Yes"]) == "Yes"
if colorwork:
    colorwork_difficulty = st.selectbox(
        "Is the colorwork simple, medium, or complex?",
        colorwork_difficulties
    )
    color_amount = st.number_input("How many colors are used?", min_value=1, step=1)

garment = st.selectbox(
    "Type of garment",
    garments
)

if garment not in ["Scarf", "Hat", "Mittens"]:
    gender = st.selectbox("Is it for a male, female, or a baby?", genders)
    size = st.selectbox("Size", sizes)

if garment == "Scarf":
    scarf_length = st.number_input("Length of the scarf in cm:", min_value=1, step=10)

if st.button("Calculate price"):
    work_amount = 0
    current_starting_rate = starting_rate

    if cables:
        work_amount += [1.2, 2.5, 3.5][cable_difficulties.index(cable_difficulty)]

    if structure:
        work_amount += [1, 1.5, 2.5][structure_difficulties.index(structure_difficulty)]

    if colorwork:
        work_amount += [1.2, 1.5, 2.5][colorwork_difficulties.index(colorwork_difficulty)]
        if color_amount > 2:
            work_amount += color_amount - 2

    if garment not in ["Scarf", "Hat", "Mittens"]:
        work_amount += [0.10, 0.15, 0.20, 0.35, 0.50, 0.60][sizes.index(size)]
        work_amount += [1.7, 1.3, -0.4][genders.index(gender)]

    if garment in ["Scarf", "Hat", "Mittens"]:
        current_starting_rate = 300

    if garment == "Scarf":
        work_amount += scarf_length / 50 * (gauge / 10) * 0.3

    work_amount += [1.8, 1.4, 1.2, 1.1, 0.8, 0.5, 1.5][garments.index(garment)]

    gauge_time = gauge / 100 * (gauge / 5)
    work_amount += gauge_time

    price = current_starting_rate * (1 + work_amount)
    price_tot = material_cost + price

    st.success(
        f"The time spent will be approximately {work_amount - 0.5:.0f} to {work_amount + 1:.0f} weeks"
    )
    st.info(
        f"Your total price is {round(price_tot, -1)}kr, including the labor fee of {round(price, -1)}kr. "
        f"The minimum fee is {current_starting_rate}kr."
    )
    st.write(
        f"This amounts to {round(price / price_tot * 100, 2)}% of the total price. "
        f"Around {round(price / work_amount, -1)}kr per week of knitting."
    )
