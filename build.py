#! /usr/bin/env python3

#REQUIRES pandoc and (sometimes) deck2pdf in the path
#pandoc - http://johnmacfarlane.net/pandoc/
#deck2pdf - https://github.com/melix/deck2pdf
#TODO should rewrite the path to reveal for markdown files further down the hierarchy


import os
import sys

fileSuffix = '.md'
clearTuple = ('.html', '.docx', '.pdf')

def clearDirectory(dir):
    for file in os.listdir(dir):
        if file.endswith(clearTuple):
            os.remove(os.path.join(dir, file))

def buildDirectory(dir):
    for file in os.listdir(dir):
        if file.endswith(fileSuffix):
            print('Working on', file)
            fileNameWithoutSuffix = file[:-len(fileSuffix)]
            file = os.path.join(dir, file)
            revealFileName = os.path.join(dir, fileNameWithoutSuffix + '.html')
            html5FileName = os.path.join(dir, fileNameWithoutSuffix + '_html5.html' )
            docxFileName = os.path.join(dir, fileNameWithoutSuffix + '.docx')
            pdfFileName = os.path.join(dir, fileNameWithoutSuffix + '.pdf')
            webtexFileName = os.path.join(dir, fileNameWithoutSuffix + '_webtex.html')
            
            os.system('pandoc ' + '-s ' + file + ' -o ' + revealFileName + ' -t revealjs' + ' -V theme=moon')
            #os.system('pandoc ' + '-s ' + file + ' -o ' + html5FileName + ' -t html5')
            #os.system('pandoc ' + '-s ' + file + ' -o ' + docxFileName + ' -t docx')
            #os.system('pandoc ' + '-s ' + file + ' -o ' + pdfFileName + ' -t latex')
            #os.system(' deck2pdf.bat --profile=revealjs ' + revealFileName + ' ' + pdfFileName)
            #os.system('pandoc ' + '-s ' + file + ' -o ' + webtexFileName + ' --webtex')
            
            #pandoc.exe -t revealjs -s file -o htmlFileName -V theme=moon

clearDirectory('.')
buildDirectory('.')