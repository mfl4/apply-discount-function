# apply-discount-function

Modul Python kecil yang menghitung harga akhir setelah menerapkan diskon
persentase. Modul ini menyediakan satu fungsi yang dapat digunakan kembali,
`apply_discount`, yang memvalidasi masukannya dan mengembalikan harga diskon
atau pesan kesalahan yang mudah dibaca manusia.

## Isi Folder

| Berkas          | Keterangan                                                    |
| --------------- | ------------------------------------------------------------- |
| `main.py`       | Mendefinisikan fungsi `apply_discount`.                       |
| `LICENSE`       | Dedikasi domain publik CC0 1.0 Universal.                     |
| `.gitignore`    | Aturan abaikan standar Python untuk version control.          |

## Cara Memulai

1. Pastikan Python 3 telah terpasang.
2. Impor dan panggil fungsi dari kode Anda sendiri, atau uji langsung:

   ```bash
   python -c "from main import apply_discount; print(apply_discount(100, 20))"
   ```

## Cara Kerja

Fungsi `apply_discount` menerima `price` dan `discount` (keduanya diharapkan
berupa angka) lalu mengembalikan harga akhir setelah diskon diterapkan.

```python
def apply_discount(price, discount):

    if type(price) not in [int, float]:
        return "The price should be a number"

    if type(discount) not in [int, float]:
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    return final_price
```

### Aturan Validasi

Sebelum menghitung apa pun, fungsi memeriksa masukan dan mengembalikan string
kesalahan bila sebuah aturan dilanggar:

- `price` harus `int` atau `float`, jika tidak `"The price should be a number"`.
- `discount` harus `int` atau `float`, jika tidak
  `"The discount should be a number"`.
- `price` harus lebih besar dari `0`, jika tidak
  `"The price should be greater than 0"`.
- `discount` harus antara `0` dan `100` inklusif, jika tidak
  `"The discount should be between 0 and 100"`.

Jika semua pemeriksaan lolos, fungsi menghitung
`discount_amount = price * (discount / 100)` dan mengembalikan
`final_price = price - discount_amount`.

### Contoh Penggunaan

```python
from main import apply_discount

print(apply_discount(100, 20))        # 80.0
print(apply_discount(50, 10))         # 45.0
print(apply_discount(100, 0))         # 100.0
print(apply_discount(100, 100))       # 0.0
print(apply_discount("100", 20))      # The price should be a number
print(apply_discount(100, 150))       # The discount should be between 0 and 100
```

> Catatan: modul ini hanya mendefinisikan fungsi — tidak ada pemanggilan `print`
> di level atas, sehingga menjalankan `python main.py` tidak menghasilkan output.
> Imporlah seperti contoh di atas untuk menggunakannya.

## Konsep Utama

- Mendefinisikan fungsi dengan parameter dan nilai `return`.
- Memvalidasi masukan dengan klausa penjaga (guard clauses) yang `return` lebih
  awal saat data tidak valid.
- Menggunakan `type()` dan pemeriksaan keanggotaan list (`in [...]`) untuk
  menerima beberapa tipe numerik.
- Menghitung diskon berbasis persentase dan mengembalikan hasil yang rapi.

## Lisensi

Dirilis di bawah [CC0 1.0](LICENSE), menempatkan karya ini ke dalam domain
publik.
