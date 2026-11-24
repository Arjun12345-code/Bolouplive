import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://pasteboard.co/IytyiyjE8e25.png', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, context=ctx) as resp:
        content = resp.read()
        ctype = resp.headers.get('content-type', '')
        print('Content type:', ctype, 'length:', len(content))
        if 'image' in ctype:
            with open('scratch/pasteboard.png', 'wb') as f:
                f.write(content)
            print('Saved direct image to scratch/pasteboard.png')
        else:
            html = content.decode('utf-8', errors='ignore')
            m = re.findall(r'<meta property="og:image" content="([^"]+)"', html)
            print('OG image matches:', m)
            if not m:
                m = re.findall(r'<img[^>]+src="([^"]+)"', html)
                print('Img tags:', m[:5])
            if m:
                target_img = m[0]
                if not target_img.startswith('http'):
                    target_img = 'https://pasteboard.co' + target_img
                print('Fetching image from:', target_img)
                req2 = urllib.request.Request(target_img, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req2, context=ctx) as r2:
                    with open('scratch/pasteboard.png', 'wb') as f2:
                        f2.write(r2.read())
                print('Saved image to scratch/pasteboard.png!')
except Exception as e:
    print('Error:', e)
