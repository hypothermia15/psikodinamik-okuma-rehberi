# -*- coding: utf-8 -*-
"""Psikodinamik Psikiyatri Okuma Rehberi: araçların içerikleri.

Kavram tanımları, savunma vinyetleri, formülasyon şablonu, ergenlik notları ve "odada kaç kişi var?"
metinleri özgündür; kitaptan alıntı ya da kitabın vakaları yoktur. Vinyetler kurgusaldır.
"""

# ---------------------------------------------------------------------------
# Kavram kartları: (terim, tanım, ÇRS'de nasıl görünür, [bölüm numaraları])
KAVRAMLAR = [
    ("Aktarım", "Geçmiş ilişkilerden gelen beklenti ve duyguların bugünkü bir ilişkiye, özellikle klinisyene taşınması.",
     "Ergenin ilk görüşmede “sen de babam gibisin” demesi.", [1, 4]),
    ("Karşı aktarım", "Klinisyenin hastaya karşı duygusal tepkilerinin bütünü; hem klinisyenin kendi geçmişinden hem hastanın "
     "ilişki örüntüsünden beslenir.", "“Bu çocuk beni çileden çıkarıyor” duygusunu eyleme dökmeden önce adlandırmak.", [1, 6]),
    ("Direnç", "Tedavide değişime ya da farkındalığa karşı devreye giren koruyucu güçler; bir engel değil, neyden korunulduğuna dair bilgi.",
     "Seansa geç gelme, susma, “bilmiyorum” yanıtları.", [4]),
    ("Savunma mekanizması", "Kaygı ve dayanılmaz duygularla baş etmek için kullanılan, çoğunlukla farkındalık dışındaki zihinsel işlemler.",
     "Kardeşi doğunca altını yeniden ıslatmaya başlayan dört yaşındaki çocuk.", [2]),
    ("Bölme", "Kendilik ve ötekilerin “tümüyle iyi” ve “tümüyle kötü” parçalara ayrılması; iki yanın aynı kişide birlikte tutulamaması.",
     "Ekipte “iyi hemşire” ve “kötü hemşire” kutuplaşması.", [2, 6, 15]),
    ("Yansıtmalı özdeşim", "Kişinin dayanamadığı bir duyguyu ötekine yansıtması ve ötekinin o duyguyu gerçekten hissetmeye başlaması.",
     "Çaresiz bir çocuğun yanında kendini çaresiz ve yetersiz hisseden klinisyen.", [2, 6, 16]),
    ("Kapsama", "Bir ötekinin dayanılmaz duyguları alıp sindirerek daha katlanılabilir bir biçimde geri vermesi.",
     "Terapistin ergenin öfkesine karşılık vermeden onu adlandırabilmesi.", [2, 15]),
    ("Yeterince iyi bakım", "Mükemmel değil, ama çocuğun ihtiyaçlarına yeterince duyarlı olan ve zamanla dozlanmış hayal kırıklıklarına "
     "izin veren bakım.", "Ebeveynin hatasını onarabilmesi, hiç hata yapmamasından daha önemlidir.", [2]),
    ("Sahte kendilik", "Bakım verenin beklentilerine uyum sağlamak için kendi duygu ve isteklerini geri çeken çocukta gelişen uyumlu "
     "ama içi boş bir kendilik.", "“Hiç sorun çıkarmayan” çocuk.", [2]),
    ("Kendilik nesnesi", "Kişinin kendilik bütünlüğünü sürdürmek için gereksindiği, ayna tutan ya da idealleştirilebilen öteki.",
     "Ergenin idolleri, akran grubu ve hayranlık duyduğu öğretmeni.", [2, 16]),
    ("Mentalizasyon", "Kendi ve başkalarının davranışını duygu, istek ve inanç gibi zihinsel durumlarla anlamlandırma kapasitesi.",
     "“Arkadaşın mesajına neden yanıt vermemiş olabilir?” sorusuna birden çok olasılık üretebilmek.", [2, 13, 15]),
    ("Psişik eşdeğerlik", "Zihindekinin dış gerçeklikle aynı sayıldığı düşünme kipi: “hissediyorsam gerçektir.”",
     "“Benden nefret ettiğini biliyorum, yüzünden belli.”", [15]),
    ("Yabancı kendilik", "Bakım verenden alınan ve kişinin kendisine ait olmayan zalim ya da boş bir parça olarak içte taşınan temsil.",
     "Ergenin ardı ardına onu küçümseyen ilişkiler bulması.", [15]),
    ("Terapötik ittifak", "Hasta ile klinisyenin ortak hedefler ve görevler üzerinde kurduğu iş birliği ve bağ.",
     "Çocuk, anne, baba ve okulla ayrı ayrı kurulan ittifaklar.", [4, 5]),
    ("İçgörü üçgeni", "Şimdiki ilişkiler, geçmiş ilişkiler ve terapistle ilişki arasındaki örüntü benzerliğini birlikte görmeye yarayan çerçeve.",
     "Zorbalığa uğrayan çocukta okul, ev ve terapi odasındaki edilgenliği birlikte düşünmek.", [4]),
    ("Yardımcı ego", "Klinisyenin, hastada henüz yeterli olmayan işlevleri (duygu adlandırma, öngörü, sınır) geçici olarak üstlenmesi.",
     "“Şu an çok öfkelisin; bu öfkeyle yarın okulda ne olabilir, birlikte düşünelim.”", [4]),
    ("Tarafsızlık", "Hastanın iç çatışmalarında taraf tutmama; soğukluk ya da yasal yükümlülüklerden kaçınma değildir.",
     "Boşanan ebeveynlerden birinin safına geçmemek, ama istismar bildirimini yapmak.", [4, 5, 17]),
    ("Çatışmasız ego alanı", "Algı, bellek ve dil gibi çatışmadan bağımsız gelişen işlevler; bunlardaki sınırlılık direnç sayılmamalıdır.",
     "Disleksi olan çocuğun “okumak istemiyor” diye etiketlenmesi.", [2]),
    ("Yakınlaşma evresi", "Yaklaşık 15–24. aylar arasında özerklik ile bakım verene yakınlık ihtiyacı arasında gidip gelme dönemi.",
     "Annesine bir yapışan bir onu iten iki yaşındaki çocuk.", [2]),
    ("Geçiş nesnesi", "Çocuğun bakım verenden ayrılmasını kolaylaştıran ve hem kendisine hem dış dünyaya ait sayılan nesne.",
     "Uykuya battaniyesiyle giden çocuk; kimi hastada ilacın da benzer bir işlev görmesi.", [2, 5]),
    ("Dezorganize bağlanma", "Bebeğin, hem güvenlik hem korku kaynağı olan bakım verene karşı tutarlı bir strateji geliştirememesi.",
     "Bakım verene yaklaşırken donakalan ya da yönünü kaybeden bebek.", [2, 10]),
    ("Belirlenmiş hasta", "Aile sisteminin gerginliğini taşıyan ve ailenin “hasta” olarak getirdiği üye.",
     "Çocuk düzelince ebeveynlerin kavgalarının artması.", [5]),
    ("Günah keçisi", "Grubun tahammül edemediği duyguların bir üyeye yüklenmesi ve o üyenin bu rolü üstlenmesi.",
     "Sınıfın hep aynı çocuğu hedef alması.", [5]),
    ("Temel varsayım grubu", "Grubun açık görevi yerine kaygıyla baş etmek için farkında olmadan benimsediği ortak varsayım: bağımlılık, "
     "savaş ya da kaç, eşleşme.", "Ekibin bütün umudunu tek bir hocaya bağlaması ya da hep birlikte bir “düşman”a yönelmesi.", [5, 6]),
    ("İfade edilen duygu", "Aile üyelerinin hastaya yönelik eleştiri, düşmanlık ve duygusal aşırı katılım düzeyi.",
     "“Yine mi uyudun, hiçbir şey olamayacaksın” gibi sık eleştirel yorumlar.", [5, 7, 8]),
    ("Vicdandaki boşluk", "Vicdanın genel olarak sağlam olduğu bir kişide belirli bir davranış alanına özgü vicdani boşluk.",
     "Çocuğun hırsızlığına gizlice gülümseyen ebeveyn.", [17]),
    ("Saldırganla özdeşleşme", "Edilgen olarak yaşanan bir şiddetin etkin biçimde başkalarına uygulanması.",
     "İstismara uğramış çocuğun daha küçük kardeşlerine benzer biçimde davranması.", [10]),
    ("Yineleme", "Kişinin acı veren ilişki örüntülerini farkında olmadan tekrar etmesi.",
     "Yeni koruyucu ailesinin yanında eski evindeki çatışmaları yeniden sahneleyen çocuk.", [6, 10]),
    ("Anaklitik ve içe atımsal depresyon", "İlişki ve bakım kaybına odaklanan (anaklitik) ile başarısızlık ve öz-eleştiriye odaklanan "
     "(içe atımsal) iki depresyon görünümü.", "“Kimse beni sevmiyor” ile “yeterince iyi değilim.”", [8]),
    ("Öz-bakım kapasitesi", "Tehlikeyi öngörme ve kendini koruma becerisi; bağımlılıkta eksikliği merkezi bir kavramdır.",
     "Riskli durumları sonuçlarını düşünmeden tekrarlayan ergen.", [12]),
    ("Yıkım tepkisi", "Kapasitesinin üstündeki bir görevle karşılaşan kişinin yaşadığı ani ve yoğun dağılma tepkisi.",
     "Beklenmedik bir değişiklikten sonra öfke nöbeti geçiren otizmli çocuk.", [13]),
    ("Kayıtsız ve aşırı tetikte narsisizm", "Narsisistik sürekliliğin iki ucu: başkalarının tepkisine kayıtsız büyüklenmeci tip ve "
     "eleştiriye aşırı duyarlı, utanç dolu tip.", "Gürültülü, övünen ergen ile sessiz, kırılgan ve kaçınan ergen.", [16]),
    ("Utanç", "Kendiliğin bütünüyle kusurlu olduğu hissi; suçluluktan farklı olarak bir eylemle değil varoluşla ilgilidir.",
     "Başarısızlıktan sonra saklanan, göz teması kuramayan ergen.", [16]),
    ("Dissosiyasyon", "Bilinç, bellek, kimlik ya da algının olağan bütünlüğünün kesintiye uğraması; dayanılmaz deneyim karşısında "
     "“orada olmamak.”", "Bağırışlar başladığında gözleri boşalan çocuk.", [10]),
    ("Bölünmüş tedavi", "İlaç ve psikoterapinin farklı klinisyenlerce yürütüldüğü tedavi düzeni.",
     "Psikiyatristin ilacı, psikoloğun terapiyi, okulun rehberliği yürüttüğü ergen.", [6]),
]

