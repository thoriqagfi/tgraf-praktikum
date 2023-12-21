# Praktikum 1

<img width="600" alt="image" src="https://github.com/thoriqagfi/tgraf-praktikum/assets/103252800/155ba72a-841b-40e3-b7a9-94cd2267d6cb">
<img width="600" alt="image" src="https://github.com/thoriqagfi/tgraf-praktikum/assets/103252800/cb5273fd-55bf-4f1a-a612-c08c5cd198bf">

## Jawab :

### Colab Link : https://colab.research.google.com/drive/1Zpr6a8mswKrPYaG9_VA79ptvpHAMy-q2?usp=sharing

### Video Demo : https://youtu.be/Xyg-RuKVWnw

### Source Code :

```
import math
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def compare(p1, p2):
  if p1[0] == p2[0]:
    return p1[1] > p2[1]
  return p1[0] < p2[0]

def buildTree(tree, pos, low, high, index, value):
    if index < low or index > high:
        return
    if low == high:
        tree[pos] = value
        return
    mid = (high + low) // 2


    if 2 * pos + 2 >= len(tree):
        tree.extend([0] * (2 * pos + 2 - len(tree) + 1))


    buildTree(tree, 2 * pos + 1, low, mid, index, value)
    buildTree(tree, 2 * pos + 2, mid + 1, high, index, value)
    tree[pos] = max(tree[2 * pos + 1], tree[2 * pos + 2])


def findMax(tree, pos, low, high, start, end):
  if low >= start and high <= end:
    return tree[pos]
  if start > high or end < low:
    return 0
  mid = (high + low) // 2
  return max(findMax(tree, 2 * pos + 1, low, mid, start, end),
      findMax(tree, 2 * pos + 2, mid + 1, high, start, end))


def findLIS(arr):
  n = len(arr)
  p = [(arr[i], i) for i in range(n)]
  p.sort(key=lambda x: (x[0], -x[1]))
  len_tree = 2 ** (math.ceil(math.sqrt(n)) + 1) - 1
  tree = [0] * len_tree
  for i in range(n):
    buildTree(tree, 0, 0, n - 1, p[i][1],
        findMax(tree, 0, 0, n - 1, 0, p[i][1]) + 1)
  return tree[0]


arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
print("The array is: " + str(arr))
print("The Length of the LIS is:", findLIS(arr))
```

### Output :

```
The array is: [4, 1, 13, 7, 0, 2, 8, 11, 3]
The Length of the LIS is: 4
```

### Penjelasan :

- Function to compare two pairs

```
def compare(p1, p2):
    if p1[0] == p2[0]:
        return p1[1] > p2[1]
    return p1[0] < p2[0]
```
Keterangan :
Untuk nilai yang sama, elemen dengan indeks lebih tinggi muncul lebih awal dalam sorted array. Ini untuk strictly increasing subsequence. Untuk increasing subsequence, indeks yang lebih rendah muncul lebih awal dalam sorted array.
Fungsi ini membandingkan dua parameter, `p1` dan `p2`, yang diasumsikan sebagai pasangan nilai. Fungsi mengembalikan nilai `True` jika elemen pertama dari `p1` sama dengan elemen pertama dari `p2` dan elemen kedua dari `p1` lebih besar dari elemen kedua dari `p2`. Jika elemen pertama tidak sama, maka fungsi mengembalikan nilai `True` jika elemen pertama dari `p1` kurang dari elemen pertama dari `p2`. Jadi, fungsi ini membandingkan pasangan nilai berdasarkan aturan yang disebutkan di atas.

- Function to build the entire Segment tree, the root of which contains the length of the LIS
```
def buildTree(tree, pos, low, high, index, value):
    if index < low or index > high:
        return
    if low == high:
        tree[pos] = value
        return
    mid = (high + low) // 2

    if 2 * pos + 2 >= len(tree):
        tree.extend([0] * (2 * pos + 2 - len(tree) + 1))

    buildTree(tree, 2 * pos + 1, low, mid, index, value)
    buildTree(tree, 2 * pos + 2, mid + 1, high, index, value)
    tree[pos] = max(tree[2 * pos + 1], tree[2 * pos + 2])
```

