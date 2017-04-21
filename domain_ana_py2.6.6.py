#!/usr/bin/python

import os
import fileinput
import csv
#from collections import Counter

EXCEL_PATH="/data/export.csv"

dir_file = r"/data/tmp.txt"
domain_list = ['a.woniu.com','uri6.com']
urls = []

def processLog(dir_file,domain):
    for line in fileinput.input(dir_file):
        line_list=line.split()
        try:
            line_domain=line_list[6]
        except IndexError, e:
            print 'warn:', e
            continue
        if line_domain == domain:
            url=''.join(line_list[-2:])
            urls.append(url)

def list_group(urls):
    data_set = set(urls)
    count_list = []
    for item in data_set:
        count_list.append((item,urls.count(item)))
    count_list_sort = sorted(count_list,key=lambda x:x[1],reverse=True)
    return count_list_sort

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
