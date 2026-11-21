# -*- coding: utf-8 -*-
"""Psikodinamik Psikiyatri Okuma Rehberi: index.html üreticisi.

Kullanım:  python3 tools/olustur.py
Girdi:     tools/icerik_bolumler.py, tools/icerik_araclar.py, tools/kaynaklar.json
Çıktı:     index.html (depo kökünde)
"""
import html
import json
import re
import sys
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))

import icerik_araclar as A  # noqa: E402
import icerik_kuramcilar as K
import icerik_bolumler as B  # noqa: E402

KAYNAK = json.loads((ARACLAR / "kaynaklar.json").read_text(encoding="utf-8"))
KULLANIM = {}      # anahtar -> [(görünüm id, adım, etiket)]
BILINMEYEN = set()
BAGLAM = {"vid": "", "adim": "", "etiket": ""}


def esc(s):
    return html.escape(str(s), quote=True)


def atif(m):
    k = m.group(1)
    r = KAYNAK.get(k)
    if not r:
        BILINMEYEN.add(k)
        return esc(k)
    yer = (BAGLAM["vid"], BAGLAM["adim"], BAGLAM["etiket"])
    if yer[0] and yer not in KULLANIM.setdefault(k, []):
        KULLANIM[k].append(yer)
    return f'<a class="atif" href="#k-{k}" data-k="k-{k}">{esc(r["etiket"])}</a>'


def md(s):
    """Kaçış + **kalın**, *eğik*, [@atıf]."""
    t = esc(s)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"\[@([\w-]+)\]", atif, t)
    return t


def baglam(vid, adim="", etiket=""):
    BAGLAM.update(vid=vid, adim=adim, etiket=etiket)


HARF = "ABCD"


def bas_harf(ad):
    p = [x for x in ad.replace(".", " ").split() if x[0].isupper()]
    return (p[0][0] + p[-1][0]) if len(p) > 1 else p[0][:2]
VIEWS = []


def view(vid, baslik, ust, ic, data_baslik=None, sinif="", h="h2"):
    return (f'<section class="view {sinif}" id="v-{vid}" data-view="{vid}" data-baslik="{esc(data_baslik or baslik)}" '
            f'aria-label="{esc(data_baslik or baslik)}"><header class="oturum-bas"><p class="ust-baslik">{esc(ust)}</p>'
            f'<{h} tabindex="-1">{esc(baslik)}</{h}></header>{ic}'
            f'<div class="oturum-son"><nav class="ileri-geri" aria-label="Bölümler arasında"></nav></div></section>')


def adim(vid, anahtar, ikon, baslik, govde, kat=1):
    sid = f"{vid}-{anahtar}"
    return (f'<section class="adim adim-{anahtar}" id="{sid}" data-kat="{kat}" aria-labelledby="{sid}-b"><h3 id="{sid}-b">'
            f'<span class="adim-ikon" aria-hidden="true">{ikon}</span> {esc(baslik)}</h3>{govde}</section>')


def test_listesi(vid, sorular):
    out = [f'<p class="sina-ust"><span class="sina-skor" data-test-skor="{vid}" aria-live="polite"></span>'
           f'<button type="button" class="sina-sifirla" data-test-sifirla="{vid}" hidden>Yanıtları sil</button></p><ol class="test">']
    for i, q in enumerate(sorular):
        assert 0 <= q["dogru"] < len(q["secenekler"]) <= 4, q["soru"]
        btn = "".join(f'<button type="button" data-secenek="{k}"><span class="harf" aria-hidden="true">{HARF[k]}</span>'
                      f'<span>{md(s)}</span></button>' for k, s in enumerate(q["secenekler"]))
        out.append(f'<li class="test-madde" data-dogru="{q["dogru"]}" data-no="{i}" data-ara><p class="soru">{md(q["soru"])}</p>'
                   f'<div class="secenekler" role="group" aria-label="Seçenekler">{btn}</div>'
                   f'<div class="test-aciklama"><p><strong>Doğru yanıt: {HARF[q["dogru"]]}.</strong> {md(q["aciklama"])}</p></div></li>')
    out.append("</ol>")
    return "".join(out)


