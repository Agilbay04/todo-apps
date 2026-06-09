# Mengambil base image Python 3.10 versi slim (ringan)
FROM python:3.10-slim

# Membuat dan pindah ke folder /app di dalam container
WORKDIR /app

# Menyalin file requirements.txt dari laptop ke container
COPY requirements.txt .

# Menginstal semua library Python tanpa menyimpan file sampah installer
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh source code project dari laptop ke container
COPY . .

# Membuka jalur port 5000 di dalam container
EXPOSE 5005

# Menjalankan aplikasi Flask saat container dinyalakan
CMD ["python", "app.py"]