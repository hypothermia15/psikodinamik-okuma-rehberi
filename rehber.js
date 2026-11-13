/* Psikodinamik Psikiyatri Okuma Rehberi — görünümler, vaka soruları, karışık test, kavram kartları,
   savunma oyunu, formülasyon şablonu, "odada kaç kişi var?", atıf penceresi, arama */
(function () {
  "use strict";
  var kok = document.documentElement;
  kok.classList.add("js");

  var ANAHTAR = "psikodinamik-okuma-rehberi:v1";
  var durum = oku();
  ["okundu", "test", "kart", "not", "form"].forEach(function (k) { durum[k] = durum[k] || {}; });
  function oku() { try { return JSON.parse(localStorage.getItem(ANAHTAR) || "{}") || {}; } catch (e) { return {}; } }
  function yaz() { try { localStorage.setItem(ANAHTAR, JSON.stringify(durum)); } catch (e) { /* özel pencere */ } }

  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function kacis(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function parla(el) { el.classList.remove("parla"); void el.offsetWidth; el.classList.add("parla"); }
  function katla(s) { return s.toLocaleLowerCase("tr").replace(/ı/g, "i").normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function kucukHarf(s) { return s.toLocaleLowerCase("tr"); }
  function karistir(a) {
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }

  var gorunumler = $$(".view");
  var bolumler = gorunumler.filter(function (v) { return !!v.querySelector(".okundu"); });
  var etkin = null;
  function baslik(v) { return v.getAttribute("data-baslik") || ""; }
  function adres(v) { return v.dataset.view === "giris" ? "#/" : "#/" + v.dataset.view; }

  /* Önceki / sonraki bağlantıları */
  gorunumler.forEach(function (v, i) {
    var nav = $(".ileri-geri", v);
    if (!nav) return;
    var h = "";
    if (i > 0) h += '<a href="' + adres(gorunumler[i - 1]) + '"><span>← Önceki</span>' + kacis(baslik(gorunumler[i - 1])) + "</a>";
    if (i < gorunumler.length - 1) h += '<a href="' + adres(gorunumler[i + 1]) + '"><span>Sonraki →</span>' + kacis(baslik(gorunumler[i + 1])) + "</a>";
    nav.innerHTML = h;
  });

  /* Görünüm değiştirme */
  function goster(ad, alt, odakla) {
    var v = document.getElementById("v-" + ad) || document.getElementById("v-giris");
    ad = v.dataset.view;
    if (etkin !== v) {
      gorunumler.forEach(function (x) { x.classList.toggle("aktif", x === v); });
      etkin = v;
      $$(".yan a[data-nav]").forEach(function (a) {
        if (a.dataset.nav === ad) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
      });
      document.title = (ad === "giris" ? "" : baslik(v) + " · ") + "Psikodinamik Psikiyatri Okuma Rehberi · Doç. Dr. Miraç Barış Usta";
      atifKapat();
      if (ad === "giris") ilerlemeCiz();
      if (ad === "kavramlar") kartBaslat(false);
      if (ad === "oda") odaCiz();
    }
    menuKapat();
    var hedef = alt ? document.getElementById(ad + "-" + alt) : null;
    if (hedef) {
      hedef.scrollIntoView({ block: "start" });
    } else {
      window.scrollTo(0, 0);
      if (odakla !== false) { var h = $("h1, h2", v); if (h) h.focus({ preventScroll: true }); }
    }
  }

  function git(v, el) {
    if (location.hash !== adres(v)) history.pushState(null, "", adres(v));
    goster(v.dataset.view, null, false);
    var det = el.closest("details");
    if (det) det.open = true;
    el.scrollIntoView({ block: "center" });
    parla(el);
  }

  var ilk = true;
  function rota() {
    var h = location.hash || "";
    var m = h.match(/^#\/([\w-]*)(?:\/([\w-]+))?$/);
    var odak = !ilk;
    ilk = false;
    if (!h || h === "#" || (m && !m[1])) return goster("giris", null, odak);
    if (m) return goster(m[1], m[2], odak);
    var el = document.getElementById(decodeURIComponent(h.slice(1)));
    var v = el && el.closest(".view");
    if (v) { goster(v.dataset.view, null, false); el.scrollIntoView({ block: "center" }); parla(el); }
  }
  window.addEventListener("hashchange", rota);

  /* Mobil menü */
  var menuD = $(".menu-dugme");
  function menuKapat() {
    document.body.classList.remove("menu-acik");
    if (menuD) menuD.setAttribute("aria-expanded", "false");
  }
  if (menuD) menuD.addEventListener("click", function () {
    var acik = document.body.classList.toggle("menu-acik");
    menuD.setAttribute("aria-expanded", acik ? "true" : "false");
  });

  /* Vaka soruları */
  function etiket(kutu, bildi) {
    if (!kutu) return;
    var et = $(".sonuc-etiket", kutu);
    if (!et) { et = document.createElement("span"); et.className = "sonuc-etiket"; kutu.insertBefore(et, kutu.firstChild); }
    et.textContent = bildi ? "✓ Bildiniz" : "✗ Bu sefer olmadı";
  }
  function testUygula(m, k) {
    var dogru = +m.dataset.dogru, bildi = k === dogru;
    m.classList.add("cevaplandi");
    m.classList.toggle("bildi", bildi);
    m.classList.toggle("bilemedi", !bildi);
    $$("button[data-secenek]", m).forEach(function (b) {
      var s = +b.dataset.secenek;
      b.disabled = true;
      b.classList.toggle("secenek-dogru", s === dogru);
      b.classList.toggle("secenek-yanlis", s === k && !bildi);
      b.setAttribute("aria-pressed", s === k ? "true" : "false");
    });
    etiket($(".test-aciklama", m), bildi);
    return bildi;
  }
  function testTemizle(m) {
    m.classList.remove("cevaplandi", "bildi", "bilemedi");
    $$("button[data-secenek]", m).forEach(function (b) {
      b.disabled = false; b.classList.remove("secenek-dogru", "secenek-yanlis"); b.removeAttribute("aria-pressed");
    });
    var et = $(".sonuc-etiket", m);
    if (et) et.remove();
  }
  function say(vid) {
    var v = document.getElementById("v-" + vid);
    var maddeler = v ? $$(".adim-test .test-madde", v) : [];
    var cev = durum.test[vid] || {}, n = 0, d = 0;
    maddeler.forEach(function (m) {
      var y = cev[m.dataset.no];
      if (y === undefined || y === null) return;
      n++;
      if (String(y) === m.dataset.dogru) d++;
    });
    return { toplam: maddeler.length, n: n, d: d };
  }
  function skorYaz(vid) {
    var s = say(vid);
    var sk = $('[data-test-skor="' + vid + '"]');
    if (sk) sk.textContent = s.n ? (s.d + " / " + s.toplam + " doğru" + (s.n < s.toplam ? " · " + (s.toplam - s.n) + " soru kaldı" : "")) : "";
    var sf = $('[data-test-sifirla="' + vid + '"]');
    if (sf) sf.hidden = !s.n;
    durumGuncelle(vid);
  }
  function durumGuncelle(vid) {
    var t = say(vid), p = [];
    if (durum.okundu[vid]) p.push("✓ Okundu");
    if (t.n) p.push("Sorular " + t.d + "/" + t.toplam);
    var kart = $('[data-durum="' + vid + '"]');
    if (kart) kart.textContent = p.join(" · ");
    var nav = $('[data-durum-nav="' + vid + '"]');
    if (nav) nav.textContent = durum.okundu[vid] ? "✓" : "";
    var ok = bolumler.filter(function (v) { return durum.okundu[v.dataset.view]; }).length;
    var il = $("[data-ilerleme]");
    if (il) il.textContent = ok ? ok + " / " + bolumler.length + " bölüm okundu" : "";
  }

  /* Karışık test */
  var kAlan = $(".karisik-alan"), kListe = [], kSira = 0, kDogru = 0;
  function kGoster() {
    var butonlar = $(".karisik-dugmeler");
    if (kSira >= kListe.length) {
      var oran = kDogru / kListe.length;
      kAlan.innerHTML = '<p class="karisik-son">' + kDogru + " / " + kListe.length + " doğru</p><p>" +
        (oran >= 0.85 ? "Çok iyi. Kitabın kavramlarını kliniğe taşımaya hazırsınız."
          : oran >= 0.6 ? "İyi. Kaçırdığınız soruların bölümlerine, özellikle “Tartışmaya açık” kısımlarına dönmek iyi olur."
            : "Bölümlerin “Ana fikirler” ve “ÇRS’de karşılığı” kısımlarıyla başlamak iyi bir tekrar olur.") + "</p>";
      if (butonlar) butonlar.hidden = false;
      var b = $(".karisik-basla", butonlar);
      if (b) { b.textContent = "Yeniden başlat"; b.focus(); }
      return;
    }
    var asil = kListe[kSira], m = asil.cloneNode(true);
    testTemizle(m);
    m.removeAttribute("data-ara");
    var kaynak = asil.closest(".view");
    kAlan.innerHTML = '<p class="karisik-ilerleme">Soru ' + (kSira + 1) + " / " + kListe.length +
      ' · <a href="' + adres(kaynak) + '/test">' + kacis(baslik(kaynak)) + "</a></p>";
    var ol = document.createElement("ol");
    ol.className = "test sina-tek";
    ol.appendChild(m);
    kAlan.appendChild(ol);
    var ilkB = $("button[data-secenek]", m);
    if (ilkB) ilkB.focus();
  }
  $$(".karisik-basla").forEach(function (b) {
    b.addEventListener("click", function () {
      kListe = karistir($$(".view .adim-test .test-madde"));
      kSira = 0; kDogru = 0;
      var butonlar = $(".karisik-dugmeler");
      if (butonlar) butonlar.hidden = true;
      kGoster();
    });
  });
  function kSonraki(bildi) {
    if (bildi) kDogru++;
    var sn = document.createElement("button");
    sn.type = "button";
    sn.className = "dugme karisik-sonraki";
    sn.textContent = kSira + 1 < kListe.length ? "Sonraki soru →" : "Sonucu gör";
    kAlan.appendChild(sn);
    sn.focus();
  }

  /* Kavram kartları */
  var kartlar = $$(".kavram").map(function (li) {
    return { id: li.dataset.id, on: $(".kavram-terim", li).textContent.trim(),
      arka: '<p class="kavram-tanim">' + $(".kavram-tanim", li).innerHTML + "</p>" + '<p class="kavram-ornek">' +
        $(".kavram-ornek", li).innerHTML + "</p>", ref: $(".ders-ref", li).innerHTML };
  });
  var deste = [], dSira = 0, kSahne = $(".kart-sahne");
  function kartBaslat(karisik) {
    if (!kSahne) return;
    var bilinmeyen = kartlar.filter(function (k) { return !durum.kart[k.id]; });
    var bilinen = kartlar.filter(function (k) { return durum.kart[k.id]; });
    deste = (karisik ? karistir(bilinmeyen) : bilinmeyen).concat(karistir(bilinen));
    dSira = 0;
    kartCiz();
  }
  function kartIlerleme() {
    var bil = kartlar.filter(function (k) { return durum.kart[k.id]; }).length;
    var el = $(".kart-ilerleme");
    if (el) el.textContent = "Bilinen: " + bil + " / " + kartlar.length + (dSira < deste.length ? " · Kart " + (dSira + 1) + " / " + deste.length : "");
  }
  function kartCiz() {
    if (dSira >= deste.length) {
      kSahne.innerHTML = '<div class="bilgi-kart bitti"><p class="kart-on-metin">Deste bitti.</p>' +
        '<p>Bilmediğiniz kartlar bir sonraki turda önce gelir.</p><button type="button" class="dugme kart-yeniden">Yeniden başla</button></div>';
      kartIlerleme();
      return;
    }
    var k = deste[dSira];
    kSahne.innerHTML = '<div class="bilgi-kart" tabindex="0" role="button" aria-pressed="false" aria-label="Kartı çevir: ' + kacis(k.on) + '">' +
      '<div class="kart-yuz kart-on"><span class="kart-oturum">Kavram' + (durum.kart[k.id] ? " · biliniyor" : "") + "</span>" +
      '<p class="kart-on-metin">' + kacis(k.on) + '</p><span class="kart-ipucu">Çevirmek için tıklayın ya da boşluk tuşuna basın</span></div>' +
      '<div class="kart-yuz kart-arka"><span class="kart-oturum">' + kacis(k.on) + "</span>" + k.arka +
      '<p class="ders-ref">' + k.ref + "</p></div></div>" +
      '<div class="kart-dugmeler"><button type="button" class="dugme dugme-ikincil kart-tekrar">↺ Tekrar sor</button>' +
      '<button type="button" class="dugme kart-biliyorum">✓ Biliyorum</button></div>';
    kartIlerleme();
  }
  function kartCevir() {
    var k = $(".bilgi-kart:not(.bitti)", kSahne);
    if (!k) return;
    var c = k.classList.toggle("cevrildi");
    k.setAttribute("aria-pressed", c ? "true" : "false");
  }
  if (kSahne) kSahne.addEventListener("keydown", function (e) {
    if ((e.key === " " || e.key === "Enter") && e.target.classList.contains("bilgi-kart")) { e.preventDefault(); kartCevir(); }
  });

  /* Savunma oyunu */
  var DUZEY = { ilkel: "İlkel", nevrotik: "Nevrotik", olgun: "Olgun" };
  var svAlan = $(".sv-alan"), svBasla = $(".sv-basla"), svListe = [], svSira = 0, svS = 0, svD = 0, svSonDogru = false;
  function svVeri() {
    return $$(".sv-veri li").map(function (li) {
      return { dogru: li.dataset.dogru, duzey: li.dataset.duzey, cel: li.dataset.celdirici.split("|"),
        vinyet: $(".sv-vinyet", li).innerHTML, aciklama: $(".sv-aciklama", li).innerHTML };
    });
  }
  function duzeyRozet(d) { return '<span class="duzey duzey-' + d + '">' + DUZEY[d] + "</span>"; }
  function svGoster() {
    if (svSira >= svListe.length) {
      var n = svListe.length, onceki = durum.savunma || {};
      var en = Math.max(onceki.en || 0, svS + svD);
      durum.savunma = { s: svS, d: svD, n: n, en: en };
      yaz();
      svAlan.innerHTML = '<p class="karisik-son">' + svS + " / " + n + " savunma · " + svD + " / " + n + " düzey</p>" +
        "<p>En iyi toplam skorunuz: " + en + " / " + 2 * n + ". Savunmalar gerçek klinikte tek başına değil, birlikte ve bağlama göre " +
        "değişerek görülür; vinyetler öğretim amaçlı sadeleştirildi.</p>";
      svBasla.hidden = false;
      svBasla.textContent = "Yeniden oyna";
      svBasla.focus();
      return;
    }
    var c = svListe[svSira];
    var secenekler = karistir([c.dogru].concat(c.cel));
    svAlan.innerHTML = '<p class="karisik-ilerleme">Vinyet ' + (svSira + 1) + " / " + svListe.length + "</p>" +
      '<div class="sv-kart"><p class="sv-vinyet">' + c.vinyet + '</p><p class="sv-soru">Hangi savunma öne çıkıyor?</p>' +
      '<div class="tahmin-dugmeler" role="group" aria-label="Savunma">' +
      secenekler.map(function (s) { return '<button type="button" data-sv="' + kacis(s) + '">' + kacis(s) + "</button>"; }).join("") +
      '</div><div class="sv-duzey" hidden><p class="sv-soru">Hangi düzeyde?</p><div class="tahmin-dugmeler" role="group" aria-label="Düzey">' +
      Object.keys(DUZEY).map(function (d) { return '<button type="button" data-svd="' + d + '">' + DUZEY[d] + "</button>"; }).join("") +
      '</div></div><div class="sv-sonuc" hidden></div></div>';
    var b = $("button[data-sv]", svAlan);
    if (b) b.focus();
  }
  if (svBasla) svBasla.addEventListener("click", function () {
    svListe = karistir(svVeri());
    svSira = 0; svS = 0; svD = 0;
    svBasla.hidden = true;
    svGoster();
  });

  /* Formülasyon şablonu */
  var form = $("#formulasyon"), fDurum = $(".form-durum");
  var SUREKLI = { 1: "Belirgin destekleyici", 2: "Destekleyici ağırlıklı", 3: "Karma", 4: "Keşfedici ağırlıklı", 5: "Belirgin keşfedici" };
  function formOku() {
    var d = {};
    $$("[data-form]", form).forEach(function (el) { if (el.value && (el.type !== "range" || el.dataset.dokunuldu)) d[el.dataset.form] = el.value; });
    var sv = $$("[data-form-savunma]:checked", form).map(function (x) { return x.value; });
    var td = $$("[data-form-tedavi]:checked", form).map(function (x) { return x.value; });
    if (sv.length) d.savunmalar = sv;
    if (td.length) d.tedavi = td;
    return d;
  }
  function formYaz(d) {
    $$("[data-form]", form).forEach(function (el) {
      var v = d[el.dataset.form];
      if (el.type === "range") { el.value = v || "3"; if (v) el.dataset.dokunuldu = "1"; else delete el.dataset.dokunuldu; }
      else el.value = v || "";
    });
    $$("[data-form-savunma]", form).forEach(function (x) { x.checked = (d.savunmalar || []).indexOf(x.value) >= 0; });
    $$("[data-form-tedavi]", form).forEach(function (x) { x.checked = (d.tedavi || []).indexOf(x.value) >= 0; });
  }
  function formBos(d) { return !Object.keys(d).length; }
  var fZam = null;
  function formKaydet() {
    clearTimeout(fZam);
    fZam = setTimeout(function () {
      durum.form = formOku();
      yaz();
      if (fDurum) fDurum.textContent = formBos(durum.form) ? "" : "Taslak bu tarayıcıya kaydedildi.";
    }, 350);
  }
  function formBolumleri() {
    var d = formOku(), out = [];
    $$(".form-alan", form).forEach(function (alan) {
      var lab = $("label, legend", alan), ad = lab ? lab.textContent.trim() : "";
      var ta = $("textarea", alan);
      if (ta) { if (ta.value.trim()) out.push({ b: ad, s: [ta.value.trim()] }); return; }
      if (alan.classList.contains("form-oruntu")) {
        var o = ["oruntu_kendilik", "oruntu_oteki", "oruntu_duygu"].map(function (k) { return d[k]; });
        if (o.some(Boolean)) out.push({ b: ad, s: ["Kendilik: " + (o[0] || "–"), "Öteki: " + (o[1] || "–"), "Aradaki duygu: " + (o[2] || "–")] });
        return;
      }
      if ($("[data-form-savunma]", alan)) { if (d.savunmalar) out.push({ b: ad, s: [d.savunmalar.join(", ")] }); return; }
      if ($("[data-form-tedavi]", alan) && (d.surekli || d.tedavi)) {
        var s = [];
        if (d.surekli) s.push("Keşfedici–destekleyici süreklilikte konum: " + SUREKLI[d.surekli]);
        if (d.tedavi) s.push("Bileşenler: " + d.tedavi.join(", "));
        out.push({ b: ad, s: s });
      }
    });
    return out;
  }
  function formMetin() {
    var satir = ["Psikodinamik formülasyon (çalışma taslağı)", ""];
    formBolumleri().forEach(function (x) { satir.push(x.b, x.s.join("\n"), ""); });
    satir.push("Psikodinamik Psikiyatri Okuma Rehberi · miracbarisusta.com/psikodinamik-okuma-rehberi/");
    return satir.join("\n");
  }
  function formBaskiHazirla() {
    var h = '<h1>Psikodinamik formülasyon</h1><p class="baski-alt">Çalışma taslağı · ' + new Date().toLocaleDateString("tr-TR") +
      " · Psikodinamik Psikiyatri Okuma Rehberi</p>";
    var bl = formBolumleri();
    if (!bl.length) h += "<p>Form henüz boş.</p>";
    bl.forEach(function (x) { h += "<h2>" + kacis(x.b) + "</h2>" + x.s.map(function (y) { return "<p>" + kacis(y) + "</p>"; }).join(""); });
    var bas = $(".form-baski");
    if (bas.parentNode !== document.body) document.body.appendChild(bas);
    bas.innerHTML = h;
  }
  var fOnay = { ornek: 0, temizle: 0 };
  if (form) {
    formYaz(durum.form || {});
    if (!formBos(durum.form || {}) && fDurum) fDurum.textContent = "Kayıtlı taslak yüklendi.";
    form.addEventListener("input", function (e) { if (e.target.type === "range") e.target.dataset.dokunuldu = "1"; formKaydet(); });
    form.addEventListener("change", formKaydet);
    form.addEventListener("submit", function (e) { e.preventDefault(); });
    window.addEventListener("afterprint", function () { document.body.classList.remove("baski-form"); });
  }
  function formOrnek(btn) {
    if (!formBos(formOku()) && Date.now() - fOnay.ornek > 4000) {
      fOnay.ornek = Date.now();
      btn.textContent = "Taslağın üzerine yazılacak; yeniden tıklayın";
      return;
    }
    var d = {};
    $$("[data-form]", form).forEach(function (el) { if (el.dataset.ornek) d[el.dataset.form] = el.dataset.ornek; });
    d.savunmalar = $$("[data-form-savunma][data-ornek-secili]", form).map(function (x) { return x.value; });
    d.tedavi = $$("[data-form-tedavi][data-ornek-secili]", form).map(function (x) { return x.value; });
    formYaz(d);
    btn.textContent = "Örnek vakayı yükle";
    formKaydet();
    if (fDurum) fDurum.textContent = "Kurgusal örnek vaka yüklendi.";
  }
  function formTemizle(btn) {
    if (Date.now() - fOnay.temizle > 4000) {
      fOnay.temizle = Date.now();
      btn.textContent = "Emin misiniz? Silmek için yeniden tıklayın";
      return;
    }
    formYaz({});
    durum.form = {};
    yaz();
    btn.textContent = "Formu temizle";
    if (fDurum) fDurum.textContent = "Form temizlendi.";
  }
  function formKopyala() {
    var metin = formMetin();
    function bitti(ok) { if (fDurum) fDurum.textContent = ok ? "Metin panoya kopyalandı." : "Kopyalanamadı; metni elle seçip kopyalayın."; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(metin).then(function () { bitti(true); }, function () { bitti(eskiKopya(metin)); });
    } else bitti(eskiKopya(metin));
  }
  function eskiKopya(metin) {
    var ta = document.createElement("textarea");
    ta.value = metin; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
    document.body.appendChild(ta); ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    ta.remove();
    return ok;
  }

  /* Odada kaç kişi var? */
  var KISI = {}, IPUCU = {}, odaKur = false;
  $$(".oda-kisiler li").forEach(function (li) { KISI[li.dataset.id] = { ad: li.dataset.ad, in: li.dataset.in }; });
  $$(".oda-veri li").forEach(function (li) { IPUCU[li.dataset.kisi + "|" + li.dataset.bakan] = li.textContent; });
  var odaTemel = ["hekim", "anne", "baba", "cocuk"], odaEk = { kardes: false, ogretmen: false };
  function odaKisileri() { return odaTemel.concat(Object.keys(odaEk).filter(function (k) { return odaEk[k]; })); }
  function hucreAd(p, v) {
    var P = KISI[p];
    if (v === p) return P.in + " kendi gözündeki hâli";
    if (v === "gercek") return P.in + " gerçekte olduğu hâli";
    return KISI[v].in + " gözündeki " + kucukHarf(P.ad);
  }
  function hucreMetin(p, v) {
    var ip = IPUCU[p + "|" + v];
    if (ip) return ip;
    var P = kucukHarf(KISI[p].ad);
    if (v === p) return KISI[p].ad + " kendini nasıl görüyor? Bu imge görüşmede neyi koruyor, neyi gizliyor olabilir?";
    if (v === "gercek") return "Gerçek " + P + ", diğer imgeler ayıklandıkça görünür. Elinizdeki bilgiler hangi imgelerden geliyor?";
    return KISI[v].in + " gözünde " + P + " nasıl biri? Bu imge görüşmede nasıl ortaya çıkıyor ve kimin davranışını yönlendiriyor?";
  }
  function odaCiz() {
    var izgara = $(".oda-izgara");
    if (!izgara) return;
    odaKur = true;
    var k = odaKisileri(), n = k.length;
    $(".oda-sayi").innerHTML = "<b>" + n + "</b> kişi × (<b>" + n + "</b> + 1) = <b>" + n * (n + 1) + "</b> imge" +
      (n > 2 ? ' <span class="kucuk">· iki kişilik görüşmede 6</span>' : "");
    var h = '<table class="oda-tablo"><caption class="gizli">Her kişinin odadaki imgeleri</caption><thead><tr><th scope="col">Kişi</th>' +
      '<th scope="col">Kendi gözünde</th>' + k.map(function (v) { return '<th scope="col">' + kacis(KISI[v].in) + " gözünde</th>"; }).join("") +
      '<th scope="col">Gerçekte</th></tr></thead><tbody>';
    k.forEach(function (p) {
      h += '<tr><th scope="row">' + kacis(KISI[p].ad) + "</th>" + hucre(p, p, "kendi");
      k.forEach(function (v) { h += v === p ? '<td aria-hidden="true"></td>' : hucre(p, v, ""); });
      h += hucre(p, "gercek", "gercek") + "</tr>";
    });
    izgara.innerHTML = h + "</tbody></table>";
  }
  function hucre(p, v, sinif) {
    var ip = IPUCU[p + "|" + v] ? " ipuclu" : "";
    return '<td><button type="button" class="oda-hucre ' + sinif + ip + '" data-p="' + p + '" data-v="' + v + '" aria-pressed="false" ' +
      'aria-label="' + kacis(hucreAd(p, v)) + '">' + (ip ? "✦" : "·") + "</button></td>";
  }

  /* Mini notlar */
  $$("textarea[data-not]").forEach(function (t) {
    var id = t.dataset.not, zam = null;
    if (durum.not[id]) t.value = durum.not[id];
    t.addEventListener("input", function () {
      clearTimeout(zam);
      zam = setTimeout(function () {
        if (t.value.trim()) durum.not[id] = t.value; else delete durum.not[id];
        yaz();
      }, 400);
    });
  });

  /* İlerleme paneli */
  var silOnay = 0;
  function ilerlemeCiz() {
    var panel = $("#ilerlemem");
    if (!panel) return;
    var ok = bolumler.filter(function (v) { return durum.okundu[v.dataset.view]; }).length;
    var q = { n: 0, d: 0, t: 0 };
    bolumler.forEach(function (v) { var b = say(v.dataset.view); q.n += b.n; q.d += b.d; q.t += b.toplam; });
    var bil = kartlar.filter(function (k) { return durum.kart[k.id]; }).length;
    var sv = durum.savunma, fv = !formBos(durum.form || {});
    var var_ = ok || q.n || bil || sv || fv;
    panel.hidden = !var_;
    if (!var_) return;
    function kutu(ad, deger, alt, adr) {
      return '<a class="ilerleme-kutu" href="' + adr + '"><span class="ik-ad">' + ad + '</span><span class="ik-deger">' + deger +
        '</span><span class="ik-alt">' + alt + "</span></a>";
    }
    $(".ilerleme-kutular", panel).innerHTML =
      kutu("Okunan bölüm", ok + " / " + bolumler.length, ok ? "devam edin" : "henüz yok", "#/bolum-1") +
      kutu("Vaka soruları", q.d + " / " + q.t, q.n + " soru yanıtlandı", "#/tekrar") +
      kutu("Kavram kartları", bil + " / " + kartlar.length, "biliniyor", "#/kavramlar") +
      kutu("Savunma oyunu", sv ? sv.en + " / " + 2 * sv.n : "–", sv ? "en iyi toplam skor" : "henüz oynanmadı", "#/savunmalar") +
      kutu("Formülasyon", fv ? "Taslak var" : "–", fv ? "bu tarayıcıda kayıtlı" : "henüz başlanmadı", "#/formulasyon");
  }

  /* Atıf penceresi */
  var pop = $("#atif-pop"), aktifAtif = null;
  function atifKapat() {
    if (pop && !pop.hidden) { pop.hidden = true; if (aktifAtif && document.activeElement && pop.contains(document.activeElement)) aktifAtif.focus(); }
    aktifAtif = null;
  }
  function atifAc(a) {
    var li = document.getElementById(a.dataset.k);
    if (!li || !pop) return false;
    if (aktifAtif === a && !pop.hidden) { atifKapat(); return true; }
    var c = li.cloneNode(true), g = $(".kaynak-geri", c);
    if (g) g.remove();
    pop.innerHTML = "<p>" + c.innerHTML + '</p><p class="atif-alt"><a href="#/kaynakca" data-git="' + li.id +
      '">Kaynakçada gör</a><button type="button" class="atif-kapat">Kapat ✕</button></p>';
    pop.hidden = false;
    var r = a.getBoundingClientRect(), w = pop.offsetWidth, h = pop.offsetHeight, sx = window.scrollX, gen = document.documentElement.clientWidth;
    var ust = r.bottom + 8 + h > window.innerHeight && r.top - h - 8 > 64;
    pop.style.left = Math.max(12, Math.min(r.left, gen - w - 12)) + sx + "px";
    pop.style.top = window.scrollY + (ust ? r.top - h - 8 : r.bottom + 8) + "px";
    aktifAtif = a;
    return true;
  }

  /* Tıklamalar */
  document.addEventListener("click", function (e) {
    var t = e.target;
    var at = t.closest("a.atif");
    if (at && !e.ctrlKey && !e.metaKey) { if (atifAc(at)) e.preventDefault(); return; }
    var g = t.closest("[data-git]");
    if (g) {
      e.preventDefault();
      var hedef = document.getElementById(g.dataset.git);
      atifKapat();
      if (hedef) git(hedef.closest(".view"), hedef);
      return;
    }
    if (t.closest(".atif-kapat")) { atifKapat(); return; }
    if (pop && !pop.hidden && !t.closest("#atif-pop")) atifKapat();

    var sc = t.closest(".test-madde button[data-secenek]");
    if (sc && !sc.disabled) {
      var tm = sc.closest(".test-madde"), k = +sc.dataset.secenek, tb = testUygula(tm, k);
      if (tm.closest(".karisik-alan")) { kSonraki(tb); return; }
      var tv = tm.closest(".view").dataset.view;
      (durum.test[tv] = durum.test[tv] || {})[tm.dataset.no] = k;
      yaz();
      skorYaz(tv);
      return;
    }
    if (t.closest(".karisik-sonraki")) { kSira++; kGoster(); return; }
    var sf = t.closest("[data-test-sifirla]");
    if (sf) {
      var id = sf.getAttribute("data-test-sifirla");
      delete durum.test[id];
      yaz();
      $$("#v-" + id + " .adim-test .test-madde").forEach(testTemizle);
      skorYaz(id);
      return;
    }
    var ok = t.closest(".okundu");
    if (ok) {
      var o = ok.dataset.okundu;
      if (durum.okundu[o]) delete durum.okundu[o]; else durum.okundu[o] = true;
      yaz();
      ok.setAttribute("aria-pressed", durum.okundu[o] ? "true" : "false");
      durumGuncelle(o);
      return;
    }
    /* kavram kartları */
    if (t.closest(".bilgi-kart:not(.bitti)") && !t.closest("a")) { kartCevir(); return; }
    if (t.closest(".kart-biliyorum") || t.closest(".kart-tekrar")) {
      var kk = deste[dSira];
      if (t.closest(".kart-biliyorum")) durum.kart[kk.id] = 1;
      else { delete durum.kart[kk.id]; deste.splice(Math.min(deste.length, dSira + 4), 0, kk); }
      yaz();
      dSira++;
      kartCiz();
      var kartEl = $(".bilgi-kart", kSahne);
      if (kartEl) kartEl.focus();
      return;
    }
    if (t.closest(".kart-yeniden") || t.closest(".kart-karistir")) { kartBaslat(true); return; }
    if (t.closest(".kart-sifirla")) { durum.kart = {}; yaz(); kartBaslat(true); return; }
    /* savunma oyunu */
    var sv = t.closest("button[data-sv]");
    if (sv && !sv.disabled) {
      var c = svListe[svSira], dogruMu = sv.dataset.sv === c.dogru;
      svSonDogru = dogruMu;
      if (dogruMu) svS++;
      $$("button[data-sv]", svAlan).forEach(function (b) {
        b.disabled = true;
        b.classList.toggle("secenek-dogru", b.dataset.sv === c.dogru);
        b.classList.toggle("secenek-yanlis", b === sv && !dogruMu);
      });
      var dz = $(".sv-duzey", svAlan);
      dz.hidden = false;
      $("button[data-svd]", dz).focus();
      return;
    }
    var svd = t.closest("button[data-svd]");
    if (svd && !svd.disabled) {
      var c2 = svListe[svSira], dzDogru = svd.dataset.svd === c2.duzey, sDogru = svSonDogru;
      if (dzDogru) svD++;
      $$("button[data-svd]", svAlan).forEach(function (b) {
        b.disabled = true;
        b.classList.toggle("secenek-dogru", b.dataset.svd === c2.duzey);
        b.classList.toggle("secenek-yanlis", b === svd && !dzDogru);
      });
      var so = $(".sv-sonuc", svAlan);
      so.innerHTML = '<p><strong class="' + (sDogru ? "iyi" : "kotu") + '">' + (sDogru ? "✓ Savunma doğru." : "✗ Savunma: " + kacis(c2.dogru) + ".") +
        '</strong> <strong class="' + (dzDogru ? "iyi" : "kotu") + '">' + (dzDogru ? "✓ Düzey doğru." : "✗ Düzey başka:") + "</strong> " +
        duzeyRozet(c2.duzey) + "</p><p>" + c2.aciklama + '</p><button type="button" class="dugme sv-sonraki">' +
        (svSira + 1 < svListe.length ? "Sonraki vinyet →" : "Sonucu gör") + "</button>";
      so.hidden = false;
      $(".sv-sonraki", so).focus();
      return;
    }
    if (t.closest(".sv-sonraki")) { svSira++; svGoster(); return; }
    /* formülasyon */
    var fo = t.closest(".form-ornek");
    if (fo) { formOrnek(fo); return; }
    var ft = t.closest(".form-temizle");
    if (ft) { formTemizle(ft); return; }
    if (t.closest(".form-kopyala")) { formKopyala(); return; }
    if (t.closest(".form-yazdir")) { formBaskiHazirla(); document.body.classList.add("baski-form"); window.print(); return; }
    /* oda */
    var od = t.closest("button[data-oda]");
    if (od) {
      odaTemel = od.dataset.oda.split(",");
      $$("button[data-oda]").forEach(function (b) { b.setAttribute("aria-pressed", b === od ? "true" : "false"); });
      odaCiz();
      return;
    }
    var ok2 = t.closest(".oda-kisi");
    if (ok2) {
      var kisi = ok2.dataset.kisi;
      odaEk[kisi] = !odaEk[kisi];
      ok2.setAttribute("aria-pressed", odaEk[kisi] ? "true" : "false");
      odaCiz();
      return;
    }
    var oh = t.closest(".oda-hayalet");
    if (oh) {
      var hy = $(".oda-hayaletler"), ac = hy.hidden;
      hy.hidden = !ac;
      oh.setAttribute("aria-pressed", ac ? "true" : "false");
      oh.textContent = ac ? "Odaya girmeyenleri gizle" : "Odaya girmeyenleri göster";
      return;
    }
    var hc = t.closest(".oda-hucre");
    if (hc) {
      $$(".oda-hucre").forEach(function (b) { b.setAttribute("aria-pressed", b === hc ? "true" : "false"); });
      $(".oda-ipucu").innerHTML = "<p><strong>" + kacis(hucreAd(hc.dataset.p, hc.dataset.v)) + ".</strong> " +
        kacis(hucreMetin(hc.dataset.p, hc.dataset.v)) + "</p>";
      return;
    }
    var hs = t.closest(".hepsini-sil");
    if (hs) {
      if (Date.now() - silOnay > 4000) { silOnay = Date.now(); hs.textContent = "Emin misiniz? Silmek için yeniden tıklayın"; return; }
      durum = { okundu: {}, test: {}, kart: {}, not: {}, form: {} };
      yaz();
      location.reload();
      return;
    }
    if (document.body.classList.contains("menu-acik") && !t.closest(".yan, .menu-dugme")) menuKapat();
    if (araS && !araS.hidden && !t.closest(".ara")) araS.hidden = true;
  });

  /* Kaynakça süzgeci */
  var ksuz = $("#kaynak-suz");
  if (ksuz) ksuz.addEventListener("input", function () {
    var q = katla(ksuz.value.trim()), n = 0;
    $$(".kaynaklar li").forEach(function (li) {
      var g = !q || katla(li.textContent).indexOf(q) >= 0;
      li.hidden = !g;
      if (g) n++;
    });
    $(".kaynak-sonuc").textContent = q ? n + " kaynak bulundu." : "";
  });

  /* Arama */
  var araK = $("#ara"), araS = $("#ara-sonuc"), dizin = null;
  function dizinKur() {
    dizin = $$("[data-ara]").filter(function (el) { return !el.closest(".karisik-alan") && el.closest(".view"); }).map(function (el) {
      var v = el.closest(".view"), adim = el.closest(".adim, .tema"), yer = baslik(v);
      if (adim) { var h = $("h3", adim); if (h) yer += " › " + h.textContent.trim(); }
      var t = el.textContent.replace(/\s+/g, " ").trim();
      return { el: el, v: v, yer: yer, t: t, k: katla(t) };
    });
  }
  function parcacik(d, terim) {
    var i = d.k.indexOf(terim);
    if (i < 0) i = 0;
    var bas = Math.max(0, i - 50), son = Math.min(d.t.length, i + terim.length + 110);
    return (bas ? "…" : "") + kacis(d.t.slice(bas, i)) + "<mark>" + kacis(d.t.slice(i, i + terim.length)) + "</mark>" +
      kacis(d.t.slice(i + terim.length, son)) + (son < d.t.length ? "…" : "");
  }
  function ara() {
    var q = araK.value.trim();
    if (q.length < 2) { araS.hidden = true; return; }
    if (!dizin) dizinKur();
    var terimler = katla(q).split(/\s+/).filter(Boolean), sonuc = [];
    for (var i = 0; i < dizin.length && sonuc.length < 40; i++) {
      var d = dizin[i];
      if (terimler.every(function (t) { return d.k.indexOf(t) >= 0; })) sonuc.push(i);
    }
    araS.innerHTML = sonuc.length ? sonuc.map(function (i) {
      return '<button type="button" data-i="' + i + '"><span class="yer">' + kacis(dizin[i].yer) + "</span>" + parcacik(dizin[i], terimler[0]) + "</button>";
    }).join("") + (sonuc.length === 40 ? '<p class="bos">İlk 40 sonuç gösteriliyor; aramayı daraltın.</p>' : "")
      : '<p class="bos">“' + kacis(q) + "” için sonuç yok.</p>";
    araS.hidden = false;
  }
  if (araK) {
    var zam = null;
    araK.addEventListener("input", function () { clearTimeout(zam); zam = setTimeout(ara, 120); });
    araK.addEventListener("focus", function () { if (araK.value.trim().length >= 2) ara(); });
    araK.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { araS.hidden = true; araK.blur(); }
      else if (e.key === "ArrowDown" || e.key === "Enter") { var b = $("button", araS); if (b && !araS.hidden) { e.preventDefault(); if (e.key === "Enter") b.click(); else b.focus(); } }
    });
    araS.addEventListener("keydown", function (e) {
      var bs = $$("button", araS), i = bs.indexOf(document.activeElement);
      if (e.key === "ArrowDown" && i < bs.length - 1) { e.preventDefault(); bs[i + 1].focus(); }
      else if (e.key === "ArrowUp") { e.preventDefault(); if (i > 0) bs[i - 1].focus(); else araK.focus(); }
      else if (e.key === "Escape") { araS.hidden = true; araK.focus(); }
    });
    araS.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-i]");
      if (!b) return;
      var d = dizin[+b.dataset.i];
      araS.hidden = true;
      git(d.v, d.el);
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { atifKapat(); menuKapat(); }
    if (e.key === "/" && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName) && araK) { e.preventDefault(); araK.focus(); }
  });

  /* Kayıtlı durumu geri yükle */
  Object.keys(durum.test).forEach(function (vid) {
    var v = document.getElementById("v-" + vid);
    if (!v) return;
    $$(".adim-test .test-madde", v).forEach(function (m) { var y = durum.test[vid][m.dataset.no]; if (y !== undefined && y !== null) testUygula(m, +y); });
  });
  gorunumler.forEach(function (v) {
    var vid = v.dataset.view, b = $(".okundu", v);
    if (b) b.setAttribute("aria-pressed", durum.okundu[vid] ? "true" : "false");
    skorYaz(vid);
  });

  rota();
})();