# ---------------------------------------------------------------- bölümler
KISA = {b["no"]: b["kisa"] for b in B.BOLUMLER}
bolum_views = []
for b in B.BOLUMLER:
    vid = f'bolum-{b["no"]}'
    etiket = f'Bölüm {b["no"]}'
    parcalar = []
    baglam(vid, "okurken", etiket)
    parcalar.append(adim(vid, "kitapta", "📖", "Kitapta", f'<p class="kitapta" data-ara>{md(b["kitapta"])}</p>', 1))
    baglam(vid, "fikirler", etiket)
    parcalar.append(adim(vid, "fikirler", "🧭", "Ana fikirler",
                         '<p class="not kat-ipucu">Başlığa dokunun: açıklaması açılır.</p><ol class="fikirler">' + "".join(
                             f'<li data-ara><details class="ac"><summary><strong>{md(h)}</strong></summary><p>{md(t)}</p></details></li>'
                             for h, t in b["fikirler"]) + "</ol>", 1))
    baglam(vid, "akilda", etiket)
    parcalar.append(adim(vid, "akilda", "🎯", "Akılda kalsın", f'<ul class="akilda"><li data-ara>{md(b["akilda"])}</li></ul>', 1))
    baglam(vid, "okurken", etiket)
    parcalar.append(adim(vid, "okurken", "🔎", "Okurken aklınızda tutun",
                         f'<ol class="okurken">{"".join(f"<li data-ara>{md(q)}</li>" for q in b["okurken"])}</ol>', 2))
    baglam(vid, "crs", etiket)
    parcalar.append(adim(vid, "crs", "🧸", "ÇRS’de karşılığı",
                         '<ul class="crs-liste">' + "".join(f"<li data-ara>{md(x)}</li>" for x in b["crs"]) + "</ul>", 2))
    kur = [k for k in K.KURAMCILAR if b["no"] in k[9]]
    if kur:
        parcalar.append(adim(vid, "kuramcilar", "👤", "Bu bölümün kuramcıları", '<ul class="kuramci-cipler">' + "".join(
            f'<li><a href="#/kuramcilar/{k[0]}"><span class="mono mono-{k[4]}" aria-hidden="true">{esc(bas_harf(k[1]))}</span>'
            f'<span>{esc(k[1])}</span></a></li>' for k in kur) + "</ul>", 2))
    baglam(vid, "tartisma", etiket)
    parcalar.append(adim(vid, "tartisma", "⚖️", "Tartışmaya açık",
                         '<p class="not">Kitabın 2014’teki kanıt zemini ile bugünkü bilgi arasındaki farklar ve tartışmalı noktalar. '
                         'Künyeler kaynakçada; makalelerin tamamı PubMed’den doğrulandı.</p><div class="tartisma-liste">' + "".join(
                             f'<article class="tartisma" data-ara><details class="ac"><summary><h4>{md(h)}</h4></summary><p>{md(t)}</p></details></article>'
                             for h, t in b["tartisma"]) + "</div>", 3))
    baglam(vid, "test", etiket)
    parcalar.append(adim(vid, "test", "✍️", "Vaka soruları",
                         '<p class="not">Vakalar kurgusaldır; kitabın vakalarından alınmamıştır.</p>' + test_listesi(vid, b["sorular"]), 3))
    parcalar.append(adim(vid, "not", "🗒️", "Kendi notum",
                         f'<div class="vaka-not"><label for="{vid}-not-alan">Bu bölümü okurken aklınıza gelenler, kendi vakalarınızla '
                         f'bağlantılar</label><textarea id="{vid}-not-alan" data-not="{vid}" rows="4" placeholder="Hasta kimlik bilgisi '
                         f'yazmayın."></textarea><p class="kucuk">Yazdıklarınız yalnızca bu tarayıcıda saklanır.</p></div>', 3))
    parcalar.append('<p class="derin-ileri"><button type="button" class="dugme" data-derin-artir></button></p>')
    nav = ('<div class="derinlik" role="group" aria-label="Okuma derinliği">'
           '<button type="button" data-derinlik-sec="1" aria-pressed="false"><strong>Göz at</strong><span>2 dakika · ana fikirler</span></button>'
           '<button type="button" data-derinlik-sec="2" aria-pressed="false"><strong>Oku</strong><span>okuma soruları · ÇRS · kuramcılar</span></button>'
           '<button type="button" data-derinlik-sec="3" aria-pressed="false"><strong>Derinleş</strong><span>tartışma · vaka soruları · not</span></button></div>')
    bas = (f'<header class="oturum-bas"><p class="ust-baslik">{esc(B.KISIMLAR[b["kisim"]].split(" · ")[0])} · Bölüm {b["no"]}</p>'
           f'<h2 tabindex="-1">{esc(b["baslik"])}</h2><p class="slogan">{md(b["slogan"])}</p></header>')
    html_ = (f'<section class="view bolum" id="v-{vid}" data-view="{vid}" data-baslik="Bölüm {b["no"]}: {esc(b["kisa"])}" '
             f'aria-label="Bölüm {b["no"]}">{bas}{nav}{"".join(parcalar)}'
             f'<div class="oturum-son"><button type="button" class="okundu" data-okundu="{vid}" aria-pressed="false">'
             f'Bu bölümü okudum</button><nav class="ileri-geri" aria-label="Bölümler arasında"></nav></div></section>')
    bolum_views.append(dict(id=vid, no=b["no"], kisim=b["kisim"], kisa=b["kisa"], baslik=b["baslik"], slogan=b["slogan"],
                            html=html_, n_tart=len(b["tartisma"]), n_soru=len(b["sorular"])))

# ---------------------------------------------------------------- kuramcılar
baglam("kuramcilar", "", "Kuramcılar")
BOLUM_NO = {b["no"] for b in B.BOLUMLER}
KAVRAM_AD = {k[0] for k in A.KAVRAMLAR}
Y0, Y1 = 1850, 2030


def gorsel(anahtar, ad, ekol):
    g = K.GORSEL_KUNYE.get(anahtar)
    if g and (KOK / "gorseller" / g["dosya"]).exists():
        return (f'<figure class="kuramci-foto"><img src="gorseller/{esc(g["dosya"])}" alt="{esc(ad)}" loading="lazy" width="96" height="96">'
                f'<figcaption><a href="{esc(g["kaynak"])}" target="_blank" rel="noopener">Görsel: {esc(g["sahibi"])}</a> · {esc(g["lisans"])}</figcaption></figure>')
    return f'<span class="mono mono-buyuk mono-{ekol}" aria-hidden="true">{esc(bas_harf(ad))}</span>'


satir = 22
svg = [f'<svg class="zaman-cizgi" viewBox="0 0 912 {len(K.KURAMCILAR) * satir + 34}" role="img" '
       f'aria-label="Kuramcıların yaşam süreleri, {Y0}–{Y1}">']
for y in range(Y0, Y1 + 1, 30):
    x = 190 + (y - Y0) / (Y1 - Y0) * 700
    svg.append(f'<line x1="{x:.0f}" y1="14" x2="{x:.0f}" y2="{len(K.KURAMCILAR) * satir + 22}" class="zc-izgara"/>'
               f'<text x="{x:.0f}" y="10" class="zc-yil" text-anchor="middle">{y}</text>')
for n, k in enumerate(sorted(K.KURAMCILAR, key=lambda k: k[2])):
    a, ad, d, o, ekol = k[:5]
    x0 = 190 + (d - Y0) / (Y1 - Y0) * 700
    x1 = 190 + ((o or 2026) - Y0) / (Y1 - Y0) * 700
    yy = 22 + n * satir
    svg.append(f'<a href="#/kuramcilar/{a}"><text x="182" y="{yy + 11}" class="zc-ad" text-anchor="end">{esc(ad)}</text>'
               f'<rect x="{x0:.0f}" y="{yy}" width="{x1 - x0:.0f}" height="14" rx="7" class="zc-cubuk zc-{ekol}{"" if o else " zc-yasiyor"}"/></a>')