# ---------------------------------------------------------------------------
# Savunma sözlüğü: ad -> (düzey, tanım)
DUZEYLER = {
    "ilkel": ("İlkel", "İmgeyi ya da gerçekliği belirgin biçimde bozar; ağır stres altında herkes kullanabilir, süreklileştiğinde ilişkileri zorlar."),
    "nevrotik": ("Nevrotik", "Gerçeklik korunur; çatışma yer değiştirme, yalıtma ya da tersine çevirme gibi yollarla yönetilir."),
    "olgun": ("Olgun", "Duygu, çatışma ve gerçeklik birlikte tutulur; uyumu ve ilişkileri destekler."),
}

SAVUNMA_SOZLUK = [
    ("Bölme", "ilkel", "Kendiliği ve ötekileri tümüyle iyi ve tümüyle kötü parçalara ayırma."),
    ("Yansıtmalı özdeşim", "ilkel", "Dayanılmaz bir duyguyu ötekine yükleme ve ötekinin o duyguyu yaşamaya başlaması."),
    ("Yansıtma", "ilkel", "Kendine ait kabul edilemeyen duyguyu başkasına atfetme."),
    ("İnkâr", "ilkel", "Acı veren bir gerçekliği görmezden gelme ya da yok sayma."),
    ("İdealleştirme ve değersizleştirme", "ilkel", "Ötekini kusursuz görmekten bütünüyle değersiz görmeye hızla geçme."),
    ("Dissosiyasyon", "ilkel", "Bilinç, bellek ya da kimlik bütünlüğünü bozarak deneyimden uzaklaşma (bazı sınıflamalarda nevrotik düzeyde yer alır)."),
    ("Eyleme vurma", "ilkel", "Bir duyguyu düşünmek ya da konuşmak yerine dürtüsel bir eylemle boşaltma."),
    ("Bedenselleştirme", "ilkel", "Duygusal sıkıntının bedensel yakınmalara dönüşmesi."),
    ("Gerileme", "ilkel", "Daha önceki bir gelişim düzeyine özgü davranışlara dönme."),
    ("Şizoid fantezi", "ilkel", "Gerçek ilişkilerden içe, hayal dünyasına çekilme."),
    ("Yer değiştirme", "nevrotik", "Bir duyguyu asıl hedefinden daha güvenli bir hedefe kaydırma."),
    ("Karşıt tepki oluşturma", "nevrotik", "Kabul edilemeyen bir duyguyu tersine çevirerek abartılı biçimde yaşama."),
    ("Entelektüelleştirme", "nevrotik", "Duygu yerine soyut bilgi ve düşünceyle meşgul olma."),
    ("Duygulanımın yalıtılması", "nevrotik", "Olayı hatırlayıp anlatırken ona eşlik eden duyguyu ayırma."),
    ("Rasyonalizasyon", "nevrotik", "Kabul edilemeyen bir durumu makul görünen gerekçelerle açıklama."),
    ("Yapıp bozma", "nevrotik", "Saldırgan bir düşünce ya da eylemi sembolik bir eylemle geri almaya çalışma."),
    ("Bastırma", "nevrotik", "Kabul edilemeyen bir istek ya da duyguyu farkındalık dışında tutma."),
    ("Mizah", "olgun", "Acı veren bir durumu gerçekliği inkâr etmeden, gülünç yanını görerek taşıyabilme."),
    ("Yüceltme", "olgun", "Dürtüyü toplumsal olarak değerli ve doyurucu bir etkinliğe yönlendirme."),
    ("Özgecilik", "olgun", "Kendi acısını başkalarına yardım ederek dönüştürme."),
    ("Baskılama", "olgun", "Bir kaygıyı bilinçli olarak sonraya erteleyip zamanı gelince ele alma."),
    ("Öngörü", "olgun", "Gelecekteki zorluğu duygusuyla birlikte önceden düşünüp ona hazırlanma."),
]

