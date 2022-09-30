# CTF best practice

## Setup

This writeup assumes that you're using Kali Linux or in case you're not, that you at least know how to install the tools that Kali has installed by default. :)

### 1. Prepare wordlists

On Kali distros we have a selection of wordlists located in the `/usr/share/wordlists/` directory. A good general wordlist is `rockyou.txt`. To extract it to a new directory called `wordlist` in your home dir, you can run this one-liner:

`mkdir ~/wordlists;gunzip -c /usr/share/wordlists/rockyou.txt.gz > ~/wordlists/rockyou.txt`

Now you'll be ready to feed your `~/wordlists/rockyou.txt` wordlist to your cracking tools.

### 2. Install audacity

Audacity is an audio editor that can be useful in certain CTF challenges that hide data in audio files. You can install it with `sudo apt install audacity` or if it's not in your repository you can get it here `https://www.audacityteam.org/download/linux/`.

### 3. Install Nessus

I personally prefer the `WMAP` scanner in metasploit but Nessus has some more power behind it, though it requires registration and isn't free if you want to unlock all of its abilities. Go to `https://www.tenable.com/downloads/nessus` and download the package for your repository (likely the Kali x64 .deb file). Then install it with `sudo dpkg -i ~/Downloads/[filename].deb`. Now run `/bin/systemctl start nessusd.service` to start the nessus service and head over to the web interface that nessus gave you. Now pick `Nessus Essentials` for the free version and register to get your activation code.

### 4. Install Sherlock

Sherlock allows you to find social media accounts by usernames. Might be useful for certain creative CTF challenges. Install with:

`git clone https://github.com/sherlock-project/sherlock.git;cd sherlock;python3 -m pip install -r requirements.txt`

---

## Identification

### Find the file type of an unknown file

**Best practice:** Use the `file` command. This uses magicbytes to try to identify what kind of file it might be.

Alternatives:
* https://www.toolsley.com/file.html

### Find the hash type of an unknown hash

**Best practice:** Use the `hash-identifier` command. This comes preinstalled on Kali.

Alternatives:
* https://hashes.com/en/tools/hash_identifier

### Steganography/information hidden in pictures

**Best practice:** https://www.aperisolve.com/

Alternatives:
* Use the `exiftool` command to check an image for exif data.

### Check a file for audio data

**Best practice:** Import the file in `audacity` and check the spectrum analyzer.

Alternatives:
* https://www.dcode.fr/spectral-analysis

### Check a file for strings

**Best practice:** Use the `strings` command.

Alternatives:
* Ghidra (GUI tool)

### Find online accounts by username

**Best practice:** Use sherlock with `python3 sherlock username`.

Alternatives:
* Manually using google/bing/yandex/etc.

---

## Hacking

### Reverse a hashed password/string

**Best practice:** https://crackstation.net/

Alternatives:
* https://hashtoolkit.com/
* https://hashes.com/en/decrypt/hash
* https://md5.gromweb.com/
* Use `hashcat`

### Unzip a 'zipception' file that nests a zip inside a zip etc.

**Best practice:** Use the script provided in this repository at `/scripts/zipception.py`.

Alternatives:
* Lots of manual clicking... :)

### Scan a web application for vulnerabilities

**Best practice:** Start metasploit with `msfconsole`. Then start WMAP with `load wmap`. Now we add the site/ip we want to attack `wmap_sites -a http://127.0.0.1`. Next we'll add the actual web interface with `wmap_targets -t http://127.0.0.1/index.php`. Now we'll actually start the scan with `wmap_run -e`. Afterwards you can use `wmap_vulns -l` to list any found vulnerabilities. Now simply use these to attack the target.

Alternatives:
* OWASP zap (GUI tool)
* Nessus (GUI tool)

### SQL injection on a web service

**Best practice:** Use `sqlmap` to scan your target.

Alternatives:
* Manual sql injection with cheatsheets like https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/
* Burp Suite (GUI tool)

### Analyze or crack a binary file

**Best Practice:** Ghidra (GUI tool)

Alternatives:
* Use the `ltrace` command.

### Crack a password protected zip file

**Best Practice:** Run `fcrackzip -u -D -p ~/wordlists/rockyou.txt filename.zip`

Alternatives:
* None?