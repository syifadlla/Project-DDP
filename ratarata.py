import streamlit as st

class RataRataApp:
    def __init__(self):
        pass

    def run(self):
        st.title("Nilai Rata-Rata Mahasiswa")

        if 'data_mahasiswa' not in st.session_state or not st.session_state['data_mahasiswa']:
            st.warning("Nilai mahasiswa belum tersedia. Silakan tambahkan nilai di menu Nilai Mahasiswa.")
        else:
            st.write("**Rata-Rata Nilai Mahasiswa:**")

            data_mahasiswa = st.session_state['data_mahasiswa']

            for idx, data in enumerate(data_mahasiswa):
                try:
                    if "Kehadiran & Tugas" not in data or "UTS" not in data or "UAS" not in data:
                        raise ValueError("Nilai belum diinput")

                    rata_rata = (data["Kehadiran & Tugas"] + data["UTS"] + data["UAS"]) / 3
                    st.write(f"{idx + 1}. **{data['Nama Mahasiswa']} ({data['NIM']})**: {rata_rata:.2f}")
                except ValueError:
                    st.error(f"{idx + 1}. **{data['Nama Mahasiswa']} ({data['NIM']})**: Nilai belum diinput. Silakan lengkapi nilai!")
