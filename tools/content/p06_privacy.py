# -*- coding: utf-8 -*-
"""Privacy, AVG en vertrouwelijkheid: de harde grenzen."""


def bouw(p):
    p.tekst(
        'Eén regel om te onthouden',
        '<p><b>Zet nooit persoonsgegevens of vertrouwelijke informatie in een '
        'AI-gesprek.</b> Niet in een prompt, niet in een bijlage, niet in een '
        'screenshot, niet "even snel om te kijken of het werkt".</p>'
        '<p>Bij ons is die regel absoluut, en dat komt door hoe we werken: iedereen '
        'gebruikt AI <b>op persoonlijke titel</b>, met een eigen Claude Pro of ChatGPT '
        'Plus. Daar hoort geen verwerkersovereenkomst bij. En zonder '
        'verwerkersovereenkomst kun je een verwerking van persoonsgegevens niet '
        'verantwoorden — er is geen afspraak over waar de gegevens heen gaan, wie '
        'erbij kan en hoe lang ze blijven staan.</p>'
        '<p>Er is dus geen "ja, maar in dit geval mag het wel". Dit hoofdstuk gaat '
        'over hoe je binnen die grens tóch bijna alles kunt doen — plus twee '
        'instellingen die je vandaag nog goedzet.</p>')

    p.tekst(
        'Wat telt als persoonsgegeven — ruimer dan je denkt',
        '<p>Een persoonsgegeven is elk gegeven waarmee je een persoon direct of '
        'indirect kunt herleiden. Dat is veel meer dan een naam:</p>'
        '<ul>'
        '<li>Namen, e-mailadressen, telefoonnummers, adressen</li>'
        '<li>Personeelsnummers, studentnummers, klantnummers, dossiernummers</li>'
        '<li>IP-adressen en apparaat-id’s</li>'
        '<li>Foto’s en video’s waarop mensen herkenbaar zijn</li>'
        '<li><b>Vrije tekst óver mensen</b> — een gespreksverslag, een klacht, een '
        'beoordeling, een verzuimmelding. Dit is de categorie die het vaakst '
        'ongemerkt in een prompt belandt.</li>'
        '<li><b>Werk van studenten of cursisten</b> — dat is hun werk, hun '
        'auteursrecht, en vaak herleidbaar tot hen.</li>'
        '<li>Combinaties die op zichzelf onschuldig lijken: "de teamleider inkoop van '
        'onze vestiging in Arnhem" is één persoon.</li>'
        '</ul>')

    p.aandacht(
        'Bijzondere persoonsgegevens: nooit, in geen enkele vorm',
        '<p>Gezondheid, ras of etnische afkomst, politieke opvattingen, geloof, '
        'vakbondslidmaatschap, seksuele geaardheid, biometrie, strafrechtelijke '
        'gegevens. Deze categorie is extra beschermd en hoort onder geen enkele '
        'omstandigheid in een AI-gesprek — ook niet "geanonimiseerd".</p>')

    p.tekst(
        'Log in met je eigen privé-account, nooit met je werkaccount',
        '<p>Dit is bij ons de afspraak: je maakt je AI-account aan op je persoonlijke '
        'mailadres, en je logt nooit in met je werkmail of via "inloggen met '
        'Microsoft/Google" van je werkomgeving.</p>'
        '<p>Waarom dat uitmaakt:</p>'
        '<ul>'
        '<li><b>Je koppelt de organisatie niet aan een dienst waarover niets is '
        'afgesproken.</b> Een account op werkmail suggereert dat het gebruik namens '
        'de organisatie gebeurt, terwijl er geen contract, geen '
        'verwerkersovereenkomst en geen beheer achter zit.</li>'
        '<li><b>Inloggen met je werkaccount opent deuren die je niet wilt '
        'openzetten.</b> Bij "inloggen met Microsoft" kan een dienst toestemming '
        'vragen voor je agenda, je bestanden of je contacten. Op een privé-account kan '
        'dat niet per ongeluk.</li>'
        '<li><b>Het houdt de grens scherp.</b> Werk je bewust op persoonlijke titel, '
        'dan blijf je je ervan bewust dat er geen bedrijfsgegevens in horen. Dat is '
        'precies het gedrag dat we willen.</li>'
        '</ul>'
        '<p>Gebruik je Claude of ChatGPT al met je werkmail? Maak dan een nieuw '
        'account aan op je privémailadres en ga daar verder. Loop je oude '
        'gespreksgeschiedenis na en verwijder wat er niet in hoort.</p>')

    p.tekst(
        'Zet modeltraining uit — dit is de belangrijkste instelling die er is',
        '<p>Op een persoonlijk account worden je gesprekken standaard gebruikt om '
        'modellen te verbeteren. Bij Claude staat dat sinds oktober 2025 '
        '<b>standaard aan</b> voor Free-, Pro- en Max-accounts. Je moet het dus zelf '
        'uitzetten; er gebeurt niets als je niets doet.</p>'
        '<p>Er hangt meer aan vast dan alleen training. Bij Claude bepaalt deze knop '
        'ook hoe lang je gegevens bewaard blijven: staat training <b>aan</b>, dan mag '
        'Anthropic je gesprekken in geanonimiseerde vorm tot vijf jaar bewaren. Zet je '
        'hem <b>uit</b>, dan val je terug op de standaard bewaartermijn van dertig '
        'dagen. Dat is een verschil van jaren, met één klik.</p>')

    p.accordeon(
        'Letterlijk: zo zet je het uit',
        '<p>Doe dit nu, het kost per platform een halve minuut. Klap open wat je '
        'gebruikt.</p>',
        [
            {'title': 'Claude (Pro, Max of Free)',
             'body': '<ol>'
                     '<li>Ga naar <b>claude.ai</b> en log in.</li>'
                     '<li>Klik <b>linksonder op je naam of initialen</b>.</li>'
                     '<li>Kies <b>Settings</b> (Instellingen).</li>'
                     '<li>Ga naar <b>Privacy</b> — bij sommige versies heet dit '
                     '<i>Privacy Settings</i>.</li>'
                     '<li>Zoek de schakelaar <b>"Help improve Claude"</b> (Help Claude '
                     'verbeteren) en zet hem <b>uit</b>.</li>'
                     '<li>Controleer dat de schakelaar daadwerkelijk grijs of uit '
                     'staat en ververs de pagina om zeker te weten dat het bewaard '
                     'is.</li>'
                     '</ol>'
                     '<p><b>Wat het wel doet:</b> nieuwe gesprekken en codesessies '
                     'worden niet meer gebruikt voor toekomstige training, en je '
                     'bewaartermijn gaat terug naar dertig dagen.</p>'
                     '<p><b>Wat het niet doet:</b> gesprekken die al in een lopende '
                     'training zijn meegenomen, haal je er niet meer uit. En als een '
                     'veiligheidsfilter een gesprek markeert, kan het alsnog gebruikt '
                     'worden voor veiligheidsonderzoek. Uitzetten is dus belangrijk, '
                     'maar het is geen wisser met terugwerkende kracht — en het is '
                     'geen vervanging voor de regel bovenaan dit hoofdstuk.</p>'},
            {'title': 'ChatGPT (Plus, Pro, Go of Free)',
             'body': '<ol>'
                     '<li>Ga naar <b>chatgpt.com</b> en log in.</li>'
                     '<li>Klik <b>rechtsboven of linksonder op je profiel</b> en kies '
                     '<b>Instellingen</b>.</li>'
                     '<li>Ga naar <b>Gegevensbeheer</b> (Data controls).</li>'
                     '<li>Zet <b>"Het model voor iedereen verbeteren"</b> (Improve the '
                     'model for everyone) <b>uit</b>.</li>'
                     '<li>Kijk meteen ook naar de andere schakelaars in dit scherm, '
                     'zoals het bewaren van gespreksgeschiedenis, en zet die naar je '
                     'hand.</li>'
                     '</ol>'
                     '<p><b>Let op:</b> deze instelling zit per account. Gebruik je '
                     'ChatGPT ook op je telefoon of in een andere browser, dan is dat '
                     'hetzelfde account en hoef je het maar één keer te doen — maar '
                     'controleer het wel even.</p>'},
            {'title': 'Tijdelijke gesprekken: de snelste noodrem',
             'body': '<p>Beide platforms hebben een modus voor gesprekken die niet '
                     'bewaard worden en niet in je geschiedenis komen — bij ChatGPT '
                     'heet dat een <i>tijdelijke chat</i>, bij Claude vind je een '
                     'vergelijkbare optie bij het starten van een gesprek.</p>'
                     '<p>Handig als je iets eenmaligs vraagt dat je niet in je '
                     'geschiedenis wilt hebben. Maar let op: het is een '
                     'opslag-instelling, geen beschermingsmuur. Wat je erin typt, gaat '
                     'nog steeds naar de servers. Het is geen excuus om er alsnog '
                     'persoonsgegevens in te zetten.</p>'},
        ])

    p.tekst(
        'Stappenplan: je account in orde maken',
        '<p>Doe dit vandaag, het kost tien minuten en het is klaar voor de rest van '
        'het jaar.</p>'
        '<ol>'
        '<li><b>Controleer met welk account je bent ingelogd.</b> Staat er een '
        'werkmailadres of een organisatienaam? Dan maak je een nieuw account aan op '
        'je privémailadres.</li>'
        '<li><b>Zet modeltraining uit</b> volgens de stappen hierboven, bij elk '
        'platform dat je gebruikt.</li>'
        '<li><b>Loop je gespreksgeschiedenis na.</b> Staat er iets in dat er niet had '
        'moeten staan — namen, klantgegevens, een geüpload dossier — verwijder het '
        'gesprek en meld het volgens de procedure van je organisatie.</li>'
        '<li><b>Controleer je gekoppelde apps.</b> Heb je ooit "inloggen met Google" '
        'of "inloggen met Microsoft" gebruikt, trek die toestemming dan in bij je '
        'Google- of Microsoft-account.</li>'
        '<li><b>Kijk of het geheugen aan staat</b> en wat erin is opgeslagen. In '
        'hoofdstuk 11 zet je daar bewust regels in; ruim nu eerst op wat er niet '
        'hoort.</li>'
        '<li><b>Zet een herinnering over zes maanden</b> om dit opnieuw te doen. '
        'Instellingen veranderen, en standaardwaarden gaan bijna altijd de kant op '
        'van méér delen, niet minder.</li>'
        '</ol>')

    p.tekst(
        'Wat wél kan: anonimiseren aan de voorkant',
        '<p>Je hoeft de meeste taken niet te laten schieten. Je haalt de personen '
        'eruit vóórdat de tekst het gesprek in gaat.</p>'
        '<ol>'
        '<li><b>Vervang namen door rollen.</b> "Mark van inkoop" wordt "de '
        'inkoper". Je verliest niets aan bruikbaarheid van het antwoord.</li>'
        '<li><b>Vervang organisaties door typeringen</b> als de naam er niet toe doet: '
        '"een gemeente van middelgrote omvang".</li>'
        '<li><b>Haal alle nummers weg</b> die naar een persoon of dossier '
        'verwijzen.</li>'
        '<li><b>Vraag jezelf af: staat hier nog iets in waarmee ik zou kunnen '
        'achterhalen om wie het gaat?</b> Zo ja, is het nog niet anoniem.</li>'
        '<li><b>Werk met een sjabloon in plaats van met een geval.</b> Vraag niet '
        '"schrijf een reactie op deze klacht", maar "schrijf een sjabloon voor een '
        'reactie op een klacht over levertijd, met velden die ik zelf invul". Nog '
        'beter, want je hergebruikt het.</li>'
        '</ol>')

    p.accordeon(
        'Ook vertrouwelijk, ook niet plakken',
        '<p>Naast persoonsgegevens is er een tweede categorie die om dezelfde reden '
        'buiten het gesprek blijft.</p>',
        [
            {'title': 'Bedrijfsgevoelige informatie',
             'body': '<p>Niet-gepubliceerde cijfers, offertes van concurrenten, '
                     'inkoopprijzen, strategiestukken, informatie onder een '
                     'geheimhoudingsverklaring. Een lek hoeft niet illegaal te zijn om '
                     'schadelijk te zijn.</p>'},
            {'title': 'Broncode en systeeminformatie van klanten',
             'body': '<p>Code van een opdrachtgever valt vaak onder een contract dat '
                     'je verbiedt hem aan derden te tonen. Een AI-dienst is een '
                     'derde.</p>'},
            {'title': 'Inloggegevens en sleutels',
             'body': '<p>Wachtwoorden, API-sleutels, tokens, certificaten. Ook niet '
                     '"tijdelijk om iets te testen" — wat je in een gesprek plakt, '
                     'staat in een logbestand.</p>'},
            {'title': 'Werk van studenten en cursisten',
             'body': '<p>Ingeleverd werk is niet van jou. Wil je AI gebruiken bij '
                     'nakijken, maak dan eerst een beoordelingsmodel met AI en pas dat '
                     'zelf toe — dan gaat er geen studentwerk het model in.</p>'},
        ])

    p.tekst(
        'AI-geletterdheid is inmiddels een verplichting',
        '<p>De Europese AI-verordening verplicht organisaties om ervoor te zorgen dat '
        'medewerkers die met AI werken, voldoende weten waar ze mee bezig zijn — wat '
        'het systeem doet, wat de beperkingen zijn en welke risico’s eraan zitten. '
        'Deze cursus is daar een invulling van; leg vast dat je hem gevolgd hebt.</p>'
        '<p>Daarnaast geldt: wees transparant. Als AI een substantiële bijdrage heeft '
        'geleverd aan iets wat je oplevert, zeg dat. Niet omdat het moet klinken als '
        'een disclaimer, maar omdat je collega’s en opdrachtgevers dan weten waar ze '
        'op moeten letten.</p>')

    p.invulvelden(
        'Oefening: instellingen goedzetten en een casus veilig maken',
        '<p>Eerst je account, dan de casus. Iemand wil dit vragen aan ChatGPT:</p>'
        '<blockquote><p><i>"Hierbij het verslag van het gesprek met Karin de Vries '
        '(personeelsnummer 44821) over haar verzuim. Ze geeft aan dat het te maken '
        'heeft met haar rugklachten en de spanning thuis. Kun je hier een '
        'verslaglegging van maken voor het dossier en adviseren over '
        'vervolgstappen?"</i></p></blockquote>',
        [
            ('p06-account', 'Met welk account werk je, en heb je het aangepast?',
             'Privémailadres, of nog werkmail?'),
            ('p06-training', 'Heb je modeltraining uitgezet? Bij welke platforms, en '
             'waar stond de knop precies?',
             'Schrijf het pad op, dan vind je het volgende keer terug'),
            ('p06-opgeruimd', 'Wat kwam je tegen bij het nalopen van je '
             'gespreksgeschiedenis?',
             'Eerlijk antwoord; het blijft in je eigen browser'),
            ('p06-fouten', 'Welke problemen zitten er in de casus hierboven? Noem ze '
             'allemaal.',
             'Denk aan: welke categorieën gegevens staan hier in?'),
            ('p06-hard', 'Welk deel mag onder geen enkele omstandigheid, ook niet '
             'geanonimiseerd? Waarom?',
             'Er zit een categorie in die extra beschermd is'),
            ('p06-alternatief', 'Hoe zou jij deze taak wél met AI aanpakken?',
             'Denk aan sjablonen in plaats van gevallen'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Bespreek je antwoorden met een collega. Privacyafspraken werken alleen als '
        'ze gedeeld zijn.</p>')

    p.vraag(
        'Even checken',
        'Je hebt bij Claude de instelling "Help improve Claude" uitgezet. Wat betekent '
        'dat wel en niet?',
        [
            ('Nieuwe gesprekken worden niet meer voor training gebruikt en je '
             'bewaartermijn gaat terug naar dertig dagen — maar het is geen '
             'verwerkersovereenkomst, dus persoonsgegevens blijven verboden.', True),
            ('Je gegevens blijven nu volledig op je eigen computer.', False),
            ('Alles wat je eerder hebt getypt, wordt met terugwerkende kracht uit de '
             'modellen verwijderd.', False),
            ('Je mag nu wel klantgegevens gebruiken, want er wordt niets meer mee '
             'gedaan.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Het is een belangrijke instelling — vooral vanwege '
                       'die bewaartermijn van dertig dagen in plaats van jaren — maar '
                       'het verandert niets aan de grondslag. Zonder '
                       'verwerkersovereenkomst blijft de regel over persoonsgegevens '
                       'absoluut.</p>',
            '_incorrect': {'final': '<p>Nog niet. De knop regelt twee dingen: geen '
                                    'nieuwe training, en een kortere bewaartermijn. Wat '
                                    'al gebruikt is, komt er niet meer uit, je gegevens '
                                    'gaan nog steeds naar de servers, en de AVG-grens '
                                    'schuift er niet door op.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
