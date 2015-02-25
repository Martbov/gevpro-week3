#!usr/bin/python3.4

import sys
import xml.etree.ElementTree as ET



def main(argv):
	spontalXML = open((argv[1]), 'r')
	spontalFilter = open('spontal_filtered.xml', 'w')
	tree = ET.parse(spontalXML)
	tree.write(spontalFilter, encoding="unicode", xml_declaration=True)
	spontalXML.close()
	
	root = tree.getroot()
	
	for point in root.iter('POINT'):
		f0_start = float(point.find('F0_START').text)
		f0_end = float(point.find('F0_END').text)
		bottom_hz = float(point.find('BOTTOM_HZ').text)
		top_hz = float(point.find('TOP_HZ').text)
		print(f0_start, f0_end, bottom_hz, top_hz)
		
		if not bottom_hz <= f0_start <= top_hz and bottom_hz <= f0_end <= top_hz:
			root.remove(point)


if __name__ == '__main__':
	main(sys.argv)