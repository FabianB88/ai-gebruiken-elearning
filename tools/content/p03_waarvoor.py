# -*- coding: utf-8 -*-
"""Waar AI zakelijk sterk in is, en waar niet."""


def bouw(p):
    p.tekst(
        'Niet "wat kan AI", maar "waar levert het mij tijd op"',
        '<p>De vraag "wat kan AI allemaal?" is onbeantwoordbaar en ook niet nuttig. '
        'De bruikbare vraag is: welke stukken van mijn week zijn tekstwerk, '
        'zoekwerk of denkwerk-met-een-vast-patroon? Dat zijn de plekken waar het '
        'meteen loont.</p>'
        '<p>Hieronder acht categorieën die in bijna elke organisatie terugkomen, met '
        'per categorie het soort opdracht dat werkt. Loop ze langs met je eigen werk '
        'in gedachten; onderaan deze pagina vul je je eigen lijst in.</p>')

    p.accordeon(
        'Acht dingen waar het echt tijd scheelt',
        '<p>Klap open wat op jouw werk lijkt.</p>',
        [
            {'title': '1. Schrijven en herschrijven',
             'body': '<p>Een eerste versie van een mail, offerte, verslag, '
                     'projectvoorstel of nieuwsbrief. Ook: dezelfde tekst omzetten '
                     'naar een andere doelgroep of een ander formaat — van rapport '
                     'naar samenvatting, van intern naar extern, van formeel naar '
                     'toegankelijk.</p>'
                     '<p>Sterkste inzet: <b>niet</b> "schrijf een mail over X", maar '
                     '"hier is mijn ruwe aantekening, maak er een mail van aan deze '
                     'ontvanger". Jouw denkwerk blijft, het typewerk verdwijnt.</p>'},
            {'title': '2. Lezen en samenvatten',
             'body': '<p>Een rapport van tachtig pagina’s doornemen op wat relevant is '
                     'voor jouw vraag. Een subsidieregeling uitpluizen. Notulen '
                     'terugbrengen tot besluiten en acties.</p>'
                     '<p>Truc: vraag niet om "een samenvatting" maar om een '
                     'samenvatting <i>vanuit een vraag</i>. "Wat zegt dit document '
                     'over onze verplichtingen rond rapportage?" levert veel meer op '
                     'dan "vat dit samen".</p>'},
            {'title': '3. Structureren en ordenen',
             'body': '<p>Losse ideeën uit een brainstorm groeperen. Een chaotische '
                     'lijst omzetten in een tabel met kolommen die je zelf kiest. Een '
                     'planning maken uit een verhaal. Dit is misschien wel de meest '
                     'onderschatte categorie.</p>'},
            {'title': '4. Analyseren en rekenen',
             'body': '<p>Een dataset doorrekenen, patronen zoeken, een grafiek maken. '
                     'Belangrijk: laat het model hiervoor <b>code uitvoeren</b> in '
                     'plaats van uit het hoofd rekenen. Vraag er expliciet om: '
                     '"reken dit uit met code en laat de code zien". Rekenen uit het '
                     'hoofd is precies waar taalmodellen zwak zijn.</p>'},
            {'title': '5. Onderzoeken',
             'body': '<p>Uitzoeken hoe iets zit, welke partijen er zijn, wat de stand '
                     'van zaken is. Zet zoeken aan, vraag om bronnen met links, en '
                     'vraag expliciet naar tegenargumenten en naar wat het model '
                     '<i>niet</i> heeft kunnen vinden.</p>'},
            {'title': '6. Kritisch meedenken',
             'body': '<p>Onderschat: laat AI je eigen werk <i>afbreken</i> in plaats '
                     'van maken. "Dit is mijn plan. Wat zijn de drie zwakste '
                     'aannames?" of "welke vraag gaat de opdrachtgever stellen waar '
                     'ik geen antwoord op heb?" Dit levert vaak meer op dan laten '
                     'schrijven.</p>'},
            {'title': '7. Bouwen',
             'body': '<p>Kleine tools, scripts, websites, formulieren, koppelingen. '
                     'Waar je vroeger een offerte voor vroeg, kun je nu vaak zelf een '
                     'werkende eerste versie maken. Hoofdstuk 13 en verder.</p>'},
            {'title': '8. Vertalen en toegankelijk maken',
             'body': '<p>Vertalen, jargon eruit halen, teksten op B1-niveau brengen, '
                     'alt-teksten schrijven bij afbeeldingen. Let op: laat een '
                     'vertaling naar een taal die je zelf niet beheerst altijd nog '
                     'door een mens controleren.</p>'},
        ])

    p.aandacht(
        'Waar je het níet voor inzet',
        '<p>Deze vijf zijn geen kwestie van betere prompts. Hier is het antwoord '
        'gewoon: doe het niet.</p>'
        '<ul>'
        '<li><b>Beslissingen over mensen.</b> Beoordelen, selecteren, rangschikken van '
        'sollicitanten, studenten of medewerkers. Juridisch riskant en inhoudelijk '
        'onbetrouwbaar.</li>'
        '<li><b>Iets wat je zelf niet kunt controleren.</b> Als je niet kunt '
        'beoordelen of het antwoord klopt, heb je geen hulpmiddel maar een gok. Denk '
        'aan juridisch, medisch of fiscaal advies.</li>'
        '<li><b>De laatste versie van iets belangrijks.</b> AI levert een goede '
        'concept­versie. Het eindstuk dat de deur uitgaat, lees jij.</li>'
        '<li><b>Alles met persoonsgegevens of vertrouwelijke informatie</b> in een '
        'omgeving zonder verwerkersovereenkomst. Hoofdstuk 6.</li>'
        '<li><b>Je eigen vakinhoudelijke oordeel vervangen.</b> AI is een versneller '
        'van jouw denkwerk, geen vervanging ervan. Wie het gebruikt om niet te hoeven '
        'nadenken, levert werk af dat daarnaar is.</li>'
        '</ul>')

    p.tekst(
        'Stappenplan: je eigen inzetplekken vinden',
        '<p>Doe dit één keer, kost een half uur, en het bepaalt de rest van je '
        'AI-gebruik.</p>'
        '<ol>'
        '<li><b>Pak je agenda van vorige week erbij.</b> Niet je functieomschrijving — '
        'je werkelijke week.</li>'
        '<li><b>Streep alles aan wat tekst opleverde of tekst verwerkte.</b> Mails, '
        'documenten, notities, presentaties, gelezen stukken.</li>'
        '<li><b>Zet er per regel bij hoe vaak dit terugkomt.</b> Dagelijks, wekelijks, '
        'maandelijks, eenmalig.</li>'
        '<li><b>Kies de twee met de hoogste frequentie.</b> Niet de leukste, niet de '
        'moeilijkste: de vaakste. Daar zit je winst.</li>'
        '<li><b>Bepaal per taak wat "goed" betekent.</b> Waar zou je een collega op '
        'afrekenen? Dat is straks je kwaliteitseis in de prompt.</li>'
        '<li><b>Toets ze aan de niet-doen-lijst hierboven.</b> Zit er een taak met '
        'persoonsgegevens of onbeoordeelbare inhoud bij, schrap hem of pas hem aan.</li>'
        '</ol>')

    p.invulvelden(
        'Oefening: jouw twee taken',
        '<p>Vul dit nu in — je gebruikt het straks in hoofdstuk 4 om je eerste echte '
        'prompt te schrijven, en aan het eind van de cursus nog een keer. Je '
        'antwoorden worden bewaard in je eigen browser.</p>',
        [
            ('p03-taak-a', 'Taak 1 — wat doe je precies?',
             'Bijv. wekelijks een projectupdate schrijven voor de stuurgroep'),
            ('p03-freq-a', 'Hoe vaak komt dit terug?', 'Bijv. elke maandag'),
            ('p03-goed-a', 'Wanneer is het resultaat goed?',
             'Waar zou je een collega op afrekenen?'),
            ('p03-taak-b', 'Taak 2 — wat doe je precies?', 'Nog een terugkerende taak'),
            ('p03-freq-b', 'Hoe vaak komt dit terug?', 'Bijv. twee keer per maand'),
            ('p03-goed-b', 'Wanneer is het resultaat goed?', 'Beschrijf het kort'),
            ('p03-niet', 'Welke taak laat je bewust NIET aan AI over, en waarom?',
             'Bijv. beoordelingsgesprekken voorbereiden — gaat over personen'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Kopieer je antwoorden naar je eigen aantekeningen als je ze buiten deze '
        'cursus wil gebruiken.</p>')

    p.vraag(
        'Even checken',
        'Een collega vraagt AI om de vijf beste kandidaten uit een stapel '
        'sollicitatiebrieven te halen. Wat is hier het grootste probleem?',
        [
            ('Het is een beslissing over mensen op basis van persoonsgegevens — dat '
             'hoort niet bij AI thuis, ongeacht hoe goed de prompt is.', True),
            ('Niets, mits de prompt goed genoeg is opgesteld.', False),
            ('Het kost te veel tokens.', False),
            ('Het model kan geen PDF’s lezen.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Twee harde grenzen tegelijk: het gaat over personen '
                       'én over persoonsgegevens. Wat wél kan: AI je '
                       'selectiecriteria laten aanscherpen vóórdat er brieven in '
                       'beeld zijn.</p>',
            '_incorrect': {'final': '<p>Nog niet. Dit is geen promptprobleem maar een '
                                    'grens: beslissingen over mensen, op basis van '
                                    'hun persoonsgegevens, laat je niet door een '
                                    'taalmodel nemen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
