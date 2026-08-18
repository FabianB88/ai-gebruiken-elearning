# -*- coding: utf-8 -*-
"""GitHub, GitHub CLI, Claude Code/Codex en Firebase: je werkplek klaarzetten."""


def bouw(p):
    p.tekst(
        'Drie gereedschappen, één middag',
        '<p>Wil je meer doen dan losse scriptjes, dan heb je drie dingen nodig. Ze '
        'zijn alle drie gratis, ze werken op Windows, en je zet ze in één middag '
        'klaar. Daarna heb je een werkplek waarin AI echt mee kan bouwen.</p>'
        '<ol>'
        '<li><b>Git en GitHub</b> — versiebeheer. Je kunt altijd terug naar een '
        'werkende versie, en je werk staat veilig online.</li>'
        '<li><b>De GitHub CLI</b> — GitHub bedienen vanaf de opdrachtregel, zodat '
        'Claude Code of Codex er zelf bij kan.</li>'
        '<li><b>De Firebase CLI</b> — een achterkant voor je toepassing: opslag, '
        'inloggen en hosting, zonder dat je een server hoeft te beheren.</li>'
        '</ol>')

    p.tekst(
        'Waarom versiebeheer juist bij AI onmisbaar is',
        '<p>Bij handmatig programmeren verandert er per keer een paar regels. Een '
        'AI-assistent past soms twintig bestanden tegelijk aan. Zonder versiebeheer '
        'weet je na een uur werken niet meer wat er veranderd is, en kun je een '
        'wijziging die iets sloopte niet meer terugdraaien.</p>'
        '<p>Met versiebeheer zie je precies wat er per stap veranderde, kun je elke '
        'stap ongedaan maken, en kan de AI zelf zien wat er sinds de laatste werkende '
        'versie gebeurd is. Dat laatste maakt hem merkbaar beter in het vinden van '
        'zijn eigen fouten.</p>')

    p.tekst(
        'Stappenplan A: Git en de GitHub CLI installeren op Windows',
        '<ol>'
        '<li><b>Maak een GitHub-account aan</b> op github.com als je die nog niet '
        'hebt. Gebruik je werkmailadres.</li>'
        '<li><b>Open PowerShell.</b> Startmenu, typ "PowerShell", enter.</li>'
        '<li><b>Installeer Git:</b><br><code>winget install --id Git.Git -e</code></li>'
        '<li><b>Installeer de GitHub CLI:</b><br>'
        '<code>winget install --id GitHub.cli -e</code></li>'
        '<li><b>Sluit PowerShell en open het opnieuw.</b> Anders kent hij de nieuwe '
        'commando’s nog niet.</li>'
        '<li><b>Controleer of het gelukt is:</b><br><code>git --version</code><br>'
        '<code>gh --version</code><br>Je krijgt twee versienummers terug.</li>'
        '<li><b>Log in bij GitHub:</b><br><code>gh auth login</code><br>Kies '
        '<i>GitHub.com</i>, dan <i>HTTPS</i>, dan <i>Login with a web browser</i>. Je '
        'krijgt een code van acht tekens te zien; die plak je in het browservenster '
        'dat opengaat.</li>'
        '<li><b>Stel je naam en mailadres in</b> zodat je wijzigingen op jouw naam '
        'staan:<br>'
        '<code>git config --global user.name "Jouw Naam"</code><br>'
        '<code>git config --global user.email "jij@organisatie.nl"</code></li>'
        '<li><b>Controleer de inlog:</b><br><code>gh auth status</code></li>'
        '</ol>')

    p.tekst(
        'Stappenplan B: je eerste project online zetten',
        '<p>Ga met PowerShell naar de map van je project (<code>cd '
        'pad\\naar\\je\\map</code>) en voer deze commando’s uit.</p>'
        '<ol>'
        '<li><b>Maak er een repository van:</b><br><code>git init</code></li>'
        '<li><b>Zet alles klaar en leg de eerste versie vast:</b><br>'
        '<code>git add .</code><br>'
        '<code>git commit -m "eerste versie"</code></li>'
        '<li><b>Maak de repository op GitHub aan en zet je werk erin — in één '
        'commando:</b><br>'
        '<code>gh repo create mijn-project --private --source=. --push</code><br>'
        'Kies bewust <code>--private</code>. Op <code>--public</code> zetten kan '
        'later; teruggaan is lastiger, want wat publiek stond, kan gekopieerd '
        'zijn.</li>'
        '<li><b>Vanaf nu, na elke werkende wijziging:</b><br>'
        '<code>git add .</code><br>'
        '<code>git commit -m "beschrijf wat je veranderd hebt"</code><br>'
        '<code>git push</code></li>'
        '<li><b>Terug naar een eerdere versie?</b> <code>git log --oneline</code> '
        'toont je geschiedenis; met <code>git checkout &lt;code&gt;</code> kijk je '
        'terug in een oudere versie. Weet je het niet zeker: vraag het je '
        'AI-assistent, met de uitvoer van <code>git status</code> erbij.</li>'
        '</ol>')

    p.aandacht(
        'Zet nooit sleutels of wachtwoorden in een repository',
        '<p>Ook niet in een private repository, en ook niet "tijdelijk". Wat één keer '
        'in de geschiedenis staat, blijft in de geschiedenis staan, ook als je het '
        'later weghaalt. Maak een bestand <code>.gitignore</code> met daarin de namen '
        'van bestanden die nooit mee mogen (bijvoorbeeld <code>.env</code>), en vraag '
        'je AI-assistent expliciet om sleutels in zo’n apart bestand te zetten.</p>')

    p.tekst(
        'Stappenplan C: Claude Code of Codex erbij zetten',
        '<p>Dit zijn AI-assistenten die in je projectmap werken: ze lezen je '
        'bestanden, schrijven wijzigingen, voeren commando’s uit en kunnen — dankzij '
        'de GitHub CLI die je net installeerde — ook je versiebeheer bedienen.</p>'
        '<ol>'
        '<li><b>Installeer Node.js</b> via nodejs.org (LTS-versie), als je dat nog '
        'niet gedaan hebt bij hoofdstuk 12.</li>'
        '<li><b>Installeer de assistent van je keuze:</b><br>'
        '<code>npm install -g @anthropic-ai/claude-code</code><br>'
        'of<br>'
        '<code>npm install -g @openai/codex</code></li>'
        '<li><b>Ga naar je projectmap</b> en start hem: <code>claude</code> '
        'respectievelijk <code>codex</code>. De eerste keer log je in.</li>'
        '<li><b>Begin met een vraag, niet met een opdracht.</b> "Leg uit wat er in '
        'deze map staat en wat het doet." Zo controleer je of hij de juiste map '
        'ziet.</li>'
        '<li><b>Laat hem zelf vastleggen in versiebeheer.</b> "Commit dit met een '
        'duidelijke beschrijving." Dat is precies waarom je de GitHub CLI hebt '
        'geïnstalleerd.</li>'
        '<li><b>Herlees hoofdstuk 11 voordat je hem zonder tussenvragen laat '
        'werken.</b> Hier geldt dat dubbel: deze assistent kan bestanden verwijderen '
        'en commando’s uitvoeren op je computer.</li>'
        '</ol>')

    p.tekst(
        'Stappenplan D: een achterkant met Firebase',
        '<p>Zodra je toepassing gegevens moet <i>bewaren</i> — een formulier, een '
        'aanmelding, een lijst die blijft staan — heb je een achterkant nodig. '
        '<b>Firebase</b> van Google geeft je database, inloggen en hosting zonder dat '
        'je een server beheert, met een gratis niveau dat voor een prototype ruim '
        'voldoende is.</p>'
        '<ol>'
        '<li><b>Installeer de Firebase CLI:</b><br>'
        '<code>npm install -g firebase-tools</code></li>'
        '<li><b>Log in:</b><br><code>firebase login</code><br>Er opent een '
        'browservenster waarin je je Google-account kiest.</li>'
        '<li><b>Maak een project aan</b> op console.firebase.google.com. Geef het een '
        'herkenbare naam en zet Google Analytics uit als je het niet nodig hebt.</li>'
        '<li><b>Koppel je map aan het project:</b><br><code>firebase init</code><br>'
        'Kies met de spatiebalk wat je nodig hebt — meestal <i>Hosting</i> en '
        '<i>Firestore</i> — en daarna je bestaande project.</li>'
        '<li><b>Publiceer:</b><br><code>firebase deploy</code><br>Je krijgt een URL '
        'terug waarop je toepassing live staat.</li>'
        '<li><b>Regel de beveiligingsregels vóór je iets echts opslaat.</b> Zie de '
        'waarschuwing hieronder.</li>'
        '</ol>')

    p.aandacht(
        'De valkuil van Firebase: de database staat standaard open',
        '<p>Als je bij het opzetten van Firestore kiest voor de testmodus, staat je '
        'database een tijdlang <b>open voor iedereen op internet</b> — lezen én '
        'schrijven. Dat is bedoeld om snel te kunnen beginnen, en het is de meest '
        'voorkomende manier waarop met AI gebouwde toepassingen gegevens lekken.</p>'
        '<p>Wat je doet: kies de <b>productiemodus</b>, en schrijf daarna '
        'beveiligingsregels die precies vastleggen wie wat mag. Vraag je '
        'AI-assistent: <i>"schrijf Firestore-beveiligingsregels waarbij alleen '
        'ingelogde gebruikers hun eigen gegevens kunnen lezen en schrijven, en leg per '
        'regel uit wat hij doet"</i>. Test daarna in de Firebase-console met de '
        'regelsimulator of een niet-ingelogde bezoeker er echt niet bij kan.</p>'
        '<p>En nogmaals hoofdstuk 6: zet geen persoonsgegevens in een zelfgebouwde '
        'toepassing zonder dat iemand met verstand van zaken ernaar heeft '
        'gekeken.</p>')

    p.tekst(
        'Alternatief: alleen publiceren, zonder achterkant',
        '<p>Heb je alleen een website of een pagina die niets hoeft te bewaren, dan '
        'heb je Firebase niet nodig. <b>GitHub Pages</b> is dan genoeg: zet je '
        'bestanden in een repository, ga naar Settings → Pages, kies de branch, en je '
        'site staat gratis online. Geen server, geen kosten, geen '
        'beveiligingsregels.</p>')

    p.invulvelden(
        'Oefening: zet je werkplek op en publiceer iets',
        '<p>Neem wat je in hoofdstuk 13 gebouwd hebt en breng het naar buiten.</p>',
        [
            ('p14-installed', 'Welke onderdelen heb je geïnstalleerd? Waar liep je '
             'vast?',
             'Git, GitHub CLI, Node, Claude Code of Codex, Firebase CLI'),
            ('p14-repo', 'Hoe heet je repository, en staat hij op private of public?',
             'En waarom die keuze?'),
            ('p14-commits', 'Beschrijf drie momenten waarop je een versie hebt '
             'vastgelegd.',
             'Wat had je net veranderd?'),
            ('p14-online', 'Waar staat het nu online? Via GitHub Pages of Firebase?',
             'Plak de URL'),
            ('p14-regels', 'Als je Firebase gebruikt: welke beveiligingsregels heb je '
             'ingesteld?',
             'En hoe heb je gecontroleerd dat ze werken?'),
            ('p14-terug', 'Heb je een keer een wijziging teruggedraaid? Hoe ging dat?',
             'Probeer het bewust een keer — dat is de hele reden voor versiebeheer'),
        ])

    p.knoppenrij('Meenemen', '<p>Bewaar de commando’s die je het vaakst gebruikt in een eigen spiekbriefje.</p>')

    p.vraag(
        'Even checken',
        'Je zet met Firebase een formulier online waarmee collega’s zich kunnen '
        'aanmelden voor een bijeenkomst. Wat is het grootste risico als je bij het '
        'opzetten de testmodus kiest?',
        [
            ('De database is dan open voor iedereen op internet — iedereen kan de '
             'aanmeldingen lezen en aanpassen.', True),
            ('Het project loopt na de testperiode automatisch kosten op.', False),
            ('De gegevens worden opgeslagen buiten de EU.', False),
            ('Het formulier werkt alleen in Chrome.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Testmodus betekent open lezen en schrijven voor '
                       'iedereen die de URL van je database kent. Kies productiemodus '
                       'en schrijf beveiligingsregels vóór er echte gegevens in '
                       'komen.</p>',
            '_incorrect': {'final': '<p>Nog niet. Waar het om gaat is toegang: in '
                                    'testmodus staat je database open voor de hele '
                                    'wereld. Dat is precies de manier waarop '
                                    'zelfgebouwde toepassingen gegevens lekken.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
