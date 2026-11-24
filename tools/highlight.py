#!/usr/bin/env python3
# Light syntax highlighting of the Java examples in index.html, with no JavaScript: it puts
# <span class="k|t|s|n|c"> around keywords, types (names that start with a capital letter),
# strings, numbers and comments in every <pre><code> block
# that starts with "import " (Java). Run it after an example changes:
#     python3 -I tools/highlight.py index.html            rewrites the file in place
#     python3 -I tools/highlight.py index.html OUT.html   writes OUT.html
# It first removes the spans it made before, so a second run gives the same file.
# The colours are in index.html's CSS (pre .k, .t, .s, .n, .c).
# Created 2026-11-24 by Frans Lundberg.
import html, re, sys

KEYWORDS = set("""abstract assert boolean break byte case catch char class const continue
default do double else enum extends final finally float for goto if implements import
instanceof int interface long native new package private protected public return short
static strictfp super switch synchronized this throw throws transient try var void volatile
while true false null record yield""".split())

TOKEN = re.compile(r'(?P<c>//[^\n]*|/\*.*?\*/)|(?P<s>"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])\')'
                   r'|(?P<w>[A-Za-z_$][A-Za-z0-9_$]*)|(?P<n>\b\d[\d_]*(?:\.\d+)?[LlFfDd]?\b)', re.S)
BLOCK = re.compile(r'(<pre><code>)(.*?)(</code></pre>)', re.S)
OLD = re.compile(r'<span class="[ktsnc]">(.*?)</span>', re.S)

def color(code):
    out, i = [], 0
    for m in TOKEN.finditer(code):
        out.append(html.escape(code[i:m.start()], quote=False))
        kind = m.lastgroup
        text = html.escape(m.group(), quote=False)
        if kind == 'w':
            w = m.group()
            if w in KEYWORDS:
                out.append('<span class="k">%s</span>' % text)
            elif w[0].isupper():
                out.append('<span class="t">%s</span>' % text)
            else:
                out.append(text)
        else:
            out.append('<span class="%s">%s</span>' % (kind, text))
        i = m.end()
    out.append(html.escape(code[i:], quote=False))
    return ''.join(out)

def block(m):
    inner = OLD.sub(r'\1', m.group(2))
    code = html.unescape(inner)
    if not code.startswith('import '):
        return m.group(1) + inner + m.group(3)
    return m.group(1) + color(code) + m.group(3)

src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else src
text = open(src, encoding='utf-8').read()
open(dst, 'w', encoding='utf-8').write(BLOCK.sub(block, text))
