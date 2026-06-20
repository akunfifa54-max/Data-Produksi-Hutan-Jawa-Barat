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
# CSS STYLE
# =========================
st.markdown("""
<style>
h1, h2, h3 {
    text-align: center;
}

.block-container {
    padding-left: 2rem;
    padding-right: 2rem;
}

[data-testid="stSidebar"] {
    background-color: #f0f2f6;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
# 🌳 Eco-Forest Valuation  
### Aplikasi Pembelajaran Ekonomi Sumber Daya Hutan  
**Referensi: Tietenberg & Lewis (Chapter 13)**  

---

## UNIVERSITAS ISLAM BANDUNG  
Fakultas Ekonomi dan Bisnis | Ekonomi Pembangunan  

### Tugas Kelompok: Ekonomi Sumber Daya Hutan (Kalimantan Selatan)
""")

st.divider()

# =========================
# SIDEBAR MENU
# =========================
menu = st.sidebar.radio(
    "📚 PILIH MODUL PEMBELAJARAN",
    [
        "Halaman Utama & Teori",
        "Modul 1: Kalkulator TEV",
        "Modul 2: Analisis Trade-off",
        "Modul 3: Kebijakan PES",
        "Modul 4: Kasus Interaktif"
    ]
)

# =========================
# HOME / TEORI
# =========================
if menu == "Halaman Utama & Teori":

    st.subheader("📘 Teori Dasar Ekonomi Ekosistem Hutan")

    st.write("""
Ekonomi sumber daya hutan berfokus pada nilai total ekosistem yang disebut **Total Economic Value (TEV)**.
    """)

    st.markdown("### 📊 Klasifikasi Jasa Lingkungan")

    st.table({
        "Kategori": ["Provisioning", "Regulating", "Cultural", "Supporting"],
        "Definisi": [
            "Penyedia barang fisik langsung",
            "Pengatur proses alam",
            "Manfaat rekreasi & spiritual",
            "Proses dasar ekosistem"
        ],
        "Contoh": [
            "Kayu, air, hasil hutan",
            "Karbon, penyerbukan",
            "Ekowisata, estetika",
            "Siklus nutrisi"
        ],
        "Metode Valuasi": [
            "Market Price",
            "Replacement Cost",
            "Travel Cost / WTP",
            "Indirect Valuation"
        ]
    })

    st.markdown("""
---

### 📈 Komposisi TEV Hutan Tropis
- Regulating Services: **45%**
- Provisioning (Kayu): **25%**
- Cultural Services: **20%**
- Supporting Services: **10%**

👉 Menunjukkan bahwa nilai terbesar hutan bukan hanya kayu, tetapi fungsi ekologisnya.
""")

# =========================
# MODUL 1 TEV
# =========================
elif menu == "Modul 1: Kalkulator TEV":

    st.subheader("💰 Kalkulator Total Economic Value (TEV)")

    provisioning = st.number_input("Nilai Provisioning (Kayu)", 0)
    regulating = st.number_input("Nilai Regulating (Karbon)", 0)
    cultural = st.number_input("Nilai Cultural (Wisata)", 0)
    supporting = st.number_input("Nilai Supporting", 0)

    tev = provisioning + regulating + cultural + supporting

    st.success(f"Total Economic Value (TEV): Rp {tev:,.0f}")

# =========================
# MODUL 2 TRADE-OFF
# =========================
elif menu == "Modul 2: Analisis Trade-off":

    st.subheader("⚖️ Trade-off Pemanfaatan Hutan")

    kayu = st.slider("Intensitas Penebangan Kayu", 0, 100, 30)
    konservasi = 100 - kayu

    st.write("📊 Hasil Analisis:")
    st.write(f"- Eksploitasi Kayu: {kayu}%")
    st.write(f"- Konservasi: {konservasi}%")

    if kayu > 60:
        st.error("Risiko deforestasi tinggi!")
    else:
        st.success("Pemanfaatan masih berkelanjutan")

# =========================
# MODUL 3 PES
# =========================
elif menu == "Modul 3: Kebijakan PES":

    st.subheader("🌿 Payment for Ecosystem Services (PES)")

    st.write("""
PES adalah mekanisme pembayaran untuk menjaga jasa lingkungan.
    """)

    st.markdown("""
Contoh:
- Petani menjaga hutan → dibayar pemerintah
- Perusahaan karbon → membayar konservasi
    """)

    dana = st.number_input("Dana PES (Rp)", 0)

    if dana > 1000000:
        st.success("Program PES berjalan efektif")
    else:
        st.warning("Dana masih rendah untuk dampak signifikan")

# =========================
# MODUL 4 KASUS
# =========================
elif menu == "Modul 4: Kasus Interaktif":

    st.subheader("🌳 Studi Kasus: Hutan Tropis Kalimantan Selatan")

    opsi = st.selectbox(
        "Pilih Kebijakan",
        ["Eksploitasi Kayu", "Konservasi Total", "Eco-Tourism"]
    )

    if opsi == "Eksploitasi Kayu":
        st.error("Pendapatan tinggi jangka pendek, kerusakan lingkungan tinggi")
    elif opsi == "Konservasi Total":
        st.success("Lingkungan terjaga, pendapatan ekonomi rendah")
    else:
        st.info("Keseimbangan ekonomi dan lingkungan lebih optimal")
