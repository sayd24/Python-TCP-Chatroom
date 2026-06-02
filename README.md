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

Simulasi ini membutuhkan minimal 3 terminal (1 Server + 2 Client). Jalankan dengan urutan berikut:

### 1. Aktifkan Server (Terminal 1)
Masuk ke direktori proyek, lalu eksekusi:
```bash
py server.py
