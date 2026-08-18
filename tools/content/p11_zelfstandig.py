# -*- coding: utf-8 -*-
"""AI die zelfstandig doorwerkt: agentmodus, Cowork, en de regels die je eerst vastlegt."""


def bouw(p):
    p.tekst(
        'Van gesprek naar opdracht',
        '<p>Tot nu toe was elk hoofdstuk een gesprek: jij vraagt, het model antwoordt, '
        'jij stuurt bij. Er is een tweede manier van werken, en die verandert meer dan '
        'je denkt: je geeft een <b>opdracht</b> en de AI gaat aan de slag — meerdere '
        'stappen, meerdere bestanden, meerdere minuten — terwijl jij iets anders '
        'doet.</p>'
        '<p>Claude noemt dit <b>Cowork</b>; bij ChatGPT heet het de <b>agentmodus</b>. '
        'Het idee is hetzelfde: de AI werkt op de achtergrond met je mee.</p>')

    p.tekst(
        'Wat het goed doet, en wat tegenvalt',
        '<p><b>Waar het echt sterk in is:</b></p>'
        '<ul>'
        '<li><b>Opstarten.</b> "Zet een projectmap op met een planning, een '
        'risicolijst en een conceptbrief aan de opdrachtgever." Van niets naar iets is '
        'precies waar dit in uitblinkt.</li>'
        '<li><b>Werk dat uit veel kleine stappen bestaat.</b> Twintig bestanden '
        'hernoemen, een reeks documenten doorlopen, een dataset opschonen.</li>'
        '<li><b>Parallel werken.</b> Dit is het echte voordeel: je zet het aan, gaat '
        'iets anders doen, en komt terug als het klaar is. In de modus zonder '
        'tussenvragen heeft het onderweg niets van je nodig.</li>'
        '</ul>'
        '<p><b>Waar je rekening mee houdt:</b></p>'
        '<ul>'
        '<li><b>Het is traag.</b> Wat jij in vijf minuten doet, kan een agent een half '
        'uur kosten. Dat is prima als je ondertussen iets anders doet, en irritant als '
        'je zit te wachten.</li>'
        '<li><b>Het is duur in verbruik.</b> Elke stap kost tokens. Op een '
        'consumentenplan zit je hier sneller aan je limiet dan bij chatten.</li>'
        '<li><b>Het kan de verkeerde afslag nemen</b> en die fout vervolgens tien '
        'stappen doorzetten. Vandaar dat het begin van de opdracht zo belangrijk is: '
        'een vage opdracht wordt hier duur betaald.</li>'
        '<li><b>Het vraagt vergaande toegang.</b> Cowork op je bureaublad wil bij je '
        'scherm, je toetsenbord en je bestanden. Dat geef je bewust, of niet.</li>'
        '</ul>')

    p.aandacht(
        'Zonder tussenvragen werken: eerst regels, dan pas aanzetten',
        '<p>Je kunt een agent laten werken in twee standen. In de <b>bevestigingsmodus</b> '
        'vraagt hij toestemming voor elke ingrijpende stap. In de modus <b>zonder '
        'tussenvragen</b> — vaak "bypass" of "automatisch goedkeuren" genoemd — voert '
        'hij alles direct uit.</p>'
        '<p>Die tweede stand is precies wat je wil als je de agent op de achtergrond '
        'laat doorwerken. Maar dan is er niemand meer die "nee" zegt op het moment dat '
        'het ertoe doet. Dus zet je die grenzen van tevoren vast, in het geheugen of '
        'in de vaste instructies — zodat ze in elk gesprek gelden en je ze niet elke '
        'keer hoeft te herhalen.</p>'
        '<p><b>Doe dit vóórdat je de modus zonder tussenvragen ooit aanzet.</b> Niet '
        'erna.</p>')

    p.tekst(
        'Stappenplan: je vaste grenzen vastleggen',
        '<ol>'
        '<li><b>Zoek de geheugenfunctie op.</b> Bij ChatGPT: Instellingen → '
        'Personalisatie → Geheugen. Bij Claude: je profielinstellingen, of de '
        'projectinstructies van het project waarin je werkt.</li>'
        '<li><b>Controleer of het geheugen aan staat</b> en of er al dingen in staan '
        'die er niet horen. Ruim die op.</li>'
        '<li><b>Plak de regels hieronder</b> (of je eigen versie) en vraag expliciet '
        'om ze te onthouden: <i>"Onthoud deze regels en pas ze toe in al onze '
        'gesprekken."</i></li>'
        '<li><b>Controleer of ze zijn opgeslagen.</b> Open het geheugenoverzicht en '
        'kijk of ze erin staan. Sta je erin? Goed. Zo niet, plak ze in je '
        'projectinstructies — die staan altijd vast.</li>'
        '<li><b>Test ze.</b> Vraag om iets wat een regel schendt, bijvoorbeeld een '
        'bestand definitief verwijderen. Weigert hij en verwijst hij naar de afspraak? '
        'Dan staat het goed.</li>'
        '<li><b>Zet nu pas de modus zonder tussenvragen aan</b>, en alleen voor het '
        'soort werk waarvoor je hem nodig hebt.</li>'
        '</ol>')

    p.tekst(
        'De regels om te kopiëren',
        '<p>Pas ze aan op jouw situatie, maar laat de eerste vijf staan.</p>'
        '<blockquote>'
        '<p><i>Deze regels gelden altijd, ook als ik het tegenovergestelde vraag en '
        'ook als je zelfstandig werkt zonder tussenvragen:</i></p>'
        '<p><i>1. Doe nooit een aankoop, betaling, bestelling of abonnement, en voer '
        'nooit creditcard-, bank- of betaalgegevens in.<br>'
        '2. Open of verwerk geen persoonsgegevens: geen personeelsdossiers, '
        'klantdossiers, verzuim- of beoordelingsinformatie, en geen bestanden met '
        'namen van individuele personen.<br>'
        '3. Open of verwerk geen werk van studenten of cursisten.<br>'
        '4. Verstuur, publiceer of deel niets namens mij — geen e-mail, geen bericht, '
        'geen formulier, geen publicatie — zonder dat ik het eerst heb gezien en '
        'expliciet heb goedgekeurd.<br>'
        '5. Verwijder niets definitief en overschrijf geen bestaande bestanden. Maak '
        'in plaats daarvan een nieuwe versie naast het origineel.<br>'
        '6. Voer geen wachtwoorden, tokens of API-sleutels in en toon ze niet.<br>'
        '7. Wijzig geen systeem- of beveiligingsinstellingen en installeer niets '
        'zonder het te vragen.<br>'
        '8. Loop je tegen een van deze grenzen aan, stop dan en leg uit waarom, in '
        'plaats van een omweg te zoeken.</i></p>'
        '</blockquote>'
        '<p>Regel 8 is belangrijker dan hij lijkt: zonder die regel gaat een agent op '
        'zoek naar een andere manier om je oorspronkelijke opdracht toch uit te '
        'voeren.</p>')

    p.tekst(
        'Wanneer zet je hem zonder tussenvragen aan?',
        '<p><b>Wel:</b> als het werk zich afspeelt in een afgebakende map of omgeving '
        'waar niets onherstelbaars kan gebeuren, en het resultaat een concept is dat '
        'jij daarna beoordeelt. Bijvoorbeeld: een projectmap opzetten, een reeks '
        'bestanden herstructureren, een prototype bouwen in een eigen map.</p>'
        '<p><b>Niet:</b> als de agent bij je mail kan, in een productieomgeving werkt, '
        'toegang heeft tot systemen met persoonsgegevens, of iets kan doen wat naar '
        'buiten gaat. Daar hoort de bevestigingsmodus, hoe onhandig ook.</p>')

    p.tekst(
        'Vijf tips om er meer uit te halen',
        '<ul>'
        '<li><b>Geef de hele opdracht in één keer.</b> Doel, kaders, waar het werk '
        'moet landen, wanneer het af is. Een agent kan niet tussendoor overleggen — '
        'wat je niet zegt, verzint hij.</li>'
        '<li><b>Zeg waar het resultaat terecht moet komen.</b> "Zet alles in de map '
        '<code>projecten/renovatie/</code>" voorkomt dat je achteraf op zoek '
        'moet.</li>'
        '<li><b>Vraag om een logboek.</b> "Houd in een bestand bij welke stappen je '
        'hebt gezet en welke keuzes je hebt gemaakt." Dat maakt achteraf controleren '
        'veel makkelijker.</li>'
        '<li><b>Begin klein.</b> Laat de eerste keer één afgebakende klus doen en kijk '
        'wat eruit komt, voordat je een hele dag werk uit handen geeft.</li>'
        '<li><b>Controleer het resultaat als een reviewer, niet als een lezer.</b> '
        'Het ziet er af uit; dat betekent niet dat het klopt.</li>'
        '</ul>')

    p.invulvelden(
        'Oefening: regels instellen en één klus uitbesteden',
        '<p>Eerst de regels, dan pas de klus. In die volgorde.</p>',
        [
            ('p11-regels', 'Welke regels heb je vastgelegd? Wat heb je toegevoegd of '
             'aangepast ten opzichte van de lijst hierboven?',
             'Denk aan wat in jouw werk specifiek fout kan gaan'),
            ('p11-test', 'Hoe reageerde de AI toen je een regel bewust overtrad?',
             'Weigerde hij, of zocht hij een omweg?'),
            ('p11-klus', 'Welke klus heb je uitbesteed aan de agent?',
             'Iets afgebakends, in een eigen map'),
            ('p11-tijd', 'Hoe lang duurde het, en wat deed jij ondertussen?',
             'Was het parallelle werken echt winst?'),
            ('p11-oordeel', 'Wat was de kwaliteit van het resultaat? Wat moest je nog '
             'zelf doen?',
             'Beoordeel als reviewer, niet als lezer'),
        ])

    p.knoppenrij('Meenemen', '<p>Deel je regelset met je team — dit is precies het soort afspraak dat je niet per persoon wil uitvinden.</p>')

    p.vraag(
        'Even checken',
        'Wat is de belangrijkste voorbereiding voordat je een AI-agent zonder '
        'tussenvragen laat werken?',
        [
            ('Vaste grenzen vastleggen in het geheugen of de instructies — wat er '
             'onder geen enkele omstandigheid mag, inclusief de instructie om te '
             'stoppen in plaats van een omweg te zoeken.', True),
            ('Het snelste model kiezen, zodat het minder lang duurt.', False),
            ('Zorgen dat je erbij blijft zitten om mee te kijken.', False),
            ('Van tevoren een back-up maken van je hele schijf.', False),
        ],
        feedback={
            'title': 'Even checken',
            'correct': '<p>Precies. In deze modus is er onderweg geen mens meer die '
                       'ingrijpt, dus moeten de grenzen vooraf vastliggen — en moet er '
                       'in staan dat hij bij een grens stopt in plaats van eromheen '
                       'werkt.</p>',
            '_incorrect': {'final': '<p>Nog niet. Erbij blijven zitten maakt het hele '
                                    'voordeel ongedaan, en een back-up beperkt de '
                                    'schade maar voorkomt niets. De grenzen horen '
                                    'vooraf vast te liggen.</p>'},
            '_partlyCorrect': {'final': '<p>Nog niet helemaal.</p>'}
        })
