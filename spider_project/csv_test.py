# #csv_writer
# import csv
# headers=['id','ordernum','date','product','price']
# rows=[(1001,'ph001','20170101','话费','50'),
#       (1002,'gm002','20170408','游戏','100'),
#       (1003,'ph003','20171009','话费','300')]
#
# with open('test.csv','w') as f:
#     f_csv=csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)

# #csv_reader_1
# import csv
#
# with open('test.csv','r') as f:
#     f_csv=csv.reader(f)
#     headers=next(f_csv)
#     print(headers)
#     for row in f_csv:
#         print(row)

# #csv_reader_2
# import csv
# from  collections import namedtuple
# with open('test.csv','r') as f:
#     f_csv=csv.reader(f)
#     headings=next(f_csv)
#     Row=namedtuple('Row',headings)
#     for r in f_csv:
#         row=Row(*r)
#         print(row.ordernum,row.date)
#         print(row)

# #csv_reader_3
# import csv
# with open('test.csv','r') as f:
#     f_csv=csv.DictReader(f)
#     for row in f_csv:
#         print(row.get('id'),row.get('ordernum'))
#         print(row)
