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
        'durft te vragen, omdat de drempel van kopiëren en plakken wegvalt. Het is de '
        'stap naar niveau 4 uit hoofdstuk 3.</p>')

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
        'Goed nieuws: je hoeft niets technisch te doen',
        '<p>Vroeger moest je hiervoor een koppeling instellen in een '
        'configuratiebestand, met Node.js erbij en dubbele backslashes in je '
        'mappaden. Dat hoeft niet meer. <b>De desktop-app kan uit zichzelf bij je '
        'bestanden</b> — je wijst een map aan en geeft toestemming, en klaar.</p>'
        '<p>MCP-koppelingen (uit hoofdstuk 8) heb je nog steeds nodig voor '
        '<i>andere systemen</i>: een database, een dienst waar geen kant-en-klare '
        'koppeling voor is. Voor gewone bestanden op je eigen schijf niet.</p>')

    p.aandacht(
        'En als er tóch iets ingesteld moet worden: laat het doen',
        '<p>Dit geldt voor de rest van de cursus net zo goed. Kom je een configuratie, '
        'een instellingenbestand of een technische foutmelding tegen — <b>ga dat niet '
        'zelf zitten uittypen.</b> Daar is de AI juist goed in, en jij maakt er '
        'gegarandeerd een typefout in.</p>'
        '<p>Wat je doet: plak de foutmelding letterlijk in een gesprek, zeg welk '
        'programma het is en wat je probeerde, en vraag om het op te lossen. Werk je '
        'met Claude Code in je projectmap, dan kan hij het bestand zelf openen, '
        'aanpassen en controleren — dan hoef je er niet eens naar te kijken.</p>'
        '<p>De enige regel: laat hem uitleggen wat hij verandert en waarom, zodat je '
        'weet wat er op je machine gebeurt. Niet begrijpen wat er staat is prima; niet '
        'weten wát er gebeurt is dat niet.</p>')

    p.tekst(
        'Stappenplan: Claude Desktop toegang geven tot een map',
        '<p>Reken op tien minuten, en de meeste tijd gaat zitten in stap 2 en 3.</p>'
        '<ol>'
        '<li><b>Installeer Claude Desktop</b> via claude.ai/download en log in met je '
        'privé-account (zie hoofdstuk 6).</li>'
        '<li><b>Maak eerst een aparte werkmap aan</b>, bijvoorbeeld '
        '<code>Documenten\\ai-werkmap</code>. Geef geen toegang tot je hele '
        'gebruikersmap, je bureaublad of je complete Documenten-map — daar staat '
        'gegarandeerd meer in dan je bedoelt.</li>'
        '<li><b>Kopieer de bestanden waar je mee wil werken naar die map.</b> '
        'Kopiëren, niet verplaatsen: dan kan er niets misgaan met je originelen. Dit '
        'is meteen het moment om te bedenken wat er níet in hoort.</li>'
        '<li><b>Wijs de map aan in Claude Desktop.</b> Je vindt dit bij de '
        'instellingen of bij het starten van een gesprek; de app vraagt om '
        'toestemming voor de map die je kiest. Geef alleen die ene map vrij.</li>'
        '<li><b>Test met een onschuldige vraag:</b> "welke bestanden staan er in mijn '
        'werkmap?" Krijg je een kloppende lijst, dan staat het goed.</li>'
        '<li><b>Test daarna of hij ook kan schrijven:</b> "maak een bestand '
        'test.md met daarin drie regels tekst." Kijk in de verkenner of het er '
        'staat.</li>'
        '<li><b>Zet je vaste regels erbij.</b> De regels uit hoofdstuk 9 gelden ook '
        'hier — en juist hier, want nu kan de AI bestanden aanmaken en wijzigen.</li>'
        '</ol>')

    p.accordeon(
        'Als het niet werkt',
        '<p>Vier oorzaken dekken vrijwel alle gevallen.</p>',
        [
            {'title': 'Hij ziet de map niet',
             'body': '<p>Meestal is de toestemming niet echt gegeven, of is er een '
                     'andere map aangewezen dan je denkt. Controleer in de '
                     'instellingen welke map er precies vrijgegeven is, en vraag hem '
                     'het volledige pad te noemen dat hij ziet.</p>'},
            {'title': 'De bestanden staan alleen in de cloud',
             'body': '<p>Dit is op Windows de meest voorkomende oorzaak. Staat je map '
                     'in OneDrive, dan zijn bestanden vaak alleen online beschikbaar '
                     'en niet echt op je schijf. Klik met de rechtermuisknop op de map '
                     'en kies <i>Altijd behouden op dit apparaat</i>, of werk in een '
                     'map buiten OneDrive.</p>'},
            {'title': 'Hij leest wel maar schrijft niet',
             'body': '<p>Controleer of de map niet alleen-lezen is, en of hij niet in '
                     'een beveiligde systeemmap staat. Verplaats hem bij twijfel naar '
                     'een gewone map onder je gebruikersmap.</p>'},
            {'title': 'Hij vindt bestanden niet terug die er wel zijn',
             'body': '<p>Vaak een naamkwestie: hij zoekt op wat jij noemt, en dat '
                     'staat net anders in de bestandsnaam. Vraag eerst om een lijst '
                     'van alle bestanden en verwijs daarna naar de exacte naam. Dit is '
                     'ook precies waarom nette bestandsnamen zich terugbetalen.</p>'},
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
        'notitie.md, werk hoofdstuk 3 uit, en bewaar het als notitie-v2.md."</li>'
        '<li><b>Grote stukken in delen laten schrijven.</b> Dit is werkvorm 4 uit '
        'hoofdstuk 10: elk hoofdstuk een eigen bestand, dus geen enkele last van de '
        'maximale antwoordlengte.</li>'
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
        '<li><b>Zet de map onder versiebeheer</b> als het om werk gaat dat ertoe doet — '
        'dan kun je elke wijziging terugdraaien. Hoofdstuk 14 laat zien hoe.</li>'
        '<li><b>Geen persoonsgegevens in de werkmap.</b> Ook niet "even tijdelijk", '
        'ook niet in een submap. Loop de map na voordat je toegang geeft, niet '
        'erna.</li>'
        '</ol>')

    p.tekst(
        'Als het écht niet weg mag: een model op je eigen machine',
        '<p>Voor werk waarbij niets naar buiten mag, kun je een model volledig lokaal '
        'draaien. Programma’s als <b>Ollama</b> en <b>LM Studio</b> maken dat '
        'eenvoudig: installeren, een model downloaden, klaar. Er gaat dan geen enkele '
        'byte naar een server.</p>'
        '<p>Wees wel eerlijk over de afweging. Een model dat op een gewone laptop '
        'draait, is merkbaar minder capabel dan Claude Opus of GPT-5.6, en je hebt een '
        'stevige machine nodig voordat het prettig werkt. Het is de juiste keuze voor '
        'gevoelige gegevens, niet voor je dagelijkse werk.</p>')

    p.invulvelden(
        'Oefening: zet je werkmap op',
        '<p>Doe het echt — dit hoofdstuk lees je niet, dit doe je.</p>',
        [
            ('p12-map', 'Welke map heb je aangemaakt en vrijgegeven?',
             'Het volledige pad, en waarom deze afbakening'),
            ('p12-check', 'Wat staat er bewust NIET in die map?',
             'Welke bestanden heb je er expres buiten gelaten?'),
            ('p12-vraag', 'Welke vraag stelde je over de inhoud van de map?',
             'Iets wat je met kopiëren en plakken niet snel had gekund'),
            ('p12-schrijven', 'Heb je hem ook een bestand laten aanmaken? Wat kwam '
             'eruit?',
             'Controleer in de verkenner of het er echt staat'),
            ('p12-werkt', 'Werkte het meteen? Zo nee, waar liep je vast?',
             'Bijv. OneDrive-bestanden die alleen online stonden'),
            ('p12-winst', 'Welke terugkerende klus ga je hiermee doen?',
             'Iets uit je opdracht van hoofdstuk 3'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Noteer het pad van je werkmap; je hebt het nodig als je overstapt naar een '
        'nieuwe computer.</p>')

    p.vraag(
        'Even checken',
        'Iemand zegt: "ik gebruik Claude Desktop met toegang tot mijn mappen, dus mijn '
        'gegevens blijven lokaal en de AVG is geen probleem." Wat klopt hier niet aan?',
        [
            ('Alleen het model draait niet lokaal: alles wat de AI leest, gaat naar de '
             'servers van de aanbieder. De AVG-regels gelden dus onverkort.', True),
            ('Niets — bij een desktop-app blijft alles op je eigen computer.', False),
            ('Het klopt wel, maar alleen als je geen internetverbinding hebt.', False),
            ('Het klopt, mits je modeltraining hebt uitgezet.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. "Op je bureaublad" is niet hetzelfde als "op je '
                       'computer verwerkt". De inhoud van elk bestand dat de AI opent, '
                       'gaat de leiding over. Modeltraining uitzetten helpt tegen '
                       'hergebruik, maar verandert dat niet.</p>',
            '_incorrect': {'final': '<p>Nog niet. De desktop-app is een venster op een '
                                    'model dat in de cloud draait. Zonder internet '
                                    'werkt hij helemaal niet — dat is meteen het '
                                    'bewijs.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
