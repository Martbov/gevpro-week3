#!usr/bin/python3.4

import sys
import xml.etree.ElementTree as ET

def main(argv):
	"""" Filters wrong data from an XML file """
	spontalXML = open((argv[1]), 'r')
	tree = ET.parse(spontalXML)
	spontalXML.close()
	
	root = tree.getroot()
	
	for point in root:
		f0_start = float(point.find('F0_START').text)
		f0_end = float(point.find('F0_END').text)
		bottom_hz = float(point.find('BOTTOM_HZ').text)
		top_hz = float(point.find('TOP_HZ').text)
		
		if not bottom_hz <= f0_start <= top_hz or not bottom_hz <= f0_end <= top_hz:
			root.remove(point)

	tree.write('spontalFilter.xml')

if __name__ == '__main__':
	main(sys.argv)