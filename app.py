import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Streamlit Simple App')

# Navigasi sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")
    
    # Baca & tampilkan file CSV
    data = pd.read_csv("pddikti_example.csv")
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    # Buat visualisasi (simpan ke variabel fig)
    fig = plt.figure(figsize=(12, 6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]
        subset = subset.sort_values(by="id", ascending=False)
        plt.plot(subset['semester'], subset['jumlah'], label=prog_studi)

    plt.title(f"Visualisasi Data untuk {selected_university}")
    plt.xlabel('Semester')
    plt.xticks(rotation=90)
    plt.ylabel('Jumlah')
    plt.legend()

    # Tampilkan grafik menggunakan objek fig
    st.pyplot(fig)