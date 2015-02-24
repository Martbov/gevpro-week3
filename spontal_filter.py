#!usr/bin/python3.4

import sys
import xml.etree.ElementTree as ET



def main(argv):
	spontalXML = open((argv[1]), 'r')
	spontalFilter = open('spontal_filtered.xml', 'w')
	tree = ET.parse(spontalXML)
	tree.write(spontalFilter, encoding="unicode", xml_declaration=True)
	spontalXML.close()
	filterTree = ET.parse(spontalFilter)
	root = filterTree.getroot()
	
	for point in root.findall('POINT'):
		f0_start = point.find('F0_START').text
		f0_end = point.find('F0_END').text
		bottom_hz = point.find('BOTTOM_HZ').text
		top_hz = point.find('TOP_HZ').text
		print(f0_start, f0_end, bottom_hz, top_hz)
		
		#if bottom_hz <= f0_start and f0_end <= top_hz:

		
			

if __name__ == '__main__':
	main(sys.argv)