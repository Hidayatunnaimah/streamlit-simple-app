import streamlit as st

# Fungsi untuk menghitung volume udara
def hitung_volume_udara(laju_alir_awal, laju_alir_akhir, lama_pengukuran):
    volume_udara_liter = ((laju_alir_awal + laju_alir_akhir) / 2) * lama_pengukuran
    volume_udara_meter_kubik = volume_udara_liter / 1000
    return round(volume_udara_meter_kubik, 2)

# Fungsi untuk menghitung volume standar
def hitung_volume_standar(volume_udara_sampling, tekanan_udara, suhu):
    if suhu == 0.0:
        return 0
    volume_udara_standar = volume_udara_sampling * ((tekanan_udara / suhu) * (298 / 760))
    return round(volume_udara_standar, 2)

# Fungsi untuk menghitung kadar debu
def hitung_kadar_debu(bobot_awal, bobot_akhir, volume_udara_standar):
    if volume_udara_standar == 0.0:
        return 0
    kadar_debu = ((bobot_awal - bobot_akhir) * 1000) / volume_udara_standar
    return round(kadar_debu, 2)

# Fungsi Utama
def main():
    
    # Judul Projek
    st.title('Perhitungan :green[Total Partikulat Suspended]')
    st.markdown('Aplikasi ini digunakan untuk membantu analisis dalam mencari **volume udara yang disampling**, **volume udara yang disampling dalam keadaan standar**, dan **kadar debu pada udara ambien menggunakan alat HVAS PM10**.')

    # Form untuk menghitung volume udara
    st.subheader(':fog: Form :gray[Volume Udara]', divider='green') 
    laju_alir_awal = st.number_input(":droplet: Input Laju Alir Awal (L/menit)", placeholder=0.0)
    laju_alir_akhir = st.number_input(":droplet: Laju Alir Akhir (L/menit)", placeholder=0.0)
    lama_pengukuran = st.number_input(":stopwatch: Input Lama Pengukuran (menit)", placeholder=0.0)

    if st.button(':green[Hitung]'):
        if laju_alir_awal == 0.0 and laju_alir_akhir == 0.0 and lama_pengukuran == 0.0:
            st.error("Harap isi inputan dengan angka yang valid")  
    volume_udara_meter_kubik = hitung_volume_udara(laju_alir_awal, laju_alir_akhir, lama_pengukuran)
    st.write(f":star: **Volume udara yang disampling adalah *{volume_udara_meter_kubik:} m³***")

    # Form Untuk menghitung volume udara standar
    st.subheader('Form :orange[Volume udara dalam kondisi standar]', divider='orange')
    volume_udara_sampling = st.number_input(":fog: Input Volume Udara yang Disampling (m³)", value=volume_udara_meter_kubik, format="%.2f")
    tekanan_udara = st.number_input(":dash: Input Tekanan Udara (mmHg)", value=0.0, format="%.2f")
    suhu = st.number_input(":thermometer: Input Suhu (K)", value=0.0, format="%.2f")
    submit_button_standar = st.button(':green[Hitung]', key='submit-button-standar')

    if submit_button_standar:
        if volume_udara_sampling == 0.0 and tekanan_udara == 0.0 and suhu == 0.0:
            st.error("Harap isi inputan dengan angka yang valid")
    volume_udara_standar = hitung_volume_standar(volume_udara_sampling, tekanan_udara, suhu)
    st.write(f":star: **Volume udara dalam kondisi standar adalah *{volume_udara_standar:} Nm³***")

    st.subheader('Form :blue[Hitung kadar debu]', divider='blue')
    bobot_awal = st.number_input("Input Bobot Awal (gram)", value=0.0, format="%.2f")
    bobot_akhir = st.number_input("Input Bobot Akhir (gram)", value=0.0, format="%.2f")
    submit_button_debu =  st.button(':green[Hitung]', key='submit_button_debu')

    if submit_button_debu:
        if bobot_awal == 0.0 and bobot_akhir == 0.0:
            st.error("Harap isi inputan dengan angka yang valid")
    kadar_debu = hitung_kadar_debu(bobot_awal, bobot_akhir, volume_udara_standar)
    st.write(f"**Kadar debu adalah *{kadar_debu:} mg/Nm³***")
    if (kadar_debu / 1000) > 150:
        st.subheader("Partikulat Tidak Memenuhi Baku Mutu")
    elif kadar_debu == 0.00:
        st.subheader("")
    else:
        st.subheader("Partikulat Memenuhi Baku Mutu")

if __name__ == '__main__':
    main()