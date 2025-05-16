import pandas as pd

# Baca CSV kecamatan dengan format string
df_kecamatan = pd.read_csv('kecamatan.csv', dtype={'kode_kecamatan': str})

# Pisahkan berdasarkan titik (.)
df_kecamatan[['kode_provinsi', 'kode_kabupaten', 'kode_kecamatan']
             ] = df_kecamatan['kode_kecamatan'].str.split('.', expand=True)

# Urutkan kolom sesuai kebutuhan
df_kecamatan = df_kecamatan[['kode_kecamatan',
                             'kode_kabupaten', 'kode_provinsi', 'name']]

# Simpan hasil ke CSV baru
df_kecamatan.to_csv('kecamatan_terpisah.csv', index=False)

# Tampilkan hasil
print(df_kecamatan)
