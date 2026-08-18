# -*- coding: utf-8 -*-
"""Welke modellen er zijn en wanneer je welke pakt. Stand: augustus 2026."""


def bouw(p):
    p.tekst(
        'Twee families, en waarom dat genoeg is',
        '<p>Er zijn tientallen aanbieders, maar voor serieus werk kom je in de '
        'praktijk uit bij twee: <b>Claude</b> van Anthropic en <b>ChatGPT</b> van '
        'OpenAI. Ze kunnen allebei bijna alles wat in deze cursus staat. Het verschil '
        'zit in details en in smaak, niet in of iets kan.</p>'
        '<p>Belangrijker dan de merkkeuze is dat je begrijpt dat elke familie '
        '<b>meerdere modellen</b> heeft, van zwaar en traag tot licht en snel. Wie '
        'altijd het zwaarste model gebruikt, wacht onnodig lang en betaalt te veel. '
        'Wie altijd het lichtste gebruikt, krijgt oppervlakkige antwoorden op '
        'moeilijke vragen en concludeert dat "AI het niet kan".</p>')

    p.aandacht(
        'Dit hoofdstuk veroudert het snelst',
        '<p>De namen hieronder kloppen in <b>augustus 2026</b>. Modelnamen wisselen '
        'een paar keer per jaar. De <i>indeling</i> — zwaar / gebalanceerd / snel — '
        'blijft wel staan, en dat is het enige wat je echt moet onthouden. Kijk bij '
        'twijfel in de modelkiezer van de app zelf; daar staat altijd de actuele '
        'lijst.</p>')

    p.tekst(
        'Claude (Anthropic)',
        '<p>De modelnamen volgen een vaste logica: hoe hoger in de lijst, hoe '
        'capabeler en duurder.</p>'
        '<ul>'
        '<li><b>Claude Opus 5</b> — het werkpaard voor moeilijk werk. Complexe '
        'analyses, langere programmeerklussen, werk dat over veel stappen '
        'samenhangend moet blijven. Dit is wat je standaard pakt als het ertoe '
        'doet.</li>'
        '<li><b>Claude Sonnet 5</b> — bijna dezelfde kwaliteit op veel taken, '
        'goedkoper en sneller. Goed voor werk in volume: veel documenten door, veel '
        'korte vragen.</li>'
        '<li><b>Claude Haiku 4.5</b> — snel en goedkoop, voor simpele afgebakende '
        'klusjes zoals classificeren of een korte samenvatting.</li>'
        '<li><b>Claude Fable 5</b> — het zwaarste model dat er is, voor de allerhardste '
        'redeneer- en langlopende agentklussen. Prijzig; alleen inzetten als Opus 5 '
        'het echt niet redt.</li>'
        '</ul>'
        '<p>Het contextvenster is bij de huidige modellen ongeveer een miljoen '
        'tokens. In de app kies je het model rechtsonder in het invoerveld.</p>')

    p.tekst(
        'ChatGPT (OpenAI)',
        '<p>OpenAI gebruikt sinds juli 2026 een familie met drie namen naast elkaar in '
        'plaats van één nummer.</p>'
        '<ul>'
        '<li><b>GPT-5.6 Sol</b> — het vlaggenschip; het zwaarste en beste model van de '
        'familie.</li>'
        '<li><b>GPT-5.6 Terra</b> — de balans tussen slim en betaalbaar. Voor de '
        'meeste dagelijkse taken de juiste keuze.</li>'
        '<li><b>GPT-5.6 Luna</b> — het snelste en goedkoopste, voor werk in volume. '
        'Sinds begin augustus 2026 ook het standaardmodel voor gratis gebruikers.</li>'
        '</ul>'
        '<p>Daarnaast staan de oudere <b>GPT-5.4 Thinking</b> en <b>Pro</b> nog in de '
        'kiezer voor wie daaraan gewend is. De 5.6-familie deelt een contextvenster '
        'van ruim een miljoen tokens en een kennisafkapdatum van 16 februari 2026 — '
        'alles daarna moet het model opzoeken.</p>')

    p.tekst(
        'Kiezen: vier vragen',
        '<p>Loop deze vier vragen langs en je zit vrijwel altijd goed.</p>'
        '<ol>'
        '<li><b>Moet het antwoord kloppen, of moet het vooral snel?</b> Klopt het '
        'ertoe — analyse, advies, code, iets wat de deur uitgaat — pak het zware '
        'model (Opus 5 of GPT-5.6 Sol). Moet het snel — een mail herschrijven, een '
        'lijst opschonen — pak het lichte.</li>'
        '<li><b>Zit er redeneerwerk in?</b> Meerdere stappen, tegenstrijdige eisen, '
        'rekenen: zet het denken aan (bij ChatGPT een Thinking-variant, bij Claude '
        'gaat dit automatisch bij de zwaardere modellen).</li>'
        '<li><b>Heb je actuele informatie nodig?</b> Zet zoeken aan en vraag om '
        'links. Zonder zoeken werkt het model uit zijn trainingsgeheugen.</li>'
        '<li><b>Doe je dit vaker?</b> Dan hoort het niet in een los gesprek maar in '
        'een project of een custom GPT — daar gaat hoofdstuk 7 over.</li>'
        '</ol>')

    p.accordeon(
        'Waar je met AI werkt: zes plekken',
        '<p>Niet alleen welk model, ook wáár je werkt maakt verschil. Deze zes komen '
        'in deze cursus allemaal langs.</p>',
        [
            {'title': '1. De chat in je browser',
             'body': '<p>claude.ai of chatgpt.com. Waar iedereen begint. Prima voor '
                     'losse vragen, slecht voor werk dat je herhaalt.</p>'},
            {'title': '2. Projecten en custom GPT’s',
             'body': '<p>Een chat met vaste instructies en vaste bronbestanden. Je '
                     'legt je context één keer vast in plaats van elke keer opnieuw. '
                     'Hoofdstuk 7.</p>'},
            {'title': '3. Connectors',
             'body': '<p>Koppelingen naar je eigen systemen: Drive, SharePoint, Teams, '
                     'Canva, Slack. De AI haalt zelf op wat hij nodig heeft. '
                     'Hoofdstuk 8.</p>'},
            {'title': '4. De browser',
             'body': '<p>Claude in Chrome of ChatGPT Atlas: de AI ziet je tabbladen en '
                     'kan klikken. Krachtig en risicovol. Hoofdstuk 9.</p>'},
            {'title': '5. De desktop-app',
             'body': '<p>Claude Desktop of de ChatGPT-app op je pc, met toegang tot '
                     'mappen op je eigen schijf. Je haalt de AI naar je informatie in '
                     'plaats van andersom. Hoofdstukken 11 en 12.</p>'},
            {'title': '6. De terminal',
             'body': '<p>Claude Code of Codex: AI die in je projectmap leest, schrijft '
                     'en commando’s uitvoert. Zo bouw je software. Hoofdstukken 13 '
                     'en 14.</p>'},
        ])

    p.vraag(
        'Even checken',
        'Je moet 200 klantreacties in een spreadsheet indelen in drie categorieën. De '
        'taak is eenvoudig maar het zijn er veel. Welke keuze ligt het meest voor de '
        'hand?',
        [
            ('Een licht, snel model — de taak is simpel en herhaalt zich vaak.', True),
            ('Het zwaarste model, want het gaat om 200 stuks en dan wil je '
             'kwaliteit.', False),
            ('Het maakt niet uit; alle modellen doen hetzelfde.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Klopt. Classificeren is precies waar de lichte modellen voor '
                       'bedoeld zijn: veel, snel en goedkoop. Controleer wel een '
                       'steekproef van de uitkomsten.</p>',
            '_incorrect': {'final': '<p>Niet helemaal. Het aantal maakt de taak niet '
                                    'moeilijker, alleen langer. Moeilijkheid van de '
                                    'taak bepaalt de modelkeuze, niet de '
                                    'hoeveelheid.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet.</p>'}
        })