svg.append("</svg>")
suz = ('<div class="ekol-suz" role="group" aria-label="Ekole göre süz"><button type="button" data-ekol="" aria-pressed="true">Tümü</button>'
       + "".join(f'<button type="button" data-ekol="{e}" aria-pressed="false"><span class="nokta mono-{e}" aria-hidden="true"></span>{esc(ad)}</button>'
                 for e, (ad, _) in K.EKOLLER.items()) + "</div>")
kartlar = []
for a, ad, d, o, ekol, tek, kitapta, crs, kavramlar, bolumler in K.KURAMCILAR:
    assert ekol in K.EKOLLER and all(x in KAVRAM_AD for x in kavramlar) and all(x in BOLUM_NO for x in bolumler), a
    yil = f"{d}–{o}" if o else f"d. {d}"
    kav = ("<p class=\"kuramci-kavram\"><span>Kavramlar:</span> " + " ".join(f'<a class="cip" href="#/kavramlar">{esc(x)}</a>' for x in kavramlar) + "</p>") if kavramlar else ""
    bol = " ".join(f'<a class="cip cip-bolum" href="#/bolum-{x}">Bölüm {x}: {esc(KISA[x])}</a>' for x in bolumler)
    kartlar.append(
        f'<li class="kuramci" id="kuramcilar-{a}" data-ekol="{ekol}" data-ara>{gorsel(a, ad, ekol)}<div class="kuramci-govde">'
        f'<h3>{esc(ad)} <span class="kuramci-yil">{yil}</span></h3><p class="kuramci-ekol"><span class="nokta mono-{ekol}" aria-hidden="true"></span>{esc(K.EKOLLER[ekol][0])}</p>'
        f'<p class="kuramci-tek">{md(tek)}</p><details class="ac"><summary>Kitapta ve ÇRS’de</summary>'
        f'<p><strong>Kitapta.</strong> {md(kitapta)}</p><p><strong>ÇRS’de.</strong> {md(crs)}</p>{kav}'
        f'<p class="kuramci-bolum"><span>Geçtiği bölümler:</span> {bol}</p></details></div></li>')
kur_ic = ('<p class="giris-metin" data-ara>Kitabın kuramsal temelini kuran ve klinik bölümlerde en çok anılan '
          f'{len(K.KURAMCILAR)} isim. Zaman çizgisinde bir ada dokunun ya da ekole göre süzün. Her kartta kuramcının tek cümlelik '
          'katkısı var; “Kitapta ve ÇRS’de” başlığı ayrıntıyı açar.</p>'
          f'<div class="zaman-kap" tabindex="0" aria-label="Zaman çizgisi; yana kaydırılabilir">{"".join(svg)}</div>{suz}'
          f'<ul class="kuramcilar">{"".join(kartlar)}</ul>'
          '<p class="kucuk">Doğum ve ölüm yılları genel başvuru kaynaklarındaki bilinen tarihlerdir. Kartlardaki metinler özgündür; '
          'kitaptan alıntı içermez. Bu sürümde kuramcı fotoğrafı yoktur.</p>')
kuramcilar = dict(id="kuramcilar", label="Kuramcılar", html=view("kuramcilar", "Kuramcılar: kim, ne dedi, kitapta nerede?", "Tema", kur_ic,
                                                                 data_baslik="Kuramcılar"))

# ---------------------------------------------------------------- ergenlik
baglam("ergenlik", "", "Ergenlik notları")
erg = [f'<p class="giris-metin" data-ara>{md(A.ERGENLIK_GIRIS)}</p>']
for i, (bas, maddeler, akil) in enumerate(A.ERGENLIK, 1):
    erg.append(f'<section class="tema" id="ergenlik-{i}" aria-labelledby="ergenlik-{i}-b"><h3 id="ergenlik-{i}-b">'
               f'<span class="tema-no">{i}</span> {md(bas)}</h3><ul class="crs-liste">'
               + "".join(f"<li data-ara>{md(m)}</li>" for m in maddeler)
               + f'</ul><p class="tema-akil" data-ara><span aria-hidden="true">🎯</span> {md(akil)}</p></section>')
erg.append('<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Akılda kalsın</h3><ul class="akilda">'
           + "".join(f"<li data-ara>{md(x)}</li>" for x in A.ERGENLIK_AKILDA) + "</ul>")
ergenlik = dict(id="ergenlik", label="Ergenlik notları",
                html=view("ergenlik", "Ergenlik notları: kitapta dağınık kalanlar", "Tema", "".join(erg),
                          data_baslik="Ergenlik notları"))

# ---------------------------------------------------------------- oda
baglam("oda", "", "Odada kaç kişi var?")
KISILER = [("hekim", "Hekim", "Hekimin"), ("ergen", "Ergen", "Ergenin"), ("cocuk", "Çocuk", "Çocuğun"),
           ("anne", "Anne", "Annenin"), ("baba", "Baba", "Babanın"), ("kardes", "Kardeş", "Kardeşin"),
           ("ogretmen", "Öğretmen", "Öğretmenin")]
oda_veri = "".join(f'<li data-kisi="{k}" data-bakan="{v}">{esc(t)}</li>' for (k, v), t in A.ODA_HUCRELER.items())
kisi_veri = "".join(f'<li data-id="{i}" data-ad="{esc(a)}" data-in="{esc(g)}"></li>' for i, a, g in KISILER)
oda_statik = ('<div class="tablo-kap oda-statik"><table class="tablo"><thead><tr><th>Kişi</th><th>Kendi gözünde</th>'
              '<th>Diğer üç kişinin gözünde</th><th>Gerçekte</th><th>Toplam</th></tr></thead><tbody>'
              + "".join(f'<tr><td data-label="Kişi">{k}</td><td data-label="Kendi gözünde">1</td><td data-label="Diğerlerinin gözünde">3</td>'
                        f'<td data-label="Gerçekte">1</td><td data-label="Toplam">5</td></tr>' for k in ("Anne", "Baba", "Çocuk", "Hekim"))
              + '</tbody></table></div><p class="not">Dört kişilik bir aile görüşmesinde: 4 × 5 = 20 imge.</p>')
