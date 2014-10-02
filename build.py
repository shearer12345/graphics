#! /usr/bin/env python3

#REQUIRES pandoc and (sometimes) deck2pdf in the path
#pandoc - http://johnmacfarlane.net/pandoc/
#deck2pdf - https://github.com/melix/deck2pdf
#TODO should rewrite the path to reveal for markdown files further down the hierarchy


import os
import sys
import time

from threading import Thread

import http.server
import socketserver

fileSuffix = '.md'
clearTuple = ('.html', '.docx', '.pdf')

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

serverThreads = []

def serverThread(port=8000):
    print( 'Starting httpServer at port', PORT);
    httpd.serve_forever()

def startServer(threadList, port=8000):
    t = Thread(target=serverThread, args=(port,))
    threadList += [t]
    t.daemon = True
    t.start()

def stopServer():
    print( 'XXX - Stopping httpServer' );
         
def clearDirectory(dir):
    for file in os.listdir(dir):
        if file.endswith(clearTuple):
            os.remove(os.path.join(dir, file))

def buildDirectory(dir, reveal=True, pdfReveal=False):
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
            
            if reveal:
                os.system('pandoc ' + '-s ' + file + ' -o ' + revealFileName + ' -t revealjs' + ' -V theme=moon')
            #os.system('pandoc ' + '-s ' + file + ' -o ' + html5FileName + ' -t html5')
            #os.system('pandoc ' + '-s ' + file + ' -o ' + docxFileName + ' -t docx')
            #os.system('pandoc ' + '-s ' + file + ' -o ' + pdfFileName + ' -t latex')
            
            #pdf of reveal
            if pdfReveal:
                phantomString = 'phantomjs ./reveal.js/plugin/print-pdf/print-pdf.js ' + 'http://localhost:8000/' + fileNameWithoutSuffix + '.html' + '?print-pdf#/ ' + pdfFileName
                os.system(phantomString)
                
            #os.system('pandoc ' + '-s ' + file + ' -o ' + webtexFileName + ' --webtex')
            
            #pandoc.exe -t revealjs -s file -o htmlFileName -V theme=moon

clearDirectory('.')
startServer(threadList = serverThreads)
time.sleep(2)
buildDirectory('.', pdfReveal=True)
stopServer()