# Savunma oyunu vinyetleri: (vinyet, doğru savunma, [3 çeldirici], açıklama)
SAVUNMA_VAKALARI = [
    ("Öğretmeninden azar işiten 12 yaşındaki bir erkek eve gelince küçük kardeşine bağırıyor.",
     "Yer değiştirme", ["Yansıtma", "Karşıt tepki oluşturma", "Eyleme vurma"],
     "Öfke asıl hedefinden (öğretmen) daha güvenli bir hedefe (kardeş) kaymış. Eyleme vurmada vurgu düşünmek yerine dürtüsel bir "
     "eylemle boşaltmadır; burada belirleyici olan hedefin değişmesidir."),
    ("Yeni doğan kardeşini kıskanan 6 yaşındaki bir kız misafirlerin önünde kardeşini abartılı biçimde öpüyor ve ona ne kadar "
     "bayıldığını ilan ediyor.",
     "Karşıt tepki oluşturma", ["Yüceltme", "İdealleştirme ve değersizleştirme", "Gerileme"],
     "Kabul edilemeyen kıskançlık tersine çevrilip abartılı bir sevgi gösterisine dönüşmüş. Abartının kendisi ipucudur."),
    ("Tuvalet eğitimini tamamlamış 4 yaşındaki bir çocuk, kardeşi doğduktan sonra yeniden altını ıslatmaya ve biberon istemeye başlıyor.",
     "Gerileme", ["Dissosiyasyon", "Bedenselleştirme", "Yapıp bozma"],
     "Çocuk, ilgiyi ve bakımı yeniden kazanmak için daha önceki bir gelişim düzeyine dönmüş. Geçici gerileme bu yaşta sık ve çoğu "
     "zaman zararsızdır; ebeveynin sakin kalması geçişi kolaylaştırır."),
    ("Yatışının ilk haftasında 15 yaşındaki bir kız gece hemşiresini “melek”, gündüz hemşiresini “canavar” olarak anlatıyor. Aynı "
     "“melek” bir gün bir kuralı hatırlatınca o da “canavar” oluyor.",
     "Bölme", ["Yansıtma", "Yer değiştirme", "Rasyonalizasyon"],
     "Kişiler ya tümüyle iyi ya tümüyle kötü olarak yaşanıyor; iyi ve kötü yanlar aynı kişide birlikte tutulamıyor. Ekipte "
     "kutuplaşmaya yol açabilir."),
    ("Sınıfta dışlandığını düşünen 14 yaşındaki bir erkek, kendi öfkesinden hiç söz etmeden “herkes bana düşman, hepsi kavga arıyor” diyor.",
     "Yansıtma", ["Yansıtmalı özdeşim", "İnkâr", "Entelektüelleştirme"],
     "Kendine ait öfke başkalarına atfediliyor. Yansıtmalı özdeşimden farkı, karşı tarafın bu duyguyu yaşamaya başlamasının "
     "vinyette yer almamasıdır."),
    ("Her seansta terapistini “işe yaramaz” diye aşağılayan 16 yaşındaki bir ergenle çalışan terapist, birkaç hafta sonra gerçekten "
     "yetersiz ve değersiz hissetmeye başlıyor; ergen ise bir süre sakinleşiyor.",
     "Yansıtmalı özdeşim", ["Yansıtma", "İdealleştirme ve değersizleştirme", "Yer değiştirme"],
     "Ergenin dayanamadığı değersizlik duygusu terapiste yüklenmiş ve terapist onu gerçekten yaşamaya başlamış. Fark edildiğinde "
     "bu karşı aktarım, ergenin iç dünyasına dair değerli bir veridir."),
    ("Tip 1 diyabet tanısı yeni konan 13 yaşındaki bir erkek “bende şeker falan yok, doktorlar abartıyor” diyerek insülin yapmayı reddediyor.",
     "İnkâr", ["Rasyonalizasyon", "Baskılama", "Eyleme vurma"],
     "Acı veren bir gerçeklik yok sayılıyor. Tanının ilk dönemlerinde sık görülür; yüzleştirmek yerine kaygıyı anlamak ve "
     "kontrolün bir kısmını ergene bırakmak uyumu artırır."),
    ("Fiziksel istismar öyküsü olan 11 yaşındaki bir kız, babası sesini yükselttiğinde gözlerinin boşaldığını, kendini “uzaktan "
     "izliyormuş gibi” hissettiğini anlatıyor.",
     "Dissosiyasyon", ["İnkâr", "Duygulanımın yalıtılması", "Şizoid fantezi"],
     "Dayanılmaz bir anda deneyimden uzaklaşma ve kendini dışarıdan izleme hissi dissosiyasyonu düşündürür. Duygulanımın "
     "yalıtılmasında bilinç ve bellek bütünlüğü korunur."),
    ("Babasının yeni evliliğini öğrenen 15 yaşındaki bir kız, konuşmak yerine o gece evden çıkıp sabaha kadar dönmüyor.",
     "Eyleme vurma", ["Yer değiştirme", "Gerileme", "İnkâr"],
     "Dayanılmaz duygu düşünülmek ya da konuşulmak yerine dürtüsel bir eylemle boşaltılmış. Hedef, eylem ile dürtü arasına "
     "düşünceyi yerleştirmektir."),
    ("Ebeveynleri boşanma sürecinde olan 9 yaşındaki bir erkek, babasının evine gideceği her pazar akşamından önce karın ağrısı "
     "yaşıyor; tetkikleri normal.",
     "Bedenselleştirme", ["Gerileme", "Yapıp bozma", "Rasyonalizasyon"],
     "Sözle ifade edilemeyen sıkıntı bedenden konuşuyor. Organik nedenler dışlandıktan sonra ağrının zamanlaması ve anlamı aileyle "
     "birlikte konuşulmalıdır."),
    ("Annesi kanser tanısı alan 17 yaşındaki bir erkek hastalığın moleküler mekanizmaları ve sağkalım istatistikleri hakkında "
     "ayrıntılı bilgi topluyor; nasıl hissettiği sorulduğunda konuyu yeniden verilere getiriyor.",
     "Entelektüelleştirme", ["Yüceltme", "Duygulanımın yalıtılması", "Öngörü"],
     "Duygu yerine soyut bilgiyle meşgul olunuyor. Öngörüden farkı, duygunun da düşünceye katılmamasıdır."),
    ("Bir trafik kazasını bütün ayrıntılarıyla hatırlayan 16 yaşındaki bir erkek, “Ne hissettin?” sorusuna “Bir şey hissetmedim, "
     "sadece neler olduğunu biliyorum” diyor.",
     "Duygulanımın yalıtılması", ["Dissosiyasyon", "İnkâr", "Bastırma"],
     "Olay hatırlanıyor ve kabul ediliyor, ama ona eşlik eden duygu ayrılmış. İnkârda olay yok sayılır; dissosiyasyonda bilinç ya "
     "da bellek bütünlüğü bozulur."),
    ("Takıma seçilmeyen 14 yaşındaki bir erkek “Zaten o takımda oynamak istemiyordum, antrenmanlar dersime engel olurdu” diyor.",
     "Rasyonalizasyon", ["İnkâr", "Yüceltme", "Karşıt tepki oluşturma"],
     "Hayal kırıklığı makul görünen gerekçelerle açıklanıyor. Gerçeklik inkâr edilmiyor; acı veren anlamı yeniden çerçeveleniyor."),
    ("Kardeşine kızıp “keşke hiç doğmasaydın” diyen 8 yaşındaki bir kız, o gece kardeşi için üç kez dua ediyor ve en sevdiği "
     "oyuncağını onun yatağına bırakıyor.",
     "Yapıp bozma", ["Karşıt tepki oluşturma", "Özgecilik", "Gerileme"],
     "Saldırgan söz sembolik eylemlerle geri alınmaya çalışılıyor. Karşıt tepki oluşturma süreğen bir tutumdur; yapıp bozma ise "
     "belirli bir eylemi iptal etmeye yönelik tek tek eylemlerle görünür."),
    ("Babasına hiç öfke duymadığını söyleyen 12 yaşındaki bir erkek, babasının başına bir kaza geldiğini gördüğü bir rüyadan "
     "korkuyla uyanıyor.",
     "Bastırma", ["İnkâr", "Yansıtma", "Dissosiyasyon"],
     "Kabul edilemeyen öfke farkındalık dışında tutuluyor ve rüyada dolaylı olarak beliriyor. Bastırmada dış gerçeklik değil iç "
     "istek ya da duygu dışarıda tutulur."),
    ("Kemoterapi nedeniyle saçları dökülen 15 yaşındaki bir kız arkadaşlarına “Artık saç kurutmaya harcadığım zaman derse kalıyor” "
     "diyerek gülüyor; aynı zamanda annesiyle korkularını da konuşabiliyor.",
     "Mizah", ["İnkâr", "Rasyonalizasyon", "Karşıt tepki oluşturma"],
     "Gerçeklik ve duygular inkâr edilmeden taşınabiliyor; korkular başka ilişkilerde de konuşulabiliyor. Bu mizahı olgun kılan budur."),
    ("Öfke patlamaları nedeniyle başvuran 14 yaşındaki bir erkek boks antrenmanına başladıktan sonra öfkesini ringde disiplinli "
     "biçimde kullanmaya ve antrenörünün kurallarına uymaya başlıyor.",
     "Yüceltme", ["Yer değiştirme", "Eyleme vurma", "Rasyonalizasyon"],
     "Saldırgan dürtü kurallı, toplumsal olarak değerli ve doyurucu bir etkinliğe yönlendirilmiş. Yer değiştirmede hedef değişir "
     "ama dürtü dönüşmez."),
    ("Kardeşini kanserden kaybeden 17 yaşındaki bir kız hastanenin çocuk onkoloji servisinde gönüllü oyun etkinlikleri düzenliyor "
     "ve yasını da konuşabiliyor.",
     "Özgecilik", ["Karşıt tepki oluşturma", "İnkâr", "İdealleştirme ve değersizleştirme"],
     "Kendi acısı başkalarına yardım ederek dönüştürülüyor; yas inkâr edilmiyor. Olgun bir savunmadır."),
    ("Sınavdan bir gün önce ebeveynlerinin kavgasını duyan 16 yaşındaki bir erkek “Bunu sınavdan sonra düşüneceğim” diyor, ders "
     "çalışıyor ve sınav bitince konuyu annesiyle konuşuyor.",
     "Baskılama", ["Bastırma", "İnkâr", "Entelektüelleştirme"],
     "Kaygı bilinçli olarak erteleniyor ve zamanı gelince ele alınıyor. Bastırmadan farkı bilinçli olmasıdır."),
    ("Babasının yurt dışına çalışmaya gideceğini öğrenen 13 yaşındaki bir kız üzüleceğini kabul ediyor, görüntülü konuşma saatlerini "
     "planlıyor ve ilk haftalarda zorlanacağını önceden konuşuyor.",
     "Öngörü", ["Entelektüelleştirme", "Rasyonalizasyon", "İnkâr"],
     "Gelecekteki zorluk duygusuyla birlikte önceden düşünülüp hazırlanılıyor. Entelektüelleştirmeden farkı duygunun da hesaba "
     "katılmasıdır."),
    ("Yeni başladığı terapistini ilk hafta “hayatımda tanıdığım en iyi doktor” diye öven 16 yaşındaki bir ergen, randevunun bir kez "
     "ertelenmesinin ardından “aslında hiçbir şey bilmiyor” diyor.",
     "İdealleştirme ve değersizleştirme", ["Rasyonalizasyon", "Yansıtma", "Yer değiştirme"],
     "Öteki kusursuzdan değersize hızla geçiyor; bölmeyle yakından ilişkilidir. İdealleştirmenin yoğunluğu, gelecek "
     "değersizleştirmenin habercisi olabilir."),
    ("Okulda hiç arkadaşı olmayan 15 yaşındaki bir erkek teneffüslerde kendi kurduğu hayalî bir krallığın haritalarını çiziyor; gerçek "
     "ilişkilere ilgisizliğini “gerek yok, orada her şey var” diye açıklıyor.",
     "Şizoid fantezi", ["Yüceltme", "İnkâr", "Gerileme"],
     "Gerçek ilişkilerden iç dünyaya çekiliniyor. Ergende böyle bir fantezi dünyası her zaman yaratıcılık ya da prodrom değildir; "
     "asıl soru dünyayla temasın kesilip kesilmediğidir."),
]

