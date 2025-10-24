#!/usr/bin/env python3
import re

files_config = {
    'index.html': 'index.html',
    'about.html': 'about.html',
    'contact.html': 'contact.html',
    'service.html': 'service.html',
    'feature.html': 'feature.html',
    'quote.html': 'quote.html',
    'team.html': 'team.html',
    'testimonial.html': 'testimonial.html',
    '404.html': '404.html',
}

nav_links = {
    'index.html': ('Anasayfa', 'index.html'),
    'about.html': ('Hakkımızda', 'about.html'),
    'service.html': ('Hizmetlerimiz', 'service.html'),
    'contact.html': ('İletişim', 'contact.html'),
}

for filename in files_config.keys():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tüm nav-link active sınıflarını kaldır
        content = re.sub(
            r'class="nav-item nav-link active"',
            'class="nav-item nav-link"',
            content
        )
        
        # Bu dosya için doğru linke active ekle
        if filename in ['index.html', 'about.html', 'contact.html', 'service.html']:
            link_text, link_file = nav_links[filename]
            # Doğru linke active class ekle
            content = re.sub(
                f'href="{link_file}" class="nav-item nav-link"',
                f'href="{link_file}" class="nav-item nav-link active"',
                content
            )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {filename} nav linkler düzeltildi")
    except Exception as e:
        print(f"✗ {filename} hatası: {e}")

print("\n✓ Tüm nav linkler ayarlandı!")
