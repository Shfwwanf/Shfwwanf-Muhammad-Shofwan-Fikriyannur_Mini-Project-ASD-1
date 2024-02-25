class Produk:
    def __init__(self, nama, harga, stok, merek, kategori):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.merek = merek
        self.kategori = kategori

    def __str__(self):
        return f"Nama: {self.nama}\nHarga: Rp{self.harga:,}\nStok: {self.stok}\nMerek: {self.merek}\nKategori: {self.kategori}"


class KatalogProduk:
    def __init__(self):
        self.produk = []

    def create(self, produk):
        self.produk.append(produk)

    def read(self):
        for produk in self.produk:
            print(produk)
            print()

    def update(self, nama, produk_baru):
        for produk in self.produk:
            if produk.nama == nama:
                produk.nama = produk_baru.nama
                produk.harga = produk_baru.harga
                produk.stok = produk_baru.stok
                produk.merek = produk_baru.merek
                produk.kategori = produk_baru.kategori
                break

    def delete(self, nama):
        for produk in self.produk:
            if produk.nama == nama:
                self.produk.remove(produk)
                break

def main():
    katalog = KatalogProduk()

    produk_baru = [
        Produk("AOC 27G4 Gaming Monitor", 2678000, 5, "AOC", "Monitor Gaming"),
        Produk("Intel Core i5 13400F", 3500000, 3, "INTEL", "Processor"),
        Produk("LENOVO Legion 9i 16IRX8", 76999000, 2, "LENOVO", "Laptop Gaming"),
        Produk("ASUS ROG Zephyrus G16 GU603ZU", 24199000, 4, "ASUS", "Laptop Gaming"),
        Produk("NVIDIA GeForce RTX 3060", 4475000, 4, "GIGABYTE", "Vga Card"),
        Produk("AMD Ryzen 5 5600G", 2179000, 5, "AMD", "Processor"),
    ]

    for produk in produk_baru:
        katalog.create(produk)

    while True:
        print("\n--- Toko Komputer ---")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Keluar")

        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            nama_produk = input("Masukkan nama produk: ")
            harga_produk = int(input("Masukkan harga produk: "))
            stok_produk = int(input("Masukkan stok produk: "))
            merek_produk = input("Masukkan merek produk: ")
            kategori_produk = input("Masukkan kategori produk: ")

            produk_baru = Produk(nama_produk, harga_produk, stok_produk, merek_produk, kategori_produk)
            katalog.create(produk_baru)

        elif pilihan == 2:
            print("Daftar Produk:")
            katalog.read()

        elif pilihan == 3:
            nama_produk = input("Masukkan nama produk yang ingin diubah: ")

            nama_baru = input("Masukkan nama baru: ")
            harga_baru = int(input("Masukkan harga baru: "))
            stok_baru = int(input("Masukkan stok baru: "))
            merek_baru = input("Masukkan merek baru: ")
            kategori_baru = input("Masukkan kategori baru: ")

            produk_baru = Produk(nama_baru, harga_baru, stok_baru, merek_baru, kategori_baru)
            katalog.update(nama_produk, produk_baru)

        elif pilihan == 4:
            nama_produk = input("Masukkan nama produk yang ingin dihapus: ")
            katalog.delete(nama_produk)

        elif pilihan == 5:
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
