# -*- coding: utf-8 -*-
"""Projecten als herhaalprompt, de prompt optimizer, en de grenzen van Claude Projects."""


def bouw(p):
    p.tekst(
        'Een project is een herhaalprompt',
        '<p>Als je je uitleg over de organisatie, de doelgroep en de huisstijl voor de '
        'derde keer intypt, ben je iets verkeerd aan het doen. Daar zijn projecten '
        'voor. Zie het niet als "een eigen assistent bouwen" — dat klinkt groter dan '
        'het is. Zie het als een <b>herhaalprompt</b>: het vaste deel van je prompt '
        'leg je één keer vast, en elk gesprek dat je erin start begint met die kennis '
        'al aanwezig.</p>'
        '<p>Wat overblijft om te typen is alleen nog de <i>taak</i>. Dat scheelt niet '
        'alleen tijd; het maakt je resultaten ook consistenter, omdat de context niet '
        'elke keer net iets anders geformuleerd is.</p>')

    p.aandacht(
        'Custom GPT’s: nieuwe maken kan niet meer op een persoonlijk account',
        '<p>Belangrijk om te weten voordat je ernaar gaat zoeken: op een persoonlijk '
        'ChatGPT-account — Free, Go, Plus of Pro — kun je <b>geen nieuwe custom GPT '
        'meer aanmaken of publiceren</b>. Dat is verplaatst naar de zakelijke '
        'omgevingen. Bestaande GPT’s blijven wel gewoon werken, en je kunt ze blijven '
        'gebruiken.</p>'
        '<p>Voor ons betekent dat: <b>projecten zijn de route</b>, bij zowel Claude als '
        'ChatGPT. En waar iemand een bruikbare custom GPT heeft die nog bestaat, '
        'gebruik je die gewoon — zoals de prompt optimizer hieronder.</p>')

    p.tekst(
        'Leer eerst de prompt optimizer gebruiken',
        '<p>Binnen ons team is er een custom GPT die je prompts en instructies '
        'aanscherpt: de <b>prompt optimizer</b>. Die is nog steeds bereikbaar en '
        'bruikbaar, en hij is precies het gereedschap dat je nodig hebt vóórdat je een '
        'project inricht.</p>'
        '<p>Waarom eerst de optimizer en dan pas het project: de instructies die je in '
        'een project zet, gebruik je maandenlang in élk gesprek. Een slordige '
        'formulering werkt daar dus honderd keer door. Het loont om er tien minuten in '
        'te steken met een hulpmiddel dat weet waar goede instructies aan moeten '
        'voldoen.</p>'
        '<p><b>Zo gebruik je hem:</b></p>'
        '<ol>'
        '<li><b>Open de prompt optimizer</b> in ChatGPT. Staat hij nog niet in je '
        'zijbalk, vraag de link op bij Fabian en zet hem daarna vast, zodat je hem '
        'terugvindt.</li>'
        '<li><b>Plak je ruwe versie erin.</b> Nog niet netjes maken — juist de rommelige '
        'versie levert de beste vragen op. Zeg erbij waar het voor is: <i>"dit worden '
        'de vaste instructies van een project, niet een losse prompt"</i>.</li>'
        '<li><b>Beantwoord de vragen die hij stelt.</b> Dat is het waardevolste deel: '
        'dat zijn de gaten die jij niet zag.</li>'
        '<li><b>Vraag om de instructies in delen.</b> Rol, gebruiker en kennisniveau, '
        'context, standaard outputvorm, grenzen — de bouwstenen uit hoofdstuk 4, maar '
        'zonder de taak. Die verschilt immers per gesprek.</li>'
        '<li><b>Test het resultaat in een leeg gesprek</b> voordat je het in je project '
        'zet. Werkt het daar niet, dan werkt het in je project ook niet.</li>'
        '<li><b>Zet de uitkomst in je projectinstructies</b> en bewaar de ruwe versie '
        'ergens, zodat je later kunt zien wat je precies veranderd hebt.</li>'
        '</ol>')

    p.tekst(
        'Delen doe je met een .md-bestand',
        '<p>Nu je een custom GPT niet meer kunt delen, is er een betere manier die '
        'bovendien overal werkt: <b>je deelt de configuratie zelf, als '
        'Markdown-bestand.</b></p>'
        '<p>Waarom dat beter is dan een gedeelde assistent:</p>'
        '<ul>'
        '<li>Het werkt bij Claude én ChatGPT — de ontvanger plakt het in zijn eigen '
        'project, waar hij ook werkt.</li>'
        '<li>Het is leesbaar. Je collega ziet precies wat er in staat en kan het '
        'aanpassen aan zijn situatie.</li>'
        '<li>Je kunt het in versiebeheer zetten, zodat je ziet wat er wanneer '
        'veranderd is.</li>'
        '<li>Markdown is precies het formaat dat een AI het beste leest — zie '
        'hoofdstuk 10.</li>'
        '</ul>'
        '<p><b>Zo maak je er een:</b></p>'
        '<ol>'
        '<li><b>Typ brainstormend precies op wat je wilt.</b> Niet netjes, niet in '
        'volzinnen. Gewoon alles wat in je hoofd zit: wat de assistent moet doen, voor '
        'wie, in welke toon, wat hij vooral niet moet doen, waar je aan denkt als het '
        'goed gaat. Hoe meer rommelige input, hoe beter het eindresultaat.</li>'
        '<li><b>Geef dat aan de prompt optimizer</b> met de opdracht: <i>"maak hier '
        'een complete configuratie van voor een AI-assistent, in '
        'Markdown-format, met koppen per onderdeel: rol, doelgroep, context, '
        'werkwijze, outputvorm, en wat er niet mag. Stel me eerst de vragen die je '
        'nodig hebt."</i></li>'
        '<li><b>Beantwoord zijn vragen</b> en laat de configuratie uitschrijven.</li>'
        '<li><b>Sla hem op als .md-bestand</b> met een duidelijke naam, bijvoorbeeld '
        '<code>assistent-projectverslagen.md</code>.</li>'
        '<li><b>Gebruik hem zelf:</b> plak de inhoud in je projectinstructies, of voeg '
        'het bestand toe aan je projectbestanden.</li>'
        '<li><b>Deel het bestand met collega’s.</b> Zij plakken het in hun eigen '
        'project en werken meteen op dezelfde manier — zonder dat iemand een assistent '
        'hoeft te beheren.</li>'
        '<li><b>Zet er bovenin een datum en een eigenaar in.</b> Een gedeeld bestand '
        'zonder eigenaar veroudert stilletjes.</li>'
        '</ol>')

    p.tekst(
        'Stappenplan: een Claude Project opzetten',
        '<ol>'
        '<li><b>Open claude.ai en klik in de linkerkolom op Projects, daarna op nieuw '
        'project.</b> Geef het een naam die zegt waar het over gaat, niet "Test".</li>'
        '<li><b>Zet de instructies erin</b> die je met de prompt optimizer hebt '
        'gemaakt. Let op: rol, wie jij bent, context, standaard outputvorm en de '
        'grenzen — de taak laat je weg.</li>'
        '<li><b>Voeg bronbestanden toe.</b> Richtlijnen, een huisstijlgids, drie '
        'voorbeelden van goed werk, veelgestelde vragen. Liever vijf goede bestanden '
        'dan vijftig middelmatige: alles wat erin zit, telt mee en concurreert om '
        'aandacht.</li>'
        '<li><b>Test met een echte taak.</b> Start een gesprek in het project en geef '
        'alléén de taak. Krijg je een antwoord dat de context al kent, dan staat het '
        'goed.</li>'
        '<li><b>Scherp de instructies aan op wat er misging</b> — maar lees eerst de '
        'waarschuwing hieronder over te veel sturen.</li>'
        '<li><b>Zet er een datum en een eigenaar in.</b> "Laatst bijgewerkt: … , '
        'beheerd door: …". Anders staat er over een jaar verouderd beleid in dat '
        'niemand meer durft aan te raken.</li>'
        '</ol>')

    p.aandacht(
        'De belangrijkste beperking van Claude Projects: te veel sturen loopt dood',
        '<p>Dit is de valkuil waar de meeste mensen in trappen, en hij is '
        'contra-intuïtief. Als je Claude in een project <b>te strak stuurt met '
        'gedetailleerde, dwingende instructies</b>, wordt het resultaat niet beter maar '
        'slechter. Het loopt vast: korte, houterige antwoorden, of eindeloos '
        'terugvallen op de instructies in plaats van op je vraag.</p>'
        '<p>Wat je ziet gebeuren:</p>'
        '<ul>'
        '<li>Je stapelt regel op regel omdat er telkens iets niet goed ging.</li>'
        '<li>De instructies worden een reeks verboden: "doe nooit…", "gebruik nooit…", '
        '"begin nooit met…".</li>'
        '<li>Het model besteedt zijn aandacht aan het naleven van jouw regels in plaats '
        'van aan je vraag, en gaat op alles slag om de arm houden.</li>'
        '</ul>'
        '<p><b>Wat wel werkt:</b></p>'
        '<ol>'
        '<li><b>Schrijf kaders, geen script.</b> Beschrijf de situatie en wat "goed" '
        'betekent; laat de aanpak aan het model. Een stap-voor-stap voorschrift voor '
        'denkwerk maakt het resultaat aantoonbaar slechter.</li>'
        '<li><b>Zeg wat je wél wilt.</b> "Schrijf beknopt en concreet" stuurt beter dan '
        'drie regels over wat niet mag.</li>'
        '<li><b>Geef voorbeelden in plaats van regels.</b> Twee goede voorbeeldteksten '
        'in de bestanden doen meer dan een pagina uitleg over de stijl.</li>'
        '<li><b>Houd het kort.</b> Loopt je instructie tegen de duizend woorden, snoei '
        'dan. Vraag de prompt optimizer: <i>"welke van deze instructies zijn overbodig '
        'of spreken elkaar tegen?"</i></li>'
        '<li><b>Ruim op na elke aanscherping.</b> Voeg je een regel toe, kijk dan of er '
        'een oude weg kan. Anders groeit je instructie alleen maar.</li>'
        '</ol>'
        '<p>Loopt het toch vast: begin een nieuw project met alleen de helft van de '
        'instructies. Dat is meestal sneller dan blijven bijschaven.</p>')

    p.tekst(
        'Stappenplan: een ChatGPT Project opzetten',
        '<ol>'
        '<li><b>Klik in het zijmenu op Projecten en maak een nieuw project aan.</b></li>'
        '<li><b>Vul de projectinstructies in</b> — dezelfde inhoud als bij Claude, '
        'gemaakt met de prompt optimizer.</li>'
        '<li><b>Voeg bestanden toe</b> die in elk gesprek beschikbaar moeten zijn.</li>'
        '<li><b>Start je gesprekken voortaan binnen het project</b> in plaats van in '
        'een los venster. Dat is de stap die mensen vergeten: een project werkt alleen '
        'als je er ook echt in werkt.</li>'
        '<li><b>Houd projecten gescheiden per onderwerp.</b> Eén project dat alles '
        'moet kunnen, doet alles half — precies hetzelfde probleem als een te lange '
        'instructie.</li>'
        '</ol>')

    p.aandacht(
        'Wat je niet in projectbestanden zet',
        '<p>Alles wat in een project zit, kan in een antwoord terugkomen. Dus: geen '
        'persoonsgegevens, geen niet-gepubliceerde cijfers, geen contracten, geen '
        'inloggegevens. Wel: richtlijnen, publieke documenten, voorbeeldteksten, '
        'sjablonen. Zie hoofdstuk 6.</p>')

    p.invulvelden(
        'Oefening: van ruwe prompt naar werkend project',
        '<p>Neem de opdracht die je in hoofdstuk 3 hebt gekozen en de prompt uit '
        'hoofdstuk 5. Laat die eerst door de prompt optimizer gaan en zet hem daarna in '
        'een project. Maak het project ook echt aan.</p>',
        [
            ('p07-naam', 'Naam van je project',
             'Iets waaruit blijkt waar het over gaat'),
            ('p07-optimizer', 'Welke vragen stelde de prompt optimizer, en wat heb je '
             'daardoor toegevoegd?',
             'Dit zijn de gaten die je zelf niet zag'),
            ('p07-instructies', 'De vaste instructies (zonder de taak)',
             'Rol, wie jij bent, context, standaard outputvorm, grenzen'),
            ('p07-lengte', 'Hoeveel woorden zijn je instructies geworden? Wat heb je '
             'geschrapt om ze korter te maken?',
             'Boven de duizend woorden: snoeien'),
            ('p07-bestanden', 'Welke bronbestanden voeg je toe?',
             'Noem er drie tot vijf — en check of ze gedeeld mogen worden'),
            ('p07-nietweten', 'Wat moet het project doen als het iets niet weet?',
             'Schrijf de exacte zin die je in de instructies zet'),
            ('p07-md', 'Heb je je configuratie als .md opgeslagen? Onder welke '
             'naam, en met wie deel je hem?',
             'Vergeet de datum en eigenaar bovenin niet'),
            ('p07-test', 'Wat ging er mis bij de eerste test, en wat heb je aangepast?',
             'Vul in nadat je het project hebt gemaakt'),
            ('p07-dood', 'Merkte je dat het vastliep door te veel sturing? Wat heb je '
             'weggehaald?',
             'Vaak is minder instructie het antwoord'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Zet meteen een herinnering over drie maanden om je instructies na te '
        'lopen — en dan vooral om erin te snoeien.</p>')

    p.vraag(
        'Even checken',
        'Je Claude Project geeft steeds kortere, houterige antwoorden en valt telkens '
        'terug op je instructies in plaats van op je vraag. Wat is de meest '
        'waarschijnlijke oorzaak?',
        [
            ('De instructies zijn te lang en te dwingend geworden — het model besteedt '
             'zijn aandacht aan het naleven van regels in plaats van aan je vraag. '
             'Snoeien helpt.', True),
            ('Er zitten te weinig bronbestanden in het project.', False),
            ('Je gebruikt een te licht model; zet het zwaarste model aan.', False),
            ('Het contextvenster is vol; begin elke dag een nieuw project.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Dit is de klassieke fout: elke keer dat er iets '
                       'misging is er een regel bij gekomen, en die stapel werkt nu '
                       'tegen je. Schrijf kaders in plaats van een script, vervang '
                       'verboden door voorbeelden, en haal weg wat je niet kunt '
                       'uitleggen.</p>',
            '_incorrect': {'final': '<p>Nog niet. Méér toevoegen — bestanden, een '
                                    'zwaarder model — verergert dit meestal. Het '
                                    'patroon van korte, houterige antwoorden die '
                                    'blijven verwijzen naar je regels, wijst op te veel '
                                    'en te dwingende instructie.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
