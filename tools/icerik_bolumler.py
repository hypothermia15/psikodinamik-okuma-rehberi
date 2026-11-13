# -*- coding: utf-8 -*-
"""Psikodinamik Psikiyatri Okuma Rehberi: bölüm içerikleri.

Bütün metinler özgündür. Kitaptan alıntı, kitabın vaka örnekleri ya da bölümlerin
bölüm bölüm yeniden anlatımı yoktur. Ana fikirler kendi sözcüklerimizle, çocuk ve ergen
ruh sağlığı ve hastalıkları (ÇRS) pratiğine çevrilerek yazıldı. Vaka soruları kurgusaldır.

Atıf sözdizimi: [@anahtar] (anahtarlar tools/kaynaklar.json içinde).
"""

KISIMLAR = {
    1: "Kısım I · Temel ilkeler ve tedavi yaklaşımları",
    2: "Kısım II · DSM-5 bozukluklarına dinamik yaklaşımlar",
}

# Rehberde henüz işlenmeyen bölümler
EKSIK = [
    (11, "Parafililer ve cinsel işlev bozuklukları"),
    (14, "A kümesi kişilik bozuklukları: paranoid, şizoid, şizotipal"),
    (18, "Histerik ve histriyonik kişilik bozuklukları"),
    (19, "C kümesi kişilik bozuklukları: obsesif-kompulsif, çekingen, bağımlı"),
]


def S(soru, secenekler, dogru, aciklama):
    return dict(soru=soru, secenekler=secenekler, dogru=dogru, aciklama=aciklama)


