#!/usr/bin/env python
# coding: utf-8

path_in = 'path'


import xml.etree.ElementTree as ET

tree = ET.parse(path_in)
root = tree.getroot()
    
nega_list = []
for anno in (root.iter ('Annotation')):
    if(anno.attrib["Id"] == "1") :
        for region in (anno.iter('Region')):
            Negative = int(region.get('NegativeROA'))
            if Negative > 0:
                nega_list.append(float(region.attrib['AreaMicrons']))     
                    
                        
viable_list = []
for anno in (root.iter ('Annotation')):
    if(anno.attrib["Id"] == "1") :
        for region in (anno.iter('Region')):
            Negative = int(region.get('NegativeROA'))
            if Negative == 0:
                viable_list.append(float(region.attrib['AreaMicrons']))
                    
                        
whole_list = []
for anno in (root.iter ('Annotation')):
    if(anno.attrib["Id"] == "3") :
        for region in (anno.iter('Region')):
             whole_list.append(float(region.attrib['AreaMicrons']))    


viable = sum(viable_list)
whole = sum(whole_list)
negative = sum(nega_list)
tumorburden = ((viable-negative)/whole)
  
print( 'tumor burden : ', tumorburden)

