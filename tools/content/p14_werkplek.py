# -*- coding: utf-8 -*-
"""Je werkplek laten inrichten door je AI-assistent, en publiceren."""


def bouw(p):
    p.tekst(
        'Je typt dit niet zelf',
        '<p>Wil je meer doen dan losse scriptjes, dan heb je een paar gereedschappen '
        'nodig: versiebeheer, een koppeling met GitHub, een assistent die in je '
        'projectmap werkt, en een achterkant voor je toepassing. Allemaal gratis, '
        'allemaal werkend op Windows.</p>'
        '<p>De oude manier was: handleidingen erbij, commando’s overtypen, hopen dat je '
        'geen spatie vergeet. Dat hoeft niet meer. <b>Je richt één assistent in, en '
        'die installeert en configureert de rest voor je.</b> Claude Code en Codex '
        'kunnen software downloaden, installeren, instellingen wegschrijven en '
        'controleren of het werkt.</p>'
        '<p>Waar deze cursus "Claude Code" schrijft, kun je overal ook "Codex" lezen — '
        'het werkt hetzelfde. Kies er één en blijf daarbij.</p>')

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
        'Stappenplan A: één keer een startpunt maken',
        '<p>Dit is het enige deel waarbij je zelf iets moet regelen. Daarna doet je '
        'assistent het werk.</p>'
        '<ol>'
        '<li><b>Zorg dat je Claude Desktop hebt draaien</b> met toegang tot een '
        'werkmap, zoals in hoofdstuk 12.</li>'
        '<li><b>Maak een GitHub-account aan</b> op github.com, als je die nog niet '
        'hebt. Gebruik je privémailadres (hoofdstuk 6) en onthoud je '
        'gebruikersnaam.</li>'
        '<li><b>Vraag de desktop-app om je machine klaar te maken.</b> Letterlijk '
        'zoiets:<br><i>"Installeer Node.js (LTS) en daarna Claude Code op deze '
        'Windows-machine. Controleer na afloop of beide werken en laat me de '
        'versienummers zien. Leg uit wat je doet voordat je iets installeert."</i></li>'
        '<li><b>Kijk mee terwijl hij bezig is.</b> Hij gebruikt de pakketbeheerder van '
        'Windows en laat zien wat er gebeurt. Vraagt Windows om toestemming, geef die '
        'dan bewust.</li>'
        '<li><b>Open daarna een nieuw terminalvenster</b> en start je assistent in je '
        'projectmap met <code>claude</code> (of <code>codex</code>). De eerste keer log '
        'je in.</li>'
        '</ol>')

    p.tekst(
        'Stappenplan B: laat je assistent de rest installeren',
        '<p>Nu je een assistent in je projectmap hebt, geef je hem de rest als één '
        'opdracht. Plak dit:</p>'
        '<blockquote><p><i>"Richt deze machine in voor ontwikkelwerk. Installeer, als '
        'ze er nog niet zijn: Git, de GitHub CLI (gh), en de Firebase CLI. Installeer '
        'daarnaast Rust Token Killer van GitHub. Controleer na elke installatie of het '
        'werkt en toon het versienummer. Vertel me daarna welke stappen ik zelf nog '
        'moet doen om in te loggen."</i></p></blockquote>'
        '<p>Die laatste zin is de belangrijkste. Inloggen en je apparaat koppelen kan '
        'hij niet voor je doen — dat moet jij zelf, en dat staat in stappenplan C '
        'hieronder. Een goede assistent zegt dat uit zichzelf; zo niet, dan heb je er '
        'nu om gevraagd.</p>'
        '<p><b>Als er iets misgaat:</b> plak de foutmelding letterlijk terug en laat '
        'hem het oplossen. Ga niet zelf zitten zoeken op internet.</p>')

    p.accordeon(
        'Wat je nu op je machine hebt staan, en waarvoor',
        '<p>Handig om te weten wat er geïnstalleerd is. Bij elk stuk staat het '
        'commando waarmee je kunt controleren of het werkt.</p>',
        [
            {'title': 'Git — versiebeheer',
             'body': '<p>Houdt bij wat er verandert in je bestanden, zodat je altijd '
                     'terug kunt naar een werkende versie.</p>'
                     '<p>Controle: <code>git --version</code></p>'},
            {'title': 'GitHub CLI (gh) — GitHub vanaf de opdrachtregel',
             'body': '<p>Hiermee kan je assistent zélf repositories aanmaken, '
                     'wijzigingen pushen en pull requests openen. Zonder dit moet je '
                     'alles via de website doen, en dan kan je assistent er niet bij. '
                     'Dit is precies wat het koppelen zo veel makkelijker maakt.</p>'
                     '<p>Controle: <code>gh --version</code> en later '
                     '<code>gh auth status</code></p>'},
            {'title': 'Rust Token Killer (rtk) — scheelt tokens',
             'body': '<p>Een hulpprogramma dat de uitvoer van ontwikkelcommando’s '
                     'filtert voordat die in het gesprek belandt. Draai je '
                     '<code>git status</code> in een grote map, dan komen daar zo '
                     'honderden regels uit die allemaal je gesprekslimiet opvreten. '
                     'Rtk knipt dat terug tot wat ertoe doet.</p>'
                     '<p>Voor lange sessies scheelt dat serieus: je houdt meer ruimte '
                     'over voor het echte werk voordat je gesprek volloopt. Zeker de '
                     'moeite waard als je met hoofdstuk 13 aan de slag gaat.</p>'
                     '<p>Controle: <code>rtk --version</code> en '
                     '<code>rtk gain</code>, dat laat zien hoeveel je bespaard '
                     'hebt.</p>'
                     '<p><b>Let op:</b> er bestaat een ander programma met dezelfde '
                     'afkorting. Werkt <code>rtk gain</code> niet, dan heb je de '
                     'verkeerde te pakken — vraag je assistent om te controleren welke '
                     'er geïnstalleerd staat.</p>'},
            {'title': 'Firebase CLI — je achterkant',
             'body': '<p>Voor als je toepassing gegevens moet bewaren of mensen moet '
                     'laten inloggen. Zie stappenplan D en E.</p>'
                     '<p>Controle: <code>firebase --version</code></p>'},
            {'title': 'Node.js — de motor eronder',
             'body': '<p>Veel van bovenstaande draait hierop. Je gebruikt het zelf '
                     'nooit rechtstreeks.</p>'
                     '<p>Controle: <code>node --version</code></p>'},
        ])

    p.aandacht(
        'Wat je wél zelf moet doen: je apparaat koppelen',
        '<p>Inloggen kan je assistent niet voor je doen, en dat is maar goed ook. Bij '
        'elke dienst hoort een moment waarop jij in een browser bevestigt dat deze '
        'computer namens jou mag handelen. Hieronder staat per dienst wat je te zien '
        'krijgt, zodat je niet schrikt.</p>')

    p.tekst(
        'Stappenplan C: inloggen bij de drie diensten',
        '<ol>'
        '<li><b>GitHub.</b> Typ <code>gh auth login</code>. Kies achtereenvolgens '
        '<i>GitHub.com</i>, <i>HTTPS</i>, en <i>Login with a web browser</i>. Je '
        'krijgt een code van acht tekens te zien; onthoud die, druk op enter, en plak '
        'hem in het browservenster dat opengaat. Controleer daarna met '
        '<code>gh auth status</code>.</li>'
        '<li><b>Je naam instellen</b> zodat wijzigingen op jouw naam komen te staan. '
        'Vraag je assistent: <i>"stel mijn git-gebruikersnaam en e-mailadres in op '
        '[naam] en [mailadres]"</i>. Gebruik hetzelfde mailadres als bij je '
        'GitHub-account.</li>'
        '<li><b>Firebase.</b> Typ <code>firebase login</code>. Er opent een '
        'browservenster waarin je je Google-account kiest en toestemming geeft. Zie je '
        'geen venster, kijk dan in de terminal — daar staat een link die je zelf kunt '
        'openen.</li>'
        '<li><b>Claude Code of Codex zelf.</b> Bij de eerste start log je in met je '
        'privé-account. Ook hier: een code of een browservenster.</li>'
        '<li><b>Werkt het niet?</b> Vraag je assistent om mee te kijken: <i>"gh auth '
        'status geeft dit terug: [plak de uitvoer]. Wat is er mis?"</i> Dit is precies '
        'het soort probleem waar hij goed in is.</li>'
        '</ol>')

    p.tekst(
        'Stappenplan D: je eerste project online zetten',
        '<p>Vanaf nu hoef je zelf niets meer te typen. Ga met je assistent naar je '
        'projectmap en vraag:</p>'
        '<blockquote><p><i>"Zet deze map onder versiebeheer, maak er een private '
        'repository van op mijn GitHub en push de eerste versie. Maak eerst een '
        '.gitignore die voorkomt dat sleutels, wachtwoorden en node_modules '
        'meegaan."</i></p></blockquote>'
        '<p>Kies bewust <b>private</b>. Op public zetten kan later; teruggaan is '
        'lastiger, want wat publiek stond, kan gekopieerd zijn.</p>'
        '<p>Daarna, na elke werkende wijziging: <i>"leg dit vast met een duidelijke '
        'beschrijving en push het"</i>. En als er iets stukgaat: <i>"laat zien wat er '
        'sinds de laatste werkende versie veranderd is"</i> of <i>"draai de laatste '
        'wijziging terug"</i>.</p>'
        '<p>Wil je begrijpen wat er onder water gebeurt — aan te raden, want dan kun '
        'je het zelf controleren — vraag dan: <i>"leg uit welke git-commando’s je hebt '
        'gebruikt en wat ze doen"</i>.</p>')

    p.aandacht(
        'Zet nooit sleutels of wachtwoorden in een repository',
        '<p>Ook niet in een private repository, en ook niet "tijdelijk". Wat één keer '
        'in de geschiedenis staat, blijft in de geschiedenis staan, ook als je het '
        'later weghaalt. Vraag je assistent expliciet om sleutels in een apart bestand '
        'te zetten dat in <code>.gitignore</code> staat, en om te controleren of er '
        'niets gevoeligs is meegegaan voordat je pusht.</p>')

    p.tekst(
        'Stappenplan E: een achterkant met Firebase',
        '<p>Zodra je toepassing gegevens moet <i>bewaren</i> — een formulier, een '
        'aanmelding, een lijst die blijft staan — heb je een achterkant nodig. '
        '<b>Firebase</b> van Google geeft je database, inloggen en hosting zonder dat '
        'je een server beheert, met een gratis niveau dat voor een prototype ruim '
        'voldoende is.</p>'
        '<ol>'
        '<li><b>Maak een project aan</b> op console.firebase.google.com. Dit doe je '
        'zelf, in de browser. Geef het een herkenbare naam en zet Google Analytics uit '
        'als je het niet nodig hebt.</li>'
        '<li><b>Laat je assistent de map koppelen:</b> <i>"koppel deze map aan mijn '
        'Firebase-project [naam], met Hosting en Firestore. Kies productiemodus, niet '
        'de testmodus."</i></li>'
        '<li><b>Laat publiceren:</b> <i>"publiceer de site en geef me de URL"</i>. '
        'Onder water is dat <code>firebase deploy</code>.</li>'
        '<li><b>Regel de beveiligingsregels vóór je iets echts opslaat.</b> Zie de '
        'waarschuwing verderop.</li>'
        '</ol>')

    p.tekst(
        'Stappenplan F: laat mensen inloggen met Google',
        '<p>Zodra je toepassing moet weten <i>wie</i> er iets doet — een aanmelding, '
        'een persoonlijke lijst, iets wat niet iedereen mag zien — heb je inloggen '
        'nodig. Bouw dat <b>nooit zelf</b>. Gebruik <b>Firebase Authentication met '
        'Google-inloggen</b>: mensen klikken op één knop, loggen in met het '
        'Google-account dat ze toch al hebben, en jij slaat nooit een wachtwoord '
        'op.</p>'
        '<p>Dat laatste is het echte voordeel. Wachtwoorden die je niet hebt, kun je '
        'ook niet lekken. En je krijgt wachtwoord vergeten, tweestapsverificatie en '
        'beveiliging tegen misbruik er gratis bij.</p>'
        '<ol>'
        '<li><b>Open de Firebase-console</b> en kies je project.</li>'
        '<li><b>Ga naar Authentication en klik op Get started.</b></li>'
        '<li><b>Kies bij Sign-in method de provider Google</b> en zet hem aan. Vul een '
        'projectnaam en een support-mailadres in. Meer hoef je hier niet te doen.</li>'
        '<li><b>Controleer de toegestane domeinen.</b> Publiceer je via Firebase '
        'Hosting, dan staat dat er al; gebruik je een eigen domein, zet het erbij. '
        'Vergeet <code>localhost</code> niet als je lokaal test.</li>'
        '<li><b>Laat de inlogknop bouwen:</b> <i>"voeg Firebase Authentication met '
        'Google-inloggen toe: een inlogknop, een uitlogknop, en toon de naam van de '
        'ingelogde gebruiker. Gebruik de officiële Firebase-bibliotheek en leg uit wat '
        'elk stuk doet."</i></li>'
        '<li><b>Test met twee accounts.</b> Log in met je eigen account, en daarna in '
        'een privévenster met een ander account. Ziet gebruiker B de gegevens van '
        'gebruiker A? Dan kloppen je beveiligingsregels niet.</li>'
        '<li><b>Beperk wie mag inloggen als dat nodig is.</b> Wil je alleen collega’s '
        'toelaten, laat dan controleren op de domeinnaam van het mailadres — en zet '
        'dat ook in je beveiligingsregels, niet alleen in de app, want de app kan '
        'iemand omzeilen.</li>'
        '</ol>')

    p.aandacht(
        'De valkuil van Firebase: de database staat standaard open',
        '<p>Als je bij het opzetten van Firestore kiest voor de testmodus, staat je '
        'database een tijdlang <b>open voor iedereen op internet</b> — lezen én '
        'schrijven. Dat is bedoeld om snel te kunnen beginnen, en het is de meest '
        'voorkomende manier waarop met AI gebouwde toepassingen gegevens lekken.</p>'
        '<p>Wat je doet: kies de <b>productiemodus</b>, en laat daarna '
        'beveiligingsregels schrijven die vastleggen wie wat mag. Vraag: <i>"schrijf '
        'Firestore-beveiligingsregels waarbij alleen ingelogde gebruikers hun eigen '
        'gegevens kunnen lezen en schrijven, en leg per regel uit wat hij doet"</i>. '
        'Test daarna in de Firebase-console met de regelsimulator of een '
        'niet-ingelogde bezoeker er echt niet bij kan.</p>'
        '<p>En nogmaals hoofdstuk 6: zet geen persoonsgegevens in een zelfgebouwde '
        'toepassing zonder dat iemand met verstand van zaken ernaar heeft '
        'gekeken.</p>')

    p.tekst(
        'Alternatief: alleen publiceren, zonder achterkant',
        '<p>Heb je alleen een website of een pagina die niets hoeft te bewaren, dan '
        'heb je Firebase niet nodig. <b>GitHub Pages</b> is dan genoeg: je bestanden '
        'staan al in een repository, dus vraag je assistent om Pages aan te zetten en '
        'je krijgt een gratis URL. Geen server, geen kosten, geen '
        'beveiligingsregels.</p>')

    p.invulvelden(
        'Oefening: laat je werkplek inrichten en publiceer iets',
        '<p>Neem wat je in hoofdstuk 13 gebouwd hebt en breng het naar buiten. Laat zo '
        'veel mogelijk doen door je assistent.</p>',
        [
            ('p14-installed', 'Wat heeft je assistent geïnstalleerd, en wat ging er '
             'mis?',
             'Node, Git, gh, rtk, Firebase CLI — noteer de versienummers'),
            ('p14-zelf', 'Welke stappen moest je zelf doen? Hoe verliep het koppelen?',
             'Inloggen bij GitHub, Firebase, en je assistent'),
            ('p14-repo', 'Hoe heet je repository, en staat hij op private of public?',
             'En waarom die keuze?'),
            ('p14-commits', 'Beschrijf drie momenten waarop je een versie hebt '
             'vastgelegd.',
             'Wat had je net veranderd?'),
            ('p14-online', 'Waar staat het nu online? Via GitHub Pages of Firebase?',
             'Plak de URL'),
            ('p14-regels', 'Als je Firebase gebruikt: welke beveiligingsregels heb je '
             'ingesteld, en hoe heb je gecontroleerd dat ze werken?',
             'Getest met een tweede account in een privévenster?'),
            ('p14-terug', 'Heb je een keer een wijziging teruggedraaid? Hoe ging dat?',
             'Probeer het bewust een keer — dat is de hele reden voor versiebeheer'),
            ('p14-rtk', 'Wat laat "rtk gain" zien na een paar sessies?',
             'Leuk om te zien hoeveel het scheelt'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Bewaar de opdrachten die je het vaakst aan je assistent geeft in een eigen '
        'spiekbriefje — dat werkt beter dan commando’s onthouden.</p>')

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
                       'en laat beveiligingsregels schrijven vóór er echte gegevens in '
                       'komen.</p>',
            '_incorrect': {'final': '<p>Nog niet. Waar het om gaat is toegang: in '
                                    'testmodus staat je database open voor de hele '
                                    'wereld. Dat is precies de manier waarop '
                                    'zelfgebouwde toepassingen gegevens lekken.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
