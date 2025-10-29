# UMN Daily Task Automation

Automasi pengisian **Daily Task UMN** menggunakan Python dan Selenium.

---

## ⚠️ Disclaimer

1. Gunakan program ini **dengan tanggung jawab masing-masing**. Penulis **tidak bertanggung jawab** atas kerugian atau kesalahan.
2. Program ini **tidak menyimpan data login** sama sekali. Credential tetap aman.
3. Pastikan data di `data.json` **sudah benar** sebelum dijalankan.

---

## 🛠 Environment Setup

### 1. Siapkan `.env`

- Copy file `.env.example` → rename jadi `.env`
- Isi dengan **credential student kalian masing-masing**

### 2. Buat virtual environment (opsional tapi direkomendasikan)

```bash
python -m venv env
```

### 3. Aktifkan environment

**Windows (cmd / PowerShell):**

```powershell
.\env\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Cara Pemakaian

1. Pastikan file `.env` berisi **data student kalian**.
2. Pastikan **Google Chrome** sudah terinstall.
3. Pastikan `data.json` sudah diisi sesuai **daily task** yang ingin diisi.
4. Jalankan program:

```bash
python main.py
```

5. Tunggu proses selesai.

> Setelah selesai, akan muncul log:
> `"All Task have been filled"`
> Tekan **Enter** di terminal untuk menutup program.

## 📌 Catatan Tambahan

- Apabila terdapat bug atau output tidak sesuai tolong hubungi developer

## Inspired by
Project ini terinspirasi dari [oscarjiro](https://github.com/username/repo](https://github.com/oscarjiro).