Keterangan :
Indeks adalah indeks asli dari elemen saat ini. Jika indeks tidak ada dalam rentang yang ditentukan, kembalikan saja. Jika rendah == tinggi, maka posisi saat ini harus diperbarui ke nilainya. Fungsi ini digunakan untuk membangun pohon segmen (segment tree) rekursif. Pohon segmen adalah struktur data yang digunakan untuk mempercepat operasi kueri terhadap rentang elemen dalam sebuah array. Fungsi menerima enam parameter: `tree` (array yang merepresentasikan pohon segmen), `pos` (posisi saat ini dalam pohon segmen), `low` (batas bawah rentang yang sedang diproses), `high` (batas atas rentang yang sedang diproses), `index` (indeks elemen yang akan diubah nilai), dan `value` (nilai baru yang akan diset pada indeks tersebut).
Jika `index` berada di luar rentang yang sedang diproses (`index < low` atau `index > high`), maka fungsi berhenti dan tidak melakukan apa-apa.
Jika `low` sama dengan `high`, ini berarti fungsi telah mencapai daun pohon segmen, dan nilai pada posisi `pos` dalam array `tree` diatur ke nilai `value`. Ini merupakan kasus dasar rekursi. Jika `low` tidak sama dengan `high`, hitung nilai tengah (`mid`) dari rentang yang sedang diproses.
Periksa apakah indeks `2 * pos + 2` melebihi panjang pohon segmen (`len(tree)`). Jika ya, perlu memperluas panjang array `tree` untuk menampung posisi tersebut. Rekursif memanggil `buildTree` untuk anak kiri (posisi `2 * pos + 1`) dengan rentang dari `low` hingga `mid`, dan untuk anak kanan (posisi `2 * pos + 2`) dengan rentang dari `mid + 1` hingga `high`.
Setelah kedua anak selesai diproses, nilai pada posisi `pos` diatur menjadi maksimum dari nilai anak kiri dan anak kanan (`tree[pos] = max(tree[2 * pos + 1], tree[2 * pos + 2])`). Fungsi ini membangun pohon segmen yang merepresentasikan array, dengan setiap simpul (node) menyimpan nilai maksimum dari rentang yang sesuai.

- Function to query the Segment tree and return the value for a given range
```
def findMax(tree, pos, low, high, start, end):
    if low >= start and high <= end:
        return tree[pos]
    if start > high or end < low:
        return 0
    mid = (high + low) // 2
    return max(findMax(tree, 2 * pos + 1, low, mid, start, end),
               findMax(tree, 2 * pos + 2, mid + 1, high, start, end))
```

Keterangan :
Query: Sama seperti fungsi kueri pohon Segmen. Jika rentang saat ini sepenuhnya berada di dalam rentang kueri, kembalikan nilai posisi saat ini. Jika di luar batas, kembalikan nilai minimum yaitu 0 dalam kasus ini. Tumpang tindih sebagian. Panggil findMax pada node anak secara rekursif dan kembalikan maksimal keduanya.
Fungsi `findMax` digunakan untuk melakukan kueri pada pohon segmen dan mengembalikan nilai maksimum dalam rentang tertentu. Berikut adalah penjelasan singkat tentang kode tersebut:
Fungsi menerima enam parameter: `tree` (array yang merepresentasikan pohon segmen), `pos` (posisi saat ini dalam pohon segmen), `low` (batas bawah rentang yang sedang diproses), `high` (batas atas rentang yang sedang diproses), `start` (batas bawah rentang kueri), dan `end` (batas atas rentang kueri).
Jika rentang yang sedang diproses sepenuhnya tercakup dalam rentang kueri (`low >= start` dan `high <= end`), maka kembalikan nilai pada posisi `pos` dalam array `tree`.
Jika rentang yang sedang diproses tidak bersinggungan dengan rentang kueri (`start > high` atau `end < low`), maka kembalikan 0 karena tidak ada tumpang tindih.
Jika rentang yang sedang diproses dan rentang kueri saling bersinggungan atau tumpang tindih, hitung nilai tengah (`mid`) dari rentang yang sedang diproses.
Rekursif memanggil `findMax` untuk anak kiri (posisi `2 * pos + 1`) dengan rentang dari `low` hingga `mid` dan untuk anak kanan (posisi `2 * pos + 2`) dengan rentang dari `mid + 1` hingga `high`.
Kembalikan nilai maksimum antara hasil kueri anak kiri dan anak kanan menggunakan fungsi `max`.
Fungsi ini memungkinkan untuk mencari nilai maksimum dalam rentang tertentu dalam pohon segmen yang telah dibangun sebelumnya.

