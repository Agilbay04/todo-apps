# Mengambil base image Python 3.10 versi slim (versi ringan)
FROM python:3.10-slim

# Membuat dan pindah ke folder /app di dalam container
WORKDIR /app

# Menyalin file requirements.txt dari laptop ke container
COPY requirements.txt .

# Menginstal semua library yang dibutuhkan
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh source code project dari laptop ke container
COPY . .

# Membuka jalur port 5005 di dalam container agar bisa diakses dari luar (laptop)
EXPOSE 5005

# Menentukan command untuk menjalankan aplikasi Flask saat container dinyalakan
CMD ["python", "app.py"]