# ---------------------------------------------------------------------------
# Formülasyon şablonu: (anahtar, başlık, ipucu, satır sayısı)
FORM_ALANLAR = [
    ("basvuru", "Başvuru ve şikâyet", "Kim getirdi, kim şikâyetçi, çocuk ya da ergen ne diyor?", 3),
    ("neden_simdi", "Neden şimdi?", "Tetikleyici olay ve bunun çocuk ve aile için anlamı.", 3),
    ("yatkinlik", "Yatkınlık", "Mizaç, biyolojik etkenler, aile öyküsü.", 2),
    ("gelisim", "Gelişimsel öykü ve bağlanma", "Erken ilişkiler, ayrılıklar, kayıplar; anlatıda hiç geçmeyen kişi ya da dönem.", 3),
    ("aile", "Aile sistemi", "Belirtinin ailedeki işlevi, ebeveynlerin işbölümü; belirlenmiş hasta olabilir mi?", 3),
    ("aktarim", "Aktarım ve karşı aktarım", "Çocuk sizi nasıl görüyor? Sizde ne uyanıyor? Ekipte ne oluyor?", 3),
    ("guclu", "Güçlü yanlar ve koruyucu etkenler", "Yetenekler, ilişkiler, okul, toplumsal destek.", 2),
    ("ozet", "Formülasyon özeti (3–5 cümle)",
     "Örnek kurgu: “… yatkınlığı olan bu çocuk, … deneyimleri nedeniyle … beklentisini geliştirmiş görünüyor. … olayı bu beklentiyi "
     "canlandırdığı için … belirtileri ortaya çıkmış olabilir.”", 5),
    ("guclukler", "Öngörülen güçlükler", "Olası direnç, aktarım örüntüsü, ailenin tedaviyi farkında olmadan zorlaştırabileceği noktalar.", 3),
]
FORM_ORUNTU = [("oruntu_kendilik", "Kendilik", "Ben … olanım"), ("oruntu_oteki", "Öteki", "Öteki … olandır"),
               ("oruntu_duygu", "Aradaki duygu", "Kaygı, öfke, utanç, suçluluk…")]
