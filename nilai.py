import streamlit as st

class NilaiMahasiswaApp:
    def __init__(self):
        pass

    def run(self):
        if 'data_mahasiswa' not in st.session_state:
            st.session_state['data_mahasiswa'] = []

        st.title("Nilai Mahasiswa")

        if not st.session_state['data_mahasiswa']:
            st.warning("Data mahasiswa belum tersedia. Silakan tambahkan data di menu Data Mahasiswa terlebih dahulu.")
            return  

        mata_kuliah_mapping = {
            "Semester 8": ["Tugas Akhir"],
            "Semester 7": ["Keterampilan Kepemimpinan", "Implementasi Solusi", "Presentasi Proyek"],
            "Semester 6": ["Keterampilan Kerjasama", "Analisis dan Desain Solusi", "Teknik Identifikasi Masalah"],
            "Semester 5": ["Enterprise Architecture Integration", "Digital Branding", "Sistem Manajemen Keamanan Informasi"],            
            "Semester 4": ["Kecerdasan Artifisial", "Cloud Computing", "Tata Kelola Teknologi Informasi"],            
            "Semester 3": ["Kewirausahaan", "Rekayasa Perangkat Lunak", "Bahasa Inggris 2"],            
            "Semester 2": ["Statistik dan Probabilitas", "Basis Data", "Presentasi Proyek"],            
            "Semester 1": ["Dasar-Dasar Pemrograman", "Pemrograman Web 1", "Pengantar Teknologi Informasi"],
        }

        mahasiswa_selected = st.selectbox(
            "Pilih Mahasiswa",
            st.session_state['data_mahasiswa'],
            format_func=lambda x: x["Nama Mahasiswa"]
        )

        nama_mahasiswa = mahasiswa_selected["Nama Mahasiswa"]
        nim_mahasiswa = mahasiswa_selected["NIM"]
        semester_mahasiswa = mahasiswa_selected["Semester"]

        st.text_input("Nama Mahasiswa", value=nama_mahasiswa, disabled=True)
        st.text_input("NIM", value=nim_mahasiswa, disabled=True)

        mata_kuliah_options = mata_kuliah_mapping.get(semester_mahasiswa, [])
        mata_kuliah = st.selectbox("Mata Kuliah", mata_kuliah_options)

        keaktifan = st.number_input("Kehadiran & Tugas", min_value=0, max_value=100, step=1)
        uts = st.number_input("UTS", min_value=0, max_value=100, step=1)
        uas = st.number_input("UAS", min_value=0, max_value=100, step=1)

        if st.button("Simpan Nilai"):
            for mahasiswa in st.session_state['data_mahasiswa']:
                if mahasiswa["NIM"] == nim_mahasiswa:
                    mahasiswa["Kehadiran & Tugas"] = keaktifan
                    mahasiswa["UTS"] = uts
                    mahasiswa["UAS"] = uas
                    mahasiswa["Mata Kuliah"] = mata_kuliah
                    break
            st.success("Nilai berhasil disimpan!")