oda_ic = (f'<p class="giris-metin" data-ara>{md(A.ODA_GIRIS)}</p>'
          '<div class="oda" id="oda"><div class="oda-araclar" role="group" aria-label="Odadakiler">'
          '<button type="button" class="filtre" data-oda="hekim,ergen" aria-pressed="false">Hekim ve ergen</button>'
          '<button type="button" class="filtre" data-oda="hekim,anne,cocuk" aria-pressed="false">Hekim, anne, çocuk</button>'
          '<button type="button" class="filtre" data-oda="hekim,anne,baba,cocuk" aria-pressed="true">Hekim, anne, baba, çocuk</button>'
          '</div><div class="oda-ekle" role="group" aria-label="Odaya ekle">'
          '<button type="button" class="dugme dugme-ikincil oda-kisi" data-kisi="kardes" aria-pressed="false">+ Kardeş</button>'
          '<button type="button" class="dugme dugme-ikincil oda-kisi" data-kisi="ogretmen" aria-pressed="false">+ Öğretmen</button>'
          '<button type="button" class="dugme dugme-ikincil oda-hayalet" aria-pressed="false">Odaya girmeyenleri göster</button></div>'
          '<p class="oda-sayi" aria-live="polite"></p><p class="oda-kaydir kucuk">Tabloyu yana kaydırabilirsiniz.</p><div class="oda-izgara"></div>'
          '<div class="oda-ipucu" aria-live="polite"><p class="kucuk">Bir hücreye dokunun: o imgenin klinikte nasıl göründüğüne dair bir ipucu açılır.</p></div>'
          f'<div class="oda-hayaletler" hidden><ul>{"".join(f"<li>{esc(h)}</li>" for h in A.ODA_HAYALETLER)}</ul>'
          f'<p data-ara>{md(A.ODA_HAYALET_NOT)}</p></div>'
          f'<ul class="oda-veri" hidden>{oda_veri}</ul><ul class="oda-kisiler" hidden>{kisi_veri}</ul>'
          f'<div class="sim-js-yok">{oda_statik}</div></div>'
          '<ul class="akilda"><li data-ara>Dört sandalye, yirmi kişi: aile görüşmesi kimin kimi nasıl gördüğünün haritasıdır.</li>'
          '<li data-ara>Muayene odasında görünen kişi sayısı, gerçekte orada olanların en küçüğüdür.</li></ul>')
oda = dict(id="oda", label="Odada kaç kişi var?",
           html=view("oda", "Odada kaç kişi var?", "Araçlar", oda_ic))

# ---------------------------------------------------------------- kavram kartları
baglam("kavramlar", "", "Kavram kartları")
kav_li = []
for i, (terim, tanim, ornek, bols) in enumerate(A.KAVRAMLAR):
    bag = ", ".join(f'<a href="#/bolum-{n}">Bölüm {n}</a>' for n in bols)
    kav_li.append(f'<li class="kavram" id="kavram-{i}" data-id="kavram-{i}" data-ara><p class="kavram-terim">{esc(terim)}</p>'
                  f'<p class="kavram-tanim">{md(tanim)}</p><p class="kavram-ornek"><span class="guncel-etiket">ÇRS’de</span> '
                  f'{md(ornek)}</p><p class="ders-ref">{bag}</p></li>')
kavram_ic = ('<p class="giris-metin">Rehberdeki temel kavramlar, kendi tanımlarımızla. Kartı çevirin, bildiklerinizi işaretleyin; '
             'bilmedikleriniz daha sık karşınıza çıkar. Boşluk tuşu kartı çevirir.</p>'
             '<div class="kart-araclar"><button type="button" class="dugme dugme-ikincil kart-karistir">Karıştır</button>'
             '<button type="button" class="sina-sifirla kart-sifirla">Bilinenleri sıfırla</button></div>'
             '<div class="kart-sahne" aria-live="polite"></div><p class="kart-ilerleme"></p>'
             '<p class="sim-js-yok">Kartlar için tarayıcıda JavaScript açık olmalı; aşağıdaki sözlük JavaScript olmadan da okunur.</p>'
             f'<h3 class="tekrar-baslik">Kavram sözlüğü <span class="sayi">{len(A.KAVRAMLAR)}</span></h3>'
             f'<ul class="kavramlar">{"".join(kav_li)}</ul>')
kavramlar = dict(id="kavramlar", label="Kavram kartları", html=view("kavramlar", "Kavram kartları", "Araçlar", kavram_ic))

# ---------------------------------------------------------------- savunma oyunu
baglam("savunmalar", "", "Savunma oyunu")
SOZ = {ad: (duz, tan) for ad, duz, tan in A.SAVUNMA_SOZLUK}
for v, dogru, celdirici, _ in A.SAVUNMA_VAKALARI:
    assert dogru in SOZ, dogru
    for c in celdirici:
        assert c in SOZ, c
    assert len(set(celdirici + [dogru])) == 4, v
vaka_li = "".join(
    f'<li data-dogru="{esc(d)}" data-duzey="{SOZ[d][0]}" data-celdirici="{esc("|".join(c))}">'
    f'<p class="sv-vinyet">{md(v)}</p><p class="sv-aciklama">{md(a)}</p></li>'
    for v, d, c, a in A.SAVUNMA_VAKALARI)
sozluk = []
for anahtar, (ad, aciklama) in A.DUZEYLER.items():
    maddeler = "".join(f'<li data-ara><strong>{esc(x)}.</strong> {md(t)}</li>' for x, d, t in A.SAVUNMA_SOZLUK if d == anahtar)
    sozluk.append(f'<div class="sozluk-sutun sozluk-{anahtar}"><h4><span class="duzey duzey-{anahtar}">{esc(ad)}</span></h4>'
                  f'<p class="kucuk">{esc(aciklama)}</p><ul>{maddeler}</ul></div>')
