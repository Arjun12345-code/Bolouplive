import requests
import re

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

login_url = 'https://bolouplive.com/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
session.post(login_url, data={'log': 'irza', 'pwd': 'XEugcL8XpK#PH^ffs0O1%H6h', 'rememberme': 'forever'})

editor_url = 'https://bolouplive.com/wp-admin/theme-editor.php?file=functions.php'
r = session.get(editor_url)

nonce = re.search(r'name=["\']nonce["\'][^>]*value=["\']([^"\']+)["\']', r.text).group(1)
print("Nonce:", nonce)

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/scratch/original_functions.php', 'r', encoding='utf-8') as f:
    orig = f.read()

snippet = """
/*
 * Update Chaty Link Phone Number (08212868780 -> 082371383705)
 */
add_action('init', function() {
    $option = get_option('cht_social_Link');
    if (is_array($option) && isset($option['value']) && strpos($option['value'], '8212868780') !== false) {
        $option['value'] = str_replace('8212868780', '82371383705', $option['value']);
        update_option('cht_social_Link', $option);
    }
}, 1);
"""

new_content = orig.strip() + "\n" + snippet

payload = {
    'nonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'coinlye',
    'newcontent': new_content,
    'submit': 'Update File'
}

r_post = session.post('https://bolouplive.com/wp-admin/theme-editor.php', data=payload, headers={'Referer': editor_url})
print("Update response status:", r_post.status_code)
print("Update final URL:", r_post.url)
print("Has 'File edited successfully':", 'File edited successfully' in r_post.text or 'updated=true' in r_post.url)

