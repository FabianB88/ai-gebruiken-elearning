# -*- coding: utf-8 -*-
"""Wat een taalmodel is, en wat het niet is."""


def bouw(p):
    p.tekst(
        'Wat je hier leert',
        '<p>Deze cursus gaat over AI leren gebruiken in je werk. Niet over hoe je '
        'een model traint, wel over hoe je er iets bruikbaars uit krijgt — van je '
        'eerste prompt tot AI die meekijkt in je eigen bestanden en meebouwt aan '
        'je projecten.</p>'
        '<p>We beginnen bij het begin: wat gebeurt er als je iets typt in ChatGPT '
        'of Claude? Dat is geen technisch trivia. Bijna elke fout die mensen met AI '
        'maken — vertrouwen op verzonnen bronnen, klagen dat het model iets '
        '"vergeten" is, verbaasd zijn dat hetzelfde verzoek twee keer een ander '
        'antwoord geeft — komt voort uit een verkeerd beeld van wat er onder de '
        'motorkap zit.</p>')

    p.tekst(
        'Het voorspelt, het zoekt niet op',
        '<p>Een taalmodel is getraind op enorme hoeveelheden tekst en heeft daarbij '
        'één ding geleerd: bij een stuk tekst voorspellen wat er logischerwijs '
        'volgt. Meer niet. Er zit geen database in met feiten die het opzoekt, en '
        'geen redenering die het van tevoren klaar heeft liggen.</p>'
        '<p>Dat verklaart de kracht én de zwakte. De kracht: het kan met elke tekst '
        'omgaan, in elke vorm, over elk onderwerp, ook eentje dat het nooit precies '
        'zo gezien heeft. De zwakte: een vloeiend, zelfverzekerd en volledig onjuist '
        'antwoord kost het model precies evenveel moeite als een juist antwoord. Het '
        'merkt het verschil zelf niet.</p>'
        '<p>Moderne modellen hebben daar hulpmiddelen bij gekregen. Ze kunnen zoeken '
        'op het web, bestanden lezen, code uitvoeren en eerst nadenken voordat ze '
        'antwoorden. Maar de kern blijft: het is een tekstvoorspeller met '
        'gereedschap, geen encyclopedie.</p>')

    p.accordeon(
        'Zes begrippen die je nodig hebt',
        '<p>Je hoeft niet technisch te zijn, maar deze zes termen kom je overal '
        'tegen, en ze verklaren het meeste gedrag dat je gaat zien.</p>',
        [
            {'title': 'Token',
             'body': '<p>De eenheid waarin het model tekst knipt — grofweg een '
                     'woorddeel. "Duurzaamheid" is meerdere tokens, "de" is er één. '
                     'Vuistregel: ongeveer 750 woorden Nederlands is 1.000 tokens. '
                     'Je betaalt per token en het contextvenster wordt in tokens '
                     'gemeten, dus het is de munteenheid van AI.</p>'},
            {'title': 'Contextvenster',
             'body': '<p>Alles wat het model tegelijk kan zien: jouw instructies, het '
                     'hele gesprek tot nu toe, en de bestanden die je meestuurt. Bij '
                     'de huidige topmodellen is dat ongeveer een miljoen tokens — een '
                     'flinke stapel documenten. Zit je eroverheen, dan valt het begin '
                     'van het gesprek weg of wordt het samengevat. Vandaar dat een '
                     'model soms iets "vergeet".</p>'},
            {'title': 'Kennisafkapdatum',
             'body': '<p>Het moment waarop de trainingsdata stopt. Alles daarna kent '
                     'het model niet uit zichzelf. Vraag je naar iets recents, dan '
                     'moet het zoeken op internet — of het verzint iets. Bij twijfel: '
                     'vraag expliciet om te zoeken, en om werkende bronlinks.</p>'},
            {'title': 'Hallucinatie',
             'body': '<p>Een verzonnen feit, bron, citaat of link, gepresenteerd met '
                     'hetzelfde gemak als een juist antwoord. Komt het vaakst voor bij '
                     'precieze details: jaartallen, paginanummers, wetsartikelen, '
                     'namen van auteurs. Alles wat je zou napluizen als een stagiair '
                     'het aanleverde, pluis je bij AI ook na.</p>'},
            {'title': 'Non-determinisme',
             'body': '<p>Dezelfde vraag geeft niet twee keer exact hetzelfde antwoord. '
                     'Dat is geen storing, dat hoort zo. Het betekent wel dat je een '
                     'prompt niet kunt beoordelen op één poging: wil je weten of een '
                     'prompt goed werkt, draai hem dan drie keer.</p>'},
            {'title': 'Redeneren (thinking)',
             'body': '<p>Nieuwere modellen kunnen eerst hardop denken in een intern '
                     'kladblok voordat ze antwoorden. Dat kost tijd en tokens, maar '
                     'levert flink betere antwoorden op bij alles wat meerdere stappen '
                     'heeft. Voor een korte herschrijfklus is het overkill; voor een '
                     'analyse of een stuk code is het het waard.</p>'},
        ])

    p.aandacht(
        'Het model weet niets van jou',
        '<p>Het kent je organisatie niet, je project niet, je collega’s niet en je '
        'huisstijl niet — tenzij je het vertelt of het koppelt aan je eigen bronnen. '
        'Bijna elk teleurstellend antwoord is in werkelijkheid een teleurstellende '
        'vraag: te weinig context. Vanaf hoofdstuk 4 lossen we dat structureel op.</p>')

    p.tekst(
        'Vier dingen die je vanaf nu anders doet',
        '<p>De rest van deze cursus bouwt op deze vier gewoontes. Ze kosten je samen '
        'geen minuut extra per dag en halen het grootste deel van de ellende weg.</p>'
        '<ol>'
        '<li><b>Geef context voordat je een taak geeft.</b> Wie ben je, voor wie is '
        'het, wat is de situatie.</li>'
        '<li><b>Controleer alles wat je zou controleren bij een onbekende '
        'stagiair.</b> Cijfers, bronnen, namen, regelgeving.</li>'
        '<li><b>Werk in rondes.</b> Eerst een opzet, dan bijsturen. Niet één prompt '
        'die alles in één keer goed moet doen.</li>'
        '<li><b>Zet nooit persoonsgegevens of vertrouwelijke informatie in een '
        'gesprek</b> waarvan je niet zeker weet hoe het verwerkt wordt. Hoofdstuk 6 '
        'gaat daarover.</li>'
        '</ol>')

    p.vraag(
        'Even checken',
        'Je vraagt een model om vijf wetenschappelijke artikelen over circulaire '
        'bouw, met auteur en jaartal. Je krijgt een keurig lijstje terug. Wat doe je?',
        [
            ('Elke bron controleren voordat je hem gebruikt — juist titels, auteurs '
             'en jaartallen zijn het gevoeligst voor hallucinatie.', True),
            ('Overnemen; het model heeft duidelijk toegang tot wetenschappelijke '
             'literatuur.', False),
            ('Alleen de nieuwste bron controleren, de rest zal wel kloppen.', False),
            ('Dezelfde vraag nog een keer stellen; komt hetzelfde lijstje terug, dan '
             'klopt het.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. Een net opgemaakte bronnenlijst zegt niets over de '
                       'juistheid ervan. Vraag om een echte zoekopdracht met werkende '
                       'links, en klik ze aan.</p>',
            '_incorrect': {'final': '<p>Nog niet. Het model heeft geen '
                                    'literatuurdatabase; het voorspelt hoe een '
                                    'plausibele bronvermelding eruitziet. Twee keer '
                                    'hetzelfde antwoord is trouwens ook geen bewijs — '
                                    'hetzelfde patroon leidt tot dezelfde '
                                    'verzinsels.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