BOLUMLER = [
    # ------------------------------------------------------------------ 1
    dict(
        no=1, kisim=1, kisa="Temel ilkeler",
        baslik="Dinamik psikiyatrinin temel ilkeleri",
        slogan="Belirti bir anlam taşır; klinisyenin duygusu da bir veridir.",
        kitapta=("Bölüm, psikodinamik bakışı ayrı bir ekol olarak değil, her klinik karşılaşmaya eşlik edebilecek bir "
                 "düşünme biçimi olarak tanıtır: zihin ile beyin ilişkisi, bilinçdışının işleyişi, öznel deneyimin değeri, "
                 "aktarım, karşı aktarım ve direnç."),
        okurken=[
            "Yazar “anlam” ile “neden” arasındaki farkı nasıl kuruyor? Bir belirtinin hem biyolojik nedeni hem kişisel anlamı olabilir mi?",
            "Karşı aktarım hangi koşulda bir engel olmaktan çıkıp bir ölçüm aracına dönüşüyor?",
            "Bölüm, derinleştirmekten kaçınılması gereken durumlar için hangi ipuçlarını veriyor?",
        ],
        fikirler=[
            ("Hem beyin hem zihin", "Biyolojik ve psikolojik açıklamalar birbirinin rakibi değil, aynı olgunun farklı düzeyleridir. "
             "Bir ilacın etkisi ne kadar gerçekse, ilacın hasta için taşıdığı anlam da klinik sonucu o kadar etkiler."),
            ("Bilinçdışı gündelik bir işleyiştir", "Davranışın önemli bir bölümü farkındalık dışında, alışkanlık ve beklenti "
             "kalıplarıyla yönlenir. Bu kalıplar en açık biçimde kişinin ilişkilerinde tekrarladığı örüntülerde görünür."),
            ("Gen bir yatkınlıktır, kader değil", "Kalıtsal yatkınlıklar çevreyle etkileşerek ifade bulur; aynı yatkınlık farklı "
             "yaşantılarda farklı sonuçlara gider. Psikodinamik bakış bu etkileşimin öznel tarafıyla ilgilenir."),
            ("Aktarım her yerdedir", "Hasta geçmiş ilişkilerinden getirdiği beklentileri klinisyene, ekibe ve kuruma taşır. Bu yalnızca "
             "terapi odasında değil, ilaç vizitinde ve acil serviste de olur."),
            ("Karşı aktarım bir veridir", "Klinisyenin hastaya karşı hissettikleri hem kendi geçmişinden hem hastanın ilişki örüntüsünden "
             "beslenir. Fark edildiğinde, hastanın çevresinde uyandırdığı duyguyu anlamanın en hızlı yoludur."),
            ("Yapmadığınız şey de tedavi eder", "Hastanın sizi çekmeye çalıştığı tanıdık role girmemek (cezalandırmamak, kurtarmaya "
             "kalkmamak, terk etmemek) tek başına düzeltici bir deneyim olabilir."),
        ],
        crs=[
            "Reçetenin çocuk ve aile için anlamını sorun: “Bu ilaç sana ne söylüyor?” Kimi çocuk için ilaç bir damga, kimi aile için “sonunda biri bizi ciddiye aldı” demektir.",
            "Ergenin “travmam yüzünden böyleyim” açıklaması hem bir anlamlandırma hem sorumluluktan bir kaçış olabilir. İkisini birlikte tutmak, ne suçlamak ne de olduğu gibi onaylamak demektir.",
            "“Bu çocuk beni çileden çıkarıyor” duygusu, çocuğun okulda ve evde de aynı duyguyu uyandırdığına dair bir ipucudur. Duyguyu eyleme dökmeden önce adlandırın; gerekiyorsa süpervizyona taşıyın.",
            "Aynı çocuğun sizinle, hemşireyle ve öğretmeniyle kurduğu ilişkiler çok farklıysa, bu bir tutarsızlık değil, iç dünyasının farklı parçalarının farklı kişilere dağıtılmasıdır.",
            "Akut yas, yerinden edilme ya da yeni açığa çıkmış istismar sırasında derinleştirmeyin; önce destek ve yapı, keşif sonra.",
            "Bir çocuğu terapiye alma ya da terapiyi sürdürme kararınızı, onu sevip sevmemenizin değil klinik ölçütlerin belirlediğini kendinize sorun.",
        ],
        tartisma=[
            ("Aday gen örnekleri eskidi",
             "Kitap gen–çevre etkileşimini anlatırken dönemin aday gen bulgularına dayanır. Serotonin taşıyıcı geni ile yaşam "
             "stresinin depresyon üzerindeki etkileşimi ilk bildirildiğinde çok etkili olmuştu ([@caspi2003]); ancak 38 binden "
             "fazla kişiyi kapsayan ortak analiz bu etkileşimi doğrulamadı ([@culverhouse2018]) ve büyük örneklemlerde aday gen "
             "hipotezlerine destek bulunamadı ([@border2019]). “Gen bir yatkınlıktır” ilkesi ayakta; tek gen örnekleri ise artık "
             "kanıtlanmış bilgi gibi öğretilmemeli."),
            ("Karşı aktarımın sınırı",
             "Klinisyenin her duygusunu hastanın iç dünyasının yansıması saymak, kendi yorgunluğunu, önyargısını ya da kişisel "
             "geçmişini hastaya yüklemek anlamına gelebilir. Karşı aktarımı veri olarak kullanmak, onu süpervizyonda ve ekip içinde "
             "sınamayı gerektirir."),
            ("Bilinçdışının iki anlamı",
             "Bilişsel bilimdeki örtük süreçler ile psikanalitik bilinçdışı örtüşür ama aynı şey değildir. Birincisi deneysel olarak "
             "iyi gösterilmiştir; çatışma ve savunma içeren ikinci anlam ise daha çok klinik çıkarıma dayanır."),
        ],
        sorular=[
            S("On iki yaşında, dikkat eksikliği ve hiperaktivite bozukluğu tanısıyla izlenen bir erkek, metilfenidat başlandıktan iki "
              "hafta sonra ilacı almayı reddediyor. Annesi “yan etkisi yok, ama içmiyor” diyor. Çocuk yalnız görüşmede “Sınıfta bana "
              "ilaçlı diyorlar” diyor. Psikodinamik açıdan en uygun ilk adım hangisidir?",
              ["Dozu artırıp etkinin belirginleşmesini beklemek",
               "İlacın onun için taşıdığı anlamı ve akranlarının tepkisini konuşmak; zamanlama ve gizlilik için birlikte çözüm aramak",
               "Ebeveynlere ilacı yemeğe karıştırarak vermelerini önermek",
               "Reddi karşıt olma belirtisi sayıp ödül sistemi kurmak"],
              1, "Uyumsuzluk çoğu zaman ilacın kendisine değil, anlamına verilen bir yanıttır; bu çocukta ilaç bir damgaya dönüşmüş. "
                 "Anlamı konuşmak ve kontrolün bir kısmını çocuğa bırakmak (ör. okulda doz gerektirmeyen bir düzen) uyumu en çok "
                 "artırabilecek adımdır. Gizlice ilaç vermek etik değildir ve güveni yıkar."),
            S("Ergen serviste çalışan bir asistan, 15 yaşındaki bir hastaya karşı her vizitte belirgin bir sabırsızlık hissettiğini, "
              "hastanın “kimse beni dinlemiyor” cümlesinin onu özellikle rahatsız ettiğini fark ediyor. En uygun yaklaşım hangisidir?",
              ["Duyguyu yok sayıp profesyonelliğini korumak",
               "Hastayı başka bir hekime devretmek",
               "Duyguyu süpervizyonda ele alıp kendi payını ve hastanın çevresinde uyandırdığı örüntüyü ayırt etmeye çalışmak",
               "Öfkesini hastaya açıkça söyleyip tepkisini gözlemek"],
              2, "Karşı aktarım ne bastırılmalı ne de doğrudan eyleme dökülmelidir. Süpervizyonda incelenen duygu, hem klinisyenin "
                 "kendi katkısını hem de hastanın başkalarında uyandırdığı tepkiyi anlamaya yardım eder. Devretmek, hastanın "
                 "“kimse dinlemiyor” beklentisini doğrulayabilir."),
            S("Deprem sonrası geçici barınma alanında annesini kaybeden 10 yaşındaki bir kız, ilk görüşmede oyun oynamak istiyor ve "
              "kayıptan hiç söz etmiyor. Hangisi “derinleştirmeme” ilkesine en uygundur?",
              ["Kaybı konuşmaya teşvik etmek için yas üzerine yorum yapmak",
               "Güvenli, öngörülebilir bir ilişki ve günlük yapı kurmaya odaklanıp keşfi zamana bırakmak",
               "Oyunu kayıpla ilgili sembolik içerik açısından yorumlamak",
               "Görüşmeyi sonlandırıp yalnızca ailenin kalan üyeleriyle görüşmek"],
              1, "Akut krizde öncelik güvenlik, destek ve yapıdır. Oyun bu evrede bir savunmadan çok bir düzenleme aracıdır; erken "
                 "yorum çocuğu korumasız bırakabilir. Keşfedici çalışma, çocuk dengelendikçe ve ilişki kurulduktan sonra gündeme gelir."),
        ],
        akilda="Önce anlamı sorun, sonra yorumlayın; bazen en iyi müdahale tanıdık role girmemektir.",
    ),
    # ------------------------------------------------------------------ 2
    dict(
        no=2, kisim=1, kisa="Kuramsal temel",
        baslik="Dinamik psikiyatrinin kuramsal temeli",
        slogan="Çocuk tek bir kişiyi değil, bir ilişkiyi içselleştirir.",
        kitapta=("Bölüm, klinikte birlikte kullanılan kuramları sırayla tanıtır: ego psikolojisi, nesne ilişkileri, kendilik "
                 "psikolojisi, bağlanma kuramı ve mentalizasyon. Gelişimin erişkinlikte de sürdüğünü vurgular; savunmaları "
                 "düzeylerine göre sınıflandıran bir tablo da bu bölümdedir."),
        okurken=[
            "Her kuram “hastayı ne hareket ettirir?” sorusuna nasıl yanıt veriyor: çatışma mı, eksik mi, ilişki mi?",
            "Savunmaları düzeylere ayırmak klinikte ne işe yarıyor? Bir savunma “ilkel” olduğu için kötü müdür?",
            "Yazar kuramları birbirinin rakibi olarak mı, farklı hastalara uyan mercekler olarak mı sunuyor?",
        ],
        fikirler=[
            ("Ego psikolojisi: belirti bir uzlaşmadır", "Belirti; bir istek, bir yasak ve gerçekliğin talepleri arasındaki pazarlığın "
             "ürünü olarak okunur. Savunmalar bu pazarlığın araçlarıdır ve kişinin savunma profili tedaviye nasıl yanıt vereceğini öngörür."),
            ("Nesne ilişkileri: iç dünyada ilişkiler yaşar", "Çocuk bakım vereni tek başına değil, onunla yaşadığı ilişkiyi (bir kendilik, "
             "bir öteki ve aralarındaki duygu) içselleştirir. Sonraki ilişkiler bu iç sahnelerin yeniden oynanmasıdır. Bölme ve "
             "yansıtmalı özdeşim bu düzeyin savunmalarıdır."),
            ("Kendilik psikolojisi: bütünlük ve utanç", "Kendilik duygusu, ayna tutan ve idealleştirilebilen ötekilerin desteğiyle "
             "sağlamlaşır. Bu destek eksik kaldığında kişi utanca, parçalanma kaygısına ve öfke patlamalarına açık hâle gelir."),
            ("Bağlanma ve mentalizasyon", "Bakım verenin çocuğun zihnini merak etmesi, çocuğun kendi ve başkalarının zihnini anlama "
             "kapasitesini büyütür. Bu kapasite stres altında çökebilir ve birçok ağır psikopatolojinin ortak paydasıdır."),
            ("Gelişim ergenlikte bitmez", "Savunmalar ve kendilik örgütlenmesi yaşam boyu yeniden düzenlenir. Uzun süreli izlem "
             "çalışmaları erişkinlikte olgun savunmalara doğru bir kayma gösterir ([@vaillant1977]); ergendeki ilkel savunma bir "
             "durak olabilir, varış noktası değil."),
        ],
        crs=[
            "Disleksi, dil bozukluğu ya da zihinsel yetersizlik “direnç” değildir; çatışmadan bağımsız ego işlevlerindeki bir sınırlılıktır. Okulda “istemiyor” denen çocukta önce kapasiteyi değerlendirin.",
            "Çocuğun içselleştirdiği anne, odadaki anneyle birebir aynı değildir. Görüşmedeki anne ile çocuğun anlattığı anne arasındaki fark, iç dünyaya açılan bir kapıdır.",
            "Ekibin bir çocuk hakkında “iyiler” ve “kötüler” diye ayrışması, çocuğun iç dünyasındaki bölmenin ekip düzeyinde sahnelenmesi olabilir.",
            "“Hiç sorun çıkarmayan çocuk” her zaman iyi değildir; ebeveynin ihtiyaçlarına uyum sağlamak için kendi isteğini geri çekmiş olabilir.",
            "Ergen ebeveynden kopmaz; kendilik desteğini ebeveynden akranlara, idollere ve ideallere taşır. Bu geçişin kesintiye uğraması ergen krizlerinin önemli bir kaynağıdır.",
            "Kendine zarar verme kimi ergende dağılan kendilik duygusunu toparlama girişimidir. İlk soru “neden yapıyorsun?” değil, “yapmadan hemen önce ne oluyordu?” olmalıdır.",
        ],
        tartisma=[
            ("Bağlanma sınıflaması bireysel tanı aracı değildir",
             "Dezorganize bağlanma orta sınıf örneklemlerde bebeklerin yaklaşık %15’inde görülür ve tek başına istismar göstergesi "
             "değildir ([@vanijzendoorn1999]). Bağlanma ölçümlerini çocuk koruma ya da velayet kararlarında bireysel kanıt gibi "
             "kullanmak bu nedenle yanlıştır ([@granqvist2017])."),
            ("Kuramların kanıt düzeyi eşit değil",
             "Bağlanma ve mentalizasyon kavramları boylamsal ve deneysel araştırmalarla sınanmıştır; konumlar kuramı ya da ölüm "
             "dürtüsü gibi kavramlar ise büyük ölçüde klinik çıkarıma dayanır. Kuramsal çoğulculuk klinikte esneklik sağlar, ama "
             "her kavramın aynı güvenle öğretilmesini gerektirmez."),
            ("Anne merkezli bir anlatı",
             "Klasik gelişim kuramları ağırlıkla anne–bebek ikilisine odaklanır. Babaların, kardeşlerin, büyükanne ve büyükbabaların, "
             "akranların ve kurum bakımının etkisi daha az işlenir; geniş aile yapısının belirgin olduğu bağlamlarda okurun "
             "tamamlaması gereken bir eksiktir."),
        ],
        sorular=[
            S("Dokuz yaşındaki bir kız öğretmeni tarafından “çok uyumlu, hiç şikâyet etmeyen” biri olarak tanımlanıyor. Annesi ağır "
              "depresyon tedavisi görüyor. Çocuk görüşmede annesinin nasıl olduğunu sık sık soruyor, kendisi hakkında konuşmaktan "
              "kaçınıyor. Bu tablo en iyi hangi kavramla düşünülür?",
              ["Çatışmasız ego alanı", "Sahte kendilik", "Psişik eşdeğerlik", "Yakınlaşma krizi"],
              1, "Sahte kendilik, bakım verenin ihtiyaçlarına uyum için kendi duygu ve isteklerini geri çeken çocuğu tarif eder. "
                 "“Sorunsuz” görünmesi iç dünyasının ihmal edilmesine yol açabilir; tedavinin hedefi çocuğun kendi ihtiyaçlarının "
                 "görünür olacağı bir alan açmaktır."),
            S("İki yaşındaki bir erkek, kreşe başladıktan sonra annesine bir yapışıyor bir onu itiyor; anne “bir sevgi bir öfke, ne "
              "istediğini anlamıyorum” diyor. Bu dönem için en uygun gelişimsel çerçeve hangisidir?",
              ["Yakınlaşma (rapprochement) alt evresi", "Depresif konum", "Ödipal çatışma", "Latans dönemi"],
              0, "Yaklaşık 15–24. aylar arasında çocuk özerkliğini keşfederken bakım verene yeniden yaklaşma ihtiyacı duyar; yakınlık "
                 "ile ayrılık arasındaki bu gidip gelme normal gelişimin parçasıdır. Ebeveynin hem yakın hem sabırlı kalabilmesi bu "
                 "evrenin sağlıklı geçmesini destekler."),
            S("Bir koruyucu aile, yanlarına yerleştirilen 6 yaşındaki çocuğun “dezorganize bağlanma” gösterdiğini bir raporda okuyunca "
              "çocuğun kesinlikle istismara uğradığını düşünüyor. En doğru yanıt hangisidir?",
              ["Dezorganize bağlanma istismarın kesin kanıtıdır",
               "İstismarla ilişkili olabilir ama tek başına istismarı kanıtlamaz; kapsamlı değerlendirme gerekir",
               "Yalnızca mizaçla açıklanır",
               "Bağlanma örüntüsü 6 yaşından sonra değişmez"],
              1, "Dezorganize bağlanma istismara uğramış çocuklarda daha sıktır, ancak istismar olmayan ailelerde de görülür ve tek "
                 "başına tanı ya da adli kanıt değildir ([@granqvist2017]). Bağlanma örüntüleri yeni ilişkilerde ve uygun "
                 "müdahalelerle değişebilir."),
        ],
        akilda="Çocuğun iç dünyasındaki anne, odadaki anneyle aynı kişi değildir; ikisini birlikte dinleyin.",
    ),
    # ------------------------------------------------------------------ 3
    dict(
        no=3, kisim=1, kisa="Değerlendirme",
        baslik="Hastanın psikodinamik değerlendirmesi",
        slogan="İlk görüşme yalnızca veri toplamak değil, ilk müdahaledir.",
        kitapta=("Bölüm, psikodinamik görüşmeyi tıbbi öykü almadan ayıran özellikleri, ilk temasta başlayan aktarım ve karşı "
                 "aktarımı, çağrışımları izleyerek öykü almayı, ruhsal durum muayenesine eklenen dinamik gözlemleri ve bunların "
                 "bir formülasyonda nasıl birleştirileceğini anlatır."),
        okurken=[
            "Yazara göre görüşmeci, hastanın anlatısındaki boşluklara nasıl dikkat etmeli?",
            "Formülasyon tanıdan neden farklıdır; tanı neyi söyler, formülasyon neyi?",
            "Kültür, göç ve ayrımcılık deneyimi değerlendirmeye nasıl katılıyor?",
        ],
        fikirler=[
            ("Görüşme bir ilişkidir", "Yalnızca ne anlatıldığı değil, nasıl anlatıldığı, neyin atlandığı ve görüşmecide hangi duyguların "
             "uyandığı da veridir. Tanı ile tedavi arasındaki sınır bulanıktır: iyi bir ilk görüşme kendi başına iyileştirici olabilir."),
            ("Aktarım odaya sizden önce girer", "Hasta randevuya gelmeden önce psikiyatriste, hastaneye ve “doktor”a dair beklentiler "
             "taşır. Bu beklentileri erken adlandırmak ittifakı kolaylaştırır."),
            ("Çağrışımları izleyin", "Soru listesi yerine hastanın bir konudan ötekine geçişini izlemek, bilinçli olarak anlatılamayanın "
             "izini sürmenin yoludur. Hiç söz edilmeyen bir ebeveyn ya da dönem, söylenenler kadar önemlidir."),
            ("Stresörün anlamı kişiseldir", "Aynı olay iki kişide çok farklı tepkiler doğurur; belirleyici olan olayın büyüklüğünden "
             "çok kişinin benlik algısında neye dokunduğudur. “Neden şimdi?” sorusu formülasyonun anahtarıdır."),
            ("Formülasyon: tanının ötesi", "Biyolojik yatkınlık, gelişimsel öykü, ilişki örüntüleri, savunmalar ve güncel stresörün "
             "anlamı birkaç cümlelik bir anlatıda birleşir. İyi bir formülasyon tedavi önerisini ve olası güçlükleri öngörür."),
        ],
        crs=[
            "Görüşmenin başında ergene “Buraya gelmeden önce psikiyatrist hakkında ne düşünüyordun, sana ne söylediler?” diye sormak, damgayı ve korkuyu konuşulabilir kılar.",
            "İçi boş güvence (“her şey düzelecek”) ittifakı güçlendirmez; gerçekçi ve somut bir plan daha güven vericidir.",
            "Ebeveynlerden alınan gelişim öyküsünde hiç anılmayan kişi (ör. baba) ya da dönem (ör. kardeşin doğumu), sorulması gereken ilk konudur.",
            "Çocuğun istismarı gülerek ya da duygusuzca anlatması olayın önemsiz olduğunu göstermez; duygulanım çoğu zaman savunmanın vitrinidir. Adli değerlendirmede bu ayrım hayati önemdedir.",
            "Göç, mültecilik, afet ve ayrımcılık deneyimi olan ailelerde gündelik incinmeler ve kültürel anlam sistemleri değerlendirmenin parçasıdır.",
            "Ergenin duyduğu sesin ne dediğini ve kime ait olduğunu sormak hem risk değerlendirmesi hem formülasyon için bilgi verir.",
            "İntihar düşüncesi olan ergende yalnızca “var mı?” değil, “bu çözüm sana neyi sağlayacak gibi görünüyor?” diye sorun.",
        ],
        tartisma=[
            ("Formülasyonun güvenilirliği",
             "Psikodinamik formülasyonlar klinisyenden klinisyene belirgin biçimde değişebilir. Psikodinamik Tanı Kılavuzu (PDM-2) "
             "gibi yapılandırılmış sistemler, çocuk ve ergen bölümleriyle bu değişkenliği azaltmayı amaçlar ([@pdm2])."),
            ("Yapılandırılmış görüşmeyle birlikte",
             "Dinamik görüşme yapılandırılmış tanı görüşmelerinin yerini almaz; ikisi farklı soruları yanıtlar. Tanının güvenilirliği "
             "için yapılandırılmış araçlar, belirtinin anlamı için dinamik görüşme gerekir."),
            ("Kültürel formülasyon",
             "Kitabın kültüre duyarlılık vurgusu değerli, ancak örnekler büyük ölçüde ABD bağlamındandır. DSM-5’in Kültürel "
             "Formülasyon Görüşmesi ([@dsm5]) aile yapısı, din, göç ve afet deneyimi gibi yerel bağlamlara uyarlanarak kullanılabilir."),
        ],
        sorular=[
            S("On dört yaşındaki bir kız okul reddi nedeniyle annesiyle geliyor. Anne 40 dakika boyunca kızın gelişimini ayrıntılı "
              "anlatıyor; babadan hiç söz etmiyor. Kız sessiz. Görüşmecinin ilk dikkat etmesi gereken nokta hangisidir?",
              ["Annenin anlatımının ayrıntılı ve tutarlı olması", "Anlatıda babanın hiç geçmemesi",
               "Kızın sessizliğinin karşıt olma göstergesi olması", "Okul reddinin süresi"],
              1, "Psikodinamik öyküde anlatılmayan, anlatılan kadar bilgi taşır. Babanın yokluğu bir ayrılığa, kayba, çatışmaya ya da "
                 "ailedeki bir sırra işaret edebilir ve okul reddinin aile içindeki işlevini anlamak için kritiktir."),
            S("Cinsel istismar bildirimiyle değerlendirilen 11 yaşındaki bir erkek, olayları gülümseyerek ve “önemli değil” diyerek "
              "anlatıyor. En doğru yorum hangisidir?",
              ["Duygulanım uyumsuz olduğu için anlatı güvenilir değildir",
               "Gülümseme ve küçümseme dayanılmaz bir duyguya karşı savunma olabilir; anlatının güvenilirliğini tek başına belirlemez",
               "Çocuk olaydan etkilenmemiştir, destek gerekmez",
               "Çocuk büyük olasılıkla yönlendirilmiştir"],
              1, "Duygulanım ile içerik arasındaki uyumsuzluk sıklıkla bir savunmanın (inkâr, küçümseme, duygulanımın yalıtılması) "
                 "işaretidir. Ne anlatının yanlış olduğunu ne de çocuğun etkilenmediğini gösterir."),
            S("Formülasyondaki “Neden şimdi?” sorusunu en iyi karşılayan ifade hangisidir?",
              ["“Ailede depresyon öyküsü var.”", "“Okul başarısı yıllardır düşük.”",
               "“Belirtiler, annenin öfkesinden onu koruyan ablasının üniversite için evden ayrılmasından iki hafta sonra başladı.”",
               "“Utangaç bir mizacı var.”"],
              2, "“Neden şimdi?” yatkınlığı değil, tetikleyiciyi ve onun kişisel anlamını arar. Üçüncü seçenek hem zamanlamayı hem "
                 "olayın çocuk için anlamını (koruyucunun kaybı) birlikte verir."),
        ],
        akilda="Anlatılmayan kişi, sorulacak ilk kişidir.",
    ),
    # ------------------------------------------------------------------ 4
    dict(
        no=4, kisim=1, kisa="Bireysel psikoterapi",
        baslik="Tedaviler: bireysel psikoterapi",
        slogan="Keşfedici ile destekleyici arasında bir süreklilik vardır; hasta seanstan seansa bu çizgide yer değiştirir.",
        kitapta=("Bölüm, bireysel dinamik psikoterapiyi keşfedici–destekleyici bir süreklilik olarak tanımlar; yorumdan onaylamaya "
                 "uzanan müdahale yelpazesini, tarafsızlığı, terapötik ittifakı, direnci, aktarım yorumunu, sonlandırmayı ve kısa "
                 "süreli terapide odak seçimini tartışır."),
        okurken=[
            "Bir müdahaleyi “keşfedici” ya da “destekleyici” yapan nedir?",
            "Aktarım yorumu hangi durumlarda risklidir?",
            "Sonlandırma neden tedavinin bir evresi olarak ele alınıyor?",
        ],
        fikirler=[
            ("Bir süreklilik, iki uç", "Keşfedici uçta içgörü ve yorum, destekleyici uçta güçlendirme, yönlendirme ve “yardımcı ego” "
             "işlevi vardır. Çoğu terapi ikisini birlikte kullanır; hastanın o anki kapasitesi hangisinin ağır basacağını belirler."),
            ("Müdahale basamakları", "Müdahaleler, hastanın söylediğini yansıtmaktan açıklama istemeye, yüzleştirmeye ve yoruma doğru "
             "giderek daha yorumlayıcı hâle gelir. Kırılgan hastada alt basamaklarda kalmak, ittifak güçlendikçe yukarı çıkmak gerekir."),
            ("Tarafsızlık soğukluk değildir", "Tarafsızlık hastanın iç çatışmalarında taraf tutmamaktır; güvenlik ve yasal "
             "yükümlülükler söz konusu olduğunda klinisyen elbette taraftır."),
            ("Direnç merak konusudur", "Direnç tedavinin önündeki bir engel değil, hastanın neyden korunmaya çalıştığını gösteren bir "
             "bilgidir; onu kırmaya değil anlamaya çalışmak gerekir."),
            ("İttifak kopar ve onarılır", "Kopmanın fark edilip onarılması, çoğu hasta için ilişkilerin bozulduktan sonra da sürebileceğine "
             "dair yeni bir deneyimdir."),
            ("Sonlandırma da tedavidir", "Bitiş, kayıp ve ayrılık temalarını yeniden canlandırır. Rotasyon ya da tayin gibi dışarıdan "
             "dayatılan bitişler, önceden konuşulmazsa terk edilme deneyimini tekrarlayabilir."),
        ],
        crs=[
            "Çocuk ve ergen terapisinde yardımcı ego işlevi sık kullanılır: duyguyu adlandırmak, sonuçları birlikte düşünmek, sınır koymak. Bu, keşfedici çalışmanın zemini olabilir.",
            "Çocuk istismarını bildirmek tarafsızlığı bozmaz; çerçevenin parçasıdır. Bunu tedavinin başında aileye ve ergene açıkça söylemek sonraki krizleri hafifletir.",
            "Akran zorbalığına uğrayan çocukta içgörü üçgenini kullanın: bugünkü ilişki (zorbalar), geçmişteki ilişki (evde kime karşı edilgen kaldı?) ve sizinle olan ilişki.",
            "Geç gelen, susan, “bilmiyorum” diyen ergende direnç çoğu zaman bağımlı görünme korkusudur; “bilmiyorum”u bir yanıt olarak kabul edip merak etmek daha verimlidir.",
            "Çocuk terapisinde ittifak çoğuldur: çocukla, anneyle, babayla, bazen okulla ayrı ayrı ittifak gerekir; biri bozulduğunda tedavi tehlikeye girer.",
            "Rotasyon ya da tayin nedeniyle biten terapilerde bitiş tarihini haftalar önceden konuşun ve çocuğun vedalaşma biçimini izleyin.",
            "Kısa süreli terapide tek bir odak seçin (ör. kardeş doğumu sonrası kıskançlık ya da okul geçişi); her şeyi çalışmaya kalkmak hiçbir şeyi çalışmamaktır.",
        ],
        tartisma=[
            ("Kanıt artıyor ama sınırlı",
             "Uzun süreli psikodinamik terapinin karmaşık bozukluklarda etkili olduğunu gösteren meta-analizler "
             "([@leichsenring2008]; [@shedler2010]) ve çocuk–ergenlerde kısa süreli modeller için olumlu bulgular var ([@abbass2013]). "
             "Ancak çocuk ve ergen çalışmalarının önemli bir bölümü küçük örneklemli ve kontrol grupsuzdur; kapsamlı bir derlemede "
             "yalnızca 22 çalışma randomize kontrollüydü ([@midgley2021])."),
            ("İttifak mı sonucu belirler, sonuç mu ittifakı?",
             "İttifak ile sonuç arasındaki ilişki erişkinlerde r≈0,28 ([@fluckiger2018]), çocuk ve ergenlerde r≈0,19 "
             "([@karver2018]) düzeyindedir. İlişki korelasyoneldir: iyi giden tedavi ittifakı güçlendiriyor da olabilir."),
            ("Aktarım yorumu ne zaman?",
             "Aktarım yorumunun kırılgan hastada yararlı mı zararlı mı olduğu tartışmalıdır. Ergenlerde aktarımı doğrudan yorumlamak "
             "yerine onu şimdiki ilişkinin içinde merakla ele almak daha güvenli bir başlangıçtır."),
        ],
        sorular=[
            S("On altı yaşındaki bir erkek üç seanstır geç geliyor ve “canım konuşmak istemiyor” diyor. Direnci anlamaya çalışan en "
              "uygun yanıt hangisidir?",
              ["“Bu tavırla tedavi işe yaramaz; gelmek istemiyorsan bırakabiliriz.”",
               "“Gelmekle gelmemek arasında kalmış gibisin. Buraya gelmenin seni zorlayan bir yanı olabilir mi?”",
               "“Annen baban seni zorla getiriyor, değil mi? Onlarla konuşayım.”",
               "“Geç kalmalarını aile görüşmesinde ele alalım.”"],
              1, "Direnç kırılacak bir engel değil, anlaşılacak bir mesajdır. İkinci seçenek davranışı yargılamadan gözlemler ve "
                 "ikircikliliği konuşulabilir kılar. Birincisi terk edilme beklentisini doğrular; diğerleri ergenin kendi deneyimini atlar."),
            S("Annesi hastanede yatan 8 yaşındaki bir kız seansta sürekli oyunu yarıda kesiyor ve terapistin saatine bakıyor. "
              "Destekleyici uca yakın, uygun müdahale hangisidir?",
              ["“Bana kızgın olduğun için oyunu bozuyorsun.”",
               "“Annen hastanedeyken buradaki zamanın ne zaman biteceğini bilmek istiyor gibisin. Bitime on dakika kala haber vereyim mi?”",
               "Saati çocuğun göremeyeceği bir yere kaldırmak",
               "Oyunu bırakıp annenin hastalığını ayrıntılı konuşmak"],
              1, "İkinci seçenek davranışın olası anlamını nazikçe adlandırır ve kriz içindeki çocuğa öngörülebilirlik ve kontrol sunar. "
                 "Birincisi erken ve suçlayıcı bir aktarım yorumudur; sonuncusu çocuğun savunmasını zorlar."),
            S("Bir asistan iki ay sonra rotasyona çıkacak ve 13 yaşındaki hastası bunu henüz bilmiyor. En uygun yaklaşım hangisidir?",
              ["Son seansta bildirmek, böylece hasta gereksiz yere üzülmez",
               "Bitişi haftalar öncesinden konuşmak, hastanın tepkilerini izlemek ve devri planlamak",
               "Devri sekreterin bildirmesi",
               "Hastaya söylemeden yeni terapisti seansa davet etmek"],
              1, "Sonlandırma ayrılık ve kayıp temalarını canlandırır. Erken konuşulan bitiş, ergenin duygularını ifade etmesine ve terk "
                 "edilme deneyiminin bu kez farklı yaşanmasına alan açar."),
        ],
        akilda="Direnci kırmayın, merak edin; bitişi saklamayın, konuşun.",
    ),
    # ------------------------------------------------------------------ 5
    dict(
        no=5, kisim=1, kisa="Grup, aile, ilaç",
        baslik="Tedaviler: grup, aile ve evlilik terapisi, farmakoterapi",
        slogan="Reçete bir molekül değil, bir mesajdır.",
        kitapta=("Bölüm üç alanı bir araya getirir: dinamik grup terapisi (grubun farkında olunmayan varsayımları, rol emilmesi, "
                 "günah keçisi), aile ve çift terapisi (belirlenmiş hasta, çiftin işbölümü, tarafsızlık) ve dinamik farmakoterapi "
                 "(uyum, ilacın anlamı, karşı aktarım ve terapötik ittifak)."),
        okurken=[
            "Grup ve aile bireysel patolojiyi nasıl üretir ya da sürdürür?",
            "İlaç uyumunu belirleyen psikolojik etkenler nelerdir?",
            "Çoklu ilaç kullanımının bir karşı aktarım tepkisi olabileceği fikri hangi gözlemlere dayanıyor?",
        ],
        fikirler=[
            ("Her grubun görünmeyen bir gündemi vardır", "Gruplar açık görevlerinin yanında, kaygıyla baş etmek için ortak ve çoğu zaman "
             "farkında olunmayan varsayımlarla hareket eder: bir lidere bağımlılık, bir düşmana karşı birleşme, bir kurtarıcı beklentisi."),
            ("Günah keçisi ve belirlenmiş hasta", "Grup ya da aile, tahammül edemediği duyguları bir üyeye yükleyebilir. O üyenin "
             "belirtileri sistemin dengesini korur; o düzeldiğinde başka bir üye bozulabilir."),
            ("Çift bir işbölümüdür", "Ebeveynlerden biri sertleştikçe öteki yumuşar; kutuplaşma bir kişilik özelliğinden çok karşılıklı "
             "bir düzenlemedir ve çocuk bu düzenlemenin ortasında yaşar."),
            ("Uyum bir ilişkidir", "İlaç uyumu hastanın hekimle kurduğu ilişkiden, ilacın onun için taşıdığı anlamdan ve kontrol "
             "ihtiyacından etkilenir. Otoriter tutum çoğu zaman ters teper."),
            ("Hekimin duyguları da reçeteye girer", "Çaresizlik, öfke ya da “bir şey yapmalıyım” baskısı gereksiz doz artışına ve ilaç "
             "eklemeye yol açabilir; çoklu ilaç kullanımı kimi zaman hastanın değil hekimin kaygısını tedavi eder."),
            ("Sözcükler yan etkiyi değiştirir", "Yan etkilerin nasıl anlatıldığı beklentiyi ve dolayısıyla deneyimi etkiler (nosebo). "
             "Aynı bilgiyi korkutmadan ve doğru biçimde vermek mümkündür."),
        ],
        crs=[
            "Ergen grubunda bir akranın geri bildirimi, terapistin aynı sözlerinden daha kolay kabul edilir; otoriteyle çatışan ergende grup, bireysel terapinin ulaşamadığı yere ulaşabilir.",
            "Sınıfta zorbalığın hedefi rastgele seçilmez; müdahale yalnızca zorbayı değil sınıfın dinamiğini de hedeflemelidir.",
            "Çocuk düzeldiğinde ailede başka bir sorun belirginleşiyorsa (kardeşte belirti, ebeveynler arasında kavga) bu bir başarısızlık değil, belirtinin aile içindeki işlevine dair bir bulgudur.",
            "Boşanma sürecindeki ailelerde “hangi ebeveyn haklı?” sorusuna çekilmek en yaygın tuzaktır; belirli bir sonuca aşırı bağlandığınızı fark ettiğinizde taraf tutmaya başlamış olabilirsiniz.",
            "Ergenin bireysel terapisi ile ebeveyn görüşmelerini mümkünse farklı klinisyenler yürütsün; gizlilik sınırlarını baştan açıkça konuşun.",
            "Karşı-bağımlı ergene kontrol verin: dozu ne zaman alacağı, ilacı kimin saklayacağı ve yan etki olursa ne yapılacağı birlikte planlansın.",
            "Açıklamayı anneye değil çocuğa yapın, adını kullanın, ona doğrudan bakın; bunlar nezaketin ötesinde uyumu artıran ittifak araçlarıdır.",
            "Üçüncü ilacı eklemeden önce durun ve sorun: bu karar kanıttan mı, çaresizlikten mi çıkıyor?",
        ],
        tartisma=[
            ("İttifak ilaç tedavisinde de önemli",
             "Ulusal bir depresyon çalışmasında terapötik ittifak psikoterapi kollarının yanı sıra aktif ilaç ve plasebo kollarında da "
             "sonucu yordadı ([@krupnick1996]). İletişim ile ilaç uyumu arasındaki ilişki gerçek ama mutlak farklar küçüktür: diyabetli "
             "erişkinlerde hekim iletişimini kötü değerlendirenlerde yetersiz uyum 4–6 yüzde puan daha sıktı ([@ratanawongsa2013])."),
            ("Ailedeki eleştirinin gücü",
             "Yüksek ifade edilen duygu (eleştiri, düşmanlık, aşırı katılım) şizofrenide relapsı yordar; bu ilişki duygudurum ve yeme "
             "bozukluklarında daha da güçlüdür ([@butzlaff1998]). Bulgu aileyi suçlamak için değil, aileyle birlikte çalışmak için "
             "kullanılmalıdır."),
            ("Gizlilik ve ergen",
             "Kitap ergen terapisinde gizlilik, ebeveynle bilgi paylaşımı ve özerklik dengesine ayrı bir yer vermez. Bu konular yerel "
             "mevzuat ve meslek etiği kılavuzlarıyla tamamlanmalıdır."),
        ],
        sorular=[
            S("On beş yaşındaki bir kız, depresyon için başlanan antidepresanı düzenli almıyor. Annesi her sabah ilacı eline verip "
              "yutmasını izliyor. Kız “Bebek gibi davranılmaktan bıktım” diyor. En uygun yaklaşım hangisidir?",
              ["Annenin denetimini artırmak", "İlacı uzun etkili bir forma geçirmek",
               "Kızla, ilacın ne zaman ve nasıl alınacağında kontrolün bir kısmını ona bırakan bir plan yapmak ve bunu anneyle konuşmak",
               "İlacı kesip yalnızca terapiye devam etmek"],
              2, "Bu ergende uyumsuzluk ilaçtan çok kontrol ve özerklik çatışmasının ifadesidir. Kontrolü paylaşan bir plan, ilacı "
                 "ebeveynle savaşın aracı olmaktan çıkarır. İntihar riski varsa ilaçların güvenli saklanması ayrıca planlanır."),
            S("Davranım sorunları olan 11 yaşındaki bir erkek yatışından iki hafta sonra belirgin düzeliyor. Aynı hafta 7 yaşındaki "
              "kardeşinde okulda saldırganlık başlıyor ve ebeveynler sık kavga etmeye başlıyor. Bu tabloyu en iyi hangi kavram açıklar?",
              ["Tesadüf", "Belirlenmiş hasta: belirtinin aile dengesindeki işlevi", "İlaç yan etkisi",
               "Kardeşin kıskançlığı; başka açıklama gerekmez"],
              1, "Belirtiler aile sisteminin dengesini korumaya hizmet ediyor olabilir. Belirlenmiş hasta düzeldiğinde sistem dengeyi "
                 "yeniden kurmak için başka bir taşıyıcı arayabilir; aile değerlendirmesinin gerekçesi budur."),
            S("Yan etkileri anlatırken nosebo etkisini azaltma olasılığı en yüksek ifade hangisidir?",
              ["“Bu ilaç ciddi yan etkiler yapabilir, prospektüsü mutlaka okuyun.”",
               "“Bu ilacı alanların çoğu belirgin bir yan etki yaşamaz; bir kısmında ilk haftalarda hafif bulantı olabilir ve genellikle geçer. Olursa bana ulaşın.”",
               "“Yan etki olmaz, merak etmeyin.”", "Yan etkilerden hiç söz etmemek"],
              1, "İkinci seçenek doğru bilgiyi verir, olumlu çerçeveyi korur ve bir eylem planı sunar. Birincisi gereksiz kaygı yaratır; "
                 "son ikisi aydınlatılmış onam ilkesine aykırıdır ve güveni zedeler."),
        ],
        akilda="İlacı yazarken ne söylediğinizi de yazmış olursunuz.",
    ),
    # ------------------------------------------------------------------ 6
    dict(
        no=6, kisim=1, kisa="Servis ve ekip",
        baslik="Tedaviler: çok tedavi edicili ortamlar",
        slogan="Servisteki kaos, çocuğun iç dünyasının dışarı serilmiş hâlidir.",
        kitapta=("Bölüm, yataklı servis ve gündüz hastanesi gibi birden çok tedavi edicinin bulunduğu ortamlarda hastanın iç ilişki "
                 "örüntülerini ekibe nasıl taşıdığını, bölmenin ekip düzeyinde nasıl işlediğini, ekip toplantısının işlevini ve "
                 "ilacı birinin, psikoterapiyi başkasının yürüttüğü bölünmüş tedaviyi ele alır."),
        okurken=[
            "Hasta iç dünyasını ekibe hangi yollarla taşır?",
            "Ekip bölünmesini önlemek mi, izlemek mi amaçlanmalı?",
            "Bölünmüş tedavide iki klinisyen arasındaki ilişki neden bu kadar önemli?",
        ],
        fikirler=[
            ("Hasta iç dünyasını ortama serer", "Hasta iç ilişki örüntülerini ekip üyeleriyle yeniden kurar; servisteki ilişkiler, ailede "
             "ve geçmişte yaşananları doğrudan gözlemleme fırsatıdır."),
            ("Tekrar bir iletişimdir", "Hasta yaşadıklarını yineler: edilgen yaşadığına etkin olarak hâkim olmak, tanıdık bağları korumak, "
             "anlatamadığını başkasında yaşatarak iletmek ya da bu kez farklı bir yanıt almak için."),
            ("Sınır eksik yapının yerini tutar", "Kurallar ceza değil, hastanın henüz içselleştiremediği düzenlemeyi dışarıdan sağlayan "
             "bir destek olarak tasarlanmalıdır."),
            ("Bölme ekipte yaşanır", "Hasta kimi ekip üyelerini idealleştirip kimilerini değersizleştirdiğinde ekip de “iyi” ve “kötü” "
             "kutuplara ayrılabilir. Hasta çoğu zaman ekipte zaten var olan bir çatlağı bulur."),
            ("Ekip toplantısı bir tedavi aracıdır", "Karşı aktarımın konuşulmadığı toplantı yalnızca vaka yönetimidir. Ekip üyelerinin "
             "hissettikleri hastanın iç dünyası ve ailesi hakkında bilgi taşır."),
            ("Bölünmüş tedavide iki model tehlikesi", "İlacı ve terapiyi farklı kişiler yürüttüğünde hastaya birbiriyle çelişen hastalık "
             "modelleri sunulabilir; düzenli iletişim ve ortak bir anlatı gerekir."),
        ],
        crs=[
            "“Bu hasta serviste kaos yaratıyor” bir şikâyet değil, formülasyonun başlangıcıdır; servisteki örüntüyü evdeki örüntüyle karşılaştırın.",
            "İstismarcı eve dönmek isteyen çocuk kötü muameleyi değil öngörülebilirliği seçiyor olabilir; koruyucu aile yerleştirmelerindeki erken kopuşlar bu açıdan okunabilir.",
            "Yalnızca şefkat sunan, hiç sınır koymayan ortam iyileştirici değildir; çocuk eski örüntüsünü sahneleyemez ve dolayısıyla onu dönüştüremez.",
            "Ekip toplantısında “Bu çocuk sende ne uyandırıyor?” sorusunu düzenli sorun; hemşirenin hissettiği, annenin her gün hissettiği şey olabilir.",
            "“Beni anlayan tek kişi sensin” cümlesi bir övgü değil, bir bulgudur; kimin değersizleştirildiğini sorun.",
            "Bölme belirdiğinde iki ekip üyesini (ya da iki ebeveyni) aynı odaya alıp makul biçimde konuşturmak en güçlü bütünleştirici müdahaledir.",
            "Serviste ani olay artışı (kaçma, kural ihlali) olduğunda, önce ekipte konuşulmamış bir anlaşmazlık olup olmadığına bakın.",
            "Ergen tedavisi çoğu zaman bölünmüştür (ilaç, psikoterapi, aile, okul); her halkanın aynı hastalık modelini paylaşması için düzenli iletişim kurun.",
        ],
        tartisma=[
            ("Kısa yatış, güçlü izlem",
             "Ergenlerde yoğun toplum temelli destekli taburculuk hizmeti, olağan bakıma göre yatak kullanımını azalttı; ancak "
             "işlevsellik ve belirtiler üzerinde ek bir etki göstermedi ([@ougrin2018]). Yani kısa yatış daha iyi sonuç değil, benzer "
             "sonucu daha az yatakla sağlıyor olabilir."),
            ("Bölme kavramının riski",
             "Ekip çatışmalarını hastanın bölmesine bağlamak klinik olarak aydınlatıcı olabilir, ama kurumsal sorunların (iş yükü, "
             "hiyerarşi, kaynak eksikliği) sorumluluğunu hastaya yükleme riski taşır. Kavram ampirik olarak az sınanmıştır."),
            ("Ortam terapisinin değişen zemini",
             "Klasik ortam terapisi uzun yatışlar için geliştirildi. Bugünün kısa yatışlarında bu ilkelerin hangilerinin işe yaradığı "
             "ayrıca araştırılmayı bekliyor."),
        ],
        sorular=[
            S("Ergen servisinde 16 yaşındaki bir hasta bir hemşireyi “tek anlayan” olarak övüyor, diğerlerini “soğuk” buluyor. Ekip "
              "toplantısında bu hemşire hastayı sürekli savunuyor. En uygun ilk adım hangisidir?",
              ["Övülen hemşireyi hastanın bakımından çekmek",
               "Toplantıda idealleştirme ve değersizleştirme örüntüsünü adlandırıp ekip üyelerinin farklı deneyimlerini bir araya getirmek",
               "Hastaya “bölme yapıyorsun” diye yorum yapmak",
               "Diğer hemşirelere daha sıcak olmalarını söylemek"],
              1, "Amaç bölmeyi önlemek değil fark edip bütünleştirmektir. Farklı deneyimleri aynı masada konuşmak, hastanın parçalanmış "
                 "iç temsillerinin ekip içinde birleştirilmesine yardım eder. Erken ve suçlayıcı yorum hastayı savunmaya iter."),
            S("Koruma altındaki 10 yaşındaki bir çocuk, kendisine çok iyi davranan koruyucu ailesinin yanında giderek daha çok kural "
              "ihlal ediyor ve “eski evime dönmek istiyorum” diyor. En olası dinamik açıklama hangisidir?",
              ["Çocuk koruyucu aileyi sevmiyor",
               "Çocuk tanıdık ilişki örüntüsünü arıyor ve yeni ilişkiyi sınıyor; tutarlı sınır ve sıcaklık birlikte gerekir",
               "Çocuğa daha fazla ayrıcalık verilmeli",
               "Dikkat eksikliği nedeniyle kuralları unutuyor"],
              1, "İhmal ve istismar yaşamış çocuk için öngörülebilir olan, iyi olandan daha güvenli gelebilir. Kural ihlali, yeni bakım "
                 "verenin de eskisi gibi tepki verip vermeyeceğini sınar. Sınır ve sıcaklığı birlikte sunan tutarlı yanıt, eski "
                 "örüntünün dönüşmesine alan açar."),
            S("Bir ergende ilacı çocuk psikiyatristi, psikoterapiyi bir psikolog yürütüyor. Psikolog ergene “sorunun tamamen aile "
              "ilişkileriyle ilgili, ilaca gerek yok” derken psikiyatrist aileye “kimyasal bir dengesizlik var” diyor. En önemli risk "
              "hangisidir?",
              ["İlacın etkisinin azalması",
               "Ergenin iki çelişen hastalık modeli arasında kalması ve klinisyenleri birbirine karşı konumlandırması",
               "Terapinin uzaması", "Ailenin ikinci görüş istemesi"],
              1, "Bölünmüş tedavide en tehlikeli şey hastaya birbiriyle çelişen hastalık modelleri sunulmasıdır; bu bölmeyi besler ve "
                 "uyumu bozar. Klinisyenler düzenli iletişim kurmalı ve ortak bir anlatı sunmalıdır."),
        ],
        akilda="Çocuklar, yetişkinlerin konuşmadığını sahneler.",
    ),
    # ------------------------------------------------------------------ 7
    dict(
        no=7, kisim=2, kisa="Şizofreni",
        baslik="Şizofreni",
        slogan="Hastalık bir kişinin başına gelir; o kişi de gelişimsel görevlerinin ortasındadır.",
        kitapta=("Bölüm, şizofreniyi biyolojik bir hastalık olarak kabul ederken hastanın öznel deneyimini, ilacın anlamını, bireysel "
                 "ve aile müdahalelerini, ifade edilen duygu araştırmalarını ve kısa yatışın amaçlarını dinamik bir bakışla tartışır."),
        okurken=[
            "Yazar, aileyi hastalığın nedeni sayan eski kuramların bıraktığı zararı nasıl değerlendiriyor?",
            "Psikotik deneyimi anlamlandırarak iyileşen hastalar ile üstünü kapatarak iyileşenler arasındaki fark tedaviyi nasıl etkiliyor?",
            "Aile müdahalelerinde hedef aileyi değiştirmek mi, desteklemek mi?",
        ],
        fikirler=[
            ("Kişi hastalığından büyüktür", "Etiyoloji ne kadar biyolojik olursa olsun, hastalık belirli bir kişinin hayatına, ilişkilerine "
             "ve kimliğine yerleşir; tedavi bu kişiyi de hedeflemelidir."),
            ("Üç küme, farklı müdahaleler", "Pozitif belirtiler, negatif belirtiler ve ilişkisel güçlükler farklı yaklaşımlar gerektirir; "
             "ilaçlar en çok ilk kümeye etki eder."),
            ("Ebeveyn suçlamasının bedeli", "Aileyi hastalığın nedeni sayan kuramlar bilimsel olarak terk edilmiş ve ailelere ağır bir yük "
             "bırakmıştır. Bugünkü bakış ailenin hastalıktan etkilendiğini ve etkileşimlerinin seyri etkileyebileceğini kabul eder."),
            ("İyileşmenin krizi", "Remisyon, kaybedilen zamanla ve değişen gelecek beklentisiyle yüzleşmeyi de getirir; depresyon ve "
             "intihar riski tam bu dönemde artabilir."),
            ("Anlamak mı, kapatmak mı?", "Bazı hastalar psikotik deneyimi anlamlandırarak, bazıları üstünü kapatarak iyileşir. "
             "İkincisini keşfe zorlamak yardım değil, zarar olabilir."),
            ("Aile müdahalesinin yeri", "Psikoeğitim ve eleştiriyi azaltmaya yönelik aile çalışmaları relapsı azaltan, kanıtı en sağlam "
             "psikososyal yaklaşımlar arasındadır."),
        ],
        crs=[
            "İlk psikotik atağı geçiren ergen aynı anda kimlik kuruyor, akranlarına tutunmaya çalışıyor ve aileden ayrışıyor; tedavi planı bu gelişimsel görevleri de içermelidir.",
            "Premorbid ve prodromal dönemi gören çoğu zaman ÇRS’dir: açıklanamayan okul başarısı düşüşü, arkadaşlardan çekilme, yeni tuhaf inançlar ve kişilik değişimi birlikte değerlendirilmelidir.",
            "Geri çekilmiş ergende “negatif belirti” demeden önce depresyonu, antipsikotik yan etkisini (akinezi, sedasyon) ve uyaransız ortamı dışlayın.",
            "Büyüklenmeci bir sanrı alevlendiğinde hemen öncesinde hangi aşağılanmanın yaşandığını sorun: sınav sonucu, akran reddi, ebeveyn eleştirisi.",
            "Sanrıyla tartışmayın; içeriğini ergenin gelişimsel temaları (beden, cinsellik, ayrılık, izlenme) açısından dinleyin.",
            "“Bir daha konuşmak istemiyorum” diyen ergeni keşfe zorlamayın; bu da geçerli bir iyileşme yoludur.",
            "Barınma ve bakım düzeni istikrarsızsa içgörü çalışmasını erteleyin; önce güvenli bir yer.",
            "Ailelere “daha az ilgilenin” değil “eleştiriyi azaltın, ilgiyi koruyun” deyin; bu hem kanıta hem kültüre daha uygundur.",
            "İlacı ergenin kendi diliyle anlatın; “kafandaki hastalık” yerine “gürültüyü süzen sistem” gibi bir benzetme daha kabul edilebilir olabilir.",
        ],
        tartisma=[
            ("Riskli zihin durumu bir kader değil",
             "Klinik yüksek riskli gençlerde psikoza geçiş riski 1 yılda yaklaşık %15, 3 yılda yaklaşık %25’tir ([@salazar2021]); "
             "yani çoğu genç psikoza geçmez. Erken müdahale hizmetleri ise erken evre psikozda olağan bakımdan daha iyi sonuç verir "
             "([@correll2018]). İkisi birlikte dikkatli bir izlem, ama kaderci olmayan bir dil gerektirir."),
            ("İfade edilen duygu ve kültür",
             "Ailedeki yüksek ifade edilen duygu relapsın güçlü bir yordayıcısıdır ([@butzlaff1998]); ancak kavram Batı örneklemlerinde "
             "geliştirildi ve “aşırı katılım”ın anlamı kültürler arasında farklıdır. Yoğun ilginin koruyucu, eleştirinin zararlı "
             "olabileceği ayrımı bu nedenle önemlidir."),
            ("Psikoterapinin yeri",
             "Şizofrenide bireysel psikodinamik terapinin kanıt temeli, psikoz için bilişsel davranışçı terapiye ve aile müdahalelerine "
             "göre zayıftır. Dinamik anlayış tek başına bir tedaviden çok ittifak, uyum ve anlam üzerine çalışmanın çerçevesi olarak "
             "değerlidir."),
        ],
        sorular=[
            S("On yedi yaşındaki bir erkek ilk psikotik ataktan sonra remisyonda. İki ay sonra okula dönmüyor ve “artık eski ben "
              "değilim, hayatım bitti” diyor. En öncelikli klinik değerlendirme hangisidir?",
              ["Antipsikotik dozunu artırmak",
               "Depresyon ve intihar riskini değerlendirmek; kayıplar ve gelecek beklentisi üzerine konuşmak",
               "Negatif belirti olarak kaydedip bilişsel rehabilitasyona yönlendirmek",
               "Okula dönüşü zorunlu tutmak"],
              1, "Remisyon, kaybedilen zamanla ve değişen gelecekle yüzleşmenin başladığı dönemdir. Psikoz sonrası depresyon ve intihar "
                 "riski bu evrede artabilir; önce bunlar değerlendirilmelidir."),
            S("Şizofreni tanılı 16 yaşındaki bir kızın annesi kızının her şeyiyle ilgileniyor; sık sık “yine mi uyudun, böyle giderse "
              "hiçbir şey olamayacaksın” diyor. Aile müdahalesinin öncelikli hedefi ne olmalıdır?",
              ["Annenin ilgisini azaltmak", "Eleştirel yorumları azaltırken desteği ve ilgiyi korumak",
               "Kızı aileden ayrı bir yere yerleştirmek", "Anneyi bireysel terapiye yönlendirip aile görüşmesi yapmamak"],
              1, "Relapsla en güçlü ilişkili bileşen eleştiridir. İlgi ve katılım ise, özellikle aile bağlarının güçlü olduğu "
                 "kültürlerde, koruyucu olabilir. Psikoeğitim ve iletişim becerileriyle eleştiriyi azaltmak hedeflenir."),
            S("Klinik yüksek risk ölçütlerini karşılayan 15 yaşındaki bir ergenin ailesi “Şizofreni olacak mı?” diye soruyor. En doğru "
              "yanıt hangisidir?",
              ["“Evet, önümüzdeki yıllarda büyük olasılıkla gelişecek.”",
               "“Risk artmış durumda, ancak bu durumdaki gençlerin çoğu psikoza geçmez; düzenli izlem ve destekle riski birlikte yöneteceğiz.”",
               "“Endişelenmeyin, ergenlikte bu normaldir.”", "“Önleyici olarak hemen antipsikotik başlayalım.”"],
              1, "Klinik yüksek riskli gençlerde geçiş riski üç yılda yaklaşık dörtte birdir ([@salazar2021]). Doğru bilgi hem paniği "
                 "hem ihmali önler; önleyici antipsikotik kullanımı rutin olarak önerilmez."),
        ],
        akilda="Sanrıyla tartışmayın; içindeki gelişimsel soruyu dinleyin.",
    ),
    # ------------------------------------------------------------------ 8
    dict(
        no=8, kisim=2, kisa="Duygudurum",
        baslik="Duygudurum bozuklukları",
        slogan="“Bu kayıp neyi kaybettirdi?” kadar “neyi aşağıladı?” sorusu da önemlidir.",
        kitapta=("Bölüm, gen–çevre etkileşimi ve erken kayıplar üzerine araştırmalardan başlayarak depresyonun psikodinamik "
                 "modellerini özetler; intiharın psikodinamiğini ve intihar riski olan hastayla çalışırken klinisyenin kendi "
                 "tepkilerini tartışır."),
        okurken=[
            "Yazar tek bir depresyon formülü olmadığını nasıl gösteriyor?",
            "İlişki odaklı (anaklitik) ve öz-eleştirel (içe atımsal) depresyon tedavide neden farklı ele alınmalı?",
            "İntihar riski olan hastada klinisyenin hangi duyguları tehlikeli olabilir?",
        ],
        fikirler=[
            ("Stresörün anlamı", "Aynı olay bir kişide kayıp, ötekinde aşağılanma olarak yaşanabilir; depresyonu yordayan çoğu zaman "
             "olayın büyüklüğünden çok kişinin benlik tanımında neye dokunduğudur."),
            ("Erken kayıp ve stres biyolojisi", "Erken ayrılık ve kötü muamele stres yanıt sistemini kalıcı biçimde duyarlı hâle "
             "getirebilir; bu, küçük stresörlere orantısız tepkiyi açıklamaya yardım eder."),
            ("İki depresyon tipi", "Bir tip ilişki ve bakım kaybına (“kimse beni sevmiyor”), öteki başarısızlık ve öz-eleştiriye "
             "(“yeterince iyi değilim”) odaklanır. İkincisi daha işlevsel görünebilir ve gözden kaçabilir."),
            ("Başkası için yaşamak", "Hayatını önemli bir ötekini memnun etmek üzerine kurmuş kişi, o ilişki ya da hedef çöktüğünde "
             "boşluğa düşer. Tedavi önce kendisi için hiç yaşamadığını fark etmesine yardım etmektir."),
            ("Umutsuzluk bir alarmdır", "İntihar riskinde depresyonun şiddetinden çok umutsuzluk ve intihar düşüncesinin "
             "kabullenilmişliği belirleyicidir."),
            ("Kurtarıcı tutum bir tuzaktır", "Sınırsız erişilebilirlik vaat etmek güven değil kaçınılmaz bir hayal kırıklığı üretir; "
             "klinisyenin sakin ve tutarlı kalması en güçlü mesajdır."),
        ],
        crs=[
            "Boşanma öyküsünde yalnızca “ayrılık var mı?” değil, “ne zaman ve hangi biçimde?” diye sorun; ölüm, terk, kademeli ya da ani ayrılık farklı riskler taşır.",
            "Ergende “kendini neyle tanımlıyor: ilişkiyle mi, başarıyla mı?” sorusu, hangi olayın depresyonu tetikleyebileceğini önceden söyler.",
            "Okulda başarılı, mükemmeliyetçi ve öz-eleştirel “iyi çocuk”un depresyonu kolay gözden kaçar; intihar riski açısından ayrıca taranmalıdır.",
            "Bir yakının intiharının yıldönümü ergen için yüksek riskli bir penceredir; bu tarihi klinik takvime işleyin.",
            "Ergene yalnızca “intihar düşüncen var mı?” değil, “bu düşünceyle mücadele ediyor musun, yoksa kabullenmiş gibi mi hissediyorsun?” diye sorun.",
            "Ebeveynlerin “bu kadar şeyin varken neden üzgünsün?” cümlesi çocuğu yalnızlaştırır; ebeveyn danışmanlığında ilk düzeltilecek şeylerdendir.",
            "Eleştirel yorum sıklığını azaltmak aileye verilebilecek somut ve izlenebilir bir hedeftir.",
            "Güvenlik planını ergen ve aileyle birlikte yazın; imzalı bir söz istemek yerine adım adım ne yapılacağını belirleyin.",
        ],
        tartisma=[
            ("Ergen depresyonunda üç tedavi, benzer sonuç",
             "11–17 yaş arası 470 ergende yapılan randomize bir çalışmada bilişsel davranışçı terapi, kısa süreli psikanalitik terapi ve "
             "kısa psikososyal müdahale 86. haftada benzer sonuç verdi ([@goodyer2017]). Bu, dinamik terapinin geçerli bir seçenek "
             "olduğunu gösterir; ama “erken travma varsa önce psikoterapi” gibi özgül önermeleri tek başına desteklemez."),
            ("Mükemmeliyetçilik ve tedavi yanıtı",
             "Ulusal bir depresyon çalışmasının yeniden analizinde mükemmeliyetçilik dört tedavi kolunun hepsinde daha kötü sonuçla "
             "ilişkiliydi ve tedavi türüyle etkileşim göstermedi ([@blatt1995]). Bu grubun uzun süreli dinamik terapiye daha iyi yanıt "
             "verdiği ise bu çalışmada sınanmadı."),
            ("Güvenlik planı, sözleşme değil",
             "İntihar etmeme sözleşmelerinin etkinliğine dair ampirik destek yoktur ([@rudd2006]). Güvenlik planı ve telefonla izlem, "
             "acil servise başvuran erişkinlerde intihar davranışında yaklaşık %45 azalmayla ilişkili bulundu ([@stanley2018]); ergenler "
             "için kanıt daha sınırlıdır. Umutsuzluk ise uzun dönem intihar riskinin bilinen bir göstergesidir ([@beck1985])."),
            ("Gen–çevre örneği doğrulanmadı",
             "Kitapta anlatılan serotonin taşıyıcı geni ile stres etkileşimi büyük ortak analizlerde doğrulanmadı "
             "([@culverhouse2018]; [@border2019]); stresin kendisi ise güçlü bir risk etkeni olarak kaldı."),
        ],
        sorular=[
            S("On altı yaşında okul birincisi bir kız, deneme sınavı sonucunun beklentisinin altında kalmasının ardından derin bir "
              "çöküş yaşıyor: “Başarısızım, kimseye faydam yok.” Arkadaş ilişkileri iyi. Tablo en çok hangi tipe uyar?",
              ["İlişki odaklı (anaklitik) depresyon", "Öz-eleştirel (içe atımsal) depresyon", "Mevsimsel depresyon",
               "Depresyon değil, olağan bir hayal kırıklığı"],
              1, "Öz-eleştiri, başarısızlık ve değersizlik temaları içe atımsal tipi düşündürür. Bu ergenler dışarıdan işlevsel görünür "
                 "ve kolay gözden kaçar; intihar riski ayrıca değerlendirilmelidir."),
            S("Annesi iki yıl önce intihar sonucu ölen 14 yaşındaki bir erkek son haftalarda giderek sessizleşiyor. Ölümün yıldönümüne "
              "üç hafta var. En uygun klinik adım hangisidir?",
              ["Yıldönümünü konuşmamak, çünkü tetikleyebilir",
               "Yıldönümünü klinik takvime işlemek, bu dönemi çocuk ve ailesiyle açıkça konuşmak, izlemi sıklaştırmak ve güvenlik planı yapmak",
               "Antidepresan dozunu önleyici olarak artırmak", "Yalnızca okul rehberlik servisine bilgi vermek"],
              1, "Yakının intiharının yıldönümleri yüksek riskli dönemlerdir. Konuyu açıkça konuşmak riski artırmaz; sessizlik ise "
                 "yalnızlığı derinleştirebilir."),
            S("Ebeveyn danışmanlığında depresif ergenin relaps riskini azaltmak için en somut hedef hangisidir?",
              ["Ergeni her gün neşelendirmeye çalışmak", "Evde eleştirel yorumların sıklığını azaltmak",
               "Ergenin bütün sorumluluklarını kaldırmak", "Depresyon hakkında hiç konuşmamak"],
              1, "Erişkin depresyonunda eşin ne kadar eleştirel algılandığı relapsın en iyi yordayıcısıydı ([@hooley1989]); ailede "
                 "eleştiriyi azaltmak somut bir hedeftir. “Neşelendirme” çabası ise ergenin duygusunu geçersiz kılıp yalnızlaştırabilir."),
        ],
        akilda="Umutsuzluğu sorun; neşelendirmeyin, doğrulayın.",
    ),
    # ------------------------------------------------------------------ 9
    dict(
        no=9, kisim=2, kisa="Anksiyete",
        baslik="Anksiyete bozuklukları",
        slogan="Kaygının içeriği kadar hangi kaybın korkusunu taşıdığı da önemlidir.",
        kitapta=("Bölüm, kaygıyı gelişimsel olarak katmanlanmış bir sinyal olarak ele alır; panik bozukluğu, fobiler ve yaygın "
                 "anksiyete bozukluğunda psikodinamik anlayışı, mizaç ve bağlanma araştırmalarını ve panik odaklı psikodinamik "
                 "terapiye dair kanıtı tartışır."),
        okurken=[
            "Kaygının katmanları (dağılma, sevilen kişinin kaybı, sevginin kaybı, cezalandırılma) klinikte nasıl ayırt edilebilir?",
            "Panik atağı “sebepsiz” görünen hastada hangi sorular sorulmalı?",
            "Mizaç ile ebeveynlik nasıl birlikte çalışır?",
        ],
        fikirler=[
            ("Kaygı katmanlıdır", "Aynı yüzeysel korku altta farklı düzeylerde kayıp korkusu taşıyabilir: kendiliğin dağılması, sevilen "
             "kişinin kaybı, sevginin kaybı ya da vicdanın cezası."),
            ("Kaygı aynı zamanda bir sinyaldir", "Kaygıyı tümüyle ortadan kaldırmak yerine onu hissedip onunla düşünebilme kapasitesini "
             "artırmak da bir tedavi hedefidir."),
            ("Panik “sebepsiz” değil, sorulmamıştır", "Atağın tam zamanlaması ve bağlamı ayrıntılı sorulduğunda çoğu zaman bir ilişkideki "
             "öfke, ayrılık ya da bağımlılık çatışmasıyla bağlantı bulunur."),
            ("Mizaç bir başlangıç noktasıdır", "Yabancıya karşı çekingen mizaç kaygı bozuklukları için risk oluşturur; ancak bakım verenin "
             "bu mizaca nasıl yanıt verdiği gidişi belirler."),
            ("Fobi ve aile dengesi", "Okul reddi ve evden çıkamama kimi zaman aile içindeki bir ilişkiyi koruyan bir düzenlemedir; tedavi "
             "yalnızca çocuğu değil sistemi de hedeflemelidir."),
            ("Herkese aynı reçete değil", "Bazı hastalar belirti odaklı kısa yaklaşımlardan, bazıları anlam arayan çalışmadan daha çok "
             "yararlanır; hastanın ne istediğini sormak uyumu öngörür."),
        ],
        crs=[
            "“Neden kaygılı olduğumu bilmiyorum” diyen çocuk yalan söylemiyor; kaygı sinyali farkındalık dışında çalışabilir.",
            "Panik atak yaşayan ergende üç soru sorun: atak tam olarak ne zaman ve nerede oluyor, o anda neye ya da kime gidiyor, o ilişkide daha önce bir çatışma oldu mu?",
            "Panik bozukluğu olan ergende istismar öyküsünü sormak rutin bir ayrıntı değil, özellikle gerekli bir sorudur.",
            "Panik atağı yaşayan çocuğa ve aileye beynin alarm sisteminin düşünme sisteminden önce devreye girdiğini anlatmak utancı ve korkuyu azaltır.",
            "Çekingen mizaçlı çocukta ebeveyn danışmanlığının hedefi eleştiri ve utandırmayı azaltmak, korkuyu küçümsemeden kademeli cesaretlendirmektir.",
            "Okul reddinde “çocuk evde kaldığında ailede kim rahatlıyor?” sorusunu sorun.",
            "Sürekli beden şikâyetleriyle gelen kaygılı ergende sabırsızlanıp “asıl mesele bu değil” demeyin; örüntü tekrarlandıkça asıl konu görünür hâle gelir.",
            "İlaç önermeden önce “Bununla ne çözülsün istiyorsun?” diye sorun; yanıt önerinin kabul görüp görmeyeceğini önceden söyler.",
        ],
        tartisma=[
            ("Panik odaklı psikodinamik terapi",
             "Erişkin panik bozukluğunda panik odaklı psikodinamik terapi gevşeme eğitimine göre daha yüksek yanıt oranı gösterdi (%73’e "
             "karşı %39; [@milrod2007]). İki merkezli daha büyük bir çalışmada ise bilişsel davranışçı terapi merkezler arasında en "
             "tutarlı sonucu verdi; psikodinamik terapi bir merkezde onunla benzerdi ([@milrod2016]). Her iki çalışma da erişkinlerde "
             "yapıldı."),
            ("Ayrılık kaygısı ve panik",
             "Çocuklukta ayrılık kaygısı bozukluğu ileride panik bozukluğu gelişme olasılığını yaklaşık 3,5 kat artırır; ancak ilişki özgül değildir, "
             "başka kaygı bozukluklarının riski de artar ([@kossowsky2013])."),
            ("Çekingen mizaç ve ebeveynlik",
             "Davranışsal ketlenme sosyal kaygı bozukluğu gelişme olasılığını yaklaşık 7,6 kat artırır ([@clauss2012]). Algılanan aşırı koruma ve "
             "ret de sosyal fobiyle ilişkili bulunmuştur, ancak bu ilişkiler mütevazıdır ([@lieb2000])."),
            ("Birinci basamak tedavi",
             "Çocuk ve ergen kaygı bozukluklarında en güçlü kanıt bilişsel davranışçı terapi, sertralin ve ikisinin birleşimi içindir "
             "([@walkup2008]). Dinamik anlayış bu tedavilerin yerine değil, uyumu ve anlamı güçlendiren bir çerçeve olarak düşünülebilir."),
        ],
        sorular=[
            S("Panik atakları olan 15 yaşındaki bir kız atakların “hiç sebepsiz” geldiğini söylüyor. Ayrıntılı sorulduğunda çoğunun "
              "babasının iş seyahatinden döndüğü akşamlarda başladığı anlaşılıyor. En uygun sonraki adım hangisidir?",
              ["Atakların sebepsiz olduğunu kabul edip yalnızca nefes egzersizi öğretmek",
               "Babayla ilişkiyi ve o akşamlarda evde neler olduğunu merakla araştırmak", "Hemen aile terapisine yönlendirmek",
               "Kardiyolojik tetkik istemek"],
              1, "Panik atakların “sebepsiz” görünmesi çoğu zaman bağlamın sorulmamış olmasındandır. Zamanlamadaki örüntü bir ilişkideki "
                 "çatışmaya işaret edebilir. Bu araştırma, kanıta dayalı tedavilerle birlikte yürütülebilir."),
            S("Davranışsal ketlenmesi belirgin 5 yaşındaki bir çocuğun ebeveynine verilebilecek en uygun öneri hangisidir?",
              ["“Onu korkutan her ortamdan uzak tutun.”", "“Utangaçlığı için uyarın, böylece daha cesur olur.”",
               "“Korkusunu küçümsemeden adlandırın; onu yeni durumlara kademeli ve destekli biçimde yaklaştırın.”",
               "“Büyüyünce geçer, bir şey yapmanıza gerek yok.”"],
              2, "Mizaç kader değildir; aşırı koruma da utandırma da kaygıyı besleyebilir. Duyarlı ve kademeli cesaretlendirme, çekingen "
                 "mizaçlı çocukta kaygı bozukluğu riskini azaltmayı hedefler."),
            S("Okul reddi olan 10 yaşındaki bir erkeğin annesi kronik ağrı nedeniyle evde yalnız kalmaktan çok korktuğunu söylüyor. "
              "Çocuk sabahları karın ağrısı yaşıyor. En kapsamlı yaklaşım hangisidir?",
              ["Yalnızca okula dönüş için kademeli maruz bırakma planı yapmak",
               "Çocuğun kaygısını ve annenin yalnız kalma kaygısını birlikte ele alan, aileyi içeren bir plan yapmak",
               "Önce karın ağrısı tetkiklerini tamamlayıp sonra düşünmek", "Evde eğitime geçmek"],
              1, "Okul reddi aile içindeki bir dengenin parçası olabilir: çocuk evde kaldıkça annenin kaygısı da yatışıyor olabilir. "
                 "Yalnızca çocuğu hedefleyen plan bu dengeyi görmezden geldiği için tıkanabilir. Organik nedenler dışlanmalıdır, ancak "
                 "tedavi bunu beklemeden planlanabilir."),
        ],
        akilda="“Sebepsiz” panik çoğu zaman sorulmamış bir hikâyedir.",
    ),
    # ------------------------------------------------------------------ 10
    dict(
        no=10, kisim=2, kisa="Travma ve dissosiyasyon",
        baslik="Travma ve stresörle ilişkili bozukluklar, dissosiyatif bozukluklar",
        slogan="Travmanın şiddeti kadar anlamı ve sonrasında yanınızda kimin olduğu da belirleyicidir.",
        kitapta=("Bölüm, travma sonrası stres bozukluğunun kimde gelişeceğini belirleyen etkenleri, dissosiyasyonun gelişimsel "
                 "kökenlerini, kendini suçlama ve yeniden mağduriyet örüntülerini, evreli tedaviyi, belleğin yeniden kurulan "
                 "doğasını ve travmatize hastayla çalışırken ortaya çıkan karşı aktarım rollerini tartışır."),
        okurken=[
            "Yazar travmanın nesnel şiddeti ile öznel anlamı arasındaki ilişkiyi nasıl kuruyor?",
            "Belleği bir kayıt değil yeniden kurulan bir süreç olarak görmenin klinik sonuçları nelerdir?",
            "Terapistin tarihî gerçeğin hakemi olmaması ne anlama geliyor ve adli değerlendirmeden nasıl ayrılıyor?",
        ],
        fikirler=[
            ("Travma yaygın, TSSB değil", "Çoğu insan hayatı boyunca travmatik bir olay yaşar ama küçük bir kısmında TSSB gelişir. "
             "Önceden var olan kaygı ve depresyon, algılanan destek ve olayın kişisel anlamı gidişi belirler."),
            ("Hız ayarı", "Travma çalışmasında hasta ne aşırı uyarılmalı ne de duyguyla teması tümüyle kesilmelidir; tedavi bu iki uç "
             "arasındaki pencerede ilerler. Dissosiye olan hastada maruz bırakmadan önce dengeleme gelir."),
            ("Dissosiyasyon gelişimsel bir yörüngedir", "Kaçamayan ve savaşamayan bir bebeğin tek seçeneği “orada olmamak”tır. "
             "Dezorganize bağlanma, sonraki travmalar ve yatıştırıcı bir erişkinin yokluğu birleştiğinde dissosiyatif bir örgütlenme "
             "gelişebilir."),
            ("Kendini suçlama bir anlamlandırmadır", "“Kötü olduğum için oldu” inancı, çocuğun bakım verenine dair inancını ve bir miktar "
             "kontrol duygusunu korur; bu inancı hızla yıkmaya çalışmak çocuğu daha da çaresiz bırakabilir."),
            ("Bellek bir kayıt değildir", "Anılar her hatırlamada yeniden kurulur. Terapistin işi geçmişi kazıp çıkarmak değil, hastanın "
             "bugün geçmişle nasıl yaşadığını anlamaktır."),
            ("Dört rollü bir sahne", "Kurban, fail, kurtarıcı ve ilgisiz tanık rolleri tedavide yeniden sahnelenir; kurtarıcı rolüne "
             "giren klinisyen tükendiğinde fail konumuna kayabilir."),
        ],
        crs=[
            "Afet ve kayıp sonrası taramada öncelik, travmadan önce zaten kaygılı ya da depresif olan çocuklara verilmelidir; deprem sonrası hizmet planlamasında kullanılabilecek bir ölçüttür.",
            "Orantısız görünen bir tepkide “Ne oldu?” kadar “Bu olay sana neyi hatırlattı?” diye sorun.",
            "Donup kalan, boş bakan, travmayı anlatırken hiçbir şey hissetmiyor görünen çocuk iyi gitmiyor olabilir; dissosiye oluyor olabilir.",
            "Okul öncesi dönemde yaşanan travma anlatılmaz, oynanır; bu çocukların öyküsü oyunda, bedende ve sizinle kurdukları ilişkide görünür.",
            "“Neden söylemedin?” ya da “anlat bakalım” baskısı travmatize çocukta isteksizliği değil dil kapasitesinin sınırını zorlar.",
            "“Bu senin suçun değil” doğru bir cümledir; ama erken ve ısrarla söylendiğinde çocuğun tek kontrol duygusunu yıkabilir. Önce kendini suçlamanın neyi koruduğunu anlayın.",
            "Size bakım vermeye çalışan (yorgun olup olmadığınızı soran, sizi üzecek şeyleri anlatmayan) çocuk kibar değil, ebeveynleşmiş olabilir.",
            "İstismara uğramış çocuğa olayı defalarca anlattırmak iyileştirici değildir; adli süreçte tek görüşme ilkesinin klinik gerekçesi de budur.",
            "Seansta uyuşuyor, saate bakıyor ya da sevk etmeyi düşünüyorsanız, koruyucu olmayan ebeveynin duygusu size aktarılıyor olabilir; bunu süpervizyonda konuşun.",
        ],
        tartisma=[
            ("Çocuk TSSB’sinde kanıt",
             "Travmaya maruz kalan çocuk ve ergenlerde psikolojik tedavilerin TSSB’yi önlemede ve belirtileri azaltmada etkili olabileceğine "
             "dair kanıt var; ancak çalışmaların kalitesi sınırlı ve heterojenlik yüksek ([@gillies2016]). Çocuk TSSB’sine özgü "
             "psikodinamik terapi çalışmaları az sayıdadır; dinamik çerçeve ittifak, hız ayarı ve karşı aktarım için tamamlayıcı değer taşır."),
            ("Dissosiyasyonun kökeni",
             "Travma modelini savunanlar travma ile dissosiyasyon arasındaki ilişkinin tutarlı ve fantezi yatkınlığından bağımsız "
             "olduğunu öne sürer ([@dalenberg2012]); eleştirmenler ise nedensellik çıkarımlarının erken olduğunu, telkinin ve sahte "
             "anıların rolünün küçümsendiğini savunur ([@lynn2014]). Tartışma çözülmüş değildir."),
            ("Çocuklar ve telkin",
             "Telkine açıklık yaşla belirgin biçimde azalır; yine de küçük çocuklar adli açıdan önemli pek çok bilgiyi doğru "
             "hatırlayabilir ([@ceci1993]). Bu, terapide yönlendirici sorulardan kaçınmayı ve adli görüşmeyi bu konuda uzmanlaşmış "
             "ekiplere bırakmayı gerektirir."),
            ("Erken bakımın ağırlığı",
             "Boylamsal bir çalışmada dezorganize ve kaçıngan bağlanma sonraki dissosiyasyonu yordadı ([@ogawa1997]); bir başka "
             "çalışmada genç erişkinlikteki dissosiyasyonu bebeklikte gözlenen ebeveyn duyarsızlığı anlamlı biçimde yordadı; travma "
             "türlerinden yalnızca sözel istismar buna katkı ekledi ([@dutra2009])."),
        ],
        sorular=[
            S("Hafif yaralandığı bir trafik kazasından sonra 9 yaşındaki bir kız arabaya binemiyor ve her gece kâbus görüyor. Kazada "
              "kimse ağır yaralanmamış. Aile “bu kadar küçük bir olaydan neden bu kadar etkilendi?” diye soruyor. En uygun klinik soru "
              "hangisidir?",
              ["“Kaza ne kadar hızlıydı?”", "“Bu kaza ona daha önce yaşadığı bir şeyi hatırlatmış olabilir mi?”",
               "“Kâbuslar ne kadar sürüyor?”", "“Arabaya binmek istemeyince ne yapıyorsunuz?”"],
              1, "TSSB’yi yordayan, olayın şiddetinden çok anlamı ve önceki deneyimlerle bağlantısıdır. Bu soru, daha önceki bir kayıp "
                 "ya da korku yaşantısının kazayla uyanıp uyanmadığını araştırır; diğer sorular bilgi verir ama orantısızlığı açıklamaz."),
            S("Cinsel istismara uğradığı belirlenen 12 yaşındaki bir erkek terapide sürekli “benim yüzümden oldu, karşı koymadım” diyor. "
              "En uygun yaklaşım hangisidir?",
              ["Her seansta “senin suçun değil” diye tekrar etmek",
               "Kendini suçlamanın ona neyi sağladığını merakla anlamaya çalışmak; zamanla sorumluluğun failde olduğunu birlikte düşünmek",
               "Konuyu açmamak; suçluluk kendiliğinden geçer", "Neden karşı koymadığını ayrıntılı sorgulamak"],
              1, "Kendini suçlama kontrol duygusunu ve bağlandığı figürlere dair inancı koruyan bir anlamlandırma olabilir. Önce bu "
                 "işlevi anlamak, sonra sorumluluğun failde olduğunu birlikte düşünmek daha kalıcı değişim sağlar. Sorgulamak utancı "
                 "derinleştirir."),
            S("İstismar şüphesiyle görülen 4 yaşındaki bir çocuk oyunda bir bebek figürüne tekrar tekrar ceza veriyor. Terapistin en "
              "uygun tutumu hangisidir?",
              ["Oyunu istismarın kanıtı olarak rapora yazmak", "Çocuğa “sana da böyle mi yapıldı?” diye sormak",
               "Oyunu izleyip duyguları oyun içinde adlandırmak; adli değerlendirmeyi uzmanlaşmış ekibe bırakmak",
               "Oyunu durdurup başka bir etkinliğe geçmek"],
              2, "Okul öncesi çocuklar yaşadıklarını oyunla ifade eder; ancak oyun tek başına adli kanıt değildir ve yönlendirici sorular "
                 "telkin riski taşır ([@ceci1993]). Terapist tarihî gerçeğin hakemi değildir; koruma gereken durumda yasal bildirim "
                 "yükümlülüğü ayrıca yerine getirilir."),
        ],
        akilda="“Ne oldu?” kadar “sana neyi hatırlattı?” diye sorun; terapist tarihin hakemi değildir.",
    ),
    # ------------------------------------------------------------------ 12
    dict(
        no=12, kisim=2, kisa="Madde ve yeme",
        baslik="Madde ile ilişkili ve bağımlılık bozuklukları, yeme bozuklukları",
        slogan="“Ne kullanıyorsun?” değil, “kullandığında ne duruyor?”",
        kitapta=("Bölüm iki alanı ele alır: madde kullanım bozukluklarında ahlaki model, hastalık modeli ve kendi kendini tedavi etme "
                 "modeli, öz-bakım ve duygulanım düzenleme güçlükleri; anoreksiya ve bulimiyada beden, kontrol, özerklik ve aile "
                 "dinamikleri ile aile temelli yaklaşımlar."),
        okurken=[
            "Üç bağımlılık modelinin her birinin klinik bedeli nedir?",
            "Yeme bozukluğunda kontrol ve özerklik temaları ergenliğin gelişimsel göreviyle nasıl ilişkilendiriliyor?",
            "Açlığın kendisinin psikolojik belirtiler üretmesi değerlendirmeyi nasıl etkiler?",
        ],
        fikirler=[
            ("Madde bir işlev görür", "Madde seçimi rastgele olmayabilir; kişinin en zor taşıdığı duyguyu (öfke, kaygı, boşluk) yatıştırma "
             "işleviyle ilişkili olabilir."),
            ("Öz-bakımda eksiklik", "Bağımlılık kendini yıkma isteğinden çok, kendine bakma ve tehlikeyi öngörme kapasitesindeki bir "
             "eksiklik olarak düşünülebilir."),
            ("Sert vicdandan kaçış", "Başarının ardından gelen nüks, acımasız bir iç eleştirmenin maddeyle susturulma girişimi olabilir."),
            ("Belirti tanıyı, kişilik tedaviyi belirler", "Aynı yeme bozukluğu belirtileri kişilik örgütlenmesi çok farklı ergenlerde "
             "görülebilir; prognoz ve tedavi buna göre değişir."),
            ("Açlık kişiliği taklit eder", "Ağır kısıtlama obsesyonlar, katılık ve sosyal geri çekilme üretir; kişilik ya da OKB "
             "değerlendirmesi kilo restorasyonundan sonra yapılmalıdır."),
            ("Aile hem kaynak hem müttefik", "Ergen anoreksiyasında aile temelli tedavi önemli bir seçenektir; aile sistemini görmezden "
             "gelen tedavi aile tarafından farkında olmadan engellenebilir."),
        ],
        crs=[
            "Ergen madde kullanımında ne “kötü çocuk” ne “elinde değil” çerçevesi yeterlidir; “bu madde bu çocukta hangi işi görüyor?” diye sorun.",
            "Ebeveyn kaybından sonraki ikinci yıl, aile “artık atlattı” diye rahatladığında risk penceresi açılabilir; izlemi bir yılla sınırlamayın.",
            "Duygu düzenleme kapasitesi zayıf ergende sert yüzleştirme içgörü değil kaçınma üretir; motive edici, yargılamayan bir tutum benimseyin.",
            "Madde kullanan ergende kurumlar arası koordinasyon (bağımlılık merkezi, okul, aile, adli süreç) idari bir iş değil, tedavinin kendisidir.",
            "“Mükemmel çocuk birdenbire değişti” anlatısında ergenlikteki inatçılık bozulmadan çok ilk özerklik girişimi olabilir.",
            "Yemeyi siz kovaladığınız sürece arzuyu hasta adına siz taşırsınız; kilo hedeflerini ekip ve aileyle paylaşın, tek başına savaşa girmeyin.",
            "Kusursuz görünen, “biz çok uyumlu bir aileyiz” diyen ailede tek “sorunlu” ergen, ailenin taşımadığı yükü taşıyor olabilir.",
            "Servisteki kontrol savaşı tedavinin bozulması değil aile dinamiğinin sahneye taşınmasıdır; doğru okunursa tanısal bir fırsattır.",
        ],
        tartisma=[
            ("Kendi kendini tedavi hipotezi",
             "Maddenin acı veren duyguları yatıştırmak için kullanıldığı fikri ([@khantzian1985]) şefkatli bir klinik çerçeve sunar; "
             "ancak ampirik desteği zayıftır ve “altta yatan bozukluk tedavi edilince bağımlılık düzelir” beklentisi madde kullanım "
             "bozukluğunun gözden kaçmasına yol açabilir ([@lembke2012])."),
            ("Yüzleştirme",
             "Sorunlu alkol kullanıcılarında yapılan bir çalışmada terapist yüzleştirdikçe danışan direnci arttı ve bir yıl sonraki içki "
             "tüketimi yükseldi ([@miller1993]). Bulgu erişkin bir örneklemden gelir, ama ergen kliniği için de güçlü bir uyarıdır."),
            ("Aile temelli tedavinin zamanlaması",
             "Ergen anoreksiyasında aile temelli tedavi tedavi sonunda bireysel tedaviden üstün değildi, ancak 6–12 aylık izlemde tam "
             "remisyon açısından üstündü ([@lock2010]; [@couturier2013])."),
            ("Açlığın psikolojisi",
             "Gönüllülerde yapılan klasik açlık deneyi, kısıtlamanın tek başına obsesyonlar, irritabilite ve sosyal geri çekilme "
             "üretebildiğini göstermiştir ([@keys1950])."),
        ],
        sorular=[
            S("On altı yaşındaki bir erkek babasının ölümünden bu yana esrar kullanıyor. “Kullanınca kafamdaki ses kısılıyor, öfkem "
              "geçiyor” diyor. En uygun ilk klinik soru hangisidir?",
              ["“Ne kadar sık kullanıyorsun?”", "“Kullandığında içinde ne duruyor, ne sakinleşiyor?”", "“Bunu kimden alıyorsun?”",
               "“Bırakmazsan ailene söylemek zorunda kalırım.”"],
              1, "Maddenin gördüğü işlevi anlamak hem formülasyon hem müdahale için yol gösterir; bu ergende öfke ve yasla baş etme "
                 "işlevi öne çıkıyor. Sıklık da sorulmalıdır; ancak tehdit ittifakı bozar."),
            S("Anoreksiya nervoza tanılı 15 yaşındaki bir kızda belirgin kilo kaybı sürerken obsesyonlar, katılık ve sosyal geri çekilme "
              "gözleniyor. Ekipten biri kişilik bozukluğu ve OKB tanılarını eklemeyi öneriyor. En doğru yaklaşım hangisidir?",
              ["Belirtiler belirgin olduğu için tanıları hemen koymak",
               "Belirtilerin açlıkla ilişkili olabileceğini göz önünde tutup kilo restorasyonu sonrası yeniden değerlendirmek",
               "OKB için hemen yüksek doz SSRI başlamak", "Belirtileri yeme bozukluğunun parçası sayıp hiç değerlendirmemek"],
              1, "Açlık kişiliği taklit eder; kısıtlama sürerken konan kişilik ya da OKB tanıları yanıltıcı olabilir. Belirtiler izlenir, "
                 "kalıcı tanılar kilo restorasyonundan sonra yeniden değerlendirilir."),
            S("Ergen anoreksiyasında aile temelli tedaviyle ilgili hangisi doğrudur?",
              ["Tedavi sonunda bireysel terapiden açıkça üstündür",
               "Tedavi sonunda benzerdir, ancak 6–12 aylık izlemde tam remisyon açısından üstün bulunmuştur",
               "Aileyi hastalığın nedeni olarak ele alır", "Yalnızca erişkinlerde çalışılmıştır"],
              1, "Randomize çalışmalarda aile temelli tedavinin üstünlüğü izlem döneminde belirginleşti ([@lock2010]; [@couturier2013]). "
                 "Bu yaklaşım aileyi suçlamaz; ebeveynleri iyileşmenin kaynağı olarak konumlandırır."),
        ],
        akilda="Yemeği kovalamayın; açlıkta kişilik tanısı koymayın.",
    ),
    # ------------------------------------------------------------------ 13
    dict(
        no=13, kisim=2, kisa="Nörogelişim",
        baslik="Nörogelişimsel ve nörobilişsel bozukluklar",
        slogan="Organik olan anlamsız değildir.",
        kitapta=("Bölüm kapsamlı olmayı hedeflemediğini belirterek otizm spektrum bozukluğu ve edinilmiş beyin hasarı gibi durumlarda "
                 "da kişinin bir iç dünyası, savunmaları ve benlik saygısı olduğunu vurgular; ailelerle çalışmayı ve klinisyenin "
                 "karşı aktarımlarını ele alır."),
        okurken=[
            "“Organik” ve “işlevsel” ayrımının neden yanıltıcı olduğu nasıl temellendiriliyor?",
            "Otizmde içgörü yerine mentalizasyondan söz etmek ne kazandırıyor?",
            "Ailenin davranışı ne zaman bir neden, ne zaman bir yanıt olarak okunmalı?",
        ],
        fikirler=[
            ("Organik olan anlamsız değildir", "Beyin farklı çalışsa da kişinin bir öyküsü, savunmaları ve benlik saygısı vardır; dinamik "
             "anlayışı “nasılsa organik” diye devretmek hastaya değil klinisyene kolaylık sağlar."),
            ("Neden ile yanıtı karıştırmayın", "Ebeveynin mesafesi ya da tükenmişliği çoğu zaman çocuğun farklılığına verilen bir yanıttır. "
             "Bu ayrım, alanın geçmişteki “buzdolabı anne” hatasının tekrarlanmasını önler."),
            ("Öngörülebilirlik güvenliktir", "Otizmli çocuğun rutine bağlılığı, karmaşık bir sosyal dünyada öngörülebilirlik arayan bir "
             "güvenlik stratejisi olarak anlaşılabilir."),
            ("Mentalizasyon öğretilebilir", "Örtük, sezgisel zihin okuma yolu kapalı olsa bile açık, bilinçli bir yol öğrenilebilir; bu "
             "yol yorucudur ve doğal görünmeyebilir."),
            ("Yıkım tepkisi", "Kapasitesinin üstündeki bir görevle karşılaşan kişi bunu bir zorlanma değil varoluşuna yönelik bir tehdit "
             "olarak yaşayabilir; öfke nöbetleri bu açıdan okunmalıdır."),
            ("Aile müdahalenin merkezindedir", "Ebeveynlerle çalışmak yan hizmet değil, çoğu zaman tercih edilecek tedavidir."),
        ],
        crs=[
            "Rutini bozmak çocuğun öngörülebilir tek dünyasını elinden almaktır; değişiklikleri önceden, görsel ve somut biçimde hazırlayın.",
            "Yoğun ilgi alanı (trenler, bayraklar, asansörler) söndürülecek bir davranış değil, çocuğun size açtığı kapıdır.",
            "Spektrumdaki ergenin “ben herkesten zekiyim, onlar aptal” söylemi çoğu zaman anlaşılamayan bir dünyada ayakta kalma aracıdır; yıkmak yerine altındaki kırılganlığı yavaş yavaş konuşulabilir kılın.",
            "Öfke nöbetinde çocuk “yapamadım” değil “dağılıyorum” yaşıyor olabilir; görevi kaldırmayın, parçalayın ve yapabildiği parçayı ona bırakın.",
            "“Kabullenmiyorlar” diye etiketlenen ebeveyn çoğu zaman parça parça yas tutuyordur; bu süreç hızlandırılamaz.",
            "Annedeki kaygı, mesafe ya da tükenmişliği gördüğünüzde bunun neden değil sonuç olma olasılığını önce değerlendirin.",
            "Kendi doğrulanma ihtiyacınızı hastadan bekliyorsanız bu grupla uzun süre çalışmak zorlaşır; kenarda kalma duygusu tablonun parçasıdır.",
        ],
        tartisma=[
            ("Ebeveyn aracılı müdahalenin uzun dönem etkisi",
             "Okul öncesi otizmli çocuklarda ebeveyn aracılı sosyal iletişim müdahalesi, yaklaşık altı yıl sonraki izlemde belirti "
             "şiddetinde azalmayla ilişkili bulundu ([@pickles2016]). Bu, ebeveyni bir neden değil değişimin ortağı olarak konumlandırır."),
            ("Nöroçeşitlilik bakışı",
             "Otizm araştırmalarında eksiklik odaklı tıbbi modelin yanına ya da yerine nöroçeşitlilik paradigmasını koyma çağrıları "
             "güçleniyor ([@pellicano2022]). “Narsisistik kırılganlık” gibi dinamik kavramların otistik bireylerin kendi deneyim "
             "anlatımlarıyla birlikte sınanması gerekir."),
            ("Tanı eşiği",
             "ABD’de 8 yaşındaki çocuklarda otizm yaygınlığı 2022 verisiyle 31 çocukta 1’e ulaştı ([@shaw2025]). Bu artışın önemli bir "
             "kısmı tanı ölçütleri, farkındalık ve hizmete erişimle ilişkilidir; spektrumun hafif ucunda tanı kararı klinisyenin "
             "eşiğine duyarlıdır."),
        ],
        sorular=[
            S("Otizm spektrum bozukluğu olan 8 yaşındaki bir erkek okulda beklenmedik bir program değişikliğinden sonra ağlama ve vurma "
              "nöbeti geçiriyor. Öğretmen “şımarıklık” diyor. En uygun açıklama hangisidir?",
              ["Davranış bilinçli bir manipülasyondur",
               "Öngörülebilirliğin aniden bozulması çocuk için yoğun bir tehdit ve dağılma deneyimi yaratmış olabilir",
               "Dikkat eksikliği tanısı atlanmıştır", "Ebeveynin aşırı hoşgörüsünün sonucudur"],
              1, "Otizmli çocuk için rutin bir güvenlik stratejisidir; ani değişiklik yıkım tepkisine yol açabilir. Değişiklikleri önceden "
                 "ve görsel olarak hazırlamak bu nöbetleri azaltır."),
            S("Otizmli 4 yaşındaki bir çocuğun annesi yorgun, mesafeli ve çökkün görünüyor. Bir stajyer “annenin soğukluğu çocuğun "
              "iletişimini bozmuş olabilir” diyor. En doğru yanıt hangisidir?",
              ["Stajyer haklıdır; annenin tutumu otizme yol açmış olabilir",
               "Annenin hâli büyük olasılıkla çocuğun farklılığına ve bakım yüküne verilen bir yanıttır; annenin desteklenmesi tedavinin parçasıdır",
               "Annenin depresyonu çocuğun tanısını geçersiz kılar", "Anne bireysel terapiye yönlendirilmeli, çocuk yalnızca izlenmelidir"],
              1, "“Buzdolabı anne” kuramı çürütülmüştür. Yanıt vermeyen bir çocukla kurulan etkileşim en sağlam ebeveyni de zorlar; "
                 "annedeki tükenmişlik çoğu zaman sonuçtur. Annenin desteklenmesi ve ebeveyn aracılı müdahaleler hem anne hem çocuk için "
                 "yararlıdır."),
            S("Zihinsel yetersizliği olan 13 yaşındaki bir kız ev işlerinden birini yapamayınca öfke nöbeti geçiriyor ve aile artık ona "
              "hiçbir iş vermiyor. En uygun öneri hangisidir?",
              ["Ailenin kararını desteklemek; kız korunmalıdır", "Görevi küçük adımlara bölüp kızın yapabildiği kısmı ona bırakmak",
               "Öfke nöbetleri için antipsikotik başlamak", "Görevi yapmadığında ceza vermek"],
              1, "Görevi tümüyle kaldırmak korumak değil, benlik saygısını aşındırmaktır. Görevi parçalara ayırıp başarılabilir kısmı "
                 "bırakmak hem yıkım tepkisini önler hem yetkinlik duygusunu destekler."),
        ],
        akilda="Neden ile yanıtı karıştırmayın; görevi kaldırmayın, parçalayın.",
    ),
    # ------------------------------------------------------------------ 15
    dict(
        no=15, kisim=2, kisa="Borderline",
        baslik="B kümesi kişilik bozuklukları: borderline",
        slogan="Aynı istismar, zihni merak eden bir erişkinin varlığında başka bir yol çizebilir.",
        kitapta=("Kitabın en kapsamlı bölümlerinden biri olan bu bölüm, borderline kişilik bozukluğunun seyrini, etiyolojik modelleri, "
                 "mentalizasyon araştırmalarını, nörobiyolojik bulguları ve farklı psikoterapi yaklaşımlarının ortak tekniklerini "
                 "tartışır; servis, aile ve grup tedavisini ele alır."),
        okurken=[
            "Erken etiyolojik modeller neden terk edildi; yerine hangi gelişimsel model önerildi?",
            "Mentalizasyon ve “yabancı kendilik” kavramları kendine zarar vermeyi anlamaya nasıl yardım ediyor?",
            "Farklı terapilerin benzer sonuç vermesi neyi düşündürüyor?",
        ],
        fikirler=[
            ("Kötü prognoz efsanesi", "Uzun izlem çalışmaları belirtilerin çoğu hastada gerilediğini gösterir; iş ve ilişki alanında "
             "iyileşme ise daha zordur. Hedef yalnızca kesmenin durması değil, bir hayatın kurulmasıdır."),
            ("Bir yörünge, bir tanı değil", "Aşırı duyarlı mizaç, bu mizaçla yorulan ya da onu geçersizleştiren bir bakım ortamı, "
             "dezorganize bağlanma ve travmatik ilişkiler bir zincir oluşturabilir; her halka bir müdahale noktasıdır."),
            ("Mentalizasyon koruyucudur", "İstismar öyküsü olanlarda yansıtıcı işlevin korunmuş olması ağır kişilik patolojisi olasılığını "
             "belirgin biçimde azaltır. Travmanın kendisi değişmez; çevresinde ne yapılabildiği değişir."),
            ("Yabancı kendilik", "İçselleştirilmiş, kişiye ait olmayan zalim bir parça dışarıda bir taşıyıcı arar; istismarcı ilişkileri "
             "tekrar tekrar bulmak bu açıdan anlaşılabilir."),
            ("Algıda değil yorumda", "Bu hastalar yüz ifadelerini çoğu zaman iyi okur; ama belirsiz ifadeleri olumsuz yorumlamaya "
             "eğilimlidir."),
            ("Ortak teknikler", "Farklı terapi okulları benzer sonuç verir; ortak noktaları yapı, tutarlılık, duygulanıma odak, "
             "mentalizasyonu destekleme ve klinisyenin kendi tepkilerini düzenlemesidir."),
        ],
        crs=[
            "Aile değerlendirmesinde babanın yokluğu, annenin varlığının niteliği kadar veri toplamayı hak eder.",
            "“Borderline-öncesi çocuk” bir tanı değil bir yörünge tanımıdır; aşırı duyarlı mizaçlı çocuğun ebeveynini desteklemek erken bir önleme adımıdır.",
            "Travma sonrası müdahalenin hedeflerinden biri, çocuğun hayatında onun zihnini merak eden ve ona kendi zihnini merak etmeyi öğreten bir erişkin bulunmasını sağlamaktır.",
            "Nötr yüzünüz bu ergen için düşmanca okunabilir; sıkıldığınızı siz fark etmeden o fark edebilir. Duygu durumunuzu kısa ve dürüstçe adlandırmak yanlış okumayı azaltır.",
            "“Dikkat çekiyor” ya da “manipülatif” etiketleri yerine kendine zarar vermeyi dayanılmaz bir duyguyu yatıştırma girişimi olarak anlamaya çalışın.",
            "Ergenin sizi kötü bir figüre dönüştürme çabası, siz direndikçe artabilir; kapsayın ama kaybolmayın. “Başkasına devredeyim” refleksini süpervizyonda sınayın.",
            "Ergen artık kesmiyor, okula gidiyor, bir arkadaş edinmişse, seansta hâlâ “yüzeysel” konuşması başarısızlık değildir.",
            "Ergenin anlatısının duygusal gerçekliğini doğrulayın, olgusal kesinliğini askıda tutun; aileyi suçlamadan ortak edin.",
            "Süpervizörden en çok saklamak istediğiniz duygu, tam da konuşmanız gereken şeydir.",
        ],
        tartisma=[
            ("Ergende borderline tanısı",
             "DSM-5 ve ICD-11 ergenlikte borderline kişilik bozukluğu tanısına izin verir; bu tanının ergenlerde geçerli, güvenilir ve "
             "tedavi edilebilir olduğuna dair kanıt birikmiştir ([@sharp2015]). Damgalanma kaygısı ise erken tanının yararlarıyla "
             "birlikte tartışılmaya devam ediyor."),
            ("Remisyon ve iyileşme",
             "On yıllık izlemde hastaların %93’ü en az iki yıl süren belirti remisyonuna ulaştı; işlevsellikle birlikte tam iyileşme ise "
             "%50’de kaldı ve iyileşenlerin üçte biri bunu sonradan kaybetti ([@zanarini2010])."),
            ("İlaç tedavisi",
             "Güncel bir Cochrane derlemesine göre hiçbir ilacın borderline kişilik bozukluğunun çekirdek patolojisini özgül olarak "
             "düzelttiğine dair inandırıcı kanıt yoktur ([@stoffers2022])."),
            ("Mentalizasyon bulgularının kaynağı",
             "Kitabın bölüme yerleştirdiği merkezi bulgu, bağlanma ve yansıtıcı işlevi psikiyatrik tabloyla ilişkilendiren erken bir "
             "çalışmaya dayanır ([@fonagy1996]). Ergenlerde mentalizasyon temelli tedavi kendine zarar vermeyi ve depresyonu azalttı "
             "([@rossouw2012]); ancak bu 80 ergenle yapılmış görece küçük bir çalışmadır."),
            ("Biyolojik hipotezler",
             "Opioid sistemi hipotezi ilgi çekici ama büyük ölçüde kuramsaldır ([@bandelow2010]). Yüz tanıma meta-analizinde en belirgin "
             "güçlük nötr yüzlerin doğru tanınmasındaydı ([@daros2013])."),
        ],
        sorular=[
            S("Kendine zarar veren 16 yaşındaki bir kız terapistinin yüzüne bakıp “Benden sıkıldın, değil mi?” diyor. Terapist o anda "
              "yalnızca yorgun. Mentalizasyon temelli bir yanıt hangisidir?",
              ["“Hayır, sıkılmadım; bu senin çarpıtman.”",
               "“Yüzümde bir şey gördün ve bunu sıkılma olarak okudun. Aslında biraz yorgunum. Bu sende nasıl bir duygu uyandırdı?”",
               "“Bu düşünce babanla ilişkini hatırlatıyor olabilir.”", "Soruyu yanıtlamadan konuyu değiştirmek"],
              1, "İkinci seçenek ergenin algısını ciddiye alır, terapistin gerçek durumunu kısaca ve dürüstçe paylaşır ve zihinsel "
                 "durumları merak etmeye davet eder. Birincisi yaşantıyı geçersiz kılar; üçüncüsü bu aşamada erken bir aktarım yorumudur."),
            S("Borderline özellikleri olan 15 yaşındaki bir ergenin ailesi kızlarının anlattıklarının “tamamen yalan” olduğunu söylüyor; "
              "kız ise aileyi “zalim” olarak tanımlıyor. Klinisyenin en uygun tutumu hangisidir?",
              ["Ergenin anlatısını olduğu gibi kabul edip aileyle yüzleşmek", "Aileyi haklı bulup anlatıyı çarpıtma saymak",
               "Anlatının duygusal gerçekliğini doğrulamak, olgusal kesinliği askıda tutmak ve aileyi suçlamadan tedaviye ortak etmek",
               "Aile görüşmelerini tümüyle sonlandırmak"],
              2, "Bir tarafa geçmek bölmeyi besler. Duygusal gerçekliği doğrulamak ittifakı korurken olgusal yargıyı askıda tutmak aileyi "
                 "kaybetmemeyi sağlar. İstismar şüphesi varsa koruma yükümlülükleri ayrıca değerlendirilir."),
            S("Borderline kişilik bozukluğunda ilaç tedavisiyle ilgili hangisi doğrudur?",
              ["Duygudurum dengeleyiciler çekirdek patolojiyi düzeltir", "Antipsikotikler birinci basamak tedavidir",
               "Hiçbir ilacın çekirdek patolojiyi özgül olarak düzelttiğine dair inandırıcı kanıt yoktur; ilaçlar eşlik eden durumlar için düşünülebilir",
               "SSRI’lar kendine zarar vermeyi kesin olarak önler"],
              2, "Güncel kanıt ([@stoffers2022]) psikoterapinin temel tedavi olduğunu, ilaçların ise eşlik eden depresyon gibi durumlar "
                 "için dikkatle kullanılması gerektiğini destekler."),
        ],
        akilda="Kapsayın ama kaybolmayın; iyileşmeyi seansın dışında da arayın.",
    ),
    # ------------------------------------------------------------------ 16
    dict(
        no=16, kisim=2, kisa="Narsisistik",
        baslik="B kümesi kişilik bozuklukları: narsisistik",
        slogan="Gürültülü olanın yanında sessiz, kırılgan bir narsisizm de vardır.",
        kitapta=("Bölüm narsisistik kişilik bozukluğunu kayıtsız ve aşırı tetikte uçları olan bir süreklilik olarak ele alır; Kohut ile "
                 "Kernberg’in yaklaşımlarını karşılaştırır, karşı aktarım örüntülerini, grup terapisinin yerini ve narsisizmin yaşam "
                 "döngüsündeki seyrini tartışır."),
        okurken=[
            "Tanı ölçütleri narsisizmin neden yalnızca bir yüzünü yakalıyor?",
            "Utanç ile suçluluk arasındaki fark tedavinin yönünü nasıl değiştiriyor?",
            "Kohut ve Kernberg’in yaklaşımları farklı hastalara mı uygundur?",
        ],
        fikirler=[
            ("İki uçlu bir süreklilik", "Bir uçta başkalarının tepkilerine kayıtsız, büyüklenmeci kişi; öbür uçta eleştiriye aşırı duyarlı, "
             "utanç dolu ve çekingen kişi vardır. Tanı ölçütleri çoğunlukla ilkini tarif eder."),
            ("Utanç ve suçluluk", "Suçluluk bir eylemin yanlışlığına, utanç kendiliğin kusurlu olduğu hissine işaret eder; utanç çok daha "
             "derin ve gizlenen bir yaradır."),
            ("İki kuram, iki hasta grubu", "Empatik, deneyime yakın yaklaşım kırılgan hastalara; yüzleştirici yaklaşım büyüklenmeci ve "
             "saldırgan hastalara daha uygun olabilir. Hangisinin uyacağı ilk seanslardaki deneme müdahaleleriyle görülür."),
            ("Karşı aktarım bir pusuladır", "Görünmez olma, sıkılma ya da yalnızca dinleyici olarak kullanılma hissi, hastanın kendi "
             "dışlanma deneyiminin klinisyene aktarılması olabilir."),
            ("Sınır da tedavidir", "Sürekli aşağılamaya sınırsız tahammül terapötik değildir; sınır koymak tedavinin sürmesini korur."),
            ("Hayat da değiştirir", "Gerçek başarılar, sağlıklı ilişkiler ve yönetilebilir hayal kırıklıkları terapi dışında da dönüştürücü "
             "olabilir."),
        ],
        crs=[
            "Sınıfta göze batmayan, çekingen, eleştiriye aşırı hassas ergen de narsisistik kırılganlık taşıyabilir; tanı ölçütleri bu tipi kolay kaçırır.",
            "Okulda başarılı, sosyal olarak becerikli “yüksek işlevli” ergen ilk ciddi başarısızlıkta çökebilir; bu dönem intihar riski açısından da izlenmelidir.",
            "Narsisistik patolojiyi tek yönlü ebeveyn suçlamasıyla açıklamayın; hem soğukluk hem abartılı övgü büyüklenmeciliği besleyebilir ve mizaç da denklemin parçasıdır.",
            "İlk görüşmede önceki klinisyenlerin adlarını hatırlamayan ve hepsini toptan değersizleştiren ergen ya da aile tanısal bir ipucu verir.",
            "Sürekli konuşan ama size hiç dönmeyen ergende hissettiğiniz sıkıntı ve dışlanmışlık, onun çocukluk deneyiminin size aktarılması olabilir.",
            "Parlak, karizmatik ergende gösteriyi izleme tuzağına düşmeyin; eleştirel mesafeyi koruyun.",
            "Narsisistik özellikli ergeni gruba doğrudan sokmak yerine önce bireysel ittifak kurun; grupta kolayca günah keçisi olabilir.",
        ],
        tartisma=[
            ("Büyüklenmeci ve kırılgan narsisizm",
             "Klinik kuram, sosyal-kişilik psikolojisi ve psikiyatrik tanı literatürleri büyüklenmeci ve kırılgan olmak üzere iki ana "
             "görünüm üzerinde buluşuyor ([@cain2008]); bu ayrım yazarın kendi önerdiği kayıtsız–aşırı tetikte tipolojisiyle örtüşür "
             "([@gabbard1989]). Klinisyen değerlendirmelerine dayanan bir çalışma ise büyüklenmeci/kötücül, kırılgan ve yüksek işlevli "
             "olmak üzere üç alt tip tanımladı ([@russ2008])."),
            ("Narsisizm yaşla azalır mı?",
             "18 ile 41 yaş arasında izlenen bir kohortta narsisizm ortalama olarak azaldı, ancak bireyler arası sıralama büyük ölçüde "
             "korundu ([@wetzel2020]). Ergenlikteki yüksek narsisistik özellikler kalıcı bir kişilik bozukluğu anlamına gelmez; ama "
             "göreli farklar sürebilir."),
            ("Tedavi kanıtı",
             "Narsisistik kişilik bozukluğuna özgü randomize kontrollü psikoterapi çalışmaları çok azdır; Kohut–Kernberg tartışması büyük "
             "ölçüde klinik gözleme dayanır."),
        ],
        sorular=[
            S("On yedi yaşındaki bir erkek sınıfta neredeyse hiç konuşmuyor, sunum yapacağı günlerde okula gelmiyor. Görüşmede “Herkes "
              "beni izliyor ve yargılıyor; aslında onlardan çok daha derin düşünüyorum ama anlamazlar” diyor. Ayırıcı tanıda mutlaka "
              "düşünülmesi gereken hangisidir?",
              ["Yalnızca sosyal kaygı bozukluğu", "Kırılgan (aşırı tetikte) narsisistik örgütlenme ile sosyal kaygının birlikte değerlendirilmesi",
               "Antisosyal kişilik bozukluğu", "Şizoid kişilik bozukluğu"],
              1, "Gizli bir büyüklenmecilikle birlikte görülen aşırı duyarlılık, utanç ve kaçınma kırılgan narsisizmi düşündürür ve sosyal "
                 "kaygıyla örtüşebilir. Ayrım tedaviyi etkiler: empatik, deneyime yakın bir tutum bu ergenlerde ittifakı kolaylaştırır."),
            S("Narsisistik özellikleri olan 16 yaşındaki bir ergen her seansta hemşireleri ve öğretmenlerini aşağılıyor; terapiste de "
              "“işe yaramaz” diyor. Terapist tükenmiş hissediyor. En uygun yaklaşım hangisidir?",
              ["Her söyleneni sınırsızca kabul etmek; kapsamak budur", "Öfkeyi anlamaya çalışırken aşağılamaya açık ve saygılı bir sınır koymak",
               "Ergeni hemen başka bir terapiste devretmek", "Ergene aynı tonla karşılık vermek"],
              1, "Sınırsız tahammül terapötik değildir ve klinisyenin tükenmesiyle tedavinin kopmasına yol açabilir. Saygılı bir sınır, "
                 "ergenin öfkesini reddetmeden ilişkinin sürmesini sağlar."),
            S("Utanç ile suçluluk ayrımıyla ilgili hangisi doğrudur?",
              ["Utanç bir davranışın yanlışlığına, suçluluk kendiliğin kusurlu olduğu hissine işaret eder",
               "Suçluluk bir eylemin yanlışlığına, utanç kendiliğin kusurlu olduğu hissine işaret eder",
               "İkisi aynı duygunun farklı adlarıdır", "Utanç yalnızca kültürel bir olgudur, klinik önemi yoktur"],
              1, "Suçluluk onarılabilir bir eyleme, utanç ise “ben kusurluyum” hissine bağlıdır. Utanç daha çok gizlenir ve öfkeyle "
                 "savunulabilir; narsisistik kırılganlıkta merkezi bir duygudur."),
        ],
        akilda="Sessiz olan da kırılgan bir büyüklenmecilik taşıyabilir; sınır koymak da tedavidir.",
    ),
    # ------------------------------------------------------------------ 17
    dict(
        no=17, kisim=2, kisa="Antisosyal",
        baslik="B kümesi kişilik bozuklukları: antisosyal",
        slogan="Davranışı ve kişilerarası–duygusal yapıyı ayrı değerlendirin.",
        kitapta=("Bölüm antisosyal kişilik bozukluğunu psikopatiden ayırır ve narsisistik patoloji sürekliliği içinde ele alır; gen–çevre "
                 "etkileşimine, vicdandaki boşluklara, kurumsal tedavinin sınırlarına, karşı aktarım tehlikelerine ve önlemenin önemine "
                 "odaklanır."),
        okurken=[
            "Antisosyal kişilik bozukluğu ve psikopati kavramları neden aynı hastaları tanımlamıyor?",
            "Hangi özellikler psikoterapiye yanıt açısından olumlu, hangileri olumsuz işaretlerdir?",
            "Tarafsızlık bu hasta grubunda neden bir hata olabilir?",
        ],
        fikirler=[
            ("Davranış ile yapı farklıdır", "Yasa dışı davranışlar gösteren ama empati ve pişmanlık kapasitesini koruyan kişi ile duygusal "
             "bağ kuramayan, soğuk ve sömürücü kişi aynı etikete girebilir; prognoz ve tedavi çok farklıdır."),
            ("Gen tek başına bir şey açıklamaz", "Antisosyal davranış riski genetik yatkınlık ile olumsuz çevrenin etkileşiminden doğar."),
            ("Her çocuk için ayrı bir aile", "Ebeveyn davranışı çocuğun kalıtsal özelliklerine göre şekillenir; aynı evde büyüyen kardeşler "
             "farklı ebeveynlik deneyimleri yaşayabilir."),
            ("Vicdandaki boşluk", "Ebeveynin belirli antisosyal davranışlara gizli onay vermesi (gülümseme, gurur), çocuğun vicdanında o "
             "alana özgü bir boşluk bırakabilir."),
            ("Kaygı iyi bir işarettir", "Eşlik eden kaygı ya da depresyon psikoterapiye yanıt açısından olumlu bir göstergedir; bu "
             "duyguları üretemeyen yapı daha kötü prognoz taşır."),
            ("En gerçek umut önlemede", "Riskli çocuklarda aile temelli erken müdahaleler biyolojik stres yanıtında bile ölçülebilir "
             "değişim üretebilir."),
        ],
        crs=[
            "Davranım bozukluğu tanısı koyarken davranışı ve kişilerarası–duygusal yapıyı ayrı değerlendirin; empati ve pişmanlık kapasitesi prognozu belirler.",
            "Antisosyal davranışa kaygı ya da depresyon eşlik eden çocuk saf psikopati çizgisinde değildir; bu bir umut işaretidir.",
            "Ebeveynin çocuğun antisosyal davranışına verdiği tepkiyi izleyin: gülümseme, gurur ya da “aslında haklıydı” cümlesi vicdandaki boşluğun kaynağını gösterebilir.",
            "Her olayı kendi dışındaki bir nedene bağlamak, tek seferde değil tutarlı bir örüntü olarak görüldüğünde tanısal ağırlık kazanır.",
            "Cazibeli, sosyal becerisi yüksek kız ergenlerde antisosyal özellikler cinsiyet önyargısıyla gözden kaçabilir ya da başka tanılara yönlendirilebilir.",
            "Personelin belirli bir hastaya olağan dışı yakınlık ve “o aslında farklı” hissi geliştirmesi bir ilerleme değil, bir alarm işaretidir.",
            "Dürtü ile eylem arasına düşünceyi sokmak ana hedeftir; bu aynı zamanda intihar önleme anlamına gelir, çünkü bu grup intihar açısından yeterince taranmaz.",
            "Şiddet karşısında ahlaki tepkisizlik empati değil dolaylı onaydır; şaşırdığınızda bunu yargılamadan söyleyin.",
            "“Ergenlik bu, geçer” cümlesi bazen gelişimsel bilgelik, bazen görmek istemediğimiz bir şeyin üzerine örtülen battaniyedir.",
        ],
        tartisma=[
            ("MAOA bulgusu ne kadar sağlam?",
             "Kötü muamele ile antisosyal davranış arasındaki ilişkinin düşük aktiviteli MAOA genotipinde daha güçlü olduğu ilk kez bir "
             "doğum kohortunda bildirildi ([@caspi2002]); erkek kohortlarını kapsayan meta-analiz bu etkileşimi destekledi, kadınlarda "
             "sonuçlar zayıftı ([@byrd2014]). Yine de bu bir aday gen bulgusudur ve bireysel risk tahmini için kullanılmamalıdır."),
            ("Çocuklarda “psikopati” yerine duygusuz–duyarsız özellikler",
             "Çocuk ve ergenlerde psikopati terimi yerine duygusuz–duyarsız özellikler kavramı kullanılıyor; bu özellikler daha ağır ve "
             "kalıcı seyirle ilişkili, ancak yoğun ve uyarlanmış müdahalelere yanıt verebiliyor ([@frick2014]). DSM-5’in davranım "
             "bozukluğundaki “sınırlı prososyal duygular” belirleyicisi bu araştırmalara dayanır ([@dsm5])."),
            ("Otonom uyarılmışlık",
             "Yüksek otonom uyarılmışlığın antisosyal ergenlerde erişkin suçuna karşı koruyucu olduğu bulgusu ([@raine1995]) her grupta "
             "17 kişilik küçük bir örneklemden gelir; tekrarlanması gerekir."),
            ("Önleme ve stres biyolojisi",
             "Antisosyal davranış riski yüksek okul öncesi çocuklarda aile temelli önleyici müdahale, akran ortamına girişte kortizol "
             "yanıtını düşük riskli çocuklarınkine benzer bir örüntüye yaklaştırdı ([@brotman2007])."),
        ],
        sorular=[
            S("Davranım bozukluğu tanılı 14 yaşındaki bir erkek, arkadaşının telefonunu çaldıktan sonra görüşmede utandığını, annesinin "
              "öğrenmesinden korktuğunu ve uyuyamadığını söylüyor. Prognoz açısından en doğru yorum hangisidir?",
              ["Utanç ve kaygı manipülasyon amaçlıdır; prognoz kötüdür",
               "Kaygı ve utanç kapasitesi olumlu bir işarettir; psikoterapiye yanıt olasılığı daha yüksektir",
               "Prognoz yalnızca suçun türüne bağlıdır", "Bu belirtiler eşlik eden bir psikotik bozukluğu düşündürür"],
              1, "Kaygı, utanç ve pişmanlık kapasitesi saf psikopati çizgisinden uzaklaştıran ve tedaviye yanıtı olumlu yönde öngören "
                 "özelliklerdir."),
            S("Ergen servisinde bir hemşire, antisosyal özellikleri belirgin bir hasta için “Onu gerçekten anlıyorum, aslında bizden "
              "farklı değil” diyor ve hastaya kurallar dışında ayrıcalıklar tanıyor. En uygun ekip yanıtı hangisidir?",
              ["Hemşirenin yaklaşımını örnek almak",
               "Durumu ekip süpervizyonunda olası bir karşı aktarım ve suç ortaklığı riski olarak ele almak",
               "Hemşireyi uyarıp hastayla temasını kesmek", "Hastayı taburcu etmek"],
              1, "Antisosyal hastalarla çalışırken personelde gelişen olağan dışı yakınlık ve ayrıcalık tanıma karşı aktarımın tehlikeli "
                 "bir biçimidir. Suçlamadan, ekip içinde açıkça konuşmak hem personeli hem hastayı korur."),
            S("Duygusuz–duyarsız özelliklerle ilgili hangisi doğrudur?",
              ["Tedaviye hiç yanıt vermezler",
               "Daha ağır ve kalıcı davranım sorunlarıyla ilişkilidirler; ancak yoğun ve uyarlanmış müdahalelere yanıt verebilirler",
               "Yalnızca kız ergenlerde görülürler", "Yalnızca ebeveyn ihmaliyle açıklanırlar"],
              1, "Duygusuz–duyarsız özellikler davranım bozukluğunda ayrı bir alt grubu tanımlar; bu gençler standart müdahalelere daha "
                 "az yanıt verir, ancak duygusal ve bilişsel özelliklerine uyarlanmış yoğun müdahalelerden yararlanabilir ([@frick2014])."),
        ],
        akilda="Kaygı iyi bir işarettir; ahlaki tepkisizlik empati değildir.",
    ),
]
