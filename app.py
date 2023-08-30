
import streamlit as st
from constants import COSTS, COMMERCIAL_TERMS
from calculations import calculate_cost

# Title
st.title("House Renovation Quote Generator")

# User details
st.subheader("User Details")
name = st.text_input("Name:")
email = st.text_input("Email:")

# Select services
st.subheader("Select Services")
selected_services = st.multiselect(
    "Choose the services you need:",
    options=list(COSTS.keys())
)

# Input for painting area if PAINT is selected
area = 0
if 'PAINT' in selected_services:
    area = st.number_input("Enter the area to be painted (in sq. meters):", min_value=0)

# Generate quote button
if st.button("Generate Quote"):
    total_cost = calculate_cost(selected_services, area)
    st.subheader(f"Total Cost: ${total_cost:.2f}")
    st.write(COMMERCIAL_TERMS)

# Footer
st.write("Thank you for considering our services!")
