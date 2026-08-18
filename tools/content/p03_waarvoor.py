# -*- coding: utf-8 -*-
"""Waar AI toe in staat is, van versnellen tot een tweede brein."""


def bouw(p):
    p.tekst(
        'De verkeerde vraag en de goede',
        '<p>De meeste mensen vragen: "kan AI dit sneller doen dan ik?" Dat is de '
        'verkeerde vraag, want het antwoord is bijna altijd ja en het levert je een '
        'paar minuten op.</p>'
        '<p>De goede vraag is: <b>wat kan ik maken dat ik eerder niet maakte?</b> Niet '
        'omdat het te moeilijk was, maar omdat het te veel werk was om aan te '
        'beginnen. Het rapport waarvoor je veertig documenten had moeten doorspitten. '
        'De tool die je werk zou vereenvoudigen maar waar geen budget voor was. Het '
        'overzicht dat je al twee jaar zou moeten maken.</p>'
        '<p>Dat is de sprong die dit hoofdstuk beschrijft, en waar de rest van de '
        'cursus je heen brengt.</p>')

    p.aandacht(
        'Deze cursus is er zelf een voorbeeld van',
        '<p>De cursus die je nu volgt is met AI gemaakt, op een gewone laptop, door '
        'één persoon, in ongeveer een dag. Vijftien hoofdstukken, zo’n 95.000 tekens, '
        'twee zelfgemaakte diagrammen, eenentwintig toetsvragen, en een website die '
        'tegelijk een SCORM-pakket voor een leeromgeving is.</p>'
        '<p>Niet door "schrijf een e-learning over AI" te typen. Wel zo: de inhoud '
        'staat in losse bronbestanden per hoofdstuk, een zelfgeschreven generator '
        'bouwt daar de cursus van, en één commando zet hem online. De AI werkte '
        'daarbij rechtstreeks in de projectmap — lezen, schrijven, bouwen, '
        'controleren — terwijl de mens bepaalde wat erin moest en of het klopte.</p>'
        '<p>Alles wat daarvoor nodig was, staat in de hoofdstukken hierna. Dit is '
        'geen showcase van wat ooit kan; het is het niveau dat je aan het eind van '
        'deze cursus zelf kunt halen.</p>')

    p.tekst(
        'Vier niveaus',
        '<p>AI-gebruik groeit in stappen. Bijna iedereen blijft op niveau 1 hangen en '
        'concludeert daar dat AI "wel handig is". De sprong zit in niveau 3 en 4.</p>'
        '<p>Klap ze hieronder open. Kijk niet alleen naar wat er kan, maar ook naar de '
        'kolom <i>wat je ervoor moet kunnen</i> — dat is eerlijker dan de meeste '
        'verhalen over AI.</p>')

    p.accordeon(
        'Van versnellen naar een tweede brein',
        '<p>Elk niveau bouwt op het vorige. Het hoofdstuk waar je het leert staat '
        'erbij.</p>',
        [
            {'title': 'Niveau 1 — Versnellen: hetzelfde werk, minder tijd',
             'body': '<p>Wat iedereen als eerste doet, en waar de meeste mensen '
                     'blijven steken.</p>'
                     '<ul>'
                     '<li>Een eerste versie van een mail, offerte, verslag of '
                     'projectvoorstel</li>'
                     '<li>Een tekst omzetten naar een andere doelgroep, toon of '
                     'taal</li>'
                     '<li>Een lang document samenvatten vanuit jouw vraag</li>'
                     '<li>Jargon eruit halen, teksten op B1-niveau brengen, '
                     'alt-teksten schrijven</li>'
                     '<li>Je eigen stuk laten afbreken: "wat zijn de drie zwakste '
                     'aannames hier?"</li>'
                     '</ul>'
                     '<p><b>Wat je ervoor moet kunnen:</b> een fatsoenlijke prompt '
                     'schrijven. Meer niet.</p>'
                     '<p><b>Waar je het leert:</b> hoofdstuk 4 en 5.</p>'
                     '<p><b>Winst:</b> minuten tot uren per week.</p>'},
            {'title': 'Niveau 2 — Ontsluiten: veel bronnen tegelijk',
             'body': '<p>Hier stopt het met losse teksten en begint het met '
                     'materiaal.</p>'
                     '<ul>'
                     '<li>Veertig subsidiedocumenten of aanbestedingsstukken naast '
                     'elkaar leggen in één vergelijkingstabel, met per regel de bron '
                     'erbij</li>'
                     '<li>Twee jaar verslagen terugbrengen tot een tijdlijn van '
                     'besluiten</li>'
                     '<li>Een dataset van duizenden regels opschonen, controleren op '
                     'onmogelijke waarden en doorrekenen — met code, niet uit het '
                     'hoofd</li>'
                     '<li>Onderzoek doen met bronnen en tegenargumenten, inclusief wat '
                     'níet gevonden kon worden</li>'
                     '<li>Een chaotische stapel ideeën omzetten in een structuur waar '
                     'je verder mee kunt</li>'
                     '</ul>'
                     '<p><b>Wat je ervoor moet kunnen:</b> je materiaal op één plek '
                     'krijgen, en de uitkomst kunnen controleren.</p>'
                     '<p><b>Waar je het leert:</b> hoofdstuk 7 en 8.</p>'
                     '<p><b>Winst:</b> werk dat je anders niet was begonnen.</p>'},
            {'title': 'Niveau 3 — Maken: echte dingen opleveren',
             'body': '<p>Hier verandert het van hulpmiddel in productiemiddel. Je '
                     'levert niet langer tekst op, maar werkende dingen.</p>'
                     '<ul>'
                     '<li>Een compleet rapport in jullie huisstijl, opgebouwd uit '
                     'bronnen die je zelf aanlevert</li>'
                     '<li>Een werkende website, kennisbank of interne handleiding, '
                     'gratis online</li>'
                     '<li>Een tool die een terugkerende klus overneemt: een '
                     'offertegenerator, een rekenmodel, een dashboard boven een '
                     'spreadsheet</li>'
                     '<li>Een klikbaar prototype in plaats van een functioneel '
                     'ontwerp op papier — tien keer concreter in een gesprek met een '
                     'opdrachtgever</li>'
                     '<li>Een script dat elke maandag zelf een rapportage '
                     'samenstelt</li>'
                     '<li>Een e-learning. Zoals deze.</li>'
                     '</ul>'
                     '<p><b>Wat je ervoor moet kunnen:</b> in rondes werken, kunnen '
                     'beoordelen of iets deugt, en durven weggooien wat niet '
                     'werkt.</p>'
                     '<p><b>Waar je het leert:</b> hoofdstuk 10, 13 en 14.</p>'
                     '<p><b>Winst:</b> dingen die er anders niet waren gekomen.</p>'},
            {'title': 'Niveau 4 — Tweede brein: je hele werkgeheugen ontsloten',
             'body': '<p>Op dit niveau staat AI niet meer naast je werk maar erin. Al '
                     'je notities, verslagen, rapporten, offertes en aantekeningen '
                     'staan in een map waar de AI bij kan — en daarmee kun je je '
                     'eigen werk bevragen alsof er een collega is die alles gelezen '
                     'heeft en niets vergeet.</p>'
                     '<ul>'
                     '<li>"Wat hebben we drie jaar geleden afgesproken over dit '
                     'onderwerp, en wijkt het huidige voorstel daarvan af?"</li>'
                     '<li>"Welke van deze twaalf offertes wijkt af van ons standaard '
                     'sjabloon, en waarop?"</li>'
                     '<li>"Maak van deze map met losse notities één samenhangend '
                     'overzicht, en zeg waar ik mezelf tegenspreek."</li>'
                     '<li>Bestanden ordenen, hernoemen en opschonen — werk dat je '
                     'altijd uitstelt</li>'
                     '<li>Een opdracht geven en iets anders gaan doen: de AI werkt op '
                     'de achtergrond door en levert af</li>'
                     '</ul>'
                     '<p><b>Wat je ervoor moet kunnen:</b> je bestanden op orde '
                     'hebben, één afgebakende werkmap aanhouden, versiebeheer '
                     'gebruiken, en scherp zijn op wat je wél en niet openstelt.</p>'
                     '<p><b>Waar je het leert:</b> hoofdstuk 11, 12 en 14.</p>'
                     '<p><b>Winst:</b> je hoeft niet meer te onthouden waar iets '
                     'stond.</p>'},
        ])

    p.tekst(
        'Wat het verschil maakt tussen aardig en echt',
        '<p>Het is geen prompttruc. Mensen die op niveau 3 en 4 werken, doen vijf '
        'dingen anders — en geen daarvan gaat over slimme zinnen typen.</p>'
        '<ol>'
        '<li><b>Ze hebben hun materiaal op orde.</b> Eén map, herkenbare '
        'bestandsnamen, geen versies met "definitief-2-echt" in de titel. Rommel in '
        'is rommel uit, en dat geldt bij AI harder dan waar ook.</li>'
        '<li><b>Ze werken in rondes.</b> Structuur goedkeuren, dan pas inhoud. Kleinste '
        'werkende versie, dan pas uitbouwen. Nooit alles in één keer.</li>'
        '<li><b>Ze weten wanneer ze weggooien.</b> Als iets na drie pogingen niet '
        'goed komt, ligt het niet aan de volgende prompt. Opnieuw beginnen met wat je '
        'geleerd hebt is sneller.</li>'
        '<li><b>Ze stellen zelf de kwaliteitsnorm.</b> AI levert altijd iets dat er af '
        'uitziet. Of het goed genoeg is, bepaal jij — en dat kun je alleen als je van '
        'tevoren hebt bedacht wat "goed" betekent.</li>'
        '<li><b>Ze investeren eerst.</b> Een middag om je werkmap, je project en je '
        'instructies op te zetten. Daarna gaat alles sneller. Wie die middag '
        'overslaat, blijft op niveau 1.</li>'
        '</ol>')

    p.aandacht(
        'Vijf harde grenzen',
        '<p>Ambitieus zijn is iets anders dan roekeloos. Deze vijf blijven staan, op '
        'elk niveau.</p>'
        '<ul>'
        '<li><b>Geen beslissingen over mensen.</b> Beoordelen, selecteren of '
        'rangschikken van sollicitanten, studenten of medewerkers.</li>'
        '<li><b>Niets wat je zelf niet kunt controleren.</b> Kun je niet beoordelen of '
        'het klopt, dan heb je geen hulpmiddel maar een gok. Denk aan juridisch, '
        'medisch of fiscaal advies.</li>'
        '<li><b>Niet de laatste versie van iets belangrijks.</b> AI levert een goed '
        'concept. Wat de deur uitgaat, lees jij.</li>'
        '<li><b>Geen persoonsgegevens of vertrouwelijke informatie</b> in een omgeving '
        'zonder verwerkersovereenkomst. Hoofdstuk 6.</li>'
        '<li><b>Niet je eigen vakinhoudelijke oordeel vervangen.</b> Wie AI gebruikt '
        'om niet te hoeven nadenken, levert werk af dat daarnaar is.</li>'
        '</ul>')

    p.tekst(
        'Stappenplan: kies je eerste echte opdracht',
        '<p>Niet "waar bespaar ik tijd", maar "wat ga ik maken". Werk deze zes stappen '
        'af; onderaan vul je ze in.</p>'
        '<ol>'
        '<li><b>Kies een niveau dat één stap boven je huidige zit.</b> Doe je nu '
        'niets met AI, begin op niveau 2 — niet op 1, want daar leer je te weinig van. '
        'Werk je al met losse prompts, ga naar niveau 3.</li>'
        '<li><b>Kies een opdracht.</b> Werk je hier al langer, kies dan iets uit je '
        'eigen werk: het overzicht dat er nooit van komt, de klus die je altijd '
        'uitstelt, het ding waarvan iedereen zegt "dat zou eigenlijk moeten". Ben je '
        'net begonnen en heb je nog geen vast patroon, kies dan een opdracht uit de '
        'catalogus hieronder.</li>'
        '<li><b>Beschrijf wat er aan het eind moet liggen.</b> Een bestand, een '
        'website, een tabel, een tool. Zo concreet dat een ander kan zien of het er '
        'is. "Meer inzicht in X" is geen opdracht.</li>'
        '<li><b>Bepaal wanneer het goed genoeg is.</b> Waar zou je een collega op '
        'afrekenen? Schrijf twee of drie eisen op. Dit is straks je maatstaf én je '
        'promptinstructie.</li>'
        '<li><b>Zoek uit wat je materiaal is en waar het staat.</b> Welke bestanden, '
        'welke bronnen, welke voorbeelden van hoe het eruit moet zien. Ontbreekt dat, '
        'dan is dat je eerste taak — niet het prompten.</li>'
        '<li><b>Toets aan de vijf grenzen en zet een datum.</b> Zitten er '
        'persoonsgegevens in, pas de opdracht aan. Zet daarna een moment in je agenda '
        'waarop het af moet zijn, anders gebeurt het niet.</li>'
        '</ol>')

    p.accordeon(
        'Catalogus: twaalf opdrachten om uit te kiezen',
        '<p>Voor wie nog geen eigen patroon heeft, of wie iets zoekt dat verder gaat '
        'dan wat hij nu doet. Kies er één. Bij elke opdracht staat wat je oplevert en '
        'welk hoofdstuk je nodig hebt.</p>',
        [
            {'title': 'Niveau 2 — ontsluiten',
             'body': '<p><b>1. De vergelijkingstabel.</b> Neem tien tot veertig '
                     'documenten over hetzelfde onderwerp — regelingen, offertes, '
                     'beleidsstukken, leveranciers — en maak er één tabel van met de '
                     'punten waarop ze verschillen, met per regel de bron erbij. '
                     '<i>Oplevering: een tabel die je kunt delen. Nodig: hoofdstuk 7 '
                     'en 10.</i></p>'
                     '<p><b>2. De tijdlijn van besluiten.</b> Haal uit twee jaar '
                     'verslagen alle genomen besluiten, met datum en wie erbij was. '
                     '<i>Oplevering: een chronologisch overzicht. Nodig: hoofdstuk 7 '
                     'en 12.</i></p>'
                     '<p><b>3. De opgeschoonde dataset.</b> Neem een export waar '
                     'niemand mee wil werken, laat hem opschonen, controleren op '
                     'onmogelijke waarden en doorrekenen — met code, zodat je kunt '
                     'nakijken wat er gebeurd is. <i>Oplevering: een schoon bestand '
                     'plus een verantwoording. Nodig: hoofdstuk 4 en 10.</i></p>'},
            {'title': 'Niveau 3 — maken',
             'body': '<p><b>4. Het rapport uit je eigen bronnen.</b> Een stuk in '
                     'huisstijl, opgebouwd uit materiaal dat jij aanlevert, met een '
                     'inhoudsopgave die je eerst goedkeurt. <i>Oplevering: een '
                     'Word-document in jullie sjabloon. Nodig: hoofdstuk 7 en '
                     '10.</i></p>'
                     '<p><b>5. De handleiding als website.</b> Zet een handleiding, '
                     'kennisbank of instructie online in plaats van in een PDF die '
                     'niemand opent. <i>Oplevering: een werkende URL. Nodig: '
                     'hoofdstuk 13 en 14.</i></p>'
                     '<p><b>6. De generator.</b> Een tooltje dat uit invoervelden een '
                     'standaardstuk maakt: een offerte, een projectbrief, een '
                     'verslagsjabloon. <i>Oplevering: een werkend hulpmiddel. Nodig: '
                     'hoofdstuk 13.</i></p>'
                     '<p><b>7. Het klikbare prototype.</b> Bouw wat je anders in een '
                     'functioneel ontwerp had opgeschreven, zodat je erover kunt '
                     'praten in plaats van erover te lezen. <i>Oplevering: iets om te '
                     'laten zien. Nodig: hoofdstuk 13.</i></p>'
                     '<p><b>8. De maandagochtendrapportage.</b> Een script dat zelf '
                     'de cijfers ophaalt en er een rapportage van maakt. '
                     '<i>Oplevering: werk dat vanzelf gebeurt. Nodig: hoofdstuk 12 en '
                     '13.</i></p>'
                     '<p><b>9. De e-learning of instructiemodule.</b> Precies wat je '
                     'nu aan het volgen bent. <i>Oplevering: een cursus die je kunt '
                     'uitzetten. Nodig: hoofdstuk 10, 13 en 14.</i></p>'},
            {'title': 'Niveau 4 — tweede brein',
             'body': '<p><b>10. Je werkarchief bevraagbaar maken.</b> Zet je notities, '
                     'verslagen en documenten in één werkmap en stel er vragen aan die '
                     'je nu niemand kunt stellen. <i>Oplevering: antwoorden op vragen '
                     'die je eerder liet liggen. Nodig: hoofdstuk 12.</i></p>'
                     '<p><b>11. De grote opruiming.</b> Laat een map met honderden '
                     'bestanden ordenen, hernoemen volgens een afspraak die je zelf '
                     'kiest, en dubbelingen eruit halen. Werk op een kopie. '
                     '<i>Oplevering: een map waar je weer iets in terugvindt. Nodig: '
                     'hoofdstuk 11 en 12.</i></p>'
                     '<p><b>12. De klus die op de achtergrond loopt.</b> Geef één '
                     'afgebakende opdracht aan een agent, ga iets anders doen, en '
                     'beoordeel het resultaat als reviewer. <i>Oplevering: ervaring '
                     'met hoe ver dit gaat en waar het misgaat. Nodig: hoofdstuk '
                     '11.</i></p>'},
        ])

    p.invulvelden(
        'Oefening: leg je opdracht vast',
        '<p>Dit is de rode draad van de hele cursus. In hoofdstuk 4 schrijf je er de '
        'prompt voor, in hoofdstuk 7 leg je hem vast in een project, in hoofdstuk 8 '
        'koppel je de bronnen, en in hoofdstuk 15 kijk je terug of het gelukt is. '
        'Vul het dus echt in — je antwoorden blijven bewaard in je eigen browser.</p>',
        [
            ('p03-niveau', 'Stap 1 — Op welk niveau werk je nu, en welk niveau kies '
             'je voor deze opdracht?',
             'Bijv. nu niveau 1, opdracht op niveau 3'),
            ('p03-opdracht', 'Stap 2 — Je hoofdopdracht. Eigen werk of een nummer uit '
             'de catalogus?',
             'Beschrijf hem in twee zinnen'),
            ('p03-oplevering', 'Stap 3 — Wat ligt er als het af is?',
             'Zo concreet dat een ander kan zien of het er is'),
            ('p03-goed', 'Stap 4 — Wanneer is het goed genoeg? Noem twee of drie '
             'eisen.',
             'Waar zou je een collega op afrekenen?'),
            ('p03-materiaal', 'Stap 5 — Welk materiaal heb je nodig en waar staat '
             'het?',
             'Bestanden, bronnen, voorbeelden van hoe het eruit moet zien'),
            ('p03-ontbreekt', 'Stap 5b — Wat ontbreekt er nog, en hoe kom je eraan?',
             'Dit is meestal je eerste echte taak'),
            ('p03-grenzen', 'Stap 6 — Loop de vijf grenzen langs. Raakt je opdracht er '
             'een? Wat pas je aan?',
             'Vooral: zitten er persoonsgegevens in?'),
            ('p03-datum', 'Stap 6b — Wanneer moet het af zijn?',
             'Zet dezelfde datum in je agenda'),
            ('p03-tweede', 'Reserve: welke tweede, kleinere opdracht doe je als deze '
             'vastloopt?',
             'Iets van één niveau lager'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Kopieer je opdracht naar je eigen aantekeningen en zet de datum uit stap 6 '
        'nu meteen in je agenda. Een opdracht zonder datum is een voornemen.</p>')

    p.vraag(
        'Even checken',
        'Iemand wil "beter worden in AI" en besluit om voortaan zijn mails te laten '
        'herschrijven. Wat is het probleem met die aanpak?',
        [
            ('Hij blijft op het niveau van versnellen hangen, waar de winst klein is '
             'en je weinig leert — de sprong zit in het maken van dingen die er '
             'anders niet waren gekomen.', True),
            ('Mails herschrijven met AI mag niet vanwege de AVG.', False),
            ('Hij zou eerst moeten leren programmeren.', False),
            ('Er is geen probleem; zo hoort iedereen te beginnen.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Niveau 1 is prima om mee kennis te maken, maar wie '
                       'daar blijft, concludeert na een maand dat AI "wel handig is" en '
                       'stopt. Kies een opdracht die één niveau hoger ligt dan waar je '
                       'nu zit.</p>',
            '_incorrect': {'final': '<p>Nog niet. Er is niets mis met mails '
                                    'herschrijven, en programmeren hoeft niet. Het punt '
                                    'is de ambitie: van hetzelfde werk sneller doen, '
                                    'naar werk opleveren dat er anders niet was '
                                    'gekomen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