FORM_TEDAVI = ["Bireysel psikoterapi", "Aile çalışması", "Ebeveyn danışmanlığı", "Grup", "İlaç", "Okul ile iş birliği"]

FORM_ORNEK = {
    "basvuru": "Annesi, son üç ayda okula gitmeyi reddetmesi ve sabahları başlayan karın ağrıları nedeniyle getirdi. E. (14) “Okulda herkes bana bakıyor” diyor.",
    "neden_simdi": "Babası dört ay önce iş nedeniyle başka bir şehre taşındı; annenin çökkünlüğü bu dönemde arttı.",
    "yatkinlik": "Küçüklükten beri yeni ortamlarda çekingen; annede anksiyete bozukluğu öyküsü.",
    "gelisim": "Okula başlarken uzun süren ayrılık güçlüğü. Annenin anlatısında babanın rolü neredeyse hiç geçmiyor.",
    "aile": "E. evde kaldığı günlerde annenin daha az yalnız ve daha sakin olduğu görülüyor. Baba “disiplinci”, anne “koruyucu” olarak kutuplaşmış.",
    "oruntu_kendilik": "Ben, ayrılırsam bir şey olacak olanım.",
    "oruntu_oteki": "Öteki, yalnız kalınca dağılan ve bana ihtiyaç duyan.",
    "oruntu_duygu": "Kaygı ve suçluluk.",
    "savunmalar": ["Bedenselleştirme", "Gerileme", "Rasyonalizasyon"],
    "aktarim": "Görüşmede terapiste aşırı uyumlu. Terapistte “onu korumalıyım” hissi ve aileye karşı bir kızgınlık uyanıyor.",
    "guclu": "Resim yeteneği, yakın bir arkadaşı, okul rehber öğretmeniyle iyi ilişki.",
    "ozet": "Çekingen bir mizaca ve kaygılı bir anneye sahip olan E., ayrılığın tehlikeli olduğu beklentisiyle büyümüş görünüyor. "
            "Babanın taşınması ve annenin çökkünlüğü, E.’nin evden ayrılmasını hem kendisi hem annesi için tehdit edici hâle "
            "getirmiş olabilir. Okul reddi ve karın ağrıları, bu kaygıyı dile getirmeden yönetmenin ve anneyi yalnız bırakmamanın "
            "bir yolu olarak işlev görüyor olabilir.",
    "surekli": "3",
    "tedavi": ["Bireysel psikoterapi", "Ebeveyn danışmanlığı", "Aile çalışması", "Okul ile iş birliği"],
    "guclukler": "Okula dönüş ilerledikçe annenin kaygısı artabilir ve süreci farkında olmadan zorlaştırabilir. E., terapiste aşırı "
                 "uyum göstererek “iyi gidiyor” görüntüsü verebilir. Annenin kendi değerlendirmesi ve desteklenmesi gerekebilir.",
}

