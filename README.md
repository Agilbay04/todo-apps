# Dockerize Todo App -- Python Flask + PostgreSQL

## 1. Deskripsi Singkat

Todo app sederhana berbasis Flask dan PostgreSQL yang di-dockerize.

## 2. Prerequisites

- Docker & Docker Compose -- [Download & Install](https://docs.docker.com/get-docker/)
- Pastikan Docker sudah berjalan di laptop

## 3. Quick Start

```bash
cp .env.example .env
docker compose up -d
```

Buka `http://localhost:5005`

## 4. Struktur Container

| Service | Fungsi                   |
|---------|--------------------------|
| db      | PostgreSQL 15 -- database|
| web     | Aplikasi Flask           |

## 5. Environment Variables

| Variable       | Default     | Keterangan             |
|----------------|-------------|------------------------|
| APP_HOST       | 0.0.0.0     | Host binding           |
| APP_PORT       | 5005        | Port aplikasi          |
| APP_ENV        | dev         | dev / stg / prod       |
| DB_PROVIDER    | postgresql  | Database engine        |
| DB_HOST        | localhost   | Host database          |
| DB_PORT        | 5432        | Port database          |
| DB_NAME        | todo        | Nama database          |
| DB_USER        | todo        | Username database      |
| DB_PASSWORD    | secret      | Password database      |

## 6. Mode Development vs Production

- `APP_ENV=dev` -- Flask dev server (auto-reload, debug aktif). Cocok untuk pengembangan.
- `APP_ENV=stg` atau `APP_ENV=prod` -- Gunicorn (multi-worker). Cocok untuk production.

## 7. Perintah Docker Penting

```bash
docker compose up -d          # Jalankan semua service
docker compose logs -f        # Lihat log secara realtime
docker compose down           # Hentikan semua service
docker compose ps             # Cek status container
```
