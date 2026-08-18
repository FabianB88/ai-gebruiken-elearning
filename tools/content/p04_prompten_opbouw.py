# -*- coding: utf-8 -*-
"""De opbouw van een goede prompt: zes bouwstenen."""


def bouw(p):
    p.tekst(
        'Een prompt is een opdrachtbriefing',
        '<p>Stel je geeft een klus aan een nieuwe collega. Iemand die enorm veel weet, '
        'razendsnel werkt, nooit moe wordt — maar die jou niet kent, je organisatie '
        'niet kent, en die je nooit terug hoort bellen met een vraag. Alles wat je '
        'niet vertelt, vult die collega zelf in.</p>'
        '<p>Dat is precies wat een prompt is. En daarmee is de kwaliteitsvraag ook '
        'beantwoord: een goede prompt bevat alles wat je een nieuwe collega zou '
        'vertellen voordat je hem alleen laat.</p>'
        '<p>Er is geen magisch woord en geen geheime formule. Er zijn zes bouwstenen. '
        'Hoe belangrijker de klus, hoe meer je er invult.</p>')

    p.tekst(
        'De zes bouwstenen',
        '<p>In deze volgorde. Je hoeft ze niet allemaal te benoemen bij een simpele '
        'vraag, maar bij een taak die ertoe doet mis je er geen.</p>'
        '<ol>'
        '<li><b>Rol</b> — wie is het model in dit gesprek? "Je bent een ervaren '
        'subsidieadviseur." Dit is geen toneelstukje: het stuurt woordkeus, '
        'aannames en wat het model als vanzelfsprekend beschouwt.</li>'
        '<li><b>Gebruiker en kennisniveau</b> — wie ben jij, en wat weet je al? '
        '"Ik ben adviseur duurzaamheid en ken de regeling op hoofdlijnen, maar niet '
        'de uitvoeringsregels." Dit voorkomt dat je uitleg krijgt die je niet nodig '
        'hebt, of juist antwoorden boven je hoofd.</li>'
        '<li><b>Taak</b> — één werkwoord, zo precies mogelijk. Niet "help me met de '
        'nieuwsbrief", maar "schrijf drie varianten van de openingsalinea".</li>'
        '<li><b>Context</b> — de situatie, het doel erachter, de doelgroep, de '
        'bronnen. Dit is meestal het langste stuk, en het stuk dat mensen '
        'overslaan.</li>'
        '<li><b>Output</b> — de vorm. Lengte, structuur, toon, taal, formaat. '
        '"Maximaal 200 woorden, in doorlopende tekst, geen opsommingstekens, '
        'Nederlands, je-vorm."</li>'
        '<li><b>Grenzen</b> — wat wel en wat niet. "Verzin geen cijfers. Gebruik '
        'alleen wat in het bijgevoegde document staat. Als iets ontbreekt, zeg dat '
        'in plaats van het in te vullen."</li>'
        '</ol>')

    p.beeld(
        'prompt-bouwstenen.svg',
        alt='Zes genummerde balken onder elkaar. 1 Rol: welke expert zou je hiervoor '
            'inhuren. 2 Gebruiker en kennisniveau: wie ben jij en wat weet je al. '
            '3 Taak: één werkwoord, zo precies mogelijk. 4 Context, meestal het '
            'langste stuk: situatie, doel, doelgroep en bronnen. 5 Output: lengte, '
            'structuur, toon, taal en formaat. 6 Grenzen: wat wel en wat niet. De '
            'balken 4 en 6 hebben een dikkere rand omdat die het verschil maken '
            'tussen een aardig en een bruikbaar antwoord.',
        onderschrift='De zes bouwstenen, in de volgorde waarin je ze opschrijft.')

    p.aandacht(
        'De belangrijkste twee zijn 4 en 6',
        '<p>Rol en outputvorm zijn de bekendste bouwstenen, maar <b>context</b> en '
        '<b>grenzen</b> maken het verschil tussen aardig en bruikbaar. Context omdat '
        'het model niets van jouw situatie weet. Grenzen omdat een model dat een gat '
        'in zijn kennis tegenkomt, dat gat standaard <i>opvult</i> in plaats van '
        'meldt. "Zeg het als je het niet weet" is de goedkoopste zin die je aan een '
        'prompt kunt toevoegen.</p>')

    p.accordeon(
        'Hetzelfde verzoek, drie keer',
        '<p>Eén taak, uitgeschreven op drie niveaus. Let op wat er telkens '
        'bijkomt.</p>',
        [
            {'title': 'Niveau 1 — zoals de meeste mensen het typen',
             'body': '<p><i>"Schrijf een stuk over onze duurzaamheidsaanpak."</i></p>'
                     '<p>Wat je terugkrijgt: een algemeen, glad en volstrekt '
                     'inwisselbaar verhaal over duurzaamheid. Iedere organisatie ter '
                     'wereld had dit kunnen sturen. Bruikbaarheid: bijna nul.</p>'},
            {'title': 'Niveau 2 — met taak, doelgroep en vorm',
             'body': '<p><i>"Schrijf een stuk van 300 woorden voor onze website over '
                     'hoe wij duurzaamheid aanpakken. Doelgroep: opdrachtgevers die '
                     'ons nog niet kennen. Toon: zakelijk, geen '
                     'marketingsuperlatieven."</i></p>'
                     '<p>Al veel beter: de vorm klopt en de toon klopt. Maar de '
                     'inhoud verzint het model nog steeds, want het weet niet wat '
                     'jullie aanpak ís.</p>'},
            {'title': 'Niveau 3 — compleet',
             'body': '<p><i>"Je bent een tekstschrijver die gespecialiseerd is in '
                     'zakelijke dienstverlening.<br><br>'
                     'Ik ben adviseur bij een organisatie die bedrijven helpt '
                     'verduurzamen. Ik schrijf zelf prima, maar ik zit te dicht op de '
                     'inhoud en gebruik te veel jargon.<br><br>'
                     'Schrijf de tekst voor de pagina "Onze aanpak" op onze '
                     'website.<br><br>'
                     'Context: onze doelgroep is een facilitair manager of '
                     'directeur van een mkb-bedrijf van 20 tot 200 mensen. Die weet '
                     'dat er iets moet met duurzaamheid, weet niet waar te beginnen, '
                     'en is bang voor een langdurig adviestraject met een dik rapport '
                     'als resultaat. Onze aanpak staat in het bijgevoegde document; '
                     'kern is dat we in vier weken tot een uitvoerbaar plan komen.<br><br>'
                     'Output: 300 woorden, drie tussenkoppen, doorlopende tekst, '
                     'geen opsommingstekens, je-vorm, Nederlands.<br><br>'
                     'Wel: concreet worden over wat de klant zelf moet doen. '
                     'Niet: cijfers of resultaten noemen die niet in het document '
                     'staan; als je iets mist, benoem het onderaan in plaats van het '
                     'in te vullen."</i></p>'
                     '<p>Dit is drie keer zo lang om te typen en tien keer zo '
                     'bruikbaar. En je hergebruikt hem: volgende keer wissel je alleen '
                     'de taak.</p>'},
        ])

    p.tekst(
        'Stappenplan: van leeg scherm naar prompt',
        '<p>Werk deze zeven stappen af. Na een week of twee doe je het uit je hoofd.</p>'
        '<ol>'
        '<li><b>Schrijf eerst op wat je wilt hebben, niet wat je wilt vragen.</b> '
        'Beschrijf het eindresultaat: "een tekst van 300 woorden die X doet". Vanuit '
        'het resultaat terugredeneren is makkelijker dan vooruit formuleren.</li>'
        '<li><b>Bepaal de rol.</b> Welke expert zou jij hiervoor inhuren? Dat is de '
        'rol.</li>'
        '<li><b>Zet jezelf erin.</b> Wat is je functie, wat weet je al, waar loop je '
        'op vast? Dit stuurt het niveau van het antwoord.</li>'
        '<li><b>Verzamel de context.</b> Alles wat een nieuwe collega zou moeten '
        'weten. Plak brondocumenten erbij in plaats van ze samen te vatten — het '
        'model leest sneller dan jij.</li>'
        '<li><b>Beschrijf de outputvorm expliciet.</b> Lengte, structuur, toon, taal. '
        'Als je het niet zegt, kiest het model, en dat kiest standaard voor lang, '
        'opsommend en Engels-achtig Nederlands.</li>'
        '<li><b>Zet de grenzen erbij.</b> Wat mag niet, wat moet uit de bron komen, '
        'wat moet het melden in plaats van invullen.</li>'
        '<li><b>Lees je prompt terug alsof je hem krijgt.</b> Zou jij hiermee aan de '
        'slag kunnen? Zo niet, ontbreekt er context.</li>'
        '</ol>')

    p.tekst(
        'Vijf technieken die er bovenop komen',
        '<ul>'
        '<li><b>Geef een voorbeeld.</b> Eén goed voorbeeld van het gewenste resultaat '
        'stuurt sterker dan drie alinea’s uitleg over de vorm. Heb je een eerdere '
        'tekst die goed was? Plak hem erbij: "in deze stijl".</li>'
        '<li><b>Vraag om varianten, niet om hét antwoord.</b> "Geef drie verschillende '
        'invalshoeken, kort uitgewerkt" levert meer op dan één uitgewerkt stuk dat je '
        'toch moet bijschaven.</li>'
        '<li><b>Laat het eerst vragen stellen.</b> "Stel me eerst maximaal vijf vragen '
        'die je nodig hebt om dit goed te doen, en wacht op mijn antwoord." Dit is '
        'verrassend effectief bij taken waarvan je zelf nog niet scherp hebt wat je '
        'wilt.</li>'
        '<li><b>Splits grote klussen op.</b> Eerst de structuur, dan per onderdeel de '
        'inhoud. Een prompt die tien dingen tegelijk vraagt, doet ze alle tien '
        'half.</li>'
        '<li><b>Zeg wat je wél wilt.</b> "Schrijf beknopt en concreet" werkt beter dan '
        '"schrijf niet te lang en niet te vaag". Modellen sturen slechter op '
        'verboden dan op richtingen.</li>'
        '</ul>')

    p.invulvelden(
        'Oefening: bouw je eerste complete prompt',
        '<p>Pak taak 1 die je in hoofdstuk 3 hebt ingevuld en schrijf daar nu de zes '
        'bouwstenen bij. Plak de zes velden daarna achter elkaar in Claude of ChatGPT '
        'en kijk wat eruit komt.</p>',
        [
            ('p04-rol', '1. Rol — welke expert zou je hiervoor inhuren?',
             'Je bent een …'),
            ('p04-gebruiker', '2. Gebruiker en kennisniveau — wie ben jij?',
             'Ik ben … en ik weet al … maar niet …'),
            ('p04-taak', '3. Taak — één werkwoord, zo precies mogelijk',
             'Schrijf / analyseer / maak een overzicht van …'),
            ('p04-context', '4. Context — situatie, doel, doelgroep, bronnen',
             'Wat zou een nieuwe collega moeten weten?'),
            ('p04-output', '5. Output — lengte, structuur, toon, taal, formaat',
             'Bijv. max 300 woorden, drie koppen, je-vorm, Nederlands'),
            ('p04-grenzen', '6. Grenzen — wat wel, wat niet',
             'Bijv. geen cijfers verzinnen; ontbrekende informatie benoemen'),
            ('p04-resultaat', 'Wat kreeg je terug? Wat viel op?',
             'Vul in nadat je de prompt hebt gedraaid'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Deze zes velden samen zijn je eerste herbruikbare prompt. Bewaar hem — in '
        'hoofdstuk 7 zet je hem vast in een project of custom GPT, zodat je hem nooit '
        'meer hoeft te typen.</p>')

    p.vraag(
        'Even checken',
        'Welke toevoeging aan een prompt vermindert het risico op verzonnen feiten '
        'het meest?',
        [
            ('"Gebruik alleen informatie uit het bijgevoegde document. Ontbreekt er '
             'iets, benoem dat dan in plaats van het in te vullen."', True),
            ('"Wees accuraat en betrouwbaar."', False),
            ('"Je bent een expert op dit gebied."', False),
            ('"Antwoord in maximaal 300 woorden."', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. Je doet twee dingen tegelijk: je begrenst de bron én '
                       'je geeft het model een uitweg voor wat het niet weet. Zonder '
                       'die uitweg vult het het gat op.</p>',
            '_incorrect': {'final': '<p>Nog niet. "Wees accuraat" en een rolomschrijving '
                                    'zijn aanmoedigingen zonder handvat — het model '
                                    'dacht al dat het accuraat was. Wat helpt is de '
                                    'bron begrenzen en een alternatief geven voor '
                                    '"ik weet het niet".</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
