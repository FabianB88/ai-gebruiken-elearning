# -*- coding: utf-8 -*-
"""Van een prompt die werkt naar een prompt die blijft werken."""


def bouw(p):
    p.tekst(
        'De eerste prompt is nooit de goede',
        '<p>Vrijwel niemand schrijft in één keer de juiste prompt. Dat hoeft ook '
        'niet. Het verschil tussen mensen die veel uit AI halen en mensen die het '
        '"wel aardig" vinden, zit niet in hun eerste prompt maar in wat ze doen met '
        'het teleurstellende antwoord dat erop volgt.</p>'
        '<p>De verkeerde reactie: de prompt weggooien en een nieuwe verzinnen. De '
        'goede reactie: benoemen wat er mis was en dat toevoegen. Elke ronde maakt de '
        'prompt beter, en die prompt hergebruik je de rest van het jaar.</p>')

    p.tekst(
        'Bijsturen in plaats van opnieuw beginnen',
        '<p>Je zit in een gesprek. Het model heeft het hele gesprek nog in beeld. Dat '
        'betekent dat je kunt corrigeren op wat er staat, in plaats van alles opnieuw '
        'te formuleren. Vier zinnen die bijna altijd werken:</p>'
        '<ul>'
        '<li><b>"Te algemeen. Maak het specifiek voor [situatie], en haal alles weg '
        'dat voor elke organisatie zou gelden."</b> — de meest voorkomende klacht, '
        'met de directe oplossing erbij.</li>'
        '<li><b>"Dit is te lang. Breng het terug naar de helft en behoud alleen wat '
        'de lezer nodig heeft om te beslissen."</b> — vertel waaróp je snijdt, anders '
        'schrapt het model willekeurig.</li>'
        '<li><b>"Alinea 2 klopt niet, want [reden]. Herschrijf alleen die alinea."</b> '
        '— begrens de herschrijving, anders verandert de rest ook en ben je het goede '
        'stuk kwijt.</li>'
        '<li><b>"Wat heb je van mij nodig om dit beter te maken?"</b> — als je zelf '
        'niet scherp krijgt wat er ontbreekt.</li>'
        '</ul>')

    p.aandacht(
        'Werkt het na drie rondes nog niet? Begin schoon opnieuw',
        '<p>Een gesprek dat de verkeerde kant op is gegaan, trek je zelden meer recht: '
        'alle mislukte pogingen staan nog in de context en sturen mee. Kopieer wat je '
        'geleerd hebt naar een verbeterde prompt en open een nieuw gesprek. Dat is '
        'sneller dan doorploeteren.</p>')

    p.tekst(
        'Laat het model je prompt schrijven',
        '<p>Dit is de meest onderbenutte techniek die er is. Een taalmodel weet '
        'uitstekend hoe een goede prompt voor een taalmodel eruitziet. Vraag het '
        'gewoon.</p>'
        '<p>Plak deze tekst, met jouw ruwe verzoek erachter:</p>'
        '<blockquote><p><i>"Hieronder staat een prompt die ik wil gebruiken. Verbeter '
        'hem. Let op: ontbrekende context, een onduidelijke taak, een ontbrekende '
        'outputvorm, en ontbrekende grenzen. Stel me eerst maximaal vijf vragen over '
        'wat je nog niet weet, en schrijf daarna de verbeterde prompt uit. Leg kort '
        'uit wat je hebt veranderd en waarom."</i></p></blockquote>'
        '<p>De vijf vragen zijn het belangrijkste deel. Dat zijn precies de gaten die '
        'jij niet zag. Beantwoord ze en je hebt in twee minuten een prompt van een '
        'niveau waar je zelf een halfuur over had gedaan.</p>')

    p.tekst(
        'Stappenplan: een prompt in vijf rondes goed krijgen',
        '<p>Gebruik dit voor een prompt die je vaker gaat gebruiken. Voor een losse '
        'vraag is het overkill.</p>'
        '<ol>'
        '<li><b>Ronde 1 — draai je ruwe prompt.</b> Nog niet perfectioneren; je wil '
        'zien waar het misgaat.</li>'
        '<li><b>Ronde 2 — benoem wat er mis is in gewone taal.</b> "Te generiek", "te '
        'formeel", "mist het financiële deel". Laat het model corrigeren.</li>'
        '<li><b>Ronde 3 — laat het model je prompt herschrijven</b> met de tekst '
        'hierboven. Beantwoord de vragen die het stelt.</li>'
        '<li><b>Ronde 4 — test de verbeterde prompt in een nieuw, leeg gesprek.</b> '
        'Dit is essentieel: in het oude gesprek staat alle context nog, waardoor je '
        'niet weet of de prompt zelf goed is of dat het gesprek het werk doet.</li>'
        '<li><b>Ronde 5 — draai hem drie keer met verschillende invoer.</b> Blijft de '
        'kwaliteit overeind, dan is hij klaar om vast te leggen. Zo niet, dan weet je '
        'nu welk stuk nog te vaag is.</li>'
        '</ol>')

    p.accordeon(
        'Zeven fouten die iedereen maakt',
        '<p>Herken je er drie of meer, dan zit daar je grootste winst.</p>',
        [
            {'title': '1. Te weinig context, te veel instructie',
             'body': '<p>Mensen schrijven vijf regels over hoe het antwoord eruit moet '
                     'zien en nul regels over de situatie. Draai de verhouding om. '
                     'Context is waar het model het van moet hebben.</p>'},
            {'title': '2. Meerdere taken in één prompt',
             'body': '<p>"Analyseer dit rapport, schrijf een samenvatting, maak een '
                     'presentatie en stel een mail op." Je krijgt vier halve '
                     'resultaten. Doe ze na elkaar in hetzelfde gesprek — de context '
                     'blijft toch staan.</p>'},
            {'title': '3. Vragen om een oordeel zonder maatstaf',
             'body': '<p>"Is dit een goed plan?" krijgt altijd een positief antwoord '
                     'met wat kanttekeningen. Vraag in plaats daarvan: "beoordeel dit '
                     'plan op haalbaarheid binnen zes maanden met twee fte, en noem '
                     'de drie grootste risico’s". Geef de maatstaf, anders verzint '
                     'het model er een.</p>'},
            {'title': '4. Blijven hangen in beleefdheid',
             'body': '<p>"Zou je misschien kunnen kijken of…" verzwakt de opdracht. '
                     'Wees direct: "analyseer", "schrijf", "vergelijk". Geen '
                     'onbeleefdheid, gewoon duidelijkheid.</p>'},
            {'title': '5. Het eerste antwoord accepteren',
             'body': '<p>Het eerste antwoord is een concept. Vraag standaard: "wat zou '
                     'je hieraan verbeteren als je nog een ronde had?" Dat kost één '
                     'zin en levert vaak een merkbaar beter stuk.</p>'},
            {'title': '6. Geen enkel voorbeeld geven',
             'body': '<p>Eén voorbeeld van hoe het eruit moet zien, stuurt sterker dan '
                     'drie alinea’s beschrijving. Heb je een eerdere versie die goed '
                     'was, plak hem erbij.</p>'},
            {'title': '7. Alles opnieuw typen in elk gesprek',
             'body': '<p>Als je dezelfde context drie keer hebt getypt, hoort hij in '
                     'een project of custom GPT. Zie hoofdstuk 7.</p>'},
        ])

    p.invulvelden(
        'Oefening: verbeter je eigen prompt',
        '<p>Neem de prompt die je in hoofdstuk 4 hebt gebouwd. Laat hem verbeteren met '
        'de tekst hierboven, en houd bij wat er gebeurt.</p>',
        [
            ('p05-vragen', 'Welke vragen stelde het model over je prompt?',
             'Dit zijn de gaten die jij niet zag'),
            ('p05-verschil', 'Wat is er veranderd aan je prompt?',
             'Wat is toegevoegd, wat is geschrapt?'),
            ('p05-beter', 'Was het resultaat beter? Waaraan merkte je dat?',
             'Wees concreet — "beter" is geen antwoord'),
            ('p05-vast', 'Welke fout uit de lijst van zeven maak jij het vaakst?',
             'Bijv. te weinig context'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Je verbeterde prompt is nu klaar om vast te leggen. Dat doe je in het '
        'volgende deel van de cursus.</p>')

    p.vraag(
        'Even checken',
        'Je hebt een prompt drie keer bijgestuurd in hetzelfde gesprek en het '
        'resultaat is eindelijk goed. Wat is de beste volgende stap?',
        [
            ('De verbeterde prompt in een nieuw, leeg gesprek testen — pas dan weet je '
             'of de prompt zelf werkt of dat de opgebouwde context het werk deed.', True),
            ('De prompt meteen vastleggen; hij is bewezen goed.', False),
            ('Nog drie rondes bijsturen om het verder aan te scherpen.', False),
            ('Het antwoord gebruiken en de prompt weggooien.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. In een lopend gesprek doet alle eerdere uitleg '
                       'stilletjes mee. Een prompt is pas bruikbaar als hij het '
                       'vanuit niets ook doet.</p>',
            '_incorrect': {'final': '<p>Nog niet. De valkuil is dat je de prompt '
                                    'crediteert voor werk dat het gesprék deed. Test '
                                    'in een leeg gesprek voordat je hem '
                                    'vastlegt.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
