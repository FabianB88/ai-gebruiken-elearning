# -*- coding: utf-8 -*-
"""AI naar je informatie brengen in plaats van andersom."""


def bouw(p):
    p.tekst(
        'Draai de richting om',
        '<p>De standaardmanier van werken is: jij zoekt een bestand, opent het, '
        'kopieert het relevante deel en plakt dat in een chatvenster. Je brengt je '
        'informatie naar de AI.</p>'
        '<p>Er is een betere manier. Je installeert de AI op je eigen computer en '
        'geeft hem toegang tot een map. Vanaf dat moment kun je vragen stellen over '
        '<i>alles</i> wat daarin staat, zonder iets te uploaden: "welke van deze '
        'twaalf offertes noemt een levertijd langer dan zes weken?", "maak van deze '
        'map met losse notities één samenvattend overzicht", "hernoem al deze '
        'bestanden volgens onze afspraak".</p>'
        '<p>Dat is niet alleen makkelijker. Het verandert wat je überhaupt aan AI '
        'durft te vragen, omdat de drempel van kopiëren en plakken wegvalt.</p>')

    p.beeld(
        'ai-naar-je-data.svg',
        alt='Twee panelen naast elkaar. Links, De gewone manier: jouw map met honderd '
            'bestanden gaat via een pijl naar een chatvenster met één geplakt stuk, '
            'en elke keer opnieuw zoek, open, kopieer en plak je. Gevolg: je stelt '
            'alleen vragen die het plakken waard zijn. Rechts, De omgekeerde manier: '
            'een afgebakende werkmap en de AI-assistent staan met pijlen in twee '
            'richtingen met elkaar verbonden; na eenmalig instellen kun je vragen '
            'stellen over de hele map, bestanden ordenen en resultaten terugkrijgen '
            'als nieuw bestand. Onderaan een waarschuwing dat in beide gevallen alles '
            'wat de AI opent naar de servers van de aanbieder gaat.',
        onderschrift='Rechts scheelt kopiëren en plakken — het is geen '
                     'privacy-oplossing.')

    p.aandacht(
        'Eén misverstand meteen uit de weg',
        '<p>"De AI werkt lokaal, dus mijn gegevens blijven bij mij" — dat klopt '
        '<b>niet</b>. Claude Desktop en de ChatGPT-app draaien het model niet op jouw '
        'computer; ze sturen wat ze lezen alsnog naar de servers van de aanbieder. Wat '
        'lokaal blijft, is alles wat de AI <i>niet</i> opent.</p>'
        '<p>Het voordeel is dus gemak en overzicht, niet automatisch privacy. Alle '
        'regels uit hoofdstuk 6 gelden onverkort: geef geen toegang tot een map met '
        'persoonsgegevens. Wil je écht dat er niets weggaat, dan heb je een lokaal '
        'draaiend model nodig — daarover onderaan meer.</p>')

    p.tekst(
        'Stappenplan: Claude Desktop toegang geven tot een map',
        '<p>Dit is de meest gebruikte route. Reken op een kwartier de eerste keer.</p>'
        '<ol>'
        '<li><b>Installeer Claude Desktop</b> via claude.ai/download en log in met je '
        'zakelijke account.</li>'
        '<li><b>Maak eerst een aparte map aan</b> waar je mee gaat werken, '
        'bijvoorbeeld <code>C:\\Users\\jouwnaam\\Documents\\ai-werkmap</code>. Geef '
        'geen toegang tot je hele gebruikersmap of je Documenten-map — daar staat '
        'gegarandeerd meer in dan je bedoelt.</li>'
        '<li><b>Kopieer de bestanden waar je mee wil werken naar die map.</b> Kopieer, '
        'niet verplaats: dan kan er niets misgaan met je originelen.</li>'
        '<li><b>Open in Claude Desktop de instellingen en kijk of er een onderdeel '
        'Extensies of Connectors is.</b> Staat de bestandstoegang daar als '
        'kant-en-klare uitbreiding, dan installeer je hem met een paar klikken, wijs '
        'je je map aan en ben je klaar. Ga dan door naar stap 7.</li>'
        '<li><b>Anders: installeer Node.js</b> via nodejs.org (de LTS-versie). Dat is '
        'de motor waarmee de koppeling draait.</li>'
        '<li><b>Bewerk het configuratiebestand.</b> Open de instellingen, ga naar '
        'Ontwikkelaar en kies het configuratiebestand bewerken. Zet daar dit in — met '
        'jouw eigen mappad, en let op de dubbele backslashes:</li>'
        '</ol>'
        '<pre><code>{\n'
        '  "mcpServers": {\n'
        '    "bestanden": {\n'
        '      "command": "npx",\n'
        '      "args": [\n'
        '        "-y",\n'
        '        "@modelcontextprotocol/server-filesystem",\n'
        '        "C:\\\\Users\\\\jouwnaam\\\\Documents\\\\ai-werkmap"\n'
        '      ]\n'
        '    }\n'
        '  }\n'
        '}</code></pre>'
        '<ol start="7">'
        '<li><b>Sluit Claude Desktop volledig af en start opnieuw.</b> Niet alleen het '
        'venster sluiten — helemaal afsluiten, ook uit het systeemvak.</li>'
        '<li><b>Test met een onschuldige vraag:</b> "welke bestanden staan er in mijn '
        'werkmap?" Krijg je een lijst, dan werkt het.</li>'
        '</ol>')

    p.accordeon(
        'Als het niet werkt',
        '<p>Vier oorzaken dekken vrijwel alle gevallen.</p>',
        [
            {'title': 'Claude ziet de map niet',
             'body': '<p>Bijna altijd de dubbele backslashes in het pad. In JSON '
                     'schrijf je <code>C:\\\\Users\\\\…</code>, met dubbele. Of het '
                     'programma is niet echt afgesloten geweest — controleer het '
                     'systeemvak rechtsonder.</p>'},
            {'title': 'Foutmelding over npx of node',
             'body': '<p>Node.js staat niet geïnstalleerd of niet in je PATH. '
                     'Installeer de LTS-versie van nodejs.org en herstart je '
                     'computer.</p>'},
            {'title': 'Het JSON-bestand geeft een fout',
             'body': '<p>Eén komma te veel of te weinig. Plak de inhoud in een '
                     'gesprek en vraag "is dit geldige JSON?" — sneller dan zelf '
                     'zoeken.</p>'},
            {'title': 'Hij mag lezen maar niet schrijven',
             'body': '<p>Controleer de rechten op de map in Windows, en of je het pad '
                     'goed hebt gespeld. Een typefout in een mapnaam geeft geen '
                     'duidelijke fout — hij vindt hem gewoon niet.</p>'},
        ])

    p.tekst(
        'Wat je er dan mee doet',
        '<ul>'
        '<li><b>Vragen stellen over een hele map.</b> "Welke van deze rapporten noemt '
        'de nieuwe subsidieregeling, en wat zeggen ze erover?"</li>'
        '<li><b>Bestanden ordenen.</b> Hernoemen volgens een afspraak, sorteren in '
        'submappen, dubbele eruit halen. Werk dat je altijd uitstelt.</li>'
        '<li><b>Uit veel documenten één overzicht maken.</b> Twintig verslagen naar '
        'één tabel met datum, aanwezigen en besluiten.</li>'
        '<li><b>Werken aan een document zonder heen en weer plakken.</b> "Open '
        'notitie.md, werk hoofdstuk 3 uit, en bewaar het als '
        'notitie-v2.md."</li>'
        '<li><b>Data doorrekenen.</b> Een CSV in de map laten analyseren, met code, en '
        'de uitkomst als nieuw bestand laten wegschrijven.</li>'
        '</ul>')

    p.tekst(
        'Vier regels voor werken in je eigen mappen',
        '<ol>'
        '<li><b>Eén afgebakende werkmap, nooit je hele schijf.</b> Wat je niet '
        'openstelt, kan niet misgaan.</li>'
        '<li><b>Werk op kopieën.</b> Zeker de eerste weken. Een agent die "opruimt" '
        'kan grondiger zijn dan je wil.</li>'
        '<li><b>Zet de map onder versiebeheer</b> als het om werk gaat dat ertoe doet '
        '— dan kun je elke wijziging terugdraaien. Hoofdstuk 14 laat zien hoe.</li>'
        '<li><b>Geen persoonsgegevens in de werkmap.</b> Ook niet "even tijdelijk". '
        'Ook niet in een submap.</li>'
        '</ol>')

    p.tekst(
        'Als het écht niet weg mag: een model op je eigen machine',
        '<p>Voor werk waarbij niets naar buiten mag, kun je een model volledig lokaal '
        'draaien. Programma’s als <b>Ollama</b> en <b>LM Studio</b> maken dat '
        'eenvoudig: installeren, een model downloaden, klaar. Er gaat dan geen enkel '
        'byte naar een server.</p>'
        '<p>Wees wel eerlijk over de afweging. Een model dat op een gewone laptop '
        'draait, is merkbaar minder capabel dan Claude Opus of GPT-5.6, en je hebt een '
        'stevige machine nodig voordat het prettig werkt. Het is de juiste keuze voor '
        'gevoelige gegevens, niet voor je dagelijkse werk.</p>')

    p.invulvelden(
        'Oefening: zet je werkmap op',
        '<p>Doe het echt — dit hoofdstuk lees je niet, dit doe je.</p>',
        [
            ('p12-map', 'Welke map heb je aangemaakt en opengesteld?',
             'Het volledige pad, en waarom deze afbakening'),
            ('p12-check', 'Wat staat er NIET in die map, bewust?',
             'Welke bestanden heb je er expres buiten gelaten?'),
            ('p12-vraag', 'Welke vraag stelde je over de inhoud van de map?',
             'Iets wat je met kopiëren en plakken niet snel had gekund'),
            ('p12-werkt', 'Werkte het meteen? Zo nee, waar liep je vast?',
             'Ook nuttig om te bewaren voor de volgende keer'),
            ('p12-winst', 'Welke terugkerende klus ga je hiermee doen?',
             'Iets uit je lijst van hoofdstuk 3'),
        ])

    p.knoppenrij('Meenemen', '<p>Bewaar het pad en de configuratie; je hebt ze nodig als je overstapt naar een nieuwe computer.</p>')

    p.vraag(
        'Even checken',
        'Iemand zegt: "ik gebruik Claude Desktop met toegang tot mijn mappen, dus mijn '
        'gegevens blijven lokaal en de AVG is geen probleem." Wat klopt hier niet aan?',
        [
            ('Alleen het model draait niet lokaal: alles wat de AI leest, gaat naar de '
             'servers van de aanbieder. De AVG-regels gelden dus onverkort.', True),
            ('Niets — bij een desktop-app blijft alles op je eigen computer.', False),
            ('Het klopt wel, maar alleen als je geen internetverbinding hebt.', False),
            ('Het klopt, mits je een betaald abonnement hebt.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. "Op je bureaublad" is niet hetzelfde als "op je '
                       'computer verwerkt". De inhoud van elk bestand dat de AI opent, '
                       'gaat de leiding over. Voor echt lokale verwerking heb je een '
                       'lokaal draaiend model nodig.</p>',
            '_incorrect': {'final': '<p>Nog niet. De desktop-app is een venster op een '
                                    'model dat in de cloud draait. Zonder internet '
                                    'werkt hij helemaal niet — dat is meteen het '
                                    'bewijs.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
