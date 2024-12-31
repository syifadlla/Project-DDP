import streamlit as st
import pandas as pd

class TabelMahasiswaApp:
    def __init__(self):
        pass

    def run(self):
        st.title("Tabel Nilai Mahasiswa")

        if 'data_mahasiswa' not in st.session_state or not st.session_state['data_mahasiswa']:
            st.warning("Data dan Nilai Mahasiswa belum tersedia. Silakan tambahkan data di menu Data Mahasiswa dan Nilai Mahasiswa.")
        else:
            data_for_table = []

            for mahasiswa in st.session_state['data_mahasiswa']:
                kehadiran_tugas = mahasiswa.get("Kehadiran & Tugas")
                uts = mahasiswa.get("UTS")
                uas = mahasiswa.get("UAS")

                if isinstance(kehadiran_tugas, (int, float)) and isinstance(uts, (int, float)) and isinstance(uas, (int, float)):
                    rata_rata = (kehadiran_tugas + uts + uas) / 3
                else:
                    rata_rata = None  

                data_for_table.append({
                    "Nama Mahasiswa": mahasiswa.get("Nama Mahasiswa", "-"),
                    "NIM": mahasiswa.get("NIM", "-"),
                    "Angkatan": mahasiswa.get("Angkatan", "-"),
                    "Semester": mahasiswa.get("Semester", "-"),
                    "Mata Kuliah": mahasiswa.get("Mata Kuliah", "Belum Diisi"),
                    "Kehadiran & Tugas": kehadiran_tugas if kehadiran_tugas is not None else "-",
                    "UTS": uts if uts is not None else "-",
                    "UAS": uas if uas is not None else "-",
                    "Rata-Rata": f"{rata_rata:.2f}" if rata_rata is not None else "-"
                })

            df = pd.DataFrame(data_for_table)
            df.index = df.index + 1
            df.reset_index(inplace=True)
            df.rename(columns={"index": "No."}, inplace=True)

            st.dataframe(df, use_container_width=True)

