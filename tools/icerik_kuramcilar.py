# -*- coding: utf-8 -*-
"""Psikodinamik Psikiyatri Okuma Rehberi: kuramcı kartları.

Kartlar, kitabın özellikle 2. bölümünde ve ilgili klinik bölümlerde anılan kuramcıları tanıtır. Metinler özgündür;
kitaptan alıntı yoktur. "bolumler" alanı kuramcının kitapta en çok anıldığı ve bu rehberde işlenen bölümleri gösterir.

Fotoğraf: bu depoda kuramcı fotoğrafı yoktur. Bir kart için görsel eklemek isterseniz dosyayı `gorseller/<anahtar>.jpg`
(ya da .png, .webp) adıyla koyun ve aşağıdaki GORSEL_KUNYE sözlüğüne kaynağını ve lisansını yazın. Künyesi olmayan görsel
sayfaya eklenmez. Görsel yoksa kartta kuramcının baş harfleri gösterilir.
"""

EKOLLER = {
    "klasik": ("Klasik psikanaliz", "Dürtü, çatışma ve bilinçdışı"),
    "ego": ("Ego psikolojisi", "Savunmalar, uyum ve ego işlevleri"),
    "nesne": ("Nesne ilişkileri", "İçselleştirilmiş ilişkiler"),
    "kendilik": ("Kendilik psikolojisi", "Bütünlük, özsaygı ve empati"),
    "gelisim": ("Bağlanma ve gelişim", "Gözlem, bağlanma ve zihinselleştirme"),
    "iliskisel": ("İlişkisel yaklaşım", "İki kişilik psikoloji"),
}

# anahtar: {"dosya": "freud.jpg", "kaynak": "https://…", "lisans": "Kamu malı / CC BY-SA 4.0 …", "sahibi": "Fotoğrafçı ya da kurum"}
GORSEL_KUNYE = {}

