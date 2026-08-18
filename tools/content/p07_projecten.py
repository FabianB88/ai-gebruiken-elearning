# -*- coding: utf-8 -*-
"""Claude Projects, ChatGPT Projects en custom GPT's: context één keer vastleggen."""


def bouw(p):
    p.tekst(
        'Stop met dezelfde context typen',
        '<p>Als je je uitleg over je organisatie, je doelgroep en je huisstijl voor de '
        'derde keer intypt, ben je iets verkeerd aan het doen. Daar zijn projecten en '
        'custom GPT’s voor: je legt de context één keer vast, en elk gesprek dat je '
        'erin start begint met die kennis al aanwezig.</p>'
        '<p>Dit is de stap waarmee AI verandert van "handig speeltje" in "onderdeel '
        'van mijn werk". Het kost een uur om goed op te zetten en het bespaart je '
        'daarna elke week tijd.</p>')

    p.accordeon(
        'Drie vormen, en wanneer je welke pakt',
        '<p>De namen lijken op elkaar, de toepassing verschilt.</p>',
        [
            {'title': 'Claude Project',
             'body': '<p>Een map met gesprekken die een gezamenlijke instructie en een '
                     'gezamenlijke set bronbestanden delen. Bedoeld voor <b>jouw eigen '
                     'terugkerende werk</b> of dat van je team. Je kunt bestanden '
                     'toevoegen (documenten, richtlijnen, voorbeelden) die Claude in '
                     'elk gesprek binnen dat project kan raadplegen.</p>'
                     '<p>Pak dit als: je werkt regelmatig aan hetzelfde onderwerp en '
                     'wil dat elk gesprek de achtergrond al kent.</p>'},
            {'title': 'ChatGPT Project',
             'body': '<p>Hetzelfde idee: een map met gesprekken, gedeelde instructies '
                     'en gedeelde bestanden. Ook hier blijft alles binnen het project '
                     'bij elkaar.</p>'
                     '<p>Pak dit als: je in ChatGPT werkt en dezelfde behoefte hebt. '
                     'Voor het onderscheid met een custom GPT: een project is voor '
                     'jou, een custom GPT is om te delen.</p>'},
            {'title': 'Custom GPT',
             'body': '<p>Een op maat gemaakte assistent met een naam, een '
                     'beschrijving, vaste instructies, eigen kennisbestanden en '
                     'eventueel eigen mogelijkheden. Het verschil met een project: een '
                     'custom GPT is bedoeld om te <b>delen</b> — met je team, je '
                     'organisatie of publiek.</p>'
                     '<p>Pak dit als: meerdere mensen dezelfde taak doen en je wil dat '
                     'ze dat op dezelfde manier doen. Bijvoorbeeld een assistent die '
                     'teksten omzet naar jullie huisstijl.</p>'},
        ])

    p.tekst(
        'Stappenplan: een Claude Project opzetten',
        '<ol>'
        '<li><b>Open claude.ai en klik in de linkerkolom op Projects, daarna op '
        'nieuw project.</b> Geef het een naam die zegt waar het over gaat, niet '
        '"Test".</li>'
        '<li><b>Schrijf de projectinstructies.</b> Dit is het hart. Gebruik de zes '
        'bouwstenen uit hoofdstuk 4, maar laat de <i>taak</i> weg — die verschilt per '
        'gesprek. Dus: rol, wie jij bent, context over de organisatie, standaard '
        'outputvorm, en de grenzen.</li>'
        '<li><b>Voeg bronbestanden toe.</b> Richtlijnen, een huisstijlgids, drie '
        'voorbeelden van goed werk, veelgestelde vragen. Liever vijf goede bestanden '
        'dan vijftig middelmatige — alles wat erin zit, telt mee.</li>'
        '<li><b>Test met een echte taak.</b> Start een gesprek in het project en geef '
        'alleen de taak. Krijg je een antwoord dat de context al kent? Dan staat het '
        'goed.</li>'
        '<li><b>Scherp de instructies aan op wat er misging.</b> Ging het model '
        'uitweiden? Zet een lengte-eis in de instructies. Verzon het cijfers? Zet de '
        'bronregel erin.</li>'
        '<li><b>Deel het project met je team</b> als je op een betaald teamplan zit, '
        'en spreek af wie de instructies beheert.</li>'
        '</ol>')

    p.tekst(
        'Stappenplan: een custom GPT bouwen',
        '<ol>'
        '<li><b>Ga naar chatgpt.com en kies in het zijmenu GPT’s, daarna "Maak een '
        'GPT".</b> Je hebt hier een betaald account voor nodig.</li>'
        '<li><b>Gebruik het bouwgesprek om te starten.</b> ChatGPT vraagt wat je wil '
        'maken en schrijft een eerste versie van de instructies. Handig om snel te '
        'beginnen — maar ga daarna zelf naar het tabblad Configureren.</li>'
        '<li><b>Vul naam en beschrijving in.</b> De beschrijving is wat je collega’s '
        'zien; maak duidelijk waar hij wél en niet voor is.</li>'
        '<li><b>Schrijf de instructies zelf uit.</b> Gebruik de zes bouwstenen. Voeg '
        'expliciet toe wat de GPT <i>niet</i> moet doen — dat wordt bijna altijd '
        'vergeten en is precies wat misgaat als anderen hem gebruiken.</li>'
        '<li><b>Zet gespreksstarters neer.</b> Drie of vier voorbeeldvragen. Dit is '
        'hoe nieuwe gebruikers leren wat ze ermee kunnen.</li>'
        '<li><b>Voeg kennisbestanden toe.</b> Let op: iemand die de GPT gebruikt, kan '
        'in sommige gevallen de inhoud van die bestanden ontlokken. Zet er dus niets '
        'in dat vertrouwelijk is.</li>'
        '<li><b>Kies de mogelijkheden.</b> Webzoeken, afbeeldingen genereren, code '
        'uitvoeren. Zet uit wat niet nodig is: hoe minder ruis, hoe voorspelbaarder '
        'het gedrag.</li>'
        '<li><b>Test met iemand anders.</b> Jij weet wat je bedoelde; je collega niet. '
        'Wat die persoon fout doet, verwerk je in de instructies.</li>'
        '<li><b>Publiceer beperkt.</b> Kies "alleen ik" of "iedereen met de link". '
        'Publiek publiceren doe je pas als er echt niets organisatie-eigens in '
        'zit.</li>'
        '</ol>')

    p.aandacht(
        'Wat je niet in kennisbestanden zet',
        '<p>Alles wat in een project of custom GPT zit, kan in een antwoord '
        'terugkomen. Bij een gedeelde custom GPT kan een gebruiker er soms zelfs '
        'gericht naar vissen. Dus: geen persoonsgegevens, geen niet-gepubliceerde '
        'cijfers, geen contracten, geen inloggegevens. Wel: richtlijnen, publieke '
        'documenten, voorbeeldteksten, sjablonen.</p>')

    p.tekst(
        'Wat maakt het verschil tussen een goede en een matige assistent',
        '<ul>'
        '<li><b>Voorbeelden verslaan beschrijvingen.</b> Drie goede voorbeeldteksten '
        'in de kennisbestanden doen meer voor de huisstijl dan een pagina uitleg over '
        'de huisstijl.</li>'
        '<li><b>Zeg wat er moet gebeuren als de assistent iets niet weet.</b> Zonder '
        'die instructie vult hij het in. Met: "als het antwoord niet in de '
        'bijgevoegde documenten staat, zeg dat en verwijs naar [collega]".</li>'
        '<li><b>Beperk de reikwijdte.</b> Eén assistent die één ding goed doet is meer '
        'waard dan één die alles half doet. Maak liever drie custom GPT’s.</li>'
        '<li><b>Zet er een datum en een eigenaar in.</b> "Laatst bijgewerkt: … , '
        'beheerd door: …". Anders staat er over een jaar verouderd beleid in dat '
        'niemand meer durft aan te raken.</li>'
        '</ul>')

    p.invulvelden(
        'Oefening: ontwerp je eigen project',
        '<p>Neem taak 1 uit hoofdstuk 3 en de prompt uit hoofdstuk 5. Zet die nu om '
        'naar een projectopzet. Maak hem daarna ook echt aan.</p>',
        [
            ('p07-naam', 'Naam van het project of de GPT',
             'Iets waaruit blijkt waar het over gaat'),
            ('p07-vorm', 'Project of custom GPT? Waarom?',
             'Alleen voor jou, of gaan collega’s hem ook gebruiken?'),
            ('p07-instructies', 'De vaste instructies (zonder de taak)',
             'Rol, wie jij bent, context, standaard outputvorm, grenzen'),
            ('p07-bestanden', 'Welke bronbestanden voeg je toe?',
             'Noem er drie tot vijf — en check of ze gedeeld mogen worden'),
            ('p07-nietweten', 'Wat moet de assistent doen als hij iets niet weet?',
             'Schrijf de exacte zin die je in de instructies zet'),
            ('p07-test', 'Wat ging er mis bij de eerste test, en wat heb je aangepast?',
             'Vul in nadat je hem hebt gemaakt'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Heb je hem aangemaakt? Zet dan meteen een herinnering over drie maanden om '
        'de instructies na te lopen.</p>')

    p.vraag(
        'Even checken',
        'Vijf collega’s schrijven elk hun eigen projectverslagen, en de kwaliteit '
        'verschilt sterk. Wat is de meest passende oplossing?',
        [
            ('Een custom GPT met de huisstijl, een sjabloon en drie voorbeeldverslagen '
             'in de kennisbestanden, gedeeld met het team.', True),
            ('Iedereen een goede prompt mailen die ze zelf kunnen plakken.', False),
            ('Eén persoon alle verslagen laten schrijven met AI.', False),
            ('Een project aanmaken in het persoonlijke account van de teamleider.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. Delen is precies waar een custom GPT voor bedoeld is: '
                       'iedereen werkt met dezelfde instructies en dezelfde '
                       'voorbeelden, en je onderhoudt het op één plek.</p>',
            '_incorrect': {'final': '<p>Nog niet. Een gemailde prompt raakt kwijt en '
                                    'wordt door iedereen anders aangepast; een project '
                                    'in een persoonlijk account is niet deelbaar. Wat '
                                    'je wil is één gedeelde assistent die je centraal '
                                    'onderhoudt.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