# ---------------------------------------------------------------------------
# Ergenlik notları
ERGENLIK_GIRIS = ("Kitapta ergenliğe ayrılmış bir bölüm yok; ergenlik pek çok bölümde kısa geçişlerle anılıyor. Aşağıda bu geçişleri "
                  "beş tema altında topladık ve kitabın bıraktığı boşlukları not ettik.")
ERGENLIK = [
    ("Gelişim ergenlikte bitmez",
     ["Savunmalar her gelişim evresinde yeniden düzenlenir; uzun süreli izlem çalışmaları erişkinlik boyunca olgun savunmalara "
      "doğru bir kayma gösterir ([@vaillant1977]).",
      "Genetik etkiler de yaşla değişir: korkular üzerine yapılan boylamsal ikiz çalışmasında erken ergenlik, geç ergenlik ve genç "
      "erişkinlikte yeni genetik etkenler devreye girdi; ailesel çevrenin etkisi ise yaşla azaldı ([@kendler2008]).",
      "Bu nedenle 9 yaşında “geçti” denen bir kaygı, 14 yaşında farklı bir biyolojiyle geri dönebilir."],
     "Ergendeki ilkel savunma bir durak olabilir, varış noktası değil."),
    ("Ergen ailenin belirti taşıyıcısı olabilir",
     ["Kitabın ergenlikle ilgili en sık tekrarladığı fikir budur: ergenin tablosu ebeveynlerin çözülmemiş çatışmalarını, aile içinde "
      "inkâr edilen dürtüleri ya da ebeveynin kendi olumsuz kendilik temsillerini taşıyor olabilir.",
      "Bu düzen ailedeki dengeyi korur; ergen düzeldikçe denge sarsılabilir (bkz. Bölüm 5)."],
     "Ergeni tedavi etmeye başladığınızda bu yükü ona kimin verdiğini de sormuş olursunuz."),
    ("İlk görüşme: sessiz ergen, konuşan ebeveynler",
     ["Ergen çoğu zaman tedaviye ikna olmadan gelir ve susar; ebeveynler uzun uzun anlatır. Yalnızca getirilen “hasta”yı görmek, "
      "ailedeki bölmeye farkında olmadan ortak olmak anlamına gelebilir.",
      "Bireysel mi, aile mi sorusunda belirleyici olan ergenin aileden ne ölçüde farklılaştığıdır: ayrı yaşayan ve görece olgun "
      "savunmaları olan geç ergen için bireysel terapi; evde yaşayan ve aileyle yoğun, çatışmalı biçimde iç içe olan ergen için aile "
      "çalışması ya da birleşik bir yaklaşım daha uygundur."],
     "Ergen ne kadar ailesinin içindeyse, tedavi de o kadar ailenin içinde olmalıdır."),
    ("Bozukluklara göre notlar",
     ["Depresyon: Erken ebeveyn kaybında yalnızca kaybın varlığı değil, zamanlaması ve biçimi de risk düzeyini değiştirir (Bölüm 8).",
      "Sosyal kaygı: Toplum temelli bir izlem çalışmasında ebeveyn psikopatolojisi ile algılanan aşırı koruma ve ret, ergenlerde "
      "sosyal fobi gelişimiyle ilişkiliydi ([@lieb2000]).",
      "Anoreksiya: Ebeveynlerini memnun ederek büyümüş “iyi” çocuğun ergenlikte inatçılaşması bir bozulmadan çok ilk özerklik "
      "girişimi olabilir; aile temelli tedavi önemli bir seçenektir ([@lock2010]).",
      "Şizotipal özellikler (kitapta Bölüm 14, bu rehberde henüz yok): Ergende tuhaf fanteziler ve uğraşlar, büyüsel düşüncenin "
      "yaşa özgü görünümü olabilir.",
      "Antisosyal davranış: Yüksek otonom uyarılmışlık antisosyal ergenlerde erişkin suçuna karşı koruyucu bulunmuştur "
      "([@raine1995]); personelin psikopatik özellikleri “ergen isyanı” diye geçiştirmesi ise bir karşı aktarım riskidir (Bölüm 17).",
      "Narsisizm: Narsisistik doyumlar en çok ergenlik ve genç erişkinlikte yaşanır; narsisistik özellikler yaşla ortalama olarak "
      "azalır ([@wetzel2020])."],
     "Ergenlikteki inat bazen bozulma değil, ilk özerklik girişimidir."),
    ("Kitabın bıraktığı boşluklar",
     ["Ergenlikte kişilik bozukluğu tanısı tartışmasına girmez; bu konuda güncel derlemeler yol göstericidir ([@sharp2015]).",
      "Ergen psikoterapisinin tekniğine (gizlilik, ebeveynle bilgi paylaşımı, özerklik ve rıza) ayrı bir yer vermez.",
      "Erken başlangıçlı psikoz ve ergen depresyonunda ilaç kanıtını tartışmaz.",
      "Ergen beyin gelişimine ve dürtüselliğin nörobiyolojisine değinmez.",
      "Bu konularda gelişimsel psikopatoloji ders kitapları, IACAPAP’ın çevrim içi ders kitabı ve güncel klinik kılavuzlar daha "
      "doğrudan kaynaklardır."],
     "“Ergenlik bu, geçer” bazen gelişimsel bilgelik, bazen üzerine örtülen bir battaniyedir."),
]
ERGENLIK_AKILDA = [
    "Ergen ne kadar ailesinin içindeyse, tedavi de o kadar ailenin içinde olmalıdır.",
    "Aşırı koruma ile ret aynı çocukta birleştiğinde çocuk dünyanın tehlikeli, kendisinin yetersiz olduğunu öğrenebilir.",
    "Ergende tuhaf bir fantezi dünyası her zaman yaratıcılık da değildir, prodrom da; asıl soru dünyayla temasın kesilip kesilmediğidir.",
    "Ergenlik narsisizmin altın çağıdır; faturası daha sonra gelir.",
]