sav_ic = ('<p class="giris-metin">Kısa, kurgusal vinyetlerde hangi savunmanın öne çıktığını bulun; ardından düzeyini tahmin edin. '
          f'{len(A.SAVUNMA_VAKALARI)} vinyet, karışık sırayla. Gerçek klinikte savunmalar tek başına değil, birlikte ve bağlama '
          'göre değişerek görülür.</p>'
          '<div class="tahmin savunma-oyun" id="savunma-oyun"><h3><span aria-hidden="true">🛡️</span> Savunma oyunu</h3>'
          '<div class="sv-alan" aria-live="polite"></div>'
          '<button type="button" class="dugme sv-basla">Oyunu başlat</button>'
          f'<ol class="sv-veri" hidden>{vaka_li}</ol></div>'
          '<h3 class="tekrar-baslik">Savunma sözlüğü</h3>'
          '<p class="not">Bu üç basamaklı sıralama öğretim amaçlıdır; farklı yazarlar savunmaları farklı düzeylere yerleştirir ve '
          'DSM-IV’ün savunma işlevselliği ölçeği yedi düzey önerir. Uzun süreli izlem çalışmaları olgun savunmaların daha iyi uyumla '
          f'ilişkili olduğunu göstermiştir ({md("[@vaillant1977]")}).</p>'
          f'<div class="sozluk">{"".join(sozluk)}</div>')
savunmalar = dict(id="savunmalar", label="Savunma oyunu", html=view("savunmalar", "Savunma oyunu", "Araçlar", sav_ic))

# ---------------------------------------------------------------- formülasyon
baglam("formulasyon", "", "Formülasyon şablonu")
ORN = A.FORM_ORNEK
alanlar = []
for k, bas, ipucu, satir in A.FORM_ALANLAR:
    alanlar.append(f'<div class="form-alan"><label for="f-{k}">{esc(bas)}</label><p class="form-ipucu" id="f-{k}-i">{esc(ipucu)}</p>'
                   f'<textarea id="f-{k}" data-form="{k}" rows="{satir}" aria-describedby="f-{k}-i" '
                   f'data-ornek="{esc(ORN.get(k, ""))}"></textarea></div>')
    if k == "aile":
        oruntu = "".join(f'<div><label for="f-{a}">{esc(b2)}</label><input id="f-{a}" type="text" data-form="{a}" '
                         f'placeholder="{esc(p)}" data-ornek="{esc(ORN.get(a, ""))}"></div>' for a, b2, p in A.FORM_ORUNTU)
        alanlar.append('<fieldset class="form-alan form-oruntu"><legend>Tekrarlayan ilişki örüntüsü</legend>'
                       '<p class="form-ipucu">Kendilik, öteki ve aradaki duygu: hasta ilişkilerde kendini nasıl, ötekini nasıl yaşıyor?</p>'
                       f'<div class="oruntu-izgara">{oruntu}</div></fieldset>')
        kutular = []
        for anahtar, (ad, _) in A.DUZEYLER.items():
            ks = "".join(f'<label class="secim"><input type="checkbox" data-form-savunma value="{esc(x)}"'
                         f'{" data-ornek-secili" if x in ORN["savunmalar"] else ""}> {esc(x)}</label>'
                         for x, d, _ in A.SAVUNMA_SOZLUK if d == anahtar)
            kutular.append(f'<div class="savunma-grup"><p class="savunma-grup-ad"><span class="duzey duzey-{anahtar}">{esc(ad)}</span></p>{ks}</div>')
        alanlar.append('<fieldset class="form-alan"><legend>Savunma profili</legend>'
                       '<p class="form-ipucu">Öne çıkan savunmaları işaretleyin (bkz. <a href="#/savunmalar">savunma sözlüğü</a>).</p>'
                       f'<div class="savunma-kutular">{"".join(kutular)}</div></fieldset>')
    if k == "ozet":
        tedavi = "".join(f'<label class="secim"><input type="checkbox" data-form-tedavi value="{esc(x)}"'
                         f'{" data-ornek-secili" if x in ORN["tedavi"] else ""}> {esc(x)}</label>' for x in A.FORM_TEDAVI)
        alanlar.append('<fieldset class="form-alan"><legend>Tedavi önerisi</legend>'
                       '<label for="f-surekli" class="form-ipucu">Keşfedici–destekleyici süreklilikte konum</label>'
                       f'<div class="surekli"><span>Destekleyici</span><input id="f-surekli" type="range" min="1" max="5" step="1" value="3" '
                       f'data-form="surekli" data-ornek="{ORN["surekli"]}"><span>Keşfedici</span></div>'
                       f'<div class="tedavi-kutular">{tedavi}</div></fieldset>')
form_ic = ('<p class="giris-metin">Kendi vakanızı psikodinamik olarak düşünmek için bir çalışma kâğıdı. Alanlar bölümlerdeki '
           'kavramlara bağlanır; doldurdukça otomatik kaydedilir. Yazdırabilir ya da PDF olarak kaydedebilirsiniz.</p>'
           '<aside class="uyari"><strong>Gerçek hasta bilgisi girmeyin.</strong> Ad, doğum tarihi, okul ya da adres gibi kimliği belli '
           'eden bilgiler yazmayın. Veriler yalnızca bu tarayıcıda saklanır, sunucuya gönderilmez.</aside>'
           '<div class="form-dugmeler"><button type="button" class="dugme dugme-ikincil form-ornek">Örnek vakayı yükle</button>'
           '<button type="button" class="dugme form-yazdir">Yazdır / PDF</button>'
           '<button type="button" class="dugme dugme-ikincil form-kopyala">Metni kopyala</button>'
           '<button type="button" class="sina-sifirla form-temizle">Formu temizle</button>'
           '<span class="form-durum kucuk" aria-live="polite"></span></div>'
           f'<form class="formulasyon" id="formulasyon" autocomplete="off">{"".join(alanlar)}</form>'
           '<div class="form-baski" aria-hidden="true"></div>')
