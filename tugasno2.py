import string
abjad = string.printable

def enkripsi(pesan):
    global abjad

    key = int(input('Masukkan Key                : '))
    cipher = ''  # Menyimpan hasil enkripsi
    for i in pesan:
        if i in abjad:
            k = abjad.find(i)  # Menentukan indeks karakter
            k = (k + key) % len(abjad)  # Menggeser indeks dengan key
            cipher += abjad[k]
        else:
            cipher += i  # Tambahkan karakter non-abjad tanpa perubahan
    return cipher

def dekrip(cipher):
    global abjad

    key = int(input('Masukkan Key                : '))
    pesan = ''  # Menyimpan hasil dekripsi
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)  # Menentukan indeks karakter
            k = (k - key) % len(abjad)  # Menggeser indeks ke arah negatif dengan key
            pesan += abjad[k]
        else:
            pesan += i  # Tambahkan karakter non-abjad tanpa perubahan
    return pesan

if __name__ == '__main__':
    while True:  # Perulangan agar program terus berjalan
        print ('--------------------------- -------------')
        print('|-------- Rendi Akbar Firmansyah --------|')
        print ('--------------------------- -------------')

        option = int(input('1. Enkripsi\n2. Deskripsi\n3. Keluar\nPilih Option                : '))
        
        if option == 1:
            pesan = input('Masukkan Pesan (Plaintext)  : ')
            print('Pesan Terenkripsi           :', enkripsi(pesan))
            print("")  # Menambahkan baris kosong sebagai jarak setelah hasil
        
        elif option == 2:
            cipher = input('Masukkan Pesan (Chipertext) : ')
            print('Pesan Terdekripsi           :', dekrip(cipher))
            print("")  # Menambahkan baris kosong sebagai jarak setelah hasil
        
        elif option == 3:
            print("Terima kasih! Program selesai.")
            break  # Menghentikan perulangan dan keluar dari program
        
        else:
            print('Masukkan Option 1, 2, atau 3!')
            print("")  # Menambahkan baris kosong sebagai jarak setelah pesan error
