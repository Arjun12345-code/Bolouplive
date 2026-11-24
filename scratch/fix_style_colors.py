with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace all remaining emerald references
css = css.replace('var(--color-emerald)', 'var(--color-pink)')
css = css.replace('Teal (#0D94B6) to Emerald Mint (#13C091) Full-Screen Gradient Theme', 'Official BoloUp Brand Theme - Deep Midnight Purple (#100524), Violet (#8B3DFF), Neon Pink (#FF2D8D)')
css = css.replace('Teal-to-Green', 'BoloUp Purple-Violet')
css = css.replace('Teal-Green Glass', 'BoloUp Midnight Glass')
css = css.replace('Vibrant Teal-Emerald', 'BoloUp Vibrant Theme')
css = css.replace('rgba(19, 192, 145, 0.25)', 'rgba(139, 61, 255, 0.35)')

# 2. Update footer styling block
footer_block_old = """/* ==========================================================================
   16. Footer Component (footer.html)
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
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.footer-desc {
  color: var(--text-muted);
  font-size: 0.95rem;
  line-height: 1.7;
  max-width: 340px;
}

.footer-col h3 {
  color: var(--text-title);
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 20px;
  letter-spacing: -0.01em;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-links a {
  color: var(--text-body);
  font-size: 0.95rem;
  transition: var(--transition);
}

.footer-links a:hover {
  color: var(--color-pink);
  transform: translateX(3px);
  display: inline-block;
}

.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid rgba(139, 61, 255, 0.35);
  padding-top: 28px;
  color: var(--text-muted);
  font-size: 0.9rem;
  flex-wrap: wrap;
  gap: 16px;
}

.footer .brand-logo-icon,
.footer .brand-logo img {
  height: 36px !important;
  max-height: 36px !important;
  width: auto !important;
  max-width: 140px !important;
}"""

footer_block_new = """/* ==========================================================================
   16. Footer Component (footer.html) - 100% Full Width Edge-to-Edge BoloUp Theme
   ========================================================================== */
.elementor-location-footer,
.elementor-1719,
.elementor-1719.e-con,
.elementor-1719 .e-con,
.elementor-1719 .e-con-boxed,
.elementor-1719 .e-con-inner,
.elementor-1719 .elementor-widget-html,
.elementor-1719 .elementor-widget-container {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 100% !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  box-sizing: border-box !important;
  background-color: #0e041e !important;
  background: rgba(14, 4, 30, 0.98) !important;
  border: none !important;
  box-shadow: none !important;
}

.footer,
footer.footer,
.site-footer {
  position: relative !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 85px 0 35px !important;
  box-sizing: border-box !important;
  background-color: #0e041e !important;
  background: rgba(14, 4, 30, 0.98) !important;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  color: var(--text-body);
  border-top: 1px solid rgba(139, 61, 255, 0.45) !important;
  box-shadow: 0 -12px 40px rgba(0, 0, 0, 0.7), 0 0 25px rgba(139, 61, 255, 0.15) !important;
}

.footer .container {
  width: 100% !important;
  max-width: var(--max-width, 1200px) !important;
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
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.footer-desc {
  color: var(--text-muted);
  font-size: 0.95rem;
  line-height: 1.7;
  max-width: 360px;
}

.footer-col h3 {
  color: var(--text-title);
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 20px;
  letter-spacing: -0.01em;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-links a {
  color: var(--text-body);
  font-size: 0.95rem;
  transition: var(--transition);
}

.footer-links a:hover {
  color: var(--color-pink) !important;
  text-shadow: 0 0 12px rgba(244, 90, 200, 0.6);
  transform: translateX(4px);
  display: inline-block;
}

.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid rgba(139, 61, 255, 0.3) !important;
  padding-top: 28px;
  color: var(--text-muted);
  font-size: 0.9rem;
  flex-wrap: wrap;
  gap: 16px;
}

.footer .brand-logo-icon,
.footer .brand-logo img {
  height: 36px !important;
  max-height: 36px !important;
  width: auto !important;
  max-width: 140px !important;
}"""

if footer_block_old in css:
    css = css.replace(footer_block_old, footer_block_new)
    print("Replaced footer block successfully!")
else:
    print("WARNING: exact footer block not matched, searching by regex...")
    import re
    css = re.sub(r'/\* =+ \r?\n   16\. Footer Component.*?(?=\r?\n/\* =+ \r?\n   17\.|\Z)', footer_block_new + '\n\n', css, flags=re.DOTALL)
    print("Replaced footer block via regex!")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css successfully!")
