import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Eco-Forest Valuation",
    page_icon="🌳",
    layout="wide"
)

# =========================
# CSS FULL DASHBOARD STYLE
# =========================
st.markdown("""
<style>

/* background utama */
.block-container {
    padding: 2rem 3rem;
}

/* judul */
h1, h2, h3 {
    text-align: center;
    color: #1b5e20;
}

/* card style */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* metric box */
.metric-box {
    background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    color: #1b5e20;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

/* sidebar */
[data-testid="stSidebar"] {
    background-color: #f5f7f6;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER INSTANSI (STYLE KPH)
# =========================
st.markdown("""
# 🌳 ECO-FOREST VALUATION SYSTEM
### Aplikasi Pembelajaran Ekonomi Sumber Daya Hutan

---

## UNIVERSITAS ISLAM BANDUNG  
Fakultas Ekonomi dan Bisnis  
Program Studi Ekonomi Pembangunan  

**Tugas Kelompok: Ekonomi Sumber Daya Hutan (TEV - Tietenberg & Lewis)**
""")

st.divider()

# =========================
# SIDEBAR NAVIGATION
# =========================
menu = st.sidebar.radio(
    "📌 NAVIGASI SISTEM",
    [
        "🏠 Dashboard Utama",
        "📘 Teori Ekosistem",
        "💰 Modul TEV",
        "⚖️ Trade-off Analysis",
        "🌿 PES System",
        "🌳 Studi Kasus"
    ]
)

# =========================
# HOME DASHBOARD
# =========================
if menu == "🏠 Dashboard Utama":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="metric-box">🌳 Hutan Tropis Indonesia</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-box">💰 TEV Framework</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-box">🌿 Ekonomi Lingkungan</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>📌 Deskripsi Sistem</h3>
    Aplikasi ini digunakan untuk menganalisis nilai ekonomi hutan berdasarkan konsep 
    <b>Total Economic Value (TEV)</b>, trade-off pemanfaatan, dan kebijakan PES.
    </div>
    """, unsafe_allow_html=True)

# =========================
# TEORI
# =========================
elif menu == "📘 Teori Ekosistem":

    st.markdown("""
    <div class="card">
    <h3>🌿 Klasifikasi Jasa Lingkungan</h3>

    <b>Provisioning</b> → Kayu, air, hasil hutan<br>
    <b>Regulating</b> → Karbon, iklim, udara bersih<br>
    <b>Cultural</b> → Wisata, spiritual, estetika<br>
    <b>Supporting</b> → Nutrisi tanah, fotosintesis
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>📊 Komposisi TEV Hutan Tropis</h3>

    Regulating: 45%  
    Provisioning: 25%  
    Cultural: 20%  
    Supporting: 10%  

    👉 Nilai terbesar berasal dari fungsi ekologis, bukan kayu.
    </div>
    """, unsafe_allow_html=True)

# =========================
# TEV CALCULATOR
# =========================
elif menu == "💰 Modul TEV":

    st.subheader("💰 Kalkulator Total Economic Value")

    p = st.number_input("Provisioning Value", 0)
    r = st.number_input("Regulating Value", 0)
    c = st.number_input("Cultural Value", 0)
    s = st.number_input("Supporting Value", 0)

    total = p + r + c + s

    st.markdown(f"""
    <div class="metric-box">
    TOTAL TEV = Rp {total:,.0f}
    </div>
    """, unsafe_allow_html=True)

# =========================
# TRADE OFF
# =========================
elif menu == "⚖️ Trade-off Analysis":

    st.subheader("⚖️ Analisis Pemanfaatan Hutan")

    exploit = st.slider("Eksploitasi Hutan (%)", 0, 100, 40)
    conserve = 100 - exploit

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f'<div class="metric-box">Eksploitasi<br>{exploit}%</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div class="metric-box">Konservasi<br>{conserve}%</div>', unsafe_allow_html=True)

    if exploit > 60:
        st.error("⚠️ Risiko deforestasi tinggi!")
    else:
        st.success("✔ Pemanfaatan masih berkelanjutan")

# =========================
# PES SYSTEM
# =========================
elif menu == "🌿 PES System":

    st.subheader("🌿 Payment for Ecosystem Services")

    st.markdown("""
    <div class="card">
    PES adalah mekanisme pembayaran untuk menjaga jasa lingkungan hutan.
    Contoh: pemerintah membayar masyarakat untuk menjaga hutan tetap lestari.
    </div>
    """, unsafe_allow_html=True)

    dana = st.number_input("Dana PES (Rp)", 0)

    if dana > 1000000:
        st.success("✔ Program PES efektif")
    else:
        st.warning("⚠ Dana masih rendah")

# =========================
# CASE STUDY
# =========================
elif menu == "🌳 Studi Kasus":

    st.subheader("🌳 Studi Kasus Hutan Tropis")

    opsi = st.selectbox(
        "Pilih Kebijakan",
        ["Eksploitasi Kayu", "Konservasi Total", "Eco Tourism"]
    )

    if opsi == "Eksploitasi Kayu":
        st.error("Keuntungan cepat, kerusakan tinggi")
    elif opsi == "Konservasi Total":
        st.success("Lingkungan terjaga, ekonomi rendah")
    else:
        st.info("Keseimbangan ekonomi & lingkungan optimal")