- Function to find Longest Increasing Sequence

```
def findLIS(arr):
    n = len(arr)
    p = [(arr[i], i) for i in range(n)]
    p.sort(key=lambda x: (x[0], -x[1]))
    len_tree = 2 ** (math.ceil(math.sqrt(n)) + 1) - 1
    tree = [0] * len_tree
    for i in range(n):
        buildTree(tree, 0, 0, n - 1, p[i][1],
                  findMax(tree, 0, 0, n - 1, 0, p[i][1]) + 1)
    return tree[0]
```
Keterangan :
Array berpasangan menyimpan bilangan bulat dan indeks di p[i]. Mengurutkan array berdasarkan peningkatan urutan elemen. Menghitung panjang segment-tree. Menginisialisasi pohon dengan nol. Membangun segment-tree, simpul akarnya berisi panjang LIS untuk n elemen.
Fungsi `findLIS` (Longest Increasing Subsequence) digunakan untuk mencari panjang maksimum dari subsequence yang terurut secara ascending dalam sebuah array. Berikut adalah penjelasan singkat kode tersebut:
Buat list `p` yang berisi pasangan nilai `(arr[i], i)` untuk setiap elemen dalam array `arr`. Ini dilakukan untuk mempertahankan informasi tentang nilai dan indeks setiap elemen.
Urutkan list `p` berdasarkan nilai elemen pertamanya (nilai dari `arr[i]`) secara ascending. Jika ada nilai yang sama, urutkan secara descending berdasarkan indeks kedua (`-x[1]`).
Hitung panjang minimum yang diperlukan untuk menyimpan pohon segmen dengan menggunakan `len_tree`. Panjang ini dihitung berdasarkan ukuran array asli.
Inisialisasikan array `tree` dengan panjang yang telah dihitung, dan isi semua elemennya dengan nilai 0.
Iterasi melalui setiap elemen `p` (pasangan nilai dan indeks) dan gunakan fungsi `buildTree` untuk membangun pohon segmen. Nilai yang disimpan diatur ke nilai dari fungsi `findMax` yang mengembalikan panjang maksimum subsequence yang dihasilkan sampai elemen saat ini.
Kembalikan nilai di posisi 0 dalam array `tree`, yang akan berisi panjang maksimum dari subsequence yang terurut secara ascending.
Fungsi ini menggunakan pohon segmen untuk menghitung panjang maksimum subsequence yang terurut secara ascending dari array asli.

- Sequence of Number of Array and print the Length of the LIS\
```
arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
print("The array is: " + str(arr))
print("The Length of the LIS is:", findLIS(arr))
```
Keterangan :
Sesuai dengan soal praktikum yang diberikan. Dideklarasikan array yang berisi urutan bilangan : 4, 1, 13, 7, 0, 2, 8, 11, 3. Selanjutnya Array tersebut akan di cetak pada output dan Length dari Longest Increasing Subsequence dari urutan bilangan tersebut adalah 4.
