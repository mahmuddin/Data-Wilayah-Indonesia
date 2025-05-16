import pandas as pd

# ============================
# 1. PROVINSI
# ============================
df_provinsi = pd.read_csv('provinsi.csv', dtype={'kode_provinsi': str})

# ============================
# 2. KABUPATEN
# ============================
df_kabupaten = pd.read_csv('kabupaten_kota.csv', dtype={'kode_kabupaten': str})

# Tambahkan kode_provinsi dari kode_kabupaten
df_kabupaten['kode_provinsi'] = df_kabupaten['kode_kabupaten'].str.split(
    '.').str[0]

# Simpan hasil kabupaten
df_kabupaten = df_kabupaten[['kode_kabupaten', 'kode_provinsi', 'name']]
df_kabupaten.to_csv('kabupaten_hierarki.csv', index=False)
print("=== Data Kabupaten ===")
print(df_kabupaten)

# ============================
# 3. KECAMATAN
# ============================
df_kecamatan = pd.read_csv('kecamatan.csv', dtype={'kode_kecamatan': str})

# Tambahkan kode_kabupaten dan kode_provinsi dari kode_kecamatan
df_kecamatan['kode_provinsi'] = df_kecamatan['kode_kecamatan'].str.split(
    '.').str[0]
df_kecamatan['kode_kabupaten'] = df_kecamatan['kode_kecamatan'].str.split(
    '.').str[0] + '.' + df_kecamatan['kode_kecamatan'].str.split('.').str[1]

df_kecamatan = df_kecamatan[['kode_kecamatan',
                             'kode_kabupaten', 'kode_provinsi', 'name']]
df_kecamatan.to_csv('kecamatan_hierarki.csv', index=False)
print("\n=== Data Kecamatan ===")
print(df_kecamatan)

# ============================
# 4. KELURAHAN
# ============================
df_kelurahan = pd.read_csv('kelurahan.csv', dtype={'kode_kelurahan': str})

# Ambil semua kode dari kode_kelurahan
df_kelurahan['kode_provinsi'] = df_kelurahan['kode_kelurahan'].str.split(
    '.').str[0]
df_kelurahan['kode_kabupaten'] = df_kelurahan['kode_provinsi'] + \
    '.' + df_kelurahan['kode_kelurahan'].str.split('.').str[1]
df_kelurahan['kode_kecamatan'] = df_kelurahan['kode_kabupaten'] + \
    '.' + df_kelurahan['kode_kelurahan'].str.split('.').str[2]

df_kelurahan = df_kelurahan[[
    'kode_kelurahan', 'kode_kecamatan', 'kode_kabupaten', 'kode_provinsi', 'name']]
df_kelurahan.to_csv('kelurahan_hierarki.csv', index=False)
print("\n=== Data Kelurahan ===")
print(df_kelurahan)
