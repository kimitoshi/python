#! /usr/bin/env python3
# renameDates.py - 米国式日付MM-DD-YYYYのファイル名を欧州式DD-MM-YYYYに書き換える

import shutil, os, re

#米国式日付のファイル名にマッチする正規表現を作る

date_pattern = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)


#TODO: カレンドディレクトリの全ファイルをループする
for amer_filename in  os.listdir('.'):
    mo = date_pattern.search(amer_filename)
    

    #TODO:日付のないファイルをスキップする。
    if mo == None:
        continue


    #TODO:ファイル名を部分分解する
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)


    #TODO:欧州式日付の部分分解する。
    euro_filename = before_part + day_part  +  '-' + month_part + '-' + \
                year_part + after_part


    #TODO:ファイル名を変更する。
    print('Renamming "{}" to "{}"...'.format(amer_filename, euro_filename))
    #shutil.move(amer_filename, euro_filename)




