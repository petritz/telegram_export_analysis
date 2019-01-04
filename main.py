#!/user/bin/env python3
"""
Telegram Data Analysis
main entry file
"""

import sys

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: ./main.py [export folder]')
    sys.exit(1)

if __name__ == '__main__:
  main()
