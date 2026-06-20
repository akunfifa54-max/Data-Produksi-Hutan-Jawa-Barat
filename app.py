import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

# ==========================================
# CONFIG & THEME REFRESH
# ==========================================
st.set_page_config(
    page_title="Babakan Siliwangi A+ Dashboard",
    page_icon="🌳",
    layout="wide"
)

# Kustomisasi CSS untuk UI modern (Warna Alam Bandung)
st.markdown("""
<style>
    .block-container { padding: 2.5rem 5rem; background-color: #fcfdfe; }
    h1, h2, h3 { font-family: 'Inter', sans-serif; color: #1b5e20; }
    .banner {
        background: linear-gradient(135deg, #1b5e20, #2e7d32);
        color: white; padding: 30px; border-radius: 16px; margin-bottom: 30px;
    }
    .metric-card {
        background: white; border: 1px solid #e0e0e0; border-radius: 14px;
        padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .metric-title { font-size: 14px; color: #666; text-transform: uppercase; }
    .metric-value { font-size: 32px; font-weight: 700; color: #2e7d32; margin-top: 5px; }
    .info-card {
        background-color: #f1f8e9; border-left: 5px solid #4caf50;
        padding: 20px; border-radius: 4px 12px 12px 4px; margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/616/616561.png", width=70)
st.sidebar.markdown("### **Navigasi Sistem**")
menu = st.sidebar.radio(
    "Pilih Menu Analisis:",
    ["🏠 Beranda & Profil", "🗺️ Pemetaan Spasial", "💰 Pemodelan TEV", "📊 Tren & Ekonomi"],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.markdown("### 🔧 Asumsi Harga Jasa")
harga_tiket = st.sidebar.slider("Tarif WTP / Orang", 5000, 25000, 10000, 1000)
harga_karbon = st.sidebar.slider("Nilai Karbon / Ton (Rp)", 50000, 200000, 150000, 10000)

# ==========================================
# SIMULASI DATA
# ==========================================
df_ekonomi = pd.DataFrame({
    "Tahun": [2021, 2022, 2023, 2024, 2025],
    "Pengunjung (Jiwa)": [11000, 14500, 16000, 18500, 22000],
    "Serapan Karbon (Ton)": [83, 88, 92, 95, 98],
    "Keanekaragaman Hayati (Spesies)": [24, 25, 28, 28, 31]
})

# ==========================================
# MODULE 1: BERANDA & PROFIL
# ==========================================
if menu == "🏠 Beranda & Profil":
    st.markdown("""
    <div class="banner">
        <h1 style="color: white; margin:0; font-size: 32px;">🌳 BABAKAN SILIWANGI A+ DASHBOARD</h1>
        <p style="margin: 5px 0 15px 0; font-size: 18px; opacity: 0.9;">Analisis Valuasi Ekonomi & Sistem Ekologi Hutan Kota Bandung</p>
        <hr style="border-color: rgba(255,255,255,0.2);">
        <p style="margin:0; font-size: 14px;"><strong>UNIVERSITAS ISLAM BANDUNG</strong> · Ekonomi Sumber Daya Alam dan Lingkungan</p>
        <p style="margin:0; font-size: 13px; opacity: 0.8;">Kelompok 2: Dadang, Anggota 2, Anggota 3, Anggota 4</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">📐 Luas Area</div>
            <div class="metric-value">3.8 Ha</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">🫁 Oksigen / Hari</div>
            <div class="metric-value">14.2 Kg</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">👥 Tren WTP</div>
            <div class="metric-value">↗️ Naik</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">🛡️ Status Hukum</div>
            <div class="metric-value">Hutan Kota</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h4>📌 Pengantar Studi Kasus</h4>
        <p><b>Babakan Siliwangi (Baksil)</b> merupakan kawasan hutan kota penopang ekologi penting di Kota Bandung. 
        Sebagai sistem ekonomi-ekologi perkotaan, Baksil menghasilkan berbagai bentuk manfaat tidak berwujud (<i>intangible benefits</i>) 
        seperti pengatur iklim mikro, tata air, dan ruang edukasi-rekreasi budaya.</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 2: PEMETAAN SPASIAL
# ==========================================
elif menu == "🗺️ Pemetaan Spasial":
    st.subheader("📍 Geospasial & Batas Zona Ekologis")
    
    map_data = pd.DataFrame({
        "lat": [-6.8895], "lon": [107.6107], "nama": ["Babakan Siliwangi"]
    })

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/outdoors-v11",
        initial_view_state=pdk.ViewState(latitude=-6.8895, longitude=107.6107, zoom=15.5, pitch=45),
        layers=[
            pdk.Layer("ScatterplotLayer", data=map_data, get_position='[lon, lat]', get_color='[46, 125, 50, 180]', get_radius=120)
        ],
    ))

