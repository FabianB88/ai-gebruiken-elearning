# -*- coding: utf-8 -*-
"""Kennischeck over de hele cursus, plus je eigen AI-werkplan."""

TOETS = 'kennischeck-ai'
DREMPEL = 75


def bouw(p):
    p.tekst(
        'Kennischeck',
        '<p>Zeven vragen over de hele cursus. Het zijn geen definitievragen: bij elke '
        'vraag staat een situatie waarin je moet kiezen wat je doet.</p>'
        '<p>Je hebt %d%% nodig om te slagen en je mag het zo vaak proberen als je '
        'wilt. Je uitslag verschijnt onderaan zodra je alle vragen hebt '
        'ingestuurd.</p>' % DREMPEL)

    p.vraag(
        'Vraag 1 — prompten',
        'Een collega stuurt deze prompt en klaagt dat het antwoord te algemeen is: '
        '"Je bent een communicatieadviseur. Schrijf een wervende tekst van 200 woorden '
        'voor onze nieuwsbrief, in de je-vorm, zonder opsommingstekens." Welke '
        'bouwsteen ontbreekt het duidelijkst?',
        [
            ('Context — er staat niets over de organisatie, het onderwerp, de '
             'doelgroep of de bron.', True),
            ('De rol — "communicatieadviseur" is te breed.', False),
            ('De outputvorm — er zou een structuur bij moeten.', False),
            ('De taak — "schrijf" is niet specifiek genoeg.', False),
        ],
        feedback={
            'title': 'Vraag 1',
            'correct': '<p>Klopt. Rol, taak en vorm staan er allemaal keurig in. Wat '
                       'ontbreekt is waar het over gaat en voor wie — en dat is precies '
                       'waarom het antwoord voor elke organisatie had kunnen '
                       'gelden.</p>',
            '_incorrect': {'final': '<p>Nog niet. Kijk welke bouwstenen er wél staan: '
                                    'rol, taak, lengte, toon, vorm. De ontbrekende is '
                                    'de inhoudelijke situatie — de context.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.koppelvraag(
        'Vraag 2 — het juiste gereedschap',
        'Koppel elke situatie aan de aanpak die daar het beste bij past.',
        rijen=[
            ('Je typt bij elke opdracht dezelfde uitleg over je organisatie en '
             'doelgroep', 'Een project met vaste instructies'),
            ('Je wilt vragen kunnen stellen over je documenten in Google Drive',
             'Een connector'),
            ('Je wilt een map met eigen bestanden laten opschonen en hernoemen',
             'De desktop-app met maptoegang'),
            ('Je moet bij een document op de SharePoint van de HAN, waarvoor geen '
             'koppeling bestaat', 'Je ingelogde browsersessie'),
        ],
        opties=['Een project met vaste instructies', 'Een connector',
                'De desktop-app met maptoegang', 'Je ingelogde browsersessie'],
        feedback={
            'title': 'Vraag 2',
            'correct': '<p>Goed. Herhaalde context wijst naar een project, doorzoeken '
                       'van een koppelbaar systeem naar een connector, werken ín '
                       'bestanden naar de desktop-app, en een geblokkeerd systeem naar '
                       'je eigen ingelogde browsersessie.</p>',
            '_incorrect': {'final': '<p>Nog niet. Vraag je per situatie af waar het '
                                    'werk zich afspeelt: in je instructies, in een '
                                    'koppelbaar systeem, in bestanden op je schijf, of '
                                    'in een browserscherm waar je zelf al bent '
                                    'ingelogd.</p>'},
            '_partlyCorrect': {'final': '<p>Deels goed. Kijk nog eens naar de regels '
                                        'die je fout had.</p>'}
        })

    p.vraag(
        'Vraag 3 — privacy',
        'Je wilt AI laten helpen bij het verwerken van evaluatieformulieren van een '
        'cursus, ingevuld door deelnemers met naam erbij. Wat is de juiste aanpak?',
        [
            ('Namen en herleidbare details eerst verwijderen, en werken in een '
             'zakelijke omgeving met verwerkersovereenkomst.', True),
            ('De formulieren als PDF uploaden; in een bestand vallen ze minder op dan '
             'in een prompt.', False),
            ('Het gewoon doen, want het gaat over een cursus en niet over '
             'gevoelige zaken.', False),
            ('Alleen de formulieren met negatieve feedback anonimiseren.', False),
        ],
        feedback={
            'title': 'Vraag 3',
            'correct': '<p>Klopt. Beide lagen: eerst anonimiseren, en dan pas in een '
                       'omgeving waarin de verwerking geregeld is.</p>',
            '_incorrect': {'final': '<p>Nog niet. Een PDF is net zo goed invoer als '
                                    'geplakte tekst. En of de inhoud gevoelig voelt, '
                                    'doet niet ter zake: een naam is een '
                                    'persoonsgegeven.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 4 — documenten',
        'Je maakt een adviesrapport dat in jullie huisstijl moet en waar nog flink aan '
        'geschaafd gaat worden. Wat is de snelste werkwijze?',
        [
            ('De inhoud in Markdown laten opleveren, in de chat afwerken, en pas aan '
             'het eind in je eigen Word-sjabloon plakken.', True),
            ('Meteen om een Word-bestand vragen, zodat de opmaak vanaf het begin '
             'klopt.', False),
            ('Per hoofdstuk een apart Word-bestand laten maken en die achteraf '
             'samenvoegen.', False),
            ('Om een PDF vragen zodat de opmaak vastligt.', False),
        ],
        feedback={
            'title': 'Vraag 4',
            'correct': '<p>Goed. Zolang de inhoud beweegt, wil je geen bestand: elke '
                       'wijziging zou een complete herbouw kosten. En je eigen '
                       'sjabloon geeft je de huisstijl die een AI-bestand niet '
                       'heeft.</p>',
            '_incorrect': {'final': '<p>Nog niet. Het punt is timing: een bestand is de '
                                    'laatste stap, niet de eerste — anders betaal je '
                                    'elke tekstwijziging met wachttijd én raak je de '
                                    'huisstijl kwijt.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 5 — zelfstandig werkende AI',
        'Je wilt een AI-agent op de achtergrond laten doorwerken zonder dat hij steeds '
        'om toestemming vraagt. Wat regel je eerst?',
        [
            ('Vaste grenzen in het geheugen of de instructies, inclusief de opdracht '
             'om bij een grens te stoppen in plaats van een omweg te zoeken.', True),
            ('Een sneller model, zodat het minder lang duurt.', False),
            ('Een tweede scherm om mee te kijken tijdens het werk.', False),
            ('Een uitgebreidere prompt met meer voorbeelden.', False),
        ],
        feedback={
            'title': 'Vraag 5',
            'correct': '<p>Precies. Zonder tussenvragen is er onderweg niemand die nee '
                       'zegt, dus de grenzen moeten er vooraf in staan — en de regel '
                       'om te stoppen in plaats van eromheen te werken is daarbij de '
                       'belangrijkste.</p>',
            '_incorrect': {'final': '<p>Nog niet. Meekijken maakt het voordeel van '
                                    'achtergrondwerk ongedaan, en snelheid verandert '
                                    'niets aan wat er mis kan gaan. De grenzen horen '
                                    'vooraf vast te liggen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.vraag(
        'Vraag 6 — zelf bouwen',
        'Je hebt met AI een aanmeldformulier gebouwd op Firebase. Welke twee dingen '
        'moeten geregeld zijn voordat je het live zet? Kies er twee.',
        [
            ('De database staat in productiemodus met beveiligingsregels die vastleggen '
             'wie wat mag.', True),
            ('Sleutels en wachtwoorden staan buiten de repository, in een bestand dat '
             'niet meegaat in versiebeheer.', True),
            ('De code is zo kort mogelijk gehouden.', False),
            ('Het formulier is getest in minstens drie browsers.', False),
        ],
        meerkeuze=True,
        feedback={
            'title': 'Vraag 6',
            'correct': '<p>Goed. Dit zijn de twee manieren waarop zelfgebouwde '
                       'toepassingen in de praktijk gegevens lekken: een open database '
                       'en sleutels in de code.</p>',
            '_incorrect': {'final': '<p>Nog niet. Browsertests en korte code zijn nette '
                                    'gewoontes, maar ze voorkomen geen datalek. De open '
                                    'testmodus en meegecommitte sleutels wel.</p>'},
            '_partlyCorrect': {'final': '<p>Eén van de twee. Denk aan de twee klassieke '
                                        'lekken: een database die openstaat, en '
                                        'sleutels die in versiebeheer belanden.</p>'}
        })

    p.vraag(
        'Vraag 7 — browser-agents',
        'Wat maakt prompt-injectie zo lastig te voorkomen bij een AI die je browser '
        'bedient?',
        [
            ('De agent handelt in al je ingelogde sessies tegelijk, dus een instructie '
             'op een onbelangrijke pagina kan worden uitgevoerd in je mail of andere '
             'systemen.', True),
            ('De agent onthoudt te veel van eerdere gesprekken.', False),
            ('Browsers versleutelen de inhoud van pagina’s, waardoor de agent er niet '
             'goed bij kan.', False),
            ('Het is alleen een probleem bij gratis accounts.', False),
        ],
        feedback={
            'title': 'Vraag 7',
            'correct': '<p>Precies. Het is een bouwkundig probleem, geen fout die je '
                       'even patcht: de scheiding tussen websites die je browser '
                       'normaal bewaakt, doorbreekt een agent per definitie. Vandaar '
                       'de regels: per taak aanzetten, apart profiel, en zelf '
                       'bevestigen wat onomkeerbaar is.</p>',
            '_incorrect': {'final': '<p>Nog niet. Het gaat niet om geheugen of om je '
                                    'abonnement, maar erom dat één agent tegelijk in '
                                    'al je ingelogde omgevingen kan handelen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })

    p.tekst(
        'Je AI-werkplan',
        '<p>Tot slot: zet op één plek wat je met deze cursus gaat doen. Kijk terug '
        'naar wat je in de eerdere hoofdstukken hebt ingevuld en maak er concrete '
        'afspraken met jezelf van.</p>')

    p.invulvelden(
        'Wat ga je vanaf morgen doen?',
        '<p>Vul dit in en kopieer het naar je eigen aantekeningen of je agenda. Een '
        'plan dat alleen in deze browser staat, is geen plan.</p>',
        [
            ('p15-taak1', 'Welke terugkerende taak ga je als eerste met AI aanpakken?',
             'Uit je lijst van hoofdstuk 3'),
            ('p15-hoe', 'Hoe ga je dat inrichten: los gesprek, project, custom GPT of '
             'desktop?',
             'En waarom die keuze?'),
            ('p15-week', 'Wat doe je deze week? Noem één concrete stap.',
             'Bijv. het project aanmaken en drie bronbestanden toevoegen'),
            ('p15-maand', 'Wat doe je deze maand?',
             'Bijv. de werkmap opzetten en één tool bouwen'),
            ('p15-grens', 'Welke drie grenzen leg je vast — voor jezelf en in het '
             'geheugen van je AI?',
             'Denk aan persoonsgegevens, aankopen, versturen namens jou'),
            ('p15-deel', 'Met wie ga je dit delen, en wat spreek je samen af?',
             'Afspraken die je alleen maakt, gelden alleen voor jou'),
            ('p15-check', 'Wanneer kijk je terug of het gewerkt heeft?',
             'Zet een datum in je agenda'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Kopieer je werkplan en zet de terugkijkdatum meteen in je agenda.</p>')


def uitslag(p):
    p.uitslag(
        TOETS, drempel=DREMPEL,
        voldoende='Voldoende. Je hebt de stof te pakken. Ga nu terug naar je '
                  'werkplan hierboven en zet de eerste stap in je agenda — dat is '
                  'wat het verschil maakt.',
        onvoldoende='Dat is nog niet voldoende. Loop de hoofdstukken van de vragen '
                    'die je fout had nog eens door en probeer het daarna opnieuw. Je '
                    'mag het zo vaak proberen als je wilt.')
