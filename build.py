#! /usr/bin/env python3

#REQUIRES pandoc 
#pandoc - http://johnmacfarlane.net/pandoc/
#TODO should rewrite the path to reveal for markdown files further down the hierarchy

pdfReveal = False
purePdf   = False

import os
import sys
import time

from threading import Thread

import http.server
import socketserver

fileSuffix = '.md'
mdppFileSuffix = '.mdpp'
clearTuple = ('.html', '.docx', '.pdf')

PORT = 8000
if pdfReveal:
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)

def serverThread(port=8000):
    print( 'Starting httpServer at port', PORT);
    httpd.serve_forever()

def startServer(port=8000):
    t = Thread(target=serverThread, args=(port,))
    t.daemon = True
    t.start()

def clearDirectory(dir):
    for file in os.listdir(dir):
        if file.endswith(clearTuple):
            os.remove(os.path.join(dir, file))

def buildDirectory(dir, reveal=True, pdfReveal=False, purePdf=False):

    #process mdpp files to create md
    for file in os.listdir(dir):
        if file.endswith(mdppFileSuffix):
            print('Working on', file)
            fileNameWithoutSuffix = file[:-len(mdppFileSuffix)]
            file = os.path.join(dir, file)
            mdFileName = os.path.join(dir, fileNameWithoutSuffix + '.md')
            os.system('py C:\\Users\\shearer\\code\\markdown-pp\\markdown-pp.py ' + file + ' ' + mdFileName)

    #process md files
    for file in os.listdir(dir):
        if file.endswith(fileSuffix):
            print('Working on', file)
            fileNameWithoutSuffix = file[:-len(fileSuffix)]
            file = os.path.join(dir, file)
            revealFileName = os.path.join(dir, fileNameWithoutSuffix + '.html')
            html5FileName = os.path.join(dir, fileNameWithoutSuffix + '_html5.html' )
            docxFileName = os.path.join(dir, fileNameWithoutSuffix + '.docx')
            pdfFileName = os.path.join(dir, fileNameWithoutSuffix + '.pdf')
            purePdfFileName = os.path.join(dir, fileNameWithoutSuffix + '_pure.pdf')
            webtexFileName = os.path.join(dir, fileNameWithoutSuffix + '_webtex.html')
            
            if reveal:
                os.system('pandoc ' + '-s ' + file + ' -o ' + revealFileName + ' -t revealjs' + ' -V theme=sky --base-header-level=1 --section-divs --slide-level=2')
            #os.system('pandoc ' + '-s ' + file + ' -o ' + html5FileName + ' -t html5')
            #os.system('pandoc ' + '-s ' + file + ' -o ' + docxFileName + ' -t docx')
            if purePdf:
                os.system('pandoc ' + '-s ' + file + ' -o ' + purePdfFileName + ' -t latex')
            
            #pdf of reveal
            if pdfReveal:
                phantomString = 'phantomjs ./reveal.js/plugin/print-pdf/print-pdf.js ' + 'http://localhost:8000/' + fileNameWithoutSuffix + '.html' + '?print-pdf#/ ' + pdfFileName
                os.system(phantomString)
                
            #os.system('pandoc ' + '-s ' + file + ' -o ' + webtexFileName + ' --webtex')
            
            #pandoc.exe -t revealjs -s file -o htmlFileName -V theme=moon

clearDirectory('.')
if pdfReveal:
    startServer()
buildDirectory('.', pdfReveal=pdfReveal, purePdf=purePdf)
