#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""G�r ett program som skriver ut talen i m�ngden {1, 2, ..., 10500} i stigande ordning.

Om talet �r j�mnt delbart med 3 s� ska www. skrivas ut ist�llet f�r sj�lva talet.
Om talet �r j�mnt delbart med 5 s� ska lantmateriet skrivas ut ist�llet f�r sj�lva talet.
Om talet �r j�mnt delbart med 7 s� ska .se skrivas ut ist�llet f�r sj�lva talet.
Om talet �r j�mnt delbart med 3, 5 och 7 s� ska www.lantmateriet.se skrivas ut ist�llet f�r sj�lva talet.

Inga nyradstecken ska skrivas ut, utan allt ska skrivas ut p� en och samma rad.

Utskriften inleds enligt nedan:
1 2 www. (och s� vidare...)

Inget mellanrum som sista tecken.

MD5-summan av utskriften �r 402087a86f4fbd5d01d80baec13fddc5

Men vad �r SHA-1-summan? 

Ta med svaret i din ans�kan!
"""

import hashlib

string = ""
for n in range (1,10501):
	if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
		string += "www.lantmateriet.se"
	elif n % 3 == 0:
		string += "www."
	elif n % 5 == 0:
		string += "lantmateriet"
	elif n % 7 == 0:
		string += ".se"
	else:
		string += str(n)
	if n < 10500:
		string += " "
	

checksumToArchive = "402087a86f4fbd5d01d80baec13fddc5".upper()

checksum1 = hashlib.md5(string).hexdigest()
print checksum1
print checksum1.upper() == checksumToArchive.upper()

checksum1 = hashlib.sha1(string).hexdigest()

print checksum1


