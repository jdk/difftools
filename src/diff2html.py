#!/usr/bin/env python

import sys

def htmlfixup(s):
    return s.replace('<','&lt;').replace('>','&gt;')

HTMLHEADER = """<html>
    <head>
        <title>%s</title>
        <style>
            div.diff {
                font-family: monospace;
                font-size: 12px;
                white-space: pre;
            }
            div.diff.add {
                color: #008800
            }
            div.diff.rem {
                color: #cc0000
            }
            div.diff.chunk_header {
                color: #990099
            }
            div.diff.header {
                color: #000088
            }
        </style>
    </head>
    <body>
"""

HTMLFOOTER = """    </body>
</html>
"""

### ENTRY ###
out = sys.stdout
inp = sys.stdin

cmdname = sys.argv.pop(0)
try:
    title = sys.argv.pop(0)
except:
    sys.stderr.write('Not enough Arguments\n')
    sys.exit(1)

out.write(HTMLHEADER % title)
for line in inp:
    line = line.rstrip('\n\r')
    out.write('        ')
    if line[0] == '-':
        out.write('<div class="diff rem">')
    elif line[0] == '+':
        out.write('<div class="diff add">')
    elif line[0] == '@':
        out.write('<div class="diff chunk_header">')
    elif line[0] == '=':
        out.write('<div class="diff header">')
    else:
        out.write('<div class="diff">')
    out.write(htmlfixup(line))
    out.write('</div>\n')

out.write(HTMLFOOTER)