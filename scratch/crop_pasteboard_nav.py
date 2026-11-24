from PIL import Image

im = Image.open(r'c:\Users\asus\Desktop\WordPress\Bolouplive\scratch\pasteboard.png')
w, h = im.size

# Let's crop Navigation column
# In pasteboard, Navigation is around x: 30% to 50%, y: 15% to 75%
crop_nav = im.crop((int(w * 0.32), int(h * 0.15), int(w * 0.52), int(h * 0.75)))
crop_nav.save(r'c:\Users\asus\Desktop\WordPress\Bolouplive\scratch\pasteboard_nav_col.png')
print("Cropped pasteboard nav col successfully!")

