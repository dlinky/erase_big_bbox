import copy
import os

import cv2
import labelimg_xml

original_dir = os.getcwd() + '/original/'

img_list = [_ for _ in os.listdir(original_dir) if _.endswith('.jpg')]
xml_list = [_ for _ in os.listdir(original_dir) if _.endswith('.xml')]

for page, img_filename in enumerate(xml_list):
    img = cv2.imread(original_dir + img_filename)
    title, table = labelimg_xml.read_xml(original_dir, xml_list[page])

    boxes_to_print = []
    for box in table[:]:
        size_of_bbox = box[3] + box[4] - box[2] - box[1]
        if size_of_bbox > 100:
            table.remove(box)
    labelimg_xml.write_xml(title, table, original_dir, xml_list[page])