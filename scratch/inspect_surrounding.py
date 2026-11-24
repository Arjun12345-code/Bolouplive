import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://bolouplive.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

lines = html.splitlines()

print("--- Around Line 147 ---")
for i in range(max(0, 130), min(len(lines), 160)):
    print(f"{i+1}: {lines[i]}")

print("\n--- Around Line 891 ---")
for i in range(max(0, 875), min(len(lines), 905)):
    print(f"{i+1}: {lines[i]}")