# ---------------------------------------------------------------------------
# Odada kaç kişi var?
ODA_GIRIS = ("Bölüm 3’ün açılışındaki fikir şudur: iki kişi konuştuğunda odada altı kişi vardır. Her biri kendi gözündeki "
             "hâliyle, karşısındakinin gözündeki hâliyle ve gerçekte olduğu hâliyle oradadır. Kitap bu fikri William James’e "
             "atfeder; benzer bir “üç John, üç Thomas” oyunu Oliver Wendell Holmes’un 1858 tarihli bir kitabında da geçer "
             "([@holmes1858]). Aile görüşmesinde sayı hızla büyür: n kişilik bir odada n × (n + 1) imge vardır.")
ODA_HUCRELER = {
    # (kişi, bakan) -> klinik ipucu; bakan == kişi: kendi gözünde; bakan == "gercek": gerçekte
    ("hekim", "cocuk"): "Çocuğun gözündeki hekim çoğu zaman tek bir soruya indirgenir: “Bu doktor kimden yana?”",
    ("hekim", "ergen"): "Ergen için “psikiyatrist” sözcüğü damga olabilir. İlk hamle bu beklentiyi adlandırmaktır: “Benim hakkımda sana ne söylediler?”",
    ("hekim", "anne"): "Anne için “beni anlayan” olabilirsiniz; bu, babanın gözünde “karıma hak veren” olmanızı da beraberinde getirebilir. Bölme burada başlar.",
    ("hekim", "baba"): "Baba sizi annenin müttefiki olarak görebilir; babayı görüşmeye ayrıca davet etmek bu imgeyi değiştirebilir.",
    ("hekim", "hekim"): "Kendinizi yardımcı ve nesnel bir uzman olarak görürsünüz; bu imge, odadaki en az sorgulanan imgedir.",
    ("hekim", "gercek"): "En sık unutulan hücre: bugün yorgun muydunuz, saate baktınız mı, sesiniz sert miydi? Ergen “sen de babam gibisin” dediğinde iki soru gerekir: hangi geçmiş tekrar ediyor ve ben bugün gerçekten ne yaptım?",
    ("cocuk", "hekim"): "Ebeveynlerin anlattığı çocuk ile odada gördüğünüz çocuk arasındaki fark en değerli veridir. Duygunuz (“beni çileden çıkarıyor”) çocuğun çevresinde ne uyandırdığını da gösterir.",
    ("ergen", "hekim"): "Sizdeki ilk izlenim (“manipülatif”, “zavallı”, “ilginç vaka”) hem bilgi hem tuzaktır; fark edilmezse ses tonunuza sızar.",
    ("cocuk", "anne"): "Annenin baktığı çocuk kısmen kendi çocukluğudur; gördüğü ile odadaki çocuk her zaman aynı değildir.",
    ("cocuk", "gercek"): "Gerçek çocuk, diğer imgeler ayıklandıkça görünür; formülasyon bu ayıklamanın ürünüdür.",
    ("ergen", "gercek"): "Gerçek ergen, diğer imgeler ayıklandıkça görünür; formülasyon bu ayıklamanın ürünüdür.",
    ("anne", "baba"): "Babanın gözündeki anne ve annenin gözündeki baba ikili görüşmede olmayan yeni bir eksendir; “disiplinci baba, koruyucu anne” kutuplaşması bu hücrelerde yaşar.",
    ("baba", "anne"): "Annenin gözündeki baba: evde olmayan, uzak, sert ya da yetersiz. Babanın kendi gözündeki hâliyle karşılaştırın.",
}
ODA_HAYALETLER = ["Annenin annesi ve babası", "Babanın annesi ve babası", "Evde olmayan ya da kaybedilen kardeş",
                  "Ayrılmış ya da ölmüş ebeveyn", "Sizin kendi aileniz"]
ODA_HAYALET_NOT = ("Odaya hiç girmeyenler de oradadır. Fraiberg ve arkadaşlarının “çocuk odasındaki hayaletler” dediği, ebeveynin "
                   "kendi çocukluğundan taşıdığı figürler bebeğe bakışını biçimlendirir ([@fraiberg1975]). Bunlar eklendiğinde sayı "
                   "belirsizleşir; ama sandalyesi olmayan bu kişileri görmek, aile görüşmesinin yarısıdır.")