formulasyon = dict(id="formulasyon", label="Formülasyon şablonu",
                   html=view("formulasyon", "Psikodinamik formülasyon şablonu", "Araçlar", form_ic,
                             data_baslik="Formülasyon şablonu"))

# ---------------------------------------------------------------- tekrar
baglam("tekrar", "", "Karışık test")
n_soru = sum(len(b["sorular"]) for b in B.BOLUMLER)
akil = "".join(f'<li><a href="#/bolum-{b["no"]}">Bölüm {b["no"]}</a> {md(b["akilda"])}</li>' for b in B.BOLUMLER)
tekrar_ic = ('<div class="karisik" id="karisik"><h3><span aria-hidden="true">🎲</span> Karışık test</h3>'
             f'<p>Bütün bölümlerin {n_soru} vaka sorusu karışık sırayla. Yanıtınızı verin; açıklama hemen ardından açılır.</p>'
             '<div class="karisik-alan" aria-live="polite"></div><p class="karisik-dugmeler">'
             f'<button type="button" class="dugme karisik-basla" data-tur="test">Testi başlat ({n_soru} soru)</button></p></div>'
             '<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Akılda kalsın: bölüm bölüm</h3>'
             f'<ul class="akilda akilda-kucuk akilda-liste">{akil}</ul>')
tekrar = dict(id="tekrar", label="Karışık test", html=view("tekrar", "Karışık test ve hızlı tekrar", "Araçlar", tekrar_ic,
                                                           data_baslik="Karışık test"))

# ---------------------------------------------------------------- giriş
baglam("giris", "", "Giriş")
kisim_kartlari = {1: [], 2: []}
for v in bolum_views:
    kisim_kartlari[v["kisim"]].append(
        f'<li><a class="kart" href="#/{v["id"]}" data-kart="{v["id"]}"><span class="kart-no" aria-hidden="true">{v["no"]}</span>'
        f'<span class="kart-govde"><span class="kart-ust">Bölüm {v["no"]}</span><span class="kart-baslik">{esc(v["baslik"])}</span>'
        f'<span class="kart-slogan">{md(v["slogan"])}</span><span class="kart-meta">{v["n_tart"]} tartışma noktası · '
        f'{v["n_soru"]} vaka sorusu</span><span class="kart-durum" data-durum="{v["id"]}"></span></span></a></li>')
eksik_kartlar = "".join(
    f'<li><div class="kart kart-eksik"><span class="kart-no" aria-hidden="true">{n}</span><span class="kart-govde">'
    f'<span class="kart-ust">Bölüm {n}</span><span class="kart-baslik">{esc(t)}</span>'
    f'<span class="kart-meta">Bu rehberde henüz işlenmedi</span></span></div></li>' for n, t in B.EKSIK)
arac_kartlari = "".join(
    f'<li><a class="kart kart-arac" href="#/{i}"><span class="kart-no" aria-hidden="true">{ik}</span><span class="kart-govde">'
    f'<span class="kart-baslik">{esc(ad)}</span><span class="kart-slogan">{esc(ac)}</span></span></a></li>'
    for i, ik, ad, ac in [
        ("kuramcilar", "👤", "Kuramcılar", f"{len(K.KURAMCILAR)} kuramcı: zaman çizgisi, tek cümlelik katkı ve kitaptaki yeri."),
        ("ergenlik", "🌱", "Ergenlik notları", "Kitapta dağınık kalan ergenlik geçişleri beş temada."),
        ("oda", "🪑", "Odada kaç kişi var?", "Aile görüşmesinde kimin kimi nasıl gördüğünün haritası."),
        ("kavramlar", "🃏", "Kavram kartları", f"{len(A.KAVRAMLAR)} temel kavram, kendi tanımlarımızla."),
        ("savunmalar", "🛡️", "Savunma oyunu", f"{len(A.SAVUNMA_VAKALARI)} kurgusal vinyette savunma ve düzey tahmini."),
        ("formulasyon", "✎", "Formülasyon şablonu", "Kendi vakanız için kaydedilen, yazdırılabilir çalışma kâğıdı."),
        ("tekrar", "🎲", "Karışık test", f"{n_soru} vaka sorusu karışık sırayla."),
    ])
