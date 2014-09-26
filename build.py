#! /usr/bin/env python3
import os
import sys

fileSuffix = '.md'
clearTuple = ('.html', '.docx', '.pdf')

for file in os.listdir('.'):
    if file.endswith(clearTuple):
        os.remove(file)

for file in os.listdir('.'):
    if file.endswith(fileSuffix):
        print('Working on', file)
        fileNameWithoutSuffix = file[:-len(fileSuffix)]
        revealFileName = fileNameWithoutSuffix + '.html'
        html5FileName = fileNameWithoutSuffix + '_html5.html' 
        docxFileName = fileNameWithoutSuffix + '.docx'
        pdfFileName = fileNameWithoutSuffix + '.pdf'
        webtexFileName = fileNameWithoutSuffix + '_webtex.html'
        
        os.system('pandoc ' + '-s ' + file + ' -o ' + revealFileName + ' -t revealjs' + ' -V theme=moon')
        #os.system('pandoc ' + '-s ' + file + ' -o ' + html5FileName + ' -t html5')
        #os.system('pandoc ' + '-s ' + file + ' -o ' + docxFileName + ' -t docx')
        #os.system('pandoc ' + '-s ' + file + ' -o ' + pdfFileName + ' -t latex')
        #os.system('pandoc ' + '-s ' + file + ' -o ' + webtexFileName + ' --webtex')
        
        #pandoc.exe -t revealjs -s file -o htmlFileName -V theme=moon
