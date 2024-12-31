import streamlit as st
from fitur import data, nilai, ratarata, tabel

def main():
    if "landing_page_visited" not in st.session_state:
        st.session_state["landing_page_visited"] = False
    if not st.session_state["landing_page_visited"]:
        landing_page()
    else:
        pilihan = st.sidebar.selectbox(
            "Pilih Menu",
            ["Data Mahasiswa", "Nilai Mahasiswa", "Rata-rata Nilai", "Hasil"]
        )
        if pilihan == "Data Mahasiswa":
            app = data.DataMahasiswaApp()
            app.run()
        elif pilihan == "Nilai Mahasiswa":
            app = nilai.NilaiMahasiswaApp()
            app.run()
        elif pilihan == "Rata-rata Nilai":
            app = ratarata.RataRataApp()
            app.run()
        elif pilihan == "Hasil":
            app = tabel.TabelMahasiswaApp()
            app.run()

def landing_page():
    """Halaman Landing Page"""
    st.session_state["landing_page_visited"] = True
    st.title("Selamat Datang di Aplikasi Laporan Nilai Mahasiswa🎓")
    st.image(
        "https://i.pinimg.com/736x/5f/74/56/5f7456edde808413876aada644d6ba78.jpg",
        use_container_width=True
    )
    st.write(
        """
        Aplikasi ini dirancang untuk membantu membuat laporan nilai mahasiswa secara mudah dan efisien.
        
        Tekan tombol dibawah untuk mulai!
        """
    )
    if st.button("Mulai"):
        st.session_state["landing_page_visited"] = True


if __name__ == "__main__":
    main()
