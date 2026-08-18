# -*- coding: utf-8 -*-
"""Slim Word-, Excel- en PowerPoint-bestanden maken met AI."""


def bouw(p):
    p.tekst(
        'Vraag niet om een bestand, vraag om de inhoud',
        '<p>"Maak hier een Word-document van" is een verleidelijke opdracht. Beide '
        'platforms kunnen het: ChatGPT bouwt het bestand met code op de achtergrond, '
        'Claude doet hetzelfde. Het werkt. Maar het is bijna nooit de slimste '
        'route.</p>'
        '<p>Wat er gebeurt als je om een bestand vraagt: het model schrijft eerst de '
        'inhoud, schrijft dan een programma dat die inhoud in een documentformaat '
        'giet, voert dat uit, loopt tegen een foutje aan, herstelt dat, en levert een '
        'bestand op. Bij ChatGPT betekent dat vooral <b>wachten</b>. Bij Claude '
        'betekent het dat je flink wat tokens verbruikt aan machinerie in plaats van '
        'aan inhoud — en op een gesprekslimiet zit je daarna sneller vast.</p>'
        '<p>En het grootste bezwaar: wil je één alinea aanpassen, dan gaat het hele '
        'circus opnieuw.</p>')

    p.tekst(
        'De werkwijze die wél snel is: eerst Markdown',
        '<p>Laat het model de inhoud opleveren in <b>Markdown</b> — gewone tekst met '
        'een paar tekens voor opmaak. Dat is direct leesbaar in de chat, kost bijna '
        'geen extra tokens, en je kunt in twee seconden om een aanpassing vragen '
        'omdat er geen bestand herbouwd hoeft te worden.</p>'
        '<p>Pas als de inhoud klopt, zet jij hem om naar Word, Excel of PowerPoint. '
        'Dat kost je een minuut en je houdt de controle over de opmaak.</p>'
        '<p>Markdown is in vijf regels uitgelegd:</p>'
        '<ul>'
        '<li><code># Kop 1</code>, <code>## Kop 2</code>, <code>### Kop 3</code></li>'
        '<li><code>**vet**</code> en <code>*cursief*</code></li>'
        '<li><code>- </code> voor een opsomming, <code>1. </code> voor een genummerde '
        'lijst</li>'
        '<li><code>| kolom | kolom |</code> voor een tabel</li>'
        '<li><code>&gt; </code> voor een citaat</li>'
        '</ul>')

    p.tekst(
        'Andersom net zo belangrijk: wat je aanlevert',
        '<p>Dit geldt niet alleen voor wat je terugkrijgt, maar ook voor wat je '
        'erin stopt. Een AI leest niet elk bestandsformaat even goed. De volgorde, '
        'van makkelijk naar moeilijk:</p>'
        '<ol>'
        '<li><b>.md en .txt</b> — het makkelijkst. Platte tekst met hooguit een paar '
        'opmaaktekens. Er valt niets te reconstrueren, dus er gaat niets mis.</li>'
        '<li><b>Word (.docx)</b> — gaat prima. De structuur zit er netjes in.</li>'
        '<li><b>PDF</b> — het moeilijkst, met afstand.</li>'
        '</ol>'
        '<p>Waarom PDF zo lastig is: het is een <i>opmaak</i>formaat, geen '
        'tekstformaat. Er staat niet "dit is een kop en dit is een tabel", er staat '
        '"zet dit stukje tekst op deze positie". Kolommen lopen door elkaar, tabellen '
        'vallen uit elkaar, kop- en voetteksten belanden midden in een zin, en een '
        'gescande PDF is helemaal geen tekst maar een plaatje. Het model moet dat '
        'allemaal reconstrueren — dat kost extra tokens én het gaat vaker mis.</p>'
        '<p><b>De vuistregel: stop geen PDF in een gesprek als het niet hoeft.</b> Dat '
        'scheelt je zowel tokens als fouten.</p>'
        '<p>Heb je alleen een PDF? Laat er dan éérst een .md van maken en werk '
        'daarmee verder. Dan betaal je die reconstructie één keer in plaats van bij '
        'elke ronde, en je kunt zelf controleren of de omzetting klopt. Werk je met '
        'een map op je eigen schijf (hoofdstuk 12), laat je assistent dan alle PDF’s '
        'in één keer omzetten naar .md — daarna is de hele map lichter en '
        'betrouwbaarder.</p>')

    p.aandacht(
        'Markdown is de spil, in beide richtingen',
        '<p>Zie je het patroon? Markdown is niet alleen de handigste vorm om iets '
        '<i>uit</i> een gesprek te krijgen, het is ook de beste vorm om iets '
        '<i>in</i> te stoppen. Als je één werkgewoonte overhoudt uit dit hoofdstuk, is '
        'het deze: <b>werk in .md, en zet pas op het laatste moment om naar het '
        'formaat dat de ontvanger nodig heeft.</b></p>'
        '<p>Dat omzetten is nauwelijks werk. In Claude kun je een Markdown-artifact '
        'met één klik als PDF laten downloaden. Voor Word gebruik je de plakroute '
        'hieronder of Pandoc. En omdat de bron .md blijft, kun je op elk moment nog '
        'iets aanpassen zonder opnieuw te beginnen.</p>')

    p.tekst(
        'De harde grens: één antwoord kan maar zo lang zijn',
        '<p>Naast het contextvenster — hoeveel het model kan <i>lezen</i> — is er een '
        'tweede grens: hoeveel het in één antwoord kan <i>schrijven</i>. Die grens is '
        'veel lager dan mensen denken en is de reden dat grote klussen mislukken.</p>'
        '<p>Je herkent hem aan drie signalen:</p>'
        '<ul>'
        '<li>Het antwoord stopt <b>midden in een zin</b> of midden in een lijst.</li>'
        '<li>Het begin is uitgewerkt en het eind wordt <b>steeds beknopter</b> — de '
        'laatste hoofdstukken zijn ineens drie bullets.</li>'
        '<li>Er staat iets als "en zo verder voor de overige onderdelen".</li>'
        '</ul>'
        '<p>Let op: de <b>kwaliteit zakt ruim voordat de limiet bereikt is</b>. Een '
        'model dat aan één stuk door een compleet rapport moet produceren, wordt in '
        'de tweede helft merkbaar oppervlakkiger. Wachten tot het afbreekt is dus te '
        'laat — je wil de klus opknippen voordat je in de buurt komt.</p>'
        '<p>De oplossing is niet "vraag om een langer antwoord". De oplossing is een '
        'andere werkvorm kiezen. Er zijn er vijf, en het onderscheid ertussen is wat '
        'dit hoofdstuk je moet opleveren.</p>')

    p.accordeon(
        'Vijf werkvormen voor werk dat niet in één antwoord past',
        '<p>Ze sluiten elkaar niet uit — je gebruikt ze vaak achter elkaar. Maar kies '
        'bewust, want de verkeerde werkvorm kost je een middag.</p>',
        [
            {'title': '1. In fases werken — als de inhoud nog moet ontstaan',
             'body': '<p>Eerst de inhoudsopgave, die keur je goed. Dan per hoofdstuk '
                     'de uitwerking, in een apart antwoord. Elk antwoord blijft ruim '
                     'binnen de limiet en houdt zijn kwaliteit vast.</p>'
                     '<p><b>Herken je aan:</b> je weet nog niet precies wat er in moet '
                     'komen. Een rapport, een advies, een plan.</p>'
                     '<p><b>Waarom dit werkt:</b> je corrigeert de structuur voordat er '
                     'tienduizend tekens omheen zijn geschreven. Een verkeerde '
                     'indeling ontdekken bij hoofdstuk 7 is duur.</p>'
                     '<p><b>Valkuil:</b> in latere fases vergeet het model afspraken '
                     'uit eerdere. Herhaal de kernafspraken kort per fase, of gebruik '
                     'werkvorm 3.</p>'},
            {'title': '2. Canvas of artifact — als één stuk tekst blijft veranderen',
             'body': '<p>Claude noemt het een <b>artifact</b>, ChatGPT een '
                     '<b>canvas</b>: de tekst komt in een apart venster naast het '
                     'gesprek te staan, en je laat er gericht stukken in wijzigen '
                     'zonder dat het geheel opnieuw geschreven wordt.</p>'
                     '<p><b>Herken je aan:</b> één document, veel rondes. Een '
                     'projectvoorstel dat vijf keer langs de opdrachtgever gaat.</p>'
                     '<p><b>Waarom dit werkt:</b> je omzeilt de outputlimiet niet, '
                     'maar je hoeft hem per ronde ook niet meer op te zoeken — alleen '
                     'de wijziging gaat heen en weer in plaats van de hele tekst.</p>'
                     '<p><b>Onderscheid met fases:</b> fases zijn voor tekst die nog '
                     'moet ontstaan, canvas is voor tekst die er al is en beter '
                     'moet.</p>'},
            {'title': '3. In een project met bronbestanden — als de context groot is',
             'body': '<p>De context (huisstijl, richtlijnen, bronmateriaal, eerdere '
                     'stukken) staat vast in het project en hoeft niet in elk gesprek '
                     'herhaald te worden. Elk antwoord kan daardoor volledig aan de '
                     'inhoud besteed worden.</p>'
                     '<p><b>Herken je aan:</b> je merkt dat je in elke ronde dezelfde '
                     'uitleg opnieuw meestuurt, of dat het model afspraken '
                     'kwijtraakt.</p>'
                     '<p><b>Waarom dit werkt:</b> het lost het probleem aan de '
                     '<i>invoerkant</i> op. Dat maakt het antwoord niet langer, maar '
                     'wel beter besteed — en het houdt latere fases scherp.</p>'
                     '<p><b>Onderscheid:</b> gebruik dit náást fases of canvas, niet '
                     'in plaats daarvan. Zie hoofdstuk 7.</p>'},
            {'title': '4. In bestanden op je eigen schijf — als het echt groot is',
             'body': '<p>De AI schrijft niet in een chatvenster maar rechtstreeks naar '
                     'bestanden in je werkmap: hoofdstuk voor hoofdstuk, bestand voor '
                     'bestand. Er is dan <b>geen limiet meer per stuk</b>, want elk '
                     'bestand is een eigen antwoord.</p>'
                     '<p><b>Herken je aan:</b> het eindresultaat bestaat uit meerdere '
                     'onderdelen. Een handleiding met tien hoofdstukken, een reeks '
                     'documenten, een website.</p>'
                     '<p><b>Waarom dit werkt:</b> je hoeft niets meer te plakken, je '
                     'ziet per bestand of het klopt, en je kunt één onderdeel opnieuw '
                     'laten doen zonder de rest aan te raken.</p>'
                     '<p><b>Nodig:</b> hoofdstuk 12, plus versiebeheer uit hoofdstuk '
                     '14 zodat je elke stap kunt terugdraaien.</p>'},
            {'title': '5. Een generator bouwen — als het geheel zich herhaalt',
             'body': '<p>De zwaarste en meest lonende vorm: je laat niet het '
                     'eindproduct maken, maar het <b>ding dat het eindproduct '
                     'maakt</b>. De inhoud staat in losse bronbestanden, en een '
                     'zelfgeschreven programmaatje bouwt daar het geheel van.</p>'
                     '<p><b>Herken je aan:</b> veel onderdelen met dezelfde vorm. Een '
                     'website, een cursus, honderd persoonlijke brieven, een '
                     'rapportage die elke maand terugkomt.</p>'
                     '<p><b>Waarom dit werkt:</b> de outputlimiet verdwijnt volledig '
                     'uit beeld. Je kunt één onderdeel wijzigen en het geheel in '
                     'seconden opnieuw laten bouwen — zonder dat er ook maar iets '
                     'opnieuw gegenereerd hoeft te worden.</p>'
                     '<p><b>Voorbeeld:</b> precies zo is deze cursus gemaakt. Elk '
                     'hoofdstuk is een bronbestand; één commando bouwt er de hele '
                     'e-learning van. Zie hoofdstuk 13 en 14.</p>'},
        ])

    p.tekst(
        'Welke werkvorm wanneer',
        '<p>Kort samengevat, zodat je niet hoeft te gokken:</p>'
        '<ul>'
        '<li><b>Eén stuk, inhoud moet nog ontstaan</b> → in fases (1)</li>'
        '<li><b>Eén stuk, bestaat al, moet beter</b> → canvas of artifact (2)</li>'
        '<li><b>Steeds dezelfde context nodig</b> → project met bronbestanden (3), '
        'naast 1 of 2</li>'
        '<li><b>Meerdere onderdelen, eenmalig</b> → in bestanden op je schijf (4)</li>'
        '<li><b>Meerdere onderdelen, herhaalt zich</b> → bouw een generator (5)</li>'
        '</ul>'
        '<p>De fout die het vaakst gemaakt wordt: werkvorm 1 of 2 gebruiken voor iets '
        'dat eigenlijk 4 of 5 is. Je merkt dat doordat je steeds langere prompts typt '
        'en steeds meer zit te plakken. Dat is het signaal om over te stappen, niet om '
        'harder je best te doen.</p>')

    p.tekst(
        'Stappenplan: van prompt naar Word-document met huisstijl',
        '<ol>'
        '<li><b>Vraag om Markdown, expliciet.</b> Zet in je prompt: <i>"Lever de '
        'tekst in Markdown, met koppen. Maak geen bestand aan."</i> Zonder die '
        'laatste zin gaat het model soms alsnog bouwen.</li>'
        '<li><b>Werk de inhoud af in de chat.</b> Bijsturen, inkorten, herschrijven. '
        'Dit is de fase waarin het snel moet gaan, en met Markdown gaat het snel.</li>'
        '<li><b>Selecteer het antwoord in het chatvenster en kopieer het.</b> Let op: '
        'kopieer de <i>weergegeven</i> tekst, niet de ruwe Markdown. De koppen, vette '
        'tekst en lijsten zitten dan al in het plakbord.</li>'
        '<li><b>Open je eigen Word-sjabloon</b> — dus niet een leeg document, maar het '
        'sjabloon met jullie huisstijl.</li>'
        '<li><b>Plak met "Alleen tekst behouden" of "Opmaak van bestemming '
        'gebruiken".</b> Rechtermuisknop bij het plakken. Zo neemt de tekst de stijlen '
        'van jouw sjabloon over in plaats van die van de chat.</li>'
        '<li><b>Loop de koppen na</b> en wijs waar nodig de juiste stijl toe. Klaar; '
        'je hebt een document in huisstijl in plaats van een generiek '
        'AI-bestand.</li>'
        '</ol>')

    p.accordeon(
        'Per bestandssoort: wat werkt het beste',
        '<p>De aanpak verschilt per formaat.</p>',
        [
            {'title': 'Word — via Markdown, of via Pandoc',
             'body': '<p>De plakroute hierboven werkt voor 95% van de gevallen. Doe je '
                     'dit vaak, of gaat het om lange documenten, dan is <b>Pandoc</b> '
                     'de moeite waard: een gratis programma dat Markdown omzet naar '
                     'Word.</p>'
                     '<p>Bewaar het antwoord als <code>stuk.md</code> en draai:</p>'
                     '<p><code>pandoc stuk.md -o stuk.docx '
                     '--reference-doc=sjabloon.docx</code></p>'
                     '<p>Met <code>--reference-doc</code> neemt hij de stijlen van '
                     'jouw eigen Word-sjabloon over. Eén keer instellen, daarna elke '
                     'keer een document in huisstijl in één regel.</p>'},
            {'title': 'Excel — vraag om CSV, niet om xlsx',
             'body': '<p>Voor tabellen met gegevens: laat het model <b>CSV</b> '
                     'opleveren (komma- of puntkommagescheiden tekst). Dat plak of '
                     'importeer je in Excel, en dan heb je meteen echte cellen.</p>'
                     '<p>Voor berekeningen: laat het model de <b>formules</b> geven in '
                     'plaats van de uitkomsten. Dan blijft je bestand rekenen als de '
                     'invoer verandert, en kun je controleren wat er gebeurt.</p>'
                     '<p>Alleen voor echt complexe werkboeken — meerdere tabbladen, '
                     'opmaak, grafieken — laat je het model het bestand zelf bouwen. '
                     'Wees dan geduldig.</p>'},
            {'title': 'PowerPoint — outline eerst, opmaak later',
             'body': '<p>Vraag om een <b>outline in Markdown</b>: per slide een kop en '
                     'drie tot vijf bullets, plus een notitie voor de spreker. Die '
                     'werk je af in de chat.</p>'
                     '<p>Daarna kun je in PowerPoint via Beeld → Overzicht een '
                     'kopstructuur plakken en heb je in één klap je slides, in jouw '
                     'sjabloon. Dat scheelt de strijd met een AI-gegenereerd deck dat '
                     'niet in jullie huisstijl staat.</p>'
                     '<p>Een deck echt láten ontwerpen door AI is wel de moeite waard '
                     'als het eenmalig is en er geen huisstijl aan te pas komt.</p>'},
            {'title': 'PDF — nooit als eindformaat uit AI',
             'body': '<p>Laat AI geen PDF maken. Maak je Word- of PowerPoint-bestand '
                     'op de manier hierboven en exporteer zelf naar PDF. Dan klopt de '
                     'opmaak, zijn de koppen doorzoekbaar en blijft het document '
                     'toegankelijk.</p>'},
        ])

    p.aandacht(
        'Wanneer je het model wél het bestand laat maken',
        '<p>Er zijn drie gevallen waarin het de moeite loont: een <b>complex '
        'werkboek</b> met meerdere tabbladen en formules, een <b>eenmalig</b> '
        'document waar geen huisstijl bij hoort, en werk waarbij het model het '
        'resultaat <b>zelf moet kunnen controleren</b> — bijvoorbeeld een grafiek '
        'waar hij naar moet kijken om te zien of hij klopt. In alle andere gevallen '
        'ben je met Markdown sneller klaar.</p>')

    p.tekst(
        'Nog vier tips',
        '<ul>'
        '<li><b>Laat lange stukken in een apart werkvenster schrijven.</b> Claude '
        'noemt dat een artifact, ChatGPT een canvas. Je krijgt een tekst naast het '
        'gesprek die je gericht kunt laten bijwerken zonder dat alles opnieuw '
        'gegenereerd wordt.</li>'
        '<li><b>Geef een bestaand document als voorbeeld mee.</b> "Schrijf in de stijl '
        'en structuur van dit eerdere rapport" is de snelste route naar iets dat bij '
        'jullie past.</li>'
        '<li><b>Laat de inhoudsopgave eerst maken.</b> Bij een langer stuk: eerst de '
        'structuur goedkeuren, dan per hoofdstuk uitwerken. Voorkomt dat je een '
        'compleet document weggooit omdat de indeling niet klopt.</li>'
        '<li><b>Controleer altijd cijfers, bronnen en namen</b> voordat het document '
        'de deur uitgaat. Ook — juist — als het er professioneel uitziet.</li>'
        '</ul>')

    p.invulvelden(
        'Oefening: hetzelfde stuk, twee routes',
        '<p>Neem een document dat je toch moest maken. Doe het één keer door om een '
        'kant-en-klaar bestand te vragen, en één keer via Markdown. Klok allebei.</p>',
        [
            ('p10-route-a', 'Route A — direct om een bestand vragen. Hoe lang duurde '
             'het, en hoe beviel het resultaat?',
             'Let op wachttijd en op of de opmaak klopte'),
            ('p10-route-b', 'Route B — Markdown, daarna zelf omzetten. Hoe lang '
             'duurde het?',
             'Inclusief de tijd die je kwijt was aan plakken en stijlen'),
            ('p10-wijziging', 'Vraag in beide routes één alinea te herschrijven. Wat '
             'is het verschil?',
             'Dit is waar het onderscheid meestal het grootst is'),
            ('p10-keuze', 'Welke route ga jij standaard gebruiken, en wanneer wijk je '
             'daarvan af?',
             'Schrijf je eigen vuistregel op'),
        ])

    p.knoppenrij('Meenemen', '<p>Zet je vuistregel in je projectinstructies, dan hoef je het niet elke keer '
        'te herhalen.</p>')

    p.vraag(
        'Even checken',
        'Je schrijft een rapport dat in jullie huisstijl moet, en je verwacht nog '
        'meerdere inhoudelijke aanpassingen. Wat is de handigste aanpak?',
        [
            ('De inhoud in Markdown laten opleveren, in de chat afwerken, en pas aan '
             'het eind in je eigen Word-sjabloon plakken.', True),
            ('Meteen om een Word-bestand vragen en dat telkens opnieuw laten '
             'genereren.', False),
            ('Om een PDF vragen, dan staat de opmaak vast.', False),
            ('De tekst in stukjes in de chat laten schrijven en zelf overtypen.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. Zolang de inhoud nog beweegt, wil je geen bestand — '
                       'elke ronde zou een nieuwe build kosten. Bestand maken is de '
                       'laatste stap, niet de eerste.</p>',
            '_incorrect': {'final': '<p>Nog niet. De vraag is wanneer je vastlegt in '
                                    'een bestandsformaat. Doe je dat te vroeg, dan '
                                    'betaal je elke tekstwijziging met een complete '
                                    'herbouw — en bij een PDF ben je de opmaak '
                                    'bovendien kwijt.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
