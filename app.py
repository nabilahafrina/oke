import streamlit as st
# ===== CSS CUSTOM STYLE =====
st.markdown("""
    <style>
        /* ===== BACKGROUND GAMBAR ===== */
        .stApp {
            background-image: url('https://pin.it/5lQrk5VD8');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
        }

        /* ===== LAPISAN TRANSPARAN AGAR TEKS TERBACA ===== */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.75); /* biru muda */
            z-index: -1;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# KONFIGURASI
# ---------------------
st.set_page_config(page_title="Web Risiko & Penanganan Bahan Kimia", layout="centered")

# ---------------------
# INISIALISASI SESSION
# ---------------------
if 'halaman' not in st.session_state:
    st.session_state.halaman = 1
if 'kuis_selesai' not in st.session_state:
    st.session_state.kuis_selesai = False
if 'jawaban_pg' not in st.session_state:
    st.session_state.jawaban_pg = {}
if 'jawaban_isian' not in st.session_state:
    st.session_state.jawaban_isian = {}
if 'nama' not in st.session_state:
    st.session_state.nama = ""
if 'nim' not in st.session_state:
    st.session_state.nim = ""

# ---------------------
# FUNGSI NAVIGASI
# ---------------------
def next():
    st.session_state.halaman += 1

def back():
    st.session_state.halaman -= 1

# ---------------------
# TAMPILAN MENU (SIDEBAR)
# ---------------------
with st.sidebar:
    st.markdown("## 🔀 Tampilan Menu ")
    if st.button("🏠 Beranda"):
        st.session_state.halaman = 1
        st.session_state.kuis_selesai = False
    if st.button("📘 Informasi Aplikasi"):
        st.session_state.halaman = 2
        st.session_state.kuis_selesai = False
    if st.button("📄 Daftar Senyawa"):
        st.session_state.halaman = 3
        st.session_state.kuis_selesai = False
    if st.button("📝 Kuis"):
        st.session_state.halaman = 4
        st.session_state.kuis_selesai = False

# ---------------------
# DAFTAR SENYAWA
# ---------------------
msds_data = {
    "Asam": {
        "HCl": {
            "nama": "Asam Klorida (HCl)",
            "bahaya": "Korosif kuat, menyebabkan luka bakar pada kulit dan mata.",
            "penanganan": "Gunakan sarung tangan tahan asam, pelindung mata, dan masker.",
            "penyimpanan": "Simpan dalam botol kaca/plastik tebal, jauh dari basa.",
            "p3k": "Jika terkena kulit, bilas dengan air selama 15 menit dan cari bantuan medis.",
            "link": "https://www.merckmillipore.com/Web-VE-Site/en_US/-/VEF/ShowDocument-File?ProductSKU=MDA_CHEM-109973&DocumentType=MSD&DocumentId=109973_SDS_ID_ID.PDF&DocumentUID=406631&Language=ID&Country=ID&Origin=null"
        },
        "H2SO4": {
            "nama": "Asam Sulfat (H2SO4)",
            "bahaya": "Sangat korosif, menghasilkan panas saat bereaksi dengan air.",
            "penanganan": "Tuangkan asam ke air (jangan sebaliknya), gunakan pelindung lengkap.",
            "penyimpanan": "Wadah tahan asam, jauh dari bahan organik dan air.",
            "p3k": "Bilas selama 20 menit, cari pertolongan medis.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/339741"
        },
        "CH3COOH": {
            "nama": "Asam Asetat (CH₃COOH)",
            "bahaya": "Iritasi dan bau menyengat",
            "penanganan": "Gunakan pelindung",
            "penyimpanan": "Tertutup rapat",
            "p3k": "Segera bilas",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/320099"
        },
        "HBr": {
            "nama": "Asam Bromida (HBr)",
            "bahaya": "Korosif dan beracun",
            "penanganan": "Gunakan goggles",
            "penyimpanan": "Botol kaca",
            "p3k": "Bilas air",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/207409"
        },
        "HI": {
            "nama": "Asam Iodida (HI)", 
            "bahaya": "Iritasi saluran napas", 
            "penanganan": "Gunakan masker", 
            "penyimpanan": "Tertutup dan sejuk", 
            "p3k": "Segera bilas", 
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/207430"
        },
        "HF": {
            "nama": "Asam Fluorida (HF)",
            "bahaya": "Sangat toksik, menyerang tulang",
            "penanganan": "Sarung tangan khusus",
            "penyimpanan": "Botol plastik khusus",
            "p3k": "Ke IGD segera",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/205228"
        },
        "H3PO4": {
            "nama": "Asam Fosfat (H₃PO₄)",
            "bahaya": "Iritasi kulit",
            "penanganan": "Gunakan APD",
            "penyimpanan": "Tempat tertutup",
            "p3k": "Bilas air",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/345245"
        },
        "H2CO3": {
            "nama": "Asam Karbonat (H₂CO₃)",
            "bahaya": "Lemah namun iritasi",
            "penanganan": "Pelindung standar",
            "penyimpanan": "Botol tertutup",
            "p3k": "Cuci air",
            "link": "#"
        },
        "H2C2O4": {
            "nama": "Asam Oksalat (H₂C₂O₄)",
            "bahaya": "Beracun",
            "penanganan": "Gunakan pelindung",
            "penyimpanan": "Tertutup rapat",
            "p3k": "Segera bilas",
            "link": "#"
        },
        "HClO4": {
            "nama": "Asam Perklorat (HClO₄)",
            "bahaya": "Sangat reaktif",
            "penanganan": "APD lengkap",
            "penyimpanan": "Botol tahan asam",
            "p3k": "Ke IGD",
            "link": "#"},
        "H2SeO4": {
            "nama": "Asam Selenat (H₂SeO₄)",
            "bahaya": "Toksik",
            "penanganan": "Masker dan goggles",
            "penyimpanan": "Jauh dari organik",
            "p3k": "Udara segar",
            "link": "#"
        },
        "HBO2": {
            "nama": "Asam Borat (HBO₂)",
            "bahaya": "Iritasi ringan",
            "penanganan": "Minimal",
            "penyimpanan": "Tutup rapat",
            "p3k": "Bilas air",
            "link": "#"
        },
        "C6H5COOH": {
            "nama": "Asam Benzoat",
            "bahaya": "Iritasi mata",
            "penanganan": "Pelindung standar",
            "penyimpanan": "Tertutup",
            "p3k": "Cuci air",
            "link": "#"
        },
        "HSO3Cl": {
            "nama": "Asam Sulfonat",
            "bahaya": "Korosif dan berasap",
            "penanganan": "Ventilasi baik",
            "penyimpanan": "Botol tahan asam",
            "p3k": "Segera bilas",
            "link": "#"
        },
        "H2S": {
            "nama": "Asam Sulfida (gas)",
            "bahaya": "Beracun, bau busuk",
            "penanganan": "Masker respirator",
            "penyimpanan": "Silinder",
            "p3k": "Ke udara segar", 
            "link": "#"
        },
        "CCl3COOH": {
            "nama": "Asam Trikloroasetat",
            "bahaya": "Toksik dan iritasi",
            "penanganan": "APD lengkap",
            "penyimpanan": "Jauh dari panas",
            "p3k": "Segera bilas",
            "link": "#"
        }
    },
    "Basa": {
        "NaOH": {
            "nama": "Natrium Hidroksida (NaOH)",
            "bahaya": "Korosif kuat, dapat menyebabkan luka bakar kimia pada kulit dan mata.",
            "penanganan": "Gunakan alat pelindung diri lengkap, termasuk sarung tangan dan goggles.",
            "penyimpanan": "Simpan dalam wadah tertutup rapat di tempat sejuk dan kering.",
            "p3k": "Bilas area terkena dengan banyak air selama minimal 15 menit.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/221465"
    },
        "KOH": {
            "nama": "Kalium Hidroksida (KOH)",
            "bahaya": "Korosif, menyebabkan iritasi kulit dan mata.",
            "penanganan": "Gunakan pelindung kimia dan hindari kontak langsung.",
            "penyimpanan": "Simpan di tempat sejuk dan tertutup rapat.",
            "p3k": "Segera bilas dengan air jika kontak.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/221473"
    },
        "Ca(OH)2": {
            "nama": "Kalsium Hidroksida (Ca(OH)₂)",
            "bahaya": "Iritasi kulit dan mata.",
            "penanganan": "Gunakan goggles dan sarung tangan.",
            "penyimpanan": "Disimpan dalam wadah tertutup.",
            "p3k": "Cuci area terkena dengan air mengalir.",
            "link": "#"
    },
        "Ba(OH)2": {
            "nama": "Barium Hidroksida",
            "bahaya": "Beracun dan korosif.",
            "penanganan": "Gunakan APD lengkap dan ventilasi baik.",
            "penyimpanan": "Jauhkan dari air dan kelembaban.",
            "p3k": "Segera hubungi layanan medis.",
            "link": "#"
    },
        "NH4OH": {
            "nama": "Amonium Hidroksida",
            "bahaya": "Menghasilkan uap menyengat yang iritatif.",
            "penanganan": "Gunakan ventilasi yang memadai dan pelindung pernapasan.",
            "penyimpanan": "Simpan dalam botol tertutup rapat.",
            "p3k": "Segera bawa ke udara segar.",
            "link": "#"
    },
        "LiOH": {
            "nama": "Litium Hidroksida",
            "bahaya": "Iritasi kuat pada kulit dan saluran pernapasan.",
            "penanganan": "Gunakan sarung tangan dan masker.",
            "penyimpanan": "Tempat kering dan tertutup rapat.",
            "p3k": "Cuci dengan air mengalir.",
            "link": "#"
    },
        "Mg(OH)2": {
            "nama": "Magnesium Hidroksida",
            "bahaya": "Iritasi ringan pada kulit dan mata.",
            "penanganan": "Penanganan minimal dengan APD dasar.",
            "penyimpanan": "Simpan di tempat kering dan tertutup.",
            "p3k": "Bilas dengan air bersih.",
            "link": "#"
    },
        "Sr(OH)2": {
            "nama": "Stronsium Hidroksida",
            "bahaya": "Korosif, dapat menyebabkan luka kimia.",
            "penanganan": "Gunakan pelindung kulit dan goggles.",
            "penyimpanan": "Simpan dalam wadah tertutup rapat.",
            "p3k": "Cuci dengan air bersih jika terkena.",
            "link": "#"
    },
        "Al(OH)3": {
            "nama": "Aluminium Hidroksida",
            "bahaya": "Iritasi ringan bila terhirup atau kontak langsung.",
            "penanganan": "Gunakan masker debu dan APD dasar.",
            "penyimpanan": "Simpan di tempat sejuk dan kering.",
            "p3k": "Bilas dengan air bersih.",
            "link": "#"
    },
        "Zn(OH)2": {
            "nama": "Seng Hidroksida",
            "bahaya": "Dapat mengiritasi mata dan kulit.",
            "penanganan": "Gunakan pelindung mata dan sarung tangan.",
            "penyimpanan": "Tutup rapat dan jauhkan dari kelembapan.",
            "p3k": "Cuci mata atau kulit dengan air mengalir.",
            "link": "#"
    },
        "Fe(OH)3": {
            "nama": "Besi(III) Hidroksida",
            "bahaya": "Iritasi ringan jika terhirup atau kontak.",
            "penanganan": "Gunakan masker debu dan APD standar.",
            "penyimpanan": "Botol tertutup dan kering.",
            "p3k": "Bilas dengan air jika kontak.",
            "link": "#"
    },
        "Cr(OH)3": {
            "nama": "Kromium(III) Hidroksida",
            "bahaya": "Korosif dan berpotensi toksik.",
            "penanganan": "Gunakan APD lengkap dan tangani di fume hood.",
            "penyimpanan": "Jauhkan dari bahan asam.",
            "p3k": "Dapatkan bantuan medis segera.",
            "link": "#"
    },
        "Ni(OH)2": {
            "nama": "Nikel(II) Hidroksida",
            "bahaya": "Iritasi saluran pernapasan dan kulit.",
            "penanganan": "Gunakan masker dan ventilasi cukup.",
            "penyimpanan": "Simpan dalam botol tertutup.",
            "p3k": "Pindahkan ke udara segar, konsultasikan medis.",
            "link": "#"
    },
        "Cu(OH)2": {
            "nama": "Tembaga(II) Hidroksida",
            "bahaya": "Iritasi kulit dan mata.",
            "penanganan": "Gunakan sarung tangan dan goggles.",
            "penyimpanan": "Tempat sejuk dan tertutup.",
            "p3k": "Cuci area terkena dengan air.",
            "link": "#"
    },
        "AgOH": {
            "nama": "Perak Hidroksida",
            "bahaya": "Tidak stabil, dapat terurai.",
            "penanganan": "Tangani dengan hati-hati dan minimalkan eksposur.",
            "penyimpanan": "Simpan dalam botol gelap dan sejuk.",
            "p3k": "Cuci dengan air jika kontak.",
            "link": "#"
    },
        "Pb(OH)2": {
            "nama": "Timbal(II) Hidroksida",
            "bahaya": "Toksik berat, terutama jika terhirup.",
            "penanganan": "Gunakan APD lengkap dan ventilasi baik.",
            "penyimpanan": "Tertutup rapat, kering, dan berlabel jelas.",
            "p3k": "Segera bawa ke IGD.",
            "link": "#"
    },
        "Sn(OH)2": {
            "nama": "Timah(II) Hidroksida",
            "bahaya": "Iritasi kulit dan mata.",
            "penanganan": "Gunakan pelindung dasar seperti sarung tangan.",
            "penyimpanan": "Tempat sejuk dan tertutup.",
            "p3k": "Bilas dengan air bersih.",
            "link": "#"
    },
        "Bi(OH)3": {
            "nama": "Bismut(III) Hidroksida",
            "bahaya": "Dapat mengiritasi mata.",
            "penanganan": "Gunakan goggles dan ventilasi cukup.",
            "penyimpanan": "Simpan di tempat kering dan tertutup.",
            "p3k": "Cuci mata atau kulit dengan air.",
            "link": "#"
    },
        "Be(OH)2": {
            "nama": "Berilium Hidroksida",
            "bahaya": "Sangat toksik dan karsinogenik.",
            "penanganan": "Gunakan APD lengkap dan ventilasi maksimal.",
            "penyimpanan": "Botol tertutup dan berlabel bahaya tinggi.",
            "p3k": "Segera ke IGD untuk penanganan darurat.",
            "link": "#"
    },
        "Co(OH)2": {
            "nama": "Kobalt(II) Hidroksida",
            "bahaya": "Iritasi dan berbahaya bila terhirup atau tertelan.",
            "penanganan": "Gunakan respirator dan sarung tangan.",
            "penyimpanan": "Wadah tertutup, jauh dari kelembaban.",
            "p3k": "Bawa ke udara segar, dapatkan bantuan medis.",
            "link": "#"
        }
    },
    "Gas Berbahaya": {
        "NH3": {
            "nama": "Amonia (NH₃)",
            "bahaya": "Gas beracun, menyengat, mengiritasi saluran napas.",
            "penanganan": "Gunakan pelindung pernapasan, pastikan ventilasi cukup.",
            "penyimpanan": "Tabung logam tertutup, jauh dari panas dan asam.",
            "p3k": "Segera bawa ke udara segar, cari bantuan medis.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/aldrich/338818"
        },
        "Cl2": {
            "nama": "Klorin (Cl₂)",
            "bahaya": "Gas kuning-hijau, sangat toksik.",
            "penanganan": "Gunakan respirator, goggles, pastikan ventilasi baik.",
            "penyimpanan": "Silinder baja, jauh dari panas dan bahan reduktor.",
            "p3k": "Evakuasi ke udara segar, beri oksigen bila perlu.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/401279"
        },
        "H2S": {
            "nama": "Hidrogen Sulfida (H₂S)",
            "bahaya": "Beracun, bau seperti telur busuk, dapat mematikan dalam konsentrasi tinggi.",
            "penanganan": "Gunakan ventilasi kuat dan detektor gas.",
            "penyimpanan": "Disimpan dalam silinder tekan khusus.",
            "p3k": "Segera pindahkan ke udara segar dan berikan oksigen.",
            "link": "#"
    },
        "CO": {
            "nama": "Karbon Monoksida (CO)",
            "bahaya": "Gas tak berwarna dan tak berbau, sangat beracun.",
            "penanganan": "Gunakan detektor CO dan sistem ventilasi baik.",
            "penyimpanan": "Simpan dalam silinder gas bertekanan.",
            "p3k": "Berikan oksigen 100% dan bawa ke layanan medis darurat.",
            "link": "#"
    },
        "NO2": {
            "nama": "Nitrogen Dioksida (NO₂)",
            "bahaya": "Iritasi paru-paru dan dapat menyebabkan edema paru.",
            "penanganan": "Gunakan respirator dan pastikan ventilasi ruangan memadai.",
            "penyimpanan": "Simpan dalam botol tahan gas bertekanan.",
            "p3k": "Bawa korban ke udara segar dan dapatkan bantuan medis segera.",
            "link": "#"
    },
        "SO2": {
            "nama": "Sulfur Dioksida (SO₂)",
            "bahaya": "Iritasi saluran pernapasan dan mata.",
            "penanganan": "Gunakan ventilasi baik dan alat pelindung diri.",
            "penyimpanan": "Simpan dalam silinder logam dengan label jelas.",
            "p3k": "Segera bawa ke udara segar, hubungi medis bila perlu.",
            "link": "#"
    },
        "F2": {
            "nama": "Fluorin (F₂)",
            "bahaya": "Sangat reaktif dan beracun, menyebabkan luka bakar kimia.",
            "penanganan": "Gunakan APD lengkap dan sistem ventilasi tertutup.",
            "penyimpanan": "Tabung baja tahan korosi khusus untuk F₂.",
            "p3k": "Segera ke IGD, jangan tunda.",
            "link": "#"
    },
        "Br2": {
            "nama": "Bromin (Br₂)",
            "bahaya": "Uap korosif dan iritasi pada saluran pernapasan.",
            "penanganan": "Gunakan masker dan goggles pelindung.",
            "penyimpanan": "Botol gelap tahan korosi, jauh dari panas.",
            "p3k": "Cuci area terkena dan beri udara segar.",
            "link": "#"
    },
        "HCl(g)": {
            "nama": "Asam Klorida (gas)",
            "bahaya": "Sangat korosif dan iritasi paru.",
            "penanganan": "Gunakan pelindung napas dan ventilasi lokal.",
            "penyimpanan": "Simpan dalam tabung logam bertekanan.",
            "p3k": "Bilas mata atau kulit, beri udara segar.",
            "link": "#"
    },
        "HF(g)": {
            "nama": "Asam Fluorida (gas)",
            "bahaya": "Sangat toksik dan menyerang jaringan dalam.",
            "penanganan": "Gunakan APD lengkap dan sistem penyaring gas.",
            "penyimpanan": "Tabung logam tahan korosi, simpan di tempat aman.",
            "p3k": "Segera ke IGD untuk penanganan darurat.",
            "link": "#"
    },
        "O3": {
            "nama": "Ozon (O₃)",
            "bahaya": "Oksidator kuat, menyebabkan iritasi paru-paru.",
            "penanganan": "Gunakan detektor ozon dan ventilasi baik.",
            "penyimpanan": "Hindari paparan sinar UV langsung.",
            "p3k": "Pindahkan ke udara segar, dapatkan bantuan medis.",
            "link": "#"
    },
        "PH3": {
            "nama": "Fosfin (PH₃)",
            "bahaya": "Sangat beracun dan mudah meledak.",
            "penanganan": "Gunakan APD lengkap dan tangani di fume hood.",
            "penyimpanan": "Simpan dalam silinder baja tertutup rapat.",
            "p3k": "Segera ke IGD.",
            "link": "#"
    },
        "AsH3": {
            "nama": "Arsina (AsH₃)",
            "bahaya": "Toksik berat, menyerang sel darah merah.",
            "penanganan": "Gunakan respirator, detektor gas, dan APD.",
            "penyimpanan": "Tabung logam tahan tekanan.",
            "p3k": "Penanganan medis darurat segera.",
            "link": "#"
    },
        "ClO2": {
            "nama": "Klorin Dioksida (ClO₂)",
            "bahaya": "Eksplosif, oksidator kuat dan toksik.",
            "penanganan": "Tangani dalam kondisi dingin, ventilasi cukup.",
            "penyimpanan": "Botol gelap bertekanan rendah, jauhkan dari cahaya.",
            "p3k": "Berikan oksigen dan bantuan medis segera.",
            "link": "#"
    },
        "HNO3(g)": {
            "nama": "Asam Nitrat Uap",
            "bahaya": "Korosif dan iritasi berat.",
            "penanganan": "Gunakan pelindung napas dan goggles.",
            "penyimpanan": "Tertutup rapat dan jauh dari panas.",
            "p3k": "Udara segar, bilas dengan air jika kontak.",
            "link": "#"
    },
        "NO": {
            "nama": "Nitric Oxide (NO)",
            "bahaya": "Gas reaktif, membentuk NO₂ di udara.",
            "penanganan": "Ventilasi kuat dan APD lengkap.",
            "penyimpanan": "Simpan dalam silinder logam.",
            "p3k": "Berikan oksigen dan pengawasan medis.",
            "link": "#"
    },
        "CO2": {
            "nama": "Karbon Dioksida (CO₂)",
            "bahaya": "Dapat menyebabkan sesak napas dalam ruang tertutup.",
            "penanganan": "Ventilasi baik dan pantau kadar CO₂.",
            "penyimpanan": "Tabung gas standar tekanan tinggi.",
            "p3k": "Pindahkan ke tempat terbuka segera.",
            "link": "#"
    },
        "H2": {
            "nama": "Hidrogen (H₂)",
            "bahaya": "Gas sangat mudah meledak bila tercampur udara.",
            "penanganan": "Jauhkan dari api dan percikan listrik.",
            "penyimpanan": "Simpan dalam tabung tekanan tinggi.",
            "p3k": "Evakuasi area, beri udara segar.",
            "link": "#"
    },
        "N2O": {
            "nama": "Nitrous Oxide (N₂O)",
            "bahaya": "Gas anestesi, memabukkan dalam jumlah tinggi.",
            "penanganan": "Gunakan ventilasi dan kontrol paparan.",
            "penyimpanan": "Tabung baja dengan label jelas.",
            "p3k": "Pindahkan ke udara segar.",
            "link": "#"
    },
        "CH4": {
            "nama": "Metana (CH₄)",
            "bahaya": "Gas mudah meledak, tidak beracun tapi mudah terbakar.",
            "penanganan": "Jauhkan dari sumber api dan gunakan detektor gas.",
            "penyimpanan": "Silinder gas tertutup rapat.",
            "p3k": "Ventilasi ruangan dan evakuasi.",
            "link": "#"
        }
    },
        "Pelarut Organik": {
        "Etanol": {
            "nama": "Etanol (C₂H₅OH)",
            "bahaya": "Mudah terbakar.",
            "penanganan": "Jauhkan dari api dan sumber panas.",
            "penyimpanan": "Simpan dalam wadah tertutup pada suhu ruang.",
            "p3k": "Pindahkan ke udara segar jika terhirup.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/aldrich/459836"
    },
        "Metanol": {
            "nama": "Metanol (CH₃OH)",
            "bahaya": "Toksik, paparan dapat menyebabkan kebutaan.",
            "penanganan": "Gunakan sarung tangan dan hindari kontak langsung.",
            "penyimpanan": "Simpan di tempat sejuk dan berventilasi baik.",
            "p3k": "Segera bawa ke fasilitas medis jika terpapar.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sial/34860"
    },
        "Aseton": {
            "nama": "Aseton (CH₃COCH₃)",
            "bahaya": "Mudah terbakar.",
            "penanganan": "Jauhkan dari api dan sumber panas.",
            "penyimpanan": "Simpan dalam botol tertutup rapat.",
            "p3k": "Pastikan ventilasi baik dan bawa ke udara segar.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/sigald/179124"
    },
        "Benzena": {
            "nama": "Benzena",
            "bahaya": "Karsinogenik dan beracun.",
            "penanganan": "Gunakan masker dan alat pelindung diri lengkap.",
            "penyimpanan": "Simpan di tempat dingin dan berventilasi.",
            "p3k": "Segera cari bantuan medis jika terpapar.",
            "link": "https://www.scribd.com/document/473505991/Benzene-MSDS"
    },
        "Toluena": {
            "nama": "Toluena",
            "bahaya": "Mudah menguap dan berbahaya jika terhirup.",
            "penanganan": "Gunakan di area berventilasi baik.",
            "penyimpanan": "Simpan dalam botol gelap yang tertutup rapat.",
            "p3k": "Pindahkan ke udara segar jika terpapar.",
            "link": "https://www.fishersci.com/store/msds?countryCode=US&language=en&partNumber=AC326980010&productDescription=TOLUENE&vendorId=VN00033901"
    },
        "Xilena": {
            "nama": "Xilena",
            "bahaya": "Iritasi dan bersifat racun.",
            "penanganan": "Gunakan pelindung pernapasan dan APD.",
            "penyimpanan": "Simpan di tempat kering dan tertutup.",
            "p3k": "Pindahkan ke udara segar.",
            "link": "https://www.pcs.com.sg/wp-content/uploads/2017/04/PCS08006.pdf"
    },
        "Kloroform": {
            "nama": "Kloroform",
            "bahaya": "Bersifat narkotik dan toksik.",
            "penanganan": "Gunakan masker uap organik dan APD.",
            "penyimpanan": "Simpan dalam botol gelap, jauh dari cahaya.",
            "p3k": "Bawa ke IGD segera jika terpapar.",
            "link": "https://www.sigmaaldrich.com/ID/en/sds/SIAL/288306"
    },
        "Diethyl Ether": {
            "nama": "Dietil Eter",
            "bahaya": "Sangat mudah terbakar dan mudah meledak.",
            "penanganan": "Jauhkan dari listrik statis dan api.",
            "penyimpanan": "Gunakan botol tahan tekanan dan tertutup rapat.",
            "p3k": "Evakuasi area dan cari bantuan medis.",
            "link": "#"
    },
        "Tetrahidrofuran": {
            "nama": "Tetrahidrofuran (THF)",
            "bahaya": "Reaktif dengan udara dan mudah terbakar.",
            "penanganan": "Gunakan alat pelindung diri lengkap.",
            "penyimpanan": "Simpan dalam botol gelap yang tertutup.",
            "p3k": "Pindahkan ke udara segar.",
            "link": "#"
    },
        "DMSO": {
            "nama": "Dimetilsulfoksida (DMSO)",
            "bahaya": "Dapat menembus kulit dan membawa zat lain ke dalam tubuh.",
            "penanganan": "Gunakan sarung tangan khusus dan APD.",
            "penyimpanan": "Simpan tertutup rapat di tempat sejuk.",
            "p3k": "Cuci dengan air mengalir jika kontak dengan kulit.",
            "link": "#"
    },
        "Formamida": {
            "nama": "Formamida",
            "bahaya": "Toksik jika terhirup atau terserap kulit.",
            "penanganan": "Gunakan di ruang berventilasi baik.",
            "penyimpanan": "Simpan di tempat kering dan tertutup.",
            "p3k": "Pindahkan ke udara segar.",
            "link": "#"
    },
        "Pyridine": {
            "nama": "Piridin",
            "bahaya": "Bau menyengat dan bersifat iritasi.",
            "penanganan": "Gunakan masker dan APD.",
            "penyimpanan": "Simpan dalam botol tertutup rapat.",
            "p3k": "Bilas area kontak dan pindahkan ke udara segar.",
            "link": "#"
    },
        "Aniline": {
            "nama": "Anilin",
            "bahaya": "Toksik dan karsinogenik.",
            "penanganan": "Gunakan alat pelindung diri lengkap.",
            "penyimpanan": "Simpan dalam wadah gelap dan tertutup.",
            "p3k": "Segera ke rumah sakit jika terpapar.",
            "link": "#"
    },
        "Nitrobenzene": {
            "nama": "Nitrobenzena",
            "bahaya": "Toksik kuat dan dapat merusak organ.",
            "penanganan": "Gunakan pelindung lengkap dan kerja di fume hood.",
            "penyimpanan": "Simpan tertutup rapat, jauh dari panas.",
            "p3k": "Segera cari pertolongan medis.",
            "link": "#"
    },
        "Butanol": {
            "nama": "Butanol",
            "bahaya": "Mudah terbakar dan iritasi.",
            "penanganan": "Hindari api dan gunakan ventilasi baik.",
            "penyimpanan": "Simpan dalam botol aman dan tertutup.",
            "p3k": "Pindahkan ke udara segar dan beri ventilasi.",
            "link": "#"
    },
        "Isopropanol": {
            "nama": "Isopropil Alkohol",
            "bahaya": "Mudah terbakar dan menyebabkan iritasi.",
            "penanganan": "Jauhkan dari panas dan nyala api.",
            "penyimpanan": "Gunakan botol kaca/plastik yang tertutup.",
            "p3k": "Pindahkan ke udara segar jika terhirup.",
            "link": "#"
    },
        "Hexane": {
            "nama": "Heksana",
            "bahaya": "Neurotoksik dan mudah menguap.",
            "penanganan": "Gunakan ventilasi baik dan APD.",
            "penyimpanan": "Simpan dalam wadah tertutup rapat.",
            "p3k": "Pindahkan ke udara segar.",
            "link": "#"
    },
        "Cyclohexane": {
            "nama": "Sikloheksana",
            "bahaya": "Iritasi dan mudah terbakar.",
            "penanganan": "Gunakan pelindung kimia lengkap.",
            "penyimpanan": "Simpan dalam wadah tertutup rapat.",
            "p3k": "Pindahkan ke udara segar.",
            "link": "#"
    },
        "Acetonitrile": {
            "nama": "Asetonitril",
            "bahaya": "Beracun dan mudah terbakar.",
            "penanganan": "Gunakan pelindung lengkap dan kerja di fume hood.",
            "penyimpanan": "Simpan dalam wadah tertutup rapat.",
            "p3k": "Segera cari pertolongan medis.",
            "link": "#"
    },
        "Chlorobenzene": {
            "nama": "Klorobenzena",
            "bahaya": "Iritasi dan bersifat toksik.",
            "penanganan": "Gunakan ventilasi dan masker.",
            "penyimpanan": "Simpan dalam botol tertutup dan jauh dari panas.",
            "p3k": "Cuci area terkena dan pindahkan ke udara segar.",
            "link": "#"
        
        }
    }
}

# ---------------------
# DATA KUIS
# ---------------------
pg = [
    {"soal": "Fungsi MSDS adalah...", "opsi": ["Label botol", "Panduan eksperimen", "Informasi bahan kimia", "Lembar nilai"], "jawaban": "Informasi bahan kimia"},
    {"soal": "Senyawa Etanol termasuk...", "opsi": ["Asam", "Basa", "Gas", "Pelarut organik"], "jawaban": "Pelarut organik"},
    {"soal": "Bahaya utama Cl2 adalah...", "opsi": ["Inflamasi kulit", "Bau harum", "Toksik", "Flu"], "jawaban": "Toksik"},
    {"soal": "Metanol jika tertelan dapat menyebabkan...", "opsi": ["Sakit perut", "Buta", "Pilek", "Demam"], "jawaban": "Buta"},
    {"soal": "NaOH sebaiknya tidak disimpan dekat dengan...", "opsi": ["Asam", "Air", "Alkohol", "Besi"], "jawaban": "Asam"},
]

isian = [
    {"soal": "Apa bahaya utama dari HCl?", "jawaban": ["korosif", "iritasi", "membakar"]},
    {"soal": "Mengapa H2SO4 tidak boleh dituangkan ke air?", "jawaban": ["eksoterm", "panas", "reaksi eksoterm"]},
]

# ---------------------
# HALAMAN 1: BERANDA
# ---------------------
if st.session_state.halaman == 1:
    st.title("💻 Web Pengenalan Risiko dan Cara Menangani Senyawa Kimia Umum")
    st.markdown("### 👥 Kelompok 10 - LPK")
    st.markdown("""
    Anggota:
    1. Aurellia Syafa Ghania (2460339)
    2. Hafis Dwi Bahariyanto (2460381)
    3. Nabilah Afrina Fatin (2460448)
    4. Raden Siti Nurul Rachma (2460486)
    5. Yuchi Berliana Resti (2460540)
    """)
    st.markdown("""
🚨 Kimia bukan cuma soal rumus, tapi juga soal *keselamatan!*  
Kenalan yuk sama *senyawa-senyawa kimia penting*,  
pelajari potensi bahayanya, dan cari tahu cara aman menghadapinya 💥
""")
    st.markdown("""
    👉 Klik Next untuk mulai dan uji wawasanmu di akhir lewat kuis seru!
    """)
    st.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 2: PENJELASAN
# ---------------------
elif st.session_state.halaman == 2:
    st.title("📘 Tentang Aplikasi")
    st.markdown("""
    Aplikasi ini dibuat untuk membantu pengguna memahami *risiko dan penanganan bahan kimia umum* yang sering digunakan di laboratorium atau lingkungan kerja.

    Dengan aplikasi ini, pengguna dapat:
    - Mengenal jenis-jenis bahan kimia yang sering dijumpai
    - Memahami potensi bahaya dari masing-masing senyawa
    - Mengetahui langkah penanganan aman jika terjadi tumpahan, paparan, atau kebocoran
    - Mengetahui cara penyimpanan yang benar
    - Memahami langkah pertolongan pertama (P3K) saat terjadi kecelakaan kimia

    Aplikasi ini juga dilengkapi dengan *kuis interaktif* untuk menguji pemahaman Anda.

    ---
    ### ⚠ Catatan Penting
    Informasi dalam aplikasi ini bersifat *edukatif* dan ditujukan untuk memberikan pemahaman dasar. Dalam praktik nyata, tetap ikuti *SOP keselamatan kerja* dan konsultasikan dengan petugas *K3 (Keselamatan dan Kesehatan Kerja)* jika diperlukan.

    ---
    ### 📚 Sumber Informasi
    Data bahan kimia diambil dan disederhanakan dari sumber-sumber terpercaya seperti:
    - MSDS resmi 
    - Lembaga keselamatan kerja 
    """)
    col1, col2 = st.columns(2)
    col1.button("⬅ Back", on_click=back)
    col2.button("Next ▶", on_click=next)
# ---------------------
# HALAMAN 3: SENYAWA KIMIA
# ---------------------
elif st.session_state.halaman == 3:
    st.title("📄 Daftar Senyawa")
    kategori = st.selectbox("Pilih kategori:", list(msds_data.keys()))
    senyawa = st.selectbox("Pilih senyawa:", list(msds_data[kategori].keys()))
    data = msds_data[kategori][senyawa]

    st.subheader(data["nama"])
    st.markdown(f"Bahaya: {data['bahaya']}")
    st.markdown(f"Penanganan: {data['penanganan']}")
    st.markdown(f"Penyimpanan: {data['penyimpanan']}")
    st.markdown(f"P3K: {data['p3k']}")
    st.markdown(f"📄 [Lihat MSDS Lengkap]({data['link']})")

    col1, col2 = st.columns(2)
    col1.button("⬅ Back", on_click=back)
    col2.button("Next ▶", on_click=next)

# ---------------------
# HALAMAN 4: KUIS
# ---------------------
elif st.session_state.halaman == 4:
    st.title("📝 Kuis Pengayaan")

    if not st.session_state.kuis_selesai:
        st.session_state.nama = st.text_input("Nama:")
        st.session_state.instansi = st.text_input("Instansi:")

        st.markdown("### Soal Pilihan Ganda")
        for i, soal in enumerate(pg):
            st.session_state.jawaban_pg[i] = st.radio(soal["soal"], soal["opsi"], key=f"pg_{i}")

        st.markdown("### Soal Isian")
        for i, soal in enumerate(isian):
            st.session_state.jawaban_isian[i] = st.text_input(soal["soal"], key=f"isian_{i}")

        if st.button("Kumpulkan Jawaban"):
            st.session_state.kuis_selesai = True
    else:
        benar = 0
        st.markdown(f"Nama: {st.session_state.nama}")
        st.markdown(f"NIM: {st.session_state.nim}")
        st.markdown("---")

        for i, soal in enumerate(pg):
            jwb = st.session_state.jawaban_pg[i]
            kunci = soal["jawaban"]
            st.markdown(f"{i+1}. {soal['soal']}")
            st.write(f"Jawaban kamu: {jwb}")
            st.write(f"Kunci: {kunci}")
            if jwb == kunci:
                benar += 1

        for i, soal in enumerate(isian):
            jwb = st.session_state.jawaban_isian[i].strip().lower()
            kunci_list = soal["jawaban"]
            st.markdown(f"{i+1+len(pg)}. {soal['soal']}")
            st.write(f"Jawaban kamu: {jwb}")
            st.write(f"Kunci kemungkinan: {', '.join(kunci_list)}")
            if jwb in kunci_list:
                benar += 1

        total = len(pg) + len(isian)
        skor = round((benar / total) * 100, 2)
        st.success(f"🎉 Skor Akhir: {skor} / 100")

        if st.button("⬅ Kembali ke Halaman Awal"):
            st.session_state.halaman = 1
            st.session_state.kuis_selesai = False
