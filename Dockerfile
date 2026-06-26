# Mengambil base image Python 3.10 versi slim (versi ringan)
FROM python:3.10-slim

# Membuat dan pindah ke folder /app di dalam image
WORKDIR /app

# Menyalin file requirements.txt dari host ke image
COPY requirements.txt .

# Menginstal semua library yang dibutuhkan di dalam image
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh source code dari host ke image
COPY . .

# Membuka port 5005 agar bisa diakses dari luar container
EXPOSE 5005

# Menyalin entrypoint.sh dari host ke image
COPY entrypoint.sh /entrypoint.sh

# Memberi izin eksekusi file entrypoint.sh
RUN chmod +x /entrypoint.sh

# Menjalankan entrypoint.sh saat container dijalankan
CMD ["/entrypoint.sh"]