# -*- coding: utf-8 -*-
"""Wie de cursus is en welke pagina's erin zitten, in deze volgorde.

Een pagina toevoegen: maak een bestand in deze map en zet hem in PAGINAS.
Een pagina verplaatsen: verschuif de regel. De id's lopen automatisch mee.
"""

ID = 'ai-gebruiken'
TITEL = 'AI leren gebruiken'
ONDERTITEL = 'Van je eerste prompt tot AI die op je eigen machine meewerkt'
OMSCHRIJVING = 'Green Office'
INLEIDING = ('Een praktische cursus voor wie AI serieus wil inzetten in het werk. '
             'Je begint bij prompten en privacy, richt daarna je eigen assistenten '
             'en koppelingen in, en eindigt met AI die in je eigen bestanden werkt '
             'en meebouwt aan je projecten. Elk hoofdstuk heeft een stappenplan en '
             'een oefening die je meteen kunt doen.')

# (bestandsnaam zonder .py, titel, samenvatting voor het menu, geschatte tijd)
PAGINAS = [
    ('p01_hoe_ai_werkt', 'Hoe een taalmodel werkt',
     'Wat er gebeurt als je iets typt, en welke zes begrippen je nodig hebt om het '
     'gedrag van AI te begrijpen.', '10 min'),
    ('p02_landschap', 'Het landschap: welk model wanneer',
     'Claude en ChatGPT, hun modellen in 2026, en vier vragen waarmee je altijd de '
     'juiste kiest.', '10 min'),
    ('p03_waarvoor', 'Waar je AI voor inzet — en waarvoor niet',
     'Vier niveaus, van versnellen tot een tweede brein, twaalf opdrachten om uit te '
     'kiezen, en vijf harde grenzen.', '20 min'),
    ('p04_prompten_opbouw', 'Prompten: de zes bouwstenen',
     'Rol, gebruiker, taak, context, output en grenzen — met een uitgewerkt voorbeeld '
     'op drie niveaus.', '20 min'),
    ('p05_prompt_optimaliseren', 'Prompts optimaliseren',
     'Bijsturen in plaats van opnieuw beginnen, je prompt laten verbeteren door het '
     'model, en zeven fouten die iedereen maakt.', '15 min'),
    ('p06_privacy', 'Privacy, AVG en vertrouwelijkheid',
     'Werken op persoonlijke titel, modeltraining uitzetten met letterlijke stappen, '
     'en wat er nooit in een gesprek hoort.', '20 min'),
    ('p07_projecten', 'Projecten als herhaalprompt',
     'Je context één keer vastleggen, de prompt optimizer gebruiken, en de grens '
     'kennen waarop Claude Projects vastlopen.', '20 min'),
    ('p08_connectors', 'Connectors en MCP',
     'Wat je in onze situatie wél kunt koppelen, wat geblokkeerd is, en drie routes '
     'voor als koppelen niet kan.', '15 min'),
    ('p09_browser', 'AI in je browser',
     'De enige route naar Teams en SharePoint, en de vaste regels die je instelt '
     'tegen prompt-injectie.', '20 min'),
    ('p10_documenten', 'Slim Word, Excel en PowerPoint maken',
     'Markdown als spil, welk formaat je aanlevert, en vijf werkvormen voor werk '
     'dat niet in één antwoord past.', '20 min'),
    ('p11_zelfstandig', 'AI die zelfstandig doorwerkt',
     'Cowork en agentmodus, werken op de achtergrond, en de regels die je vastlegt '
     'vóór je zonder tussenvragen werkt.', '20 min'),
    ('p12_desktop', 'AI naar je informatie brengen',
     'Je desktop-app toegang geven tot een eigen werkmap — zonder configuratie, met '
     'foutzoeker en de grenzen daarvan.', '20 min'),
    ('p13_vibe_coden', 'Vibe coden: zelf iets bouwen',
     'Software maken door te beschrijven wat je wil. Wat lukt, wat niet, en een '
     'stappenplan van idee naar prototype.', '20 min'),
    ('p14_werkplek', 'Je werkplek laten inrichten',
     'Laat je assistent Git, de GitHub CLI, rtk en Firebase installeren — en leer '
     'wat je zelf moet doen.', '25 min'),
    ('p15_toets', 'Kennischeck en je werkplan',
     'Zeven vragen over de hele cursus, en een plan voor wat je vanaf morgen anders '
     'doet.', '15 min'),
]
