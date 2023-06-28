import streamlit as st
import pandas as pd

st.title("_:blue[Aldi Rizki Yudistira]_")
def main():
	st.title("thank you")

import streamlit as st

profil_image = st.image("foto_profil/kaka.jpg", width=100, caption="Foto Profil", use_column_width=True,)


st.write('Nama 			: Aldi Rizki Yudistira')
st.write('TTL 			: Sumedang, 21 Mei 2001')
st.write('Prodi 		: Manajemen Informasi Kesehatan')
st.write('NIM 			: B01.022.002')
       # Input form

st.write("**:red[Silahkan klik dibawah ini untuk melihat informasi!]**")
namaa = ['Who is he?', 'Aldi Rizki Yudistira']
pilihan_nama = st.selectbox('', namaa)
if pilihan_nama == 'Aldi Rizki Yudistira':
	st.write('Adalah seorang perekam medis yang handal dengan pengetahuan yang mendalam dan pengalaman yang luas dalam mengelola dan memelihara rekam medis secara efisien dan akurat. Dedikasi saya terhadap integritas data pasien dan kepatuhan terhadap privasi serta regulasi industri menjadikan saya seorang profesional yang terpercaya dalam bidang ini. Dalam peran saya sebagai perekam medis, saya memiliki keahlian dalam menggunakan sistem rekam medis elektronik (EHR) dan memahami prosedur dan standar dalam pembuatan, penyimpanan, dan pengelolaan rekam medis. Saya terampil dalam mengumpulkan, memvalidasi, dan memperbarui informasi medis, serta mengatur dan mengindeks data dengan presisi tinggi')
else:
	st.write('')

prodi = ['jurusan apa yang sesuai agar bisa menjadi perekam medis?', 'Manajemen Informasi Kesehatan']
pilihan_prodi = st.selectbox('', prodi)
if pilihan_prodi == 'Manajemen Informasi Kesehatan' :
	st.write('Manajemen Informasi Kesehatan mempelajari Sistem Informasi kesehatan untuk penyelesaian masalah di bidang kesehatan sehingga terciptanya pelayanan kesehatan yang good clinical governance. Dengan Lulusan Sarjana Manajemen Informasi Kesehatan (S.MIK)')
else:
	st.write('')

tugas = ['Tugas dan tanggung jawab seorang rekam medis?', 'Disini']
pilihan_prod = st.selectbox('', tugas)
if pilihan_prod == 'Disini' :
	st.write('Seorang staf rekam medis bertanggung jawab juga dalam pemanfaatan data rekam medis sebagai penelitian atau publisitas. Basis data dan informasi tersebut diolah dengan menyediakan rangkuman statistik medis dan penyakit untuk publikasi penelitian ilmiah di bidang kesehatan. Staf rekam medis juga harus bertindak cepat jika suatu waktu data rekam medis diperlukan. Oleh karena itu, menjadi staf rekam medis harus teliti dan mahir dalam pengelolaan dan penyimpanan data.')
else: 
	st.write('')

prod = ['Contact Person', 'WhatsApp', 'Instagram', 'Email']
pilihan_prod = st.selectbox('', prod)
if pilihan_prod == 'WhatsApp' :
	st.write('Click Link [WhatsApp](https://wa.me/087872624702)')
elif pilihan_prod == 'Instagram':
	st.write('Click Link [Instagram](https://instagram.com/aryudistira_)')
elif pilihan_prod == 'Email' :
	st.write('Email: aldiyudistira00@gmail.com')
else:
	st.write('')


#input
nama = st.text_input('Nama :')
umur = st.text_input('umur:')
jenis_kelamin = st.text_input('Jenis Kelamin')

       # Output
st.write("Nama: ", nama)
st.write("Program studi: ", umur)
st.write("NIM: ", jenis_kelamin)



   
if __name__ == "__main__":
	main()
