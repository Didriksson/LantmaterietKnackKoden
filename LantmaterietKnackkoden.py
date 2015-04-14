#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib, base64

code = "R8O2ciBldHQgcHJvZ3JhbSBzb20gc2tyaXZlciB1dCB0YWxlbiBpIG3DpG5nZGVuIHsxLCAyLCAu Li4sIDEwNTAwfSBpIHN0aWdhbmRlIG9yZG5pbmcuCgpPbSB0YWxldCDDpHIgasOkbW50IGRlbGJh"\
"cnQgbWVkIDMgc8OlIHNrYSB3d3cuIHNrcml2YXMgdXQgaXN0w6RsbGV0IGbDtnIgc2rDpGx2YSB0 YWxldC4KT20gdGFsZXQgw6RyIGrDpG1udCBkZWxiYXJ0IG1lZCA1IHPDpSBza2EgbGFudG1hdGVy"\
"aWV0IHNrcml2YXMgdXQgaXN0w6RsbGV0IGbDtnIgc2rDpGx2YSB0YWxldC4KT20gdGFsZXQgw6Ry IGrDpG1udCBkZWxiYXJ0IG1lZCA3IHPDpSBza2EgLnNlIHNrcml2YXMgdXQgaXN0w6RsbGV0IGbD"\
"tnIgc2rDpGx2YSB0YWxldC4KT20gdGFsZXQgw6RyIGrDpG1udCBkZWxiYXJ0IG1lZCAzLCA1IG9j aCA3IHPDpSBza2Egd3d3LmxhbnRtYXRlcmlldC5zZSBza3JpdmFzIHV0IGlzdMOkbGxldCBmw7Zy"\
"IHNqw6RsdmEgdGFsZXQuCgpJbmdhIG55cmFkc3RlY2tlbiBza2Egc2tyaXZhcyB1dCwgdXRhbiBh bGx0IHNrYSBza3JpdmFzIHV0IHDDpSBlbiBvY2ggc2FtbWEgcmFkLgoKVXRza3JpZnRlbiBpbmxl"\
"ZHMgZW5saWd0IG5lZGFuOgoxIDIgd3d3LiAob2NoIHPDpSB2aWRhcmUuLi4pCgpJbmdldCBtZWxs YW5ydW0gc29tIHNpc3RhIHRlY2tlbi4KCk1ENS1zdW1tYW4gYXYgdXRza3JpZnRlbiDDpHIgNDAy"\
"MDg3YTg2ZjRmYmQ1ZDAxZDgwYmFlYzEzZmRkYzUKCk1lbiB2YWQgw6RyIFNIQS0xLXN1bW1hbj8g CgpUYSBtZWQgc3ZhcmV0IGkgZGluIGFuc8O2a2FuIQo="

decoded = base64.b64decode(code)

print decoded
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

checksum1 = hashlib.sha1(string).hexdigest().upper()

print "SHA-1 värde: ",checksum1


