import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Beam Deflection Calculator")

# Inputs
L = st.number_input("Length of Beam (m)", value=2.0)
P = st.number_input("Load (N)", value=1000.0)
E = st.number_input("Young's Modulus (Pa)", value=2e11)
I = st.number_input("Moment of Inertia (m^4)", value=1e-6)

# Calculation (Cantilever Beam)
x = np.linspace(0, L, 100)
y = (P * x**2) / (6 * E * I) * (3*L - x)

# Plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Deflection Curve")
ax.set_xlabel("Length (m)")
ax.set_ylabel("Deflection (m)")

st.pyplot(fig)
