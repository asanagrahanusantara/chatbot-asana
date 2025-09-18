# Impor "Flask" untuk membuat server web dan "request" untuk membaca data yang masuk
from flask import Flask, request
# Impor "MessagingResponse" dari library Twilio untuk membuat balasan TwiML
from twilio.twiml.messaging_response import MessagingResponse

# Inisialisasi aplikasi Flask
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    """
    Fungsi ini berisi logika lengkap untuk chatbot properti
    ASANA GRAHA NUSANTARA.
    """
    # Ambil teks pesan yang masuk dan ubah ke huruf kecil
    pesan_masuk = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    balasan = "" # Siapkan variabel balasan kosong

    # --- MENU UTAMA ---
    if 'halo' in pesan_masuk or 'menu' in pesan_masuk:
        balasan = (
            "Selamat datang di layanan ASANA GRAHA NUSANTARA! 👋\n\n"
            "Silakan ketik nama *PRODUK* yang Anda minati:\n"
            "👉 *Azura* (Tanah Kavling)\n"
            "👉 *Zaraya* (Villa Mewah)\n"
            "👉 *Graha* (Hunian Keluarga)\n\n"
            "Atau pilih opsi lain:\n"
            "👉 *Alamat* - Lokasi kantor kami\n"
            "👉 *Marketing* - Hubungi tim kami"
        )

    # --- DAFTAR PRODUK (UMUM) ---
    elif 'produk' in pesan_masuk:
        balasan = (
            "Kami memiliki 3 lini properti unggulan. Silakan balas dengan nama produk yang ingin Anda ketahui lebih lanjut:\n\n"
            "1. *Azura Pasut* (Tanah Kavling Premium di Tabanan)\n"
            "2. *Zaraya Villas* (Villa Mewah di Berawa & Balangan)\n"
            "3. *Graha Harmonia* (Hunian Keluarga Modern di Tabanan)"
        )

    # --- DETAIL PRODUK: AZURA PASUT ---
    elif 'azura' in pesan_masuk:
        balasan = (
            "Anda memilih *AZURA PASUT* - Tanah Kavling Eksklusif di Tabanan.\n\n"
            "Sebuah investasi cerdas di area tren pariwisata Bali yang sedang berkembang ke barat. Berlokasi hanya 200 meter dari Pantai Pasut dengan pemandangan sawah yang menenangkan.\n\n"
            "✅ Status: SHM (Hak Milik)\n"
            "✅ Zona: Pariwisata (ITR Pink)\n"
            "✅ Harga: Mulai dari 550 Juta per are\n\n"
            "Ketik *Marketing* untuk terhubung dengan tim kami dan dapatkan penawaran terbaik."
        )

    # --- DETAIL PRODUK: ZARAYA (MENU PILIHAN) ---
    elif 'zaraya' in pesan_masuk and 'berawa' not in pesan_masuk and 'balangan' not in pesan_masuk:
        balasan = (
            "Anda memilih *ZARAYA VILLAS* - Pilihan Villa Mewah di Lokasi Premium Bali.\n\n"
            "Kami memiliki dua lokasi unggulan. Silakan pilih yang Anda minati:\n\n"
            "👉 Ketik *Zaraya Berawa* untuk villa di jantung lifestyle Canggu.\n"
            "👉 Ketik *Zaraya Balangan* untuk villa dengan potensi ROI tinggi di Bali Selatan."
        )

    # --- DETAIL PRODUK: ZARAYA BERAWA ---
    elif 'berawa' in pesan_masuk:
        balasan = (
            "Anda memilih *ZARAYA VILLAS CANGGU* - Luxury & Lifestyle in Canggu.\n\n"
            "Villa eksklusif di pusat turis Berawa-Canggu yang sangat diminati. Nikmati kemewahan dengan akses mudah ke beach club, cafe, dan destinasi populer lainnya.\n\n"
            "✅ Status: Leasehold 23 Tahun\n"
            "✅ Kondisi: Fully Furnished\n"
            "✅ Lokasi: Sangat strategis, 15 menit ke Atlas/Finns Beach Club\n\n"
            "Ketik *Marketing* untuk info harga dan jadwal survey."
        )

    # --- DETAIL PRODUK: ZARAYA BALANGAN ---
    elif 'balangan' in pesan_masuk:
        balasan = (
            "Anda memilih *ZARAYA VILLAS BALANGAN* - High-Return Investment Villa.\n\n"
            "Investasi properti premium di Bali Selatan yang dikelilingi hotel bintang 7. Menawarkan potensi ROI (Return on Investment) luar biasa hingga 21,3% per tahun.\n\n"
            "✅ Potensi ROI: 21,3% / tahun\n"
            "✅ Status: Freehold (Hak Milik) atau Leasehold\n"
            "✅ Harga Spesial: Mulai dari 220.000 USD\n\n"
            "Ketik *Marketing* untuk konsultasi investasi Anda."
        )

    # --- DETAIL PRODUK: GRAHA HARMONIA ---
    elif 'graha' in pesan_masuk:
        balasan = (
            "Anda memilih *GRAHA HARMONIA* - Hunian Keluarga Modern di Tabanan.\n\n"
            "Pilihan tepat untuk keluarga yang mendambakan hidup seimbang di Tabanan yang tenang dan asri. Desain minimalis dengan sentuhan hangat budaya Bali.\n\n"
            "✅ Tipe: 36/72\n"
            "✅ Fasilitas: 2 Kamar Tidur, Ruang Keluarga, Dapur, Garasi, Kebun\n\n"
            "Ketik *Marketing* untuk informasi KPR dan promo terbaru."
        )

    # --- MENU ALAMAT KANTOR ---
    elif 'alamat' in pesan_masuk:
        balasan = (
            "Anda dapat menemukan kantor pemasaran kami di:\n\n"
            "*PT. Asana Graha Nusantara*\n"
            "Gedung Cenennial TowerLt.29 Unit D-F, Jl. Jend. Gato Subroto Kav. 24-25 RT.002 RW. 002 Kel. Karet Semanggi, Kec. Setiabudi, Jakarta Selatan- DKI Jakarta.\n\n"
            "Untuk memastikan tim kami tersedia, silakan ketik *Marketing* untuk membuat janji temu terlebih dahulu."
        )

    # --- MENU HUBUNGI MARKETING ---
    elif 'marketing' in pesan_masuk or 'kontak' in pesan_masuk or 'hubungi' in pesan_masuk:
        # GANTI NOMOR INI DENGAN NOMOR WA MARKETING YANG SEBENARNYA
        nomor_wa = "6285711881010" 
        balasan = (
            "Untuk informasi lebih lanjut, presentasi produk, atau jadwal survey lokasi, silakan hubungi Marketing Executive kami.\n\n"
            "Anda bisa langsung klik link di bawah ini untuk memulai percakapan via WhatsApp:\n"
            f"https://wa.me/{nomor_wa}?text=Halo,%20saya%20tertarik%20dengan%20properti%20Asana%20Graha%20Nusantara."
        )

    # --- JIKA KATA KUNCI TIDAK DITEMUKAN ---
    else:
        balasan = "Maaf, saya tidak mengerti. Silakan ketik *Menu* untuk melihat semua pilihan yang tersedia."

    # Tambahkan pesan balasan ke dalam respons TwiML
    resp.message(balasan)
    return str(resp)

# --- BAGIAN DI BAWAH INI SENGAJA DINONAKTIFKAN ---
# Baris ini hanya untuk pengujian lokal. Di server produksi seperti Railway,
# Gunicorn akan menjalankan aplikasi ini secara langsung.
# if __name__ == '__main__':
#     app.run(debug=True)

