import streamlit as st
import math

st.set_page_config(page_title="CPHEEO STP Design Tool", layout="wide")

st.title("CPHEEO Based STP Design Calculator")

st.sidebar.header("Input Para")

population = st.sidebar.number_input("Population", min_value=1, value=50000)
lpcd = st.sidebar.number_input("LPCD (120-150)", min_value=100, max_value=200, value=135)
peak_factor = st.sidebar.number_input("Peak Factor (2-3)", min_value=1.0, max_value=5.0, value=2.5)

if st.sidebar.button("Calculate STP Design"):

    # FLOW
    Q_avg = (population * lpcd) / 1000
    Q_peak = Q_avg * peak_factor

    # SCREEN
    Q_peak_m3s = Q_peak / 86400
    velocity = 0.8
    screen_area = Q_peak_m3s / velocity

    # GRIT
    detention_grit = 45
    grit_volume = Q_peak_m3s * detention_grit

    # PST
    detention_time = 2
    SOR_peak = 100
    weir_loading = 250

    V_pst = Q_avg * (detention_time / 24)
    A_pst = Q_peak / SOR_peak
    W_pst = math.sqrt(A_pst / 3)
    L_pst = 3 * W_pst
    weir_length = Q_peak / weir_loading

    # AERATION
    MLSS = 3000
    FM = 0.25
    BOD_after_pst = 175
    BOD_load = Q_avg * BOD_after_pst / 1000
    V_aeration = BOD_load / (FM * (MLSS/1000))

    # CLARIFIER
    SOR_clarifier = 25
    A_clarifier = Q_avg / SOR_clarifier
    D_clarifier = math.sqrt((4*A_clarifier)/math.pi)

    st.header("📊 Design Results")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Flow Details")
        st.write("Average Flow (m³/day):", round(Q_avg,2))
        st.write("Peak Flow (m³/day):", round(Q_peak,2))

        st.subheader("Primary Sedimentation Tank")
        st.write("Volume (m³):", round(V_pst,2))
        st.write("Length (m):", round(L_pst,2))
        st.write("Width (m):", round(W_pst,2))
        st.write("Weir Length (m):", round(weir_length,2))

    with col2:
        st.subheader("Screen & Grit")
        st.write("Screen Area (m²):", round(screen_area,3))
        st.write("Grit Volume (m³):", round(grit_volume,2))

        st.subheader("Biological Treatment")
        st.write("Aeration Volume (m³):", round(V_aeration,2))
        st.write("Clarifier Diameter (m):", round(D_clarifier,2))

    st.success("Design Completed Successfully ✅")
