import barcode
from barcode.writer import ImageWriter
from barcode import generate
from datetime import datetime
from random import randint

def generateBarcode(provider: object, filename: str, serial: str) -> str:
	barcode = provider(serial, writer=ImageWriter())
	f = open(filename + '.png', 'wb')
	barcode.write(f)
	f.close()
	return filename + '.png'

if __name__ == '__main__':
	print(barcode.PROVIDED_BARCODES)
	filename = str(datetime.timestamp(datetime.now()))
	EXPONENTIAL = 13;
	# x^n-1...((x^n) - 1))
	serialNumber = str(randint(10**(EXPONENTIAL - 1), (10**EXPONENTIAL) - 1))
	EAN = barcode.get_barcode_class('ean13')
	generateBarcode(EAN, filename, serialNumber)

	# generate svg
	# ean = EAN(serialNumber)
	# fullname = ean.save(filename)

	# generate png
	# ean = EAN(serialNumber, writer=ImageWriter())
	# fullname = ean.save('ean13_barcode') v0.10
	# v0.4
	# f = open(filename + '.png', 'wb')
	# ean.write(f)
	# version 0.5
	# name = generate('EAN13', '5901234123457', output='barcode_svg')
	# generate('EAN13', '5901234123457', writer=ImageWriter(), output='barcode')