giris_ic = f"""
<div class="kahraman">
  <p class="ust-baslik">Glen O. Gabbard · <i lang="en">Psychodynamic Psychiatry in Clinical Practice</i> · 5. baskı</p>
  <h1 tabindex="-1">Psikodinamik Psikiyatri Okuma Rehberi</h1>
  <p class="alt-baslik">Çocuk ve ergen psikiyatrisi gözüyle, bölüm bölüm</p>
  <p class="kahraman-metin" data-ara>Bu rehber, Gabbard’ın dinamik psikiyatri kitabını ({md("[@gabbard2014]")}) çocuk ve ergen ruh sağlığı ve
  hastalıkları (ÇRS) pratiğine çevirerek okumak için hazırlandı. Her bölüm için okurken sorulacak sorular, ana fikirler, ÇRS’deki
  karşılığı, bugünkü kanıtla tartışmaya açık noktalar ve kurgusal vaka soruları var.</p>
  <p class="kahraman-dugmeler"><a class="dugme" href="#/bolum-1">Bölüm 1’den başla <span aria-hidden="true">→</span></a>
  <a class="dugme dugme-ikincil" href="#/kavramlar">Kavram kartları</a> <a class="dugme dugme-ikincil" href="#/savunmalar">Savunma oyunu</a>
  <a class="dugme dugme-ikincil" href="#/formulasyon">Formülasyon şablonu</a></p>
  <aside class="yeni-not"><strong>Bu bir okuma rehberidir, kitabın yerine geçmez.</strong> Kitaptan alıntı, kitabın vakaları ya da
  bölümlerin ayrıntılı özeti yoktur; fikirler kendi sözcüklerimizle yazıldı. Her bölümü önce kitaptan okuyun, sonra buraya dönün.</aside>
</div>
<section class="ilerlemem" id="ilerlemem" hidden aria-labelledby="ilerleme-b"><h2 id="ilerleme-b" class="bolum-baslik">İlerlemem</h2>
<div class="ilerleme-kutular"></div>
<p class="kucuk">İlerleme yalnızca bu tarayıcıda saklanır. <button type="button" class="sina-sifirla hepsini-sil">Bütün ilerlemeyi sil</button></p></section>
<section class="kurallar kullanim" aria-labelledby="kurallar-b"><h2 id="kurallar-b" class="bolum-baslik">Nasıl kullanılır?</h2>
<ol><li data-ara><span class="kural-no">1</span> <strong>Göz at.</strong> Her bölüm önce kısa hâliyle açılır: kitapta ne var, ana fikirler, akılda kalacak cümle.</li>
<li data-ara><span class="kural-no">2</span> <strong>Oku.</strong> Bölümü kitaptan okurken okuma sorularını, ÇRS’deki karşılığını ve kuramcıları açın.</li>
<li data-ara><span class="kural-no">3</span> <strong>Derinleş.</strong> Tartışmaya açık noktalar, vaka soruları ve kendi notunuz en alt katta.</li></ol></section>
<section aria-labelledby="k1-b"><h2 id="k1-b" class="bolum-baslik">{esc(B.KISIMLAR[1])}</h2><ol class="kartlar">{"".join(kisim_kartlari[1])}</ol></section>
<section aria-labelledby="k2-b"><h2 id="k2-b" class="bolum-baslik">{esc(B.KISIMLAR[2])}</h2><ol class="kartlar">{"".join(kisim_kartlari[2])}</ol>
<p class="kucuk">Kitabın 19 bölümünden 15’i bu rehberde işlendi. Kalan dört bölüm ileride eklenebilir:</p>
<ol class="kartlar kartlar-eksik">{eksik_kartlar}</ol></section>
<section aria-labelledby="arac-b"><h2 id="arac-b" class="bolum-baslik">Tema ve araçlar</h2><ol class="kartlar">{arac_kartlari}</ol></section>
"""
giris = dict(id="giris", label="Giriş",
             html=f'<section class="view aktif" id="v-giris" data-view="giris" data-baslik="Giriş" aria-label="Giriş">{giris_ic}</section>')

# ---------------------------------------------------------------- kaynakça (en son: kullanım bilgisi gerekiyor)
SIRA = ["giris"] + [v["id"] for v in bolum_views] + ["kuramcilar", "ergenlik", "oda", "kavramlar", "savunmalar", "formulasyon", "tekrar"]
ETIKET = {"giris": "Giriş", "kuramcilar": "Kuramcılar", "ergenlik": "Ergenlik notları", "oda": "Odada kaç kişi var?", "kavramlar": "Kavram kartları",
          "savunmalar": "Savunma oyunu", "formulasyon": "Formülasyon şablonu", "tekrar": "Karışık test"}
ETIKET.update({v["id"]: f'Bölüm {v["no"]}' for v in bolum_views})


def kaynak_li(k):
    r = KAYNAK[k]
    ek = []
    if r.get("doi"):
        ek.append(f'<a href="https://doi.org/{esc(r["doi"])}" target="_blank" rel="noopener">doi:{esc(r["doi"])}</a>')
    if r.get("pmid"):
        ek.append(f'<a href="https://pubmed.ncbi.nlm.nih.gov/{r["pmid"]}/" target="_blank" rel="noopener">PMID {r["pmid"]}</a>')
    yerler = sorted(KULLANIM.get(k, []), key=lambda y: SIRA.index(y[0]) if y[0] in SIRA else 99)
    gor = []
    for vid, ad, et in yerler:
        hedef = f"#/{vid}/{ad}" if ad else f"#/{vid}"
        if hedef not in [g[0] for g in gor]:
            gor.append((hedef, ETIKET.get(vid, et)))
    geri = (' <span class="kaynak-geri">Geçtiği yer: ' + ", ".join(f'<a href="{h}">{esc(e)}</a>' for h, e in gor) + "</span>") if gor else ""
    return f'<li id="k-{k}" data-ara>{esc(r["metin"])} {" · ".join(ek)}{geri}</li>'


makaleler = sorted([k for k, r in KAYNAK.items() if r.get("pmid")], key=lambda k: KAYNAK[k]["metin"].lower())
kitaplar = [k for k in ["dsm5", "pdm2", "holmes1858", "keys1950", "vaillant1977"] if k in KAYNAK]
kay_ic = ('<p class="giris-metin">Rehberde anılan bütün kaynaklar. Makalelerin künyeleri Kasım 2026’da PubMed’den doğrulandı; '
          'her makalenin yanında DOI ve PubMed bağlantısı, rehberde geçtiği yerler var.</p>'
          '<p class="kaynak-ara"><label for="kaynak-suz">Kaynakçada süz</label>'
          '<input id="kaynak-suz" type="search" placeholder="Yazar, yıl ya da başlık" autocomplete="off"></p>'
          '<p class="kaynak-sonuc" aria-live="polite"></p>'
          f'<section class="kaynak-grup"><h3>Rehberin eşlik ettiği kitap <span class="sayi">1</span></h3><ol class="kaynaklar">{kaynak_li("gabbard2014")}</ol></section>'
          f'<section class="kaynak-grup"><h3>Diğer kitaplar ve kılavuzlar <span class="sayi">{len(kitaplar)}</span></h3><ol class="kaynaklar">'
          + "".join(kaynak_li(k) for k in kitaplar) + "</ol></section>"
          f'<section class="kaynak-grup"><h3>Makaleler <span class="sayi">{len(makaleler)}</span></h3><ol class="kaynaklar">'
          + "".join(kaynak_li(k) for k in makaleler) + "</ol></section>")
kaynakca = dict(id="kaynakca", label="Kaynakça", html=view("kaynakca", "Kaynakça", "Araçlar", kay_ic))

ORDER = [giris] + bolum_views + [kuramcilar, ergenlik, oda, kavramlar, savunmalar, formulasyon, tekrar, kaynakca]


