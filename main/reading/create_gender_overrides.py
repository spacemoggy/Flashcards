import pandas as pd

def create_gender_overrides_file():
    """Create CSV file with gender overrides"""
    overrides = {
        # Highest frequency (>1000)
        'main': 'f',      # la main
        'enfant': 'm',    # l'enfant (but can refer to f/m)
        'maison': 'f',    # la maison
        'mort': 'f',      # la mort
        
        # Very high frequency (400-1000)
        'fin': 'f',       # la fin
        'gens': 'm',      # les gens (always plural)
        'part': 'f',      # la part
        'tour': 'f',      # la tour (f), different from le tour (m)
        'livre': 'm',     # le livre
        'voiture': 'f',   # la voiture
        
        # High frequency (200-400)
        'geste': 'm',     # le geste
        'ombre': 'f',     # l'ombre
        'gauche': 'f',    # la gauche
        'chef': 'm',      # le chef (can be f in modern usage)
        'cours': 'm',     # le cours
        
        # Medium-high frequency (100-200)
        'poche': 'f',     # la poche
        'politique': 'f', # la politique (as noun)
        'chance': 'f',    # la chance
        'plat': 'm',      # le plat
        'page': 'f',      # la page
        'garde': 'f',     # la garde (f), different from le garde (m)
        'mémoire': 'f',   # la mémoire
        'saint': 'm',     # le saint
        'camarade': 'm',  # le/la camarade (can be both)
        'merci': 'm',     # le merci
        'oeuvre': 'f',    # l'oeuvre
        'poste': 'm',     # le poste (usually m, but la poste for post office)
        'espace': 'm',    # l'espace
        'gorge': 'f',     # la gorge
        'ministre': 'm',  # le/la ministre (can be both)
        'somme': 'f',     # la somme
        'couple': 'm',    # le couple
        'professeur': 'm', # le professeur (can be f in modern usage)
        'gosse': 'm',     # le/la gosse (can be both)
        'môme': 'm',      # le/la môme (can be both)
        'manche': 'f',    # la manche (sleeve), but le manche (handle)
        'arabe': 'm',     # l'arabe
        'élève': 'm',     # l'élève (can be both)
        'aide': 'f',      # l'aide
        'chéri': 'm',     # le chéri
        'radio': 'f',     # la radio
        'artiste': 'm',   # l'artiste (can be both)
        'mode': 'f',      # la mode
        'gloire': 'f',    # la gloire
        'barbe': 'f',     # la barbe
        'communiste': 'm', # le/la communiste
        'voile': 'm',     # le voile
        'justice': 'f',   # la justice
        'mai': 'm',       # le mai
        'peintre': 'm',   # le peintre (can be f)
        'imbécile': 'm',  # l'imbécile (can be both)
        'secrétaire': 'm', # le/la secrétaire
        'auto': 'f',      # l'auto(mobile)
        'adulte': 'm',    # l'adulte (can be both)
        'commissaire': 'm', # le commissaire (can be f)
        'carrière': 'f',  # la carrière
        'i': 'm',         # le i
        'vase': 'm',      # le vase
        'propriétaire': 'm', # le/la propriétaire
        'collègue': 'm',  # le/la collègue
        'pratique': 'f',  # la pratique
        'boche': 'm',     # le boche
        'critique': 'm',  # le/la critique
        'journaliste': 'm', # le/la journaliste
        'crème': 'f',     # la crème
        'domestique': 'm', # le/la domestique
        'orange': 'f',    # l'orange
        'mousse': 'f',    # la mousse
        'concierge': 'm', # le/la concierge
        'esclave': 'm',   # l'esclave (can be both)
        'technique': 'f', # la technique
        'souris': 'f',    # la souris
        'fonctionnaire': 'm', # le/la fonctionnaire
        'vapeur': 'f',    # la vapeur
        'malaise': 'm',   # le malaise
        'manoeuvre': 'f', # la manoeuvre (action), le manoeuvre (worker)
        'hérétique': 'm', # l'hérétique
        'adversaire': 'm', # l'adversaire
        'office': 'm',    # l'office
        'touriste': 'm',  # le/la touriste
        'plastique': 'm', # le plastique
        'ordonnance': 'f', # l'ordonnance
        'guide': 'm',     # le/la guide
        'ancêtre': 'm',   # l'ancêtre
        'philosophe': 'm', # le philosophe
        'amateur': 'm',   # l'amateur
        'remarque': 'f',  # la remarque
        'prof': 'm',      # le/la prof
        'poêle': 'm',     # le poêle
        'litre': 'm',     # le litre
        'alentour': 'm',  # l'alentour
        'photographe': 'm', # le/la photographe
        'spécialiste': 'm', # le/la spécialiste
        'ivrogne': 'm',   # l'ivrogne
        'partenaire': 'm', # le/la partenaire
        'foudre': 'f',    # la foudre
        'disciple': 'm',  # le disciple
        'locataire': 'm', # le/la locataire
        'claque': 'f',    # la claque
        'enseigne': 'f',  # l'enseigne
        'tien': 'm',      # le tien
        'bosse': 'f',     # la bosse
        'pédal': 'm',     # le pédal
        'pendule': 'f',   # la pendule
        'notable': 'm',   # le notable
        'trompette': 'f', # la trompette
        'aigle': 'm',     # l'aigle
        'pilote': 'm',    # le pilote
        'diplomate': 'm', # le diplomate
        'cycliste': 'm',  # le/la cycliste
        'mannequin': 'm', # le mannequin
        'tap': 'm',       # le tap
        'pensionnaire': 'm', # le/la pensionnaire
        'galer': 'm',     # le galer
        'rebelle': 'm',   # le/la rebelle
        'intermédiaire': 'm', # l'intermédiaire
        'infirme': 'm',   # l'infirme
        'cartouche': 'f', # la cartouche
        'indigène': 'm',  # l'indigène
        'moule': 'f',     # la moule
        'compatriote': 'm', # le/la compatriote
        'solde': 'f',     # la solde
        'crêpe': 'f',     # la crêpe
        'paillasse': 'f', # la paillasse
        'hymne': 'm',     # l'hymne
        'interprète': 'm', # l'interprète
        'sandal': 'm',    # le sandal
        'fleuriste': 'm', # le/la fleuriste
        'major': 'm',     # le major
        'micro': 'm',     # le micro
        'jockey': 'm',    # le jockey
        'psychiatre': 'm', # le/la psychiatre
        'nomade': 'm',    # le/la nomade
        'coco': 'm',      # le coco
        'contraint': 'm', # le contraint
        'plain': 'm',     # le plain
        'architecte': 'm', # l'architecte
        'anarchiste': 'm', # l'anarchiste
        'faste': 'm',     # le faste
        'avant-guerre': 'f', # l'avant-guerre
        'dixième': 'm',   # le dixième
        'pique': 'f',     # la pique
        'antiquaire': 'm', # l'antiquaire
        'comptable': 'm', # le/la comptable
        'patriote': 'm',  # le patriote
        'gîte': 'm',      # le gîte
        'man': 'm',       # le man
        'décombre': 'm',  # le décombre
        'convive': 'm',   # le/la convive
        'bourre': 'f',    # la bourre
        'faune': 'f',     # la faune
        'gaulliste': 'm', # le/la gaulliste
        'hirondelle': 'f', # l'hirondelle
        'fanatique': 'm', # le fanatique
        'martyre': 'm',   # le martyre
        'relâche': 'f',   # la relâche
        'greffe': 'f',    # la greffe
        'casse': 'f',     # la casse
        'auxiliaire': 'm', # l'auxiliaire
        'dentiste': 'm',  # le/la dentiste
        'somnambule': 'm', # le/la somnambule
        'pupille': 'f',   # la pupille
        'automate': 'm',  # l'automate
        'syrte': 'f',     # la syrte
        'coke': 'm',      # le coke
        'arbitre': 'm',   # l'arbitre
        'libraire': 'm',  # le/la libraire
        'garagiste': 'm', # le garagiste
        'pianiste': 'm',  # le/la pianiste
        'invalide': 'm',  # l'invalide
        'prolétaire': 'm', # le prolétaire
        'clope': 'f',     # la clope
        'sandwiche': 'm', # le sandwich
        'représaille': 'f', # la représaille
        'momi': 'm',      # le momi
        'vétérinaire': 'm', # le/la vétérinaire
        'parachutiste': 'm', # le/la parachutiste
        'masaï': 'm',     # le masaï
        'dactylo': 'f',   # la dactylo
        'athée': 'm',     # l'athée
        'archéologue': 'm', # l'archéologue
        'pub': 'f',       # la pub
        'milliardaire': 'm', # le/la milliardaire
        'guitariste': 'm', # le/la guitariste
        'athlète': 'm',   # l'athlète
        'dignitaire': 'm', # le dignitaire
        'métèque': 'm',   # le métèque
        'terroriste': 'm', # le/la terroriste
        'acrobate': 'm',  # l'acrobate
        'punk': 'm',      # le punk
        'cache': 'f',     # la cache
        'pompiste': 'm',  # le pompiste
        'novice': 'm',    # le novice
        'romance': 'f',   # la romance
        'der': 'm',       # le der
        'aristocrate': 'm', # l'aristocrate
        'môle': 'm',      # le môle
        'détective': 'm', # le détective
        'bohème': 'f',    # la bohème
        'rouquemoute': 'f', # la rouquemoute
        'gynécologue': 'm', # le/la gynécologue
        'psy': 'm',       # le/la psy
        'carpe': 'f',     # la carpe
        'automobiliste': 'm', # l'automobiliste
        'psychologue': 'm', # le/la psychologue
        'orge': 'f',      # l'orge
        'séminariste': 'm', # le séminariste
        'baume': 'm',     # le baume
        'corsaire': 'm',  # le corsaire
        'palabre': 'f',   # la palabre
        'intempérie': 'f', # l'intempérie
        'basket': 'm',    # le basket
        'psychanalyste': 'm', # le/la psychanalyste
        'matricule': 'm', # le matricule
        'yougoslave': 'm', # le/la yougoslave
        'germain': 'm',   # le germain
        'mercenaire': 'm', # le mercenaire
        'platine': 'f',   # la platine
        'bougnoule': 'm', # le bougnoule
        'aubergiste': 'm', # l'aubergiste
        'frusque': 'f',   # la frusque
        'orfèvre': 'm',   # l'orfèvre
        'hirondeau': 'm', # l'hirondeau
        'après-guerre': 'f', # l'après-guerre
        'bure': 'f',      # la bure
        'salin': 'm',     # le salin
        'condisciple': 'm', # le condisciple
        'virtuose': 'm',  # le/la virtuose
        'petit-enfant': 'm', # le petit-enfant
        'prolo': 'm',     # le prolo
        'rocker': 'm',    # le rocker
        'tartare': 'm',   # le tartare
        'fan': 'm',       # le/la fan
        'mandataire': 'm', # le mandataire
        'gréviste': 'm',  # le/la gréviste
        'alchimiste': 'm', # l'alchimiste
        'autochtone': 'm', # l'autochtone
        'donne': 'f',     # la donne
        'adepte': 'm',    # l'adepte
        'finale': 'f',    # la finale
        'idéaliste': 'm', # l'idéaliste
        'missionnaire': 'm', # le missionnaire
        'lessiveur': 'm', # le lessiveur
        'gauchiste': 'm', # le/la gauchiste
        'méninge': 'f',   # la méninge
        'cornette': 'f',  # la cornette
        'rombier': 'm',   # le rombier
        'claude': 'm',    # le claude
        'coca': 'm',      # le coca
        'motocycliste': 'm', # le/la motocycliste
        'berceur': 'm',   # le berceur
        'esthète': 'm',   # l'esthète
        'loquedu': 'm',   # le loquedu
        'bibliothécaire': 'm', # le/la bibliothécaire
        'stagiaire': 'm', # le/la stagiaire
        'collabo': 'm',   # le collabo
        'violoniste': 'm', # le/la violoniste
        'tortionnaire': 'm', # le tortionnaire
        'diamantaire': 'm', # le diamantaire
        'correctionnel': 'm', # le correctionnel
        'dépositaire': 'm', # le dépositaire
        'éden': 'm',      # l'éden
        'charentais': 'm', # le charentais
        'vêpre': 'f',     # la vêpre
        'affre': 'f',     # l'affre
        'honoraire': 'm', # l'honoraire
        'muqueux': 'm',   # le muqueux
        'ponte': 'm',     # le ponte
        'ébat': 'm',      # l'ébat
        'mioche': 'm',    # le/la mioche
        'destinataire': 'm', # le destinataire
        'noctambule': 'm', # le/la noctambule
        'flashe': 'm',    # le flashe
        'chromo': 'm',    # le chromo
        'déshérité': 'm', # le déshérité
        'saltimbanque': 'm', # le saltimbanque
        'opalin': 'm',    # l'opalin
        'congénère': 'm', # le congénère
        'cosaque': 'm',   # le cosaque
        'millionnaire': 'm', # le/la millionnaire
        'bouquiniste': 'm', # le/la bouquiniste
        'bénéficiaire': 'm', # le/la bénéficiaire
        'quinquagénaire': 'm', # le/la quinquagénaire
        'pro': 'm',       # le pro
        'soprano': 'm',   # le/la soprano
        'protagoniste': 'm', # le/la protagoniste
        'entrefaite': 'f', # l'entrefaite
        'souillard': 'm', # le souillard
        'dope': 'f',      # la dope
        'étale': 'f',     # l'étale
        'maure': 'm',     # le maure
        'permissionnaire': 'm', # le permissionnaire
        'réceptionniste': 'm', # le/la réceptionniste
        'mythomane': 'm', # le/la mythomane
        'créole': 'm',    # le/la créole
        'coche': 'f',     # la coche
        'moraliste': 'm', # le moraliste
        'externe': 'm',   # l'externe
        'serbe': 'm',     # le serbe
        'die': 'f',       # la die
        'cinéaste': 'm',  # le/la cinéaste
        'suspense': 'm',  # le suspense
        'comparse': 'm',  # le/la comparse
        'humaniste': 'm', # l'humaniste
        'automitrailleur': 'm', # l'automitrailleur
        'amerloque': 'm', # l'amerloque
        'accordéoniste': 'm', # l'accordéoniste
        'retardataire': 'm', # le retardataire
        'factionnaire': 'm', # le factionnaire
        'magnéto': 'm',   # le magnéto
        'croate': 'm',    # le croate
        'rustre': 'm',    # le rustre
        'funambule': 'm', # le funambule
        'douairier': 'm', # le douairier
        'bureaucrate': 'm', # le bureaucrate
        'espingo': 'm',   # l'espingo
        'pamplemousse': 'm', # le pamplemousse
        'archiviste': 'm', # l'archiviste
        'modiste': 'f',   # la modiste
        'chimiste': 'm',  # le/la chimiste
        'manucure': 'f',  # la manucure
        'oripeau': 'm',   # l'oripeau
        'ébéniste': 'm',  # l'ébéniste
        'standardiste': 'm', # le/la standardiste
        'exhibitionniste': 'm', # l'exhibitionniste
        'sociologue': 'm', # le/la sociologue
        'israélite': 'm', # l'israélite
        'épileptique': 'm', # l'épileptique
        'dilettante': 'm', # le dilettante
        'énergumène': 'm', # l'énergumène
        'instit': 'm',    # l'instit
        'alpiniste': 'm', # l'alpiniste
        'transat': 'm',   # le transat
        'apache': 'm',    # l'apache
        'pédagogue': 'm', # le pédagogue
        'sikh': 'm',      # le sikh
        'quadragénaire': 'm', # le/la quadragénaire
        'abdominal': 'm', # l'abdominal
        'extraterrestre': 'm', # l'extraterrestre
        'légiste': 'm',   # le légiste
        'réserviste': 'm', # le réserviste
        'bolchevik': 'm', # le bolchevik
        'astronome': 'm', # l'astronome
        'vigile': 'm',    # le vigile
        'matche': 'm',    # le matche
        'aristo': 'm',    # l'aristo
        'cannibale': 'm', # le cannibale
        'teneur': 'f',    # la teneur
        'alcoolo': 'm',   # l'alcoolo
        'homo': 'm',      # l'homo
        'gymnaste': 'm',  # le/la gymnaste
        'philologue': 'm', # le philologue
        'choriste': 'm',  # le/la choriste
        'entomologiste': 'm', # l'entomologiste
        'schizophrène': 'm', # le/la schizophrène
        'autodidacte': 'm', # l'autodidacte
        'entournure': 'f', # l'entournure
        'moujingue': 'm', # le moujingue
        'petro': 'm',     # le petro
        'oto-rhino': 'm', # l'oto-rhino
        'apatride': 'm',  # l'apatride
        'téléphoniste': 'm', # le/la téléphoniste
        'concessionnaire': 'm', # le concessionnaire
        'démêlé': 'm',    # le démêlé
        'néophyte': 'm',  # le néophyte
        'miro': 'm',      # le miro
        'commissionnaire': 'm', # le commissionnaire
        'rotond': 'm',    # le rotond
        'franquiste': 'm', # le franquiste
        'cinquantième': 'm', # le cinquantième
        'saussaie': 'f',  # la saussaie
        'régicide': 'm',  # le régicide
        'anar': 'm',      # l'anar
        'trotskiste': 'm', # le trotskiste
        'cosmétique': 'm', # le cosmétique
        'septuagénaire': 'm', # le/la septuagénaire
        'arpète': 'm',    # l'arpète
        'mini': 'f',      # la mini
        'aune': 'f',      # l'aune
        'garde-malade': 'm', # le/la garde-malade
        'bégonia': 'm',   # le bégonia
        'parano': 'm',    # le parano
        'machiniste': 'm', # le machiniste
        'chausse': 'f',   # la chausse
        'brandebourg': 'm', # le brandebourg
        'taoïste': 'm',   # le taoïste
        'meulier': 'm',   # le meulier
        'commanditaire': 'm', # le commanditaire
        'yankee': 'm',    # le yankee
        'alto': 'm',      # l'alto
        'tronçonneur': 'm', # le tronçonneur
        'souillon': 'm',  # le souillon
        'analyste': 'm',  # l'analyste
        'intello': 'm',   # l'intello
        'statuaire': 'm', # le statuaire
        'soliste': 'm',   # le/la soliste
        'arrière-grand-parent': 'm', # l'arrière-grand-parent
        'pandore': 'm',   # le pandore
        'astrologue': 'm', # l'astrologue
        'surgé': 'm',     # le surgé
        'fusilier-marin': 'm', # le fusilier-marin
        'typographe': 'm', # le typographe
        'traditionaliste': 'm', # le traditionaliste
        'vandale': 'm',   # le vandale
        'garenne': 'f',   # la garenne
        'pécore': 'f',    # la pécore
        'sexagénaire': 'm', # le/la sexagénaire
        'activiste': 'm', # l'activiste
        'barbouze': 'f',  # la barbouze
        'scarlatin': 'm', # le scarlatin
        'proxénète': 'm', # le proxénète
        'fortif': 'f',    # la fortif
        'étampe': 'f',    # l'étampe
        'organiste': 'm', # l'organiste
        'trapéziste': 'm', # le/la trapéziste
        'hellène': 'm',   # l'hellène
        'cadène': 'f',    # la cadène
        'travailliste': 'm', # le travailliste
        'humoriste': 'm'  # l'humoriste
    }
    
    df = pd.DataFrame(list(overrides.items()), columns=['lemme', 'gender'])
    df.to_csv('main/gender_overrides.csv', index=False)
    print("Created gender_overrides.csv with all gender overrides")

def check_word_frequency(words):
    """Check frequency data for specified words"""
    lexique_df = pd.read_csv('main/Lexique383.tsv', sep='\t')
    for word in words:
        word_data = lexique_df[lexique_df['lemme'] == word]
        print(f"\nFrequency data for '{word}':")
        print(word_data[['ortho', 'lemme', 'cgram', 'freqlivres']].to_string())

if __name__ == '__main__':
    check_word_frequency(['aune', 'miro'])
    create_gender_overrides_file() 