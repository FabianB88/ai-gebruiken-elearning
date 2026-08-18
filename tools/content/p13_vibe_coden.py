# -*- coding: utf-8 -*-
"""Vibe coden: zelf software maken zonder programmeur te zijn."""


def bouw(p):
    p.tekst(
        'Beschrijven in plaats van programmeren',
        '<p><b>Vibe coden</b> is de term voor software maken door te beschrijven wat '
        'je wil, de AI de code te laten schrijven, en het resultaat te beoordelen op '
        'of het doet wat je bedoelde — niet op hoe de code eruitziet. Je stuurt op '
        'gedrag, niet op regels code.</p>'
        '<p>Voor mensen die niet kunnen programmeren, is dit de grootste verandering '
        'in deze hele cursus. Dingen waar je vroeger een offerte voor moest vragen — '
        'een intern dashboard, een rekenmodel, een aanmeldformulier, een script dat '
        'elke maandag een rapport maakt — kun je nu in een middag zelf bouwen.</p>'
        '<p>En het is tegelijk het gebied waar het het makkelijkst grondig misgaat. '
        'Dit hoofdstuk gaat over allebei.</p>')

    p.accordeon(
        'Wat je er realistisch mee maakt',
        '<p>Vier categorieën die goed werken, en wat er in elke categorie misgaat.</p>',
        [
            {'title': 'Scripts die werk automatiseren',
             'body': '<p>Bestanden hernoemen, gegevens uit een reeks documenten '
                     'halen, een maandelijkse rapportage samenstellen, een export '
                     'omzetten naar een ander formaat.</p>'
                     '<p>Dit is de dankbaarste categorie: kleine omvang, duidelijk of '
                     'het werkt, en het draait op jouw machine.</p>'},
            {'title': 'Interne hulpmiddelen',
             'body': '<p>Een rekentool, een checklist-app, een dashboard dat een '
                     'spreadsheet leesbaar maakt, een generator die uit invoervelden '
                     'een standaardbrief maakt.</p>'
                     '<p>Let op de grens: zodra collega’s hun eigen gegevens gaan '
                     'invoeren, wordt het een systeem met verantwoordelijkheden.</p>'},
            {'title': 'Websites en pagina’s',
             'body': '<p>Een projectpagina, een landingspagina, een interactieve '
                     'uitleg. Prima te doen, en je kunt het gratis publiceren via '
                     'GitHub Pages — hoofdstuk 14.</p>'},
            {'title': 'Prototypes om iets uit te leggen',
             'body': '<p>Misschien wel de sterkste toepassing: in plaats van een '
                     'document schrijven over hoe iets zou moeten werken, bouw je in '
                     'twee uur een klikbaar model. Dat maakt een gesprek met een '
                     'opdrachtgever tien keer concreter.</p>'},
        ])

    p.aandacht(
        'Wat je zo niet bouwt',
        '<p>Zonder iemand die de code echt kan lezen, blijf je weg bij:</p>'
        '<ul>'
        '<li><b>Alles met persoonsgegevens.</b> Een aanmeldformulier dat namen en '
        'e-mailadressen opslaat, is een verwerking onder de AVG met alles wat daarbij '
        'hoort.</li>'
        '<li><b>Inloggen en accounts.</b> Authenticatie zelf bouwen gaat mis, ook voor '
        'ervaren programmeurs. Gebruik een bestaande dienst.</li>'
        '<li><b>Betalingen.</b> Nooit zelf, in geen enkele vorm.</li>'
        '<li><b>Iets waar de organisatie van afhangt.</b> Als het stukgaan van jouw '
        'tooltje het werk van twintig mensen stillegt, is het geen tooltje meer.</li>'
        '<li><b>Wijzigingen in bestaande systemen.</b> Een AI die "even" iets aanpast '
        'in een draaiend systeem, kan meer kapotmaken dan je kunt overzien.</li>'
        '</ul>')

    p.tekst(
        'Stappenplan: van idee naar werkend prototype',
        '<ol>'
        '<li><b>Schrijf eerst op wat het moet doen, in gewone taal.</b> Wie gebruikt '
        'het, wat stopt die erin, wat komt eruit. Vijf zinnen is genoeg, maar '
        'schrijf ze op.</li>'
        '<li><b>Benoem wat het nadrukkelijk niet hoeft te doen.</b> Dit is de '
        'belangrijkste stap en iedereen slaat hem over. Zonder deze grens bouwt de AI '
        'er van alles bij.</li>'
        '<li><b>Kies je gereedschap.</b> Iets kleins en visueels: laat het maken in '
        'een artifact bij Claude of een canvas bij ChatGPT — dan zie je het meteen '
        'draaien. Iets met meerdere bestanden: gebruik Claude Code of Codex in een '
        'projectmap (hoofdstuk 14).</li>'
        '<li><b>Vraag eerst om een plan, niet om code.</b> <i>"Beschrijf hoe je dit '
        'zou aanpakken, welke onderdelen er zijn en welke keuzes je maakt. Schrijf nog '
        'geen code."</i> Klopt het plan niet, dan klopt de code ook niet.</li>'
        '<li><b>Laat de kleinste werkende versie bouwen.</b> Eén functie, één scherm. '
        'Nog geen opmaak, nog geen extra’s.</li>'
        '<li><b>Test hem zelf, meteen.</b> Werkt het? Dan pas verder. Werkt het niet, '
        'plak de foutmelding letterlijk terug — niet "hij doet het niet".</li>'
        '<li><b>Bouw uit in kleine stappen</b> en test na elke stap. Vijf dingen '
        'tegelijk vragen levert vijf half werkende dingen op.</li>'
        '<li><b>Probeer het stuk te maken.</b> Voer lege waarden in, rare tekens, een '
        'veel te groot bestand, een negatief getal. Wat je zelf niet stuk krijgt, '
        'krijgt een collega wel stuk.</li>'
        '<li><b>Laat de AI zijn eigen werk beoordelen.</b> <i>"Bekijk deze code '
        'kritisch. Waar zitten fouten, wat gaat er mis bij onverwachte invoer, en wat '
        'is een beveiligingsrisico?"</i> Doe dat in een nieuw gesprek — anders '
        'verdedigt hij zijn eigen keuzes.</li>'
        '<li><b>Laat het uitleggen in gewone taal.</b> <i>"Leg uit wat elk bestand '
        'doet, alsof ik geen programmeur ben."</i> Snap je het niet, dan kun je het '
        'ook niet onderhouden.</li>'
        '</ol>')

    p.tekst(
        'Wel doen',
        '<ul>'
        '<li><b>Versiebeheer vanaf regel één.</b> Voordat je begint, niet als het '
        'misgaat. Hoofdstuk 14.</li>'
        '<li><b>Elke werkende versie vastleggen.</b> Dan kun je altijd terug naar het '
        'moment dat het nog wél deed wat je wilde.</li>'
        '<li><b>Sleutels en wachtwoorden buiten de code houden.</b> In een apart '
        'bestand dat niet meegaat in versiebeheer. Vraag de AI hier expliciet om, '
        'anders zet hij ze er gewoon in.</li>'
        '<li><b>Testgegevens gebruiken, geen echte.</b> Verzin namen en cijfers.</li>'
        '<li><b>Laat iemand die het wél kan lezen ernaar kijken</b> voordat anderen '
        'het gaan gebruiken. Eén uur van een programmeur is hier veel waard.</li>'
        '</ul>')

    p.tekst(
        'Niet doen',
        '<ul>'
        '<li><b>Blijven doorvragen als iets vijf keer niet lukt.</b> Je zit vast in '
        'een gesprek dat de verkeerde kant op is gegaan. Begin opnieuw met wat je '
        'geleerd hebt.</li>'
        '<li><b>Code accepteren die je niet kunt uitleggen.</b> Vraag om uitleg, of '
        'om een simpelere oplossing.</li>'
        '<li><b>"Maak het maar productieklaar" vragen.</b> Dat betekent niets. Vraag '
        'om concrete dingen: foutafhandeling, invoercontrole, een logboek.</li>'
        '<li><b>Extra’s laten toevoegen die je niet gevraagd hebt.</b> Elke regel code '
        'die je niet nodig hebt, is een regel die kapot kan gaan. Zeg het expliciet: '
        '<i>"voeg niets toe wat ik niet gevraagd heb"</i>.</li>'
        '<li><b>Je prototype stilletjes in productie laten glijden.</b> Dat gebeurt '
        'vaker dan je denkt: "het werkte toch?" Bepaal bewust wanneer iets van '
        'experiment naar systeem gaat, en wat er dan moet gebeuren.</li>'
        '</ul>')

    p.invulvelden(
        'Oefening: bouw iets kleins dat af komt',
        '<p>Kies iets waar je vandaag last van hebt en dat in een uur te bouwen is. '
        'Niet je grootste idee — je kleinste ergernis.</p>',
        [
            ('p13-wat', 'Wat ga je bouwen? Beschrijf het in vijf zinnen.',
             'Wie gebruikt het, wat gaat erin, wat komt eruit'),
            ('p13-niet', 'Wat hoeft het nadrukkelijk NIET te doen?',
             'De belangrijkste vraag van dit hoofdstuk'),
            ('p13-plan', 'Wat kwam er uit de planfase? Klopte de aanpak?',
             'Vraag eerst om een plan, dan pas om code'),
            ('p13-stuk', 'Hoe heb je het stukgekregen, en wat heb je aangepast?',
             'Lege invoer, rare tekens, te grote bestanden'),
            ('p13-review', 'Wat kwam er uit de kritische review in een nieuw gesprek?',
             'Fouten, onverwachte invoer, beveiligingsrisico’s'),
            ('p13-uitleg', 'Kun je in eigen woorden uitleggen wat het doet?',
             'Zo niet, is het nog niet af'),
        ])

    p.knoppenrij('Meenemen', '<p>In het volgende hoofdstuk zet je dit onder versiebeheer en publiceer je het.</p>')

    p.vraag(
        'Even checken',
        'Je hebt met AI een handig intern tooltje gebouwd. Een collega vraagt of hij '
        'het ook mag gebruiken, en of jullie er klantnamen in kunnen zetten. Wat is de '
        'juiste reactie?',
        [
            ('Delen kan, maar klantnamen erin betekent dat het een verwerking van '
             'persoonsgegevens wordt — dan is het geen prototype meer en moet er '
             'iemand naar kijken die de code kan beoordelen.', True),
            ('Prima, het werkt toch — gewoon doen.', False),
            ('Nee, zelfgebouwde tools mag je nooit met collega’s delen.', False),
            ('Alleen als je de klantnamen afkort tot initialen.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Delen op zich is prima. De grens wordt overschreden '
                       'bij persoonsgegevens: dat is het punt waarop een experiment een '
                       'systeem wordt, met beveiliging, bewaartermijnen en '
                       'verantwoordelijkheid.</p>',
            '_incorrect': {'final': '<p>Nog niet. Het is niet zwart-wit: delen mag, '
                                    'persoonsgegevens erin veranderen de aard van het '
                                    'ding. En initialen maken gegevens niet anoniem — '
                                    'initialen plus organisatie is vaak genoeg om '
                                    'iemand te herleiden.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
