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

    p.knoppenrij('Meenemen', '<p>Zet je vuistregel in je project of custom GPT, dan hoef je het niet elke keer te herhalen.</p>')

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
