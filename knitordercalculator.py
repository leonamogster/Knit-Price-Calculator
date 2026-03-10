import streamlit as st

st.set_page_config(page_title="Knit Price Calculator", page_icon="🧶", layout="centered")

st.title("🧶 Knit Price Calculator")
st.write("This app suggests a pricing range for knit orders based on pattern difficulty, size, and estimated time.")

starting_rate = 400
work_amount = 0

sizes = ["XXS", "XS", "S", "M", "L", "XL"]
genders = ["male", "female", "baby"]
garments = ["Sweater", "Poncho", "T-shirt", "Singlet", "Scarf", "Hat", "Mittens"]
structure_difficulties = ["simple", "medium", "complex"]
colorwork_difficulties = ["simple", "medium", "complex"]
cable_difficulties = ["simple", "medium", "complex"]

with st.form("knit_price_form"):
    material_cost = st.number_input("Total material cost (kr)", min_value=0, step=50)
    gauge = st.number_input("Gauge (stitches per 10 cm)", min_value=1, step=1)

    cables = st.checkbox("Are there cables?")
    cable_difficulty = None
    if cables:
        cable_difficulty = st.selectbox(
            "Cable difficulty",
            cable_difficulties
        )

    structure = st.checkbox("Are there any significant texture/structural decorations?")
    structure_difficulty = None
    if structure:
        structure_difficulty = st.selectbox(
            "Structure difficulty",
            structure_difficulties,
            help="If the garment is mostly ribbing, select complex."
        )

    colorwork = st.checkbox("Is there colorwork?")
    colorwork_difficulty = None
    color_amount = 0
    if colorwork:
        colorwork_difficulty = st.selectbox(
            "Colorwork difficulty",
            colorwork_difficulties
        )
        color_amount = st.number_input("How many colors are used?", min_value=1, step=1)

    garment = st.selectbox("Type of garment", garments)

    gender = None
    size = None
    scarf_length = 0

    if garment not in ["Scarf", "Hat", "Mittens"]:
        gender = st.selectbox("Who is it for?", genders)
        size = st.selectbox("Size", sizes)

    if garment == "Scarf":
        scarf_length = st.number_input("Length of the scarf (cm)", min_value=1, step=10)

    submitted = st.form_submit_button("Calculate price")

if submitted:
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
    total_price = material_cost + price

    st.subheader("Result")
    col1, col2, col3 = st.columns(3)

    col1.metric("Estimated work amount", f"{work_amount:.2f}")
    col2.metric("Labor fee", f"{round(price, -1):.0f} kr")
    col3.metric("Total price", f"{round(total_price, -1):.0f} kr")

    st.write(
        f"**Estimated time spent:** approximately {work_amount - 0.5:.0f} to {work_amount + 1:.0f} weeks"
    )
    st.write(
        f"**Minimum fee:** {current_starting_rate} kr"
    )
    st.write(
        f"**Labor share of total price:** {round(price / total_price * 100, 2)}%"
    )
    st.write(
        f"**Approximate pay per week of knitting:** {round(price / work_amount, -1):.0f} kr"
    )

    with st.expander("Show calculation details"):
        st.write(f"Garment: {garment}")
        st.write(f"Gauge contribution: {gauge_time:.2f}")

        if cables:
            st.write(f"Cables ({cable_difficulty}): {[1.2, 2.5, 3.5][cable_difficulties.index(cable_difficulty)]}")

        if structure:
            st.write(f"Structure ({structure_difficulty}): {[1, 1.5, 2.5][structure_difficulties.index(structure_difficulty)]}")

        if colorwork:
            st.write(f"Colorwork ({colorwork_difficulty}): {[1.2, 1.5, 2.5][colorwork_difficulties.index(colorwork_difficulty)]}")
            if color_amount > 2:
                st.write(f"Extra colors: {color_amount - 2}")

        if garment not in ["Scarf", "Hat", "Mittens"]:
            st.write(f"Size ({size}): {[0.10, 0.15, 0.20, 0.35, 0.50, 0.60][sizes.index(size)]}")
            st.write(f"Recipient ({gender}): {[1.7, 1.3, -0.4][genders.index(gender)]}")

        if garment == "Scarf":
            scarf_bonus = scarf_length / 50 * (gauge / 10) * 0.3
            st.write(f"Scarf length contribution: {scarf_bonus:.2f}")

        st.write(f"Garment base: {[1.8, 1.4, 1.2, 1.1, 0.8, 0.5, 1.5][garments.index(garment)]}")