# ---------------------------------------------------------------- gezinti
def nav_item(vid, no, ad):
    return (f'<li><a href="#/{vid}" data-nav="{vid}"><span class="nav-no" aria-hidden="true">{esc(no)}</span>'
            f'<span class="nav-ad">{esc(ad)}</span><span class="nav-durum" data-durum-nav="{vid}"></span></a></li>')


nav = ('<nav class="yan" id="yan" aria-label="Rehber içeriği"><div class="yan-ic">'
       '<ol class="nav-liste"><li><a href="#/" data-nav="giris"><span class="nav-no" aria-hidden="true">⌂</span>'
       '<span class="nav-ad">Giriş</span></a></li></ol>'
       '<p class="nav-baslik">Kısım I · Temeller ve tedavi</p><ol class="nav-liste">'
       + "".join(nav_item(v["id"], str(v["no"]), v["kisa"]) for v in bolum_views if v["kisim"] == 1) + "</ol>"
       '<p class="nav-baslik">Kısım II · Bozukluklar</p><ol class="nav-liste">'
       + "".join(nav_item(v["id"], str(v["no"]), v["kisa"]) for v in bolum_views if v["kisim"] == 2) + "</ol>"
       '<p class="nav-baslik">Tema</p><ol class="nav-liste">' + nav_item("kuramcilar", "👤", "Kuramcılar") + nav_item("ergenlik", "🌱", "Ergenlik notları") + "</ol>"
       '<p class="nav-baslik">Araçlar</p><ol class="nav-liste">'
       + nav_item("oda", "🪑", "Odada kaç kişi var?") + nav_item("kavramlar", "🃏", "Kavram kartları")
       + nav_item("savunmalar", "🛡", "Savunma oyunu") + nav_item("formulasyon", "✎", "Formülasyon şablonu")
       + nav_item("tekrar", "🎲", "Karışık test") + nav_item("kaynakca", "§", "Kaynakça") + "</ol>"
       '<p class="ilerleme" data-ilerleme></p></div></nav>')

DESC = ("Glen O. Gabbard’ın Psychodynamic Psychiatry in Clinical Practice (5. baskı) kitabına çocuk ve ergen psikiyatrisi "
        "gözüyle eşlik eden etkileşimli okuma rehberi: 15 bölüm için ana fikirler, ÇRS’deki karşılığı, tartışmaya açık noktalar, "
        "kurgusal vaka soruları, kavram kartları, savunma oyunu ve formülasyon şablonu.")
URL = "https://miracbarisusta.com/psikodinamik-okuma-rehberi/"

page = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Psikodinamik Psikiyatri Okuma Rehberi · Doç. Dr. Miraç Barış Usta</title>
<meta name="description" content="{esc(DESC)}">
<meta name="author" content="Miraç Barış Usta">
<meta name="theme-color" content="#fbf7f0">
<meta property="og:title" content="Psikodinamik Psikiyatri Okuma Rehberi">
<meta property="og:description" content="{esc(DESC)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<link rel="canonical" href="{URL}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Lora:ital,wght@0,600;0,700;1,500&amp;display=swap">
<link rel="stylesheet" href="rehber.css">
<script src="rehber.js" defer></script>
</head>
<body>
<a class="atla" href="#icerik">İçeriğe geç</a>
<header class="ust">
  <a class="geri" href="https://miracbarisusta.com/rehberler/"><span aria-hidden="true">←</span> Rehberler</a>
  <a class="marka" href="#/">Psikodinamik Okuma Rehberi</a>
  <div class="ara" role="search">
    <label class="gizli" for="ara">Rehberde ara</label>
    <input id="ara" type="search" placeholder="Rehberde ara…" autocomplete="off" aria-controls="ara-sonuc">
    <div class="ara-sonuc" id="ara-sonuc" hidden></div>
  </div>
  <button type="button" class="menu-dugme" aria-controls="yan" aria-expanded="false">Bölümler</button>
</header>
<div class="duzen">
{nav}
<main id="icerik" tabindex="-1">
{"".join(v["html"] for v in ORDER)}
</main>
</div>
<footer class="alt">
  <p><strong>Hazırlayan:</strong> Doç. Dr. Miraç Barış Usta · Kasım 2026 · <a href="https://miracbarisusta.com">miracbarisusta.com</a></p>
  <p>Glen O. Gabbard’ın <i lang="en">Psychodynamic Psychiatry in Clinical Practice</i> (5. baskı, American Psychiatric Publishing, 2014)
  kitabına eşlik eden bağımsız bir okuma rehberidir. Kitaptan alıntı ya da kitabın vakalarını içermez ve kitabın yerine geçmez.
  Yazar ya da yayıneviyle bağlantılı değildir.</p>
  <p>Eğitim amaçlıdır; bilgiler Kasım 2026 itibarıyladır. Vakalar kurgusaldır. Tanı ve tedavi kararları için güncel kılavuzlara ve
  klinik değerlendirmeye başvurun.</p>
  <p>© 2026 Miraç Barış Usta · <a href="https://github.com/hypothermia15/psikodinamik-okuma-rehberi/blob/main/LICENSE">Kullanım koşulları</a></p>
</footer>
<div class="atif-pop" id="atif-pop" role="dialog" aria-label="Kaynak" hidden></div>
</body>
</html>
"""
(KOK / "index.html").write_text(page, encoding="utf-8")
kullanilmayan = sorted(k for k in KAYNAK if k not in KULLANIM and k != "gabbard2014")
print(f"{len(ORDER)} görünüm, {len(bolum_views)} bölüm, {n_soru} vaka sorusu, {len(A.KAVRAMLAR)} kavram, "
      f"{len(A.SAVUNMA_VAKALARI)} savunma vinyeti, {len(KAYNAK)} kaynak, {page.count('class=\"atif\"')} atıf → "
      f"{KOK / 'index.html'} ({len(page) // 1024} KB)")
if BILINMEYEN:
    print("BİLİNMEYEN ATIF:", ", ".join(sorted(BILINMEYEN)))
if kullanilmayan:
    print("Kullanılmayan kaynak:", ", ".join(kullanilmayan))
