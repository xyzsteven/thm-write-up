import socket
import string

# Sesuaikan IP dengan IP Target Machine di TryHackMe
HOST = '10.49.158.174'
PORT = 1337

def solve():
    print(f"[*] Menghubungkan ke {HOST}:{PORT}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # 1. Terima pesan pembuka dari server
    data = s.recv(4096).decode()
    print("[*] Pesan dari server:\n" + data)

    # 2. Ekstrak string hex dari pesan server
    # Format pesan: "This XOR encoded text has flag 1: <hex_string>\n"
    hex_encoded = data.split('flag 1: ')[1].split('\n')[0].strip()
    ciphertext = bytes.fromhex(hex_encoded)

    # 3. Cari 4 karakter pertama dari key (Known Plaintext Attack)
    known_plaintext = b'THM{'
    key_part = ""
    for i in range(4):
        key_part += chr(ciphertext[i] ^ known_plaintext[i])
    
    print(f"[*] 4 Karakter pertama key ditemukan: {key_part}")

    # 4. Brute-force karakter ke-5 dari key
    possible_chars = string.ascii_letters + string.digits
    found_key = None
    flag_1 = ""

    print("[*] Mencari karakter ke-5...")
    for char in possible_chars:
        test_key = key_part + char
        decrypted = ""
        
        # Coba dekripsi ciphertext dengan test_key
        for i in range(len(ciphertext)):
            decrypted += chr(ciphertext[i] ^ ord(test_key[i % 5]))
        
        # Flag yang benar pasti diakhiri dengan '}'
        if decrypted.endswith('}'):
            found_key = test_key
            flag_1 = decrypted
            break

    if found_key:
        print(f"\n[+] KEY DITEMUKAN: {found_key}")
        print(f"[+] FLAG 1: {flag_1}")

        # 5. Kirim key ke server untuk mendapatkan Flag 2
        # Biasanya server mengirim prompt "What is the encryption key?"
        prompt = s.recv(1024).decode()
        
        print(f"[*] Mengirim key ke server...")
        s.sendall((found_key + '\n').encode())

        # 6. Terima Flag 2
        response = s.recv(4096).decode()
        print(f"\n[+] RESPON SERVER (FLAG 2):\n{response}")
    else:
        print("[-] Gagal menemukan key.")

    s.close()

if __name__ == '__main__':
    solve()
