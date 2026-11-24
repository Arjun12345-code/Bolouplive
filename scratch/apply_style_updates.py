with open('c:/Users/asus/Desktop/WordPress/Bolouplive/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace green/emerald/teal colors with BoloUp brand colors (Magenta #FF2D8D, Violet #8B3DFF, Pink #F45AC8)
replacements = [
    # Badges and highlights
    ('rgba(19, 192, 145, 0.18)', 'rgba(255, 45, 141, 0.18)'),
    ('rgba(19, 192, 145, 0.45)', 'rgba(255, 45, 141, 0.45)'),
    ('rgba(19, 192, 145, 0.5)', 'rgba(255, 45, 141, 0.5)'),
    ('rgba(13, 148, 182, 0.35)', 'rgba(139, 61, 255, 0.35)'),
    ('rgba(13, 148, 182, 0.6)', 'rgba(139, 61, 255, 0.6)'),
    ('rgba(19, 192, 145, 0.15)', 'rgba(139, 61, 255, 0.18)'),
    ('rgba(19, 192, 145, 0.35)', 'rgba(139, 61, 255, 0.35)'),
    ('rgba(19, 192, 145, 0.22)', 'rgba(255, 45, 141, 0.22)'),
    ('rgba(19, 192, 145, 0.3)', 'rgba(255, 45, 141, 0.3)'),
    ('rgba(19, 192, 145, 0.7)', 'rgba(255, 45, 141, 0.7)'),
    ('rgba(19, 192, 145, 0.2)', 'rgba(139, 61, 255, 0.2)'),
    ('rgba(19, 192, 145, 0.6)', 'rgba(255, 45, 141, 0.6)'),
    ('rgba(19, 192, 145, 0.4)', 'rgba(255, 45, 141, 0.4)'),
    ('rgba(19, 192, 145, 0.25)', 'rgba(139, 61, 255, 0.25)'),
    ('var(--color-emerald)', 'var(--color-pink)'),
    ('var(--color-teal)', 'var(--color-violet)'),
    ('#13C091', '#FF2D8D'),
    ('#0D94B6', '#8B3DFF')
]

for old, new in replacements:
    css = css.replace(old, new)

# Update footer CSS for full width and 4 columns
old_footer_css = """/* ==========================================================================
   16. Footer Component (footer.html) - Matches Header Glass Theme
   ========================================================================== */
.footer,
footer.footer,
.site-footer,
.elementor-location-footer {
  width: 100% !important;
  max-width: 100% !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  box-sizing: border-box !important;
  position: relative;
  background-color: #0e041e !important;
  background: rgba(16, 6, 36, 0.95) !important;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  color: var(--text-body);
  border-top: 1px solid rgba(139, 61, 255, 0.35);
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.4);
  padding: 80px 0 35px;
}

.footer .container {
  width: 100% !important;
  max-width: var(--max-width);
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: 24px !important;
  padding-right: 24px !important;
  box-sizing: border-box !important;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.6fr 1.2fr 1.2fr;
  gap: 48px;
  margin-bottom: 56px;
}"""

new_footer_css = """/* ==========================================================================
   16. Footer Component (footer.html) - Full-Bleed BoloUp Midnight Brand Theme
   ========================================================================== */
.elementor-location-footer,
.elementor-location-footer .e-con,
.elementor-location-footer .e-con-boxed,
.elementor-location-footer .e-con-full,
.elementor-location-footer .e-con-inner,
.elementor-location-footer .elementor-widget-html,
.elementor-1719,
.elementor-1719 .e-con,
.elementor-1719 .e-con-boxed,
.elementor-1719 .e-con-full,
.elementor-1719 .e-con-inner,
.elementor-1719 .elementor-widget-html {
  width: 100% !important;
  max-width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  box-sizing: border-box !important;
}

.footer,
footer.footer,
.site-footer,
.elementor-location-footer {
  width: 100% !important;
  max-width: 100% !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  box-sizing: border-box !important;
  position: relative;
  background-color: var(--color-bg-deep) !important;
  background: rgba(10, 3, 22, 0.98) !important;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  color: var(--text-body);
  border-top: 1px solid rgba(139, 61, 255, 0.35);
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.4);
  padding: 80px 0 35px;
}

.footer .container {
  width: 100% !important;
  max-width: var(--max-width);
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: 24px !important;
  padding-right: 24px !important;
  box-sizing: border-box !important;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1.2fr;
  gap: 48px;
  margin-bottom: 56px;
}"""

if old_footer_css in css:
    css = css.replace(old_footer_css, new_footer_css)
    print("Replaced footer CSS block")
else:
    print("Could not find exact old_footer_css block, searching...")

with open('c:/Users/asus/Desktop/WordPress/Bolouplive/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated c:/Users/asus/Desktop/WordPress/Bolouplive/style.css successfully")

