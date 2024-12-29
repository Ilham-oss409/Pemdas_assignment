 menampilkan data
Perubahan di Master

print(f"hasil panen jagung di lokasi2: {data_panen['lokasi2']['hasil_panen']['jagung']}")


print(f"nama lokasi dari lokasi3: {data_panen['lokasi3']['nama_lokasi']}")


jumlah_padi = {key: value['hasil_panen']['padi'] for key, value in data_panen.items()}
jumlah_kedelai = {key: value['hasil_panen']['kedelai'] for key, value in data_panen.items()}

for lokasi, info in data_panen.items():
    padi = info['hasil_panen']['padi']
    jagung = info['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {info['nama_lokasi']} Memerlukan perhatian khusus.")
    #else:
        print(f"Lokasi {info['nama_lokasi']} dalam kondisi baik.")
