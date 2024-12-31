import streamlit as st

class DataMahasiswaApp:
    def __init__(self):
        pass

    def run(self):
        if 'data_mahasiswa' not in st.session_state:
            st.session_state['data_mahasiswa'] = []

        st.title("Data Mahasiswa")

        nama = st.text_input("Nama Mahasiswa")
        nim = st.text_input("NIM")
        angkatan = st.selectbox("Angkatan", ["2021", "2022", "2023", "2024"], key="angkatan")

        semester_options = self.get_semester_options(angkatan)
        semester = st.selectbox("Semester", semester_options, key="semester")

        if st.button("Masukkan"):
            if not (nama and nim and angkatan and semester):
                st.error("Semua kolom harus diisi!")
            else:
                st.session_state['data_mahasiswa'].append({
                    "Nama Mahasiswa": nama,
                    "NIM": nim,
                    "Angkatan": angkatan,
                    "Semester": semester
                })
                st.success("Data berhasil dimasukkan!")
                st.session_state['nama'] = ''
                st.session_state['nim'] = ''

    def get_semester_options(self, angkatan):
        if angkatan == "2021":
            return ["Semester 7", "Semester 8"]
        elif angkatan == "2022":
            return ["Semester 5", "Semester 6"]
        elif angkatan == "2023":
            return ["Semester 3", "Semester 4"]
        elif angkatan == "2024":
            return ["Semester 1", "Semester 2"]
        return []
