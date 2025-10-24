#!/usr/bin/env python3
import re

page_headers = {
    'about.html': 'Hakkımızda',
    'contact.html': 'İletişim',
    'service.html': 'Hizmetlerimiz',
    'feature.html': 'Özellikler',
    'quote.html': 'Fiyat Teklifi',
    'team.html': 'Ekibimiz',
    'testimonial.html': 'Müşteri Yorumları',
    '404.html': 'Sayfa Bulunamadı',
}

for filename, turkish_title in page_headers.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Page Header başlığını Türkçe yap
        content = re.sub(
            r'<h1 class="display-4 text-white animated slideInDown mb-4">.*?</h1>',
            f'<h1 class="display-4 text-white animated slideInDown mb-4">{turkish_title}</h1>',
            content,
            count=1
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {filename} başlığı '{turkish_title}' olarak ayarlandı")
    except Exception as e:
        print(f"✗ {filename} hatası: {e}")

print("\n✓ Tüm sayfa başlıkları Türkçeye çevrildi!")
