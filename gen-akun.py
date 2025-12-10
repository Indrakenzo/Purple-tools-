import random
import string

def banner_gen():
    print("========================================")
    print("   GENERATOR KOMBINASI (INDRA SOC)      ")
    print("   Output: separated_users.txt & pass.txt")
    print("========================================")

def generate_random_string(length):
    # Gabungan huruf dan angka
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def main():
    banner_gen()
    try:
        jumlah = int(input("Mau generate berapa akun bro? "))
    except ValueError:
        print("Masukin angka yang bener elah.")
        return

    users = []
    passwords = []

    print("\nSedang meracik data...")

    for i in range(jumlah):
        # Pola user: user_random
        user = "user_" + generate_random_string(5)
        # Pola pass: Pass_Random_Angka
        pwd = generate_random_string(10) + "!"
        
        users.append(user)
        passwords.append(pwd)

    # Simpan ke file terpisah
    with open("USERNAME.txt", "w") as f_user:
        for u in users:
            f_user.write(u + "\n")
            
    with open("PASSWORD.txt", "w") as f_pass:
        for p in passwords:
            f_pass.write(p + "\n")

    print(f"\n[SUKSES] {jumlah} data berhasil dibuat!")
    print("Cek file 'USERNAME.txt' dan 'PASSWORD.txt' di folder lu.")

if __name__ == "__main__":
    main()
