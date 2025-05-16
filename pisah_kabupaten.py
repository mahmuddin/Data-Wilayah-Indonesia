import pandas as pd

# Baca CSV dengan memastikan 'kode_kabupaten' dibaca sebagai string
df_provinsi = pd.read_csv('provinsi.csv', dtype={'kode_provinsi': str})
df_kabupaten = pd.read_csv('kabupaten_kota.csv', dtype={'kode_kabupaten': str})

# Pisahkan 'kode_provinsi' dan 'kode_kabupaten'
df_kabupaten[['kode_provinsi', 'kode_kabupaten']
             ] = df_kabupaten['kode_kabupaten'].str.split('.', expand=True)

# Simpan hasilnya
df_kabupaten.to_csv('kabupaten_terpisah.csv', index=False)

# Tampilkan hasil
print(df_kabupaten[['kode_kabupaten', 'kode_provinsi', 'name']])
