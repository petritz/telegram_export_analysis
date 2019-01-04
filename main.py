#!/usr/bin/env python3
"""
Telegram Data Analysis
Convert html files to .csv
"""

import sys
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import csv

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: ./convert.py [folder to convert]')
    sys.exit(1)

  # get files
  messages = check_folder(args[0])
  
  if len(messages) <= 0:
    print('No telegram export could be found. Please choose the directory with the messages.html file inside.')
    sys.exit(1)

  # fieldnames
  fieldnames = ['msgid', 'message']

  # create our csv writer
  csvFilePath = join(args[0], 'output.csv')
#  if isfile(csvFilePath):
#    answer = input('output.csv already exists. Do you want to override it? [y/n] ')
#    if answer != 'y':
#      sys.exit(1)

  with open(csvFilePath, 'w') as csvFile:
    csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
    csvWriter.writeheader()

    # now lets parse all of them
    for msgList in messages:
      data = parse_messages(args[0], msgList)
      break
      # save to csv
      for row in data:
        csvWriter.writerow(row)

"""
Reads directly from the messages.html file and pares its content to a list
of dictionaries.
"""
def parse_messages(path, msgList):
  fileName = 'messages'
  if msgList > 1:
    fileName += str(msgList)
  fileName += '.html'
  fullPath = join(path, fileName)
  with open(fullPath) as fp:
    soup = BeautifulSoup(fp, 'lxml', from_encoding='utf8')
    name = soup.find('div', class_='page_header')
    print('Chat \"' + name.text.strip() + '\" Part ' + str(msgList))

"""
Reads the given path and saves the files into the list.
But only allow .html files because they are the only interesting for us.
"""
def check_folder(path):
  files = []
  for f in listdir(path):
    if isfile(join(path, f)):
      if f.endswith('.html'):
        filename = f.split('.')[0]
        number = filename.split('messages')[1]
        if number == '':
          number = 1
        else:
          number = int(number)
        files.append(number)
  files.sort()
  return files

if __name__ == '__main__':
  main()
