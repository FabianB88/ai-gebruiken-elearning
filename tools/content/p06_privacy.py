# -*- coding: utf-8 -*-
"""Privacy, AVG en vertrouwelijkheid: de harde grenzen."""


def bouw(p):
    p.tekst(
        'Eén regel om te onthouden',
        '<p><b>Zet nooit persoonsgegevens of vertrouwelijke informatie in een '
        'AI-gesprek.</b> Niet in een prompt, niet in een bijlage, niet in een '
        'screenshot, niet "even snel om te kijken of het werkt".</p>'
        '<p>Dat klinkt streng, en dat is het ook. De reden is simpel: zodra jij '
        'persoonsgegevens door een AI-systeem haalt, ben je volgens de AVG '
        'verwerkingsverantwoordelijke. Dan moet je kunnen uitleggen waarom je het '
        'deed, op welke grondslag, waar de gegevens terechtkomen en hoe lang ze '
        'blijven staan. Bij een gratis account kun je dat niet, want je hebt geen '
        'verwerkersovereenkomst.</p>'
        '<p>Dit hoofdstuk gaat over hoe je dat praktisch oplost, zonder dat je '
        'daardoor niets meer met AI kunt doen. Want dat hoeft niet.</p>')

    p.tekst(
        'Wat telt als persoonsgegeven — ruimer dan je denkt',
        '<p>Een persoonsgegeven is elk gegeven waarmee je een persoon direct of '
        'indirect kunt herleiden. Dat is veel meer dan een naam:</p>'
        '<ul>'
        '<li>Namen, e-mailadressen, telefoonnummers, adressen</li>'
        '<li>Personeelsnummers, studentnummers, klantnummers, dossiernummers</li>'
        '<li>IP-adressen en apparaat-id’s</li>'
        '<li>Foto’s en video’s waarop mensen herkenbaar zijn</li>'
        '<li><b>Vrije tekst óver mensen</b> — een gespreksverslag, een klacht, een '
        'beoordeling, een verzuimmelding. Dit is de categorie die het vaakst '
        'ongemerkt in een prompt belandt.</li>'
        '<li><b>Werk van studenten of cursisten</b> — dat is hun werk, hun '
        'auteursrecht, en vaak herleidbaar tot hen.</li>'
        '<li>Combinaties die op zichzelf onschuldig lijken: "de teamleider inkoop van '
        'onze vestiging in Arnhem" is één persoon.</li>'
        '</ul>')

    p.aandacht(
        'Bijzondere persoonsgegevens: nooit, in geen enkele vorm',
        '<p>Gezondheid, ras of etnische afkomst, politieke opvattingen, geloof, '
        'vakbondslidmaatschap, seksuele geaardheid, biometrie, strafrechtelijke '
        'gegevens. Deze categorie is extra beschermd en hoort onder geen enkele '
        'omstandigheid in een AI-gesprek — ook niet met een zakelijk contract, ook '
        'niet "geanonimiseerd".</p>')

    p.tekst(
        'Gratis account versus zakelijk account',
        '<p>Het verschil is groter dan alleen betalen.</p>'
        '<ul>'
        '<li><b>Gratis of persoonlijk betaald account.</b> Geen '
        'verwerkersovereenkomst. Je invoer kan gebruikt worden om modellen te '
        'trainen, tenzij je dat zelf uitzet — en of je dat gedaan hebt, kun je niet '
        'aantonen aan een toezichthouder. Voor privéwerk prima, voor werk met '
        'gegevens van anderen niet.</li>'
        '<li><b>Zakelijk account (Team, Business, Enterprise) of de API.</b> Hier '
        'hoort een verwerkersovereenkomst bij, wordt je invoer standaard niet voor '
        'training gebruikt, en zijn er afspraken over bewaartermijnen en '
        'toegang.</li>'
        '</ul>'
        '<p>Werkt jouw organisatie met een zakelijk account, gebruik dat dan ook — en '
        'niet je privé-account omdat dat toevallig al openstaat. Is er nog geen '
        'zakelijk account, dan is dat het eerste wat je regelt voordat je AI serieus '
        'inzet.</p>')

    p.tekst(
        'Stappenplan: je eigen account nalopen',
        '<p>Doe dit vandaag, het kost vijf minuten.</p>'
        '<ol>'
        '<li><b>Kijk met welk account je bent ingelogd.</b> Privé of zakelijk? Staat '
        'er een organisatienaam bij? Bij twijfel: vraag het je '
        'systeembeheerder.</li>'
        '<li><b>Zoek de trainingsinstelling op.</b> Bij ChatGPT staat die onder '
        'Instellingen bij de data-instellingen; bij Claude onder je profiel bij '
        'privacy. Zet het gebruik van je gesprekken voor modelverbetering '
        '<b>uit</b>.</li>'
        '<li><b>Controleer of er een verwerkersovereenkomst is.</b> Weet je het niet, '
        'dan is het antwoord in de praktijk nee.</li>'
        '<li><b>Ruim je gespreksgeschiedenis op.</b> Staat er nog iets in dat er niet '
        'had moeten staan, verwijder het en meld het volgens de procedure van je '
        'organisatie.</li>'
        '<li><b>Spreek af waar je collega’s werken.</b> Eén gedeelde zakelijke '
        'omgeving is veiliger dan tien losse privé-accounts.</li>'
        '</ol>')

    p.tekst(
        'Wat wél kan: anonimiseren aan de voorkant',
        '<p>Je hoeft de meeste taken niet te laten schieten. Je haalt de personen '
        'eruit vóórdat de tekst het gesprek in gaat.</p>'
        '<ol>'
        '<li><b>Vervang namen door rollen.</b> "Mark van inkoop" wordt "de '
        'inkoper". Je verliest niets aan bruikbaarheid van het antwoord.</li>'
        '<li><b>Vervang organisaties door typeringen</b> als de naam er niet toe doet: '
        '"een gemeente van middelgrote omvang".</li>'
        '<li><b>Haal alle nummers weg</b> die naar een persoon of dossier '
        'verwijzen.</li>'
        '<li><b>Vraag jezelf af: staat hier nog iets in waarmee ik zou kunnen '
        'achterhalen om wie het gaat?</b> Zo ja, is het nog niet anoniem.</li>'
        '<li><b>Werk met een sjabloon in plaats van met een geval.</b> Vraag niet '
        '"schrijf een reactie op deze klacht", maar "schrijf een sjabloon voor een '
        'reactie op een klacht over levertijd, met velden die ik zelf invul". Nog '
        'beter, want je hergebruikt het.</li>'
        '</ol>')

    p.accordeon(
        'Ook vertrouwelijk, ook niet plakken',
        '<p>Naast persoonsgegevens is er een tweede categorie die om dezelfde reden '
        'buiten het gesprek blijft.</p>',
        [
            {'title': 'Bedrijfsgevoelige informatie',
             'body': '<p>Niet-gepubliceerde cijfers, offertes van concurrenten, '
                     'inkoopprijzen, strategiestukken, informatie onder een '
                     'geheimhoudingsverklaring. Een lek hoeft niet illegaal te zijn om '
                     'schadelijk te zijn.</p>'},
            {'title': 'Broncode en systeeminformatie van klanten',
             'body': '<p>Code van een opdrachtgever valt vaak onder een contract dat '
                     'je verbiedt hem aan derden te tonen. Een AI-dienst is een '
                     'derde.</p>'},
            {'title': 'Inloggegevens en sleutels',
             'body': '<p>Wachtwoorden, API-sleutels, tokens, certificaten. Ook niet '
                     '"tijdelijk om iets te testen" — wat je in een gesprek plakt, '
                     'staat in een logbestand.</p>'},
            {'title': 'Werk van studenten en cursisten',
             'body': '<p>Ingeleverd werk is niet van jou. Wil je AI gebruiken bij '
                     'nakijken, maak dan eerst een beoordelingsmodel met AI en pas dat '
                     'zelf toe — dan gaat er geen studentwerk het model in.</p>'},
        ])

    p.tekst(
        'AI-geletterdheid is inmiddels een verplichting',
        '<p>De Europese AI-verordening verplicht organisaties om ervoor te zorgen dat '
        'medewerkers die met AI werken, voldoende weten waar ze mee bezig zijn — wat '
        'het systeem doet, wat de beperkingen zijn en welke risico’s eraan zitten. '
        'Deze cursus is daar een invulling van; leg vast dat je hem gevolgd hebt.</p>'
        '<p>Daarnaast geldt: wees transparant. Als AI een substantiële bijdrage heeft '
        'geleverd aan iets wat je oplevert, zeg dat. Niet omdat het moet klinken als '
        'een disclaimer, maar omdat je collega’s en opdrachtgevers dan weten waar ze '
        'op moeten letten.</p>')

    p.invulvelden(
        'Oefening: maak deze casus veilig',
        '<p>Iemand wil dit vragen aan ChatGPT:</p>'
        '<blockquote><p><i>"Hierbij het verslag van het gesprek met Karin de Vries '
        '(personeelsnummer 44821) over haar verzuim. Ze geeft aan dat het te maken '
        'heeft met haar rugklachten en de spanning thuis. Kun je hier een '
        'verslaglegging van maken voor het dossier en adviseren over '
        'vervolgstappen?"</i></p></blockquote>'
        '<p>Zoek uit wat hier misgaat en schrijf een werkwijze die wél kan.</p>',
        [
            ('p06-fouten', 'Welke problemen zitten er in deze vraag? Noem ze allemaal.',
             'Denk aan: welke categorieën gegevens staan hier in?'),
            ('p06-hard', 'Welk deel kan zelfs met een zakelijk account niet? Waarom?',
             'Er zit een categorie in die extra beschermd is'),
            ('p06-alternatief', 'Hoe zou jij deze taak wél met AI aanpakken?',
             'Denk aan sjablonen in plaats van gevallen'),
            ('p06-eigen', 'Welke informatie plakte jij tot nu toe wel eens in een '
             'AI-gesprek die daar niet hoort?',
             'Eerlijk antwoord; het blijft in je eigen browser'),
        ])

    p.knoppenrij(
        'Meenemen',
        '<p>Bespreek je antwoorden met een collega. Privacyafspraken werken alleen als '
        'ze gedeeld zijn.</p>')

    p.vraag(
        'Even checken',
        'Je wilt AI laten helpen bij het samenvatten van klantgesprekken. Welke aanpak '
        'is verantwoord?',
        [
            ('Namen, nummers en herleidbare details eruit halen, en werken in een '
             'zakelijke omgeving met verwerkersovereenkomst.', True),
            ('Gewoon plakken; het gaat om zakelijke gesprekken, geen privézaken.', False),
            ('Alleen de achternamen weglaten en de rest laten staan.', False),
            ('Een privé-account gebruiken zodat het niet aan de organisatie '
             'gekoppeld is.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. Twee lagen: anonimiseren aan de voorkant én een '
                       'omgeving waarin de verwerking geregeld is. Eén van de twee is '
                       'niet genoeg.</p>',
            '_incorrect': {'final': '<p>Nog niet. Zakelijke gesprekken bevatten '
                                    'persoonsgegevens van klanten. Alleen achternamen '
                                    'weglaten maakt iets niet anoniem — functie plus '
                                    'organisatie is vaak al herleidbaar. En een '
                                    'privé-account maakt het probleem groter, niet '
                                    'kleiner: dan is er helemaal geen '
                                    'verwerkersovereenkomst.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
