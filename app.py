import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="BL 6 - Eco Forest Valuation",
    page_icon="🌳",
    layout="wide"
)

# =========================
# CSS DASHBOARD STYLE
# =========================
st.markdown("""
<style>

.block-container {
    padding: 2rem 3rem;
}

h1, h2, h3 {
    text-align: center;
    color: #1b5e20;
}

.card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.metric-box {
    background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    color: #1b5e20;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

[data-testid="stSidebar"] {
    background-color: #f5f7f6;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
# 🌳 BL 6 — Eco-Forest Valuation System  
## Babakan Siliwangi (Urban Forest Bandung)

---

### Mata Kuliah  
Ekonomi Sumber Daya Alam dan Lingkungan  

### Dosen Pengampu  
Yuhka Sundaya, S.E., M.Si.

---

## KELOMPOK 4  
- Salsa Zahratul Aulia (10090224004)  
- Aida Farida Kultsum (10090224014)  
- Nabil Athala Naufal (10090224022)  
""")

st.divider()

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "📌 NAVIGASI",
    [
        "🏠 Dashboard Utama",
        "🌳 Profil Hutan",
        "🪵 Produksi",
        "📊 Master Data",
        "📈 Dashboard",
        "⚙️ Simulasi TEV"
    ]
)

# =========================
# DASHBOARD UTAMA (KPI STYLE)
# =========================
if menu == "🏠 Dashboard Utama":

    st.markdown("## 📊 Dashboard Ringkasan")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-box">
        🌳 Profil Hutan<br><br>
        <h2>19</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-box">
        🪵 Produksi<br><br>
        <h2>12</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-box">
        📊 Master Data<br><br>
        <h2>28</h2>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-box">
        📈 Dashboard<br><br>
        <h2>6</h2>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <div class="card">
    <h3>📌 Deskripsi Aplikasi</h3>

    Aplikasi ini digunakan untuk analisis ekonomi sumber daya hutan pada kawasan 
    <b>Babakan Siliwangi (Urban Forest Bandung)</b>.

    <br><br>
    Fitur utama:
    <ul>
        <li>Profil Hutan</li>
        <li>Produksi / Aktivitas Ekosistem</li>
        <li>Master Data Lingkungan</li>
        <li>Simulasi TEV</li>
        <li>Dashboard Summary</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PROFIL HUTAN
# =========================
elif menu == "🌳 Profil Hutan":

    st.markdown("""
    <div class="card">
    <h3>🌳 Babakan Siliwangi</h3>

    Urban Forest Kota Bandung yang berfungsi sebagai:
    <br><br>
    • Paru-paru kota  
    • Ruang terbuka hijau  
    • Wisata alam  
    • Penyerap karbon  
    • Edukasi lingkungan  
    </div>
    """, unsafe_allow_html=True)

# =========================
# PRODUKSI
# =========================
elif menu == "🪵 Produksi":

    st.markdown("""
    <div class="card">
    <h3>🪵 Aktivitas Ekosistem</h3>

    Dalam hutan kota, produksi tidak berupa kayu, tetapi:
    <br>
    • Jumlah pengunjung  
    • Aktivitas wisata  
    • Pemanfaatan ruang publik  
    </div>
    """, unsafe_allow_html=True)

    st.info("Data bersifat estimasi berbasis aktivitas urban forest")

# =========================
# MASTER DATA
# =========================
elif menu == "📊 Master Data":

    st.markdown("""
    <div class="card">
    <h3>📊 Klasifikasi Jasa Lingkungan</h3>

    • Provisioning: udara bersih, air tanah  
    • Regulating: karbon, suhu  
    • Cultural: wisata & estetika  
    • Supporting: biodiversitas  
    </div>
    """, unsafe_allow_html=True)

# =========================
# DASHBOARD
# =========================
elif menu == "📈 Dashboard":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🌿 Ekosistem Stabil")

    with col2:
        st.success("💰 Nilai Ekonomi Tinggi")

    with col3:
        st.success("🌳 Fungsi Lingkungan Aktif")

# =========================
# SIMULASI TEV
# =========================
elif menu == "⚙️ Simulasi TEV":

    st.subheader("💰 Total Economic Value (TEV)")

    p = st.number_input("Provisioning", 0)
    r = st.number_input("Regulating", 0)
    c = st.number_input("Cultural", 0)
    s = st.number_input("Supporting", 0)

    total = p + r + c + s

    st.markdown(f"""
    <div class="metric-box">
    TOTAL TEV<br><br>
    Rp {total:,.0f}
    </div>
    """, unsafe_allow_html=True)
