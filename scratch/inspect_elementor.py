import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import json
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# Login
login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
data = urllib.parse.urlencode({'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=data, headers={'User-Agent': 'Mozilla/5.0'}))

admin_req = urllib.request.Request('https://bolouplive.com/wp-admin/', headers={'User-Agent': 'Mozilla/5.0'})
with opener.open(admin_req) as resp:
    admin_html = resp.read().decode('utf-8', errors='ignore')

nonce = re.search(r'wpApiSettings\s*=\s*\{.*?"nonce":"([^"]+)".*?\}', admin_html).group(1)

# Check custom post types or elementor_library
lib_req = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/types', headers={
    'User-Agent': 'Mozilla/5.0',
    'X-WP-Nonce': nonce
})
with opener.open(lib_req) as resp:
    types = json.loads(resp.read().decode('utf-8'))
    print("Types:", list(types.keys()))

# Check elementor library posts
if 'elementor_library' in types:
    el_req = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/elementor_library', headers={
        'User-Agent': 'Mozilla/5.0',
        'X-WP-Nonce': nonce
    })
    try:
        with opener.open(el_req) as resp:
            el_posts = json.loads(resp.read().decode('utf-8'))
            print("Elementor library posts:")
            for p in el_posts:
                print(f"ID: {p['id']}, Title: {p['title']['rendered']}, Type: {p.get('type')}")
    except Exception as e:
        print("EL library error:", e)

# Check page 648 meta
p_req = urllib.request.Request('https://bolouplive.com/wp-json/wp/v2/pages/648?context=edit', headers={
    'User-Agent': 'Mozilla/5.0',
    'X-WP-Nonce': nonce
})
with opener.open(p_req) as resp:
    page_data = json.loads(resp.read().decode('utf-8'))
    meta = page_data.get('meta', {})
    print("_elementor_edit_mode:", meta.get('_elementor_edit_mode'))
    print("_elementor_template_type:", meta.get('_elementor_template_type'))
    el_data = meta.get('_elementor_data')
    if el_data:
        print("el_data length:", len(el_data))
        try:
            parsed = json.loads(el_data)
            print("el_data parsed structure:", len(parsed), "elements")
            # print widget types
            def find_widgets(elements):
                w = []
                for el in elements:
                    if 'widgetType' in el:
                        w.append(el['widgetType'])
                    if 'elements' in el:
                        w.extend(find_widgets(el['elements']))
                return w
            print("Widgets:", find_widgets(parsed))
        except Exception as e:
            print("Error parsing el_data:", e)

