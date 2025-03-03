import streamlit as st
import math

# Initialize variables
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

st.title("Build a Skincare Smoothie")

# Order quantity input
#orderQty = int(st.number_input("Order Qty", min_value=0, step=1))

# Checkboxes to determine ingredient
a = 1 if st.checkbox("Protini Polypeptide Cream") else 0
b = 1 if st.checkbox("Lala Retro Whipped Cream") else 0
c = 1 if st.checkbox("O-Bloos Rosi Drops") else 0
d = 1 if st.checkbox("B-Goldi Bright Drops") else 0
e = 1 if st.checkbox("D-Bronzi Anti-Pollution Sunshine Drops") else 0
f = 1 if st.checkbox("B-Hydra Intensive Hydration Serum") else 0
g = 1 if st.checkbox("C-Firma Day Serum") else 0
h = 1 if st.checkbox("T.L.C. Framboos Glycolic Night Serum") else 0


sum = a + b + c + d + e + f + g + h

# Display results
if (sum > 3):
  st.header("Blending... ")

else:
  st.header("Add another ingredient!")
