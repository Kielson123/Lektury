// Baza danych lektur i 3 kontekstów interpretacyjnych do każdej z nich
// Zgodne z wymaganiami CKE (Formuła 2023/2024/2025/2026)

const LEKTURY_DATA = [
  // ==========================================
  // ZAKRES PODSTAWOWY
  // ==========================================
  {
    id: "biblia",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Biblia (fragmenty Księgi Rodzaju, Hioba, Koheleta, Psalmów, Apokalipsy św. Jana)",
    autor: "Autorzy natchnieni (praca zbiorowa)",
    epoka: "Starożytność",
    gatunek: "Księgi święte / poemat filozoficzny, zbiór hymnów, apokalipsa",
    motywy: ["cierpienie", "vanitas", "stworzenie świata", "eschatologia", "wiara", "bunt i pokora"],
    synteza: "Fundament kultury śródziemnomorskiej; zbiór ksiąg religijnych tłumaczących pochodzenie świata, sens cierpienia niezawinionego, marność dóbr doczesnych oraz ostateczny los ludzkości.",
    tematyMaturalne: [
      "Sens ludzkiego cierpienia w świetle doświadczeń człowieka.",
      "Marność świata doczesnego a poszukiwanie wartości trwałych.",
      "Wizje końca świata i sądu ostatecznego w literaturze."
    ],
    konteksty: [
      {
        typ: "Archetypiczny / Mitologiczny",
        tytul: "Topos cierpienia niezawinionego – Księga Hioba a mit o Prometeuszu",
        opis: "Hiob jest archetypem człowieka dotkniętego cierpieniem niezawinionym, który mimo utraty majątku, dzieci i zdrowia nie przeklina Boga, lecz zmaga się z tajemnicą cierpienia. Można zestawić go z greckim mitem o Prometeuszu, który również cierpiał bez winy, lecz jego bunt miał charakter antyteistyczny, podczas gdy postawa Hioba ostatecznie prowadzi do pokornego uznania transcendencji Stwórcy.",
        funkcja: "Pozwala ukazać dwa odmienne wzorce kulturowe znoszenia cierpienia: bunt prometejski (grecki heroizm) oraz zaufanie tajemnicy Boga ponad ludzkim rozumem (judeochrześcijańska teodycea)."
      },
      {
        typ: "Filozoficzny",
        tytul: "Filozofia vanitas Księgi Koheleta a pesymizm Arthura Schopenhauera i egzystencjalizm",
        opis: "Koheletowa sentencja „Vanitas vanitatum et omnia vanitas” (Marność nad marnościami i wszystko marność) wskazuje na ulotność ludzkich dążeń: bogactwa, mądrości i sławy w obliczu nieuchronnej śmierci. Koresponduje to z dziewiętnastowieczną filozofią Artura Schopenhauera o bezsensie pogoni za pragnieniami oraz dwudziestowiecznym egzystencjalizmem, podkreślającym poczucie absurdu istnienia bez zakorzenienia w wartościach wyższych.",
        funkcja: "Służy do udowodnienia, że motyw przemijania i poczucie bezsensu doczesności nie są domeną wyłącznie nowoczesności, lecz odwiecznym pytaniem filozoficznym o hierarchię wartości człowieka."
      },
      {
        typ: "Intertekstualny / Literacki",
        tytul: "Apokalipsa św. Jana a „Piosenka o końcu świata” Czesława Miłosza",
        opis: "Janowa Apokalipsa operuje grozą, kosmicznymi kataklizmami, potworami i pieczęciami, budując patetyczny obraz Sądu Ostatecznego. Czesław Miłosz w wierszu „Piosenka o końcu świata” dokonuje dekonstrukcji tego biblijnego schematu – koniec świata dokonuje się niepostrzeżenie w zwykły, słoneczny dzień, a staruszek przewiązujący pomidory przypomina, że „innego końca świata nie będzie”.",
        funkcja: "Pozwala ukazać kontrast między patetyczną wizją biblijnej eschatologii a dwudziestowiecznym doświadczeniem codziennego przemijania i pamięcią o katastrofie wojennej."
      }
    ]
  },
  {
    id: "parandowski-mitologia",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Mitologia, cz. I Grecja",
    autor: "Jan Parandowski",
    epoka: "Starożytność (rekonstrukcja XX w.)",
    gatunek: "Zbiór mitów",
    motywy: ["archetypy", "fatum", "heroizm", "bunt", "natura ludzka", "przeznaczenie"],
    synteza: "Literackie opracowanie wierzeń starożytnych Greków, ukazujące narodziny bogów, herosów oraz archetypiczne sytuacje ludzkiego losu.",
    tematyMaturalne: [
      "Mity jako uniwersalne opowieści o kondycji człowieka.",
      "Pragnienie przekraczania granic – odwaga czy pycha?",
      "Cena buntu w imię dobra ludzkości."
    ],
    konteksty: [
      {
        typ: "Psychologiczny / Psychoanalityczny",
        tytul: "Koncepcja archetypów i nieświadomości zbiorowej Carla Gustava Junga",
        opis: "Zgodnie z teorią psychologii głębi C.G. Junga mity greckie nie są jedynie naiwnymi bajkami, lecz projekcjami archetypów – uniwersalnych wzorców tkwiących w nieświadomości zbiorowej każdego człowieka (np. archetyp Cienia, Wielkiej Matki, Wyprawy Bohatera czy Narcyza).",
        funkcja: "Uzasadnia nieprzemijającą aktualność mitów; pozwala dowieść, że opowieści o Dedalu, Ikarze czy Demeter opisują uniwersalne mechanizmy psychologiczne i relacje międzyludzkie."
      },
      {
        typ: "Filozoficzno-egzystencjalny",
        tytul: "Mit o Syzyfie w ujęciu eseju Alberta Camusa",
        opis: "W mitologii greckiej Syzyf jest przebiegłym władcą ukaranym przez bogów wiecznym wtaczaniem głazu. Albert Camus w eseju „Mit Syzyfa” czyni z niego uosobienie człowieka absurdalnego, który ma pełną świadomość beznadziejności swego trudu, lecz buntuje się poprzez uśmiech i afirmację wysiłku („Trzeba wyobrażać sobie Syzyfa szczęśliwym”).",
        funkcja: "Ukazuje ewolucję odczytania postaci mitologicznej: od przestrogi przed pychą (hybris) w starożytności do symbolu heroizmu i godności ludzkiej w filozofii egzystencjalnej XX wieku."
      },
      {
        typ: "Kulturowo-malarski",
        tytul: "Mit o Ikarze w malarstwie Pietera Bruegla („Pejzaż z upadkiem Ikara”)",
        opis: "Słynne płótno Bruegla z XVI w. przedstawia dramat Ikara zepchnięty na daleki, ledwo zauważalny plan – widać jedynie nogi tonącego chłopca w wodzie, podczas gdy na pierwszym planie oracz spokojnie uprawia pole, a pasterz patrzy w niebo. Obraz ten zainspirował m.in. Tadeusza Różewicza i W.H. Audena.",
        funkcja: "Stanowi kontekst artystyczny ilustrujący obojętność świata wobec jednostkowej tragedii i zderzenie wzniosłego idealizmu z pragmatyczną codziennością."
      }
    ]
  },
  {
    id: "homer-iliada",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Iliada (fragmenty)",
    autor: "Homer",
    epoka: "Starożytność",
    gatunek: "Epos heroiczny",
    motywy: ["wojna", "honor", "gniew", "fatum", "arete", "żałoba i pojednanie"],
    synteza: "Opis 49 dni z ostatniego roku wojny trojańskiej, skupiony wokół gniewu Achillesa, tragizmu Hektora i bezlitosnego fatum ciążącego nad ludźmi.",
    tematyMaturalne: [
      "Wojna jako sprawdzian człowieczeństwa i źródło cierpienia.",
      "Bohater tragiczny wobec wyroków przeznaczenia.",
      "Pojednanie ponad podziałami w obliczu śmierci."
    ],
    konteksty: [
      {
        typ: "Kulturowo-obyczajowy",
        tytul: "Antyczny etos rycerski oraz pojęcia arete i kalokagatii",
        opis: "Kultura homerycka opierała się na ideale arete (dzielności, cnoty rycerskiej) oraz dążeniu do pośmiertnej sławy (kleos), która stanowiła jedyny sposób na pokonanie niebytu. Achilles woli krótkie, lecz chwalebne życie wojownika od długiej i spokojnej egzystencji bez sławy.",
        funkcja: "Pomaga zrozumieć motywacje bohaterów, dla których utrata honoru (odebranie Bryzeidy Achillesowi przez Agamemnona) była gorsza niż śmierć i determinowała losy całej wojny."
      },
      {
        typ: "Filozoficzno-religijny",
        tytul: "Determinizm starożytny – koncepcja Mojry (Fatum) a wolna wola",
        opis: "W świecie przedstawionym Iliady losem ludzi, a nawet bogów, rządzi nieodwołalne przeznaczenie (Mojra / Ananke). Złota waga Zeusa jedynie waży losy Hektora i Achillesa, wskazując wyrok, którego nikt nie może zmienić.",
        funkcja: "Podkreśla tragizm człowieka antycznego, którego wielkość objawia się nie w uniknięciu przeznaczenia, lecz w godnym stawieniu mu czoła mimo świadomości nieuchronnej klęski."
      },
      {
        typ: "Intertekstualny / Współczesny",
        tytul: "„Głosy z przeszłości” – wiersz Zbigniewa Herberta „Do Marka Aurelego” lub motyw Achillesa w literaturze wojennej",
        opis: "Scena spotkania Priama z zabójcą swego syna, Achillesem (Księga XXIV), w której obaj płaczą nad wspólnym ludzkim losem, stanowi uniwersalny topos humanitaryzmu. Zbigniew Herbert wielokrotnie odwoływał się do antyku, wskazując, że mimo zniszczeń wojennych to zdolność do współczucia stanowi fundament cywilizacji.",
        funkcja: "Umożliwia interpretację sceny wykupienia zwłok Hektora jako triumfu ludzkiej empatii nad prawem wojny i bezwzględną żądzą zemsty."
      }
    ]
  },
  {
    id: "sofokles-antygona",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Antygona",
    autor: "Sofokles",
    epoka: "Starożytność",
    gatunek: "Tragedia antyczna",
    motywy: ["konflikt tragiczny", "prawo boskie a ludzkie", "władza", "bunt", "rodzina", "hybris"],
    synteza: "Dramatyczne starcie Antygony, broniącej świętego prawa do pochówku brata, z Kreonem, stojącym na straży autorytetu państwa i prawa stanowionego.",
    tematyMaturalne: [
      "Jednostka wobec prawa i autorytetu władzy.",
      "Konflikt równorzędnych racji jako źródło tragedii.",
      "Kobieta jako buntowniczka w literaturze."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-prawny",
        tytul: "Koncepcja prawa naturalnego (lex naturalis) a prawo stanowione (lex humana)",
        opis: "Spór Antygony z Kreonem jest klasycznym dylematem filozofii prawa. Antygona reprezentuje odwieczne, niezapisane prawa boskie i moralne (prawo naturalne), które stoją wyżej niż dekrety władców. Kreon uosabia rację stanu i bezwzględne posłuszeństwo literze prawa pozytywnego, bez którego państwu grozi anarchia.",
        funkcja: "Pozwala ukazać istotę konfliktu tragicznego – obie strony reprezentują racje logicznie uzasadnione w swoich systemach wartości, co uniemożliwia bezkrwawy kompromis."
      },
      {
        typ: "Historyczno-polityczny",
        tytul: "Funkcjonowanie ateńskiej polis w dobie klasycznej (wiek Peryklesa)",
        opis: "Sztuka Sofoklesa była wystawiana w demokratycznych Atenach V w. p.n.e. Kreon z początku jawi się jako odpowiedzialny wódz dbający o porządek po wojnie domowej, lecz w toku akcji ulega uwiądowi władzy (autorytaryzmowi), odrzucając głos ludu i mędrców (Tejrezjasza).",
        funkcja: "Służy do analizy portretu władcy i mechanizmów tyranii; dowodzi, że dramat był ostrzeżeniem dla obywateli polis przed zgubnymi skutkami pychy rządzących i lekceważenia opinii publicznej."
      },
      {
        typ: "Współczesny / Literacki",
        tytul: "Marek Edelman w „Zdążyć przed Panem Bogiem” Hanny Krall jako „Antygona XX wieku”",
        opis: "Marek Edelman w getcie warszawskim walczył o prawo do godnej śmierci i pamięci dla mordowanego narodu żydowskiego, sprzeciwiając się zbrodniczemu prawu okupanta. Podobnie jak Antygona, pozostał wierny swoim moralnym obowiązkom wobec zmarłych i cierpiących na przekór terrorowi.",
        funkcja: "Ukazuje ponadczasowość postawy heroicznego sprzeciwu wobec nieludzkiego prawa w realiach totalitarnych XX wieku."
      }
    ]
  },
  {
    id: "lament-swietokrzyski",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Lament świętokrzyski (Żale Matki Boskiej pod krzyżem)",
    autor: "Anonim",
    epoka: "Średniowiecze",
    gatunek: "Plankt (lament / pieśń żałobna)",
    motywy: ["cierpienie matki", "humanizacja sacrum", "compassio", "śmierć Chrystusa", "żałoba"],
    synteza: "Monolog Maryi stojącej pod krzyżem, która nie jako Królowa Niebios, lecz jako bezradna, kochająca matka opłakuje mękę swego jedynego Syna i szuka współczucia u innych matek.",
    tematyMaturalne: [
      "Obraz cierpienia matki w literaturze.",
      "Humanizacja wizerunku sacrum w sztuce średniowiecza.",
      "Różne oblicza żałoby i bezradności wobec śmierci."
    ],
    konteksty: [
      {
        typ: "Kulturowo-teologiczny",
        tytul: "Motyw Stabat Mater Dolorosa i mistyka franciszkańska XV wieku",
        opis: "W późnym średniowieczu pod wpływem ruchu franciszkańskiego rozwinęła się idea 'compassio' (współcierpienia). Odeszto od hieratycznego, chłodnego przedstawiania Maryi na rzecz Matki Bolejącej (Mater Dolorosa), która cierpi po ludzku. 'Lament świętokrzyski' wpisuje się w ten nurt, ukazując Maryję pragnącą otrzeć krew Syna i podzielić z Nim rany.",
        funkcja: "Pozwala wyjaśnić proces 'humanizacji sacrum' – zbliżenia postaci biblijnych do zwykłego człowieka, aby wierny mógł utożsamić się z ich cierpieniem."
      },
      {
        typ: "Sztuka / Ikonograficzny",
        tytul: "Rzeźba piety w sztuce gotyckiej (np. Pietà z Tubądzina, Pietà z Lubiąża)",
        opis: "W sztukach plastycznych XIV i XV wieku niezwykłą popularność zyskał motyw piety – rzeźbiarskiego przedstawienia Maryi trzymającej na kolanach martwe ciało Jezusa. Podobnie jak w 'Lamencie...', akcentowano w tych rzeźbach fizyczny ból, skurcz mięśni i matczyną rozpacz.",
        funkcja: "Stanowi kontekst plastyczny unaoczniający jedność ówczesnej kultury: ten sam motyw realizowano w poezji wernakularnej (w języku narodowym) oraz w rzeźbie sakralnej."
      },
      {
        typ: "Intertekstualny / Literacki",
        tytul: "Krzysztof Kamil Baczyński „Elegia o... [chłopcu polskim]”",
        opis: "Wiersz Baczyńskiego z 1944 roku jest monologiem polskiej matki opłakującej syna poległego w powstaniu warszawskim. Poeta posłużył się stylizacją na 'Lament świętokrzyski' – matka mówi do syna o jego zniszczonej młodości, a jego śmierć w walce z okupantem zyskuje rys ofiary chrystusowej.",
        funkcja: "Dowodzi uniwersalizmu toposu matki cierpiącej; umożliwia zestawienie średniowiecznego planktu z wojenną poezją pokolenia Kolumbów."
      }
    ]
  },
  {
    id: "rozmowa-polikarpa",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Rozmowa Mistrza Polikarpa ze Śmiercią (fragmenty)",
    autor: "Anonim",
    epoka: "Średniowiecze",
    gatunek: "Dialog wierszowany, satyra stanowa",
    motywy: ["danse macabre", "śmierć", "równość wobec śmierci", "memento mori", "groteska", "satyra stanowa"],
    synteza: "Uczony Polikarp prosi Boga o ujrzenie Śmierci. Zjawa w postaci rozkładającego się kobiecego trupa z kosą ukazuje swoją niszczycielską moc i przypomina, że nikt – od papieża po żebraka – nie uniknie jej wyroku.",
    tematyMaturalne: [
      "Motyw tańca śmierci (danse macabre) i jego rola w kulturze.",
      "Egalitaryzm śmierci a krytyka wad społecznych.",
      "Groteskowy obraz śmierci w literaturze dawnej i współczesnej."
    ],
    konteksty: [
      {
        typ: "Kulturowo-historyczny",
        tytul: "Topos Danse Macabre po pandemii Czarnej Śmierci (1347–1351)",
        opis: "Masowe epidemie dżumy w XIV-wiecznej Europie wywołały głęboki szok cywilizacyjny i uświadomiły ludziom kruchość życia. Śmierć w sztuce i literaturze zyskała status wszechobecnej tancerki porywającej przedstawicieli wszystkich stanów do korowodu, co uczyło zasady 'memento mori'.",
        funkcja: "Tłumaczy genezę fascynacji makabrą w utworze oraz wskazuje na dydaktyczny cel tekstu: przygotowanie człowieka na nagły zgon (ars moriendi)."
      },
      {
        typ: "Społeczno-historyczny",
        tytul: "Egalitaryzm śmierci jako narzędzie satyry społecznej i antyklerykalnej",
        opis: "Śmierć w 'Rozmowie...' z lubością wymienia swoje ofiary: przekupnych sędziów, rozpustnych mnichów, karczmarzy dolewających wody do piwa i chciwych lekarzy. W ten sposób średniowieczny autor wykorzystał motyw eschatologiczny do bezwzględnego rozliczenia ówczesnych elit.",
        funkcja: "Pozwala ukazać utwór nie tylko jako tekst religijny, lecz jako odważną średniowieczną satyrę społeczną, demaskującą hipokryzję stanów uprzywilejowanych."
      },
      {
        typ: "Współczesny / Filmowy",
        tytul: "Film Ingmara Bergmana „Siódma pieczęć” (1957) lub poezja Wisławy Szymborskiej",
        opis: "U Bergmana rycerz Antonius Block gra ze Śmiercią w szachy o swoje życie w świecie spustoszonym przez zarazę. Z kolei Szymborska w wierszu „O śmierci bez przesady” polemizuje ze średniowieczną personifikacją, zauważając, że śmierć „nie zna się na żartach, na gwiazdach, na mostach” i jest bezradna wobec życia.",
        funkcja: "Pozwala skonfrontować średniowieczny makabryczny i groteskowy wizerunek Śmierci z jej egzystencjalnymi oraz zdemitologizowanymi ujęciami w kulturze XX wieku."
      }
    ]
  },
  {
    id: "piesn-o-rolandzie",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Pieśń o Rolandzie (fragmenty)",
    autor: "Anonim (przypisywana Turoldowi)",
    epoka: "Średniowiecze",
    gatunek: "Chanson de geste (pieśń o czynach)",
    motywy: ["etos rycerski", "honor", "patriotyzm", "wierność Bogu i władcy", "ars moriendi"],
    synteza: "Opowieść o wyprawie Karola Wielkiego i bohaterskiej śmierci hrabiego Rolanda w wąwozie Roncevaux, stanowiąca kanon średniowiecznego etosu rycerskiego.",
    tematyMaturalne: [
      "Wzorzec rycerza idealnego w literaturze.",
      "Honor jako wartość najwyższa – siła czy zguba bohatera?",
      "Scena śmierci jako podsumowanie życia człowieka."
    ],
    konteksty: [
      {
        typ: "Kulturowo-obyczajowy",
        tytul: "Średniowieczny etos rycerski i kodeks feudalny",
        opis: "Roland uosabia cnoty idealnego rycerza chrześcijańskiego: bezgraniczną wierność Bogu, lojalność wobec suzerena (Karola Wielkiego), umiłowanie 'słodkiej Francji', odwagę, obronę wiary przed poganami oraz dbałość o nieskazitelny honor.",
        funkcja: "Wyjaśnia decyzję Rolanda o nieużyciu rogu (Olifanta) na początku bitwy – wezwanie pomocy uważał za plamę na honorze swego rodu, co dowodzi, że kodeks rycerski stawiał cześć wyżej niż przetrwanie biologiczne."
      },
      {
        typ: "Historyczny",
        tytul: "Wyprawa Karola Wielkiego za Pireneje (778 r.) i ideologia wypraw krzyżowych",
        opis: "Historyczna potyczka w wąwozie Roncevaux była drobnym starciem tylnej straży Franków z chrześcijańskimi Baskami. W pieśni (zredagowanej na przełomie XI i XII w., w epoce wypraw krzyżowych) została przekształcona w gigantyczny bój dobra ze złem – chrześcijan z Saracenami.",
        funkcja: "Pokazuje mechanizm mitologizacji historii na potrzeby propagandy religijnej i zagrzewania rycerstwa do walki z niewiernymi w dobie krucjat."
      },
      {
        typ: "Intertekstualny / Literacki",
        tytul: "Henryk Sienkiewicz „Trylogia” – kreacja Longinusa Podbipięty i Michała Wołodyjowskiego",
        opis: "Sienkiewicz świadomie stylizował śmierć Podbipięty pod Zbarażem oraz Wołodyjowskiego w Kamieńcu na średniowieczną 'ars moriendi' Rolanda. Podbipięta ginie naszpikowany strzałami w obronie ojczyzny i wiary, modląc się do Matki Boskiej, otoczony anielskim spokojem.",
        funkcja: "Dowodzi ciągłości toposu heroicznej śmierci rycerza w literaturze polskiej pisanej 'ku pokrzepieniu serc'."
      }
    ]
  },
  {
    id: "szekspir-makbet",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Makbet",
    autor: "William Szekspir",
    epoka: "Renesans / Barok (teatr elżbietański)",
    gatunek: "Tragedia szekspirowska",
    motywy: ["żądza władzy", "wina i kara", "zbrodnia", "destrukcja psychiczna", "zło", "fatum a wolna wola"],
    synteza: "Tragiczne dzieje szkockiego wodza, który pod wpływem przepowiedni czarownic i namowy żony morduje prawowitego króla Dunkana, wkraczając na drogę krwawego tyranobójstwa i moralnego samounicestwienia.",
    tematyMaturalne: [
      "Destrukcyjny wpływ żądzy władzy na psychikę człowieka.",
      "Zbrodnia i jej nieuchronne konsekwencje moralne.",
      "Rola sił nadprzyrodzonych w życiu i wyborach jednostki."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-polityczny",
        tytul: "Myśl polityczna Niccolò Machiavellego („Książę”)",
        opis: "Machiavelli głosił, że skuteczny władca musi odrzucić zasady moralne na rzecz racji stanu („cel uświęca środki”). Makbet próbuje realizować ten model cynicznej polityki opartej na strachu i eliminacji rywali, lecz ponosi całkowitą klęskę, ponieważ zbrodnia rodzi spiralę paranoi i nienawiści poddanych.",
        funkcja: "Pozwala ukazać tragedię jako demaskację machiawelizmu – zdobycie i utrzymanie korony drogą niemoralną prowadzi do upadku tyrana i wewnętrznego piekła sumienia."
      },
      {
        typ: "Psychologiczny",
        tytul: "Studium neurozy, somatyzacji winy i mechanizmu wyparcia",
        opis: "Szekspir genialnie ukazał psychologiczne stadium rozpadu osobowości pod wpływem zbrodni. U Makbeta pojawiają się halucynacje wzrokowe (krwawy sztylet, duch Banka) i bezsenność („Makbet zabił sen”), zaś Lady Makbet ulega obłędowi somnambulicznemu, bezskutecznie próbując zmyć niewidzialną krew z dłoni.",
        funkcja: "Umożliwia głęboką analizę psychiki bohatera; dowodzi, że prawdziwą karą za zbrodnię jest natychmiastowe zniszczenie wewnętrznego spokoju i integralności człowieka."
      },
      {
        typ: "Historyczno-kulturowy",
        tytul: "Panowanie króla Jakuba I Stuarta, spisek prochowy (1605) i wiara w czarnoksięstwo",
        opis: "Dramat powstał tuż po objęciu tronu angielskiego przez Jakuba I Stuarta (pochodzącego ze Szkocji, rzekomego potomka Banka). Król był autorem traktatu o polowaniu na czarownice („Daemonologie”), a po udaremnionym spisku prochowym w kraju panowała atmosfera lęku przed zdradą i zamachem na monarchę.",
        funkcja: "Tłumaczy obecność czarownic i zjawy w dramacie jako elementy odpowiadające ówczesnym wierzeniom dworu oraz ideę nienaruszalności porządku boskiego nadanego prawowitemu monarsze."
      }
    ]
  },
  {
    id: "molier-skapiec",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Skąpiec",
    autor: "Molier",
    epoka: "Barok / Klasycyzm francuski",
    gatunek: "Komedia charakterów",
    motywy: ["chciwość", "pieniądz", "rodzina", "hipokryzja", "tyrania domowa", "komizm"],
    synteza: "Satyryczny portret Harpagona, paryskiego mieszczanina, którego obsesyjna miłość do szkatułki z dukatami niszczy relacje z dziećmi i czyni go postacią zarazem śmieszną i odrażającą.",
    tematyMaturalne: [
      "Wpływ pieniądza na relacje międzyludzkie i rodzinne.",
      "Karykatura i komizm jako narzędzia demaskowania wad ludzkich.",
      "Konflikt pokoleń: egoizm rodziców a prawo dzieci do szczęścia."
    ],
    konteksty: [
      {
        typ: "Społeczno-historyczny",
        tytul: "Narodziny wczesnego kapitalizmu i kult pieniądza we Francji Ludwika XIV",
        opis: "W XVII-wiecznej Francji rosła potęga ekonomiczna burżuazji (mieszczaństwa). Pieniądz stawał się kluczem do awansu społecznego i kupowania urzędów szlacheckich. Harpagon uosabia patologię tej rodzącej się mentalności kapitalistycznej, w której człowiek jest wyceniany wyłącznie przez pryzmat swego kapitału.",
        funkcja: "Pomaga osadzić postać Harpagona w realiach epoki; ukazuje, że Molier nie stworzył abstrakcyjnego dziwaka, lecz poddał krytyce realne zjawisko dehumanizacji relacji przez akumulację bogactwa."
      },
      {
        typ: "Literacki / Tradycja antyczna",
        tytul: "Antyczna komedia rzymska – Plaut i komedia „Aulularia” (Skarb)",
        opis: "Molier zaczerpnął postać i motyw przewodni z komedii rzymskiego pisarza Plauta. Euklion, bohater „Aulularii”, również żyje w panicznym strachu przed kradzieżą garnka ze złotem, podejrzewa o to własnych służących i koguta, co Molier zręcznie przetworzył na realia XVII-wiecznego Paryża.",
        funkcja: "Ukazuje klasycystyczną zasadę naśladowania antycznych wzorców (imitatio antiquorum) oraz to, jak tradycja literacka utrwaliła archetyp chorobliwego skąpca w kulturze europejskiej."
      },
      {
        typ: "Filozoficzno-etyczny",
        tytul: "Arystotelesowska etyka cnót i pojęcie złotego środka (aurea mediocritas)",
        opis: "Zgodnie z etyką Arystotelesa cnota leży pośrodku między dwiema skrajnościami (wadami): hojność jest cnotą pomiędzy marnotrawstwem (reprezentowanym przez Kleanta) a skąpstwem (reprezentowanym przez Harpagona). Obie te skrajności zaburzają równowagę rozumu i prowadzą do moralnej degradacji.",
        funkcja: "Pozwala zinterpretować utwór w duchu dydaktyzmu oświeceniowo-klasycystycznego jako wezwanie do umiaru i harmonii w życiu społecznym."
      }
    ]
  },
  {
    id: "krasicki-satyry",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Satyry (wybrana satyra, np. „Świat zepsuty”, „Do króla”, „Pijaństwo”)",
    autor: "Ignacy Krasicki",
    epoka: "Oświecenie",
    gatunek: "Satyra",
    motywy: ["krytyka wad", "sarmatyzm", "pijaństwo", "rozum", "demaskacja hipokryzji", "ojczyzna"],
    synteza: "Błyskotliwe, rymowane utwory dydaktyczne, w których biskup warmiński piętnuje wady polskiej szlachty: pijaństwo, bezmyślne cudzoziemszczenie, ciemnotę i anarchię, stawiając diagnozę upadku Rzeczypospolitej.",
    tematyMaturalne: [
      "Satyra jako narzędzie naprawy państwa i obyczajów.",
      "Obraz społeczeństwa polskiego w literaturze oświecenia.",
      "Konflikt starego z nowym – krytyka pozornego postępu i tradycyjnego pijaństwa."
    ],
    konteksty: [
      {
        typ: "Historyczno-polityczny",
        tytul: "I rozbiór Polski (1772 r.) i reformy Sejmu Czteroletniego za Stanisława Augusta Poniatowskiego",
        opis: "Satyry Krasickiego powstały w epoce stanisławowskiej, w cieniu traumy po I rozbiorze Rzeczypospolitej. Król i środowisko 'Monitora' dążyli do głębokiej reformy państwa, czemu sprzeciwiała się konserwatywna, sarmacka szlachta. Krasicki w 'Świecie zepsutym' bije na alarm: 'Ginie Polska!', wskazując, że bez naprawy obyczajów państwo czeka zagłada.",
        funkcja: "Uzasadnia patriotyczny i reformatorski cel powstania satyr; dowodzi, że śmiech i drwina służyły ocaleniu niepodległości kraju."
      },
      {
        typ: "Filozoficzno-dydaktyczny",
        tytul: "Oświeceniowy racjonalizm i maksyma „uczyć, bawiąc” (docere, delectare, movere)",
        opis: "Myśl oświeceniowa kładła nacisk na prymat rozumu nad przesądami i namiętnościami. Zgodnie z zasadą poetyki klasycystycznej literatura miała charakter utylitarny – satyra nie atakowała konkretnych osób z imienia (personalnie), lecz ośmieszała uniwersalne wady i postawy (typy ludzkie), aby skłonić czytelnika do autorefleksji.",
        funkcja: "Pozwala wyjaśnić formę artystyczną utworu: zastosowanie ironii, dowcipu i dystansu jako najskuteczniejszego sposobu perswazji pedagogicznej."
      },
      {
        typ: "Literacki / Tradycja antyczna",
        tytul: "Tradycja rzymskiej satyry – Horacy i Juwenalis",
        opis: "Krasicki świadomie czerpał ze wzorców antycznych: pogodnej, wyrozumiałej satyry horacjańskiej oraz bezkompromisowej, oburzonej satyry juwenalisowej. W 'Świecie zepsutym' dominuje ton gniewnego Juwenalisa ('Cnoto! gdzieś się podziała?'), z kolei w 'Pijaństwie' pobłażliwy uśmiech Horacego.",
        funkcja: "Ukazuje kunszt poetycki Krasickiego jako spadkobiercy wielkiej europejskiej tradycji klasycznej."
      }
    ]
  },
  {
    id: "mickiewicz-ballady",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Wybrane ballady, w tym „Romantyczność”",
    autor: "Adam Mickiewicz",
    epoka: "Romantyzm",
    gatunek: "Ballada romantyczna",
    motywy: ["irracjonalizm", "wiara i czucie", "szaleństwo z miłości", "ludowość", "kontakt z zaświatami"],
    synteza: "Manifest polskiego romantyzmu (1822 r.). Historia obłąkanej Karusi rozmawiającej z duchem zmarłego Jasieńka staje się areną sporu między chłodnym szkiełkiem i okiem mędrca (Starca) a prawdą serca i współczucia.",
    tematyMaturalne: [
      "Serce i rozum – dwa przeciwstawne sposoby poznawania świata.",
      "Rola ludowości i wierzeń prostego ludu w literaturze romantycznej.",
      "Człowiek odrzucony przez społeczeństwo z powodu swej wrażliwości."
    ],
    konteksty: [
      {
        typ: "Filozoficzny",
        tytul: "Spór klasyków z romantykami: Oświeceniowy empiryzm a romantyczny irracjonalizm",
        opis: "Postać Starca w 'Romantyczności' uosabia Jana Śniadeckiego – profesora Uniwersytetu Wileńskiego, autora rozprawy potępiającej romantyzm. Śniadecki wierzył tylko w to, co da się zmierzyć i dowieść rozumowo ('szkiełko i oko'). Mickiewicz przeciwstawia mu koncepcję poznania intuicyjnego, metafizycznego i uczuciowego ('miej serce i patrzaj w serce').",
        funkcja: "Kluczowy kontekst epoki tłumaczący ideowy przełom roku 1822 w Polsce: odrzucenie chłodnego racjonalizmu na rzecz wiary w świat duchowy i uczucia."
      },
      {
        typ: "Kulturowo-folklorystyczny",
        tytul: "Ludowość (ludomania) i kodeks moralny gminu",
        opis: "Romantycy uważali lud wiejski za jedynego depozytariusza nieskażonej prawdy duchowej i moralnej. W balladach ('Świtezianka', 'Lilije', 'Romantyczność') ludowe wierzenia niosą prostą, surową sprawiedliwość: nie ma zbrodni bez kary, a miłość i wierność są wartościami absolutnymi.",
        funkcja: "Pozwala wykazać, że dla romantyków folklor nie był jedynie dekoracją, lecz fundamentem etyki i źródłem nowej estetyki poetyckiej."
      },
      {
        typ: "Biograficzny",
        tytul: "Nieszczęśliwa miłość Mickiewicza do Maryli Wereszczakówny",
        opis: "Wydanie 'Ballad i romansów' zbiegło się z osobistym dramatem młodego poety: jego ukochana Maryla wyszła za mąż za bogatego hrabiego Wawrzyńca Puttkamera. Motyw nieszczęśliwej, przekraczającej granice śmierci miłości (jak u Karusi i Jasieńka) był bezpośrednim echem tego zawodu sercowego.",
        funkcja: "Uwiarygadnia emocjonalną temperaturę wiersza i pomaga zrozumieć postawę poety utożsamiającego się z cierpieniem odrzuconych kochanków."
      }
    ]
  },
  {
    id: "mickiewicz-dziady-3",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Dziady cz. III",
    autor: "Adam Mickiewicz",
    epoka: "Romantyzm",
    gatunek: "Dramat romantyczny",
    motywy: ["martyrologia", "mesjanizm", "prometeizm", "bunt przeciw Bogu", "walka dobra ze złem", "tyrania"],
    synteza: "Arcydzieło polskiego dramatu romantycznego, ukazujące cierpienie młodzieży wileńskiej pod carskim zaborem, bunt Konrada żądającego władzy nad duszami oraz mesjanistyczną wizję Polski jako Chrystusa narodów.",
    tematyMaturalne: [
      "Różne postawy wobec cierpienia narodu: bunt (Konrad) czy pokora (ks. Piotr).",
      "Martyrologia narodu polskiego i jej sens w perspektywie dziejów.",
      "Portret zaborcy i postawy Polaków wobec cara (Salon warszawski)."
    ],
    konteksty: [
      {
        typ: "Historyczno-polityczny",
        tytul: "Klęska powstania listopadowego (1830–1831) i proces filomatów (1823–1824)",
        opis: "Dramat powstał w Dreźnie w 1832 r., tuż po stłumieniu powstania listopadowego. Mickiewicz, dręczony wyrzutami sumienia, że sam nie wziął udziału w walce, połączył dawne wspomnienia wileńskich aresztowań młodzieży przez Nowosilcowa z narodową tragedią popowstaniową i Wielką Emigracją.",
        funkcja: "Tłumaczy genezę utworu jako próby wytłumaczenia sensu narodowej klęski i nadania sensu ofiarom składanym przez pokolenia młodych Polaków na Sybirze."
      },
      {
        typ: "Filozoficzno-religijny",
        tytul: "Koncepcja polskiego mesjanizmu narodowego („Polska Chrystusem narodów”)",
        opis: "W 'Widzeniu księdza Piotra' Mickiewicz wykłada doktrynę mesjanizmu: Polska, podobnie jak niewinny Chrystus, została ukrzyżowana przez trzech zaborców (trzech żołdaków), lecz jej męka doprowadzi do zmartwychwstania i wyzwolenia wszystkich ludów Europy.",
        funkcja: "Kluczowa koncepcja historiozoficzna, która miała podnieść na duchu załamany po upadku powstania naród i przekształcić klęskę militarną w moralne zwycięstwo."
      },
      {
        typ: "Archetypiczny / Mityczny",
        tytul: "Bunt prometejski w Wielkiej Improwizacji",
        opis: "Konrad w celi klasztoru Bazylianów rzuca wyzwanie Bogu w imię miłości do cierpiącego narodu („Nazywam się Milijon – bo za milijony kocham i cierpię katusze”). Jego postawa jest bezpośrednim nawiązaniem do mitu o Prometeuszu – buntuje się przeciw najwyższemu władcy z pobudek altruistycznych, ryzykując wieczne potępienie.",
        funkcja: "Pozwala ukazać wielkość i niebezpieczeństwo pychy jednostki wybitnej (indywidualizmu romantycznego), która w szlachetnym uniesieniu ociera się o bluźnierstwo i szatańską pokusę."
      }
    ]
  },
  {
    id: "prus-lalka",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Lalka",
    autor: "Bolesław Prus",
    epoka: "Pozytywizm",
    gatunek: "Powieść realistyczna / społeczno-obyczajowa",
    motywy: ["miłość destrukcyjna", "praca organiczna i u podstaw", "awans społeczny", "antysemityzm", "idealizm", "miasto"],
    synteza: "Panorama społeczeństwa polskiego końca XIX wieku ukazana przez pryzmat losów Stanisława Wokulskiego – człowieka z pogranicza romantyzmu i pozytywizmu, którego genialną energię kupiecką niszczy obsesyjna miłość do arystokratki Izabeli Łęckiej.",
    tematyMaturalne: [
      "Tragizm człowieka rozdartego między dwiema epokami.",
      "Ocena polskiego społeczeństwa (arystokracja, mieszczaństwo, lud).",
      "Wokulski – romantyk czy pozytywista?"
    ],
    konteksty: [
      {
        typ: "Filozoficzno-społeczny",
        tytul: "Idee polskiego pozytywizmu: praca organiczna i praca u podstaw a darwinizm społeczny",
        opis: "Powieść weryfikuje program polskich pozytywistów (Świętochowskiego, Prusa). Wokulski realizuje postulaty pracy u podstaw (pomoc prostytutce Mariannie, braciom Wysockim) oraz pracy organicznej (spółka do handlu ze Wschodem). Zderza się jednak z pasożytnictwem arystokracji i bezwzględną walką o byt na rynku (darwinizm społeczny H. Spencera).",
        funkcja: "Pozwala udowodnić tezę, że 'Lalka' jest gorzkim rozliczeniem ze złudzeniami ideologii pozytywistycznej, która nie sprawdziła się w warunkach zaboru i braku własnego państwa."
      },
      {
        typ: "Historyczny",
        tytul: "Trauma powstania styczniowego (1863 r.) i jej wpływ na losy bohaterów",
        opis: "Młodość Wokulskiego i Rzeckiego naznaczona była walką narodowowyzwoleńczą. Wokulski brał udział w powstaniu styczniowym, za co został zesłany do Irkucka, z kolei Rzecki walczył na Węgrzech w Wiośnie Ludów (1848). Doświadczenie klęski zbrojnej zmusiło ich do przewartościowania ideałów i szukania innych dróg ratowania kraju.",
        funkcja: "Wyjaśnia psychologiczne pęknięcie w Wokulskim: z jednej strony nosi w sobie romantyczny etos walki i poświęcenia, z drugiej próbuje budować potęgę na drodze pragmatyzmu handlowego."
      },
      {
        typ: "Biograficzno-urbanistyczny",
        tytul: "Dziennikarska działalność Bolesława Prusa i kronikarski realizm Warszawy lat 70. XIX w.",
        opis: "Prus pisał powieść jako autor popularnych 'Kronik tygodniowych'. Warszawa w 'Lalce' jest oddana z topograficzną precyzją: Powiśle jako dzielnica skrajnej nędzy, Krakowskie Przedmieście i Łazienki jako rejony arystokracji. Autor osobiście obserwował proces asymilacji Żydów, relacje polsko-niemieckie oraz upadek ekonomiczny ziemiaństwa.",
        funkcja: "Stanowi dowód na realizm krytyczny utworu; pokazuje, że powieść jest bezcennym dokumentem socjologicznym epoki kapitalistycznej transformacji."
      }
    ]
  },
  {
    id: "sienkiewicz-potop",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Potop (fragmenty)",
    autor: "Henryk Sienkiewicz",
    epoka: "Pozytywizm",
    gatunek: "Powieść historyczna",
    motywy: ["przemiana wewnętrzna", "patriotyzm", "zdrada i rehabilitacja", "wojna", "obrona Jasnej Góry", "pokrzepienie serc"],
    synteza: "Historia Andrzeja Kmicica, który z hulaki i nieświadomego zdrajcy pod wpływem wstrząsu moralnego staje się ofiarnym obrońcą ojczyzny podczas najazdu szwedzkiego, zdobywając przebaczenie narodu i miłość Oleńki Billewiczówny.",
    tematyMaturalne: [
      "Motyw przemiany wewnętrznej bohatera i zadośćuczynienia za winy.",
      "Rola literatury tworzonej 'ku pokrzepieniu serc' w czasach niewoli.",
      "Zdrada narodowa a wierność ojczyźnie w momentach próby dziejowej."
    ],
    konteksty: [
      {
        typ: "Historyczno-narodowy",
        tytul: "Idea pisania „ku pokrzepieniu serc” w dobie zaborów i kryzysu tożsamości",
        opis: "W latach 80. XIX w. Polacy znajdowali się pod presją intensywnej rusyfikacji i germanizacji (Kulturkampf), a krakowska szkoła historyczna oskarżała naród o spowodowanie własnego upadku przez warcholstwo. Sienkiewicz stworzył 'Trylogię', by przypomnieć chwile, gdy Rzeczpospolita znajdowała się na skraju przepaści, lecz dzięki solidarności zdołała odeprzeć wroga.",
        funkcja: "Wyjaśnia nadrzędną funkcję społeczną powieści: budowanie dumy narodowej i podtrzymywanie wiary w odzyskanie niepodległości."
      },
      {
        typ: "Archetypiczno-biblijny",
        tytul: "Parabola o synu marnotrawnym oraz nawrócenie Szawła (św. Pawła)",
        opis: "Droga życiowa Andrzeja Kmicica wpisuje się w archetyp upadłego grzesznika, który doświadcza moralnego olśnienia. Po zdradzie Radziwiłłów Kmicic przyjmuje nazwisko Babinicz (akt pokory), naraża życie w obronie Jasnej Góry i własną krwią odkupuje winy, co przypomina nawrócenie Szawła z Tarsu.",
        funkcja: "Pozwala zinterpretować postać Kmicica nie tylko jako bohatera przygodowego, lecz jako metaforę duchowego odrodzenia całego narodu polskiego."
      },
      {
        typ: "Historyczny",
        tytul: "Najazd szwedzki na Rzeczpospolitą (1655–1660) i obrona klasztoru na Jasnej Górze",
        opis: "Obrona sanktuarium jasnogórskiego przez o. Augustyna Kordeckiego miała wymiar historyczny i symboliczny. Choć militarnie nie było to największe starcie wojny, atak protestanckich Szwedów na katolicką twierdzę wstrząsnął sumieniami szlachty i wywołał powszechne powstanie przeciw najeźdźcy.",
        funkcja: "Służy do analizy roli religii katolickiej jako spoiwa tożsamości narodowej Polaków w momentach największych kryzysów politycznych."
      }
    ]
  },
  {
    id: "dostojewski-zbrodnia-i-kara",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Zbrodnia i kara",
    autor: "Fiodor Dostojewski",
    epoka: "Pozytywizm / Realizm psychologiczny",
    gatunek: "Powieść psychologiczna / polifoniczna",
    motywy: ["wina i odkupienie", "zbrodnia", "nadczłowiek", "cierpienie", "nawrócony grzesznik", "miasto jako labirynt"],
    synteza: "Studium morderstwa dokonanego przez ubogiego petersburskiego studenta Rodiona Raskolnikowa, który wierząc w podział ludzi na 'zwykłych' i 'niezwykłych', zabija lichwiarkę, po czym pod wpływem cierpienia i miłości Soni wkracza na drogę duchowego zmartwychwstania.",
    tematyMaturalne: [
      "Czy cel uświęca środki? Moralna odpowiedzialność za czyny.",
      "Rola miłości i cierpienia w odrodzeniu duchowym człowieka.",
      "Miasto jako przestrzeń wyobcowania i deprawacji jednostki."
    ],
    konteksty: [
      {
        typ: "Filozoficzny",
        tytul: "Krytyka radykalnego utylitaryzmu, nihilizmu i koncepcja nadczłowieka (proto-nietzscheanizm)",
        opis: "Raskolnikow stworzył artykuł 'O zbrodni', dzieląc ludzi na 'drżące stworzenia' (materiał biologiczny) oraz jednostki niezwykłe (jak Napoleon), mające moralne prawo deptać normy dla dobra ludzkości. Dostojewski poddał bezwzględnej krytyce zachodni utylitaryzm i nihilizm, pokazując, że rozumowe kalkulacje bez Boga prowadzą wprost do tyranii i rozlewu krwi.",
        funkcja: "Kluczowy kontekst demaskujący niebezpieczeństwo ideologii wyższości jednostki; dowodzi, że żadna teoria nie unieważnia uniwersalnego dekalogu."
      },
      {
        typ: "Biblijny",
        tytul: "Przypowieść o wskrzeszeniu Łazarza z Ewangelii św. Jana",
        opis: "Kluczowa scena powieści to czytanie przez prostytutkę Sonię fragmentu Ewangelii o wskrzeszeniu Łazarza leżącego od czterech dni w grobie. Raskolnikow po morderstwie jest duchowym trupem ('sam siebie zabiłem, a nie babinę'), a jego nawrócenie na Syberii jest symbolicznym zmartwychwstaniem do nowego życia.",
        funkcja: "Daje religijny klucz interpretacyjny do epilogu powieści: nikt nie jest bezpowrotnie stracony, jeśli przyjmie cierpienie i zadośćuczynienie jako drogę do łaski."
      },
      {
        typ: "Biograficzny",
        tytul: "Katorga Dostojewskiego na Syberii po procesie Koła Pietraszewskiego",
        opis: "W 1849 r. Dostojewski stał przed plutonem egzekucyjnym za działalność w rewolucyjnym Kole Pietraszewskiego (ułaskawiony w ostatniej sekundzie przez cara). Następnie spędził 4 lata na katordze w Omsku wśród najgorszych morderców, gdzie jedyną dozwoloną książką była Nowy Testament, co doprowadziło do jego głębokiego nawrócenia.",
        funkcja: "Tłumaczy realizm psychologiczny w opisie przeżyć więziennych Raskolnikowa oraz niezłomną wiarę pisarza w możliwość odkupienia każdego upadłego człowieka."
      }
    ]
  },
  {
    id: "wyspianski-wesele",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Wesele",
    autor: "Stanisław Wyspiański",
    epoka: "Młoda Polska",
    gatunek: "Dramat symboliczny / narodowy",
    motywy: ["chłopomania", "niemoc narodowa", "symbole", "widma i zjawy", "chocholi taniec", "mit wolnościowy"],
    synteza: "Rzeczywiste wesele w podkrakowskich Bronowicach staje się dla Wyspiańskiego zwierciadłem polskiej duszy: ujawnia głęboką przepaść między inteligencją a chłopami, narodowe kompleksy oraz niezdolność do podjęcia czynu niepodległościowego.",
    tematyMaturalne: [
      "Diagnoza społeczeństwa polskiego u progu XX wieku.",
      "Rola symboli narodowych w budzeniu świadomości historycznej.",
      "Mit zjednoczenia narodowego a rzeczywistość."
    ],
    konteksty: [
      {
        typ: "Biograficzno-historyczny",
        tytul: "Autentyczne wesele Lucjana Rydla i Jadwigi Mikołajczykówny (listopad 1900 r.)",
        opis: "Akcja dramatu opiera się na autentycznym wydarzeniu towarzyskim w dworku Włodzimierza Tetmajera w Bronowicach. Postacie dramatu miały żywe pierwowzory (Gospodarz – Tetmajer, Pan Młody – poeta Lucjan Rydel, Dziennikarz – Rudolf Starzewski, Rachela – Pepa Singer). Wyspiański był gościem na weselu i z fotograficzną pamięcią zanotował nastroje inteligencji.",
        funkcja: "Pozwala odróżnić warstwę realistyczno-obyczajową utworu od warstwy symboliczno-fantastycznej; ukazuje autentyzm krytykowanych postaw krakowskiej bohemy."
      },
      {
        typ: "Malarstwo i sztuka",
        tytul: "Dzieła Jana Matejki: „Stańczyk”, „Wernyhora” i „Kościuszko pod Racławicami”",
        opis: "Wyspiański był uczniem Jana Matejki. W dramacie ożywają matejkowskie płótna: Stańczyk z obrazu 'Stańczyk w czasie balu na dworze królowej Bony...' wręcza Dziennikarzowi Kaduceusz polski, a Wernyhora pojawia się jako posłaniec czynu niepodległościowego. Inteligencja zna historię jedynie przez pryzmat muzealnych obrazów, nie potrafiąc przenieść jej w realny czyn.",
        funkcja: "Służy do analizy fenomenu uwięzienia wyobraźni Polaków w mitach malarskich i literackich, które usypiają wolę walki zamiast do niej prowadzić."
      },
      {
        typ: "Społeczno-polityczny",
        tytul: "Fenomen młodopolskiej chłopomanii (ludomanii) i pamięć rzezi galicyjskiej (1846 r.)",
        opis: "Młodopolscy artyści ulegli powierzchownej fascynacji barwną kulturą wsi (chłopomanii), żeniąc się z chłopkami. Wyspiański brutalnie demaskuje tę modę: pod płaszczykiem zachwytu kryje się wzajemna nieufność. Dziad i Pan Młody przypominają o krwawej rabacji Jakuba Szeli z 1846 roku ('Myśmy wszystko zapomnieli; ostatek krwią zachlany...'), co dowodzi, że prawdziwe przymierze inteligencji z ludem jest mitem.",
        funkcja: "Kluczowy kontekst wyjaśniający przyczynę niemocy narodowej – brak zaufania i nieprzepracowane traumy społeczne uniemożliwiające wspólne powstanie."
      }
    ]
  },
  {
    id: "reymont-chlopi",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Chłopi (fragmenty tomu I: Jesień)",
    autor: "Władysław Stanisław Reymont",
    epoka: "Młoda Polska",
    gatunek: "Epopeja chłopska / powieść młodopolska",
    motywy: ["wieś", "ziemia jako świętość", "rytuał", "natura", "moralność gromady", "namiętność"],
    synteza: "Monumentalny obraz życia wsi Lipce, ujęty w ramy czterech pór roku, gdzie losy ludzkie (trójkąt: Maciej Boryna – Jagna – Antek) są nierozerwalnie splecione z rytmem przyrody, obyczajem i bezwzględną walką o ziemię.",
    tematyMaturalne: [
      "Człowiek cząstką przyrody – biologizm i fatalizm w życiu człowieka.",
      "Ziemia jako źródło bytu, dumy i konfliktów w gromadzie.",
      "Jednostka wykraczająca poza normy wobec prawa zbiorowości (los Jagny)."
    ],
    konteksty: [
      {
        typ: "Antropologiczno-filozoficzny",
        tytul: "Koncepcja czasu mitycznego (sakralnego) i cykliczności natury Mircei Eliadego",
        opis: "W Lipcach czas nie biegnie linearnie, lecz kołowo, wyznaczany przez następstwo pór roku oraz kalendarz świąt liturgicznych Kościoła katolickiego. Prace polowe (wykopki, siew, żniwa) mają charakter odwiecznego rytuału powtarzanego z pokolenia na pokolenie.",
        funkcja: "Pozwala ukazać powieść nie jako zwykły zapis obyczajowy, lecz jako uniwersalny mit o losie człowieka wtopionego w kosmiczny porządek natury."
      },
      {
        typ: "Malarstwo i sztuka",
        tytul: "Malarstwo Józefa Chełmońskiego („Bociany”, „Babie lato”) a realizm impresjonistyczny",
        opis: "Reymont opisuje pejzaże Lipiec z mistrzostwem malarza impresjonisty (gra światła, kolory, mgły, zapachy ziemi). Jego opisy korespondują bezpośrednio ze słynnymi płótnami Chełmońskiego ukazującymi surowe piękno mazowieckiej wsi, bose pastuszki i głębokie przywiązanie chłopa do ojczystego krajobrazu.",
        funkcja: "Stanowi kontekst estetyczny; pomaga w analizie języka powieści (poetyzacja, młodopolski impresjonizm połączony z naturalistyczną brutalnością faktów)."
      },
      {
        typ: "Społeczno-prawny",
        tytul: "Sytuacja wsi polskiej po uwłaszczeniu chłopów (1864 r.) i bezwzględny kult morgów",
        opis: "Po carskim dekrecie uwłaszczeniowym z 1864 r. chłopi zyskali ziemię na własność, co uczyniło grunt najwyższą wartością determinującą pozycję społeczną. Małżeństwa kojarzono wyłącznie z przyczyn majątkowych ('morgi szły do morgów'), a starzy rodzice bez majątku byli spychani na margines i skazywani na żebraczy los (jak Jagustynka czy komornicy).",
        funkcja: "Uzasadnia zachowanie Macieja Boryny i jego konflikt z Antkiem: ziemia była jedynym gwarantem godności, niezależności i biologicznego przetrwania."
      }
    ]
  },
  {
    id: "zeromski-przedwiosnie",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Przedwiośnie",
    autor: "Stefan Żeromski",
    epoka: "Dwudziestolecie międzywojenne",
    gatunek: "Powieść polityczno-społeczna",
    motywy: ["rewolucja", "odbudowa państwa", "szklane domy", "dojrzewanie", "nędza i nierówności", "patriotyzm"],
    synteza: "Dzieje Cezarego Baryki na tle przełomowych wydarzeń historycznych: od krwawej rewolucji w Baku, przez wojnę polsko-bolszewicką i sielankę w Nawłoci, po poszukiwanie drogi reform dla odrodzonej, zmagającej się z nędzą Polski.",
    tematyMaturalne: [
      "Entuzjazm i rozczarowanie odzyskaną niepodległością.",
      "Koszty i oblicza rewolucji – nadzieja czy zagłada cywilizacji?",
      "Szklane domy jako symbol marzenia o idealnej ojczyźnie."
    ],
    konteksty: [
      {
        typ: "Historyczno-polityczny",
        tytul: "Rewolucja bolszewicka w Baku (1917–1918) oraz wojna polsko-bolszewicka (1920 r.)",
        opis: "Żeromski z drastycznym realizmem ukazał rozpad cywilizacji w naftowym Baku: samosądy, głód, grabieże i rzeź ormiańsko-tatarską. Wydarzenia te ukształtowały Cezarego, który przekonał się, że rewolucja nie przynosi sprawiedliwości, lecz bestialstwo, co zweryfikował podczas obrony Warszawy w 1920 r.",
        funkcja: "Wyjaśnia genezę pęknięcia światopoglądowego bohatera i stanowi przestrogę przed przeniesieniem bolszewickich metod walki na grunt odradzającej się Polski."
      },
      {
        typ: "Ideowo-polityczny",
        tytul: "Dyskurs o drogach rozwoju II RP: ewolucjonizm Szymona Gajowca a radykalizm komunistów",
        opis: "W części trzeciej powieści autor zestawia dwie koncepcje naprawy państwa: program państwowotwórczy Gajowca (powolne, ewolucyjne reformy, waluta Władysława Grabskiego, edukacja) oraz rewolucyjny program komunistów (Antoni Lulek), żądających obalenia rządu i oddania władzy klasie robotniczej.",
        funkcja: "Ukazuje powieść jako diagnozę kryzysu społecznego Polski lat 20. XX w. i krzyk pisarza o natychmiastowe reformy społeczne, nim zdesperowany lud sięgnie po rewolucję."
      },
      {
        typ: "Biograficzno-publicystyczny",
        tytul: "Gorzka troska Żeromskiego o niepodległą Polskę (krytyka poeuforii 1918 roku)",
        opis: "Żeromski, nazywany 'sumieniem polskiej literatury', po 1918 r. przeżył głębokie rozczarowanie stanem odrodzonego państwa (analfabetyzm, korupcja, nędza dzielnic robotniczych Warszawy). Wizja 'szklanych domów' opowiedziana przez Seweryna Barykę była wyrazem tęsknoty za Polską nowoczesną, czystą i sprawiedliwą, która okazała się bolesną utopią.",
        funkcja: "Pozwala zinterpretować finałowy marsz Baryki na Belweder nie jako poparcie dla komunizmu, lecz jako dramatyczny protest przeciw bierności władz wobec nędzy obywateli."
      }
    ]
  },
  {
    id: "gombrowicz-ferdydurke",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Ferdydurke (fragmenty)",
    autor: "Witold Gombrowicz",
    epoka: "Dwudziestolecie międzywojenne",
    gatunek: "Powieść awangardowa / groteskowa",
    motywy: ["Forma", "Gęba", "Pupa", "infantylizacja", "konformizm", "groteska", "nowoczesność a tradycja"],
    synteza: "Groteskowa historia trzydziestoletniego Józia Kowalskiego, który zostaje przez profesora Pimkę cofnięty do szkoły i poddany procesowi przymusowego upupiania, demaskująca opresyjność wszelkich społecznych ról i konwencji.",
    tematyMaturalne: [
      "Człowiek w niewoli formy i opinii innych ludzi.",
      "Krytyka skostniałego systemu edukacji i pozornej nowoczesności.",
      "Groteska i absurd jako narzędzia badania natury ludzkiej."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-egzystencjalny",
        tytul: "Filozofia egzystencjalna: koncepcja Innego (Jean-Paul Sartre: „Piekło to inni”)",
        opis: "Gombrowicz w powieści formułuje własną filozofię człowieka: człowiek nie istnieje autonomicznie, lecz jest nieustannie stwarzany przez drugiego człowieka ('człowiek jest stwarzany przez formę'). Nie ma ucieczki przed 'Gębą' (maską narzuconą przez otoczenie), jak tylko w inną gębę, co koresponduje z tezą Sartre'a o uprzedmiotowieniu człowieka przez spojrzenie Innego.",
        funkcja: "Kluczowy kontekst filozoficzny dowodzący, że utwór nie jest zwykłą zgrywą, lecz głębokim traktatem antropologicznym o niemożności osiągnięcia autentyczności w społeczeństwie."
      },
      {
        typ: "Psychologiczno-psychoanalityczny",
        tytul: "Teoria psychoanalizy Zygmunta Freuda i problem sztucznej infantylizacji",
        opis: "Zabieg profesora Pimki polega na wtłoczeniu dorosłego mężczyzny w rolę dziecka ('upupienie'). Gombrowicz demaskuje mechanizmy kultury, która tłumi dojrzałość, seksualność i szczerość, wymuszając zachowania infantylne i uległe wobec autorytetu belfrów.",
        funkcja: "Pomaga przeanalizować sceny pojedynku na miny (Miętus – Syfon) oraz szkolnych lekcji polskiego jako satyry na tresurę społeczną niszczącą niezależne myślenie."
      },
      {
        typ: "Społeczno-obyczajowy",
        tytul: "Krytyka polskich mitów społecznych II RP: tradycjonalizmu ziemiańskiego i snobizmu modernistycznego",
        opis: "Autor bezlitośnie obnaża dwa dominujące modele kultury międzywojennej: snobistyczną, postępową rodzinę Młodziaków ('nowoczesna pensjonarka' Zuta) oraz anachroniczny, oparty na feudalnym biciu parobka w twarz dwór ziemiański w Bolimowie (wujostwo Hurleccy).",
        funkcja: "Ukazuje utwór jako wszechstronną satyrę demaskującą hipokryzję zarówno polskiego tradycjonalizmu, jak i bezkrytycznie importowanego z Zachodu nowinkarstwa obyczajowego."
      }
    ]
  },
  {
    id: "borowski-opowiadania",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Proszę państwa do gazu (z tomu „Pożegnanie z Marią”)",
    autor: "Tadeusz Borowski",
    epoka: "Wojna i okupacja / Współczesność",
    gatunek: "Opowiadanie obozowe (literatura lagrowa)",
    motywy: ["lagier", "człowiek zlagrowany", "odczłowieczenie", "behawioryzm", "obojętność na śmierć", "przetrwanie"],
    synteza: "Wstrząsający opis rozładunku transportu ludzi na rampie w Auschwitz-Birkenau, ukazany z perspektywy więźnia funkcyjnego z komanda Kanady (Tadka), zmuszonego do grabieży dobytku idących na śmierć w imię własnego przetrwania.",
    tematyMaturalne: [
      "Człowiek zlagrowany – granice kompromisu moralnego w obliczu śmierci.",
      "Behawiorystyczna technika narracyjna w ukazywaniu zbrodni ludobójstwa.",
      "Upadek europejskiego dekalogu wartości w warunkach obozowych."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-etyczny",
        tytul: "Koncepcja „człowieka zlagrowanego” i upadek kultury śródziemnomorskiej",
        opis: "Borowski wprowadził pojęcie 'człowieka zlagrowanego' – jednostki, która przyswoiła nieludzkie reguły obozu jako naturalną normę. W warunkach skrajnego głodu i terroru podstawowym instynktem staje się biologiczne przetrwanie za wszelką cenę kosztem innych więźniów, co oznacza całkowitą kapitulację tradycyjnej moralności.",
        funkcja: "Służy do analizy tragizmu narratora Tadka, który czuje fizyczny wstręt i wściekłość nie do oprawców SS, lecz do prowadzonych na śmierć ofiar, bo ich obecność zagraża jego względnemu bezpieczeństwu."
      },
      {
        typ: "Teoretycznoliteracki",
        tytul: "Behawioryzm i redukcja psychologizmu w narracji",
        opis: "Borowski zastosował metodę behawioralną: odrzucił patos, moralizowanie i wnikanie w stany emocjonalne bohaterów na rzecz chłodnego, precyzyjnego rejestrowania faktów, gestów i reakcji fizjologicznych organizmu (pot, głód, pragnienie, mechaniczna selekcja).",
        funkcja: "Pozwala wyjaśnić siłę rażenia prozy Borowskiego – obiektywny, suchy ton potęguje grozę sytuacji i uniemożliwia czytelnikowi ucieczkę w łatwe poczucie moralnej wyższości."
      },
      {
        typ: "Biograficzno-historyczny",
        tytul: "Doświadczenie obozowe Tadeusza Borowskiego i powojenna debata o nihilizmie",
        opis: "Borowski był więźniem Auschwitz i Dachau. Po opublikowaniu opowiadań został gwałtownie zaatakowany przez część krytyki (m.in. Zofię Kossak-Szczucką) za rzekomy cynizm, amoralność i brak wiary w człowieka. Pisarz nie potrafił odnaleźć się w powojennej rzeczywistości i w 1951 r. w wieku 29 lat popełnił samobójstwo.",
        funkcja: "Rzuca światło na dramat ocalałych z Holokaustu (syndrom obozowy) i dowodzi bezkompromisowości Borowskiego w dążeniu do prawdy o mechanizmach odczłowieczenia."
      }
    ]
  },
  {
    id: "herling-inny-swiat",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Inny świat (fragmenty)",
    autor: "Gustaw Herling-Grudziński",
    epoka: "Wojna i okupacja / Współczesność",
    gatunek: "Pamiętnik / proza dokumentarna (literatura łagrowa)",
    motywy: ["łagier", "sowiecki totalitaryzm", "próba człowieczeństwa", "godność", "głód", "ocalenie moralne"],
    synteza: "Zapis doświadczeń autora z sowieckiego łagru w Jercewie, dokumentujący funkcjonowanie nieludzkiego systemu Gułagu, który poprzez głód i morderczą pracę niszczył ludzką duszę, a zarazem świadectwo heroicznej obrony resztek godności.",
    tematyMaturalne: [
      "Czy człowiek może ocalić człowieczeństwo w warunkach nieludzkich?",
      "System sowieckiego łagru a obóz nazistowski – podobieństwa i różnice.",
      "Cena powrotu do normalnego świata i problem przebaczenia (epilog w Rzymie)."
    ],
    konteksty: [
      {
        typ: "Historyczno-polityczny",
        tytul: "System sowieckiego Gułagu i masowe represje NKWD wobec obywateli polskich po 17 września 1939 r.",
        opis: "Po agresji ZSRR na Polskę autor został aresztowany przez NKWD w Grodnie i skazany na 5 lat łagru pod absurdalnym zarzutem szpiegostwa (miał buty oficerskie i nazwisko brzmiące jak marszałek Göring). Powieść obnaża mechanizm sowieckiego obozu pracy jako machiny niewolniczej eksploatacji człowieka i ideologicznego prania mózgu.",
        funkcja: "Stanowi bezcenny dokument historyczny o zbrodniach totalitaryzmu stalinowskiego, ukrywanych przez lata przed zachodnią opinią publiczną."
      },
      {
        typ: "Filozoficzno-polemiczny",
        tytul: "Polemika z pesymizmem Tadeusza Borowskiego: granice ludzkiej odpowiedzialności",
        opis: "Słynne zdanie z utworu: 'Człowiek jest ludzki w ludzkich warunkach i głupotą jest sądzić go według norm, które stworzono w warunkach normalnych' koresponduje z Borowskim, lecz Herling-Grudziński nie popada w nihilizm. Ukazuje postacie, które potrafiły ocalić godność za cenę życia (np. Kostylew opalający rękę w ogniu, by nie pracować dla oprawców, czy Natalia Lwowna czytająca Dostojewskiego).",
        funkcja: "Pozwala na wielowymiarowe zestawienie literatury lagrowej i łagrowej: udowadnia, że według Herlinga człowiek nawet w piekle zachowuje iskrę wolnej woli i zdolność do heroizmu."
      },
      {
        typ: "Literacki",
        tytul: "Fiodor Dostojewski „Wspomnienia z domu umarłych” jako motto i klucz kompozycyjny",
        opis: "Książka Dostojewskiego o carskiej katordze na Syberii krążyła po łagrze w Jercewie jako zakazana relikwia. Herling zaczerpnął z niej motto utworu, podkreślając, że sowiecki Gułag był kontynuacją i potwornym udoskonaleniem carskich metod niszczenia człowieka.",
        funkcja: "Tworzy ramę interpretacyjną powieści, łącząc doświadczenie XX-wiecznego łagru z rosyjską tradycją literatury męczeństwa i zmagania o duszę człowieka."
      }
    ]
  },
  {
    id: "krall-zdazyc-przed-panem-bogiem",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Zdążyć przed Panem Bogiem",
    autor: "Hanna Krall",
    epoka: "Współczesność",
    gatunek: "Reportaż biograficzny / literatura faktu",
    motywy: ["Holokaust", "powstanie w getcie", "pamięć", "godna śmierć", "medycyna", "deheroizacja"],
    synteza: "Wywiad-rzeka z Markiem Edelmanem, ostatnim przywódcą powstania w getcie warszawskim, łączący wspomnienia z piekła Umschlagplatzu z powojenną pracą kardiochirurga ratującego ludzkie serca w wyścigu ze śmiercią.",
    tematyMaturalne: [
      "Różne wymiary heroizmu – wybór sposobu umierania a ratowanie życia.",
      "Deheroizacja mitu powstania w getcie w relacji świadka historii.",
      "Etyczna odpowiedzialność lekarza i świadka Holokaustu."
    ],
    konteksty: [
      {
        typ: "Historyczny",
        tytul: "Likwidacja getta warszawskiego (Grossaktion Warschau) i powstanie w kwietniu 1943 r.",
        opis: "Wiosną 1943 r. garstka słabo uzbrojonych bojowników Żydowskiej Organizacji Bojowej (ŻOB) podjęła nierówną walkę z oddziałami SS pacyfikującymi getto. Edelman podkreśla, że celem powstania nie było militarne zwycięstwo, lecz wybór sposobu śmierci z bronią w ręku zamiast biernego marszu do komór gazowych Treblinki.",
        funkcja: "Kluczowy kontekst faktograficzny pozwalający zrozumieć tragizm powstania w getcie jako dramatycznego aktu godności ludzkiej skazanych na zagładę."
      },
      {
        typ: "Filozoficzno-etyczny",
        tytul: "Koncepcja 'wyścigu z Panem Bogiem' w pracy lekarza kardiochirurga",
        opis: "Edelman po wojnie został wybitnym kardiochirurgiem. Swoją pracę przy stole operacyjnym traktował jako bezpośrednie przedłużenie misji z getta: skoro w getcie nie zdołał ocalić 400 tysięcy ludzi, to teraz staje do pojedynku z Bogiem o życie choćby jednego pacjenta, starając się 'zasłonić płomień' gasnącego życia, nim Bóg zdąży go zdmuchnąć.",
        funkcja: "Łączy dwie płaszczyzny czasowe utworu i definiuje postawę człowieka odpowiedzialnego: ratowanie jednostkowego życia ma taką samą wartość jak wielkie czyny zbrojne."
      },
      {
        typ: "Teoretycznoliteracki",
        tytul: "Technika deheroizacji i demitologizacji w reportażu Hanny Krall",
        opis: "Marek Edelman celowo unika patosu, wzniosłych haseł i budowania spiżowych pomników. Opowiada o powstańcach jako o zwykłych, głodnych, często wystraszonych młodych ludziach (np. Anielewicz noszący czapkę z żółtym otokiem z próżności). Krall stosuje nielinearny montaż scen, zderzając tragedię getta z drobiazgami życia codziennego.",
        funkcja: "Pozwala przeanalizować formę reportażu jako sprzeciwu wobec zakłamywania historii przez patriotyczny kicz; pokazuje, że surowa prawda o człowieku jest bardziej poruszająca niż mit."
      }
    ]
  },
  {
    id: "camus-dzuma",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Dżuma",
    autor: "Albert Camus",
    epoka: "Współczesność",
    gatunek: "Powieść parabola (alegoryczna)",
    motywy: ["epidemia", "zło", "heroizm laicki", "solidarność", "absurd istnienia", "cierpienie niewinnych"],
    synteza: "Historia wybuchu dżumy w algierskim mieście Oran, będąca uniwersalną przypowieścią o zmaganiu człowieka ze złem, bezsensem cierpienia i koniecznością solidarnego oporu w imię ludzkiej przyzwoitości.",
    tematyMaturalne: [
      "Różne postawy ludzi wobec zagrożenia i cierpienia (Rieux, Tarrou, Paneloux, Cottard).",
      "Pojęcie laickiego heroizmu i moralności bez Boga.",
      "Dżuma jako uniwersalna metafora zła i systemów totalitarnych."
    ],
    konteksty: [
      {
        typ: "Filozoficzny",
        tytul: "Egzystencjalizm laicki i pojęcie heroizmu przyzwoitości (dr Bernard Rieux)",
        opis: "W filozofii Camusa świat jest absurdalny, pozbawiony obiektywnego boskiego sensu, a zło (bakcyl dżumy) jest trwałym elementem kondycji ludzkiej. Odpowiedzią dr. Bernarda Rieux na ten absurd nie jest jednak rezygnacja czy nihilizm, lecz bunt poprzez codzienną pracę i niesienie pomocy chorym bez oczekiwania na nagrodę w niebie ('być przyzwoitym').",
        funkcja: "Pozwala ukazać postawę heroizmu laickiego: człowiek tworzy sens własnego istnienia poprzez solidarność z cierpiącymi i walkę ze złem, nawet jeśli ta walka jest z góry skazana na ostateczną porażkę."
      },
      {
        typ: "Historyczno-alegoryczny",
        tytul: "Dżuma jako metafora 'brunatnej zarazy' – nazizmu i okupacji Europy",
        opis: "Camus pisał powieść tuż po II wojnie światowej, działając wcześniej we francuskim ruchu oporu (Resistance). Zamknięcie Oranu kordonem sanitarnym, bramy cmentarza, palenie ciał i bezradność ludności były bezpośrednią aluzją do nazistowskiego terroru, obozów zagłady i okupacji hitlerowskiej.",
        funkcja: "Daje klucz historyczny do odczytania paraboli; dowodzi, że bakcyl zła nigdy nie umiera na zawsze i może w każdej chwili uśpić czujność demokratycznych społeczeństw."
      },
      {
        typ: "Teologiczno-religijny",
        tytul: "Problem teodycei i ewolucja postawy ojca Paneloux",
        opis: "Jezuita Paneloux w pierwszym kazaniu grzmi, że dżuma jest sprawiedliwą karą boską za grzechy mieszkańców. Jednak widok potwornej, powolnej agonii niewinnego małego synka sędziego Othona łamie jego pewność teologiczną. W drugim kazaniu ojciec mówi już nie 'wy', lecz 'my' i przyznaje, że wobec cierpienia dziecka człowiek staje bezradny i może jedynie wierzyć wbrew rozumowi.",
        funkcja: "Stanowi wstrząsający kontekst filozoficzno-religijny ukazujący odwieczny spór o istnienie zła w świecie stworzonym przez miłosiernego Boga."
      }
    ]
  },
  {
    id: "orwell-1984",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Rok 1984",
    autor: "George Orwell",
    epoka: "Współczesność",
    gatunek: "Dystopia (antyutopia polityczna)",
    motywy: ["totalitaryzm", "inwigilacja", "nowomowa", "manipulacja historią", "zniewolenie umysłu", "bunt jednostki"],
    synteza: "Mroczna wizja totalitarnego państwa Oceania rządzonego przez Wielkiego Brata i Partię Angsocu, gdzie prywatność nie istnieje, myślozbrodnia jest karana torturami, a język i przeszłość są nieustannie fałszowane w celu pełnego zniszczenia ludzkiego 'ja'.",
    tematyMaturalne: [
      "Mechanizmy manipulacji i zniewolenia jednostki w państwie totalitarnym.",
      "Rola języka i fałszowania pamięci w sprawowaniu władzy absolutnej.",
      "Czy jednostka ma szansę w starciu z bezdusznym aparatem represji?"
    ],
    konteksty: [
      {
        typ: "Historyczno-polityczny",
        tytul: "Doświadczenie totalitaryzmów XX wieku: stalinizmu w ZSRR i hitleryzmu w Niemczech",
        opis: "Orwell napisał powieść w 1948 r., czerpiąc wzorce z realnie istniejących reżimów: kult jednostki Wielkiego Brata (Stalin), nienawiść do Goldsteina (Trocki), policja myśli (NKWD, Gestapo), procesy pokazowe i zmienne sojusze wojenne (pakt Ribbentrop-Mołotow).",
        funkcja: "Pokazuje, że Oceania nie jest fikcją science-fiction, lecz logicznym doprowadzeniem do skrajności metod stosowanych przez dwudziestowieczne reżimy dyktatorskie."
      },
      {
        typ: "Filozoficzno-lingwistyczny",
        tytul: "Koncepcja Nowomowy (Newspeak) a determinizm językowy (hipoteza Sapira-Whorfa)",
        opis: "Partia dąży do corocznego ograniczania liczby słów w słowniku nowomowy, aby uniemożliwić popełnienie myślozbrodni ('jeśli nie ma słowa oznaczającego wolność, myśl o wolności staje się niemożliwa'). Prawda staje się płynna w myśl pojęcia 'dwumyślenia' (doublethink): Wojna to pokój, Wolność to niewola, Ignorancja to siła.",
        funkcja: "Kluczowy kontekst demaskujący rolę manipulacji semantycznej we współczesnej propagandzie; dowodzi, że kontrola nad językiem oznacza pełną kontrolę nad ludzką świadomością."
      },
      {
        typ: "Literacki / Intertekstualny",
        tytul: "Tradycja literatury antyutopijnej – Jewgienij Zamiatin „My” i Aldous Huxley „Nowy wspaniały świat”",
        opis: "Orwell wpisuje się w nurt wielkich ostrzeżeń przed inżynierią społeczną. O ile jednak u Huxleya ludzie są zniewoleni za pomocą przyjemności, seksu i narkotyku soma, o tyle u Orwella Partia rządzi za pomocą czystego strachu, bólu i upokorzenia ('jeśli chcesz wiedzieć, czym jest przyszłość, wyobraź sobie but depczący ludzką twarz – wiecznie').",
        funkcja: "Umożliwia zestawienie dwóch przeciwstawnych modeli totalitaryzmu i pogłębioną dyskusję o metodach pacyfikowania wolności obywatelskiej."
      }
    ]
  },
  {
    id: "mrozek-tango",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Tango",
    autor: "Sławomir Mrożek",
    epoka: "Współczesność",
    gatunek: "Dramat groteskowy / teatr absurdu",
    motywy: ["bunt przeciw wolności", "kryzys tradycji", "brutalna siła", "groteska", "rodzina", "upadek kultury"],
    synteza: "Tragikomedia o rodzinie Stomila i Eleonory, która zburzyła wszelkie normy moralne, i ich synu Arturze, który paradoksalnie buntuje się przeciw anarchii, próbując na siłę przywrócić ład i tradycję. Jego klęska otwiera drogę do dyktatury prymitywnego chama Edka.",
    tematyMaturalne: [
      "Bunt odwrócony – młodzi w obronie zasad przeciw anarchii rodziców.",
      "Gdy abdykuje kultura i wartości, triumfuje brutalna siła fizyczna.",
      "Groteskowy obraz współczesnej rodziny w kryzysie tożsamości."
    ],
    konteksty: [
      {
        typ: "Kulturowo-społeczny",
        tytul: "Kryzys tradycyjnych wartości i rewolucja obyczajowa lat 60. XX wieku",
        opis: "Sztuka Mrożka (1964 r.) antycypowała nastroje buntu hippisowskiego i rozpadu autorytetów na Zachodzie. Pokolenie rodziców (Stomil) odrzuciło religię, śluby, konwenanse i dress code, żyjąc w wiecznym bałaganie. Artur odkrywa jednak tragiczny paradoks: skoro wszystko wolno, to bunt stał się niemożliwy, a pełna wolność bez formy rodzi nihilizm i pustkę.",
        funkcja: "Pozwala zrozumieć psychologiczną motywację Artura i zinterpretować utwór jako ostrzeżenie przed pułapką permisywizmu moralnego."
      },
      {
        typ: "Intertekstualny / Literacki",
        tytul: "Nawiązanie do „Wesela” Stanisława Wyspiańskiego (chocholi taniec a tango La Cumparsita)",
        opis: "Finałowa scena, w której prymitywny cham Edek w za małej marynarce Artura tańczy tango 'La Cumparsita' ze starym wujem Eugeniuszem, jest bezpośrednią trawestacją chocholego tańca z 'Wesela'. U Wyspiańskiego taniec oznaczał uśpienie narodu, u Mrożka – bezwzględne zniewolenie inteligencji przez chamską dyktaturę.",
        funkcja: "Ukazuje ciągłość rozrachunku z polską inteligencją; dowodzi, że słabość intelektualistów kończy się oddaniem władzy w ręce bezwzględnych populistów."
      },
      {
        typ: "Historiozoficzno-polityczny",
        tytul: "Mechanizm rodzenia się autorytaryzmów i dyktatur faszystowsko-komunistycznych",
        opis: "Dramat Mrożka jest historiozoficzną parabolą: gdy tradycyjne elity tracą wiarę w swoje ideały, a próby intelektualnego przywrócenia ładu zawodzą z powodu braku siły, w społeczeństwie pojawia się próżnia. Tę próżnię natychmiast wypełnia 'człowiek z dołu' (Edek), który nie potrzebuje ideologii, lecz rządzi czystą pięścią ('Ja tu teraz jestem szef').",
        funkcja: "Daje klucz politologiczny do zrozumienia genezy faszyzmu i totalitaryzmów w Europie w XX wieku."
      }
    ]
  },
  {
    id: "nowakowski-gora-edek",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Górą „Edek” (z tomu „Prawo prerii”)",
    autor: "Marek Nowakowski",
    epoka: "Współczesność",
    gatunek: "Opowiadanie obyczajowe / mikropowieść realistyczna",
    motywy: ["brutalność życia", "transformacja ustrojowa", "prawo dżungli", "arogancja", "bezradność inteligencji"],
    synteza: "Krótka, dosadna scenka z warszawskiego korka ulicznego, gdzie kierowca małego fiata (inteligent) zostaje bezczelnie zepchnięty z pasa przez potężnego forda scorpio prowadzonego przez współczesnego, aroganckiego nuworysza – nowego Edka.",
    tematyMaturalne: [
      "Prawo silniejszego jako zagrożenie dla kultury i norm społecznych.",
      "Przemiany mentalności Polaków w okresie wczesnego kapitalizmu.",
      "Bezradność tradycyjnej kultury wobec prymitywnej bezwzględności."
    ],
    konteksty: [
      {
        typ: "Społeczno-historyczny",
        tytul: "Transformacja ustrojowa w Polsce lat 90. XX wieku i narodziny drapieżnego kapitalizmu",
        opis: "Po upadku PRL w 1989 r. Polska weszła w okres gwałtownej budowy wolnego rynku. Obok wolności gospodarczej zjawisku temu towarzyszyło zachłyśnięcie się pieniądzem, cwaniactwo, brak szacunku dla prawa i narodziny tzw. 'dresiarstwa' i nuworyszostwa, gardzącego tradycyjnymi wartościami inteligenckimi.",
        funkcja: "Osadza opowiadanie w konkretnym momencie dziejowym; pozwala zinterpretować konflikt na jezdni jako socjologiczną diagnozę przemian w polskim społeczeństwie lat 90."
      },
      {
        typ: "Intertekstualny",
        tytul: "Bezpośrednie nawiązanie do postaci Edka z „Tanga” Sławomira Mrożka",
        opis: "Nowakowski celowo umieścił imię mrożkowskiego bohatera w cudzysłowie w tytule. Postać kierowcy wielkiego forda to zmaterializowany Edek z dramatu Mrożka, który wyszedł z teatru na ulice polskich miast: ma gruby kark, złoty łańcuch, czuje się bezkarny i dyktuje warunki słabszym.",
        funkcja: "Ukazuje ewolucję toposu chama u władzy: u Mrożka był to problem filozoficzno-teatralny, u Nowakowskiego staje się brutalną rzeczywistością codziennego życia w wolnej Polsce."
      },
      {
        typ: "Aksjologiczno-etyczny",
        tytul: "Kryzys etosu inteligenckiego i zasady ustępowania mądrzejszego",
        opis: "Kierowca malucha reprezentuje dawną kulturę: jest wykształcony, taktowny, szanuje kodeks drogowy i przepisy współżycia. Jednak w starciu z bezczelnością jego kultura staje się bezbronna – inteligent ustępuje z drogi, co agresor odczytuje nie jako klasę, lecz jako słabość.",
        funkcja: "Prowokuje do refleksji nad paradoksem tolerancji: czy kultura ma narzędzia do obrony przed wulgarną agresją, czy też jest skazana na kapitulację?"
      }
    ]
  },
  {
    id: "stasiuk-miejsce",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Miejsce (z tomu „Opowieści galicyjskie”)",
    autor: "Andrzej Stasiuk",
    epoka: "Współczesność",
    gatunek: "Opowiadanie eseistyczne / proza poetycka",
    motywy: ["pamięć", "przemijanie", "Łemkowszczyzna", "ślady przeszłości", "sacrum", "pustka"],
    synteza: "Opis pustego placu w Beskidzie Niskim, gdzie niegdyś stała drewniana łemkowska cerkiew. Narrator odtwarza w wyobraźni jej zapach, drewniane ściany i dawnych modlących się ludzi, dowodząc, że pamięć miejsca trwa mimo fizycznego zniszczenia materii.",
    tematyMaturalne: [
      "Pamięć o przeszłości zaklęta w krajobrazie i przedmiotach.",
      "Tragedia wysiedlonych narodów a tożsamość małych ojczyzn.",
      "Materialność a duchowość w doświadczeniu upływu czasu."
    ],
    konteksty: [
      {
        typ: "Historyczno-etniczny",
        tytul: "Akcja „Wisła” (1947 r.) i wykorzenienie kultury łemkowskiej z Beskidu Niskiego",
        opis: "W 1947 r. władze komunistyczne w ramach Akcji 'Wisła' przymusowo przesiedliły tysiące Łemków i Ukraińców na Ziemie Zachodnie. Ich wsie zostały spalone, a cerkwie zburzone lub zamienione na magazyny. Pustka opisywana przez Stasiuka jest bezpośrednią raną historyczną po tej czystce etnicznej.",
        funkcja: "Niezbędny kontekst faktograficzny; tłumaczy, dlaczego cerkiew zniknęła i uświadamia tragedię zagłady unikalnej, wielowiekowej kultury Karpat."
      },
      {
        typ: "Filozoficzno-metafizyczny",
        tytul: "Fenomenologia pamięci i sacrum miejsca (genius loci)",
        opis: "Według koncepcji 'genius loci' (ducha miejsca) przestrzeń nasycona przez wieki ludzką modlitwą, potem i obecnością zachowuje swój sakralny charakter nawet po zburzeniu budowli. Narrator Stasiuka w skupieniu bada cień fundamentów, dowodząc, że prawdziwe 'miejsce' istnieje poza czasem i fizyczną architekturą.",
        funkcja: "Pozwala zinterpretować opowiadanie jako głęboki esej filozoficzny o trwaniu niematerialnego śladu człowieka w przyrodzie."
      },
      {
        typ: "Kulturowo-muzealny",
        tytul: "Cerkiew łemkowska w skansenie a utrata autentyczności sacrum",
        opis: "W opowiadaniu pojawia się motyw rozebrania cerkwi i przeniesienia jej do muzeum na wolnym powietrzu (skansenu). Choć uratowało to belki przed zgniciem, w nowym miejscu cerkiew stała się martwym eksponatem dla turystów, tracąc swój pierwotny, żywy sens.",
        funkcja: "Służy do dyskusji o granicach ochrony zabytków: czy wyrwanie obiektu sakralnego z jego naturalnego krajobrazu nie jest formą uśmiercenia jego duszy?"
      }
    ]
  },
  {
    id: "tokarczuk-profesor-andrews",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Profesor Andrews w Warszawie (z tomu „Gra na wielu bębenkach”)",
    autor: "Olga Tokarczuk",
    epoka: "Współczesność",
    gatunek: "Opowiadanie psychologiczno-społeczne",
    motywy: ["stan wojenny", "obcość", "wieża Babel", "izolacja", "absurd", "solidarność ludzka"],
    synteza: "Angielski profesor psychologii przylatuje do Warszawy w przeddzień wprowadzenia stanu wojennego (grudzień 1981 r.). Odcięty od telefonów, nieznający języka polskiego, staje się bezradnym świadkiem czołgów na ulicach, kolejek po karpia i aresztowań, doświadczając skrajnej obcości i zagubienia.",
    tematyMaturalne: [
      "Stan wojenny oczami obcokrajowca – odmienność perspektywy narracyjnej.",
      "Bariera językowa i poczucie alienacji w obcym świecie.",
      "Zwykła ludzka solidarność w obliczu historycznego paraliżu."
    ],
    konteksty: [
      {
        typ: "Historyczno-polityczny",
        tytul: "Wprowadzenie stanu wojennego w Polsce (13 grudnia 1981 r.)",
        opis: "Generał Wojciech Jaruzelski ogłosił stan wojenny: wyłączono telefony, wprowadzono godzinę milicyjną, cenzurę korespondencji, czołgi na skrzyżowaniach i internowano tysiące działaczy 'Solidarności'. Polska została nagle odcięta od reszty świata.",
        funkcja: "Pozwala zrozumieć realia historyczne, w których znalazł się bohater; ukazuje szok cywilizacyjny człowieka z wolnego Zachodu wrzuconego w sam środek komunistycznego paraliżu państwa."
      },
      {
        typ: "Literacki / Kafkowski",
        tytul: "Motyw absurdu i alienacji rodem z „Procesu” Franza Kafki",
        opis: "Sytuacja profesora Andrewsa przypomina los Józefa K.: świat wokół niego traci racjonalne reguły, znikają opiekunowie, nie działają telefony, ludzie na ulicy mówią niezrozumiałym językiem i nikt nie potrafi wyjaśnić, co się dzieje. Bohater ulega narastającej paranoi.",
        funkcja: "Umożliwia interpretację utworu jako kafkowskiej metafory bezradności jednostki uwięzionej w bezdusznym, niezrozumiałym labiryncie historii."
      },
      {
        typ: "Archetypiczny / Biblijny",
        tytul: "Mit o wieży Babel i problem porozumienia między ludźmi",
        opis: "Nieznajomość polskiego przez Anglika i brak angielskiego u warszawiaków tworzy mur komunikacyjny (wieża Babel). Jednak w decydującym momencie, gdy profesor jest głodny i przemarznięty, zwykli Polacy dzielą się z nim chlebem i karpiem, porozumiewając się prostym językiem gestów i empatii.",
        funkcja: "Wskazuje na optymistyczną puentę: elementarna ludzka życzliwość potrafi przełamać najgłębsze bariery językowe i historyczne podziały."
      }
    ]
  },
  {
    id: "kapuscinski-herodot",
    kategoria: "podstawowy",
    kategoriaNazwa: "Zakres podstawowy",
    tytul: "Podróże z Herodotem (fragmenty)",
    autor: "Ryszard Kapuściński",
    epoka: "Współczesność",
    gatunek: "Reportaż podróżniczy / esej autobiograficzny",
    motywy: ["podróż", "spotkanie z Innym", "reportaż", "poznawanie świata", "ciekawość", "przekraczanie granic"],
    synteza: "Opowieść o początkach kariery reporterskiej autora, który wyjeżdżając w latach 50. i 60. XX w. do Indii, Chin i Afryki, zabiera ze sobą egzemplarz 'Dziejów' Herodota z Halikarnasu, odnajdując w starożytnym Greku swego mistrza duchowego i pierwszego globalnego korespondenta.",
    tematyMaturalne: [
      "Podróż jako próba zrozumienia Innego i samego siebie.",
      "Ciekawość świata jako źródło wiedzy i tolerancji.",
      "Starożytność jako żywy przewodnik po problemach współczesności."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-antropologiczny",
        tytul: "Filozofia dialogu Emmanuela Levinasa i koncepcja spotkania z „Innym”",
        opis: "W filozofii dialogu (Levinas, Tischner) spotkanie twarzą w twarz z Innym nakłada na człowieka moralną odpowiedzialność: wymaga odrzucenia europocentryzmu, pychy i przemocy na rzecz uważnego słuchania. Kapuściński, podobnie jak Herodot, nie ocenia obcych kultur przez pryzmat wyższości, lecz próbuje pojąć ich odmienny punkt widzenia.",
        funkcja: "Stanowi klucz etyczny do całego dorobku Kapuścińskiego; dowodzi, że reportaż jest nie tylko zawodem, lecz postawą szacunku wobec odmienności kulturowej."
      },
      {
        typ: "Historyczno-antyczny",
        tytul: "Herodot z Halikarnasu i narodziny metody reportażowej w V w. p.n.e.",
        opis: "Herodot, zwany 'ojcem historii', był przede wszystkim niestrudzonym podróżnikiem. Zbierał relacje naoczne (autopsja), dociekał przyczyn wojen grecko-perskich, spisywał mity i zwyczaje Scytów, Egipcjan i Persów, pytając miejscowych ludzi o ich pamięć.",
        funkcja: "Pozwala ukazać ciągłość dziennikarstwa: współczesny reporter korzysta z tego samego narzędzia co starożytny Grek – własnych nóg, oczu i zdolności do nawiązywania rozmowy."
      },
      {
        typ: "Biograficzno-historyczny",
        tytul: "Polska lat 50. za żelazną kurtyną i marzenie o przekroczeniu granicy",
        opis: "Młody Kapuściński dorastał w zniszczonej powojennej Warszawie w szarych czasach stalinizmu. Granica państwowa była wówczas barierą nie do przebycia. Wyjazd do Indii był dla niego szokiem kulturowym i zrzuceniem ideologicznych klapek z oczu.",
        funkcja: "Tłumaczy młodzieńczą zachłanność autora na świat i wyjaśnia, dlaczego podróż była dla pokolenia żyjącego w PRL aktem najwyższej wolności wewnętrznej."
      }
    ]
  },

  // ==========================================
  // SZKOŁA PODSTAWOWA (DO MATURY)
  // ==========================================
  {
    id: "krasicki-bajki",
    kategoria: "podstawowa-szkola",
    kategoriaNazwa: "Szkoła podstawowa",
    tytul: "Bajki (np. „Kruk i lis”, „Dewotka”, „Ptaszki w klatce”, „Jagnię i wilcy”)",
    autor: "Ignacy Krasicki",
    epoka: "Oświecenie",
    gatunek: "Bajka epigramatyczna / narracyjna",
    motywy: ["ludzkie wady", "prawo silniejszego", "fałszywa pobożność", "wolność a niewola", "morał", "rozum"],
    synteza: "Krótkie, mistrzowskie wierszowane powiastki zwierzęce niosące uniwersalne pouczenie moralne: obnażają naiwność ulegających pochlebstwom, hipokryzję bigotów i bezwzględność silniejszych wobec słabych.",
    tematyMaturalne: [
      "Zwierzęce maski jako lustro ludzkich przywar.",
      "Krytyka hipokryzji religijnej i naiwności.",
      "Wolność jako wartość najwyższa w bajkach Ignacego Krasickiego."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-racjonalistyczny",
        tytul: "Oświeceniowy racjonalizm i walka z ciemnotą umysłową",
        opis: "Myśliciele oświecenia wierzyli, że człowiek powinien kierować się chłodnym osądem rozumu, a nie emocjami czy przesądami. W bajce 'Kruk i lis' próżność odbiera krukowi rozum, a w 'Dewotce' Krasicki demaskuje fałszywą religijność kobiety, która bijąc służącą, odmawia słowa 'i odpuść nam nasze winy'.",
        funkcja: "Pozwala ukazać bajki jako miniaturowe traktaty filozoficzne służące wychowaniu krytycznie myślącego obywatela."
      },
      {
        typ: "Literacki / Tradycja gatunku",
        tytul: "Antyczna bajka ezopowa i bajkopisarstwo Jeana de La Fontaine’a",
        opis: "Krasicki był kontynuatorem tradycji sięgającej Ezopa, Fedrusa i XVII-wiecznego mistrza francuskiego La Fontaine'a. Wprowadził jednak bajkę epigramatyczną o rygorystycznej zwięzłości i lakonizmie, gdzie każde słowo jest precyzyjnie zważone.",
        funkcja: "Stanowi dowód na mistrzostwo językowe Krasickiego i wpisuje polskie bajki w nurt arcydzieł literatury europejskiej."
      },
      {
        typ: "Historyczno-alegoryczny",
        tytul: "Rozbiory Polski w bajkach „Ptaszki w klatce” oraz „Jagnię i wilcy”",
        opis: "Bajka 'Ptaszki w klatce' to aluzja do utraty niepodległości: stary czyżyk płacze, bo pamięta wolność, a młody dziwi się łzom, bo urodził się w klatce i niewola jest dla niego normą. Z kolei 'Jagnię i wilcy' ('Smacznyś, słaby i w lesie!') to bezwzględny portret imperialnej polityki zaborców (Rosji, Prus, Austrii) rozdzierających bezbronną Rzeczpospolitą.",
        funkcja: "Umożliwia odczytanie bajek nie tylko jako uniwersalnych pouczeń moralnych, lecz jako przenikliwego komentarza do tragedii rozbiorów Polski."
      }
    ]
  },
  {
    id: "mickiewicz-dziady-2",
    kategoria: "podstawowa-szkola",
    kategoriaNazwa: "Szkoła podstawowa",
    tytul: "Dziady cz. II",
    autor: "Adam Mickiewicz",
    epoka: "Romantyzm",
    gatunek: "Dramat romantyczny",
    motywy: ["obrzęd dziadów", "wina i kara", "cierpienie jako warunek człowieczeństwa", "zaświaty", "ludowa moralność"],
    synteza: "Przedstawienie archaicznego, pogańskiego obrzędu wywoływania duchów zmarłych w cmentarnej kaplicy pod przewodnictwem Guślarza, gdzie zjawy Józia i Rózi, Złego Pana oraz Zosi głoszą twarde prawdy moralne o warunkach osiągnięcia zbawienia.",
    tematyMaturalne: [
      "Ludowy kodeks moralny – czego uczy nas spotkanie z duchami?",
      "Cierpienie i empatia jako miara prawdziwego człowieczeństwa.",
      "Świat żywych i umarłych w wierzeniach romantycznych."
    ],
    konteksty: [
      {
        typ: "Kulturowo-antropologiczny",
        tytul: "Przedchrześcijański obrzęd dziadów na Kresach Wschodnich",
        opis: "Mickiewicz we wstępie sam opisuje pogański rytuał uczty cmentarnej odprawiany potajemnie przez lud białoruski i litewski. Wierzono, że głodne dusze zmarłych przybywają w noc zaduszną, by prosić o strawę i modlitwę, a żywi mogą od nich zyskać pouczenie duchowe.",
        funkcja: "Pozwala ukazać głębokie zakorzenienie dramatu w autentycznym folklorze Kresów i fascynację romantyków tym, co pierwotne, ludowe i zakazane przez oficjalny Kościół."
      },
      {
        typ: "Aksjologiczno-moralny",
        tytul: "Moralność naturalna: pełnia człowieczeństwa wymaga znoszenia cierpienia i współczucia",
        opis: "Trzy kategorie duchów formułują ludowy dekalog: Józio i Rózia przypominają, że kto nie doznał goryczy na ziemi, nie zazna słodyczy w niebie; Zły Pan dowodzi, że kto nie był człowiekiem dla poddanych, temu nikt nie pomoże; Zosia uczy, że lekceważenie miłości ziemskiej uniemożliwia zbawienie.",
        funkcja: "Służy do analizy humanistycznego przesłania utworu: życie ludzkie musi być przeżyte w pełni – z jego trudami, odpowiedzialnością za innych i dojrzałymi uczuciami."
      },
      {
        typ: "Literacki / Szekspirowski",
        tytul: "Dramaturgia Williama Szekspira („Hamlet”, „Makbet”) a świat zjaw",
        opis: "Romantycy odrzucili klasycystyczną zasadę prawdopodobieństwa, czerpiąc z teatru elżbietańskiego, gdzie duchy realnie wkraczały na scenę i ingerowały w sumienia żywych. Słynne motto z 'Hamleta': 'Zdaje się, że widzę... gdzie? przed oczyma duszy mojej' patronuje całej koncepcji kontaktu z transcendencją.",
        funkcja: "Pozwala osadzić utwór w europejskim przewrocie romantycznym, legitymizującym obecność świata metafizycznego na scenie teatralnej."
      }
    ]
  },
  {
    id: "fredro-zemsta",
    kategoria: "podstawowa-szkola",
    kategoriaNazwa: "Szkoła podstawowa",
    tytul: "Zemsta",
    autor: "Aleksander Fredro",
    epoka: "Romantyzm (forma klasycystyczna)",
    gatunek: "Komedia kontuszowa (charakterów i intrygi)",
    motywy: ["sarmatyzm", "spór o mur graniczny", "miłość wbrew zwaśnionym rodom", "Papkin", "komizm", "pojednanie"],
    synteza: "Arcydzieło polskiej komedii ukazujące zaciekły spór dwóch sarmatów – gwałtownego Cześnika Raptusiewicza i obłudnego Rejenta Milczka – mieszkających w jednym zamku, zakończony ślubem ich wychowanków: Klary i Wacława.",
    tematyMaturalne: [
      "Karykaturalny i ciepły obraz polskiej sarmacji.",
      "Różne typy komizmu (sytuacyjny, słowny, postaci) w „Zemście”.",
      "Spór sąsiedzki i sposoby jego zażegnania."
    ],
    konteksty: [
      {
        typ: "Biograficzno-historyczny",
        tytul: "Autentyczny spór o zamek Kamieniec w Odrzykoniu (akta procesowe z 1630 r.)",
        opis: "Fredro znalazł inspirację we własnym majątku: żeniąc się z Zofią Jabłonowską, wszedł w posiadanie połowy zamku w Odrzykoniu. W starych dokumentach sądowych odkrył historię wieloletniego procesu między autentycznymi właścicielami: gwałtownikiem Janem Skotnickim (pierwowzór Rejenta) a Piotrem Firlejem (pierwowzór Cześnika), zakończonego ślubem ich dzieci.",
        funkcja: "Dowodzi, że z pozoru absurdalny konflikt o mur graniczny był wiernym odzwierciedleniem pieniactwa i obyczajowości dawnej szlachty polskiej."
      },
      {
        typ: "Kulturowo-obyczajowy",
        tytul: "Mit i dekonstrukcja polskiego sarmatyzmu",
        opis: "Komedia jest portretem schyłkowego sarmatyzmu. Cześnik reprezentuje staroszlachecką krewkość, gest, tradycję militarną i gościnność, z kolei Rejent – dewocję, chciwość i prawnicze pieniactwo. Postać Papkina uosabia zubożałego sarmatę-samochwała o mentalności żołnierza-tchórza.",
        funkcja: "Pozwala na wielowymiarową ocenę mentalności sarmackiej: Fredro z jednej strony wyśmiewa warcholstwo szlacheckie, z drugiej patrzy na odchodzący świat kontuszowy z melancholią i życzliwym uśmiechem."
      },
      {
        typ: "Literacki / Tradycja komedii",
        tytul: "Kunszt wiersza ośmiozgłoskowego i tradycja Molierowska",
        opis: "Fredro mistrzowsko operuje ośmiozgłoskowcem ze zmiennym akcentem, tworząc frazy, które na stałe weszły do języka polskiego ('Niech się dzieje wola Nieba, z nią się zawsze zgadzać trzeba!', 'Jeśli nie chcesz mojej zguby, krokodyla daj mi, luby'). Nawiązuje do komedii Moliera, łącząc intrygę matrymonialną z bezbłędnym rysunkiem psychologicznym postaci.",
        funkcja: "Ukazuje 'Zemstę' jako niedościgniony wzorzec polskiego humoru językowego i kunsztu wersyfikacyjnego."
      }
    ]
  },
  {
    id: "slowacki-balladyna",
    kategoria: "podstawowa-szkola",
    kategoriaNazwa: "Szkoła podstawowa",
    tytul: "Balladyna",
    autor: "Juliusz Słowacki",
    epoka: "Romantyzm",
    gatunek: "Tragedia romantyczna / baśń dramatyczna",
    motywy: ["zbrodnia i kara", "żądza władzy", "wypieranie się matki", "świat baśniowy", "krwawa plama", "sprawiedliwość"],
    synteza: "Krwawa droga prostej dziewczyny z wiejskiej chaty na królewski tron w Gnieźnie: od zamordowania w lesie siostry Aliny w konkursie zbierania malin, po serię kolejnych zbrodni, wyparcie się matki i śmierć od boskiego pioruna po wydaniu na samą siebie sprawiedliwego wyroku.",
    tematyMaturalne: [
      "Zbrodnia jako środek do zdobycia władzy i jej nieuchronne skutki.",
      "Motyw wyparcia się własnego pochodzenia i matczynej miłości.",
      "Przenikanie się świata realnego z baśniową fantastyką."
    ],
    konteksty: [
      {
        typ: "Literacki / Szekspirowski",
        tytul: "Inspiracje dramaturgią Williama Szekspira („Makbet”, „Sen nocy letniej”, „Król Lear”)",
        opis: "Słowacki stworzył arcydzieło, jawnie nawiązując do sztuk Szekspira: Balladyna idzie śladem Makbeta (zbrodnia pociąga za sobą kolejne morderstwa, krwawa plama na czole nie daje się zmyć jak krew na rękach Lady Makbet); postacie Goplany, Skierki i Chochlika to świat elfa Puka ze 'Snu nocy letniej'; cierpienie wygnanej Wdowy nawiązuje do tragedii Króla Leara.",
        funkcja: "Pozwala odczytać dramat jako wielką, świadomą grę z tradycją szekspirowską, przeniesioną w słowiański, baśniowy krajobraz okolic jeziora Gopło."
      },
      {
        typ: "Kulturowo-baśniowy",
        tytul: "Struktura baśni ludowej i topos sprawiedliwości metafizycznej",
        opis: "Utwór wykorzystuje archetypiczne motywy baśniowe: dwie siostry (dobra i zła), konkurs zbierania malin, czarodziejski dzban, zaklęty wierzbowy kochanek Grabiec, korona Popielów. W finale zbrodniarka jako królowa musi wydać trzy wyroki śmierci za nierozliczone zbrodnie, ściągając na siebie sprawiedliwy piorun z nieba.",
        funkcja: "Dowodzi nadrzędnego przesłania moralnego: na świecie istnieje ład moralny, którego nie da się bezkarnie zniszczyć – zło rodzi samozagładę."
      },
      {
        typ: "Historyczno-narodowy",
        tytul: "Legendarne początki państwa polskiego i kwestia prawowitej władzy",
        opis: "Akcja toczy się 'za czasów bajecznych koło jeziora Gopło'. Słowacki wplata motyw korony Lecha – symbolu prawowitej, suwerennej i czystej władzy w Polsce, którą zagubił zły król Popiel IV. Walka o koronę jest metaforą zmagań o duszę i wolność ojczyzny w dobie zaborów.",
        funkcja: "Pozwala spojrzeć na dramat głębiej: poza baśniową intrygą kryje się w nim romantyczna refleksja o przyczynach upadku dawnej Polski i poszukiwaniu czystej moralnie władzy."
      }
    ]
  },

  // ==========================================
  // LEKTURY DODATKOWE
  // ==========================================
  {
    id: "kochanowski-treny",
    kategoria: "dodatkowy",
    kategoriaNazwa: "Lektury dodatkowe",
    tytul: "Treny (jako cykl poetycki)",
    autor: "Jan Kochanowski",
    epoka: "Renesans",
    gatunek: "Cykl poetycki (epicedium żałobne)",
    motywy: ["żałoba ojca", "kryzys światopoglądowy", "upadek stoicyzmu", "humanizm", "Urszulka", "pocieszenie"],
    synteza: "Genialny, autobiograficzny cykl 19 utworów napisanych po śmierci ukochanej dwuletniej córki Urszulki, będący zarazem poruszającym zapisem ojcowskiego bólu i dramatycznym kryzysem renesansowej wiary w rozum, stoicyzm i ład świata.",
    tematyMaturalne: [
      "Rozpad renesansowego światopoglądu pod wpływem osobistej tragedii.",
      "Obraz ojcowskiego cierpienia i proces wychodzenia z żałoby.",
      "Treny jako nowatorskie przełamanie antycznych reguł gatunkowych."
    ],
    konteksty: [
      {
        typ: "Filozoficzny",
        tytul: "Kryzys renesansowego stoicyzmu (Cicero, Seneka) i upadek cnoty",
        opis: "Kochanowski całe życie budował światopogląd oparty na stoickim opanowaniu (afekty nie powinny mącić spokoju mędrca). W Trenie IX i XI autor z goryczą wyznaje bankructwo tej filozofii: cnota nie chroni przed nieszczęściem, a filozof płacze jak każdy prosty człowiek ('Fraszka cnota! – powiada Brutus porażony').",
        funkcja: "Kluczowy kontekst ukazujący wielkość intelektualną Kochanowskiego: odważył się zakwestionować fundamenty renesansowego humanizmu w zderzeniu z nagą rzeczywistością cierpienia."
      },
      {
        typ: "Gatunkowo-antyczny",
        tytul: "Przełamanie konwencji antycznego trenu (epicedium)",
        opis: "W starożytnej Grecji i Rzymie treny pisano wyłącznie ku czci wybitnych wodzów, władców i mężów stanu. Kochanowski dokonał rewolucji estetycznej: bohaterem monumentalnego cyklu uczynił małe, dwuletnie dziecko, podnosząc żal rodzicielski do rangi uniwersalnego dramatu egzystencjalnego.",
        funkcja: "Świadczy o nowatorstwie poetyckim Czarnolasu i humanizmie renesansowym, dla którego każda indywidualna istota ludzka ma nieskończoną wartość."
      },
      {
        typ: "Religijno-chrystianizacyjny",
        tytul: "Pojednanie z Bogiem i koncepcja pocieszenia w Trenie XIX (Sen)",
        opis: "Kres rozpaczy przynosi Tren XIX, w którym poecie ukazuje się we śnie zmarła matka z Urszulką na ręku. Matka napomina go, by zaufał Opatrzności, przypominając, że mała uniknęła ziemskich cierpień, i zaleca chrześcijańską pokorę: 'Ludzkie przygody ludzko noś'.",
        funkcja: "Zamyka kompozycję cyklu jako drogi: od buntu i bluźnierstwa, przez zwątpienie, po powrót do dojrzałej wiary chrześcijańskiej i harmonii."
      }
    ]
  },
  {
    id: "slowacki-kordian",
    kategoria: "dodatkowy",
    kategoriaNazwa: "Lektury dodatkowe",
    tytul: "Kordian",
    autor: "Juliusz Słowacki",
    epoka: "Romantyzm",
    gatunek: "Dramat romantyczny",
    motywy: ["dojrzewanie bohatera", "ból istnienia (Weltschmerz)", "winkelriedyzm", "zamach na cara", "Strach i Imaginacja"],
    synteza: "Dramat o duchowym dojrzewaniu młodego arystokraty: od młodzieńczego rozczarowania miłością i światem w trakcie podróży po Europie, przez narodziny idei walki o wolność na szczycie Mont Blanc ('Polska Winkelriedem narodów!'), po tragiczny spisek na życie cara w Warszawie.",
    tematyMaturalne: [
      "Ewolucja bohatera romantycznego – od marzyciela do bojownika.",
      "Winkelriedyzm jako polemika z mesjanizmem Mickiewicza.",
      "Moralne dylematy walki o wolność – zabójstwo tyrana a etyka rycerska."
    ],
    konteksty: [
      {
        typ: "Historyczno-polityczny",
        tytul: "Powstanie listopadowe i spisek koronacyjny na cara Mikołaja I (1829 r.)",
        opis: "Dramat analizuje przyczyny klęski zrywu z 1830 r. W scenie w podziemiach katedry św. Jana Słowacki ukazuje autentyczny spisek podchorążych planujących zamach na cara podczas jego koronacji na króla Polski. Przedstawia kunktatorstwo starych generałów (Prezes – Niemcewicz) i bezsilność młodego pokolenia.",
        funkcja: "Stanowi bezwzględną diagnozę słabości psychicznej przywódców powstania listopadowego, którzy bali się podjąć radykalny czyn rewolucyjny."
      },
      {
        typ: "Polemiczno-literacki",
        tytul: "Polemika z mesjanizmem Mickiewicza: Winkelriedyzm zamiast „Polski Chrystusem narodów”",
        opis: "Monolog na Mont Blanc jest bezpośrednią odpowiedzią na Wielką Improwizację z 'Dziadów cz. III'. Słowacki odrzuca bierne cierpienie narodu ('Polska Chrystusem narodów') jako usypiające i proponuje winkelriedyzm: aktywną walkę zbrojną na wzór szwajcarskiego bohatera Arnolda Winkelrieda, który skupił na własnej piersi włócznie wrogów, by otworzyć drogę rodakom.",
        funkcja: "Kluczowy kontekst ideowy ukazujący rywalizację dwóch wieszczów o rząd dusz i wskazujący na czyn zbrojny jako jedyną drogę do wolności."
      },
      {
        typ: "Filozoficzno-psychologiczny",
        tytul: "„Choroba wieku” (Weltschmerz) oraz psychomachia pod drzwiami sypialni cara",
        opis: "Młody Kordian cierpi na typową dla epoki apatię i brak celu życiowego. Gdy wreszcie decyduje się zabić cara, pod drzwiami jego sypialni toczy się walka psychiczna (psychomachia): uosobione Strach i Imaginacja paraliżują jego wolę, ponieważ etos rycerski nie pozwala mu na skrytobójczy mord w sypialni.",
        funkcja: "Dowodzi, że Kordian poniósł klęskę nie z powodu tchórzostwa, lecz przez zbyt wielką wrażliwość moralną uniemożliwiającą mu bycie bezwzględnym zbrodniarzem."
      }
    ]
  },
  {
    id: "legenda-o-sw-aleksym",
    kategoria: "dodatkowy",
    kategoriaNazwa: "Lektury dodatkowe",
    tytul: "Legenda o św. Aleksym (fragmenty)",
    autor: "Anonim",
    epoka: "Średniowiecze",
    gatunek: "Legenda hagiograficzna (żywot świętego)",
    motywy: ["asceza", "świętość", "wyrzeczenie się dóbr", "męczeństwo za życia", "cuda", "teocentryzm"],
    synteza: "Średniowieczny wierszowany żywot rzymskiego patrycjusza, który w noc poślubną opuszcza młodą żonę i bogaty dom, rozdaje majątek ubogim i wybiera skrajne poniżenie oraz ascezę, spędzając 16 lat jako nierozpoznany żebrak pod schodami pałacu własnego ojca.",
    tematyMaturalne: [
      "Wzorzec świętego ascety w kulturze średniowiecza.",
      "Wyrzeczenie się doczesności w imię wartości wiecznych.",
      "Cuda i niezwykłe znaki jako potwierdzenie świętości."
    ],
    konteksty: [
      {
        typ: "Kulturowo-religijny",
        tytul: "Średniowieczny teocentryzm i parenetyczny wzorzec ascety",
        opis: "W kulturze średniowiecza Bóg stanowił centrum wszelkiej myśli i dążeń (teocentryzm). Literatura miała charakter parenetyczny – tworzyła gotowe wzorce do naśladowania (święty, rycerz, władca). Asceza (umartwianie ciała, głód, chłód) była postrzegana jako najdoskonalsza droga do oczyszczenia duszy i osiągnięcia życia wiecznego.",
        funkcja: "Tłumaczy motywacje Aleksego, które dla współczesnego odbiorcy mogą wydawać się nieludzkie lub egoistyczne wobec porzuconej rodziny; ukazuje prymat zbawienia nad więzami rodzinnymi."
      },
      {
        typ: "Teoretycznoliteracki / Tradycja gatunku",
        tytul: "Konwencja hagiograficzna (legenda z 'Legenda Aurea' Jakuba de Voragine)",
        opis: "Utwór realizuje żelazne reguły średniowiecznego żywota świętego: cudowne narodziny wymodlone przez rodziców, wczesna pobożność, radykalna decyzja o ucieczce, próby wiary, upokorzenie i pośmiertne cuda (dzwony w Rzymie dzwoniące same, uzdrawiający zapach ciała, list, który z dłoni zmarłego może wyjąć tylko czysta żona).",
        funkcja: "Pozwala przeanalizować mechanizmy literatury dewocyjnej i jej rolę w budowaniu autorytetu Kościoła w średniowieczu."
      },
      {
        typ: "Intertekstualny / Reinterpretacja współczesna",
        tytul: "Poezja ks. Jana Twardowskiego lub Kazimiery Iłłakowiczówny – demitologizacja ascezy",
        opis: "Współczesna kultura chrześcijańska i literatura (np. wiersze ks. Jana Twardowskiego) często polemizują ze średniowieczną formą ascezy, podkreślając, że miłość do Boga powinna wyrażać się w miłości i odpowiedzialności za drugiego człowieka (rodzinę, żonę), a nie w ucieczce od świata.",
        funkcja: "Daje doskonały punkt wyjścia do dyskusji o ewolucji pojmowania świętości: od średniowiecznego umartwienia po współczesny humanizm chrześcijański."
      }
    ]
  },
  {
    id: "kwiatki-sw-franciszka",
    kategoria: "dodatkowy",
    kategoriaNazwa: "Lektury dodatkowe",
    tytul: "Kwiatki świętego Franciszka z Asyżu (fragmenty)",
    autor: "Anonim (tłum. Leopold Staff)",
    epoka: "Średniowiecze",
    gatunek: "Przypowieść hagiograficzna / zbiór opowieści",
    motywy: ["franciszkanizm", "miłość do stworzenia", "święte ubóstwo", "radość wiary", "braterstwo", "wilk z Gubbio"],
    synteza: "Zbiór uroczych, prostych opowieści o życiu św. Franciszka i jego pierwszych braci, głoszących pochwałę radosnej wiary, dobrowolnego ubóstwa, pokory oraz braterstwa ze wszystkimi stworzeniami (kazanie do ptaków, nawrócenie krwiożerczego wilka z Gubbio).",
    tematyMaturalne: [
      "Franciszkanizm jako radosna alternatywa dla surowej ascezy średniowiecznej.",
      "Człowiek w harmonii z przyrodą – miłość do braci mniejszych.",
      "Siła pokory i dobroci w przezwyciężaniu zła."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-teologiczny",
        tytul: "Ruch franciszkański i afirmacja stworzenia w XIII wieku",
        opis: "Św. Franciszek z Asyżu dokonał duchowego przewrotu w Kościele: w miejsce lęku przed piekłem i pogardy dla ciała wprowadził teologię miłości, zachwytu nad pięknem świata jako dzieła Bożego oraz ideę 'świętego ubóstwa' (odrzucenia bogactwa rodzącego pychę i wojny).",
        funkcja: "Stanowi kontrast dla postawy św. Aleksego; ukazuje dwa diametralnie różne modele średniowiecznej duchowości: ascezę ucieczki od świata vs radosną ascezę braterstwa z całym stworzeniem."
      },
      {
        typ: "Intertekstualny / Młodopolski",
        tytul: "Młodopolski franciszkanizm – poezja Jana Kasprowicza („Księga ubogich”) i Leopolda Staffa",
        opis: "Na przełomie XIX i XX wieku pod wpływem dekadentyzmu i pesymizmu nastąpił renesans franciszkanizmu. Leopold Staff (który genialnie przetłumaczył 'Kwiatki...' na polski) oraz Jan Kasprowicz odnaleźli w postawie Biedaczyny z Asyżu ratunek przed rozpaczą, tworząc wiersze pełne pokornego zachwytu nad polnymi kwiatami i prostym życiem.",
        funkcja: "Pokazuje ponadczasowość myśli franciszkańskiej jako uniwersalnego lekarstwa na kryzysy duchowe kolejnych epok."
      },
      {
        typ: "Ekologiczno-etyczny",
        tytul: "Św. Franciszek jako patron ekologii i etyki poszanowania zwierząt",
        opis: "Epizod z oswojeniem wilka z Gubbio oraz kazanie do ptaków ukazują zwierzęta nie jako przedmioty eksploatacji, lecz jako 'braci mniejszych', czujące istoty mające swoje miejsce w Bożym planie. Franciszek proponuje mieszkańcom Gubbio zawarcie paktu: ludzie będą karmić wilka, a wilk przestanie ich atakować.",
        funkcja: "Umożliwia odczytanie średniowiecznego tekstu w kontekście współczesnej wrażliwości ekologicznej i etyki praw zwierząt."
      }
    ]
  },
  {
    id: "szekspir-romeo-i-julia",
    kategoria: "dodatkowy",
    kategoriaNazwa: "Lektury dodatkowe",
    tytul: "Romeo i Julia",
    autor: "William Szekspir",
    epoka: "Renesans / Teatr elżbietański",
    gatunek: "Tragedia miłosna",
    motywy: ["miłość tragiczna", "zwaśnione rody", "konflikt pokoleń", "przypadek a przeznaczenie", "śmierć kochanków"],
    synteza: "Nieśmiertelna historia miłości dwojga młodych ludzi w Weronie, którzy wbrew rodowej nienawiści Montekich i Kapuletich biorą potajemny ślub, a seria tragicznych nieporozumień prowadzi ich do samobójczej śmierci, stającej się jedyną ceną za pojednanie ich rodzin.",
    tematyMaturalne: [
      "Miłość silniejsza niż nienawiść – walka uczucia z konwenansem.",
      "Rola przypadku i nieuchronnego losu w tragedii kochanków.",
      "Cena, jaką płacą dzieci za błędy i nienawiść rodziców."
    ],
    konteksty: [
      {
        typ: "Kulturowo-archetypiczny",
        tytul: "Antyczny mit o Pyramie i Tyzbe (z „Metamorfoz” Owidiusza)",
        opis: "Fabuła tragedii Szekspira jest bezpośrednim przetworzeniem antycznego mitu o babilońskich kochankach Pyramie i Tyzbe, których rodzice zabraniali im się widywać. Podczas schadzki przy grobowcu nieporozumienie z zakrwawionym welonem i lwem doprowadza oboje do samobójstwa.",
        funkcja: "Pozwala ukazać Romea i Julię jako archetyp nieszczęśliwych kochanków wpisany w odwieczną tradycję kultury śródziemnomorskiej."
      },
      {
        typ: "Społeczno-obyczajowy",
        tytul: "Włoskie wendety rodowe epoki renesansu a wolny wybór małżeński",
        opis: "W renesansowych miastach-państwach Włoch (jak Werona czy Florencja) krwawe wendety między arystokratycznymi klanami paraliżowały życie publiczne. Małżeństwa były traktowane jako kontrakty polityczno-finansowe zawierane przez ojców (Kapulet zmuszający Julię do poślubienia Parysa).",
        funkcja: "Ukazuje bunt Julii i Romea jako rewolucyjny krok w stronę wolności jednostki i prawa do decydowania o własnym sercu przeciw opresyjnemu patriarchalizmowi."
      },
      {
        typ: "Intertekstualny / Poetycki",
        tytul: "Cyprian Kamil Norwid „W Weronie” – reinterpretacja tragedii kochanków",
        opis: "Norwid w słynnym wierszu opisuje ruiny grobu Julii, nad którym toczy się spór: czy spadający deszcz meteorytów to łzy aniołów płaczących nad ludzkim losem, czy jedynie bezduszne kamienie rzucane przez naturę ('A ludzie mówią, i mówią uczenie, że to nie łzy są, ale że kamienie...').",
        funkcja: "Pozwala zestawić renesansowy dramat miłosny z XIX-wieczną refleksją filozoficzną nad sensem cierpienia i miejscem współczucia w kosmosie."
      }
    ]
  },
  {
    id: "mickiewicz-konrad-wallenrod",
    kategoria: "dodatkowy",
    kategoriaNazwa: "Lektury dodatkowe",
    tytul: "Konrad Wallenrod",
    autor: "Adam Mickiewicz",
    epoka: "Romantyzm",
    gatunek: "Powieść poetycka",
    motywy: ["wallenrodyzm", "zdrada w imię ojczyzny", "machiawelizm", "ofiara życia i honoru", "rola poezji (Wajdelota)"],
    synteza: "Tragiczna opowieść o litewskim patriocie Walterze Alfie, który wychowany przez Krzyżaków pod fałszywym nazwiskiem Konrada Wallenroda staje na czele Zakonu, by podstępem doprowadzić go do militarnej klęski, płacąc za ocalenie Litwy utratą honoru, miłości Aldony i własnym życiem.",
    tematyMaturalne: [
      "Moralne granice walki o ojczyznę – czy cel uświęca środki?",
      "Tragizm bohatera zmuszonego do działania podstępem (wallenrodyzm).",
      "Rola poezji jako strażniczki tożsamości narodowej (Pieśń Wajdeloty)."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-polityczny",
        tytul: "Machiawelizm – motto z Niccolò Machiavellego: „Trzeba być lisem i lwem”",
        opis: "Mickiewicz opatrzył utwór mottem z 'Księcia': naród słaby militarnie w starciu z potęgą musi stosować metody lisa (chytrość, zdradę, podstęp), gdy metody lwa (otwarta walka) prowadzą do rzezi. Wallenrod łamie rycerski kodeks honoru, dokonując zdrady, co niszczy jego psychikę i moralną czystość.",
        funkcja: "Kluczowy kontekst definiujący pojęcie wallenrodyzmu: tragiczny konflikt między obowiązkiem patriotycznym a uniwersalnym kodeksem moralnym jednostki."
      },
      {
        typ: "Historyczno-aluzyjny",
        tytul: "Sytuacja Polaków pod zaborem rosyjskim przed powstaniem listopadowym (konspiracja pod cenzurą)",
        opis: "Książka ukazała się w Petersburgu w 1828 r. Mickiewicz zastosował kamuflaż historyczny (kostium średniowiecznych wojen polsko-krzyżackich), by zmylić carską cenzurę. W rzeczywistości utwór był wezwaniem do podziemnej walki z caratem skierowanym do spiskowców w Warszawie.",
        funkcja: "Tłumaczy historyczną funkcję utworu, który stał się moralnym katalizatorem wybuchu powstania listopadowego ('Słowo stało się ciałem, a Wallenrod Belwederem')."
      },
      {
        typ: "Teoretycznoliteracki / Rola poezji",
        tytul: "Powieść Wajdeloty i topos poezji jako „arki przymierza między dawnymi i młodszymi laty”",
        opis: "Starzec Halban uosabia moc pieśni ludowej, która przechowała w małym Walterze pamięć o litewskim pochodzeniu i zapaliła w nim ogień zemsty. Pieśń Wajdeloty głosi, że najeźdźca może zniszczyć miasta i zamordować ludzi, lecz dopóki żyje poezja narodowa, naród nie zginie.",
        funkcja: "Ukazuje romantyczną koncepcję sztuki jako niezniszczalnego depozytu tożsamości narodowej i duchowej broni w walce z okupantem."
      }
    ]
  },
  {
    id: "krasinski-nie-boska-komedia",
    kategoria: "dodatkowy",
    kategoriaNazwa: "Lektury dodatkowe",
    tytul: "Nie-Boska Komedia",
    autor: "Zygmunt Krasiński",
    epoka: "Romantyzm",
    gatunek: "Dramat romantyczny / dramat racji / historiozoficzny",
    motywy: ["rewolucja społeczna", "kryzys poezji", "walka klas", "Hrabia Henryk i Pankracy", "Opatrzność", "Galilaee vicisti"],
    synteza: "Dramat historiozoficzny ukazujący wybuch krwawej rewolucji społecznej: starcie ginącego świata arystokracji pod wodzą Hrabiego Henryka z mściwym obozem zbuntowanego ludu dowodzonym przez Pankracego, zakończone zagładą obu stron i objawieniem Chrystusa Mściciela.",
    tematyMaturalne: [
      "Obraz rewolucji społecznej – sprawiedliwość dziejowa czy zagłada cywilizacji?",
      "Dramat racji cząstkowych: Hrabia Henryk kontra Pankracy.",
      "Tragizm poezji przeklętej i fałszywego powołania artysty."
    ],
    konteksty: [
      {
        typ: "Filozoficzno-historiozoficzny",
        tytul: "Heglowska dialektyka dziejów a chrześcijańska historiozofia Opatrzności",
        opis: "Krasiński ukazuje historię jako walkę dwóch skrajnych racji cząstkowych: zdegenerowanej arystokracji broniącej tradycji i wiary (teza) oraz żądnych odwetu, zdemoralizowanych rewolucjonistów niosących zniszczenie (antyteza). Żadna ze stron nie ma racji absolutnej. Ostateczną syntezą i rozwiązaniem dziejów jest interwencja Chrystusa (Chrystianizm dziejowy).",
        funkcja: "Pozwala zrozumieć finał utworu: rewolucja jest karą za grzechy klas posiadających, lecz sama w sobie jest destrukcją, a ład może przywrócić jedynie boski sędzia."
      },
      {
        typ: "Historyczno-społeczny",
        tytul: "Rewolucje europejskie: rewolucja lipcowa we Francji (1830 r.) i bunty tkaczy lyońskich",
        opis: "Krasiński, pochodzący z arystokratycznego rodu magnackiego, z przerażeniem obserwował wrzenie rewolucyjne w Europie Zachodniej i narodziny socjalizmu utopijnego (Saint-Simon). Przewidział z niezwykłą trafnością hekatombę wojen klasowych i krwawy charakter totalitarnych rewolucji XX wieku.",
        funkcja: "Nadaje utworowi wymiar profetyczny; dowodzi, że dramat był genialnym ostrzeżeniem przed iluzją, jakoby za pomocą terroru można było zbudować szczęśliwe społeczeństwo."
      },
      {
        typ: "Literacki / Autotematyczny",
        tytul: "Dante Alighieri „Boska Komedia” – tytuł jako gorzka parafraza",
        opis: "Krasiński świadomie nawiązał tytułem do poematu Dantego. U Dantego wędrówka przez piekło prowadziła do boskiego ładu i zbawienia, u Krasińskiego dzieje ludzkie bez Boga stają się 'Nie-Boską komedią' – groteskowym, bezsensownym piekłem na ziemi, gdzie poezja oderwana od czynu moralnego staje się przekleństwem niszczącym rodzinę poety.",
        funkcja: "Stanowi klucz interpretacyjny do części rodzinnej dramatu: bezlitosna autokrytyka romantycznego kultu poezji, która zamiast zbawiać, staje się przyczyną obłędu żony i ślepoty syna Orcia."
      }
    ]
  },
  {
    id: "mickiewicz-pan-tadeusz",
    kategoria: "dodatkowy",
    kategoriaNazwa: "Lektury dodatkowe / Szkoła Podstawowa",
    tytul: "Pan Tadeusz (w tym księgi I, II, IV, X, XI, XII)",
    autor: "Adam Mickiewicz",
    epoka: "Romantyzm",
    gatunek: "Epopeja narodowa",
    motywy: ["Soplicowo jako oaza polskości", "rehabilitacja Jacka Soplicy (ks. Robak)", "zajazd szlachecki", "Koncert Jankiela", "Napoleon i nadzieja na wolność", "obyczaje szlacheckie"],
    synteza: "Narodowa epopeja przedstawiająca dworek w Soplicowie w przededniu wyprawy Napoleona na Moskwę (1811–1812), gdzie prywatny spór o zamek Horeszków przeplata się z patriotyczną misją księdza Robaka i marzeniem o zmartwychwstaniu wolnej Rzeczypospolitej.",
    tematyMaturalne: [
      "Dworek w Soplicowie jako ostoja polskiej tradycji i patriotyzmu.",
      "Przemiana Jacka Soplicy – od dumnego warchoła do pokornego emisariusza.",
      "Koncert Jankiela jako muzyczna synteza historii Polski."
    ],
    konteksty: [
      {
        typ: "Historyczny",
        tytul: "Wyprawa Napoleona na Rosję (1812 r.) i nadzieje na odrodzenie Rzeczypospolitej",
        opis: "Tło akcji stanowi wkroczenie Wielkiej Armii Napoleona na Litwę wiosną 1812 r., niosącej w szeregach polskich legionistów (Dąbrowski, Kniaziewicz) obietnicę wolności. Rok 1812 został opisany jako mityczna wiosna nadziei, urodzaju i ogólnonarodowego zjednoczenia.",
        funkcja: "Niezbędny kontekst historyczny tłumaczący entuzjazm bohaterów i wyjaśniający, dlaczego prywatne spory szlacheckie ustępują miejsca wielkiej sprawie narodowej."
      },
      {
        typ: "Biograficzno-emigracyjny",
        tytul: "Nostalgia paryska po klęsce powstania listopadowego („Epilog”)",
        opis: "Mickiewicz pisał poemat w Paryżu w latach 1832–1834, otoczony skłóconą, zgorzkniałą Wielką Emigracją. 'Pan Tadeusz' był dla poety ucieczką od paryskiego bruku w idealizowany 'kraj lat dziecinnych', który pozostał w jego pamięci 'święty i czysty jak pierwsze kochanie'.",
        funkcja: "Tłumaczy arkadyjski, pełen ciepła i humoru ton epopei: Mickiewicz stworzył mit minionej, szczęśliwej Polski, by uleczyć rozdarte serca tułaczy."
      },
      {
        typ: "Kulturowo-obyczajowy",
        tytul: "Etykieta szlachecka i kultura staropolska (grzybobranie, polowanie, polonez)",
        opis: "Soplicowo jest żywym muzeum ginącej kultury szlacheckiej. Sędzia dba o porządek precedencji przy stole, Wojski odgrywa na rogu koncert myśliwski, a finałowy polonez prowadzony przez Podkomorzego symbolizuje harmonijne pożegnanie z dawnym światem sarmackim u progu nowoczesności.",
        funkcja: "Pozwala ukazać utwór jako arcydzieło kultury pamięci: poemat ocalił dla potomności detale polskiego stroju, obyczaju i ducha gościnności."
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.LEKTURY_DATA = LEKTURY_DATA;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = LEKTURY_DATA;
}
