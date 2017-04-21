#!/usr/bin/python

import os
import fileinput
import csv
from collections import Counter

EXCEL_PATH="/root/export.csv"

dir_file = r"/root/tmp.txt"
domain_list = ['d3g.qq.com','msg.71.am']
urls = []

def processLog(dir_file,domain):
    for line in fileinput.input(dir_file):
        line_list=line.split()
        line_domain=line_list[6]
        if line_domain == domain:
            url=''.join(line_list[-2:])
            urls.append(url)

def list_group(urls):
    count = Counter(urls)
    resu = count.most_common()
    return resu

def export_excel(resu):
    with open('%s' % (EXCEL_PATH), 'wb') as csvfile:
        csv_writer = csv.writer(csvfile,dialect='excel')
        for item in resu:
            csv_writer.writerow(item)
    


if __name__=='__main__':
    for domain in domain_list:
        processLog(dir_file,domain)
    resu = list_group(urls)
    export_excel(resu)
