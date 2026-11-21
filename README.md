# Psikodinamik Psikiyatri Okuma Rehberi

Doç. Dr. Miraç Barış Usta’nın, Glen O. Gabbard’ın *Psychodynamic Psychiatry in Clinical Practice* (5. baskı, 2014) kitabını çocuk ve ergen psikiyatrisi gözüyle okumak için hazırladığı etkileşimli okuma rehberi (Kasım 2026).

**Canlı sürüm:** https://miracbarisusta.com/psikodinamik-okuma-rehberi/

## İçerik

- Kitabın 19 bölümünden 15’i (1–10, 12, 13, 15–17). Her bölümde yedi adım: kitapta ve okurken (okuma soruları) · ana fikirler · ÇRS’deki karşılığı · tartışmaya açık noktalar · üç kurgusal vaka sorusu · akılda kalsın · kendi notum.
- “Tartışmaya açık” kutuları kitabın 2014’teki kanıt zeminini bugünkü literatürle karşılaştırır; 61 makalenin künyesi PubMed’den doğrulanmış, DOI ve PubMed bağlantılarıyla verilmiştir.
- Okuma derinliği: her bölüm üç katta açılır. **Göz at** (kitapta ne var, başlıkları açılan ana fikirler, akılda kalsın), **Oku** (okuma soruları, ÇRS’deki karşılığı, bölümün kuramcıları), **Derinleş** (tartışmaya açık noktalar, vaka soruları, not). Seçim tarayıcıda saklanır; `#/bolum-15/tartisma` gibi doğrudan bağlantılar gereken katı kendiliğinden açar.
- Kuramcılar: kitapta en çok anılan 17 kuramcı için zaman çizgisi, ekole göre süzme, tek cümlelik katkı, kitaptaki yeri, ÇRS’deki karşılığı ve geçtiği bölümler (`#/kuramcilar`, `#/kuramcilar/kohut`).
- Ergenlik notları: kitapta dağınık kalan ergenlik geçişleri beş temada ve kitabın bıraktığı boşluklar.
- Araçlar:
  - “Odada kaç kişi var?”: görüşmedeki kişi sayısına göre imge haritası (n × (n + 1)) ve hücre hücre klinik ipuçları;
  - 35 kavram kartı (kendi tanımlarımızla);
  - savunma oyunu: 22 kurgusal vinyette savunma ve düzey tahmini, savunma sözlüğü;
  - psikodinamik formülasyon şablonu: tarayıcıda kaydedilen, yazdırılabilir çalışma kâğıdı ve kurgusal örnek vaka;
  - 45 vaka sorusundan karışık test.

## Kullanım

- Okundu işaretleri, vaka sorusu yanıtları, bilinen kartlar, notlar ve formülasyon taslağı yalnızca kullanıcının tarayıcısında saklanır. Formülasyon şablonuna gerçek hasta bilgisi girilmemelidir.
- Bir atfa tıklayınca künyesi açılır; kaynakçada her kaynağın rehberde geçtiği yerler listelenir.
- `/` tuşu aramaya odaklanır. Doğrudan bağlantı örnekleri: `#/bolum-15`, `#/bolum-15/tartisma`, `#/savunmalar`, `#/formulasyon`, `#/oda`, `#/kaynakca`.

## Dosyalar

| Dosya | İçerik |
| --- | --- |
| `index.html` | Rehber; `tools/olustur.py` ile üretilir. |
| `rehber.css`, `rehber.js` | Görünüm ve etkileşim; dış betik ya da kütüphane kullanmaz. |
| `tools/icerik_bolumler.py` | Bölüm içerikleri: okuma soruları, ana fikirler, ÇRS karşılıkları, tartışma noktaları, vaka soruları. |
| `tools/icerik_araclar.py` | Kavramlar, savunma vinyetleri ve sözlüğü, formülasyon şablonu, ergenlik notları, “odada kaç kişi var?” metinleri. |
| `tools/icerik_kuramcilar.py` | Kuramcı kartları, ekoller ve görsel künyeleri. |
| `tools/kaynaklar.json` | Doğrulanmış künyeler (PMID, DOI). |

## Kuramcı görselleri

Depoda kuramcı fotoğrafı yoktur; kartlarda baş harfler gösterilir. Görsel eklemek için dosyayı `gorseller/` klasörüne koyun ve `gorseller/kunye.csv` içinde o satırın kaynak, lisans ve hak sahibi sütunlarını doldurun (ayrıntı: `gorseller/OKU.txt`). Künyesi eksik görsel sayfaya eklenmez. Yalnızca kamu malı ya da açık lisanslı görseller kullanılmalıdır.

## Kaynak ve sorumluluk

Bu bir okuma rehberidir, kitabın yerine geçmez. Kitaptan alıntı, kitabın vaka örnekleri ya da bölümlerin ayrıntılı özeti yoktur; fikirler kendi sözcüklerimizle yazılmış ve çocuk ve ergen ruh sağlığı pratiğine çevrilmiştir. Rehber yazar ya da yayıneviyle bağlantılı değildir. Eğitim amaçlıdır; bilgiler Kasım 2026 itibarıyladır. Vakalar kurgusaldır.

## Lisans

© 2026 Miraç Barış Usta. Tüm hakları saklıdır; ayrıntılar için [LICENSE](LICENSE).
