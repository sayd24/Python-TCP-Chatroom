# Python-TCP-Chatroom
Tugas Pemrograman Socket - Jaringan Komputer

# Python-TCP-Chatroom
Tugas Pemrograman Socket - Jaringan Komputer

# Simulasi Chat Room Berbasis Protokol TCP Menggunakan Python Socket

Proyek ini mendemonstrasikan komunikasi antar-client (*client-to-client*) melalui perantara server menggunakan **Socket Programming** berbasis protokol **TCP (`SOCK_STREAM`)**. Implementasi menggunakan metode **Multithreading** agar server mampu menangani banyak koneksi client secara bersamaan (*concurrent*) tanpa terjadi interupsi.

## Fitur Utama
* **Protokol TCP:** Menjamin pengiriman data yang reliabel, utuh, dan berurutan.
* **Multithreading:** Mengelola setiap client pada thread terpisah menggunakan library `threading`.
* **Sistem Broadcast:** Meneruskan pesan dari satu client ke seluruh jaringan client aktif.
* **Log Server:** Mencatat lalu lintas pesan secara real-time di terminal server untuk monitoring.

---

## Struktur Berkas
* `server.py` — Mengatur manajemen jaringan, jabat tangan (*handshake*) nama pengguna, dan distribusi pesan.
* `client.py` — Sisi pengguna untuk memasukkan identitas, mengirim, dan menerima data pesan.

---

## Panduan Menjalankan Simulasi

Simulasi ini membutuhkan minimal 3 terminal (1 Server + 2 Client). Buka 3 terminal terpisah di dalam direktori proyek, lalu jalankan perintah berikut secara berurutan:

```bash
# 1. Aktifkan Server di Terminal 1
py server.py

# 2. Hubungkan Client Pertama di Terminal 2 (Lalu masukkan nama, misal: sayd)
py client.py

# 3. Hubungkan Client Kedua di Terminal 3 (Lalu masukkan nama, misal: aldi)
py client.py
```

Setelah ketiga terminal aktif, komunikasi dua arah antar-client sudah dapat dilakukan secara real-time melalui jaringan lokal.

---

Setelah ketiga terminal aktif, komunikasi dua arah antar-client sudah dapat dilakukan secara real-time melalui jaringan lokal.
