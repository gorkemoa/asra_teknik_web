#!/usr/bin/env python3
import re

# index.html'den doğru navbar ve topbar yapısını al
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Topbar Start'tan Topbar End'e kadar olan bölümü çıkar
topbar_match = re.search(
    r'<!-- Topbar Start -->.*?<!-- Topbar End -->',
    index_content,
    re.DOTALL
)
topbar = topbar_match.group(0) if topbar_match else None

# Navbar Start'tan Navbar End'e kadar olan bölümü çıkar
navbar_match = re.search(
    r'<!-- Navbar Start -->.*?<!-- Navbar End -->',
    index_content,
    re.DOTALL
)
navbar = navbar_match.group(0) if navbar_match else None

if not topbar or not navbar:
    print("Topbar veya Navbar bulunamadı!")
    exit(1)

# Düzeltilmesi gereken dosyalar
files_to_fix = [
    'about.html', 'contact.html', 'service.html', 'feature.html',
    'quote.html', 'team.html', 'testimonial.html', '404.html'
]

for filename in files_to_fix:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Eski topbar ve navbar'ı kaldır ve yerine yenisini koy
        content = re.sub(
            r'<!-- Topbar Start -->.*?<!-- Topbar End -->',
            topbar,
            content,
            flags=re.DOTALL
        )
        
        content = re.sub(
            r'<!-- Navbar Start -->.*?<!-- Navbar End -->',
            navbar,
            content,
            flags=re.DOTALL
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {filename} düzeltildi")
    except Exception as e:
        print(f"✗ {filename} hatası: {e}")

print("\n✓ Tüm dosyalar düzeltildi!")