# (anahtar, ad, doğum, ölüm ya da None, ekol, tek cümle, kitaptaki yeri, ÇRS'de, kavramlar, bölümler)
KURAMCILAR = [
    ("freud", "Sigmund Freud", 1856, 1939, "klasik",
     "Belirtinin bir anlamı olduğunu ve bu anlamın çoğu kez bilinç dışında kaldığını öne sürdü.",
     "Kitabın başlangıç noktasıdır: bilinçdışı, çatışma, aktarım ve direnç kavramları onunla girer. Savunmalar içinde en çok "
     "bastırma üzerinde durmuştur. Sonraki kuramların çoğu onun dürtü kuramına yanıt olarak okunabilir.",
     "Çocukta belirtiyi “ne anlatıyor?” diye sormak bu mirastır; yanıtı ise bugün gelişim ve aile bağlamıyla birlikte aranır.",
     ["Aktarım", "Direnç", "Savunma mekanizması"], [1, 2, 8]),
    ("klein", "Melanie Klein", 1882, 1960, "nesne",
     "İç dünyayı, bebeğin ilk aylarından başlayan iyi ve kötü nesne ilişkileriyle anlattı.",
     "Paranoid-şizoid ve depresif konum ayrımı kitapta bölme ve yansıtmalı özdeşimi anlamanın zeminidir. Depresyon bölümünde "
     "saldırganlığın içe dönmesi fikriyle birlikte anılır.",
     "“Hep iyi” ve “hep kötü” arasında gidip gelen çocuğu ya da ekibi ikiye bölen ergeni düşünürken yararlı bir mercektir.",
     ["Bölme", "Yansıtmalı özdeşim"], [2, 8]),
    ("fairbairn", "W. R. D. Fairbairn", 1889, 1964, "nesne",
     "İnsanın haz değil ilişki aradığını savundu; içselleştirilenin nesne değil, ilişkinin kendisi olduğunu vurguladı.",
     "Dürtü kuramından en çok uzaklaşan nesne ilişkileri kuramcısı olarak sunulur. Şizoid hastaları, ilişki isteği ile "
     "ihtiyaçlarının ötekine zarar vereceği korkusu arasındaki çatışmayla açıklar.",
     "Kötü muamele gören çocuğun bakımverenine bağlı kalması, “ilişki arayışı” fikriyle daha anlaşılır olur.",
     ["Bölme"], [2, 10]),
    ("hartmann", "Heinz Hartmann", 1894, 1970, "ego",
     "Egonun çatışmadan bağımsız, uyuma hizmet eden bir alanı olduğunu öne sürdü.",
     "Ego psikolojisinin “uyum” bakışını temsil eder: algı, bellek, dil ve hareket gibi işlevler çatışmanın ürünü olmak "
     "zorunda değildir.",
     "Dil bozukluğu, disleksi ya da zihinsel yetersizlik “direnç” değildir; önce kapasite değerlendirilir.",
     ["Çatışmasız ego alanı"], [2]),
    ("annafreud", "Anna Freud", 1895, 1982, "ego",
     "Savunma düzeneklerini sistemli biçimde tanımladı ve çocuk analizinin kurucularından oldu.",
     "Savunmaların çeşitliliği ve terapistin id, ego, süperego ve dış gerçeklik karşısındaki eşit uzaklığı fikriyle anılır.",
     "Çocuğun savunmasını yıkmak yerine anlamak ve gelişim çizgisine göre değerlendirmek onun mirasıdır.",
     ["Savunma mekanizması", "Tarafsızlık", "Saldırganla özdeşleşme"], [2, 4]),
    ("winnicott", "Donald W. Winnicott", 1896, 1971, "nesne",
     "Bebeği bakımından ayrı düşünmenin mümkün olmadığını, gelişimin “yeterince iyi” bir çevre istediğini söyledi.",
     "Yeterince iyi anne, tutan çevre ve geçiş nesnesi kavramları kitapta hem gelişimi hem tedavi ortamını anlatmak için "
     "kullanılır; servis ve ekip çalışması ile narsisizm bölümlerinde yeniden karşımıza çıkar.",
     "Çocuk psikiyatrisinde hastanın her zaman bir sistem olduğu fikrinin en yalın ifadesidir.",
     ["Yeterince iyi bakım", "Geçiş nesnesi", "Sahte kendilik"], [2, 6, 15, 16]),
    ("balint", "Michael Balint", 1896, 1970, "nesne",
     "Bazı hastalardaki “bir şey eksik” duygusunu erken bakımdaki yetersizliğe bağladı.",
     "“Temel kusur” kavramıyla, çatışmadan çok eksiklikle açıklanan tabloların öncülerinden biri olarak anılır.",
     "Erken yoksunluk yaşamış çocukta yorumdan önce güvenilir ve sürekli bir ilişkinin gerektiğini hatırlatır.",
     [], [2, 12]),
    ("bion", "Wilfred R. Bion", 1897, 1979, "nesne",
     "Grupların görünen işinin altında, kaygıyı yöneten ortak varsayımlar bulunduğunu gösterdi.",
     "Grup terapisi bölümünde temel varsayım gruplarıyla, ekip bölümünde ise katlanılmaz duyguların kapsanması fikriyle yer alır.",
     "Vaka toplantısında ekibin birden suçlu aramaya başlaması bir temel varsayım örneği olarak okunabilir.",
     ["Kapsama", "Temel varsayım grubu"], [5, 6, 15]),
    ("mahler", "Margaret S. Mahler", 1897, 1985, "gelisim",
     "Bebek ve küçük çocuk gözlemleriyle ayrılma-bireyleşme sürecini tanımladı.",
     "Gözleme dayalı ilk gelişim çalışmalarından biri olarak, ego psikolojisi ile nesne ilişkileri kuramı arasında köprü sayılır.",
     "İki yaşındaki çocuğun hem yapışıp hem itmesi, yakınlaşma evresinin gündelik görünümüdür.",
     ["Yakınlaşma evresi"], [2, 15]),
    ("bowlby", "John Bowlby", 1907, 1990, "gelisim",
     "Çocuğun bakımverenine bağlanmasını hayatta kalmaya hizmet eden temel bir sistem olarak tanımladı.",
     "Bağlanma kuramı kitapta gelişim anlayışının ampirik ayağıdır; depresyon bölümünde kayıp ve ayrılıkla birlikte ele alınır.",
     "Bağlanma örüntüsü bir risk göstergesidir, tek başına tanı ya da adli kanıt değildir.",
     ["Dezorganize bağlanma"], [2, 8]),
    ("kohut", "Heinz Kohut", 1913, 1981, "kendilik",
     "Kendiliğin bütünlüğünü, başkalarından alınan aynalama ve idealleştirme deneyimlerine bağladı.",
     "Kendilik psikolojisinin kurucusudur. Narsisizm bölümünde Kernberg ile karşılaştırılır: Kohut eksikliği ve empatiyi, "
     "hastanın yaşantısının olumlu yanını öne çıkarır.",
     "Ergenin akranlara, idollere ve ideallere tutunması, kendilik desteğinin ebeveynden dışarı taşınmasıdır.",
     ["Kendilik nesnesi", "Utanç", "Kayıtsız ve aşırı tetikte narsisizm"], [2, 16]),
    ("kernberg", "Otto F. Kernberg", 1928, None, "nesne",
     "Ego psikolojisi ile nesne ilişkileri kuramını birleştirdi; kişilik örgütlenmesinin düzeylerini tanımladı.",
     "Sınır ve narsisistik kişilik bölümlerinin ana seslerindendir. Kohut'un aksine erken olumsuz aktarımın sistemli biçimde "
     "ele alınmasını ve saldırganlığın yorumlanmasını savunur.",
     "Ergende kimlik dağınıklığı ile olağan ergenlik krizini ayırmak, onun yapısal bakışının güncel kullanımıdır.",
     ["Bölme", "Kayıtsız ve aşırı tetikte narsisizm"], [2, 15, 16, 17]),
    ("stern", "Daniel N. Stern", 1934, 2012, "gelisim",
     "Bebek gözlemleriyle kendilik duyumunun doğumdan başlayarak katman katman geliştiğini gösterdi.",
     "Gözleme dayalı gelişim kuramının temsilcisidir; hastanın yaşam öyküsünü anlatırken ortaya çıkan “anlatısal kendilik” "
     "fikri kitapta onunla anılır.",
     "Erken ebeveyn-bebek etkileşimini doğrudan gözlemek, çocuk psikiyatrisinin değerlendirme yöntemidir.",
     [], [2, 13]),
    ("vaillant", "George E. Vaillant", 1934, None, "ego",
     "Savunmaları olgunluk düzeylerine göre sıraladı ve bu sıralamayı on yıllar süren izlemle sınadı.",
     "Savunma hiyerarşisinin ampirik dayanağıdır. Madde kullanımı bölümünde hastalık modeline ilişkin boylamsal "
     "çalışmalarıyla yeniden karşımıza çıkar.",
     "Ergende ilkel savunma bir durak olabilir, varış noktası değil; savunmalar yaşla olgunlaşabilir.",
     ["Savunma mekanizması"], [2, 8, 12]),
    ("ogden", "Thomas H. Ogden", 1946, None, "nesne",
     "Yansıtmalı özdeşimi yalnızca iç dünyada değil, iki kişi arasında yaşanan bir süreç olarak tanımladı.",
     "Kitapta yansıtmalı özdeşimin kişilerarası okuması onun modeline dayanır; ekip bölümlerinde hastanın iç dünyasının "
     "serviste nasıl sahnelendiğini anlamaya yarar.",
     "Bir çocuğun ekipte herkese aynı çaresizliği hissettirmesi, bu sürecin klinikteki izidir.",
     ["Yansıtmalı özdeşim", "Kapsama"], [2, 6, 7]),
    ("mitchell", "Stephen A. Mitchell", 1946, 2000, "iliskisel",
     "Terapiyi tek kişinin iç dünyası olarak değil, iki öznenin karşılıklı etkilediği bir alan olarak ele aldı.",
     "İlişkisel yaklaşımın temsilcisi olarak anılır; terapistin tarafsız bir ekran olmadığı, sürecin ortak yaratıldığı "
     "görüşü onunla girer.",
     "Ergenle çalışırken klinisyenin kendi tepkilerini veri saymasının kuramsal dayanaklarından biridir.",
     ["Karşı aktarım"], [2, 4, 12]),
    ("fonagy", "Peter Fonagy", 1952, None, "gelisim",
     "Kendi ve başkalarının davranışını zihin durumlarıyla anlama kapasitesini, zihinselleştirmeyi tanımladı.",
     "Bağlanma kuramını klinik uygulamaya taşır. Sınır kişilik bölümünde Bateman ile geliştirdiği zihinselleştirme temelli "
     "tedavi ayrıntılı ele alınır; travma bölümünde de sık anılır.",
     "Ergenin duygusu yükseldiğinde zihinselleştirmesinin çökmesi, kendine zarar verme anlarını anlamada işe yarar.",
     ["Mentalizasyon", "Psişik eşdeğerlik", "Yabancı kendilik"], [2, 10, 15]),
]
