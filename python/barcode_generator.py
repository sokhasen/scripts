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
	# x^n-1...((x^n) - 1))
	EXPONENTIAL = 13;
	serialNumber = str(randint(10**(EXPONENTIAL - 1), (10**EXPONENTIAL) - 1))
	filename = str(datetime.timestamp(datetime.now()))
	barcodeProvider = 'ean13'
	EAN = barcode.get_barcode_class(barcodeProvider)
	generateBarcode(EAN, filename, serialNumber)

	""" default generate with svg in v.0.10
	EAN = barcode.get_barcode_class(barcodeProvider)
	ean = EAN(serialNumber)
	fullname = ean.save(filename)
	"""

	"""Or generate with png in v 0.4
		name = generate('EAN13', '5901234123457', output='barcode_svg')
		generate('EAN13', '5901234123457', writer=ImageWriter(), output='barcode')
	"""