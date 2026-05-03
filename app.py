import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Elixir Analytical Lab", page_icon="🧪", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🧪 Elixir Analytical Lab")
st.sidebar.subheader("Select Lab Category:")

category = st.sidebar.selectbox(
    "Category",
    ("1. Redox Titrations", "2. Electrochemistry", "3. Complexometric Titrations")
)

# --- 1. Redox Titrations ---
if category == "1. Redox Titrations":
    st.header("🔄 Redox Titrations")
    experiment = st.radio("Select Experiment:", ("Hydrogen Peroxide Assay", "Determination of Ferrous Salts"))
    
    if experiment == "Hydrogen Peroxide Assay":
        st.subheader("💧 Assay of Hydrogen Peroxide (H2O2)")
        st.write("Calculates % w/v and Volume Strength based on 0.1N KMnO4 titration.")
        
        ep_vol = st.number_input("Enter End Point Volume (ml of KMnO4):", min_value=0.0, step=0.1)
        dilution_factor = st.number_input("Enter Dilution Factor (e.g., 250/2 = 125):", value=125.0, step=1.0)
        
        if st.button("Calculate H2O2 Strength"):
            # Equivalent: 1 ml of 0.1N KMnO4 = 0.001702 g H2O2
            eq_wt = 0.001702
            sample_vol = 10.0 # From the 10ml pipetted volume
            
            percent_wv = (ep_vol * eq_wt * dilution_factor * 100) / sample_vol
            vol_strength = percent_wv * 3.292 # 329.2 / 100
            
            st.success(f"**Concentration (% w/v):** {percent_wv:.4f} %")
            st.info(f"**Volume Strength:** {vol_strength:.4f} ml O2")
            
    elif experiment == "Determination of Ferrous Salts":
        st.subheader("🔗 Determination of Ferrous Salts")
        st.write("Using 0.1N Potassium Dichromate (K2Cr2O7).")
        
        ep_vol = st.number_input("Enter End Point Volume (ml of K2Cr2O7):", min_value=0.0, step=0.1)
        sample_vol = st.number_input("Sample Volume taken (ml):", value=10.0, step=1.0)
        
        if st.button("Calculate Fe2+ %"):
            # Equivalent: 1 ml 0.1N K2Cr2O7 = 0.0278 g FeSO4.7H2O
            percent_ferrous = (ep_vol * 0.0278 * 100) / sample_vol
            st.success(f"**Ferrous (% w/v):** {percent_ferrous:.4f} %")

# --- 2. Electrochemistry ---
elif category == "2. Electrochemistry":
    st.header("⚡ Electrochemical Analysis")
    experiment = st.radio("Select Method:", ("Conductometric Titration", "Potentiometric Titration"))
    
    if experiment == "Conductometric Titration":
        st.subheader("📈 Conductometric Titration Curve")
        st.write("Plot conductance vs. volume of titrant to find the equivalence point.")
        
        col1, col2 = st.columns(2)
        with col1:
            vol_input = st.text_input("Enter Volumes (ml) separated by commas:", "0, 1, 2, 3, 4, 5, 6, 7")
        with col2:
            cond_input = st.text_input("Enter Conductance separated by commas:", "100, 80, 60, 45, 55, 75, 95, 115")
            
        if st.button("Plot Conductogram"):
            try:
                v_list = [float(i.strip()) for i in vol_input.split(",")]
                c_list = [float(i.strip()) for i in cond_input.split(",")]
                
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.plot(v_list, c_list, marker='s', linestyle='-', color='purple', label='Conductance')
                ax.set_title("Conductometric Titration Curve", fontsize=14, fontweight='bold')
                ax.set_xlabel("Volume of Titrant (ml)", fontsize=12)
                ax.set_ylabel("Conductance", fontsize=12)
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.legend()
                
                st.pyplot(fig)
                st.caption("The equivalence point is located at the minimum conductance value (for Strong Acid/Strong Base).")
            except:
                st.error("Invalid input. Ensure numbers are separated by commas.")

    elif experiment == "Potentiometric Titration":
        st.subheader("🔋 Potentiometric Titration Curve")
        st.write("Plot Potential (mV) vs. Volume (ml) to locate the steep jump.")
        
        col1, col2 = st.columns(2)
        with col1:
            vol_input = st.text_input("Enter Volumes (ml) separated by commas:", "0, 10, 20, 24, 24.5, 25, 25.5, 26, 30")
        with col2:
            pot_input = st.text_input("Enter Potential (mV) separated by commas:", "100, 120, 150, 200, 300, 700, 800, 820, 850")
            
        if st.button("Plot Potentiogram"):
            try:
                v_list = [float(i.strip()) for i in vol_input.split(",")]
                p_list = [float(i.strip()) for i in pot_input.split(",")]
                
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.plot(v_list, p_list, marker='o', linestyle='-', color='teal', label='Potential (mV)')
                ax.set_title("Potentiometric Titration Curve", fontsize=14, fontweight='bold')
                ax.set_xlabel("Volume of Titrant (ml)", fontsize=12)
                ax.set_ylabel("Potential (mV)", fontsize=12)
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.legend()
                
                st.pyplot(fig)
                st.caption("The equivalence point corresponds to the steepest portion of the curve.")
            except:
                st.error("Invalid input. Ensure numbers are separated by commas.")

# --- 3. Complexometric Titrations ---
elif category == "3. Complexometric Titrations":
    st.header("🔗 Complexometric Titrations (EDTA)")
    experiment = st.radio("Select Assay:", ("Direct Titration of Zinc Sulfate", "Determination of Total Ca & Mg"))
    
    if experiment == "Direct Titration of Zinc Sulfate":
        st.subheader("🛡️ Assay of Zinc Sulfate (ZnSO4)")
        st.write("Direct titration using 0.05M EDTA at pH 10 or pH 5.")
        
        ep_vol = st.number_input("Enter End Point Volume (ml of 0.05M EDTA):", min_value=0.0, step=0.1)
        sample_vol = st.number_input("Sample Volume taken (ml):", value=10.0, step=1.0)
        
        if st.button("Calculate ZnSO4 %"):
            # Equivalent: 1 ml 0.05M EDTA = 0.01438 g ZnSO4.7H2O
            percent_zn = (ep_vol * 0.01438 * 100) / sample_vol
            st.success(f"**Zinc Sulfate (% w/v):** {percent_zn:.4f} %")
            
    elif experiment == "Determination of Total Ca & Mg":
        st.subheader("🥛 Total Calcium & Magnesium")
        st.write("Direct titration with 0.05M EDTA at pH 10 using Erio-T.")
        
        ep_vol = st.number_input("Enter End Point Volume (ml of 0.05M EDTA):", min_value=0.0, step=0.1)
        
        if st.button("Calculate Equivalents"):
            st.info(f"**Calcium Equivalent:** {(ep_vol * 0.002):.4f} g Ca2+")
            st.info(f"**Magnesium Equivalent:** {(ep_vol * 0.001):.4f} g Mg2+")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Developed by Elixir Initiative for Sohag University Clinical Pharmacy</p>", unsafe_allow_html=True)


