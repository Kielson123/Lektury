# -*- coding: utf-8 -*-
"""
Generator pliku data.js ze ściśle zewnętrznymi kontekstami interpretacyjnymi
dla 41 lektur maturalnych.
Każdy kontekst zawiera wiedzę ZEWNĘTRZNĄ wobec tekstu (fakt historyczny,
dokument, traktat filozoficzny, inne dzieło sztuki/literatury, badania naukowe,
biografię autora) oraz sfunkcjonalizowanie na maturze.
"""

import json

LEKTURY = [
  # ==========================================
  # ZAKRES PODSTAWOWY
  # ==========================================
  {
    "id": "biblia",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Biblia (fragmenty Księgi Rodzaju, Hioba, Koheleta, Psalmów, Apokalipsy św. Jana)",
    "autor": "Autorzy natchnieni (tradycja biblijna)",
    "epoka": "Starożytność",
    "gatunek": "Księgi sakralne / poemat mądrościowy, hymny, apokalipsa",
    "motywy": ["cierpienie niezawinione", "marność (vanitas)", "początek i koniec świata", "teodycea", "wiara", "eschatologia"],
    "synteza": "Fundament cywilizacji judeochrześcijańskiej; zbiór ksiąg religijnych tłumaczących genezę człowieka, tajemnicę cierpienia sprawiedliwego oraz ostateczny sens dziejów.",
    "tematyMaturalne": [
      "Sens ludzkiego cierpienia w świetle doświadczeń człowieka i filozofii.",
      "Marność dóbr doczesnych a poszukiwanie wartości nieprzemijających.",
      "Koniec świata i sąd ostateczny w wyobraźni twórców różnych epok."
    ],
    "konteksty": [
      {
        "typ": "Kontekst mitologiczny / kulturowy",
        "zrodloZewnetrzne": "Mitologia grecka – mit o Prometeuszu i teogonia Hezjoda o puszce Pandory",
        "tytul": "Antyczna koncepcja cierpienia i zła (bunt prometejski a teodycea Hiobowa)",
        "opis": "W mitologii greckiej cierpienie jest konsekwencją otwarcia puszki Pandory lub zemsty bogów, a Prometeusz staje się archetypem buntownika przeciwko Zeusowi w imię miłości do ludzi. W kulturze biblijnej Księga Hioba oferuje zupełnie inne, zewnętrzne wobec greckiego mitu spojrzenie: cierpienie sprawiedliwego nie wynika ze złośliwości Stwórcy ani nie usprawiedliwia buntu, lecz jest tajemnicą boskiego planu przekraczającą ludzką logikę rozumu.",
        "funkcja": "Umożliwia zestawienie dwóch przeciwstawnych modeli znoszenia cierpienia: greckiego heroizmu opartego na buncie i dumie z judeochrześcijańskim zaufaniem Bogu mimo braku racjonalnego wytłumaczenia nieszczęścia."
      },
      {
        "typ": "Kontekst filozoficzny",
        "zrodloZewnetrzne": "Filozofia pesymizmu Artura Schopenhauera („Świat jako wola i przedstawienie”, 1819) oraz Blaise Pascal („Myśli”)",
        "tytul": "Filozoficzne koncepcje marności doczesności i nieskończoności",
        "opis": "Arthur Schopenhauer głosił, że życie człowieka jest ciągłym pasmem cierpienia napędzanym przez ślepy, nienasycony popęd (wolę), a wszelkie ziemskie dążenia do bogactwa i zaszczytów są iluzją. Z kolei Blaise Pascal pisał o człowieku jako „trzcinie myślącej” zawieszonej między nicością a nieskończonością. Myśli te stanowią zewnętrzną podbudowę teoretyczną dla sentencji Koheleta „Vanitas vanitatum et omnia vanitas”.",
        "funkcja": "Pozwala udowodnić, że koheletowy motyw przemijania nie był jedynie starożytnym aforyzmem religijnym, lecz prekursorem nowożytnej refleksji egzystencjalnej nad poczuciem absurdu i kruchością ludzkich osiągnięć."
      },
      {
        "typ": "Kontekst intertekstualny / literacki",
        "zrodloZewnetrzne": "Wiersz Czesława Miłosza „Piosenka o końcu świata” (Warszawa, 1944 r.) oraz hymn Jana Kasprowicza „Dies irae”",
        "tytul": "Wizje eschatologiczne: groza sądu ostatecznego a dekonstrukcja katastrofy",
        "opis": "Kasprowicz w młodopolskim hymnie „Dies irae” odwoływał się do biblijnej grozy Janowej: ryczących trąb, pękającej ziemi i płonących gwiazd. Czesław Miłosz w wojennej „Piosence o końcu świata” dokonał radykalnej dekonstrukcji tego toposu – koniec świata następuje nie w huku gromów, lecz w słoneczny dzień, gdy staruszek podwiązuje pomidory, a ludzie zajmują się codziennymi sprawami.",
        "funkcja": "Służy do pokazania ewolucji wyobrażeń o końcu świata: od patetycznej, kosmicznej trwogi w literaturze dawnej do kameralnej, zdemitologizowanej refleksji o powszednim przemijaniu w obliczu traumy wojennej XX wieku."
      }
    ]
  },
  {
    "id": "parandowski-mitologia",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Mitologia, cz. I Grecja",
    "autor": "Jan Parandowski",
    "epoka": "Starożytność (opracowanie XX w.)",
    "gatunek": "Zbiór mitów starożytnych",
    "motywy": ["archetyp", "fatum", "heroizm", "bunt", "hybris", "natura ludzka"],
    "synteza": "Literackie opracowanie podań i wierzeń starożytnych Greków, rekonstruujące mity kosmogoniczne, teogoniczne oraz heroiczne.",
    "tematyMaturalne": [
      "Mity greckie jako zwierciadło uniwersalnych prawd o człowieku.",
      "Pragnienie przekraczania granic a odpowiedzialność za własne czyny.",
      "Bunt w imię wartości wyższych i jego konsekwencje."
    ],
    "konteksty": [
      {
        "typ": "Kontekst psychologiczny / naukowy",
        "zrodloZewnetrzne": "Psychologia analityczna Carla Gustava Junga – teoria nieświadomości zbiorowej i archetypów",
        "tytul": "Archetypy nieświadomości zbiorowej w ujęciu psychoanalizy głębi",
        "opis": "C.G. Jung dowodził, że mity nie są prymitywnymi bajkami, lecz projekcjami archetypów – wrodzonych, wspólnych dla całej ludzkości wzorców reagowania i przeżywania (np. archetyp Wyprawy Bohatera, Wielkiej Matki, Cienia, Narcyza czy Ikara). Mity greckie przetrwały tysiąclecia właśnie dlatego, że ucieleśniają struktury psychiczne obecne w każdym człowieku niezależnie od epoki i kultury.",
        "funkcja": "Stanowi naukowy dowód na to, dlaczego postacie mitologiczne (np. Ikar, Dedal, Edyp) są wciąż żywymi metaforami postaw psychologicznych we współczesnej literaturze i kulturze."
      },
      {
        "typ": "Kontekst filozoficzno-egzystencjalny",
        "zrodloZewnetrzne": "Traktat filozoficzny Alberta Camusa „Mit Syzyfa” (1942)",
        "tytul": "Koncepcja człowieka absurdalnego i heroizmu laickiego",
        "opis": "Albert Camus w swoim słynnym eseju poddał mitologiczną postać Syzyfa reinterpretacji filozoficznej. Syzyf skazany przez bogów na wieczne wtaczanie głazu staje się dla Camusa symbolem każdego człowieka, którego życie jest pozbawione wyższego, transcendentalnego celu. Momentem heroizmu jest jednak świadomość absurdu i uśmiech buntu („Trzeba wyobrażać sobie Syzyfa szczęśliwym”).",
        "funkcja": "Ukazuje, jak mit starożytny posłużył XX-wiecznemu filozofowi do zbudowania nowożytnej etyki godności człowieka buntującego się przeciw nicości i bezsensowi istnienia."
      },
      {
        "typ": "Kontekst plastyczny / malarski",
        "zrodloZewnetrzne": "Malarstwo renesansowe – obraz Pietera Bruegla Starszego „Pejzaż z upadkiem Ikara” (ok. 1558 r.)",
        "tytul": "Zderzenie idealizmu jednostki z pragmatyzmem i obojętnością świata",
        "opis": "Na obrazie Bruegla upadek Ikara został zepchnięty na odległy margines kompozycji – w morskiej wodzie widać jedynie bezradnie wystające nogi tonącego chłopca. Na pierwszym planie oracz spokojnie zaoruje pole, pasterz opiera się o kij, a statek odpływa. Artysta ukazał zupełną obojętność natury i społeczeństwa wobec wzniosłego, lecz tragicznego porywu jednostki.",
        "funkcja": "Wzbogaca interpretację mitu o Ikarze o kontekst gorzkiej ironii społecznej: świat nie zatrzymuje się w obliczu czyjejś śmierci, a codzienny pragmatyzm bierze górę nad marzeniami o przekraczaniu ludzkich granic."
      }
    ]
  },
  {
    "id": "homer-iliada",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Iliada (fragmenty)",
    "autor": "Homer",
    "epoka": "Starożytność",
    "gatunek": "Epos heroiczny",
    "motywy": ["wojna", "gniew", "arete", "honor rycerski", "fatum", "pojednanie w obliczu śmierci"],
    "synteza": "Epos opisujący epizod z dziesiątego roku wojny trojańskiej, wywołany gniewem Achillesa po zniewadze doznanej od Agamemnona, tragiczny pojedynek z Hektorem oraz spotkanie z królem Priamem.",
    "tematyMaturalne": [
      "Wojna jako źródło cierpienia i sprawdzian człowieczeństwa.",
      "Pojęcie honoru i sławy w starożytnym etosie wojownika.",
      "Przeznaczenie (fatum) a wolność wyboru bohatera antycznego."
    ],
    "konteksty": [
      {
        "typ": "Kontekst kulturowo-antropologiczny",
        "zrodloZewnetrzne": "Archaiczny kodeks etyczny starożytnej Grecji: pojęcia arete (dzielności), kalokagatii oraz kleos aphthiton (nieprzemijającej sławy)",
        "tytul": "Kultura wstydu (shame culture) i dążenie do nieśmiertelnej sławy wojennej",
        "opis": "Antropolodzy kultury (np. E.R. Dodds w pracy „Grecy i irracjonalność”) klasyfikują świat homerycki jako „kulturę wstydu”. Wartość człowieka zależała wyłącznie od uznania społecznego, cnoty rycerskiej (arete) i zdobycia pośmiertnej sławy (kleos). Utrata czci lub publiczne poniżenie (jak odebranie branki Bryzeidy Achillesowi) było dla wojownika katastrofą gorszą niż śmierć fizyczna.",
        "funkcja": "Pozwala zrozumieć psychologiczną motywację Achillesa i jego odmowę walki – nie wynikała ona z tchórzostwa czy kaprysu, lecz z żelaznych reguł archaicznego kodeksu honorowego, według którego zniewaga domagała się zadośćuczynienia."
      },
      {
        "typ": "Kontekst historyczno-archeologiczny",
        "zrodloZewnetrzne": "Odkrycia archeologiczne Heinricha Schliemanna w Hissarlik (Troja) oraz groby szybowe w Mykenach (lata 70. XIX w.)",
        "tytul": "Kultura mykeńska epoki brązu jako historyczny fundament eposu homeryckiego",
        "opis": "Do XIX wieku opowieść o Troi uważano wyłącznie za poetycką baśń. Wykopaliska Schliemanna w Turcji (odkrycie zniszczonych warstw Troi VIIa) oraz w Grecji (złota Maska Agamemnona w Mykenach) dowiodły, że u podłoża mitu trojańskiego leżały autentyczne konflikty zbrojne z XIII w. p.n.e. o kontrolę nad szlakami handlowymi przez cieśninę Dardanele.",
        "funkcja": "Ukazuje relację między realiami epoki brązu a późniejszą o kilka stuleci poetycką kreacją Homera; dowodzi, jak pamięć historyczna o katastrofie wojennej przekształciła się w narodowy mit Greków."
      },
      {
        "typ": "Kontekst literacki / współczesny",
        "zrodloZewnetrzne": "Esej i wiersze Zbigniewa Herberta o antyku (np. „Do Marka Aurelego”, „Apollo i Marsjasz”) oraz „Iliada, czyli poemat o sile” Simone Weil",
        "tytul": "Deheroizacja wojny i refleksja nad niszczącą mocą brutalnej siły",
        "opis": "Francuska filozofka Simone Weil w słynnym eseju z 1940 r. zdefiniowała Iliadę jako „poemat o sile”, która uprzedmiotawia zarówno tego, kto jej doznaje, jak i tego, kto ją stosuje. Jedynym przełamaniem tego zaklętego kręgu przemocy jest scena z XXIV księgi – spotkanie Priama z Achillesem, gdzie wrogowie płaczą razem nad wspólnym losem ludzi skazanych na cierpienie.",
        "funkcja": "Pozwala zinterpretować scenę wykupienia zwłok Hektora nie tylko w kategoriach dawnej etykiety rycerskiej, lecz jako uniwersalny triumf miłosierdzia i humanizmu nad bezdusznym mechanizmem wojny."
      }
    ]
  },
  {
    "id": "sofokles-antygona",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Antygona",
    "autor": "Sofokles",
    "epoka": "Starożytność",
    "gatunek": "Tragedia antyczna",
    "motywy": ["konflikt tragiczny", "prawo boskie a ludzkie", "autorytaryzm władzy", "bunt moralny", "hybris", "wina tragiczna"],
    "synteza": "Konflikt między córką Edypa, wypełniającą religijny obowiązek pochówku brata Polinika, a władcą Teb Kreonem, uznającym rację stanu i bezwzględne posłuszeństwo prawu państwowemu.",
    "tematyMaturalne": [
      "Jednostka w konflikcie z władzą i prawem państwowym.",
      "Konflikt tragiczny jako zderzenie dwóch równorzędnych racji moralnych.",
      "Pycha władcy (hybris) jako źródło katastrofy państwa i rodziny."
    ],
    "konteksty": [
      {
        "typ": "Kontekst filozoficzno-prawny",
        "zrodloZewnetrzne": "Spór filozoficzny o prawo naturalne (physis) i prawo stanowione (nomos) – Arystoteles „Retoryka” oraz myśl sofistów",
        "tytul": "Antynomia prawa naturalnego i pozytywizmu prawniczego",
        "opis": "W greckiej filozofii V w. p.n.e. sofiści i Arystoteles rozróżniali 'nomos' (prawa stanowione przez społeczność, zmienne i umowne) oraz 'physis' (odwieczne, niezmienne prawa boskie i naturalne wpisane w ład kosmosu). Antygona staje się rzeczniczką prawa naturalnego, twierdząc, że dekrety śmiertelnego władcy nie mogą unieważniać odwiecznych praw bogów podziemia.",
        "funkcja": "Dostarcza aparatu pojęciowego do analizy istoty konfliktu tragicznego: dowodzi, że konflikt między Antygoną a Kreonem nie jest sporem dobra ze złem, lecz nierozstrzygalnym starciem dwóch autonomicznych porządków prawnych."
      },
      {
        "typ": "Kontekst historyczno-polityczny",
        "zrodloZewnetrzne": "Funkcjonowanie ateńskiej demokracji za czasów Peryklesa (V w. p.n.e.) i instytucja ostracyzmu",
        "tytul": "Demokracja ateńska a lęk przed tyranią i samowolą jednostki",
        "opis": "Sztuka Sofoklesa była wystawiana przed obywatelami demokratycznych Aten, którzy byli niezwykle wyczuleni na punkcie odradzania się tyranii (dlatego stosowali sąd skorupkowy – ostracyzm). Kreon z początku jawi się jako wzorowy przywódca dbający o stabilność państwa po wojnie domowej, lecz gdy odrzuca rady syna Hajmona i mędrca Tejrezjasza, staje się klasycznym tyranem lekceważącym wolę ludu.",
        "funkcja": "Służy do analizy portretu psychologicznego władcy; pokazuje, że dramat był dla ateńskich obywateli żywą przestrogą przed autorytaryzmem i gubiącą pychą (hybris) rządzących."
      },
      {
        "typ": "Kontekst religijno-kulturowy",
        "zrodloZewnetrzne": "Starożytne greckie rytuały pogrzebowe (prothesis, ekphora) i religijne wierzenia o wędrówce dusz przez rzekę Styks",
        "tytul": "Świętość pochówku zmarłych w wierzeniach religijnych starożytnych Greków",
        "opis": "W religii greckiej brak pochówku zmarłego był najstraszniejszą karą, jaka mogła spotkać człowieka. Wierzono, że dusza niepogrzebanego ciała nie mogła przekroczyć rzeki Styks za monetą w ustach (obol dla Charona) i błąkała się wiecznie jako nieszczęsny cień, sprowadzając zmazę rytualną (miasma) i gniew bogów na całe miasto.",
        "funkcja": "Wyjaśnia determinację Antygony – jej czyn nie był jedynie siostrzaną empatią, lecz bezwzględnym nakazem religijnym ratującym duszę brata przed potępieniem i oczyszczającym polis z duchowego skażenia."
      }
    ]
  },
  {
    "id": "lament-swietokrzyski",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Lament świętokrzyski (Posłuchajcie, bracia miła...)",
    "autor": "Anonim",
    "epoka": "Średniowiecze",
    "gatunek": "Plankt (lament maryjny / żal)",
    "motywy": ["cierpienie matki", "humanizacja sacrum", "współcierpienie (compassio)", "śmierć dziecka", "żałoba"],
    "synteza": "Monolog Maryi opłakującej mękę i śmierć Jezusa pod krzyżem; Maryja zwraca się do ludzi, archanioła Gabriela i innych matek, ukazując bezmiar swego macierzyńskiego bólu.",
    "tematyMaturalne": [
      "Obraz matki cierpiącej w literaturze różnych epok.",
      "Humanizacja wizerunku świętych i Boga w kulturze średniowiecza.",
      "Różne sposoby wyrażania żałoby i bezradności wobec śmierci bliskiej osoby."
    ],
    konteksty: [
      {
        "typ": "Kontekst teologiczno-kulturowy",
        "zrodloZewnetrzne": "Ruch franciszkański XIII–XV w. oraz łaciński hymn liturgiczny „Stabat Mater Dolorosa” przypisywany Jacopone da Todi",
        "tytul": "Koncepcja compassio (współcierpienia) i zwrot ku humanizmowi chrześcijańskiemu",
        "opis": "W dojrzałym średniowieczu pod wpływem św. Franciszka z Asyżu nastąpił przełom teologiczny: surowego, majestatycznego Chrystusa Sędziego (Maiestas Domini) zastąpił Chrystus Cierpiący (Christus Patiens). Wraz z tym rozwinął się kult boleści Maryi (Mater Dolorosa). Teolodzy kładli nacisk na 'compassio' – wewnętrzne współcierpienie wiernego z ludzkim bólem Matki Bożej stojącej pod krzyżem.",
        "funkcja": "Tłumaczy nowatorski charakter utworu na tle średniowiecza: odejście od łacińskiego dogmatyzmu na rzecz emocjonalnego, ludzkiego przeżywania wiary w języku ojczystym."
      },
      {
        "typ": "Kontekst plastyczny / ikonograficzny",
        "zrodloZewnetrzne": "Średniowieczna rzeźba sakralna – motyw piety (np. gotycka Pieta z Tubądzina, Pieta z Lubiąża, XV w.)",
        "tytul": "Plastyczne realizacje motywu matki trzymającej martwe ciało syna",
        "opis": "W XV-wiecznej rzeźbie na ziemiach polskich i w Europie niezwykłą popularność zyskały piety – rzeźby przedstawiające Maryję z bezwładnym, poranionym ciałem dorosłego Jezusa na kolanach. Cechowały się one ekspresyjnym realizmem: skurczem mięśni, śladami krwi, naturalistycznym grymasem rozpaczy na twarzy kobiety.",
        "funkcja": "Stanowi kontekst plastyczny ilustrujący jedność ówczesnej kultury: ten sam motyw macierzyńskiej bezradności i fizycznego cierpienia był równolegle realizowany w poezji wernakularnej i w sztuce rzeźbiarskiej."
      },
      {
        "typ": "Kontekst literacki / współczesny",
        "zrodloZewnetrzne": "Wiersz Krzysztofa Kamila Baczyńskiego „Elegia o... [chłopcu polskim]” (20 marca 1944 r.)",
        "tytul": "Topos polskiej matki opłakującej syna poległego w walce",
        "opis": "Baczyński w wierszu stylizowanym na średniowieczny lament ukazał monolog matki żegnającej syna, który poszedł na wojnę i poległ od kuli w głowę. Poeta wykorzystał dokładnie ten sam mechanizm sakralizacji cierpienia macierzyńskiego: śmierć młodego powstańca zostaje zrównana z męką Chrystusa, a zrozpaczona matka zostaje sama z pustką.",
        "funkcja": "Dowodzi trwałości toposu 'Stabat Mater' w polskiej literaturze; umożliwia porównanie średniowiecznego planktu religijnego z XX-wieczną liryką wojenną pokolenia Kolumbów."
      }
    ]
  },
  {
    "id": "rozmowa-polikarpa",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Rozmowa Mistrza Polikarpa ze Śmiercią (fragmenty)",
    "autor": "Anonim",
    "epoka": "Średniowiecze",
    "gatunek": "Dialog wierszowany / satyra stanowa",
    "motywy": ["danse macabre", "równość wobec śmierci", "memento mori", "makabra i groteska", "krytyka stanów"],
    "synteza": "Polikarp prosi Boga o spotkanie ze Śmiercią. Ukazuje mu się odrażający, rozkładający się trup niewieści z kosą, który z groteskową satysfakcją wykłada swoją niszczycielską moc i przypomina, że nikt nie ujdzie jej wyrokowi.",
    "tematyMaturalne": [
      "Motyw tańca śmierci (danse macabre) w kulturze dawnej i współczesnej.",
      "Śmierć jako sędzia demaskujący wady społeczeństwa i hipokryzję elit.",
      "Groteskowy i makabryczny obraz śmierci w literaturze."
    ],
    konteksty: [
      {
        "typ": "Kontekst historyczno-demograficzny",
        "zrodloZewnetrzne": "Pandemia Czarnej Śmierci (dżumy) w Europie w latach 1347–1351 i jej skutki cywilizacyjne",
        "tytul": "Doświadczenie masowego umierania i narodziny obsesji śmierci w XIV i XV wieku",
        "opis": "W połowie XIV wieku dżuma pochłonęła od 30% do 60% ludności kontynentu europejskiego. Nagłość zgonów, bezradność lekarzy i widok gnijących ciał na ulicach wywołały głęboki szok psychiczny. Załamało się poczucie bezpieczeństwa, co zaowocowało w kulturze paniczną potrzebą przygotowania się na nieuchronny zgon (powstanie traktatów 'ars moriendi' – sztuki dobrego umierania).",
        "funkcja": "Tłumaczy genezę makabrycznego realizmu utworu: opis gnijącego ciała Śmierci (zapadłe oczy, żółte żebra, cieknący nos) był dosłownym odzwierciedleniem codziennych widoków epidemicznych ówczesnej Europy."
      },
      {
        "typ": "Kontekst ikonograficzny / sztuka",
        "zrodloZewnetrzne": "Europejska tradycja drzeworytów i fresków Danse Macabre (np. freski w Clusone we Włoszech, drzeworyty Hansa Holbeina Młodszego z 1538 r.)",
        "tytul": "Egalitaryzm śmierci w sztukach plastycznych późnego średniowiecza",
        "opis": "W plastyce późnego średniowiecza upowszechnił się motyw korowodu, w którym kościotrup lub personifikacja śmierci prowadzi za rękę papieża, cesarza, kardynała, ale też kupca, żebraka i niemowlę. Obrazy te uczyły zasady 'memento mori' oraz egalitaryzmu: w obliczu grobu wszelkie ziemskie hierarchie, tytuły i majątki stają się bezwartościowe.",
        "funkcja": "Pozwala zanalizować kompozycję utworu: Śmierć w rozmowie z Polikarpem kolejno wylicza i 'zaprasza do tańca' poszczególne stany społeczne, dokładnie odtwarzając strukturę ówczesnych przedstawień malarskich."
      },
      {
        "typ": "Kontekst literacko-filmowy / współczesny",
        "zrodloZewnetrzne": "Arcydzieło filmowe Ingmara Bergmana „Siódma pieczęć” (1957) oraz wiersz Wisławy Szymborskiej „O śmierci bez przesady”",
        "tytul": "Gra człowieka ze śmiercią i dekonstrukcja średniowiecznej personifikacji",
        "opis": "U Bergmana rycerz powracający z wyprawy krzyżowej staje do partii szachów ze Śmiercią ubraną w czarny płaszcz, próbując zyskać czas na odnalezienie sensu wiary. Szymborska z kolei drwi z dawnej personifikacji, zauważając, że śmierć 'nie zna się na żartach, na gwiazdach, na mostach' i choć triumfuje nad ciałem, jest bezradna wobec tego, co człowiek po sobie pozostawia w pamięci i sztuce.",
        "funkcja": "Umożliwia zestawienie średniowiecznego, jarmarczno-groteskowego wyobrażenia Śmierci z jej egzystencjalnymi i zdemitologizowanymi interpretacjami w kulturze XX wieku."
      }
    ]
  },
  {
    "id": "piesn-o-rolandzie",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Pieśń o Rolandzie (fragmenty)",
    "autor": "Anonim (przypisywana Turoldowi)",
    "epoka": "Średniowiecze",
    "gatunek": "Chanson de geste (pieśń o czynach)",
    "motywy": ["etos rycerski", "honor", "patriotyzm feudalny", "obrona wiary", "ars moriendi rycerza"],
    "synteza": "Epos rycerski opowiadający o zdradzie Ganelona, heroicznej walce tylnej straży wojsk Karola Wielkiego w pirenejskim wąwozie Roncevaux i męczeńskiej śmierci hrabiego Rolanda.",
    "tematyMaturalne": [
      "Wzorzec rycerza idealnego w literaturze i kulturze średniowiecza.",
      "Honor jako nadrzędna wartość determinująca losy bohatera.",
      "Śmierć rycerza jako spektakl wiary i wierności ojczyźnie."
    ],
    "konteksty": [
      {
        "typ": "Kontekst historyczno-kronikarski",
        "zrodloZewnetrzne": "Kronika Einharda „Życie Karola Wielkiego” (Vita Karoli Magni, ok. 830 r.) – autentyczna potyczka z chrześcijańskimi Baskami w 778 r.",
        "tytul": "Prawda historyczna a propagandowa mitologizacja wyprawy hiszpańskiej",
        "opis": "W autentycznych rocznikach frankijskich potyczka w Roncevaux z 15 sierpnia 778 r. była drobnym starciem z chrześcijańskimi góralami baskijskimi, którzy zaatakowali tylną straż Karola Wielkiego wracającego z nieudanej wyprawy na Saragossę. W 'Pieśni o Rolandzie' (spisanej na przełomie XI i XII w.) fakt ten został przekształcony w monumentalną, kosmiczną batalię chrześcijaństwa z pogańskim światem islamu.",
        "funkcja": "Pokazuje mechanizm politycznej manipulacji historią: epos przekształcił militarną wpadkę władcy w chwalebny mit religijny służący budowaniu dumy monarchii francuskiej."
      },
      {
        "typ": "Kontekst polityczno-religijny",
        "zrodloZewnetrzne": "Synod w Clermont (1095 r.), apel papieża Urbana II i narodziny ideologii wypraw krzyżowych (krucjat)",
        "tytul": "Ideologia świętej wojny i religijna propaganda epoki krucjat",
        "opis": "Czas powstania zachowanej redakcji 'Pieśni o Rolandzie' zbiega się z I wyprawą krzyżową do Ziemi Świętej. Kościół promował wówczas ideę 'milites Christi' (rycerzy Chrystusa), którym za udział w wojnie z niewiernymi obiecywano całkowite odpuszczenie grzechów i natychmiastowe zbawienie w razie śmierci na polu walki.",
        "funkcja": "Wyjaśnia scenę śmierci Rolanda: archanioł Michał i anioł Gabriel osobiście zstępują z nieba po duszę hrabiego, co stanowiło bezpośrednią obietnicę zbawienia dla ówczesnych krzyżowców walczących z muzułmanami."
      },
      {
        "typ": "Kontekst prawno-obyczajowy",
        "zrodloZewnetrzne": "Średniowieczny kodeks rycerski, obyczaj pasowania oraz feudalny akt hołdu lennego (homagium i feodum)",
        "tytul": "Feudalna hierarchia zależności i pojęcie nieskazitelnego honoru rycerskiego",
        "opis": "Struktura społeczna średniowiecza opierała się na sieci osobistych przysiąg wierności między wasalem a seniorem. Złamanie przysięgi lub posądzenie o tchórzostwo było plamą, której nie zmywały żadne dobra materialne. Rycerz był zobowiązany do obrony Kościoła, wdów, sierot i sławy swego rodu.",
        "funkcja": "Pozwala pojąć motywację Rolanda, gdy ten początkowo odmawia zadęcia w róg (Olifant) na widok przeważających sił wroga: wezwanie pomocy uważał za zniewagę swego rodu i hańbę dla 'słodkiej Francji'."
      }
    ]
  },
  {
    "id": "szekspir-makbet",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Makbet",
    "autor": "William Szekspir",
    "epoka": "Renesans / Barok (teatr elżbietański)",
    "gatunek": "Tragedia szekspirowska",
    "motywy": ["żądza władzy", "zbrodnia i kara", "demoniczne zło", "destrukcja sumienia", "halucynacje", "tyrania"],
    "synteza": "Dramat szkockiego wodza, który pod wpływem przepowiedni wiedźm i ambicji żony morduje prawowitego króla Dunkana, wstępuje na tron i ulega obłędowi zbrodni, pociągającemu za sobą kolejne morderstwa i moralny upadek.",
    "tematyMaturalne": [
      "Wpływ żądzy władzy na degradację moralną człowieka.",
      "Zbrodnia i psychologiczne mechanizmy winy w literaturze.",
      "Rola sił nadprzyrodzonych w podejmowaniu decyzji przez jednostkę."
    ],
    konteksty: [
      {
        "typ": "Kontekst filozoficzno-polityczny",
        "zrodloZewnetrzne": "Traktat polityczny Niccolò Machiavellego „Książę” (Il Principe, 1532 r.)",
        "tytul": "Doktryna amoralnej racji stanu (machiawelizm) a sprawowanie władzy",
        "opis": "Machiavelli dowodził, że skuteczny władca musi wyzbyć się tradycyjnych skrupułów moralnych i umieć stosować przemoc oraz podstęp („cel uświęca środki”), aby utrzymać władzę w państwie. Makbet próbuje działać wedle tych cynicznych reguł: likwiduje rywali politycznych (Banko, rodzina Macduffa) i rządzi terrorem, lecz w przeciwieństwie do wyrachowanego 'Księcia' niszczy go własne sumienie i paranoja.",
        "funkcja": "Pozwala ukazać tragedię Szekspira jako polemikę z machiawelizmem: dowodzi, że władza zdobyta drogą niemoralną nie buduje trwałego państwa, lecz zamienia życie tyrana w piekło wewnętrzne i ściąga na niego sprawiedliwy odwet poddanych."
      },
      {
        "typ": "Kontekst historyczno-biograficzny",
        "zrodloZewnetrzne": "Panowanie króla Jakuba I Stuarta, spisek prochowy Guy Fawkesa (1605 r.) oraz traktat monarchy „Daemonologie” (1597 r.)",
        "tytul": "Szkockie powiązania dynastii Stuartów, lęk przed królobójstwem i wiara w czary",
        "opis": "Dramat powstał tuż po objęciu tronu Anglii przez Jakuba I (pochodzącego ze Szkocji, rzekomego potomka szlachetnego Banka). Król był osobiście zafascynowany procesami o czary i napisał traktat o demonologii. Ponadto po udaremnionym katolickim zamachu na parlament i króla (spisek prochowy) w Anglii panowała psychoza zdrady i wiara w boską ochronę prawowitego monarchy.",
        "funkcja": "Tłumaczy obecność czarownic i zjaw w utworze oraz gloryfikację postaci Banka (przodka króla Jakuba I), a także ideowe przesłanie sztuki potępiające bunt przeciw legalnej władzy namaszczonej przez Boga."
      },
      {
        "typ": "Kontekst historiograficzny / źródłowy",
        "zrodloZewnetrzne": "Dzieło kronikarskie Raphaela Holinsheda „Kroniki Anglii, Szkocji i Irlandii” (Chronicles of England, Scotland, and Ireland, 1577 r.)",
        "tytul": "Szekspirowska modyfikacja faktów historycznych na potrzeby dramatu",
        "opis": "Holinshed w swojej kronice opisywał autentycznego króla Makbeta z XI wieku, który rządził Szkocją przez kilkanaście lat sprawiedliwie i pomyślnie, a historyczny Dunkan był młodym, nieudolnym wodzem. Co więcej, w kronice Banko był bezpośrednim wspólnikiem Makbeta w spisku. Szekspir celowo zmienił te fakty: uczynił Dunkana świętym starcem, Banka niewinnym sprawiedliwym, a z Makbeta stworzył potwora pchanego żądzą krwi.",
        "funkcja": "Ukazuje kunszt dramaturga: Szekspir nie pisał kroniki historycznej, lecz świadomie przetworzył materiał faktograficzny, by stworzyć uniwersalne studium psychologiczne narodzin i rozrostu zła w człowieku."
      }
    ]
  },
  {
    "id": "molier-skapiec",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Skąpiec",
    "autor": "Molier",
    "epoka": "Barok / Klasycyzm francuski",
    "gatunek": "Komedia charakterów",
    "motywy": ["chciwość", "pieniądz", "tyrania domowa", "hipokryzja", "małżeństwo dla posagu", "komizm"],
    "synteza": "Komedia przedstawiająca postać paryskiego mieszczanina Harpagona, którego obsesyjna żądza gromadzenia złota niszczy relacje z dziećmi (Kleantem i Elizą) i doprowadza go do karykaturalnego szaleństwa.",
    "tematyMaturalne": [
      "Wpływ pieniądza i chciwości na relacje rodzinne.",
      "Karykatura i komizm jako narzędzia naprawy ludzkich obyczajów.",
      "Konflikt pokoleń: bezduszny egoizm rodziców a prawo młodych do szczęścia."
    ],
    konteksty: [
      {
        "typ": "Kontekst literacki / tradycja antyczna",
        "zrodloZewnetrzne": "Antyczna komedia rzymska Plauta „Aulularia” (Skarb, przełom III i II w. p.n.e.)",
        "tytul": "Rzymski archetyp skąpca – Euklion jako literacki protoplasta Harpagona",
        "opis": "Plaut stworzył w literaturze archetyp chorobliwego ciułacza: stary Euklion po znalezieniu garnka złota popada w paniczną paranoję, podejrzewa o kradzież niewolników, a nawet koguta grzebiącego w ziemi. Molier przeniósł niemal dosłownie całe sceny z komedii rzymskiej (np. słynny monolog po zniknięciu szkatułki i podejrzewanie widowni teatralnej).",
        "funkcja": "Świadczy o klasycystycznej zasadzie imitatio antiquorum (naśladowania mistrzów starożytności); pozwala wykazać, że motyw destrukcyjnej siły chciwości jest odwiecznym toposem komediowym w kulturze europejskiej."
      },
      {
        "typ": "Kontekst historyczno-gospodarczy",
        "zrodloZewnetrzne": "Przemiany gospodarcze w monarchii Ludwika XIV – doktryna merkantylizmu Jean-Baptiste Colberta i wzrost znaczenia burżuazji",
        "tytul": "Narodziny nowożytnego kapitalizmu i kult kapitału w XVII-wiecznej Francji",
        "opis": "W epoce Króla Słońce tradycyjna arystokracja traciła pozycję finansową na rzecz bogacącego się mieszczaństwa (burżuazji). Pieniądz stał się nową miarą wartości człowieka, umożliwiającą kupowanie ziemi i tytułów szlacheckich. Harpagon jest uosobieniem najgorszych patologii tego wczesnokapitalistycznego kultu akumulacji kapitału, gdzie lichwa wypiera wszelkie ludzkie uczucia.",
        "funkcja": "Pozwala odczytać komedię nie tylko jako uniwersalną psychodramę rodzinną, lecz jako przenikliwą satyrę na realne procesy ekonomiczne zachodzące we Francji w dobie absolutyzmu."
      },
      {
        "typ": "Kontekst filozoficzno-estetyczny",
        "zrodloZewnetrzne": "Filozoficzna teoria komizmu Henriego Bergsona wyłożona w eseju „Śmiech” (Le Rire, 1900 r.)",
        "tytul": "Koncepcja komizmu jako „mechaniczności narzuconej na żywą naturę człowieka”",
        "opis": "Bergson sformułował tezę, że źródłem komizmu jest usztywnienie i automatyzm psychiczny jednostki, która przestaje elastycznie reagować na świat i działa jak nakręcona maszyna. Harpagon jest podręcznikowym przykładem takiej 'automatyzacji': cokolwiek się dzieje (miłość, małżeństwo, uczta, śmierć), jego umysł reaguje wyłącznie jedną kategorią – kosztem finansowym ('bez posagu!').",
        "funkcja": "Stanowi znakomite narzędzie teoretyczne do analizy komizmu postaci Harpagona: jego komizm wynika z dehumanizacji własnej osobowości na rzecz mechanicznej obsesji na punkcie szkatułki."
      }
    ]
  },
  {
    "id": "krasicki-satyry",
    "kategoria": "podstawowy",
    "kategoriaNazwa": "Zakres podstawowy",
    "tytul": "Satyry (wybrana satyra, np. „Świat zepsuty”, „Do króla”, „Pijaństwo”)",
    "autor": "Ignacy Krasicki",
    "epoka": "Oświecenie",
    "gatunek": "Satyra",
    "motywy": ["krytyka sarmatyzmu", "pijaństwo", "rozum i umiar", "naprawa państwa", "demaskacja hipokryzji", "patriotyzm"],
    "synteza": "Wierszowane utwory dydaktyczne ośmieszające wady społeczeństwa polskiego dobie stanisławowskiej: pijaństwo, pieniactwo, kosmopolityzm i zawiść szlachecką wobec reformatorskich działań króla.",
    "tematyMaturalne": [
      "Satyra jako narzędzie walki o naprawę obyczajów i ocalenie ojczyzny.",
      "Konflikt między sarmackim konserwatyzmem a oświeceniowym racjonalizmem.",
      "Obłuda i słabości ludzkiej natury w zwierciadle literatury Oświecenia."
    ],
    konteksty: [
      {
        "typ": "Kontekst historyczno-polityczny",
        "zrodloZewnetrzne": "Trauma I rozbioru Polski (1772 r.) i opór szlachty sarmackiej wobec reform Sejmu Rozbiorowego i króla Stanisława Augusta",
        "tytul": "Kryzys państwowości I Rzeczypospolitej jako bezpośredni impuls twórczy",
        "opis": "Satyry Krasickiego powstały w cieniu utraty części terytorium Rzeczypospolitej na rzecz Rosji, Prus i Austrii. W 'Świecie zepsutym' poeta bije na alarm: 'Ginie ojczyzna!'. Z kolei w satyrze 'Do króla' w genialny sposób, posługując się chwytem pozornego ataku, obnaża tępotę konserwatywnej szlachty zarzucającej Poniatowskiemu, że jest za młody, za mądry i nie jest cudzoziemcem.",
        "funkcja": "Uzasadnia patriotyczny cel powstania satyr: utwory biskupa warmińskiego nie były salonową rozrywką, lecz publicystyką ratunkową dla chylącego się ku upadkowi państwa."
      },
      {
        "typ": "Kontekst kulturowo-publicystyczny",
        "zrodloZewnetrzne": "Działalność warszawskiego czasopisma „Monitor” (1765–1785) oraz mecenat obiadów czwartkowych",
        "tytul": "Oświeceniowy program dydaktyczny „uczyć, bawiąc” (docere, delectare, movere)",
        "opis": "Środowisko skupione wokół Stanisława Augusta Poniatowskiego i czasopisma 'Monitor' (wzorowanego na angielskim 'The Spectator') stawiało sobie za cel wychowanie nowej elity obywatelskiej. Zgodnie z poetyką oświeceniową satyra miała krytykować zjawiska i postawy ogólne, a nie konkretne nazwiska, aby czytelnik sam zawstydził się własnych przywar.",
        "funkcja": "Tłumaczy formę wypowiedzi poetyckiej: użycie humoru, dystansu i wyrafinowanej ironii jako najskuteczniejszej metody pedagogiki narodowej w dobie polskiego Oświecenia."
      },
      {
        "typ": "Kontekst retoryczno-antyczny",
        "zrodloZewnetrzne": "Rzymska tradycja satyryczna: satyry Horacego (Sermones) i satyry Juwenalisa",
        "tytul": "Horacjański uśmiech wyrozumiałości a juwenalisowy gniew oburzenia",
        "opis": "Krasicki świadomie czerpał z dwóch biegunów antycznej satyry. W 'Pijaństwie' dominuje ton Horacego – pogodna drwina z ludzkich słabości i braku umiaru, z kolei w 'Świecie zepsutym' słychać patetyczny gniew Juwenalisa, który pisał: 'Difficile est satiram non scribere' (Trudno satyry nie pisać, widząc bezmiar niegodziwości świata).",
        "funkcja": "Dowodzi kunsztu literackiego Krasickiego jako spadkobiercy wielkiej europejskiej tradycji klasycznej, potrafiącego łączyć rzymską retorykę z realiami polskiego dworku szlacheckiego."
      }
    ]
  }
]

print(f"Liczba przygotowanych lektur podstawowych (część 1): {len(LEKTURY)}")
