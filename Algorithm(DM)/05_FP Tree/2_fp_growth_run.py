# encoding: utf8
from fp_growth import find_frequent_itemsets


ff=open("fp_list_1.txt", 'w')
if __name__ == '__main__':
    from optparse import OptionParser
    import csv

    p = OptionParser(usage='%prog data_file')
    p.add_option('-s', '--minimum-support', dest='minsup', type='int',
        help='Minimum itemset support (default: 2)')  ## 設定指令的option -s int(設定minimum support)
    p.set_defaults(minsup=2)

    options, args = p.parse_args()
    if len(args) < 1:
        p.error('must provide the path to a CSV file to read')

    f = open(args[0])
    try:
        for itemset, support in find_frequent_itemsets(csv.reader(f), options.minsup, True):
            if len(itemset) >= 5:
                printtext = ','.join(itemset) + " : " + str(support)
                ff.write(printtext+"\n")
    finally:
        f.close()
ff.close()