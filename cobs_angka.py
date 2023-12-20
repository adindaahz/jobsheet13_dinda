import random

def game_menebak_angka():
    secret_number = random.randint(1, 100)  # Angka acak antara 1 dan 100
    guess_limit = 15  # Batas jumlah tebakan
    guess_count = 0  # Inisialisasi jumlah tebakan

    print("Selamat datang di Game Menebak Angka!")
    print(f"Tebak angka antara 1 dan 100. Kamu memiliki {guess_limit} kesempatan.")

    while guess_count < guess_limit:
        try:
            guess = int(input("Tebakanmu: "))
        except ValueError:
            print("Masukkan angka valid.")
            continue

        guess_count += 1

        if guess == secret_number:
            print(f"Selamat! Kamu menebak angka dengan benar dalam {guess_count} tebakan.")
            break
        elif guess < secret_number:
            print("Tebakan terlalu rendah. Coba lagi.")
        else:
            print("Tebakan terlalu tinggi. Coba lagi.")

    if guess_count == guess_limit:
        print(f"Maaf, kamu habis kesempatan. Angka yang benar adalah {secret_number}.")

if __name__ == "__main__":
    game_menebak_angka()
