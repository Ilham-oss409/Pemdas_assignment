data_panen = {
    'lokasi1': {'nama_lokasi': 'Kebun A', 'hasil_panen': {'padi': 1200, 'jagung': 800, 'kedelai': 500}},
    'lokasi2': {'nama_lokasi': 'Kebun B', 'hasil_panen': {'padi': 1500, 'jagung': 900, 'kedelai': 450}},
    'lokasi3': {'nama_lokasi': 'Kebun C', 'hasil_panen': {'padi': 1100, 'jagung': 750, 'kedelai': 600}},
    'lokasi4': {'nama_lokasi': 'Kebun D', 'hasil_panen': {'padi': 1300, 'jagung': 850, 'kedelai': 550}},
    'lokasi5': {'nama_lokasi': 'Kebun E', 'hasil_panen': {'padi': 1400, 'jagung': 950, 'kedelai': 480}}
}


for lokasi, info in data_panen.items():
    print(f"nama Lokasi: {info['nama_lokasi']}, hasil Panen: {info['hasil_panen']}")

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