# ==========================================
# MODULE 3: PEMODELAN TEV
# ==========================================
elif menu == "💰 Pemodelan TEV":
    st.subheader("📈 Simulasi Perhitungan Total Economic Value (TEV)")

    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.markdown("### **1. Nilai Guna Langsung**")
        p = st.slider("Asumsi Pengunjung / Tahun", 5000, 30000, 18000, step=1000)
        direct_use = p * harga_tiket
        st.caption(f"Estimasi Nilai Rekreasi: Rp {direct_use:,.0f}")
        
        st.markdown("### **2. Nilai Guna Tidak Langsung**")
        r = st.slider("Volume Penyerapan Karbon (Ton/Thn)", 50, 150, 95, step=5)
        indirect_use = r * harga_karbon
        st.caption(f"Estimasi Regulasi Udara: Rp {indirect_use:,.0f}")

    with col_right:
        st.markdown("### **3. Nilai Non-Use**")
        c = st.slider("Nilai Pendidikan (Rp Juta/Thn)", 10, 100, 45) * 1000000
        s = st.slider("Nilai Keanekaragaman Hayati (Rp Juta/Thn)", 10, 100, 35) * 1000000
        non_use = c + s

    tev_total = direct_use + indirect_use + non_use

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #efebe9, #d7ccc8); padding: 25px; border-radius: 14px; text-align: center; margin-top:25px;">
        <span style="color:#5d4037; font-weight: bold; font-size:14px;">HASIL VALUASI EKONOMI TOTAL (TEV)</span>
        <h1 style="color: #4e342e; margin: 10px 0 0 0; font-size:42px;">Rp {tev_total:,.0f} <span style="font-size:18px;">/ Tahun</span></h1>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 4: TREN & GRAFIK EKONOMI
# ==========================================
elif menu == "📊 Tren & Ekonomi":
    st.subheader("📉 Analisis Tren Multi-Tahun Jasa Lingkungan")
    
    tab1, tab2 = st.tabs(["👥 Grafik Analisis", "📋 Dataset Mentah"])
    
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            fig1 = px.line(df_ekonomi, x="Tahun", y="Pengunjung (Jiwa)", title="Pertumbuhan Minat Kunjungan (WTP)", markers=True, color_discrete_sequence=['#2e7d32'])
            fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig1, use_container_width=True)
            
        with c2:
            fig2 = px.bar(df_ekonomi, x="Tahun", y="Serapan Karbon (Ton)", title="Kapasitas Sekuestrasi Karbon Hutan Kota", color_discrete_sequence=['#81c784'])
            fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig2, use_container_width=True)
            
    with tab2:
        st.dataframe(df_ekonomi, use_container_width=True)

    st.markdown("""
    <div style="background: white; padding: 18px; border-radius: 14px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-top: 4px solid #1b5e20;">
        💡 <b>Interpretasi Ekonomis:</b> Trend peningkatan pengunjung mengindikasikan surplus konsumen yang membesar, sedangkan kenaikan kapasitas karbon menunjukkan penguatan ketahanan ekologis lingkungan kota (Carbon Sink).
    </div>
    """, unsafe_allow_html=True)
