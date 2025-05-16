import pandas as pd

# Baca CSV kelurahan dengan kode sebagai string
df_kelurahan = pd.read_csv('kelurahan.csv', dtype={'kode_kelurahan': str})

# Pisahkan berdasarkan titik (.)
df_kelurahan[['kode_provinsi', 'kode_kabupaten', 'kode_kecamatan',
              'kode_kelurahan']] = df_kelurahan['kode_kelurahan'].str.split('.', expand=True)

# Urutkan kolom sesuai keinginan
df_kelurahan = df_kelurahan[[
    'kode_kelurahan', 'kode_kecamatan', 'kode_kabupaten', 'kode_provinsi', 'name']]

# Simpan hasil ke CSV baru
df_kelurahan.to_csv('kelurahan_terpisah.csv', index=False)

# Tampilkan hasil
print(df_kelurahan)
