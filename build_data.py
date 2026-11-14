# -*- coding: utf-8 -*-
import json

def get_all_lektury():
    # Zwraca listę wszystkich 41 lektur z 3 w pełni zewnętrznymi kontekstami
    # Zgodnie z poleceniem: informacje w kontekstach są zewnętrzne dziełu i nie są w nim zawarte!
    return [
      # 1. BIBLIA
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
            "typ": "Kontekst mitologiczny / archetypiczny",
            "zrodloZewnetrzne": "Mitologia grecka – mit o Prometeuszu i teogonia Hezjoda o puszce Pandory",
            "tytul": "Antyczna koncepcja cierpienia i zła (bunt prometejski a teodycea Hiobowa)",
            "opis": "W mitologii greckiej cierpienie jest konsekwencją otwarcia puszki Pandory lub zemsty bogów, a Prometeusz staje się archetypem buntownika przeciwko Zeusowi w imię miłości do ludzi. W kulturze biblijnej Księga Hioba oferuje zupełnie inne, zewnętrzne wobec greckiego mitu spojrzenie: cierpienie sprawiedliwego nie wynika ze złośliwości Stwórcy ani nie usprawiedliwia buntu, lecz jest tajemnicą boskiego planu przekraczającą ludzką logikę rozumu.",
            "funkcja": "Umożliwia zestawienie dwóch przeciwstawnych modeli znoszenia cierpienia: greckiego heroizmu opartego na buncie i dumie z judeochrześcijańskim zaufaniem Bogu mimo braku racjonalnego wytłumaczenia nieszczęścia."
          },
          {
            "typ": "Kontekst filozoficzny",
            "zrodloZewnetrzne": "Filozofia pesymizmu Artura Schopenhauera („Świat jako wola i przedstawienie”, 1819) oraz myśli Blaise'a Pascala",
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

      # 2. JAN PARANDOWSKI - MITOLOGIA
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

      # 3. HOMER - ILIADA
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

      # 4. SOFOKLES - ANTYGONA
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

      # 5. LAMENT ŚWIĘTOKRZYSKI
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
        "konteksty": [
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

      # 6. ROZMOWA MISTRZA POLIKARPA ZE ŚMIERCIĄ
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
        "konteksty": [
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

      # 7. PIEŚŃ O ROLANDZIE
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

      # 8. WILLIAM SZEKSPIR - MAKBET
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
        "konteksty": [
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

      # 9. MOLIER - SKĄPIEC
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
        "konteksty": [
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

      # 10. IGNACY KRASICKI - SATYRY
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
        "konteksty": [
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
      },

      # 11. ADAM MICKIEWICZ - BALLADY (W TYM ROMANTYCZNOŚĆ)
      {
        "id": "mickiewicz-ballady",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Wybrane ballady, w tym „Romantyczność”",
        "autor": "Adam Mickiewicz",
        "epoka": "Romantyzm",
        "gatunek": "Ballada romantyczna",
        "motywy": ["poznanie pozazmysłowe", "wiara i czucie", "szaleństwo z miłości", "ludowość", "świat duchów", "manifest epoki"],
        "synteza": "Ballada programowa otwierająca tomik 'Ballad i romansów' (1822 r.), przedstawiająca obłąkaną Karusię rozmawiającą z duchem Jasieńka oraz spór poety ze Starcem o prymat serca nad szkiełkiem i okiem mędrca.",
        "tematyMaturalne": [
          "Serce czy rozum? Dwa sprzeczne modele poznawania świata.",
          "Rola wierzeń ludowych w formowaniu nowego światopoglądu romantycznego.",
          "Odrzucenie i samotność jednostki wybitnie wrażliwej w społeczeństwie."
        ],
        "konteksty": [
          {
            "typ": "Kontekst filozoficzno-naukowy",
            "zrodloZewnetrzne": "Rozprawa prof. Jana Śniadeckiego „O pismach klasycznych i romantycznych” (1819 r.) oraz wileński spór klasyków z romantykami",
            "tytul": "Racjonalizm wileńskiego oświecenia contra irracjonalizm młodych romantyków",
            "opis": "Postać Starca w 'Romantyczności' jest bezpośrednią aluzją do Jana Śniadeckiego – wybitnego matematyka, astronoma i rektora Uniwersytetu Wileńskiego, który w swoich pismach potępiał romantyzm jako bełkot, zabobon i 'szkołę zdrady rozumu'. Mickiewicz polemizuje z autorytetem profesora, twierdząc, że empiryczne metody naukowe ('szkiełko i oko') są ślepe na duchowe prawdy bytu.",
            "funkcja": "Kluczowy kontekst epoki: ujawnia, że wiersz był manifestem ideologicznym młodego pokolenia wileńskiego, które wypowiedziało posłuszeństwo autorytetom naukowym oświecenia na rzecz metafizyki i intuicjonizmu."
          },
          {
            "typ": "Kontekst etnograficzny / naukowy",
            "zrodloZewnetrzne": "Badania etnograficzne Zoriana Dołęgi-Chodakowskiego wyłożone w dziele „O Sławiańszczyźnie przed chrześcijaństwem” (1818 r.)",
            "tytul": "Pionierskie odkrycie duchowej wartości kultury ludowej u progu romantyzmu",
            "opis": "Dołęga-Chodakowski był prekursorem zbierania pieśni, podań i obrzędów ludu białoruskiego i ukraińskiego, głosząc, że to w wiejskim ludzie przetrwała czysta, pierwotna tożsamość słowiańska. Mickiewicz pod wpływem tych idei uznał gminny kodeks moralny (kara za zdradę w 'Świteziance', zbrodnia w 'Lilijach') za fundament nowej estetyki poetyckiej.",
            "funkcja": "Dowodzi, że zwrot Mickiewicza ku ludowości nie był powierzchowną modą estetyczną, lecz świadomym programem kulturowym czerpiącym z ówczesnych badań nad tożsamością narodową."
          },
          {
            "typ": "Kontekst biograficzny",
            "zrodloZewnetrzne": "Listy Mickiewicza do przyjaciół z lat 1820–1822 oraz małżeństwo Maryli Wereszczakówny z hrabią Wawrzyńcem Puttkamerem (1821 r.)",
            "tytul": "Autentyczny dramat miłosny poety jako źródło motywu miłości silniejszej niż śmierć",
            "opis": "Wydanie 'Ballad i romansów' zbiegło się z największym dramatem osobistym poety: ukochana Maryla z przyczyn majątkowych poślubiła bogatego hrabiego Puttkamera. Mickiewicz popadł w głęboką depresję i myśli samobójcze. Motyw Karusi cierpiącej po stracie Jasieńka był bezpośrednim, emocjonalnym echem jego własnego poczucia osamotnienia i niezgody na prawa rządzące światem materialnym.",
            "funkcja": "Nadaje utworowi autentyzm przeżycia: udowadnia, że romantyczne rozdarcie między marzeniem a brutalną rzeczywistością miało swe źródło w osobistej biografii wieszcza."
          }
        ]
      },

      # 12. ADAM MICKIEWICZ - DZIADY CZ. III
      {
        "id": "mickiewicz-dziady-3",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Dziady cz. III",
        "autor": "Adam Mickiewicz",
        "epoka": "Romantyzm",
        "gatunek": "Dramat romantyczny",
        "motywy": ["martyrologia narodowa", "mesjanizm", "prometeizm", "bunt przeciw Bogu", "walka dobra ze złem", "despotyzm caratu"],
        "synteza": "Dramat narodowy osnuty wokół carskich represji wobec wileńskiej młodzieży, Wielkiej Improwizacji Konrada wadzącego się z Bogiem o los ojczyzny oraz mistycznej wizji Polski jako Chrystusa narodów w Widzeniu ks. Piotra.",
        "tematyMaturalne": [
          "Cierpienie narodu i próby nadania mu sensu dziejowego.",
          "Postawa prometejska – duma i poświęcenie jednostki dla milionów.",
          "Portret władzy despotycznej i oblicza konformizmu społeczeństwa (Salon warszawski)."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-dokumentalny",
            "zrodloZewnetrzne": "Archiwalne akta śledztwa senatora Nikołaja Nowosilcowa przeciw Towarzystwu Filomatów i Filaretów w Wilnie (1823–1824 r.)",
            "tytul": "Autentyczne carskie śledztwo i proces wileński jako kanwa martyrologii",
            "opis": "Bohaterowie uwięzieni w klasztorze bazylianów (Jan Sobolewski, Tomasz Zan, Feliks Kółakowski, Janczewski) byli autentycznymi przyjaciółmi Mickiewicza z procesu z 1823 r. Nowosilcow, dążąc do zrobienia kariery na dworze cara Aleksandra I, wyolbrzymił działalność samokształceniowych kółek młodzieży do rangi groźnego spisku rewolucyjnego, skazując dziesiątki studentów na katorgę lub wcielenie do wojsk carskich.",
            "funkcja": "Stanowi dokumentalny fundament dramatu: dowodzi, że wstrząsające sceny wywózek kibitkami na Sybir nie były fikcją literacką, lecz artystycznym utrwaleniem autentycznych represji carskich na Kresach."
          },
          {
            "typ": "Kontekst biograficzno-emigracyjny",
            "zrodloZewnetrzne": "Pobyt Adama Mickiewicza w Dreźnie wiosną 1832 r. i jego wyrzuty sumienia po upadku powstania listopadowego",
            "tytul": "Drezdeński kryzys moralny poety po nieobecności w walkach powstańczych",
            "opis": "W czasie wybuchu powstania listopadowego (1830 r.) Mickiewicz przebywał we Włoszech i z nie do końca jasnych przyczyn nie dotarł do walczącej Warszawy (zatrzymał się w Wielkopolsce). Po klęsce powstania znalazł się w Dreźnie wśród tysięcy zgorzkniałych emigrantów, dręczony kompleksem winy, że nie przelał krwi za ojczyznę. 'Dziady cz. III' powstały w ciągu zaledwie kilku tygodni jako próba duchowej ekspiacji (odkupienia winy) poety wobec walczących rodaków.",
            "funkcja": "Tłumaczy niezwykłą temperaturę emocjonalną utworu: pasja buntu Konrada i sakralizacja cierpienia narodu były próbą psychologicznego poradzenia sobie z własną bezczynnością militarną i spłaceniem długu wobec powstańców."
          },
          {
            "typ": "Kontekst filozoficzno-religijny",
            "zrodloZewnetrzne": "Filozofia mesjanizmu europejskiego: pisma Louisa-Claude'a de Saint-Martina oraz teozofia Andrzeja Towiańskiego",
            "tytul": "Doktryna mesjanizmu historiozoficznego („Polska Chrystusem narodów”)",
            "opis": "Mesjanizm głosił, że historia świata podlega boskiemu planowi zbawienia, w którym naród dotknięty największym cierpieniem staje się zbiorowym Mesjaszem odkupującym winy całej ludzkości. W Widzeniu ks. Piotra Mickiewicz przenosi tę doktrynę na grunt polski: rozbiory i klęska zrywu listopadowego są ukrzyżowaniem narodu, które doprowadzi do zmartwychwstania i wyzwolenia wszystkich uciemiężonych ludów Europy.",
            "funkcja": "Dostarcza klucza do historiozofii dramatu: Mickiewicz przekształcił militarną i polityczną klęskę powstania w moralne zwycięstwo, dając załamanym Polakom wiarę w nadrzędny, metafizyczny sens ich ofiary."
          }
        ]
      },

      # 13. BOLESŁAW PRUS - LALKA
      {
        "id": "prus-lalka",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Lalka",
        "autor": "Bolesław Prus",
        "epoka": "Pozytywizm",
        "gatunek": "Powieść realistyczna / społeczno-obyczajowa",
        "motywy": ["praca organiczna i u podstaw", "miłość romantyczna a pragmatyzm", "rozkład arystokracji", "asymilacja Żydów", "kapitalizm", "miasto jako organizm"],
        "synteza": "Panorama Warszawy lat 70. XIX wieku ukazana przez pryzmat losów Stanisława Wokulskiego – dawnego powstańca i genialnego kupca, którego wybitną energię społeczną niszczy destrukcyjna miłość do arystokratki Izabeli Łęckiej.",
        "tematyMaturalne": [
          "Tragizm człowieka zawieszonego między ideałami dwóch epok (romantyzmu i pozytywizmu).",
          "Krytyczny obraz społeczeństwa polskiego u schyłku XIX wieku.",
          "Praca organiczna i praca u podstaw – wielkie idee a twarda rzeczywistość."
        ],
        "konteksty": [
          {
            "typ": "Kontekst filozoficzno-naukowy",
            "zrodloZewnetrzne": "Filozofia pozytywizmu: teoria ewolucjonizmu Karola Darwina, scjentyzm Auguste'a Comte'a oraz socjologiczny organicyzm Herberta Spencera",
            "tytul": "Koncepcja społeczeństwa jako żywego organizmu i bezwzględna walka o byt",
            "opis": "Herbert Spencer dowodził, że społeczeństwo funkcjonuje jak biologiczny organizm: aby było zdrowe, wszystkie jego komórki (warstwy społeczne) muszą harmonijnie współpracować. Z kolei Karol Darwin opisał walkę o przetrwanie, w której zwyciężają jednostki najlepiej przystosowane. Prus zderza te teorie z polską rzeczywistością: 'organizm' polski jest chory, ponieważ arystokracja pasożytuje na reszcie narodu, a polscy kupcy nie wytrzymują konkurencji z kapitałem niemieckim i żydowskim.",
            "funkcja": "Stanowi fundament intelektualny powieści: pozwala dowieść, że 'Lalka' jest wielkim traktatem socjologicznym weryfikującym pozytywistyczne złudzenia o harmonijnym postępie ludzkości."
          },
          {
            "typ": "Kontekst historyczno-społeczny",
            "zrodloZewnetrzne": "Trauma klęski powstania styczniowego (1863 r.), carski ukaz uwłaszczeniowy (1864 r.) i zjawisko pauperyzacji szlachty",
            "tytul": "Popowstaniowy szok cywilizacyjny i narodziny nowej struktury społecznej",
            "opis": "Po upadku zrywu z 1863 r. carska władza skonfiskowała majątki tysiącom polskich ziemian, a uwłaszczenie chłopów odebrało dworom darmową siłę roboczą. Zubożała szlachta (tzw. wysadzeni z siodła) masowo uciekała do Warszawy, nie potrafiąc pracować ani zarabiać na siebie (reprezentantem tej grupy jest Tomasz Łęcki). Jednocześnie Wokulski – były zesłaniec na Sybir – zmuszony jest porzucić wzniosły etos walki zbrojnej na rzecz handlu galanterią.",
            "funkcja": "Wyjaśnia historyczne pęknięcie w psychice Wokulskiego: w jego sercu wciąż tli się romantyczny kult ofiary i walki narodowej, lecz realia zaborów wymagają chłodnego, kupieckiego pragmatyzmu."
          },
          {
            "typ": "Kontekst dziennikarsko-biograficzny",
            "zrodloZewnetrzne": "Wieloletnia praca Bolesława Prusa jako felietonisty „Kuriera Warszawskiego” („Kroniki tygodniowe”) i autentyczne realia handlowe Warszawy",
            "tytul": "Kronikarska metoda pracy pisarza i topograficzna precyzja w opisie nędzy Powiśla",
            "opis": "Bolesław Prus (Aleksander Głowacki) pisał powieść jako wytrawny dziennikarz śledczy. Przez lata badał realne budżety warszawskich rodzin, odwiedzał szynki na Powiślu, analizował procesy asymilacji Żydów i relacje handlowe. Sklep Wokulskiego był wzorowany na autentycznym luksusowym magazynie Jana Minca przy Krakowskim Przedmieściu, a opis ruder i zanieczyszczeń ściekowych Powiśla dokładnie pokrywał się z jego alarmistycznymi felietonami prasowymi.",
            "funkcja": "Świadczy o najwyższym poziomie realizmu krytycznego dzieła: dowodzi, że Warszawa w powieści nie jest tłem dekoracyjnym, lecz bezcennym dokumentem socjologicznym epoki wczesnego kapitalizmu."
          }
        ]
      },

      # 14. HENRYK SIENKIEWICZ - POTOP
      {
        "id": "sienkiewicz-potop",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Potop (fragmenty)",
        "autor": "Henryk Sienkiewicz",
        "epoka": "Pozytywizm",
        "gatunek": "Powieść historyczna „ku pokrzepieniu serc”",
        "motywy": ["metamorfoza moralna", "patriotyzm", "zdrada a rehabilitacja", "obrona Jasnej Góry", "pokrzepienie serc", "wojna ze Szwedami"],
        "synteza": "Dzieje Andrzeja Kmicica, który z samowolnego warchoła i mimowolnego poplecznika zdradzieckich Radziwiłłów przekształca się w ofiarnego obrońcę klasztoru na Jasnej Górze i bohatera narodowego odkupującego winy pod nazwiskiem Babinicza.",
        "tematyMaturalne": [
          "Motyw przemiany wewnętrznej bohatera i zadośćuczynienia za popełnione błędy.",
          "Literatura pisana 'ku pokrzepieniu serc' w czasach zaborów.",
          "Zdrada narodowa a wierność ojczyźnie w momentach próby historycznej."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historiograficzno-polemiczny",
            "zrodloZewnetrzne": "Polemika z krakowską szkołą historyczną (Józef Szujski, Michał Bobrzyński – „Dzieje Polski w zarysie”, 1879 r.)",
            "tytul": "Polemika Sienkiewicza z pesymizmem historycznym konserwatystów krakowskich",
            "opis": "Historycy krakowscy (stańczycy) głosili surową tezę, że Polska upadła na własne życzenie przez anarchię, warcholstwo szlachty i słabość władzy królewskiej. Sienkiewicz w 'Trylogii' podjął z nimi świadomą polemikę: ukazał, że choć Rzeczpospolita w 1655 r. była moralnie zepsuta i uległa Szwedom bez walki, to naród znalazł w sobie siłę moralną do odrodzenia i wypędzenia wroga.",
            "funkcja": "Tłumaczy nadrzędną ideę dzieła: pisarz stworzył mit wielkiego zwycięstwa militarnego, by przełamać narodowy kompleks klęski po powstaniu styczniowym i podtrzymać wiarę Polaków w odzyskanie suwerenności."
          },
          {
            "typ": "Kontekst źródłowy / literacki",
            "zrodloZewnetrzne": "Siedemnastowieczne „Pamiętniki” Jana Chryzostoma Paska (wydane drukiem przez Edwarda Raczyńskiego w 1836 r.)",
            "tytul": "Autentyczny język i mentalność sarmacka jako fundament stylizacji powieściowej",
            "opis": "Pamiętniki szlachcica Paska, uczestnika wojen ze Szwedami i wojsk Stefana Czarnieckiego, były dla Sienkiewicza głównym skarbcem językowym. Autor przejął od Paska składnię barokową, makaronizmy łacińskie, rubaszny humor szlachecki oraz typową dla epoki mentalność łączącą krewkość i pijaństwo z głęboką, rycerską pobożnością maryjną.",
            "funkcja": "Pozwala docenić mistrzostwo stylizacyjne Sienkiewicza: autor nie napisał współczesnej powieści w historycznym kostiumie, lecz wykreował autentyczny, pulsujący życiem świat sarmackiego XVII stulecia."
          },
          {
            "typ": "Kontekst historyczno-dyplomatyczny",
            "zrodloZewnetrzne": "Autentyczny traktat z Radnot (6 grudnia 1656 r.) – pierwszy historyczny projekt rozbioru Rzeczypospolitej",
            "tytul": "Geopolityczne zagrożenie rozbiorem państwa przez koalicję Karola Gustawa i Radziwiłłów",
            "opis": "W Radnot król Szwecji, elektor brandenburski, książę Siedmiogrodu Jerzy II Rakoczy, Bohdan Chmielnicki oraz Bogusław Radziwiłł podpisali porozumienie o całkowitym podziale ziem Rzeczypospolitej. Był to historyczny pierwowzór późniejszych rozbiorów z XVIII wieku. Zdrada Janusza i Bogusława Radziwiłłów w Kiejdanach miała realne podłoże w postaci chęci wykrojenia dla siebie suwerennego Księstwa Litewskiego pod protektoratem szwedzkim.",
            "funkcja": "Ukazuje historyczny ciężar zdrady, w którą uwikłał się Kmicic: sprawa nie dotyczyła prywatnych animozji magnackich, lecz śmiertelnego zagrożenia całkowitym wymazaniem Polski z mapy Europy."
          }
        ]
      },

      # 15. FIODOR DOSTOJEWSKI - ZBRODNIA I KARA
      {
        "id": "dostojewski-zbrodnia-i-kara",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Zbrodnia i kara",
        "autor": "Fiodor Dostojewski",
        "epoka": "Pozytywizm / Realizm psychologiczny",
        "gatunek": "Powieść psychologiczna / polifoniczna",
        "motywy": ["wina i odkupienie", "idea nadczłowieka", "radykalny nihilizm", "cierpienie jako oczyszczenie", "prostytucja i nędza", "moralne zmartwychwstanie"],
        "synteza": "Dramatyczne dzieje petersburskiego studenta Rodiona Raskolnikowa, który uwierzywszy w stworzoną przez siebie teorię o podziale ludzi na 'zwykłych' i 'niezwykłych' mających prawo deptać normy moralne, zabija starą lichwiarkę, po czym pod wpływem wyrzutów sumienia i miłości Soni wkracza na drogę chrześcijańskiej ekspiacji.",
        "tematyMaturalne": [
          "Czy cel uświęca środki? Moralna odpowiedzialność człowieka za głoszone teorie.",
          "Rola miłości i cierpienia w duchowym odrodzeniu zbrodniarza.",
          "Miasto jako przestrzeń deprawacji i nędzy psychicznej jednostki."
        ],
        "konteksty": [
          {
            "typ": "Kontekst filozoficzno-ideowy",
            "zrodloZewnetrzne": "Rosyjski radykalny nihilizm lat 60. XIX wieku: manifesty Dmitrija Pisariewa oraz powieść Nikołaja Czernyszewskiego „Co robić?” (1863 r.)",
            "tytul": "Krytyka utylitaryzmu, racjonalnego egoizmu i kultu 'napoleonizmu'",
            "opis": "W latach 60. XIX w. w Rosji narodził się ruch młodych radykałów (nihilistów), którzy odrzucali religię, duszę i tradycyjną moralność na rzecz czystego materializmu i utylitaryzmu (słynna teza, że zrobienie pary butów jest cenniejsze niż poezja Szekspira). Raskolnikow w swoim artykule 'O zbrodni' doprowadza te idee do logicznej skrajności: jeśli Boga nie ma, a celem jest szczęście milionów, jednostka wybitna (Napoleon) ma prawo usunąć ze świata 'szkodliwą wesz' (lichwiarkę).",
            "funkcja": "Kluczowy kontekst demaskujący niebezpieczeństwo ideologii: Dostojewski dowodzi, że próba zbudowania raju na ziemi za pomocą kalkulacji matematycznej i niemoralnych środków prowadzi wprost do tyranii i rozlewu niewinnej krwi."
          },
          {
            "typ": "Kontekst teologiczno-biblijny",
            "zrodloZewnetrzne": "Prawosławna teologia kenozy (pokornego uniżenia) oraz biblijna opowieść o wskrzeszeniu Łazarza z Ewangelii św. Jana",
            "tytul": "Chrystusowe zmartwychwstanie duchowe upadłego człowieka",
            "opis": "Centralną sceną duchową powieści jest nocne czytanie przez prostytutkę Sonię fragmentu Ewangelii o Łazarzu, który leżał w grobie cztery dni i cuchnął, nim Chrystus przywrócił go do życia. W tradycji prawosławnej kenoza oznacza dobrowolne uniżenie się i przyjęcie cierpienia na wzór Chrystusa jako jedyną drogę do przebóstwienia (theosis). Raskolnikow jest duchowym trupem w grobie własnej pychy, a Sonia – uosobieniem pokornej miłości niosącej zbawienie.",
            "funkcja": "Daje religijny klucz do odczytania epilogu na Syberii: morderca nie może odrodzić się przez spryt prawniczy czy racjonalizację winy, lecz jedynie przez pokorę, cierpienie i przyjęcie łaski Nowego Testamentu."
          },
          {
            "typ": "Kontekst biograficzno-psychologiczny",
            "zrodloZewnetrzne": "Aresztowanie Dostojewskiego w sprawie Koła Pietraszewskiego (1849 r.), sfingowana egzekucja i 4 lata katorgi w Omsku",
            "tytul": "Osobiste doświadczenie celi śmierci i katorgi syberyjskiej pisarza",
            "opis": "Dostojewski w młodości sam uległ fascynacji utopijnym socjalizmem. Aresztowany przez carską ochranę, stanął na placu Siemionowskim przed plutonem egzekucyjnym i w ostatniej sekundzie usłyszał o ułaskawieniu przez cara Mikołaja I. Następnie spędził 4 lata na ciężkiej katordze wśród najgorszych kryminalistów, gdzie jedyną lekturą, jaką mógł posiadać, była Ewangelia podarowana mu przez żony dekabrystów.",
            "funkcja": "Tłumaczy psychologiczny geniusz pisarza: Dostojewski nie opisywał katorgi Raskolnikowa z wyobraźni, lecz z własnego, bolesnego doświadczenia wewnętrznej przemiany od rewolucyjnego buntu do chrześcijańskiego przebaczenia."
          }
        ]
      },

      # 16. STANISŁAW WYSPIAŃSKI - WESELE
      {
        "id": "wyspianski-wesele",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Wesele",
        "autor": "Stanisław Wyspiański",
        "epoka": "Młoda Polska",
        "gatunek": "Dramat symboliczny / narodowy",
        "motywy": ["chłopomania", "niemoc narodowa", "symbole narodowe", "widma i zjawy", "chocholi taniec", "mit zjednoczenia klas"],
        "synteza": "Autentyczne wesele poety Lucjana Rydla z chłopką Jadwigą Mikołajczykówną w Bronowicach staje się dla Wyspiańskiego zwierciadłem polskiej niemocy: ujawnia nieprzekraczalną przepaść między inteligencją a chłopstwem, uwięzienie w mitach historycznych i niezdolność do podjęcia walki o niepodległość.",
        "tematyMaturalne": [
          "Diagnoza polskiego społeczeństwa na przełomie XIX i XX wieku.",
          "Rola mitów narodowych i symboli w kształtowaniu świadomości Polaków.",
          "Konfrontacja marzeń o wspólnym powstaniu z rzeczywistością wzajemnych uprzedzeń."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-traumatyczny",
            "zrodloZewnetrzne": "Rzeź galicyjska (rabacja chłopska pod przywództwem Jakuba Szeli z lutego 1846 r.)",
            "tytul": "Krwawa pamięć rzezi ziemiaństwa jako bariera w zjednoczeniu inteligencji z ludem",
            "opis": "W 1846 r. austriackie władze zaborcze sprowokowały chłopów do krwawego buntu przeciwko polskiej szlachcie planującej powstanie. Chłopi mordowali panów, palili dwory i zwozili odcięte głowy do cyrkułu w Tarnowie za austriackie guldeny. Pamięć tej hekatomby była wciąż żywa w Galicji w 1900 r. – zjawa Jakuba Szeli (Upiór) ukazuje się Dziadowi, a Pan Młody wspomina: 'Myśmy wszystko zapomnieli; ostatek krwią zachlany...'.",
            "funkcja": "Kluczowy fakt historyczny obnażający fałsz młodopolskiej chłopomanii: dowodzi, że zachwyt krakowskich poetów nad folklorem wsi był jedynie powierzchowną maską, pod którą krył się paniczny lęk przed ponownym chłopskim nożem i siekierą."
          },
          {
            "typ": "Kontekst plastyczno-malarski",
            "zrodloZewnetrzne": "Dzieła Jana Matejki („Stańczyk”, 1862 r.; „Wernyhora”, 1883 r.; „Kościuszko pod Racławicami”) oraz obrazy Jacka Malczewskiego („Melancholia”, „Błędne koło”)",
            "tytul": "Ożywające obrazy krakowskiego malarstwa historycznego i symbolicznego",
            "opis": "Wyspiański był wybitnym malarzem i uczniem Jana Matejki. W 'Weselu' postacie dramatu konfrontują się dosłownie z postaciami z matejkowskich płócien: Stańczyk z obrazu wręcza Dziennikarzowi Kaduceusz polski, wzywając do przebudzenia z narodowego uśpienia, a kozacki wieszcz Wernyhora powierza Gospodarzowi Złoty Róg. Finałowy taniec wokół chochoła przypomina z kolei malarski korowód postaci wirujących w letargu na płótnie 'Melancholia' Jacka Malczewskiego.",
            "funkcja": "Pozwala zanalizować dramat jako rozrachunek z kulturą wizualną Polaków: Wyspiański oskarża naród o to, że traktuje wielką historię wyłącznie jak muzealne obrazy na ścianie, nie potrafiąc przekształcić patriotycznych uniesień w realny czyn zbrojny."
          },
          {
            "typ": "Kontekst publicystyczno-polityczny",
            "zrodloZewnetrzne": "Publikacja konserwatystów krakowskich „Teka Stańczyka” (1869 r.) i spór o przyczyny upadku Polski",
            "tytul": "Stańczykowski lojalizm wobec zaborcy a młodopolski marazm ideowy",
            "opis": "Ugrupowanie 'stańczyków' (Józef Szujski, Stanisław Tarnowski) zwalczało tradycję powstań zbrojnych jako nieodpowiedzialne szaleństwo niszczące substancję narodową, głosząc ugodę z cesarzem Franciszkiem Józefem. Dziennikarz z 'Wesela' (jego pierwowzorem był Rudolf Starzewski, redaktor konserwatywnego 'Czasu') jest duchowym dzieckiem tej ideologii – dręczy go świadomość, że sącząc w społeczeństwo jad rezygnacji i lojalizmu, uśpił duszę narodu.",
            "funkcja": "Tłumaczy scenę spotkania Dziennikarza ze Stańczykiem: jest to głęboki polityczny wyrzut sumienia krakowskich elit konserwatywnych, które w imię spokoju i karier w monarchii austro-węgierskiej wyrzekły się marzeń o niepodległości."
          }
        ]
      },

      # 17. WŁADYSŁAW STANISŁAW REYMONT - CHŁOPI
      {
        "id": "reymont-chlopi",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Chłopi (fragmenty tomu I: Jesień)",
        "autor": "Władysław Stanisław Reymont",
        "epoka": "Młoda Polska",
        "gatunek": "Epopeja chłopska / powieść młodopolska",
        "motywy": ["wieś i ziemia jako sacrum", "czas mityczny i rytualny", "biologizm i namiętność", "moralność gromady", "izolacja jednostki (Jagna)"],
        "synteza": "Monumentalny obraz życia łowickiej wsi Lipce, ujęty w ramy czterech pór roku, gdzie losy Macieja Boryny, Antka i Jagny podporządkowane są rytmowi prac polowych, naturze, katolickiej liturgii oraz surowym prawom gromady.",
        "tematyMaturalne": [
          "Ziemia jako źródło bytu, godności i najgłębszych konfliktów ludzkich.",
          "Człowiek cząstką kosmosu – biologizm i fatalizm w życiu człowieka.",
          "Konflikt wybitnej, nieprzystosowanej jednostki z bezwzględnym prawem zbiorowości."
        ],
        "konteksty": [
          {
            "typ": "Kontekst antropologiczno-religioznawczy",
            "zrodloZewnetrzne": "Koncepcja czasu sakralnego (illud tempus) i cykliczności mitu Mircei Eliadego („Sacrum i profanum”, 1957 r.)",
            "tytul": "Mityzacja czasu: czas kołowy (kosmiczny) a czas linearny (historyczny)",
            "opis": "Mircea Eliade dowodził, że w tradycyjnych kulturach agrarnych czas nie płynie w sposób linearny od przeszłości do przyszłości, lecz odnawia się cyklicznie w wiecznym rytmie powrotu pór roku i obrzędów. W Lipcach wydarzenia historyczne prawie nie istnieją – życie wyznaczają odwieczne czynności: siew, wykopki, żniwa i święta liturgiczne (Dzień Zaduszny, Boże Narodzenie). Siewca w polu powtarza gest prastarego demiurga stwarzającego świat.",
            "funkcja": "Pozwala spojrzeć na powieść ponad poziomem realizmu etnograficznego: Reymont nie stworzył jedynie zapisu obyczajów łowickich, lecz uniwersalny mit kosmogoniczny o człowieku wtopionym w odwieczny ład przyrody."
          },
          {
            "typ": "Kontekst plastyczny / malarski",
            "zrodloZewnetrzne": "Malarstwo polskiego realizmu i nastrojowego pejzażu: Józef Chełmoński („Babie lato”, „Bociany”, „Krzyż w zadymce”)",
            "tytul": "Malarstwo Chełmońskiego jako wizualny odpowiednik opisów przyrody u Reymonta",
            "opis": "Reymont i Chełmoński znali się osobiście i czerpali z tego samego krajobrazu Mazowsza (okolic Łowicza). Scena, w której leżąca na miedzy Jagna wpatruje się w niebo i goni nitki babiego lata, jest niemal kadr po kadrze ożywieniem słynnego płótna 'Babie lato' (1875 r.). Podobnie opisy jesiennych błot, stad ptaków odlatujących na południe i surowej nędzy chłopskich chat korespondują z realizmem malarskim Chełmońskiego.",
            "funkcja": "Stanowi kontekst estetyczny ułatwiający analizę techniki pisarskiej Reymonta, łączącej młodopolski impresjonizm (barwy, światłocień, zapach ziemi) z naturalistyczną brutalnością praw biologii."
          },
          {
            "typ": "Kontekst społeczno-prawny",
            "zrodloZewnetrzne": "Carska reforma uwłaszczeniowa w Królestwie Polskim (ukaz cara Aleksandra II z 2 marca 1864 r.) i zjawisko serwitutów",
            "tytul": "Głód ziemi i walka o przetrwanie ekonomiczne na wsi polskiej po uwłaszczeniu",
            "opis": "Ukaz uwłaszczeniowy nadał chłopom ziemię na własność, ale stworzył też zarzewie krwawych konfliktów: rozdrobnienie gospodarstw między dzieci, problem komorników (ludzi bez własnej ziemi, jak Jagustynka) oraz spory z dworem o serwituty (prawo do wypasu bydła i zbierania chrustu w lasach dworskich). W świecie Lipiec brak ziemi oznaczał degradację do roli parobka i śmierć głodową pod kościelnym murem.",
            "funkcja": "Wyjaśnia bezwzględność zachowań Macieja Boryny i jego syna Antka: ich walka o morgi ziemi nie wynikała ze zwykłej chciwości, lecz z twardych realiów społecznych, w których morgi były jedyną rękojmią godności i biologicznego bytu rodziny."
          }
        ]
      },

      # 18. STEFAN ŻEROMSKI - PRZEDWIOŚNIE
      {
        "id": "zeromski-przedwiosnie",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Przedwiośnie",
        "autor": "Stefan Żeromski",
        "epoka": "Dwudziestolecie międzywojenne",
        "gatunek": "Powieść polityczno-społeczna",
        "motywy": ["rewolucja bolszewicka", "mit szklanych domów", "odbudowa niepodległej Polski", "nędza proletariatu", "wojna 1920 r.", "poszukiwanie drogi dla ojczyzny"],
        "synteza": "Dojrzewanie Cezarego Baryki na tle wstrząsów epoki: od zbrodni rewolucji w naftowym Baku, przez wojnę polsko-bolszewicką i sielankę ziemiańską w Nawłoci, po konfrontację z nędzą warszawskiego proletariatu i dyskusję o przyszłości odrodzonej Rzeczypospolitej.",
        "tematyMaturalne": [
          "Entuzjazm i gorycz odzyskanej niepodległości – Polska marzeń a Polska rzeczywista.",
          "Rewolucja społeczna: nadzieja na sprawiedliwość czy krwawa zagłada cywilizacji?",
          "Mit szklanych domów jako symbol tęsknoty za nowoczesnym, sprawiedliwym państwem."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-geopolityczny",
            "zrodloZewnetrzne": "Rewolucja bolszewicka w Rosji, walki w Baku (rzeź ormiańsko-azerska w 1918 r.) oraz wojna polsko-bolszewicka i Bitwa Warszawska 1920 r.",
            "tytul": "Konfrontacja z autentycznym bestialstwem bolszewizmu i obrona niepodległości",
            "opis": "Baryka w Baku obserwuje rozpad struktur państwowych: bezprawie, głód, grabieże i masowe mordy na ulicach dokonywane w imię rewolucyjnych haseł. Gdy trafia do Polski, zaciąga się do wojska i bierze udział w wojnie 1920 r., walcząc przeciwko tej samej armii bolszewickiej, której terror widział na Kaukazie.",
            "funkcja": "Tłumaczy sceptycyzm Cezarego wobec komunistycznych haseł głoszonych później w Warszawie przez Antoniego Lulka: Baryka znał rewolucję z autopsji i wiedział, że przynosi ona nie wyzwolenie, lecz powszechny terror, nędzę i zezwierzęcenie człowieka."
          },
          {
            "typ": "Kontekst ekonomiczno-państwowy",
            "zrodloZewnetrzne": "Reformy rządu Władysława Grabskiego (1924 r.) – powołanie Banku Polskiego, reforma walutowa (wprowadzenie złotego) i stabilizacja skarbu",
            "tytul": "Spór o drogi reform gospodarczych II Rzeczypospolitej (program Gajowca)",
            "opis": "Powieść ukazała się w 1924 r., w momencie gdy Polska zmagała się z gigantyczną hiperinflacją marki polskiej i zapaścią budżetową po zniszczeniach wojennych. Postać Szymona Gajowca reprezentuje autentyczny obóz państwowotwórczy skupiony wokół premiera Władysława Grabskiego: głosi potrzebę powolnych, ewolucyjnych reform monetarnych, edukacji rolnej i tworzenia armii, odrzucając rewolucyjną drogę na skróty.",
            "funkcja": "Pozwala odczytać utwór jako wielką debatę politologiczną epoki: powieść rejestruje autentyczne programy ratowania młodego państwa polskiego przed zapaścią ekonomiczną i buntem zdesperowanych mas."
          },
          {
            "typ": "Kontekst publicystyczno-biograficzny",
            "zrodloZewnetrzne": "Publicystyka Stefana Żeromskiego: esej „Snobizm i postęp” (1923 r.) oraz artykuły pisarza o zapaści moralnej elit II RP",
            "tytul": "Osobista gorycz „sumienia polskiej literatury” po pierwszych latach niepodległości",
            "opis": "Żeromski, który przez dziesięciolecia zaborów pisał o marzeniu o wolnej Polsce ('Popioły', 'Ludzie bezdomni'), po 1918 r. przeżył głębokie rozczarowanie. Zamiast 'szklanych domów' ujrzał korupcję, nędzę w dzielnicach żydowskich i robotniczych (opis warszawskich Nalewek i biedy na Woli), analfabetyzm i zbrodniczy zamach na prezydenta Gabriela Narutowicza w 1922 r.",
            "funkcja": "Wyjaśnia dramatyczną puentę utworu: marsz Baryki na Belweder u boku komunistów nie był apoteozą marksizmu, lecz rozpaczliwym krzykiem ostrzegawczym Żeromskiego pod adresem rządzących, że jeśli państwo nie przeprowadzi natychmiastowych reform socjalnych, zepchnie zdesperowanych ludzi w objęcia rewolucji."
          }
        ]
      },

      # 19. WITOLD GOMBROWICZ - FERDYDURKE
      {
        "id": "gombrowicz-ferdydurke",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Ferdydurke (fragmenty)",
        "autor": "Witold Gombrowicz",
        "epoka": "Dwudziestolecie międzywojenne",
        "gatunek": "Powieść awangardowa / groteskowa",
        "motywy": ["Forma", "Gęba i Pupa", "upupienie (infantylizacja)", "Inny jako źródło zniewolenia", "parodia instytucji społecznych", "groteska"],
        "synteza": "Groteskowa historia trzydziestoletniego Józia Kowalskiego, który zostaje porwany przez profesora Pimkę do szkoły i poddany przymusowemu upupieniu, ukazująca bezradność człowieka uwikłanego w narzucane przez innych role społeczne.",
        "tematyMaturalne": [
          "Człowiek w niewoli formy – czy istnieje ucieczka przed 'Gębą'?",
          "Krytyka skostniałych instytucji społecznych (szkoła, moderna, tradycjonalizm szlachecki).",
          "Groteska i absurd jako nowatorskie narzędzia badania kondycji ludzkiej."
        ],
        "konteksty": [
          {
            "typ": "Kontekst filozoficzno-egzystencjalny",
            "zrodloZewnetrzne": "Filozofia egzystencjalna Jeana-Paula Sartre’a („Byt i nicość”, 1943 r.) – teoria spojrzenia Innego i uprzedmiotowienia",
            "tytul": "Człowiek stwarzany przez drugiego człowieka – kategoria „Innego”",
            "opis": "Sartre sformułował słynną tezę: 'Piekło to inni' – człowiek w samotności czuje się wolny, lecz w chwili gdy pada na niego spojrzenie drugiego człowieka, zostaje zredukowany do przedmiotu i określonej roli. Gombrowicz niezależnie od francuskich egzystencjalistów doszedł do identycznego wniosku: człowiek nie jest samouzasadniającym się bytem, lecz nieustannie podlega 'przyprawianiu Gęby' w kontakcie międzyludzkim (tzw. kościół międzyludzki).",
            "funkcja": "Dostarcza fundamentu filozoficznego do odczytania powieści: dowodzi, że kategorie 'Pupy' i 'Gęby' to nie dziecinne żarty, lecz wybitna koncepcja ontologiczna demaskująca niemożność osiągnięcia czystej autentyczności w relacjach z ludźmi."
          },
          {
            "typ": "Kontekst psychologiczno-psychoanalityczny",
            "zrodloZewnetrzne": "Psychoanaliza Zygmunta Freuda: teoria mechanizmów obronnych, regresji psychicznej i opresyjności kultury („Kultura jako źródło cierpień”, 1930 r.)",
            "tytul": "Przymusowa infantylizacja i stłumienie popędów przez opresję kulturową",
            "opis": "Freud wykazał, że kultura i edukacja działają poprzez represję naturalnych popędów człowieka, zmuszając go do konformizmu pod groźbą wykluczenia ze stada. W szkole dyrektora Piórkowskiego profesor Pimko stosuje mechanizm przymusowej infantylizacji ('upupienia'): dorośli młodzieńcy są celowo traktowani jak niewinne dzieciątka, aby stłumić w nich wszelką samodzielność myślenia i bunty dojrzałości.",
            "funkcja": "Pomaga zanalizować scenę pojedynku na miny Miętusa z Syfonem oraz lekcję języka polskiego z profesorem Bladaczką ('Słowacki zachwyca, bo wielkim poetą był') jako satyrę na system edukacyjny kastrujący jednostkę z krytycyzmu."
          },
          {
            "typ": "Kontekst biograficzno-literacki",
            "zrodloZewnetrzne": "Debiut literacki Gombrowicza „Pamiętnik z okresu dojrzewania” (1933 r.) i ataki krytyki literackiej zarzucające autorowi niedojrzałość",
            "tytul": "Autorska polemika Gombrowicza z protekcjonalizmem polskich krytyków literackich",
            "opis": "Gdy Gombrowicz wydał swój debiutancki tom opowiadań, konserwatywni krytycy potraktowali go jak niedojrzałego młodzika, który 'jeszcze musi dorosnąć do wielkiej literatury'. Pisarza doprowadziła do szału ta protekcjonalna poza mentorów literackich. Odpowiedzią była 'Ferdydurke', gdzie postać profesora Pimki ucieleśnia właśnie takiego wszechwiedzącego, zramolałego belfra, który każdemu młodemu twórcy na siłę doprawia gębę pensjonarza.",
            "funkcja": "Rzuca światło na genezę dzieła: ukazuje utwór jako prywatną, genialną zemstę pisarza na protekcjonalnym środowisku literackim II RP."
          }
        ]
      },

      # 20. TADEUSZ BOROWSKI - PROSZĘ PAŃSTWA DO GAZU
      {
        "id": "borowski-opowiadania",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Proszę państwa do gazu (z tomu „Pożegnanie z Marią”)",
        "autor": "Tadeusz Borowski",
        "epoka": "Wojna i okupacja / Współczesność",
        "gatunek": "Opowiadanie obozowe (literatura lagrowa)",
        "motywy": ["człowiek zlagrowany", "Auschwitz-Birkenau", "behawioralna technika narracji", "przetrwanie za cenę zasad", "odczłowieczenie", "moralność obozowa"],
        "synteza": "Drastyczny opis rozładunku transportu ludzi na rampie kolejowej w Brzezince, ukazany z perspektywy więźnia funkcyjnego z komanda Kanady (Tadka), zmuszonego do odbierania dobytku ofiarom prowadzonym do komór gazowych w imię przedłużenia własnego biologicznego bytu.",
        "tematyMaturalne": [
          "Człowiek zlagrowany – granice kompromisu moralnego w obliczu totalitarnego terroru.",
          "Behawiorystyczna metoda ukazywania Zagłady w literaturze wojennej.",
          "Upadek europejskiego humanizmu i kultury śródziemnomorskiej w obozach koncentracyjnych."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-obozowy",
            "zrodloZewnetrzne": "Realia funkcjonowania niemieckiego nazistowskiego obozu koncentracyjnego i zagłady Auschwitz-Birkenau: komando 'Kanada' i mechanizm selekcji",
            "tytul": "Przemysłowy charakter Zagłady i wprzęgnięcie ofiar w aparat eksterminacji",
            "opis": "W Auschwitz-Birkenau hitlerowcy stworzyli unikalny, przemysłowy system zagłady. Częścią tego mechanizmu było zmuszanie starych więźniów (komando 'Aufräumungskommando' zwane Kanadą) do rozładowywania bydlęcych wagonów, sortowania zrabowanego mienia i kierowania nowo przybyłych prosto na śmierć. Więźniowie ci zyskiwali lepsze racje żywnościowe i ubrania, lecz stawali się mimowolnymi trybikami w machinie ludobójstwa.",
            "funkcja": "Stanowi dokumentalną podstawę opowiadania: pozwala zrozumieć, że w świecie lagru nie było miejsca na czarno-białe podziały; oprawcy stworzyli system, w którym ofiara stawała się współwinną morderstwa, aby przeżyć kolejny dzień."
          },
          {
            "typ": "Kontekst psychologiczno-metodologiczny",
            "zrodloZewnetrzne": "Koncepcja behawioryzmu w psychologii (John B. Watson) zaadaptowana do teorii narracji literackiej",
            "tytul": "Narracyjny behawioryzm jako metoda rejestracji nagich faktów i odruchów fizjologicznych",
            "opis": "Behawioryzm w nauce odrzucał badanie subiektywnych stanów wewnętrznych i duszy, skupiając się wyłącznie na rejestracji zewnętrznych bodźców i reakcji organizmu. Borowski dokonał rewolucji stylistycznej: usunął z narracji komentarz moralizatorski, patos i psychologizowanie na rzecz suchego, precyzyjnego zapisu czynności fizycznych: potu, pragnienia, wyrywania walizek, krzyku, wymiotów i mechanicznego ładowania ciał na ciężarówki.",
            "funkcja": "Tłumaczy piorunującą siłę oddziaływania prozy Borowskiego: brak oburzenia narratora i jego chłodny, znieczulony ton potęguje grozę sytuacji i uniemożliwia czytelnikowi ucieczkę w łatwe, uspokajające moralizatorstwo."
          },
          {
            "typ": "Kontekst krytycznoliteracki / powojenny",
            "zrodloZewnetrzne": "Powojenna debata o amoralizmie literatury oświęcimskiej: gwałtowny atak pisarki katolickiej Zofii Kossak-Szczuckiej na Tadeusza Borowskiego",
            "tytul": "Oskarżenia o nihilizm i cynizm a próba ocalenia bezwzględnej prawdy o obozie",
            "opis": "Po opublikowaniu opowiadań Zofia Kossak-Szczucka (sama była więźniarka Auschwitz) oskarżyła Borowskiego o szerzenie nihilizmu, cynizm i deptanie godności więźniów, którzy jej zdaniem zachowywali w obozie wiarę i solidarność. Borowski odpowiadał, że pisanie o Auschwitz wzniosłym językiem męczeństwa jest zakłamywaniem prawdy: w komorach gazowych nie ginęli antyczni herosi, lecz oszukani, odarci z człowieczeństwa ludzie, którzy w walce o chleb potrafili wydrzeć go z rąk matki.",
            "funkcja": "Ukazuje fundamentalny powojenny spór o to, jak mówić o Holokauście: czy przez pryzmat heroizacji i martyrologii, czy przez bezwzględny, bolesny realizm odsłaniający najciemniejszą prawdę o zezwierzęceniu człowieka w warunkach granicznych."
          }
        ]
      },

      # 21. GUSTAW HERLING-GRUDZIŃSKI - INNY ŚWIAT
      {
        "id": "herling-inny-swiat",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Inny świat (fragmenty)",
        "autor": "Gustaw Herling-Grudziński",
        "epoka": "Wojna i okupacja / Współczesność",
        "gatunek": "Pamiętnik / proza dokumentarna (literatura łagrowa)",
        "motywy": ["Gułag", "sowiecki totalitaryzm", "próba człowieczeństwa", "głód jako narzędzie tortur", "ocalenie godności", "epilog rzymski i problem przebaczenia"],
        "synteza": "Zapis dwuletniego pobytu autora w sowieckim łagrze w Jercewie pod Archangielskiem, dokumentujący nieludzki mechanizm Gułagu niszczącego duszę człowieka głodem i pracą ponad siły, a zarazem heroiczne próby ocalenia resztek moralności.",
        "tematyMaturalne": [
          "Czy człowiek w warunkach nieludzkich może ocalić człowieczeństwo i godność?",
          "System sowieckiego łagru a obóz nazistowski – techniki łamania sumienia.",
          "Cena powrotu do normalnego świata i granice przebaczenia (epilog rzymski)."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-polityczny",
            "zrodloZewnetrzne": "Sowiecki system Gułagu (Gławnoje Uprawlenije Łagieriej), rozkazy NKWD i masowe represje wobec Polaków po 17 września 1939 r.",
            "tytul": "Funkcjonowanie Gułagu jako niewolniczego systemu gospodarczego ZSRR",
            "opis": "Herling-Grudziński został aresztowany przez NKWD w Grodnie w 1940 r. pod absurdalnym zarzutem szpiegostwa na rzecz Niemiec i skazany na 5 lat łagru. Książka obnażała prawdę, którą ZSRR ukrywał przed światem: sowieckie obozy nie były miejscami reedukacji, lecz potężnym imperium niewolniczej pracy leśnej i górniczej, w którym więźnia (zek) eksploatowano głodowymi normami wydajności aż do całkowitego wycieńczenia biologicznego ('dokurzacze').",
            "funkcja": "Stanowi bezcenny dokument historyczny demaskujący zbrodnie stalinizmu; pozwala wykazać, że łagier był zorganizowaną machiną niszczenia nie tylko ciała, ale przede wszystkim ludzkiego poczucia prawdy i tożsamości."
          },
          {
            "typ": "Kontekst literacko-filozoficzny",
            "zrodloZewnetrzne": "Dzieło Fiodora Dostojewskiego „Wspomnienia z domu umarłych” (1862 r.) jako bezpośrednie motto utworu",
            "tytul": "Dostojewski jako duchowy przewodnik po piekle carskiej i sowieckiej katorgi",
            "opis": "Herling zaczerpnął motto z książki Dostojewskiego o carskiej katordze w Omsku: 'Tu otwierał się świat odrębny, do niczego niepodobny...'. W Jercewie zniszczony egzemplarz tej książki krążył wśród więźniów jak relikwia (scena z Natalią Lwowną). Herling udowadnia, że sowiecki Gułag był potwornym udoskonaleniem metod carskich: o ile u Dostojewskiego przestępcy mieli jeszcze resztki sumienia i Boga, o tyle system komunistyczny dążył do całkowitego wykorzenienia moralności.",
            "funkcja": "Tworzy ramę kompozycyjną i filozoficzną: wskazuje, że 'Inny świat' jest kontynuacją wielkiej literatury męczeństwa badającej granice ludzkiej duszy w starciu z bezdusznym aparatem państwa."
          },
          {
            "typ": "Kontekst etyczno-polemiczny",
            "zrodloZewnetrzne": "Polemika z koncepcją 'człowieka zlagrowanego' Tadeusza Borowskiego oraz zatajanie prawdy o Gułagu przez zachodnią lewicę (np. Jean-Paul Sartre)",
            "tytul": "Wiara w ocalenie godności w warunkach ekstremalnych a amoralizm",
            "opis": "Herling formułuje słynną maksymę: 'Człowiek jest ludzki w ludzkich warunkach i głupotą jest sądzić go według norm stworzonych w warunkach normalnych', lecz w przeciwieństwie do Borowskiego nie popada w nihilizm. Ukazuje bohaterów, którzy potrafili powiedzieć 'nie' oprawcom (Kostylew opalający rękę w ogniu, by nie pracować dla sowietów; inżynier Polenko). Ponadto książka przez lata nie mogła ukazać się we Francji, ponieważ zachodni intelektualiści sympatyzujący z komunizmem (Sartre) nie chcieli wierzyć w zbrodnie Stalina.",
            "funkcja": "Pozwala na głębokie zestawienie literatury łagrowej i lagrowej: dowodzi, że wedle Herlinga nawet na dnie piekła człowiek posiada iskrę wolności, za którą może oddać życie, byle nie ulec całkowitej deprawacji."
          }
        ]
      },

      # 22. HANNA KRALL - ZDĄŻYĆ PRZED PANEM BOGIEM
      {
        "id": "krall-zdazyc-przed-panem-bogiem",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Zdążyć przed Panem Bogiem",
        "autor": "Hanna Krall",
        "epoka": "Współczesność",
        "gatunek": "Reportaż biograficzny / literatura faktu",
        "motywy": ["powstanie w getcie warszawskim", "Umschlagplatz", "pamięć Zagłady", "deheroizacja", "kardiochirurgia", "wyścig ze śmiercią"],
        "synteza": "Wywiad-rzeka z Markiem Edelmanem, jedynym ocalałym przywódcą powstania w getcie warszawskim, zestawiający dramatyczne wspomnienia z Umschlagplatzu i walk ŻOB w 1943 r. z jego powojenną pracą wybitnego kardiochirurga ratującego ludzkie serca.",
        "tematyMaturalne": [
          "Różne wymiary bohaterstwa – śmierć z bronią w ręku a ratowanie jednostkowego życia.",
          "Deheroizacja mitu wojennego w relacji naocznego świadka historii.",
          "Etyczny obowiązek ocalenia pamięci o bezimiennych ofiarach Zagłady."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczny / dokumentalny",
            "zrodloZewnetrzne": "Wielka akcja likwidacyjna getta warszawskiego (Grossaktion Warschau, lipiec-wrzesień 1942 r.) oraz powstanie w kwietniu 1943 r.",
            "tytul": "Wywózka 300 tysięcy Żydów do komór gazowych Treblinki i zryw ŻOB",
            "opis": "Latem 1942 r. Niemcy wywieźli z Umschlagplatzu do obozu zagłady w Treblince ponad 300 tysięcy mieszkańców getta. Edelman stał przy bramie jako goniec szpitalny, widząc codziennie tysiące ludzi prowadzonych na śmierć. Kiedy w kwietniu 1943 r. Żydowska Organizacja Bojowa chwyciła za broń, celem nie było zwycięstwo militarne, bo to było niemożliwe, lecz wybór sposobu umierania: 'Chodziło tylko o wybór sposobu umierania. Chodziło o to, żeby nie dać się zarżnąć'.",
            "funkcja": "Stanowi konieczny kontekst faktograficzny: pozwala zrozumieć tragiczną motywację powstańców z getta, dla których walka zbrojna była wyłącznie manifestacją godności i wolnej woli w obliczu pewnej zagłady."
          },
          {
            "typ": "Kontekst medyczno-biograficzny",
            "zrodloZewnetrzne": "Rozwój powojennej kardiochirurgii w Polsce – pionierskie operacje zawałów serca prof. Jana Molla w Łodzi",
            "tytul": "Pojedynek z Bogiem przy stole operacyjnym jako przedłużenie misji z getta",
            "opis": "Po wojnie Marek Edelman został kardiochirurgiem i pracował w klinice prof. Molla, biorąc udział w pierwszych w Polsce nowatorskich operacjach na otwartym sercu w stanie ostrego zawału. Swoją pracę lekarską traktował w sposób metafizyczny: jako kontynuację roli z Umschlagplatzu. Twierdził, że Pan Bóg chce zdmuchnąć płomień życia pacjenta, a jego zadaniem jako lekarza jest wyprzedzić Boga i choć na chwilę osłonić ten płomień.",
            "funkcja": "Łączy dwie płaszczyzny czasowe utworu i definiuje humanistyczne przesłanie Edelmana: ratowanie jednego ludzkiego życia na sali operacyjnej ma dokładnie taką samą wartość jak walka z bronią na barykadzie w getcie."
          },
          {
            "typ": "Kontekst teoretycznoliteracki / reporterski",
            "zrodloZewnetrzne": "Polska szkoła reportażu i koncepcja deheroizacji historii Hanny Krall",
            "tytul": "Odrzucenie patosu i koturnowości na rzecz nagiej prawdy o człowieku",
            "opis": "Edelman w rozmowie z Krall świadomie niszczy spiżowy, pomnikowy mit powstania. Mówi prostym, niemal oschłym językiem, opowiadając o rzeczach przyziemnych: o wszołowatym głodzie, o tym, że Mordechaj Anielewicz pomalował sobie czapkę na żółto ze snobizmu, a dziewczyna oddała się za bochenek chleba. Krall stosuje nielinearny montaż scen i technikę zbliżeń detalu (żółte żonkile, oczy pacjenta, numerek na Umschlagplatzu).",
            "funkcja": "Pozwala przeanalizować reportaż jako bunt przeciwko patriotycznemu kiczowi i mitomaństwu: pokazuje, że naga prawda o ludzkim strachu i słabości jest znacznie bardziej wstrząsająca i prawdziwa niż koturnowe legendy."
          }
        ]
      },

      # 23. ALBERT CAMUS - DŻUMA
      {
        "id": "camus-dzuma",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Dżuma",
        "autor": "Albert Camus",
        "epoka": "Współczesność",
        "gatunek": "Powieść parabola (alegoryczna)",
        "motywy": ["epidemia jako metafora zła", "absurd istnienia", "heroizm laicki", "solidarność i przyzwoitość", "cierpienie niewinnych dzieci", "teodycea"],
        "synteza": "Zamknięcie algierskiego miasta Oran z powodu wybuchu epidemii dżumy staje się uniwersalną przypowieścią o zmaganiu człowieka z niszczącą siłą zła, bezsensem cierpienia i koniecznością solidarnego oporu ucieleśnionego przez doktora Bernarda Rieux.",
        "tematyMaturalne": [
          "Różne postawy człowieka wobec zagrożenia, cierpienia i zła.",
          "Heroizm laicki – moralność i odpowiedzialność za innych w świecie bez Boga.",
          "Dżuma jako uniwersalna parabola zła biologicznego, metafizycznego i politycznego."
        ],
        "konteksty": [
          {
            "typ": "Kontekst filozoficzno-etyczny",
            "zrodloZewnetrzne": "Traktaty filozoficzne Alberta Camusa: esej „Mit Syzyfa” (1942 r.) oraz „Człowiek zbuntowany” (1951 r.)",
            "tytul": "Etyka buntu i koncepcja laickiej przyzwoitości doktora Rieux",
            "opis": "W filozofii Camusa świat jest z natury absurdalny i obojętny na los ludzi, a zło (bakcyl dżumy) nigdy nie ginie na zawsze. Jedyną godną odpowiedzią człowieka na absurd nie jest jednak rezygnacja, lecz solidarny bunt. Doktor Rieux nie uważa się za bohatera ani świętego – twierdzi po prostu, że jedynym sposobem walki z dżumą jest 'uczciwość', która polega na wykonywaniu swego zawodu i ratowaniu chorych bez oczekiwania na zbawienie wieczne.",
            "funkcja": "Stanowi klucz filozoficzny do powieści: pozwala zdefiniować pojęcie laickiego humanizmu – człowiek musi pomagać innym i sprzeciwiać się złu nie z lęku przed piekłem czy dla nagrody w niebie, lecz z czystego szacunku dla ludzkiej godności."
          },
          {
            "typ": "Kontekst historyczno-alegoryczny",
            "zrodloZewnetrzne": "Doświadczenie II wojny światowej: nazistowska okupacja Francji, 'brunatna zaraza' i udział Camusa w podziemnym piśmie ruchu oporu „Combat”",
            "tytul": "Dżuma jako alegoria faszyzmu, okupacji hitlerowskiej i obozów zagłady",
            "opis": "Powieść powstała tuż po zakończeniu II wojny światowej. Kordon sanitarny wokół Oranu, odcięcie od bliskich, godziny policyjne, masowe groby i palenie ciał w krematoriach były bezpośrednią, czytelną dla współczesnych aluzją do okupacji Francji przez wojska III Rzeszy i zbrodni w obozach koncentracyjnych. Sformowane przez Jeana Tarrou ochotnicze formacje sanitarne symbolizowały francuski ruch oporu (Résistance).",
            "funkcja": "Daje historyczny klucz interpretacyjny do paraboli: uzasadnia ostrzeżenie z finału powieści, że bakcyl dżumy nigdy nie umiera i może ponownie obudzić swoje szczury w jakimś szczęśliwym mieście, gdy społeczeństwa ulegną uśpieniu."
          },
          {
            "typ": "Kontekst teologiczno-religijny",
            "zrodloZewnetrzne": "Filozoficzny problem teodycei i motyw cierpienia niewinnych dzieci w „Braciach Karamazow” Fiodora Dostojewskiego",
            "tytul": "Kryzys wiary wobec niewytłumaczalnego cierpienia dziecka (spór Rieux z o. Paneloux)",
            "opis": "Jezuita Paneloux w pierwszym kazaniu grzmi, że dżuma jest sprawiedliwą karą Bożą za grzechy mieszkańców. Przełomem jest jednak wstrząsająca scena powolnej agonii małego, niewinnego synka sędziego Othona. Doktor Rieux, widząc cierpienie dziecka, rzuca zakonnikowi w twarz: 'To przynajmniej było niewinne, wie pan o tym doskonale!'. W drugim kazaniu ojciec Paneloux nie potrafi już racjonalizować zła i przyznaje, że wobec cierpienia dziecka rozum staje bezradny, a wierzącemu pozostaje tylko dramatyczny akt ślepej wiary wbrew logice.",
            "funkcja": "Ukazuje fundamentalny problem filozofii religii: konfrontuje chrześcijańską teodyceę z laickim humanizmem i dowodzi, że żadna konstrukcja teologiczna nie potrafi w pełni usprawiedliwić łez cierpiącego dziecka."
          }
        ]
      },

      # 24. GEORGE ORWELL - ROK 1984
      {
        "id": "orwell-1984",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Rok 1984",
        "autor": "George Orwell",
        "epoka": "Współczesność",
        "gatunek": "Dystopia (antyutopia polityczna)",
        "motywy": ["totalitaryzm", "inwigilacja (Wielki Brat)", "nowomowa (newspeak)", "fałszowanie przeszłości", "zniewolenie umysłu (dwumyślenie)", "tortury w Ministerstwie Miłości"],
        "synteza": "Przerażająca wizja totalitarnego superpaństwa Oceania, rządzonego przez wszechwładną Partię Angsocu i Wielkiego Brata, gdzie jednostka (Winston Smith) zostaje całkowicie pozbawiona prywatności, wolności myśli oraz tożsamości poprzez inwigilację, nowomowę i fizyczne złamanie.",
        "tematyMaturalne": [
          "Mechanizmy sprawowania władzy absolutnej i zniewolenia jednostki w państwie totalitarnym.",
          "Język jako narzędzie propagandy, dezinformacji i kontroli umysłów (nowomowa).",
          "Fałszowanie historii i pamięci w walce o władzę nad przyszłością."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-politologiczny",
            "zrodloZewnetrzne": "Zbrodnie stalinizmu w ZSRR: wielkie czystki lat 30., procesy pokazowe w Moskwie, kult jednostki Stalina i pakt Ribbentrop-Mołotow (1939 r.)",
            "tytul": "Autentyczne techniki terroru stalinowskiego jako fundament konstrukcji Oceanii",
            "opis": "Orwell napisał powieść w 1948 r. (tytuł powstał przez przestawienie cyfr), korzystając z obserwacji realnych reżimów. Wielki Brat nosił rysy Józefa Stalina, wróg ludu Emmanuel Goldstein uosabiał Lwa Trockiego, a nagłe zmiany sojuszy wojennych Oceanii z Eurazją i Wschódazją dokładnie kopiowały pakt Stalina z Hitlerem z 1939 r., kiedy to z dnia na dzień nazistowskie Niemcy przestały być w radzieckiej prasie wrogiem, a stały się 'sojusznikiem'.",
            "funkcja": "Udowadnia, że powieść Orwella nie jest fantastyką, lecz precyzyjną wiwisekcją politologiczną: obnaża mechanizmy, za pomocą których autentyczne reżimy XX wieku zdołały sprawować pełną kontrolę nad milionami obywateli."
          },
          {
            "typ": "Kontekst lingwistyczny / naukowy",
            "zrodloZewnetrzne": "Hipoteza relatywizmu językowego Edwarda Sapira i Benjamina Lee Whorfa (determinizm językowy)",
            "tytul": "Determinizm językowy a orwellowska koncepcja nowomowy (Newspeak)",
            "opis": "Hipoteza Sapira-Whorfa zakłada, że struktura języka, jakim się posługujemy, bezpośrednio determinuje i ogranicza nasze procesy myślowe i postrzeganie świata. Orwell przeniósł tę tezę na grunt inżynierii totalitarnej: celem Nowomowy było coroczne niszczenie słów. Jeśli z języka zniknie słowo oznaczające 'wolność' czy 'bunt', myśl o rebelii stanie się fizycznie i pojęciowo niemożliwa do sformułowania w mózgu człowieka.",
            "funkcja": "Kluczowy kontekst lingwistyczny: demaskuje rolę manipulacji semantycznej w propagandzie i dowodzi, że walka o czystość języka i wolność słowa jest warunkiem koniecznym zachowania wolności politycznej."
          },
          {
            "typ": "Kontekst literacki / tradycja antyutopii",
            "zrodloZewnetrzne": "Klasyka literatury dystopijnej: powieść Jewgienija Zamiatina „My” (1920 r.) oraz Aldousa Huxleya „Nowy wspaniały świat” (1932 r.)",
            "tytul": "Model totalitaryzmu przemocowego (Orwell) a totalitaryzm konsumpcyjny (Huxley)",
            "opis": "U Huxleya ludzie są zniewoleni za pomocą przyjemności, wolnego seksu, rozrywki i narkotyku soma, dobrowolnie rezygnując z wolności. Orwell, nawiązując do zakazanego w ZSRR dzieła Zamiatina 'My', wybrał drogę przeciwną: w Oceanii Partia rządzi za pomocą czystego bólu, strachu, ciągłej biedy i nienawiści ('Jeżeli chcesz wiedzieć, czym będzie przyszłość, wyobraź sobie but depczący ludzką twarz – wiecznie').",
            "funkcja": "Umożliwia zestawienie dwóch przeciwstawnych, przenikliwych modeli zniewolenia ludzkości: przez konsumpcyjną apatię i przyjemność (Huxley) kontra przez terror policyjny, nędzę i strach (Orwell)."
          }
        ]
      },

      # 25. SŁAWOMIR MROŻEK - TANGO
      {
        "id": "mrozek-tango",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Tango",
        "autor": "Sławomir Mrożek",
        "epoka": "Współczesność",
        "gatunek": "Dramat groteskowy / teatr absurdu",
        "motywy": ["bunt przeciw anarchii", "rozpad tradycyjnej rodziny", "kryzys wartości", "triumf brutalnej siły (Edek)", "chocholi taniec a tango", "groteska"],
        "synteza": "Dramat o rodzinie Stomila i Eleonory, która zburzyła wszelkie normy moralne w imię absolutnej wolności, oraz ich synu Arturze, który paradoksalnie buntuje się przeciw chaosowi, próbując przywrócić formę i tradycję. Jego klęska otwiera drogę do krwawej dyktatury prymitywnego chama Edka.",
        "tematyMaturalne": [
          "Bunt odwrócony – młodzi w obronie tradycji i zasad przeciw anarchii rodziców.",
          "Gdy elity abdykują z kultury, do władzy dochodzi brutalna siła fizyczna.",
          "Groteskowy obraz rodziny jako diagnoza kryzysu cywilizacji europejskiej."
        ],
        "konteksty": [
          {
            "typ": "Kontekst socjologiczno-kulturowy",
            "zrodloZewnetrzne": "Rewolucja obyczajowa lat 60. XX wieku w Europie Zachodniej, ruch hippisowski i załamanie tradycyjnych autorytetów",
            "tytul": "Pułapka permisywizmu moralnego i paradoks buntu w świecie bez zakazów",
            "opis": "Mrożek w 1964 r. genialnie przewidział kryzys kulturowy buntu młodzieżowego na Zachodzie (maj 1968 r.). Pokolenie Stomila i Eleonory obaliło Kościół, małżeństwo, kindersztubę i normy obyczajowe, chodząc w piżamach i uprawiając wolną miłość. Artur staje przed dramatycznym dylematem: jeśli wszystko wolno, bunt staje się niemożliwy. Pełna wolność bez granic i norm zamienia się w anarchię, nudę i duchową pustkę.",
            "funkcja": "Pozwala zrozumieć motywację Artura jako 'buntownika przeciw wolności': dramat Mrożka jest diagnozą pułapki permisywizmu – człowiek potrzebuje formy i reguł, bez których staje się bezbronną ofiarą chaosu."
          },
          {
            "typ": "Kontekst intertekstualny / literacki",
            "zrodloZewnetrzne": "Dramat Stanisława Wyspiańskiego „Wesele” (1901 r.) – motyw tańca chocholego i zdrady inteligencji",
            "tytul": "Tango „La Cumparsita” jako współczesna trawestacja chocholego tańca",
            "opis": "Finał 'Tanga' jest bezpośrednim, ironicznym nawiązaniem do finału 'Wesela'. U Wyspiańskiego uśpieni inteligenci i chłopi krążyli w letargu za dźwiękiem słomianego chochoła. U Mrożka stary inteligent wuj Eugeniusz tańczy tango z prymitywnym prolem Edkiem nad trupem zamordowanego Artura. Edek założył marynarkę Artura i dyktuje kroki – inteligencja zostaje ostatecznie upokorzona i tańczy tak, jak zagra jej bezczelny cham.",
            "funkcja": "Ukazuje ciągłość polskiego dramatu narodowego: Mrożek aktualizuje diagnozę Wyspiańskiego, dowodząc, że bierność i słabość psychiczna intelektualistów kończy się oddaniem władzy w ręce bezwzględnej dyktatury."
          },
          {
            "typ": "Kontekst politologiczno-historiozoficzny",
            "zrodloZewnetrzne": "Teoria krążenia elit socjologa Vilfredo Pareto oraz mechanizm powstawania reżimów faszystowskich i totalitarnych",
            "tytul": "Próżnia aksjologiczna jako podatny grunt dla narodzin bezwzględnych autorytaryzmów",
            "opis": "Socjologia dowodzi, że gdy tradycyjne elity kulturalne tracą wiarę we własne wartości i oddają się jałowym dyskusjom, w społeczeństwie powstaje groźna próżnia. Tę próżnię natychmiast wypełnia 'człowiek z dołu' – prymitywna jednostka siłowa (Edek), która nie potrzebuje ideologii, praw ani skrupułów, lecz rządzi czystą pięścią ('Teraz moja kolej. Wy będziecie mnie słuchać'). W ten sposób w Europie w XX wieku rodziły się reżimy dyktatorskie.",
            "funkcja": "Daje politologiczne wyjaśnienie finału sztuki: Mrożek ostrzega, że odrzucenie zasad moralnych i kulturowych przez elity zawsze toruje drogę rządom bezwzględnych bandytów i populizmu."
          }
        ]
      },

      # 26. MAREK NOWAKOWSKI - GÓRĄ „EDEK”
      {
        "id": "nowakowski-gora-edek",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Górą „Edek” (z tomu „Prawo prerii”)",
        "autor": "Marek Nowakowski",
        "epoka": "Współczesność",
        "gatunek": "Opowiadanie obyczajowe / miniatura realistyczna",
        "motywy": ["transformacja ustrojowa", "drapieżny kapitalizm", "prawo dżungli", "arogancja nowobogackich", "kapitulacja inteligencji", "chuligaństwo"],
        "synteza": "Krótka scenka uliczna z warszawskiego korka: kierowca małego fiata (kulturalny inteligent) zostaje chamsko i bezczelnie zepchnięty z pasa przez potężnego forda scorpio prowadzonego przez współczesnego, agresywnego nuworysza – zmaterializowanego Edka.",
        "tematyMaturalne": [
          "Prawo silniejszego jako zagrożenie dla kultury i współżycia społecznego.",
          "Przemiany mentalności Polaków w okresie transformacji ustrojowej lat 90.",
          "Bezradność tradycyjnej kultury inteligenckiej wobec prymitywnej bezwzględności."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-społeczny",
            "zrodloZewnetrzne": "Polska transformacja ustrojowa lat 90. XX wieku (plan Balcerowicza, szok rynkowy, kult szybkiego bogacenia się i narodziny nowobogactwa)",
            "tytul": "Realne procesy społeczne wczesnego, drapieżnego kapitalizmu w Polsce",
            "opis": "Po 1989 r. runął ustrój komunistyczny, a Polska weszła w fazę dzikiego kapitalizmu. Obok wolności gospodarczej eksplodowało zjawisko bezwzględnej pogoni za pieniądzem, cwaniactwa i demonstracyjnego bogacenia się. Posiadanie zachodniego samochodu stawało się symbolem bezkarności, a brak stabilnych norm prawnych sprzyjał powstawaniu postaw rodem z 'prawa prerii'.",
            "funkcja": "Osadza mikroopowiadanie w konkretnym momencie dziejowym: dowodzi, że konflikt drogowy jest mikrokosmosem oddającym brutalne realia polskiego społeczeństwa epoki transformacji."
          },
          {
            "typ": "Kontekst intertekstualny",
            "zrodloZewnetrzne": "Dramat Sławomira Mrożka „Tango” (1964 r.) – postać Edka jako kulturowego archetypu chama",
            "tytul": "Wyjście Edka z teatru absurdu na ulice współczesnej Warszawy",
            "opis": "Nowakowski celowo umieścił imię mrożkowskiego bohatera w tytule opowiadania. O ile u Mrożka Edek był figurą filozoficzno-teatralną, o tyle w latach 90. Edek stał się realnym panem polskich ulic: ma gruby kark, ostentacyjny samochód, gardzi słabszymi i manifestuje siłę. Nowakowski stawia gorzką diagnozę: to, przed czym Mrożek przestrzegał w teatrze, stało się polską codziennością.",
            "funkcja": "Wskazuje na dialog między tekstami kultury: ukazuje ewolucję toposu prymitywa u władzy od metafory scenicznej do bezwzględnego faktu socjologicznego."
          },
          {
            "typ": "Kontekst aksjologiczno-etyczny",
            "zrodloZewnetrzne": "Socjologiczna koncepcja kryzysu etosu polskiej inteligencji (analizy prof. Jerzego Jedlickiego i prof. Andrzeja Walickiego)",
            "tytul": "Tradycyjny kodeks inteligencki w zderzeniu z bezwzględnością pragmatyczną",
            "opis": "Kierowca malucha reprezentuje dawną kulturę inteligencką: jest wychowany w poszanowaniu prawa, zasad kodeksu drogowego i taktu ('mądrzejszy ustępuje'). Jednak w zderzeniu z agresywnym chamstwem jego kultura staje się bezsilna: uległość nie zostaje odebrana jako klasa czy szlachetność, lecz jako słabość zasługująca na pogardliwe zatrąbienie.",
            "funkcja": "Prowokuje do refleksji nad dramatem współczesnej kultury: czy kultura i uprzejmość są w stanie przetrwać w świecie, w którym premiowana jest wyłącznie brutalna siła i brak skrupułów?"
          }
        ]
      },

      # 27. ANDRZEJ STASIUK - MIEJSCE
      {
        "id": "stasiuk-miejsce",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Miejsce (z tomu „Opowieści galicyjskie”)",
        "autor": "Andrzej Stasiuk",
        "epoka": "Współczesność",
        "gatunek": "Opowiadanie eseistyczne / proza poetycka",
        "motywy": ["Łemkowszczyzna", "Akcja Wisła", "pamięć miejsca (genius loci)", "trwanie śladów", "sacrum i profanum", "przemijanie"],
        "synteza": "Eseistyczny opis pustego placu w Beskidzie Niskim, gdzie niegdyś stała drewniana cerkiew łemkowska; narrator rekonstruuje w pamięci jej zapach, drewniane ściany i obecność dawnych modlących się ludzi, udowadniając, że duchowość miejsca trwa mimo fizycznego zniknięcia materii.",
        "tematyMaturalne": [
          "Pamięć o przeszłości zaklęta w krajobrazie i przedmiotach codzienności.",
          "Tragedia wykorzenionych narodów a tożsamość małych ojczyzn.",
          "Materialność a niematerialny wymiar sacrum w doświadczeniu upływu czasu."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-etniczny",
            "zrodloZewnetrzne": "Wojskowa operacja Akcja „Wisła” (kwiecień-lipiec 1947 r.) i przymusowe wysiedlenie ponad 140 tys. Łemków i Ukraińców",
            "tytul": "Tragedia czystek etnicznych i zagłada wielokulturowego świata Karpat",
            "opis": "W 1947 r. władze komunistyczne pod pretekstem walki z UPA przeprowadziły brutalną deportację ludności łemkowskiej i ukraińskiej z Beskidu Niskiego i Bieszczadów na Ziemie Odzyskane. Wsie zostały spalone, a wielowiekowa kultura górali karpackich została w ciągu kilku tygodni wymazana z mapy. Pustka w krajobrazie, którą kontempluje narrator Stasiuka, jest bezpośrednią blizną po tej operacji historycznej.",
            "funkcja": "Konieczny kontekst faktograficzny: bez wiedzy o Akcji 'Wisła' czytelnik nie zrozumie, dlaczego cerkiew zniknęła i z jakiego powodu krajobraz Beskidu jest przesiąknięty melancholią i poczuciem winy."
          },
          {
            "typ": "Kontekst kulturoznawczo-architektoniczny",
            "zrodloZewnetrzne": "Architektura drewnianych cerkwi łemkowskich typu zachodniego (wpisanych na listę Światowego Dziedzictwa UNESCO, np. w Kwiatoniu i Owczarach)",
            "tytul": "Trójdzielna symbolika cerkwi karpackiej i jej relacja z przyrodą",
            "opis": "Cerkiew łemkowska była konstruowana z drewna jodłowego lub modrzewiowego w układzie trójdzielnym (babiniec, nawa, prezbiterium), symbolizującym Trójcę Świętą i etapy wędrówki duszy do Boga. Cerkwie te nie były obcymi bryłami, lecz organicznie wrastały w góry, pachnąc żywicą i woskiem świec. Przeniesienie świątyni do skansenu w Nowym Sączu uratowało belki, lecz uśmierciło jej sens religijny.",
            "funkcja": "Ułatwia zrozumienie opisu Stasiuka: cerkiew była żywym bytem powiązanym z otaczającymi ją drzewami i potokiem; wyrwana ze swego miejsca staje się martwym eksponatem muzealnym."
          },
          {
            "typ": "Kontekst filozoficzno-humanistyczny",
            "zrodloZewnetrzne": "Koncepcja „miejsc pamięci” (lieux de mémoire) francuskiego historyka Pierre'a Nory oraz kategoria genius loci",
            "tytul": "Pamięć kulturowa zaklęta w niematerialnym śladzie przestrzeni",
            "opis": "Pierre Nora badał, w jaki sposób pamięć zbiorowa przechowuje się w konkretnych punktach przestrzeni, gdy zanikają żywe społeczności. Z kolei rzymskie pojęcie 'genius loci' (ducha opiekuńczego miejsca) zakłada, że przestrzeń przez stulecia nasycana ludzkimi modlitwami zachowuje swój sakralny ład nawet po zburzeniu murów. Narrator Stasiuka wpatruje się w cień fundamentów w pokrzywach, udowadniając, że pamięć jest zjawiskiem metafizycznym.",
            "funkcja": "Pozwala odczytać opowiadanie jako traktat filozoficzny o triumfie duchowej pamięci nad materialnym zniszczeniem: świątynia nadal istnieje, dopóki ktoś potrafi ją w skupieniu pomyśleć."
          }
        ]
      },

      # 28. OLGA TOKARCZUK - PROFESOR ANDREWS W WARSZAWIE
      {
        "id": "tokarczuk-profesor-andrews",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Profesor Andrews w Warszawie (z tomu „Gra na wielu bębenkach”)",
        "autor": "Olga Tokarczuk",
        "epoka": "Współczesność",
        "gatunek": "Opowiadanie psychologiczno-społeczne",
        "motywy": ["stan wojenny", "obcość i izolacja", "wieża Babel", "kafkowska paranoja", "solidarność ludzka", "karp wigilijny"],
        "synteza": "Angielski profesor psychologii przylatuje do Warszawy w przeddzień wprowadzenia stanu wojennego (grudzień 1981 r.); odcięty od telefonów i nieznający języka polskiego, błąka się po zaśnieżonym, zmilitaryzowanym mieście, doświadczając przerażającej obcości i kafkowskiego absurdu.",
        "tematyMaturalne": [
          "Wojna i stan wojenny widziane oczami obcokrajowca – technika obcej perspektywy.",
          "Bariery komunikacyjne, alienacja i samotność człowieka w nieznanym świecie.",
          "Elementarna ludzka życzliwość jako jedyny ratunek w obliczu katastrofy historycznej."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-polityczny",
            "zrodloZewnetrzne": "Wprowadzenie stanu wojennego w Polsce przez Wojskową Radę Ocalenia Narodowego (13 grudnia 1981 r.)",
            "tytul": "Paraliż komunikacyjny, militaryzacja ulic i odcięcie Polski od świata",
            "opis": "W nocy z 12 na 13 grudnia 1981 r. generał Wojciech Jaruzelski ogłosił stan wojenny. Wyłączono wszystkie telefony miejskie i międzynarodowe, wprowadzono godzinę milicyjną, cenzurę korespondencji, zamknięto granice i lotniska, a na skrzyżowaniach miast stanęły czołgi T-55 i koksowniki. Dla Anglika z wolnego świata był to niewyobrażalny szok cywilizacyjny – nagłe zniknięcie praworządnego świata.",
            "funkcja": "Dostarcza niezbędnych faktów historycznych tłumaczących zachowanie bohatera: uświadamia, że profesor Andrews nie miał obiektywnej możliwości skontaktowania się z ambasadą ani powrotu do domu, wpadając w środek komunistycznego paraliżu państwa."
          },
          {
            "typ": "Kontekst literacki / kafkowski",
            "zrodloZewnetrzne": "Powieść Franza Kafki „Proces” (1925 r.) – motyw labiryntu biurokratycznego i osaczenia",
            "tytul": "Kafkowska atmosfera absurdu, alienacji i niewytłumaczalnego osaczenia",
            "opis": "Sytuacja angielskiego profesora przypomina los Józefa K.: świat wokół traci logikę, opiekunka Gosia znika, ludzie mówią niezrozumiałym językiem, na ulicach stoją uzbrojeni żołnierze grzejący ręce przy ogniu, a w sklepie ludzie stoją w gigantycznej kolejce po żywe ryby pływające w wannie. Brak wyjaśnienia przyczyn rodzi w bohaterze narastającą paranoję i poczucie winy.",
            "funkcja": "Umożliwia odczytanie opowiadania w planie uniwersalnym: jako metafory człowieka wrzuconego w absurdalny, bezduszny mechanizm wielkiej historii, której reguł nie rozumie."
          },
          {
            "typ": "Kontekst psychologiczny / naukowy",
            "zrodloZewnetrzne": "Psychologiczna teoria szoku kulturowego (Kalervo Oberg) oraz zjawisko deprywacji informacyjnej",
            "tytul": "Regresja psychologiczna człowieka pozbawionego kodu komunikacyjnego",
            "opis": "Badania psychologiczne nad szokiem kulturowym dowodzą, że nagłe pozbawienie jednostki możliwości porozumienia i przewidywania zachowań otoczenia prowadzi do gwałtownej paniki, zaburzeń poznawczych i regresji do zachowań pierwotnych (poszukiwanie ciepła i jedzenia). Profesor psychologii zachowań behawioralnych sam staje się bezradnym obiektem własnej nauki, a ratuje go dopiero prosty, przedwerbalny gest polskich przechodniów dzielących się z nim chlebem.",
            "funkcja": "Służy do analizy przemiany psychicznej profesora: dowodzi, że w sytuacjach granicznych wyrafinowane teorie naukowe zawodzą, a jedynym mostem porozumienia staje się pierwotny odruch ludzkiej empatii."
          }
        ]
      },

      # 29. RYSZARD KAPUŚCIŃSKI - PODRÓŻE Z HERODOTEM
      {
        "id": "kapuscinski-herodot",
        "kategoria": "podstawowy",
        "kategoriaNazwa": "Zakres podstawowy",
        "tytul": "Podróże z Herodotem (fragmenty)",
        "autor": "Ryszard Kapuściński",
        "epoka": "Współczesność",
        "gatunek": "Reportaż podróżniczy / esej autobiograficzny",
        "motywy": ["podróż jako poznanie", "spotkanie z Innym", "Herodot jako pierwszy reporter", "przekraczanie granic", "ciekawość świata", "pluralizm kultur"],
        "synteza": "Zapis reporterskich wędrówek autora po Indiach, Chinach i Afryce w latach 50. i 60. XX w., spleciony z lekturą 'Dziejów' starożytnego greckiego historyka Herodota, który staje się dla polskiego dziennikarza mistrzem otwartego, pozbawionego pychy spotkania z odmienną kulturą.",
        "tematyMaturalne": [
          "Podróż jako próba zrozumienia Innego i samego siebie.",
          "Ciekawość świata i tolerancja jako fundamenty rzetelnego dziennikarstwa.",
          "Antyk jako żywy przewodnik po problemach współczesnego świata."
        ],
        "konteksty": [
          {
            "typ": "Kontekst filozoficzno-antropologiczny",
            "zrodloZewnetrzne": "Filozofia dialogu Emmanuela Levinasa („Całość i nieskończoność”, 1961 r.) oraz myśl ks. Józefa Tischnera („Filozofia dramatu”)",
            "tytul": "Etyka spotkania twarzą w twarz z „Innym” bez europocentrycznej pychy",
            "opis": "Emmanuel Levinas głosił, że spojrzenie w twarz Innego nakłada na człowieka bezwzględną odpowiedzialność moralną: wymaga odrzucenia pokusy podporządkowania sobie obcego i zrezygnowania z przemocy. Kapuściński wciela tę filozofię w życie: podróżując po Trzecim Świecie, odrzuca kolonialną wyższość białego człowieka, siada w kurzu z mieszkańcami indyjskich i afrykańskich wiosek i próbuje pojąć ich świat z ich własnej perspektywy.",
            "funkcja": "Stanowi fundament etyczny twórczości Kapuścińskiego: definiuje reportaż nie jako sensacyjną pogoń za newsem, lecz jako głębokie, humanistyczne spotkanie z obcym człowiekiem wymagające pokory i szacunku."
          },
          {
            "typ": "Kontekst antyczno-metodologiczny",
            "zrodloZewnetrzne": "Starożytne dzieło Herodota z Halikarnasu „Dzieje” (Historiai, V w. p.n.e.) – narodziny metody autopsji",
            "tytul": "Herodot jako pierwszy globalny reporter stosujący zasadę naocznego świadectwa",
            "opis": "Herodot w V w. p.n.e. wyruszył w podróż do Egiptu, Babilonii i Scytii, by dociec przyczyn wojen grecko-perskich. Zastosował nowatorską metodę: autopsję (osobiste naoczne oglądanie), 'historie' (dociekanie i wypytywanie świadków) oraz powstrzymanie się od osądzania cudzych wierzeń. Kapuściński odkrywa, że współczesny korespondent nie ma lepszego narzędzia niż to, które 2500 lat wcześniej stworzył starożytny Grek.",
            "funkcja": "Ukazuje klamrę kompozycyjną łączącą starożytność ze współczesnością: dowodzi, że ciekawość drugiego człowieka jest odwiecznym spoiwem cywilizacji śródziemnomorskiej."
          },
          {
            "typ": "Kontekst geopolityczny / historyczny",
            "zrodloZewnetrzne": "Polska za żelazną kurtyną w dobie stalinizmu oraz globalny proces dekolonizacji Trzeciego Świata (konferencja w Bandungu, 1955 r.)",
            "tytul": "Marzenie o przekroczeniu granicy PRL i narodziny niepodległych państw Azji i Afryki",
            "opis": "Młody Kapuściński dorastał w zniszczonej powojennej Polsce, gdzie granica państwowa była barierą nie do przebycia strzeżoną przez wieżyczki i cenzurę. Gdy w 1956 r. po odwilży październikowej wyrusza do Indii, trafia w sam środek wielkich procesów dekolonizacyjnych – rozpadu imperium brytyjskiego i francuskiego oraz narodzin wolnych narodów Azji i Afryki.",
            "funkcja": "Tłumaczy młodzieńczą zachłanność poznawczą autora: dla człowieka wyrwanego z zamkniętego bloku komunistycznego podróż była aktem najwyższej wolności wewnętrznej i odkrywaniem wielobarwnego świata poza dogmatami propagandy."
          }
        ]
      },

      # ==========================================
      # SZKOŁA PODSTAWOWA (DO MATURY)
      # ==========================================

      # 30. IGNACY KRASICKI - BAJKI
      {
        "id": "krasicki-bajki",
        "kategoria": "podstawowa-szkola",
        "kategoriaNazwa": "Szkoła podstawowa",
        "tytul": "Bajki (np. „Kruk i lis”, „Dewotka”, „Ptaszki w klatce”, „Jagnię i wilcy”)",
        "autor": "Ignacy Krasicki",
        "epoka": "Oświecenie",
        "gatunek": "Bajka epigramatyczna / narracyjna",
        "motywy": ["ludzkie przywary", "prawo silniejszego", "fałszywa pobożność", "wolność a niewola", "zwierzęce maski", "morał"],
        "synteza": "Zwięzłe, poetyckie miniatury dydaktyczne, w których pod kostiumem zwierzęcym biskup warmiński obnaża uniwersalne wady ludzkiej natury: próżność, naiwność, obłudę religijną oraz bezwzględność silniejszych wobec słabych.",
        "tematyMaturalne": [
          "Maska zwierzęca w literaturze jako lustro wad ludzkiego charakteru.",
          "Problem wolności i niewoli w twórczości Ignacego Krasickiego.",
          "Krytyka pozornej moralności i dewocji w duchu oświeceniowego rozumu."
        ],
        "konteksty": [
          {
            "typ": "Kontekst literacki / tradycja gatunkowa",
            "zrodloZewnetrzne": "Antyczna i nowożytna tradycja bajkopisarstwa: zbiory Ezopa (VI w. p.n.e.), Fedrusa oraz Jeana de La Fontaine'a (XVII w.)",
            "tytul": "Ezopowy język i ewolucja bajki epigramatycznej w Europie",
            "opis": "Gatunek bajki zwierzęcej wywodzi się od greckiego niewolnika Ezopa, który musiał ukrywać prawdę o wadach swych panów pod maskami zwierząt (tzw. język ezopowy). Krasicki udoskonalił ten gatunek, tworząc bajkę epigramatyczną – arcydzieło zwięzłości (często zaledwie 4 wersy), w której wyeliminował długie narracje La Fontaine'a na rzecz matematycznej wręcz precyzji słowa i błyskotliwej puenty.",
            "funkcja": "Wskazuje na kunszt literacki Krasickiego: autor nie wymyślał nowych motywów, lecz doprowadził do doskonałości klasyczną europejską formę bajki."
          },
          {
            "typ": "Kontekst filozoficzno-polityczny",
            "zrodloZewnetrzne": "Filozofia prawa naturalnego Thomasa Hobbesa („Lewiatan”, 1651 r.) i maksyma „homo homini lupus est”",
            "tytul": "Człowiek człowiekowi wilkiem – bezwzględne prawa natury w stosunkach międzyludzkich",
            "opis": "Thomas Hobbes dowodził, że w stanie natury relacjami między ludźmi rządzi egoizm i siła ('wojna wszystkich przeciw wszystkim'). W bajce 'Jagnię i wilcy' Krasicki z przerażającym lakonizmem ilustruje tę tezę: wilcy pożerają jagnię nie dlatego, że zawiniło, lecz dlatego, że 'smacznyś, słaby i w lesie'. W świecie bez praw moralnych rację ma ten, kto ma kły.",
            "funkcja": "Pozwala odczytać bajki głębiej niż naiwne czytanki dla dzieci: jako bezlitosną diagnozę polityczną natury człowieka i stosunków międzynarodowych, gdzie słaby zawsze pada ofiarą potężniejszego drapieżnika."
          },
          {
            "typ": "Kontekst historyczno-rozbiorowy",
            "zrodloZewnetrzne": "Aneksja Warmii przez Prusy Fryderyka II Wielkiego (1772 r.) i doświadczenie utraty niepodległości",
            "tytul": "Bajka „Ptaszki w klatce” jako alegoria rozbioru Polski i pamięci o wolności",
            "opis": "Po I rozbiorze Warmia, której biskupem był Krasicki, została wcielona do militarystycznego Królestwa Prus, a sam poeta stał się pruskim poddanym. W bajce 'Ptaszki w klatce' stary czyżyk płacze w klatce, a młody dziwi się jego łzom, bo urodził się w zamknięciu i ma pod dostatkiem ziarna. Stary odpowiada: 'Jam był wolny, dziś w klatce – i dlatego płaczę'.",
            "funkcja": "Stanowi bezpośrednią aluzję do losu Polaków pod zaborami: jest ostrzeżeniem przed groźbą przyzwyczajenia się młodych pokoleń do niewoli i zapomnienia o wolnej ojczyźnie."
          }
        ]
      },

      # 31. ADAM MICKIEWICZ - DZIADY CZ. II
      {
        "id": "mickiewicz-dziady-2",
        "kategoria": "podstawowa-szkola",
        "kategoriaNazwa": "Szkoła podstawowa",
        "tytul": "Dziady cz. II",
        "autor": "Adam Mickiewicz",
        "epoka": "Romantyzm",
        "gatunek": "Dramat romantyczny",
        "motywy": ["obrzęd dziadów", "wina i kara", "cierpienie jako warunek człowieczeństwa", "zaświaty", "ludowa moralność", "kontakt z duchami"],
        "synteza": "Przedstawienie archaicznego obrzędu wywoływania dusz zmarłych w cmentarnej kaplicy pod przewodnictwem Guślarza; przybywające duchy lekkie (Józio i Rózia), ciężkie (Zły Pan) oraz pośrednie (Zosia) głoszą uniwersalne prawdy o warunkach osiągnięcia zbawienia.",
        "tematyMaturalne": [
          "Ludowy kodeks moralny – zasady sprawiedliwości i człowieczeństwa w 'Dziadach cz. II'.",
          "Cierpienie, miłość i odpowiedzialność za innych jako warunki pełni człowieczeństwa.",
          "Wzajemne przenikanie się świata żywych i umarłych w wyobraźni romantycznej."
        ],
        "konteksty": [
          {
            "typ": "Kontekst etnograficzno-religioznawczy",
            "zrodloZewnetrzne": "Prace etnograficzne nad przedchrześcijańskimi rytuałami zadusznymi Słowian (Kazimierz Władysław Wójcicki, Zorian Dołęga-Chodakowski)",
            "tytul": "Przedchrześcijański kult przodków u Słowian i obrzęd karmienia dusz",
            "opis": "We wstępie do utworu Mickiewicz wyjaśnia, że 'Dziady' to autentyczny obrzęd pogański odprawiany potajemnie przez lud na Litwie i Białorusi w wigilię Wszystkich Świętych. Wierzono, że głodne dusze czyśćcowe przybywają do żywych po strawę (kutia, mleko) i modlitwę, a w zamian mogą udzielić żyjącym pouczenia moralnego. Kościół katolicki bezskutecznie próbował wykorzenić ten rytuał.",
            "funkcja": "Ukazuje zakorzenienie utworu w autentycznej kulturze Kresów: romantycy uważali pogańskie wierzenia ludu za nieskażone źródło pradawnej mądrości duchowej narodu."
          },
          {
            "typ": "Kontekst literacki / szekspirowski",
            "zrodloZewnetrzne": "Tragedie Williama Szekspira („Hamlet”, „Makbet”) – obecność duchów ingerujących w sumienia żywych",
            "tytul": "Szekspirowskie motto: „Są dziwy na niebie i na ziemi, o których ani śniło się waszym filozofom”",
            "opis": "Mickiewicz opatrzył dramat mottem ze sceny spotkania Hamleta z duchem ojca. Romantycy odrzucili klasycystyczną zasadę prawdopodobieństwa na rzecz elżbietańskiej koncepcji świata, w którym zaświaty realnie przenikają się z materią, a zjawy pełnią funkcję sędziów ludzkich zbrodni.",
            "funkcja": "Uzasadnia wprowadzenie zjaw na scenę: spotkanie z duchami nie jest baśniowym trickiem, lecz próbą dotknięcia metafizycznej tajemnicy istnienia i moralnej odpowiedzialności człowieka za swoje czyny."
          },
          {
            "typ": "Kontekst aksjologiczny / filozofia człowieka",
            "zrodloZewnetrzne": "Koncepcja 'moralności naturalnej' i romantyczna teza o konieczności doświadczenia pełni losu ludzkiego",
            "tytul": "Warunki pełni człowieczeństwa w ludowej teologii moralnej",
            "opis": "Przestrogi duchów tworzą spójny system etyczny: Józio i Rózia przypominają, że kto nie zaznał goryczy cierpienia, nie pozna słodyczy nieba; widmo Złego Pana uczy, że brak miłosierdzia i głodzenie poddanych zamyka drogę do zbawienia; pasterka Zosia dowodzi, że życie bez dojrzałej miłości i odpowiedzialności jest jałowe.",
            "funkcja": "Służy do sformułowania definicji człowieczeństwa: Mickiewicz dowodzi, że istotą ludzkiego losu jest pełne uczestnictwo w świecie – trzeba zaznać trudu, kochać innych i okazywać empatię słabszym, by zasłużyć na zbawienie."
          }
        ]
      },

      # 32. ALEKSANDER FREDRO - ZEMSTA
      {
        "id": "fredro-zemsta",
        "kategoria": "podstawowa-szkola",
        "kategoriaNazwa": "Szkoła podstawowa",
        "tytul": "Zemsta",
        "autor": "Aleksander Fredro",
        "epoka": "Romantyzm (estetyka klasycystyczno-oświeceniowa)",
        "gatunek": "Komedia kontuszowa (charakterów i intrygi)",
        "motywy": ["sarmatyzm", "spór o mur graniczny", "miłość wbrew waśniom rodowym", "Papkin jako miles gloriosus", "komizm językowy i sytuacyjny"],
        "synteza": "Arcydzieło polskiej komedii wierszowanej ukazujące zaciekły spór dwóch szlachciców mieszkających w jednym zamku – porywczego Cześnika Raptusiewicza i obłudnego Rejenta Milczka – zakończony niespodziewanym ślubem Klary i Wacława.",
        "tematyMaturalne": [
          "Ciepły i krytyczny portret polskiej sarmacji w komedii Aleksandra Fredry.",
          "Mistrzostwo komizmu słownego, postaci i sytuacji w 'Zemście'.",
          "Spory sąsiedzkie w polskiej tradycji literackiej i sposoby ich rozwiązywania."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-archiwalny",
            "zrodloZewnetrzne": "Autentyczne akta procesowe sądu wyższego w Sanoku z 1630 roku – spór o zamek Kamieniec w Odrzykoniu",
            "tytul": "Prawdziwa historia procesu Jana Skotnickiego z Piotrem Firlejem",
            "opis": "Aleksander Fredro w 1828 r. żeniąc się z Zofią Jabłonowską, wszedł w posiadanie połowy zamku w Odrzykoniu. W starych dokumentach archiwalnych odkrył akta autentycznego, trwającego kilkadziesiąt lat procesu między dawnymi właścicielami zamku: Janem Skotnickim (pierwowzór Rejenta) a wojewodą Piotrem Firlejem (pierwowzór Cześnika). Skotnicki złośliwie naprawił rynnę, by woda zalewała dziedziniec Firleja, a konflikt zakończył dopiero ślub Mikołaja Firleja z kasztelanką Zofią Skotnicką w 1638 r.",
            "funkcja": "Dowodzi niezwykłego realizmu utworu: pokazuje, że Fredro nie wymyślił absurdalnego sporu o mur graniczny przy biurku, lecz przeniósł na scenę autentyczny wycinek szlacheckiego pieniactwa z XVII stulecia."
          },
          {
            "typ": "Kontekst prawno-obyczajowy",
            "zrodloZewnetrzne": "Staropolskie prawo szlacheckie: instytucja zbrojnego zajazdu, sądy ziemskie i specyfika pieniactwa sarmackiego",
            "tytul": "Sarmacka kultura procesowa i kultura szabli w dawnej Polsce",
            "opis": "W dawnej Rzeczypospolitej szlachta cieszyła się niemal absolutną nietykalnością (Neminem captivabimus). Pieniacki tryb życia był normą – procesowano się o każdą miedzę przez pokolenia, a wyroki trybunalskie z powodu słabości władzy królewskiej egzekwowano często siłą poprzez tzw. zajazd szlachecki. Cześnik i Rejent reprezentują dwa bieguny tej kultury: Cześnik wierzy w szablę (Panią Barską) i siłę, Rejent w kruczki prawne, fałszowanie zeznań mularzy i bezwzględne pozwy.",
            "funkcja": "Ułatwia socjologiczną analizę postaci: Fredro genialnie ukazał dwie twarze schyłkowego sarmatyzmu – jawną, gwałtowną agresję rębajły skontrastowaną z cichą, dewocyjną hipokryzją szlacheckiego jurysty."
          },
          {
            "typ": "Kontekst literacko-teatralny",
            "zrodloZewnetrzne": "Antyczny topos żołnierza samochwała (miles gloriosus Plauta) oraz włoska commedia dell'arte (postać Capitana)",
            "tytul": "Geneza literacka postaci Józefa Papkina",
            "opis": "Postać Papkina nie jest jedynie polskim szlachetką na łasce magnata, lecz realizacją odwiecznego archetypu komediowego sięgającego komedii rzymskiej Plauta i włoskiego teatru improwizowanego. Żołnierz samochwał opowiada niestworzone bajki o swoich podbojach wojennych i sercowych, lecz przy pierwszym zagrożeniu okazuje się tchórzem, panicznie bojącym się pojedynku i trucizny.",
            "funkcja": "Wzbogaca interpretację komizmu postaci Papkina: ukazuje go jako postać tragikomiczną – rozdartą między wielkimi marzeniami o rycerskiej sławie a żałosną pozycją zubożałego rezydenta zmuszonego do płaszczenia się przed chlebodawcą."
          }
        ]
      },

      # 33. JULIUSZ SŁOWACKI - BALLADYNA
      {
        "id": "slowacki-balladyna",
        "kategoria": "podstawowa-szkola",
        "kategoriaNazwa": "Szkoła podstawowa",
        "tytul": "Balladyna",
        "autor": "Juliusz Słowacki",
        "epoka": "Romantyzm",
        "gatunek": "Tragedia romantyczna / baśń dramatyczna",
        "motywy": ["żądza władzy", "zbrodnia rodząca zbrodnię", "krwawe znamię", "wyparcie się matki", "świat baśniowy (Goplana)", "sprawiedliwość metafizyczna"],
        "synteza": "Krwawa droga prostej dziewczyny z wiejskiej chaty na królewski tron w Gnieźnie: od zabójstwa siostry Aliny w leśnym konkursie zbierania malin, przez kolejne morderstwa męża i sprzymierzeńców, aż po wyparcie się matki i śmierć od pioruna po wydaniu na samą siebie sprawiedliwego wyroku.",
        "tematyMaturalne": [
          "Zbrodnia jako środek zdobycia władzy i psychologiczne konsekwencje winy.",
          "Motyw wyparcia się własnych korzeni i matczynej miłości.",
          "Rola baśniowej sprawiedliwości i ładu moralnego w świecie przedstawionym."
        ],
        "konteksty": [
          {
            "typ": "Kontekst literacki / szekspirowski",
            "zrodloZewnetrzne": "Dramaturgia Williama Szekspira: motyw zbrodni z „Makbeta”, świat leśnych elfów ze „Snu nocy letniej” oraz tragedia Króla Leara",
            "tytul": "Świadoma gra Słowackiego z kanonem dramaturgii elżbietańskiej",
            "opis": "Słowacki jawnie skomponował 'Balladynę' jako syntezę motywów szekspirowskich: Balladyna idzie drogą Makbeta (jedna zbrodnia pociąga lawinę kolejnych morderstw, a krwawa plama na czole nie daje się zmyć jak krew z rąk Lady Makbet); postacie Goplany, Skierki i Chochlika to świat elfa Puka ze 'Snu nocy letniej'; oślepiona, wygnana na burzę matka (Wdowa) cierpi jak król Lear wygnany przez niewdzięczne córki.",
            "funkcja": "Ukazuje kunszt poetycki Słowackiego: dramat nie jest naiwną bajką ludową, lecz wyrafinowaną, nowatorską grą literacką z arcydziełami europejskiego teatru, przeniesioną w baśniowe realia okolic jeziora Gopło."
          },
          {
            "typ": "Kontekst historiograficzny / legendarny",
            "zrodloZewnetrzne": "Kroniki Marcina Bielskiego i Jana Długosza – podania o legendarnych początkach państwa polskiego, dynastii Popielidów i koronie Lecha",
            "tytul": "Legendarna prehistoria Polski jako kostium dla rozważań o czystości władzy",
            "opis": "Akcja toczy się 'za czasów bajecznych koło jeziora Gopło'. Słowacki wykorzystał kronikarskie podania o okrutnym Popielu IV, który otruł swoich stryjów i został zjedzony przez myszy w wieży w Kruszwicy. W ten świat wplótł motyw korony Lecha – mitycznego insygnium prawowitej, suwerennej władzy, która została utracona przez grzech i bezprawie.",
            "funkcja": "Pozwala odczytać utwór w kontekście politycznym: tragedia Balladyny była dla romantyków metaforą skażenia władzy w Polsce; dowodziła, że państwo zbudowane na zbrodni, bezprawiu i uzurpacji jest skazane na boski gniew i upadek."
          },
          {
            "typ": "Kontekst baśniowo-antropologiczny",
            "zrodloZewnetrzne": "Morfologia baśni ludowej (badania Vladimira Proppa) oraz zbiory baśni braci Grimm (1812 r.)",
            "tytul": "Archetypiczna struktura baśni: zakazany pokój, próba zbierania owoców i nieuchronna kara",
            "opis": "Fabuła wykorzystuje żelazne toposy baśniowe: dwie siostry (jedna dobra, jasnowłosa, druga zła, ciemna), magiczną próbę zbierania malin do dzbanka, wierzbę płaczącą kryjącą tajemnicę morderstwa oraz krwawe piętno na czole jako niezmywalny znak Kainowy. W finale baśniowa sprawiedliwość domaga się symetrii: morderczyni jako sprawiedliwy sędzia sama skazuje się na śmierć, ściągając na siebie piorun z nieba.",
            "funkcja": "Uzasadnia przesłanie moralne utworu: świat opiera się na obiektywnym ładzie moralnym – zło rodzi samozagładę, a żadna zbrodnia nie ujdzie bezkarnie, nawet jeśli zbrodniarz wyeliminuje wszystkich ziemskich świadków."
          }
        ]
      },

      # ==========================================
      # LEKTURY DODATKOWE
      # ==========================================

      # 34. JAN KOCHANOWSKI - TRENY
      {
        "id": "kochanowski-treny",
        "kategoria": "dodatkowy",
        "kategoriaNazwa": "Lektury dodatkowe",
        "tytul": "Treny (jako cykl poetycki)",
        "autor": "Jan Kochanowski",
        "epoka": "Renesans",
        "gatunek": "Cykl poetycki (epicedium żałobne)",
        "motywy": ["żałoba ojca", "kryzys humanizmu", "załamanie stoicyzmu", "bunt przeciw Bogu", "Urszulka", "pocieszenie chrześcijańskie"],
        "synteza": "Autobiograficzny cykl 19 utworów napisanych po nagłej śmierci dwuletniej córki Urszulki w Czarnolesie, stanowiący zapis bezgranicznego ojcowskiego bólu oraz dramatycznego rozpadu renesansowej wiary w potęgę rozumu, cnoty i stoickiego opanowania.",
        "tematyMaturalne": [
          "Kryzys światopoglądu humanistycznego pod wpływem osobistej tragedii.",
          "Etapy przeżywania żałoby – od rozpaczy i buntu do chrześcijańskiego ukojenia.",
          "Treny jako rewolucyjne przełamanie antycznych reguł poetyckich."
        ],
        "konteksty": [
          {
            "typ": "Kontekst filozoficzny",
            "zrodloZewnetrzne": "Rzymska filozofia stoicyzmu: traktaty Marka Tulliusza Cycerona („Rozmowy tuskulańskie”) i Seneki Młodszego („O pocieszeniu”)",
            "tytul": "Kryzys stoickiej cnoty (apatheia) w zderzeniu z nagą rzeczywistością cierpienia",
            "opis": "Kochanowski całe życie budował renesansowy światopogląd na stoickiej zasadzie 'cnoty' – mędrzec miał panować nad afektami i zachowywać niewzruszony spokój zarówno w szczęściu, jak i w nieszczęściu. W Trenie IX i XI autor z goryczą wyznaje bankructwo tej filozofii: stoicyzm okazał się bezużyteczną teorią książkową, a mędrzec płacze nad trumną dziecka jak każdy prosty człowiek ('Fraszka cnota! – powiada Brutus porażony').",
            "funkcja": "Kluczowy kontekst ukazujący wielkość myśli Kochanowskiego: odważył się publicznie zakwestionować fundamenty renesansowego humanizmu i przyznać, że rozum ludzki jest bezradny wobec tajemnicy śmierci."
          },
          {
            "typ": "Kontekst poetycko-antyczny",
            "zrodloZewnetrzne": "Antyczna teoria poezji żałobnej: traktat Menandra z Laodycei o gatunku epicedium i trenu",
            "tytul": "Złamanie antycznej hierarchii tematów w poezji funeralnej",
            "opis": "W starożytnej poetyce greckiej i rzymskiej treny i epicedia rezerwowano wyłącznie dla wielkich mężów stanu, królów, wodzów i bohaterów wojennych. Napisanie monumentalnego, 19-częściowego cyklu poświęconego dwuletniemu dziecku było w epoce renesansu szokującym złamaniem reguł estetycznych (wielu współczesnych zarzucało Kochanowskiemu przesadę).",
            "funkcja": "Świadczy o rewolucyjnym nowatorstwie Kochanowskiego: podniósł jednostkowy, intymny żal rodzicielski do rangi najwyższej poezji filozoficznej, czyniąc małe dziecko równorzędnym bohaterem dramatu egzystencjalnego."
          },
          {
            "typ": "Kontekst teologiczno-religijny",
            "zrodloZewnetrzne": "Chrześcijańska teologia pocieszenia: „Wyznania” św. Augustyna oraz biblijna mądrość Hiobowa",
            "tytul": "Od buntu i zwątpienia do chrześcijańskiej pokory w Trenie XIX (Sen)",
            "opis": "Cykl Kochanowskiego ma przemyślaną strukturę dramatyczną: od żalu (Treny I–VIII), przez narastający kryzys światopoglądowy i bluźniercze zwątpienie w zaświaty (Tren X: 'Gdzieśkolwiek jest, jeśliś jest...'), po ostateczne ukojenie w Trenie XIX. Ukazuje się w nim zmarła matka poety z Urszulką na ręku, napominając syna, by zaufał boskiemu miłosierdziu i zalecając pokorną mądrość: 'Ludzkie przygody ludzko noś'.",
            "funkcja": "Ukazuje proces duchowego uzdrowienia: Kochanowski ostatecznie odnajduje spokój nie w pogańskim stoicyzmie, lecz w dojrzałej chrześcijańskiej nadziei na ponowne spotkanie z córką w wieczności."
          }
        ]
      },

      # 35. JULIUSZ SŁOWACKI - KORDIAN
      {
        "id": "slowacki-kordian",
        "kategoria": "dodatkowy",
        "kategoriaNazwa": "Lektury dodatkowe",
        "tytul": "Kordian",
        "autor": "Juliusz Słowacki",
        "epoka": "Romantyzm",
        "gatunek": "Dramat romantyczny",
        "motywy": ["dojrzewanie bohatera", "ból istnienia (Weltschmerz)", "winkelriedyzm", "spisek na cara", "Strach i Imaginacja", "psychomachia"],
        "synteza": "Duchowa ewolucja młodego arystokraty: od młodzieńczego rozczarowania miłością i światem materialnym podczas wędrówki po Europie, przez narodziny idei walki o wolność na szczycie Mont Blanc ('Polska Winkelriedem narodów!'), po tragiczny, samotny spisek na życie cara w Warszawie.",
        "tematyMaturalne": [
          "Ewolucja bohatera romantycznego – od marzyciela do bojownika o wolność.",
          "Winkelriedyzm jako aktywna polemika z mickiewiczowskim mesjanizmem.",
          "Moralne dylematy walki podziemnej – zabójstwo tyrana a kodeks rycerski."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-dokumentalny",
            "zrodloZewnetrzne": "Encyklika papieża Grzegorza XVI „Cum primum” (z 9 czerwca 1832 r.) potępiająca powstanie listopadowe",
            "tytul": "Zdrada Watykanu wobec walczącej Polski jako tło sceny papieskiej",
            "opis": "Papież Grzegorz XVI pod naciskiem carskiej dyplomacji wydał encyklikę nakazującą polskim biskupom i wiernym bezwzględne posłuszeństwo zaborcy, nazywając powstańców listopadowych 'wichrzycielami i siewcami niezgody'. Scena audiencji Kordiana w Watykanie jest bezpośrednim echem tego dokumentu: papież odrzuca ziemię zroszoną krwią męczenników, każe Polakom czcić cara Mikołaja I i grozi rzuceniem klątwy na buntowników.",
            "funkcja": "Kluczowy fakt polityczny: tłumaczy szok światopoglądowy Kordiana i całego pokolenia romantyków, którzy musieli dokonać bolesnego rozróżnienia między wiarą w Chrystusa a uległą wobec caratu polityką hierarchii watykańskiej."
          },
          {
            "typ": "Kontekst polemiczno-literacki",
            "zrodloZewnetrzne": "Dramat Adama Mickiewicza „Dziady cz. III” (1832 r.) oraz szwajcarski mit o Arnoldzie Winkelriedzie z bitwy pod Sempach (1386 r.)",
            "tytul": "Winkelriedyzm jako czynna alternatywa dla biernego mesjanizmu Mickiewicza",
            "opis": "Monolog Kordiana na szczycie Mont Blanc jest bezpośrednią polemiką z Wielką Improwizacją i Widzeniem ks. Piotra. Słowacki odrzuca mickiewiczowską koncepcję 'Polski Chrystusem narodów' jako usypiającą i promującą bierność ofiary. W jej miejsce proponuje winkelriedyzm: aktywny czyn zbrojny na wzór szwajcarskiego bohatera narodowego, który wbił we własną pierś lance wrogów, aby stworzyć wyłom dla towarzyszy broni ('Polska Winkelriedem narodów!').",
            "funkcja": "Ukazuje fundamentalny spór ideowy polskiego romantyzmu: pojedynek dwóch wieszczów o drogę do niepodległości – między cierpieniem ekspiacyjnym (Mickiewicz) a bezkompromisowym poświęceniem w boju (Słowacki)."
          },
          {
            "typ": "Kontekst psychologiczno-etyczny",
            "zrodloZewnetrzne": "Zjawisko 'choroby wieku' (Weltschmerz / mal du siècle) oraz etos rycerski w starciu z carskim despotyzmem",
            "tytul": "Psychomachia pod drzwiami carskiej sypialni – etyczna niemożność skrytobójstwa",
            "opis": "Gdy Kordian podejmuje samotną próbę zamordowania cara w Zamku Królewskim, pod drzwiami sypialni toczy się walka psychiczna (psychomachia): uosobione Strach i Imaginacja paraliżują jego siły. Kordian pada zemdlony nie z tchórzostwa, lecz dlatego, że rycerski kodeks honorowy, w którym został wychowany, nie pozwala mu zabić śpiącego tyrana jak pospolity skrytobójca.",
            "funkcja": "Ukazuje tragizm jednostki szlachetnej: Słowacki dowodzi, że Kordian poniósł klęskę, ponieważ był poetą o zbyt wrażliwym sumieniu, by stać się bezwzględnym, makiawelicznym zbrodniarzem."
          }
        ]
      },

      # 36. LEGENDA O ŚW. ALEKSYM
      {
        "id": "legenda-o-sw-aleksym",
        "kategoria": "dodatkowy",
        "kategoriaNazwa": "Lektury dodatkowe",
        "tytul": "Legenda o św. Aleksym (fragmenty)",
        "autor": "Anonim",
        "epoka": "Średniowiecze",
        "gatunek": "Legenda hagiograficzna (żywot świętego)",
        "motywy": ["skrajna asceza", "świętość", "wyrzeczenie się dóbr doczesnych", "teocentryzm", "cud pośmiertny", "męczeństwo za życia"],
        "synteza": "Wierszowany żywot rzymskiego patrycjusza, który w noc poślubną porzuca bogatą rodzinę i młodą żonę, rozdaje majątek ubogim i wybiera skrajne upokorzenie oraz samotną ascezę, spędzając 16 lat pod schodami własnego pałacu.",
        "tematyMaturalne": [
          "Wzorzec świętego ascety w kulturze i literaturze średniowiecza.",
          "Wyrzeczenie się doczesności w imię życia wiecznego – egoizm czy heroizm wiary?",
          "Rola cudów i niezwykłych znaków w potwierdzaniu świętości."
        ],
        "konteksty": [
          {
            "typ": "Kontekst religijno-kulturowy",
            "zrodloZewnetrzne": "Tradycja monastyczna Ojców Pustyni (św. Antoni Wielki, św. Szymon Słupnik) i średniowieczna teologia teocentryzmu",
            "tytul": "Asceza (askesis) jako droga do mistycznego przebóstwienia duszy",
            "opis": "W średniowiecznym teocentryzmie Bóg był jedynym celem istnienia, a ziemskie ciało uważano za źródło grzechu i siedlisko szatana. Ruch eremicki, zapoczątkowany przez Ojców Pustyni w Egipcie i Syrii, traktował umartwianie ciała (głód, chłód, bezdomność, bicie) jako duchowy trening ('askesis' po grecku: ćwiczenie). Cierpienie fizyczne było narzędziem wyzwalania duszy z więzów materii.",
            "funkcja": "Tłumaczy motywację Aleksego, która dla współczesnego odbiorcy wydaje się nieludzkim okrucieństwem wobec rodziny: w kategoriach średniowiecznych zbawienie wieczne wymagało radykalnego zerwania ze wszelkimi ziemskimi przywiązaniami."
          },
          {
            "typ": "Kontekst gatunkowy / tradycja tekstowa",
            "zrodloZewnetrzne": "Średniowieczny zbiór hagiograficzny Jakuba de Voragine „Legenda aurea” (Złota legenda, ok. 1260 r.)",
            "tytul": "Żelazne reguły średniowiecznego kanonu hagiograficznego",
            "opis": "Zbiór Jakuba de Voragine był najpopularniejszą po Biblii książką średniowiecznej Europy. Ustalił on żelazny schemat żywota świętego: szlachetne pochodzenie, pobożność w dzieciństwie, radykalny gest zerwania ze światem, próby wiary, cierpliwe znoszenie upokorzeń i seria spektakularnych cudów pośmiertnych (dzwony w Rzymie dzwoniące same, uzdrawiający zapach ciała, list zaciśnięty w dłoni, który może wyjąć tylko czysta żona).",
            "funkcja": "Pozwala przeanalizować utwór jako wzorzec parenetyczny: tekst nie miał być realistyczną biografią, lecz dydaktyczną instrukcją doskonałości chrześcijańskiej przeznaczoną do budowania autorytetu Kościoła."
          },
          {
            "typ": "Kontekst społeczno-prawny",
            "zrodloZewnetrzne": "Struktura patrycjatu rzymskiego w późnym Cesarstwie Rzymskim (V w. n.e.) i rzymskie prawo małżeńskie",
            "tytul": "Konflikt feudalno-rodzinny: obowiązek dynastyczny a powołanie religijne",
            "opis": "Aleksy był jedynym dziedzicem potężnego rzymskiego rodu senatorskiego Eufemijana. W realiach późnorzymskich porzucenie dziewiczej żony w noc poślubną i brak spłodzenia potomka oznaczało świadomą zagładę rodu i przejście wielkiego majątku w obce ręce. Aleksy oddaje żonie pierścień małżeński, nakazując jej zachowanie czystości dla nieba.",
            "funkcja": "Podkreśla radykalizm gestu świętego: uświadamia, jak wielką ofiarę poniósł bohater, odrzucając nie tylko komfort materialny, lecz również najwyższe zaszczyty państwowe i dynastyczny obowiązek przedłużenia rodu."
          }
        ]
      },

      # 37. KWIATKI ŚWIĘTEGO FRANCISZKA Z ASYŻU
      {
        "id": "kwiatki-sw-franciszka",
        "kategoria": "dodatkowy",
        "kategoriaNazwa": "Lektury dodatkowe",
        "tytul": "Kwiatki świętego Franciszka z Asyżu (fragmenty)",
        "autor": "Anonim (tłum. Leopold Staff)",
        "epoka": "Średniowiecze",
        "gatunek": "Zbiór przypowieści hagiograficznych",
        "motywy": ["franciszkanizm", "miłość do przyrody (bracia mniejsi)", "święte ubóstwo", "radość wiary", "pokora", "oswojenie wilka z Gubbio"],
        "synteza": "Zbiór prostych opowieści o życiu św. Franciszka z Asyżu i jego pierwszych braci, głoszących pochwałę ewangelicznego ubóstwa, radosnej miłości do Boga oraz braterstwa ze wszystkimi stworzeniami przyrody.",
        "tematyMaturalne": [
          "Franciszkanizm jako radosna alternatywa dla surowej ascezy średniowiecza.",
          "Człowiek i przyroda – harmonia stworzenia i szacunek dla 'braci mniejszych'.",
          "Moc pokory i dobroci w przezwyciężaniu agresji i zła."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-kościelny",
            "zrodloZewnetrzne": "Bulla papieża Honoriusza III „Solet annuere” (1223 r.) zatwierdzająca regułę Zakonu Braci Mniejszych",
            "tytul": "Odnowa moralna Kościoła w dobie kryzysu feudalnego bogactwa",
            "opis": "W XIII wieku Kościół katolicki zmagał się z głębokim kryzysem moralnym: biskupi żyli jak feudałowie, a bogactwo rodziło korupcję i bunty heretyckie (katarzy, waldensi). Św. Franciszek (syn bogatego kupca z Asyżu) dokonał pokojowej rewolucji: zrzucił szaty przed biskupem, wyrzekł się majątku ojca i wybrał absolutne ubóstwo, ratując autorytet Ewangelii bez uciekania się do herezji.",
            "funkcja": "Osadza tekst w realiach historycznych: wyjaśnia, dlaczego ruch franciszkański zyskał tak gigantyczne poparcie mas ludowych jako autentyczny powrót do czystości pierwotnego chrześcijaństwa."
          },
          {
            "typ": "Kontekst teologiczno-filozoficzny",
            "zrodloZewnetrzne": "Średniowieczna filozofia św. Bonawentury („Droga duszy do Boga”) – widzenie śladów Boga (vestigia Dei) w przyrodzie",
            "tytul": "Teologia afirmacji stworzenia i braterstwa kosmicznego",
            "opis": "Podczas gdy tradycyjna asceza (jak u św. Aleksego) uważała przyrodę za zagrożenie dla duszy, św. Franciszek widział w każdym stworzeniu ślad mądrości Stwórcy. W 'Pieśni słonecznej' nazywa słońce bratem, księżyc siostrą, a ogień towarzyszem. Kazanie do ptaków i zawarcie paktu z krwiożerczym wilkiem z Gubbio ukazują przywrócenie rajskiej harmonii między człowiekiem a naturą.",
            "funkcja": "Stanowi doskonały kontrast dla postawy św. Aleksego: ukazuje dwa zupełnie odmienne modele średniowiecznej świętości – ucieczkę od świata materii vs radosne braterstwo ze wszystkim, co żyje."
          },
          {
            "typ": "Kontekst literacki / młodopolski",
            "zrodloZewnetrzne": "Młodopolski renesans franciszkanizmu: poezja Leopolda Staffa (tłumacza „Kwiatków...”) oraz Jana Kasprowicza („Księga ubogich”, 1916 r.)",
            "tytul": "Franciszkanizm jako ratunek przed dekadenckim pesymizmem przełomu wieków",
            "opis": "Na przełomie XIX i XX wieku młodopolscy poeci, zmęczeni dekadentyzmem, nihilizmem i schopenhauerowskim pesymizmem, odnaleźli ratunek duchowy w postawie Biedaczyny z Asyżu. Leopold Staff przetłumaczył 'Kwiatki...' genialną, archaizowaną polszczyzną, a Jan Kasprowicz po buncie 'Hymnów' stworzył 'Księgę ubogich' pełną franciszkańskiego zachwytu nad polnymi kwiatami i prostą wiarą tatrzańskich górali.",
            "funkcja": "Dowodzi ponadczasowości myśli franciszkańskiej: pokazuje, że średniowieczna pochwała prostoty i pokory stała się skutecznym lekarstwem na kryzysy duchowe kolejnych stuleci."
          }
        ]
      },

      # 38. WILLIAM SZEKSPIR - ROMEO I JULIA
      {
        "id": "szekspir-romeo-i-julia",
        "kategoria": "dodatkowy",
        "kategoriaNazwa": "Lektury dodatkowe",
        "tytul": "Romeo i Julia",
        "autor": "William Szekspir",
        "epoka": "Renesans / Teatr elżbietański",
        "gatunek": "Tragedia miłosna",
        "motywy": ["miłość tragiczna", "zwaśnione rody", "konflikt pokoleń", "przypadek a fatum", "przełamanie konwenansów", "śmierć kochanków"],
        "synteza": "Dzieje dwojga młodych kochanków z Werony, których miłość staje się ofiarą odwiecznej nienawiści rodów Montekich i Kapuletich; ich samobójcza śmierć w grobowcu kładzie kres krwawemu konfliktowi ich rodzin.",
        "tematyMaturalne": [
          "Miłość silniejsza niż rodowa nienawiść – walka uczucia z konwenansami społecznymi.",
          "Rola nieszczęśliwego przypadku i przeznaczenia w tragedii bohaterów.",
          "Cena, jaką dzieci płacą za błędy i uprzedzenia rodziców."
        ],
        "konteksty": [
          {
            "typ": "Kontekst antyczno-mitologiczny",
            "zrodloZewnetrzne": "Poemat Owidiusza „Metamorfozy” (Księga IV) – mit o nieszczęśliwych kochankach Pyramie i Tyzbe",
            "tytul": "Antyczny archetyp kochanków rozdzielonych przez zakazy rodziców",
            "opis": "Owidiusz opisał babilońskich kochanków, którym rodzice zabronili ślubu. Młodzi rozmawiali przez szczelinę w murze dzielącym ich domy i umówili się na schadzkę przy grobowcu Ninusa. Zbieg okoliczności z zakrwawioną chustą i lwem sprawił, że Pyram sądząc, iż Tyzbe zginęła, przebił się mieczem, a powracająca dziewczyna odebrała sobie życie tym samym ostrzem.",
            "funkcja": "Wskazuje na starożytny rodowód fabuły Szekspira: dowodzi, że motyw tragicznej miłości i fatalnego nieporozumienia przy grobowcu jest odwiecznym archetypem kultury śródziemnomorskiej."
          },
          {
            "typ": "Kontekst nowelistyczno-źródłowy",
            "zrodloZewnetrzne": "Renesansowa nowela włoska Mattea Bandello (1554 r.) oraz angielski poemat Arthura Brooke’a „The Tragical History of Romeus and Juliet” (1562 r.)",
            "tytul": "Renesansowe źródła literackie dramatu Szekspira",
            "opis": "Szekspir nie wymyślił fabuły z Weroną od zera – oparł się bezpośrednio na angielskim tłumaczeniu noweli Bandella dokonanym przez Brooke'a. Brooke potępiał jednak kochanków za nieposłuszeństwo wobec rodziców. Szekspir dokonał genialnej zmiany: zdjął z młodych moralną winę, skondensował czas akcji z dziewięciu miesięcy do zaledwie pięciu upalnych dni i uczynił z nich niewinne ofiary rodowej ślepoty dorosłych.",
            "funkcja": "Ukazuje kunszt dramatopisarski Szekspira: autor przekształcił dydaktyczną, moralizatorską nowelkę w wielką, uniwersalną tragedię o prawie jednostki do wolnego wyboru uczucia."
          },
          {
            "typ": "Kontekst historyczno-społeczny",
            "zrodloZewnetrzne": "Realia rodowych wendet (faida) w renesansowych Włoszech oraz patriarchalne prawo małżeńskie",
            "tytul": "Krwawa wendeta klanowa a traktowanie małżeństwa jako kontraktu majątkowego",
            "opis": "W miastach-państwach renesansowych Włoch (Werona, Florencja) prywatne wendety między arystokratycznymi rodami paraliżowały życie publiczne i skutkowały krwawymi bójkami na ulicach. Jednocześnie córka była traktowana przez ojca jak własność rodowa – pan Kapulet aranżuje ślub 14-letniej Julii z hrabią Parysem bez pytania jej o zdanie, grożąc jej wyrzuceniem z domu na bruk w razie sprzeciwu.",
            "funkcja": "Podkreśla rewolucyjny charakter miłości Romea i Julii: ich potajemny ślub był nie tylko uniesieniem serca, lecz aktem buntu przeciwko patriarchalnej opresji i rodowej nienawiści niszczącej miasto."
          }
        ]
      },

      # 39. ADAM MICKIEWICZ - KONRAD WALLENROD
      {
        "id": "mickiewicz-konrad-wallenrod",
        "kategoria": "dodatkowy",
        "kategoriaNazwa": "Lektury dodatkowe",
        "tytul": "Konrad Wallenrod",
        "autor": "Adam Mickiewicz",
        "epoka": "Romantyzm",
        "gatunek": "Powieść poetycka",
        "motywy": ["wallenrodyzm", "zdrada w imię ojczyzny", "machiawelizm", "moralna klęska bohatera", "rola poezji (Pieśń Wajdeloty)", "tragizm losu"],
        "synteza": "Tragiczna historia litewskiego patrioty Waltera Alfa, który wychowany przez Krzyżaków pod przybranym nazwiskiem Konrada Wallenroda zdobywa godność Wielkiego Mistrza Zakonu, by podstępem doprowadzić go do militarnej klęski, płacąc za ocalenie Litwy utratą honoru, miłości Aldony i śmiercią samobójczą.",
        "tematyMaturalne": [
          "Czy cel uświęca środki? Moralne granice walki o wolność ojczyzny.",
          "Tragizm wallenrodyzmu – cena zdrady i złamania kodeksu rycerskiego.",
          "Poezja jako strażniczka tożsamości i pamięci narodowej (Pieśń Wajdeloty)."
        ],
        "konteksty": [
          {
            "typ": "Kontekst filozoficzno-polityczny",
            "zrodloZewnetrzne": "Traktat polityczny Niccolò Machiavellego „Książę” (Il Principe, 1532 r.) – rozdział XVIII i maksyma o lisie i lwie",
            "tytul": "Motto utworu: „Macie bowiem wiedzieć, że są dwa sposoby walczenia... trzeba być lisem i lwem”",
            "opis": "Mickiewicz zaczerpnął motto bezpośrednio z Machiavellego: naród słaby militarnie w starciu z potężnym imperium nie ma szans w otwartej walce (metoda lwa), dlatego musi sięgnąć po chytrość, zdradę i kamuflaż (metoda lisa). Wallenrod łamie rycerską przysięgę chrześcijańską, udaje lojalnego brata zakonnego i prowadzi Krzyżaków w bagna pod Kownem, niszcząc ich armię.",
            "funkcja": "Definiuje istotę pojęcia wallenrodyzmu: ukazuje nierozwiązywalny konflikt moralny patrioty, który ratuje ojczyznę metodami podłymi, płacąc za to całkowitym rozpadem własnego sumienia i śmiercią moralną."
          },
          {
            "typ": "Kontekst historyczno-cenzuralny",
            "zrodloZewnetrzne": "Konspiracja w Królestwie Polskim przed powstaniem listopadowym (Towarzystwo Patriotyczne Waleriana Łukasińskiego) i carska cenzura w Petersburgu (1828 r.)",
            "tytul": "Historyczny kamuflaż krzyżacki jako wezwanie do walki z caratem",
            "opis": "Mickiewicz napisał i wydał utwór w Petersburgu, gdzie przebywał na zesłaniu. Aby ominąć carską cenzurę, zastosował kamuflaż historyczny: przeniósł akcję w realia XIV-wiecznych wojen litewsko-krzyżackich. Dla polskich czytelników aluzja była krystalicznie jasna: Krzyżacy reprezentowali zaborczą Rosję carską, a podstęp Wallenroda był instrukcją spiskową dla oficerów w Warszawie (późniejszych podchorążych Wysockiego).",
            "funkcja": "Wyjaśnia polityczną rolę utworu: poemat stał się bezpośrednim katalizatorem wybuchu powstania listopadowego w 1830 r., zgodnie ze słynnym powiedzeniem: 'Słowo stało się ciałem, a Wallenrod Belwederem'."
          },
          {
            "typ": "Kontekst estetyczno-literacki",
            "zrodloZewnetrzne": "Angielska powieść poetycka George'a Gordona Byrona („Giaur”, „Korsarz”) i koncepcja bohatera bajronicznego",
            "tytul": "Bohater bajroniczny w kostiumie bojownika o wolność narodu",
            "opis": "Wallenrod wykazuje wszystkie cechy mrocznego bohatera bajronicznego: jest samotnikiem otoczonym tajemnicą, gardzi otoczeniem, pije na umór, nosi w sercu krwawą ranę i popełnia samobójstwo z kielichem trucizny. Mickiewicz przekształcił jednak ten zachodni model: u Byrona bohater walczył z pobudek czysto egoistycznych lub miłosnych, u Mickiewicza został podporządkowany nadrzędnemu obowiązkowi patriotycznemu.",
            "funkcja": "Ułatwia analizę konstrukcji psychologicznej Konrada: łączy romantyczny bunt i tragizm samotności z polskim etosem poświęcenia życia i zbawienia duszy dla ratowania narodu."
          }
        ]
      },

      # 40. ZYGMUNT KRASIŃSKI - NIE-BOSKA KOMEDIA
      {
        "id": "krasinski-nie-boska-komedia",
        "kategoria": "dodatkowy",
        "kategoriaNazwa": "Lektury dodatkowe",
        "tytul": "Nie-Boska Komedia",
        "autor": "Zygmunt Krasiński",
        "epoka": "Romantyzm",
        "gatunek": "Dramat romantyczny / dramat racji historiozoficznych",
        "motywy": ["rewolucja społeczna", "walka klas", "fałszywa poezja", "Hrabia Henryk i Pankracy", "Opatrzność Boża", "Galilaee, vicisti!"],
        "synteza": "Wizyjny dramat historiozoficzny przedstawiający wybuch krwawej rewolucji mas ludowych pod wodzą Pankracego przeciwko zdegenerowanej arystokracji dowodzonej przez Hrabiego Henryka w Okopach Świętej Trójcy, zakończony zagładą obu obozów i interwencją Chrystusa Sędziego.",
        "tematyMaturalne": [
          "Obraz rewolucji społecznej – sprawiedliwy odwet mas czy ślepa zagłada kultury?",
          "Dramat racji cząstkowych: starcie konserwatyzmu Hrabiego Henryka z rewolucjonizmem Pankracego.",
          "Tragizm poety przeklętego i krytyka poezji oderwanej od odpowiedzialności moralnej."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-społeczny",
            "zrodloZewnetrzne": "Rewolucja lipcowa we Francji (1830 r.), krwawe powstanie tkaczy w Lyonie (1831 r.) oraz narodziny socjalizmu utopijnego",
            "tytul": "Wrzenie rewolucyjne w Europie Zachodniej i narodziny walki klasowej",
            "opis": "Krasiński, pochodzący z magnackiego rodu hrabiowskiego, z przerażeniem obserwował w Europie Zachodniej bunty robotników fabrycznych i hasła Saint-Simona domagające się likwidacji własności prywatnej i religii. Pisarz z profetyczną trafnością przewidział, że kolejnym etapem historii nie będą walki narodowowyzwoleńcze, lecz globalna, totalna wojna klasowa biednych przeciw bogatym.",
            "funkcja": "Nadaje dramatowi wymiar historiozoficzny: utwór był genialnym, wyprzedzającym manifest Marksa o kilkanaście lat ostrzeżeniem przed krwawymi totalitaryzmami rewolucyjnymi XX wieku."
          },
          {
            "typ": "Kontekst filozoficzno-historiozoficzny",
            "zrodloZewnetrzne": "Filozofia dziejów Georga Wilhelma Friedricha Hegla – dialektyka tezy i antytezy a chrześcijański prowidencjalizm",
            "tytul": "Dialektyka dziejów i pojęcie racji cząstkowych a ostateczny sąd Opatrzności",
            "opis": "U Hegla historia rozwija się poprzez ścieranie się przeciwieństw: arystokracja u Krasińskiego to teza (obrońcy wiary i dawnej kultury, lecz skompromitowani pychą i uciskiem poddanych), rewolucjoniści to antyteza (mają rację, żądając chleba, lecz niosą nihilizm, mord i ateizm). Żadna ze stron nie posiada racji absolutnej. Ostateczną syntezą historii nie jest jednak ludzki porządek, lecz nadprzyrodzona interwencja Opatrzności Bożej.",
            "funkcja": "Tłumaczy finałową scenę dramatu: Pankracy zwycięża militarnie, lecz pada rażony piorunem na widok objawiającego się na niebie Chrystusa z okrzykiem: 'Galilaee, vicisti!' (Galilejczyku, zwyciężyłeś!), co dowodzi, że ludzkie próby zbudowania raju przez zbrodnię kończą się boskim sądem."
          },
          {
            "typ": "Kontekst literacko-polemiczny",
            "zrodloZewnetrzne": "Poemat Dantego Alighieri „Boska Komedia” (La Divina Commedia, XIV w.)",
            "tytul": "Tytuł jako gorzka polemika z dantejską wizją harmonii boskiego kosmosu",
            "opis": "U Dantego wędrówka przez piekło i czyściec prowadziła do raju i poznania wiecznego ładu boskiego. Krasiński świadomie zatytułował swój dramat 'Nie-Boska Komedia', aby podkreślić, że świat ludzi odrzucających Boga staje się groteskowym, bezsensownym chaosem – piekłem na ziemi, gdzie zdrada małżeńska, obłęd żony i rzeź klasowa niszczą wszelkie wartości.",
            "funkcja": "Stanowi klucz interpretacyjny do części rodzinnej: jest bezwzględną autokrytyką romantycznego kultu poezji, która zamiast uszlachetniać, staje się przyczyną tragedii rodzinnej (Hrabia Henryk jako 'poeta przeklęty', niszczący Marię i małego Orcia)."
          }
        ]
      },

      # 41. ADAM MICKIEWICZ - PAN TADEUSZ
      {
        "id": "mickiewicz-pan-tadeusz",
        "kategoria": "dodatkowy",
        "kategoriaNazwa": "Lektury dodatkowe / Szkoła Podstawowa",
        "tytul": "Pan Tadeusz (w tym księgi I, II, IV, X, XI, XII)",
        "autor": "Adam Mickiewicz",
        "epoka": "Romantyzm",
        "gatunek": "Epopeja narodowa",
        "motywy": ["Soplicowo jako arkadia", "rehabilitacja Jacka Soplicy (ks. Robak)", "zajazd szlachecki", "Koncert Jankiela", "wyprawa Napoleona 1812 r.", "kultura sarmacka"],
        "synteza": "Narodowa epopeja przedstawiająca dworek w Soplicowie w przededniu wyprawy Napoleona na Rosję (1811–1812), gdzie prywatny spór o zamek Horeszków przeplata się z patriotyczną misją emisariusza księdza Robaka i marzeniem o zmartwychwstaniu wolnej Rzeczypospolitej.",
        "tematyMaturalne": [
          "Dworek w Soplicowie jako ostoja polskiej tożsamości, obyczaju i patriotyzmu.",
          "Przemiana Jacka Soplicy – od dumnego warchoła do pokornego sługi narodu.",
          "Koncert Jankiela jako muzyczna synteza węzłowych wydarzeń z historii Polski."
        ],
        "konteksty": [
          {
            "typ": "Kontekst historyczno-militarny",
            "zrodloZewnetrzne": "Wyprawa Wielkiej Armii Napoleona na Rosję (1812 r.) i formowanie 100-tysięcznego korpusu Wojska Polskiego pod wodzą księcia Józefa Poniatowskiego",
            "tytul": "Mityczna „wiosna roku 1812” jako moment największych nadziei niepodległościowych",
            "opis": "Wkroczenie wojsk francuskich i polskich legionów na Litwę w czerwcu 1812 r. zostało zapamiętane przez współczesnych jako chwila narodowego cudu i entuzjazmu. Rok ten obfitował w niezwykłe zjawiska przyrodnicze (wielka kometa z 1811 r., urodzaj zbóż). Mickiewicz ukazuje przemarsz wojsk generała Dąbrowskiego przez Soplicowo jako mityczny moment zjednoczenia skłóconej szlachty ponad dawnymi urazami.",
            "funkcja": "Niezbędny kontekst historyczny: wyjaśnia radosny, pełen światła ton ksiąg XI i XII; epopeja utrwala w pamięci zbiorowej Polaków moment, gdy wolność wydawała się na wyciągnięcie ręki."
          },
          {
            "typ": "Kontekst biograficzno-emigracyjny",
            "zrodloZewnetrzne": "Kłótnie polskiej Wielkiej Emigracji w Paryżu po 1831 r. (obóz ks. Czartoryskiego vs Towarzystwo Demokratyczne Polskie) oraz „Epilog” epopei",
            "tytul": "Paryska nostalgia i ucieczka poety od zgorzknienia emigracji do „kraju lat dziecinnych”",
            "opis": "Mickiewicz pisał poemat w Paryżu w latach 1832–1834, otoczony skłóconymi, obwiniającymi się wzajemnie o klęskę powstania emigrantami. W słynnym Epilogu poeta wyznaje, że ucieka od 'przeklętych swarów na paryskim bruku' w idealizowany świat dzieciństwa na Nowogródczyźnie, który w jego wspomnieniach pozostał 'święty i czysty jak pierwsze kochanie'.",
            "funkcja": "Tłumaczy arkadyjski, pełen ciepła i humoru charakter Soplicowa: Mickiewicz nie pisał bezkrytycznego peanu na cześć pijaństwa sarmackiego, lecz stworzył mit ojczyzny idealnej, by ukoić rany i wlać nadzieję w serca wygnanych rodaków."
          },
          {
            "typ": "Kontekst kulturowo-pamiętnikarski",
            "zrodloZewnetrzne": "Sarmacka literatura obyczajowa i pamiętnikarska (Jędrzej Kitowicz „Opis obyczajów za panowania Augusta III”, Jan Chryzostom Pasek)",
            "tytul": "Soplicowo jako muzeum ginącej kultury staropolskiej (grzybobranie, polowanie, polonez)",
            "opis": "Mickiewicz z etnograficzną precyzją utrwalił na kartach epopei odchodzący świat kultury szlacheckiej: hierarchię precedencji przy stole, rytuał parzenia kawy, polowanie z ogarami, grzybobranie, grę na rogu Wojskiego i finałowy polonez prowadzony przez Podkomorzego. Korzystał przy tym z bezcennych relacji ks. Jędrzeja Kitowicza opisującego detale staropolskiego stroju kontuszowego i biesiad.",
            "funkcja": "Ukazuje epopeję jako arcydzieło kultury pamięci narodowej: Mickiewicz zdawał sobie sprawę, że dawna Polska bezpowrotnie odchodzi w przeszłość pod naporem nowoczesności i zaborów, dlatego ocalił jej najpiękniejsze barwy dla przyszłych pokoleń."
          }
        ]
      }
    ]

if __name__ == '__main__':
    lektury = get_all_lektury()
    print(f"Liczba przygotowanych lektur: {len(lektury)}")
    
    # Zapis do data.js z formatem JS
    js_content = "// Baza danych 41 lektur z 3 ŚCIŚLE ZEWNĘTRZNYMI kontekstami interpretacyjnymi do każdej lektury\n"
    js_content += "// Informacje w kontekstach są zewnętrzne wobec dzieła (fakt historyczny, dokument, filozofia, inne dzieło sztuki, biografia)\n"
    js_content += "// Zgodne z wymaganiami CKE na egzamin maturalny (Formuła 2023-2026)\n\n"
    js_content += "const LEKTURY_DATA = " + json.dumps(lektury, ensure_ascii=False, indent=2) + ";\n\n"
    js_content += "if (typeof window !== 'undefined') {\n  window.LEKTURY_DATA = LEKTURY_DATA;\n}\n"
    js_content += "if (typeof module !== 'undefined' && module.exports) {\n  module.exports = LEKTURY_DATA;\n}\n"

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Zapisano pomyślnie data.js!")
