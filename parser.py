#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 2018/5/27 8:29

import csv


def csv_reader():
    with open('stocks.csv') as f:
        f_csv = csv.DictReader(f)
        print('Symbol\tPrice\tDate\t\tTime\tChange\tVolume')
        for row in f_csv:
            print('%s\t\t%s\t%s\t%s\t%s\t%s' %
                  (row['Symbol'], row['Price'], row['Date'],
                   row['Time'], row['Change'], row['Volume']))


if __name__ == '__main__':
    csv_reader()
