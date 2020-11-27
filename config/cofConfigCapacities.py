# -*- coding: utf-8 -*-
from cof.properties import *
from ClusterShell.NodeSet import RangeSet

capacities = {
    "capacities": [
      {
        "oid": "http://co-drs.org/capacites/nuees-de-criquets/",
        "count": 1,
        "full_description": "Cette capacité remplace la capacité «Nuée d’insectes». En réussissant "
                            "un test d’attaque magique (portée 20 m), le druide libère sur sa cible "
                            "une nuée de criquet affamés qui la dévorent à petit feu pendant "
                            "[5 + Mod de SAG.] tours. La victime subit 2 points de DM par tour et "
                            "un malus de -3 à toutes ses actions. Les DM de zone détruisent la nuée.",
        "short_description": "Sur une attaque magique réussie, le druide libère sur sa cible une "
                            "nuée de criquet affamés qui la dévorent à petit feu.",
        "limited": True,
        "name": "Nuées de criquets",
        "range": Range(value=20, unit="m"),
        "duration": Duration(value="5+[SAG]", unit="tr"),
        "special_property": [
              "Destruction: DM de zone uniquement",
              "Cible: malus -3 à toutes ses actions",
              "Cible: 2 DM / tr"
        ],
        "way_rank": 1,
        "wid": "unknown-id_voie-des-vermines"
      },
      {
        "oid": "http://co-drs.org/capacites/cone-de-froid/",
        "count": 1,
        "full_description": "Le cône de affecte toute les créatures dans un cône approximatif de "
                            "20 mètres de long sur 10 mètres de large à son extrémité. Les "
                            "victimes subissent [2d6+Mod d’INT] DM et sont Ralenties pour 1 tour "
                            "si elles ratent un test de CON difficulté 13. Sinon, elles subissent "
                            "seulement la moitié des DM et ne sont pas ralenties.",
        "short_description": "Un cône de froid qui sort des mains de l'ensorceleur et affecte "
                             "toutes créatures prises à l'intérieure.",
        "limited": True,
        "name": "Cône de froid",
        "range": Range(value=20, unit="m"),
        "area": Area(value=10, unit="m"),
        "attack": Attack(
          atype="magical",
          damages=Damage(
            base=[],
            other=[Mod(die=6, count=2, target="froid"),
                   Mod(target="INT", mtype="+")],
          ),
          critical=RangeSet([20])
        ),
        "duration": Duration(value="1", unit="tr"),
        "special_property": [
              "Test CON < 13: Ralenti",
              "Test CON >= 12: DM / 2"
        ],
        "way_rank": 3,
        "wid": "unknown-id_voie-du-gel"
      }

    ],
    'http://co-drs.org/capacites/aura-feerique/': {'wid': 'Unknown-id_aura-feerique'},
    'addons': {
      "http://co-drs.org/capacites/6eme-sens/": {
          "short_description": "L’Ensorceleur sait toujours légèrement en avance ce qui va arriver.",
          "special_property": ["Initiative: +1 / rang dans la voie",
                               "DEF: +1 / rang dans la voie",
                               "Éviter d'être surpris : +2 / rang dans la voie"]
      },
      "http://co-drs.org/capacites/a-couvert/": {
        "short_description": "Jusqu’à son prochain tour, l’Arquebusier divise par 2 les DM dus aux attaques à "
                             "distance et de zone qu’il reçoit, et peut se déplacer de 20 mètres."
      },
      "http://co-drs.org/capacites/absorber-un-coup/": {
        "short_description": "A son tour, le Guerrier fait seulement une action d’attaque ou de déplacement."
      },
      "http://co-drs.org/capacites/acrobate/": {
        "short_description": "Le Barde obtient un bonus de +2 par rang à tous ses tests de DEX visant à réaliser "
                             "des acrobaties, tenir en équilibre, faire des sauts ou de l’escalade."
      },
      "http://co-drs.org/capacites/acrobaties/": {
        "short_description": "Si le Voleur réussit un test de DEX difficulté 15, il peut effectuer une acrobatie "
                             "pour franchir un obstacle ou pour surprendre son adversaire par une cabriole."
      },
      "http://co-drs.org/capacites/action-concertee/": {
        "short_description": "Une fois par tour, l’Arquebusier peut échanger son Initiative avec un autre "
                             "personnage volontaire."
      },
      "http://co-drs.org/capacites/adaptable/": {
        "short_description": "Après avoir raté un test de Carac., le personnage obtient un bonus de +5 au test "
                             "s’il a la possibilité de retenter la même action au tour suivant."
      },
      "http://co-drs.org/capacites/agrandissement/": {
        "short_description": "Le Magicien ou une cible volontaire (au contact) voit sa taille augmenter de "
                             "50%.",
        "skill": [Mod(mtype="+", count=2, label="Test", target="FOR"),
                  Mod(mtype="-", count=2, label="Test", target="DEX")],
        "duration": Duration(value="5+[INT]", unit="tr"),
        "special_property": ["DM : +2"]
                            
      },
      "http://co-drs.org/capacites/agripper/": {
        "short_description": "Sur un résultat de 15-20 au d20 en attaque, la créature agrippe sa proie et ne la "
                             "lâche plus."
      },
      "http://co-drs.org/capacites/ailes-celestes/": {
        "short_description": "Des ailes divines poussent dans le dos du Prêtre, qui peut voler à une vitesse "
                             "équivalente à deux fois son déplacement normal.",
        "duration": Duration(value="5+[SAG]", unit="tr"),
        "special_property": ["Vol stationnaire (action de mouvement)"]
      },
      "http://co-drs.org/capacites/ambidextrie/": {
        "short_description": "Le Voleur peut à présent utiliser une arme dans chaque main sans pénalité."
      },
      "http://co-drs.org/capacites/amitie/": {
        "short_description": "Si l’Ensorceleur réussit un test d’Attaque magique contre le score max de PV "
                             "d'une cible humanoïde, celle-ci se comporte comme un ami de longue date tant "
                             "qu’elle n’est pas attaquée.",
        "range": Range(value=10, unit="m"),
        "special_property": ["Résister: Test SAG > 12 + [CHA]",
                             "Résister: (1 fois / jour)"]
      },
      "http://co-drs.org/capacites/animal-fabuleux/": {
        "short_description": "Le loup du Rôdeur devient un spécimen particulièrement puissant."
      },
      "http://co-drs.org/capacites/animal-fabuleux-2/": {
        "short_description": "L’ours du Rôdeur devient un spécimen en pleine possession de ses moyens."
      },
      "http://co-drs.org/capacites/animation-des-morts/": {
        "short_description": "Le Nécromancien anime anime (1/rang) le cadavre d’un humanoïde "
                             "de taille moyenne, décédé depuis moins d’une heure. Le zombi "
                             "comprend les ordres: Attaquer, Suivre, Garder et Pas bouger. Il "
                             "se déplace 2 fois moins vite, perd 1 PV/min et à 0 PV tombe en "
                             "poussière.",
        "creature": [ Mod(label="monster", target="monster-name", count="Zombi"),
                  Mod(label="monster", target="PV", count=12),
                  Mod(label="monster", target="init", count="8"), 
                  Mod(label="monster", target="DEF", count=10), 
                  Mod(label="monster", target="attack-melee", count="+3: 1d6+1")],
      },
      "http://co-drs.org/capacites/animation-d-un-arbre/": {
        "short_description": "Une fois par combat, le Druide peut animer un arbre en le touchant.",
        "duration": Duration(value="[niveau]", unit="tr")
      },
      "http://co-drs.org/capacites/animer-un-cadavre/": {
        "short_description": "Ce pouvoir permet d’animer le cadavre d’une créature morte pendant le combat."
      },
      "http://co-drs.org/capacites/archer-emerite/": {
        "short_description": "Lorsqu’il utilise un arc, l’elfe sylvain obtient une réussite critique sur un "
                             "résultat de 19-20 au d20."
      },
      "http://co-drs.org/capacites/argument-de-taille/": {
        "short_description": "Le Barbare ajoute son Mod. de FOR à son score de PV maximum ainsi qu’à ses tests "
                             "de CHA et à ceux de ses alliés au contact pour les tests de négociation, de "
                             "persuasion ou d’intimidation."
      },
      "http://co-drs.org/capacites/arme-benie/": {
        "short_description": "Le Prêtre bénit son arme sacrée. S’il obtient un résultat de « 1 » sur son dé de "
                             "DM, il relance le dé et garde le second résultat."
      },
      "http://co-drs.org/capacites/arme-dansante/": {
        "short_description": "Le sort crée une lame d’énergie lumineuse. Dès le premier tour, l’Ensorceleur "
                                 "peut lui ordonner d’attaquer une cible de son choix (action gratuite).",
        "duration": Duration(value="5+[CHA]", unit="tr"),
        "attack": Attack(
          atype='magical',
          range=Range(value=20, unit="m"),
          damages=Damage(
            base=[],
            other=[Mod(die=8, count=1),Mod(mtype="+", target="CHA")],
          ),
          critical=RangeSet([20])
        ),

      },
      "http://co-drs.org/capacites/arme-de-predilection/": {
        "short_description": "Le Guerrier choisit une arme de prédilection et gagne +1 en attaque lorsqu’il "
                             "l’utilise."
      },
      "http://co-drs.org/capacites/arme-d-argent/": {
        "short_description": "Ce miracle crée pour la durée du combat une arme d’argent et de lumière que seul "
                             "le Prêtre peut utiliser.",
        "duration": Duration(value="", unit="Combat"),
        "attack": Attack(
          atype='melee',
          damages=Damage(
            base=[],
            other=[Mod(die=6, count=1),Mod(mtype="+", target="SAG")],
          ),
          critical=RangeSet([20])
        ),
        "special_property": [
          "Démon: attaque +2, DM +1d6"
          "Mort vivant: attaque +2, DM +1d6"
        ]

      },
      "http://co-drs.org/capacites/arme-enflammee/": {
        "short_description": "Le Magicien peut enflammer une arme qui infige alors des dégâts "
                             "supplémentaires de feu.",
        "special_property": ["DM arme enflamée: +1d6 feu"],
        "duration": Duration(value="5+[INT]", unit="tr")
      },
      "http://co-drs.org/capacites/arme-secrete/": {
        "short_description": "Une fois par combat, le Barde peut utiliser un subterfuge de séducteur pour "
                             "surprendre et déstabiliser un adversaire du sexe opposé."
      },
      "http://co-drs.org/capacites/armee-des-morts/": {
        "short_description": "Une fois par jour, le Nécromancien peut invoquer d’innombrables squelettes "
                             "émergeant du sol pour attaquer ses ennemis"
      },
      "http://co-drs.org/capacites/armure-de-mage/": {
        "short_description": "Le Magicien fait apparaître un nuage magique argenté qui le protège contre les "
                             "attaques adverses.",
        "defense": [Mod(label="DEF", target="", count=4, mtype="+", limitation="Seulement +2 si on porte une armure")],
        "duration": Duration(value="", unit="combat")
      },
      "http://co-drs.org/capacites/armure-de-vent/": {
        "short_description": "Le Barbare obtient un bonus en DEF égal à son Rang dans la voie lorsqu’il ne porte "
                             "aucune armure."
      },
      "http://co-drs.org/capacites/armure-lourde/": {
        "short_description": "Le Guerrier peut porter une Armure de Plaque."
      },
      "http://co-drs.org/capacites/armure-magique/": {
        "short_description": "La créature possède un pouvoir magique qui lui permet de diviser tous les DM "
                             "physiques subits par 2 pour le reste du combat."
      },
      "http://co-drs.org/capacites/armure-naturelle/": {
        "short_description": "Le Guerrier a endurci son corps. Il bénéficie d’un bonus de +2 à la DEF."
      },
      "http://co-drs.org/capacites/armure-sur-mesure/": {
        "short_description": "L’armure du Chevalier est parfaitement ajustée, aussi il n’ajoute que la moitié "
                             "de sa DEF à la difficulté des tests où l'armure inflige une pénalité."
      },
      "http://co-drs.org/capacites/arret-du-temps/": {
        "short_description": "Le Magicien arrête le temps pendant [1d6 + Mod. d’INT] tours."
      },
      "http://co-drs.org/capacites/artefact-majeur/": {
        "short_description": "Le Forgesort peut enchanter des objets."
      },
      "http://co-drs.org/capacites/as-de-la-gachette/": {
        "short_description": "Lorsqu’il atteint une DEF de 25 ou plus sur son attaque à distance avec une arme "
                             "à poudre ou une arbalète, l’Arquebusier ajoute +1d6 aux DM de son attaque.",
      },
      "http://co-drs.org/capacites/ascetisme/": {
        "short_description": "Le Moine peut subsister sans nourriture, sans eau et sans sommeil pendant "
                             "[5 + Mod. SAG] jour."
      },
      "http://co-drs.org/capacites/aspect-de-la-succube/": {
        "short_description": "Le Nécromancien acquiert une beauté fascinante. S'il utilise l'attaque magique, "
                             "les DM de celle-ci lui régénère autant de PV.",
        "duration": Duration(value="5+[INT]", unit="tr"),
        "attack": Attack(
          atype='magical',
          name="(contact)",
          damages=Damage(
            base=[],
            other=[Mod(die=4, count=1),Mod(mtype="+", target="CHA")],
          ),
          critical=RangeSet([20])
        ),
        "skill": [Mod(label="Test", target="CHA", count=5, mtype="+")],
        "special_property": ["DM d'attaque transformée en PV"]
      },
      "http://co-drs.org/capacites/aspect-du-demon/": {
        "short_description": "Le Nécromancien prend l’apparence d’un démon. Elle ne peut pas se "
                             "cumuler avec la potion d'aspect de la succube.",
        "duration": Duration(value="5+[INT]", unit="tr"),
        "skill": [Mod(label="Test", target="FOR", count=2, mtype="+"),
                  Mod(label="Test", target="DEX", count=2, mtype="+"),
                  Mod(label="Test", target="CON", count=2, mtype="+")],
        "attack": Attack(
          atype='melee',
          name="griffe [ x2 (L) ]",
          damages=Damage(
            other=[Mod(die=6, count=1),
                  Mod(mtype="+", count=4, target='natural')],
          ),
          critical=RangeSet([20])
        ),
        "special_property": ["Attaque au contact: +2", "DEF: +2"]
      },
      "http://co-drs.org/capacites/asphyxie/": {
        "short_description": "Avec une attaque magique, le magicien prive la créature "
                             "ciblée d’air. La victime étouffe progressivement et subit des dégâts à chaque tour.",
        "range": Range(value=20,unit="m"),
        "duration": Duration(value="1+[INT]", unit="tr"),
        "attack": Attack(
              atype='magical',
              damages=Damage(
                  other=[Mod(die=6, count=1)],
              ),
              critical=RangeSet([20])
        ),
      },
      "http://co-drs.org/capacites/assassinat/": {
        "short_description": "Au premier tour de combat, si la cible est Surprise, une Attaque mortelle réussie "
                             "l’oblige à réussir un test de CON difficulté 15 ou tomber à 0 PV.",
      },
      "http://co-drs.org/capacites/attaque-bondissante/": {
        "short_description": "Le Druide parcourt jusqu’à 30 m et bénéficie d’un bonus de +5 au test d’attaque "
                             "et de +1d6 aux DM contre sa cible."
      },
      "http://co-drs.org/capacites/attaque-brutale/": {
        "short_description": "Le Barbare réalise une attaque au contact avec une pénalité de -2 en attaque et "
                             "+1d6 au DM."
      },
      "http://co-drs.org/capacites/attaque-circulaire/": {
        "short_description": "Le Guerrier peut tenter une attaque au contact contre chaque adversaire engagé au"
                             " contact avec lui.",
      },
      "http://co-drs.org/capacites/attaque-eclair/": {
        "short_description": "Le Rôdeur peut effectuer une attaque au contact très percutante."
      },
      "http://co-drs.org/capacites/attaque-en-finesse/": {
        "short_description": "Le Voleur peut utiliser son score d’Attaque à distance pour une attaque au "
                             "contact lorsqu’il utilise une arme légère comme une dague ou une rapière."
      },
      "http://co-drs.org/capacites/attaque-en-traitre/": {
        "short_description": "Une fois par tour, si un allié blesse une créature au contact du Voleur, celui-ci "
                             "peut lui porter une attaque normale gratuite."
      },
      "http://co-drs.org/capacites/attaque-en-traitre-2/": {
        "short_description": "Si la créature attaque en même temps qu’un allié, de dos ou par surprise, elle "
                             "réalise une Attaque sournoise."
      },
      "http://co-drs.org/capacites/attaque-flamboyante/": {
        "short_description": "Le style de combat du Barde est flamboyant et surprenant"
      },
      "http://co-drs.org/capacites/attaque-magique/": {
        "short_description": "La créature possède un pouvoir magique qui inflige [1d6 x NC] DM sur un test "
                             "d’attaque magique réussi (portée 30 m) sur une cible unique."
      },
      "http://co-drs.org/capacites/attaque-mortelle/": {
        "short_description": "Une attaque similaire à l’Attaque sournoise du Voleur qui doit être exécutée "
                             "de dos ou par surprise."
      },
      "http://co-drs.org/capacites/attaque-paralysante/": {
        "short_description": "Une fois par combat, le Voleur peut, en réussissant une attaque de contact, "
                             "paralyser un adversaire de douleur."
      },
      "http://co-drs.org/capacites/attaque-parfaite/": {
        "short_description": "Lancez deux d20 en attaque au contact et gardez le meilleur résultat, "
                             "ajoutez +1d6 aux DM.",
      },
      "http://co-drs.org/capacites/attaque-puissante/": {
        "short_description": "Le Guerrier peut choisir d’utiliser 1d12 en attaque au contact au lieu du d20 "
                             "habituel. En cas de réussite, il ajoute +2d6 aux DM."
      },
      "http://co-drs.org/capacites/attaque-sanglante/": {
        "short_description": "Le demi-orque réalise une attaque de contact violente qui provoque une hémorragie."
      },
      "http://co-drs.org/capacites/attaque-sonore/": {
        "short_description": "Le barde pousse un cri dont les effets sont dévastateurs."
      },
      "http://co-drs.org/capacites/attaque-sournoise/": {
        "short_description": "Quand il attaque un adversaire dans le dos* ou par surprise, le Voleur inflige "
                             "1d6 de DM supplémentaires par rang possédé dans cette voie."
      },
      "http://co-drs.org/capacites/attaque-tourbillon/": {
        "short_description": "Une fois par combat, le Barbare tourne sur lui-même en assénant des attaques à "
                             "toutes les cibles au contact."
      },
      "http://co-drs.org/capacites/aura-feerique/": {
        "short_description": "La victime se voit entourée d’un halo lumineux coloré qui permet de la distinguer "
                             "facilement dans le noir et lui interdit de se rendre invisible."
      },
      "http://co-drs.org/capacites/autorite-naturelle/": {
        "short_description": "Le chevalier obtient un bonus égal à [1 + Mod. de CHA] en Initiative et en DEF."
      },
      "http://co-drs.org/capacites/baies-magiques/": {
        "short_description": "Le Druide fait pousser des fruits qu’il peut cueillir. Chaque fruit offre "
                             "l’équivalent d’un repas."
      },
      "http://co-drs.org/capacites/baiser-du-vampire/": {
        "short_description": "Le Nécromancien fait une attaque infligeant des "
                             "dégâts qui lui permettent de récupèrer autant de PV.",
        "attack": Attack(
          atype='magical',
          range=Range(value=50, unit="m"),
          damages=Damage(
            base=[],
            other=[Mod(die=8, count=1), Mod(target="INT", mtype="+", label="(DM => PV)")],
          ),
          critical=RangeSet([20])
        ),
        "special_property": ["Ne peut pas dépasser son score de PV"]
      },
      "http://co-drs.org/capacites/balayage/": {
        "short_description": "La créature utilise sa grande taille pour affecter plusieurs créatures face à "
                             "elle d’un seul coup de patte/arme."
      },
      "http://co-drs.org/capacites/baton-de-druide/": {
        "short_description": "Le Druide combat avec les deux extrémités de son bâton de bois noueux."
      },
      "http://co-drs.org/capacites/baton-de-mage/": {
        "short_description": "Le Forgesort crée un grand bâton magique."
      },
      "http://co-drs.org/capacites/benediction/": {
        "short_description": "Le Prêtre entonne un chant pour encourager ses compagnons en vue. "
                             "Ceux-ci (ainsi que le Prêtre) bénéficient d’un bonus.",
        "duration": Duration(value="3+[SAG]", unit="tr"),
        "skill": [Mod(label="Test", mtype="+", count=1), Mod(label="Attaque", mtype="+", count=1)]

      },
      "http://co-drs.org/capacites/blocage/": {
        "short_description": "Le Forgesort scelle une porte ou un coffre pour une durée en minutes égale "
                             "à sa valeur d’INT."
      },
      "http://co-drs.org/capacites/bon-pour-le-moral/": {
        "short_description": "Un halfelin qui mange bien est un halfelin heureux. À chaque repas où le personnage "
                             "boit ou mange un met de qualité, il récupère des PV."
      },
      "http://co-drs.org/capacites/bonne-nature/": {
        "short_description": "Le gnome augmente ses valeurs de CON et de CHA de +2."
      },
      "http://co-drs.org/capacites/botte-mortelle/": {
        "short_description": "Lors d’une attaque au contact réussie de +10 par rapport à la défense de son "
                             "adversaire, le Barde obtient un bonus de +2d6 aux DM de son attaque.",
      },
      "http://co-drs.org/capacites/botte-secrete/": {
        "short_description": "Lorsque le Voleur obtient un critique sur une attaque au contact, l’attaque devient"
                             " automatiquement une Attaque sournoise."
      },
      "http://co-drs.org/capacites/bouclier-de-la-foi/": {
        "short_description": "Le Prêtre porte le symbole de sa foi sur son bouclier, ce qui lui confère un bonus "
                             "supplémentaire de +1 en DEF.",
      },
      "http://co-drs.org/capacites/boule-de-feu/": {
        "short_description": "Le magicien lance une boule de feu qui inflige des dégâts à toutes personnes "
                             "(y compris ses alliés) se trouvant dans la zone d'effet.",
        "attack": Attack(
          atype='magical',
          area=Area(value=6, unit="m"),
          range=Range(value=30, unit="m"),
          damages=Damage(
            base=[],
            other=[Mod(die=6, count=4, target="feu"),
                   Mod(target="INT", mtype="+", label="(Échec: DM / 2)")],
          ),
          critical=RangeSet([20])
        ),
        "special_property": ["Test DEX > 10 + [INT]: DM / 2"]
      },
      "http://co-drs.org/capacites/boulet-explosif/": {
        "short_description": "L’Arquebusier sait fabriquer et lancer de petites boules de métal munies de poudre "
                             "et d’une mèche."
      },
      "http://co-drs.org/capacites/briser-les-coeurs/": {
        "short_description": "Le Nécromancien fait mine de broyer le coeur de sa victime."
      },
      "http://co-drs.org/capacites/briseur-d-os/": {
        "short_description": "Les coups critiques du Barbare sont terribles et provoquent des handicaps durables."
      },
      "http://co-drs.org/capacites/cadence-de-tir/": {
        "short_description": "Recharger une pétoire ou un mousquet devient une action de mouvement."
      },
      "http://co-drs.org/capacites/capacite-fabuleuse/": {
        "short_description": "Le joueur choisit une capacité limitée que son personnage connaît. Celle-ci ne "
                             "nécessite dorénavant plus une action limitée pour être utilisée."
      },
      "http://co-drs.org/capacites/capacite-signature/": {
        "short_description": "Une fois par combat, le personnage peut interrompre le court normal du tour pour "
                             "utiliser une capacité limitée choisie en plus de ses actions normales dans le tour.",
      },
      "http://co-drs.org/capacites/capacite-superieure/": {
        "short_description": "Le joueur choisit une capacité limitée que connaît son personnage, lorsqu’il "
                             "utilise cette capacité, il ajoute +1d6 aux DM produits."
      },
      "http://co-drs.org/capacites/capitaine/": {
        "short_description": "Le capitaine donne un bonus de +2 en Initiative, en attaque et aux DM à toutes les "
                             "créatures sous ses ordres à portée de vue."
      },
      "http://co-drs.org/capacites/caracteristique-fabuleuse/": {
        "short_description": "Le joueur augmente de 2 points la valeur de la plus haute Caractéristique de son "
                             "personnage."
      },
      "http://co-drs.org/capacites/cavalier-emerite/": {
        "short_description": "Lorsqu’il est en selle, le Chevalier gagne un bonus de +2 en attaque au contact, "
                             "et sa monture obtient une DEF égale à celle du Chevalier."
      },
      "http://co-drs.org/capacites/cercle-de-protection/": {
        "short_description": "Le Magicien peut tracer un cercle sur le sol pour se protéger des sorts adverses. "
                             "Une fois par tour, lorsqu’un sort (attaque magique) prend pour cible un personnage "
                             "situé dans le cercle, le Magicien fait un test d’attaque magique en opposition "
                             "à celui de l’adversaire. En cas de succès le sort adverse n’a aucun effet.",
        "special_property": [
          "Cercle: Peut contenir 3 personnes"
        ]
      },
      "http://co-drs.org/capacites/chair-a-canon/": {
        "short_description": "Une fois par tour, le PNJ peut décider qu’une attaque qui le visait touche à la "
                             "place un de ses sous-fifres situé à moins de 3 m et venu s’interposer."
      },
      "http://co-drs.org/capacites/chant-des-heros/": {
        "short_description": "Le barde chante et inspire ses compagnons : tous les alliés à portée de voix "
                             "obtiennent un bonus de +1 à tous leurs tests pendant [5+ Mod. de CHA] tours."
      },
    "http://co-drs.org/capacites/charge/": {
        "short_description": "Le Barbare se déplace en ligne droite d’au moins 5 mètres et effectue une attaque "
                             "au contact avec un bonus de +2 en attaque et +1d6 aux DM."
      },
      "http://co-drs.org/capacites/charge-2/": {
        "short_description": "A cheval, le chevalier peut effectuer un déplacement en ligne droite, et une "
                             "attaque de contact placée au moment son choix."
      },
      "http://co-drs.org/capacites/charge-3/": {
        "short_description": "La créature parcourt une distance maximum de 30 mètres et réalise une attaque, "
                             "lancez deux d20 et gardez le meilleur résultat."
      },
      "http://co-drs.org/capacites/charge-fantastique/": {
        "short_description": "Une fois par combat, le Chevalier et tous ses alliés en vue bénéficient d’un "
                             "déplacement en ligne droite, suivi d’une action d’attaque."
      },
      "http://co-drs.org/capacites/charisme-heroique/": {
        "short_description": "Le personnage augmente sa valeur de CHA de +2."
      },
      "http://co-drs.org/capacites/charmant/": {
        "short_description": "Le Barde obtient un bonus de +2 par rang atteint dans cette voie pour tous ses "
                             "tests de CHA visant à séduire, baratiner ou mentir.",
      },
      "http://co-drs.org/capacites/chasseur-emerite/": {
        "short_description": "Le Rôdeur obtient un bonus de +2 en attaque et aux DM lorsqu’il combat des animaux "
                             "et un bonus de +2 par Rang dans cette Voie pour pister ou retrouver des traces.",
      },
      "http://co-drs.org/capacites/chatiment-divin/": {
        "short_description": "Le Prêtre effectue une attaque de contact avec un bonus en attaque et "
                             "aux dégâts égal à son Mod. de SAG.",
      },
      "http://co-drs.org/capacites/chimiste/": {
        "short_description": "L’Arquebusier sait fabriquer sa propre poudre et d’autres substances explosives, "
                             "et obtient un bonus de +2 par Rang à tous les tests de chimie ou d’alchimie."
      },
      "http://co-drs.org/capacites/chute/": {
        "short_description": "Le Voleur peut tomber d’une hauteur de 3 m par rang sans se faire mal."
      },
      "http://co-drs.org/capacites/chute-ralentie/": {
        "short_description": "Le Magicien affecte une cible qui peut chuter de 6 mètres par rang "
                             "dans la Voie sans subir de dégâts. Au delà, sa chute est réduite d’autant.",
        "range": Range(value=6, unit="m")
      },
      "http://co-drs.org/capacites/clairvoyance/": {
        "short_description": "L’Ensorceleur peut voir et entendre "
                             "ce qui se passe dans un lieu qu’il connait, tant qu’il reste "
                             "concentrée. Les créatures présentes peuvent se sentir observées.",
        "special_property": ["Rester concentrer (L) / tour",
                             "Test SAG (observé): 12+[CHA]"]
      },
      "http://co-drs.org/capacites/colosse/": {
        "short_description": "Le demi-orque augmente ses valeurs de FOR et de CON de +2."
      },
      "http://co-drs.org/capacites/combat/": {
        "short_description": "Le loup du Rôdeur peut désormais se battre comme un véritable personnage."
      },
      "http://co-drs.org/capacites/combat-2/": {
        "short_description": "L’ours du Rôdeur peut désormais se battre comme un véritable personnage."
      },
      "http://co-drs.org/capacites/combat-a-deux-armes-ameliore/": {
        "short_description": "Lorsqu’il utilise une action d’attaque, le personnage effectue une attaque de "
                             "chaque main."
      },
      "http://co-drs.org/capacites/combat-a-deux-armes-parfait/": {
        "short_description": "Lorsqu’il utilise une action d’attaque, le personnage effectue une attaque de "
                             "chaque main."
      },
      "http://co-drs.org/capacites/combat-de-masse/": {
        "short_description": "L’Arquebusier obtient une action de mouvement ou une action d’attaque supplémentaire "
                             "à chaque tour si le combat implique au moins 10 créatures."
      },
      "http://co-drs.org/capacites/combat-en-phalange/": {
        "short_description": "Lorsque vous combattez la même créature qu’un allié, vous gagnez +1 en attaque et "
                             "en DEF par allié au contact avec vous et avec la créature."
      },
      "http://co-drs.org/capacites/combattant-aguerri/": {
        "short_description": "l’Arquebusier peut choisir n’importe quelle capacité de rang 2 d’une voie de "
                             "Guerrier de son choix et gagne 3 PV supplémentaires."
      },
      "http://co-drs.org/capacites/commandant/": {
        "short_description": "Le commandant offre un bonus de +3 en Initiative, en attaque, aux DM et en DEF à "
                             "toutes les créatures sous ses ordres à portée de vue."
      },
      "http://co-drs.org/capacites/comprehension-des-langues/": {
        "short_description": "Ce sort permet au Barde de lire, écrire et parler n’importe quelle langue ancienne "
                             "ou vivante pendant [1d6 + Mod. de CHA] minutes."
      },
      "http://co-drs.org/capacites/confusion/": {
        "short_description": "En réussissant un test d’Attaque magique, l’Ensorceleur désoriente sa cible pendant "
                             "[3 + Mod. de CHA] tours."
      },
      "http://co-drs.org/capacites/constitution-heroique/": {
        "short_description": "Le personnage augmente son score de CON de +2 et il peut désormais lancer deux d20 "
                             "à chaque fois qu’un test de CON lui est demandé et conserver le meilleur résultat.",
      },
      "http://co-drs.org/capacites/corps-enflamme/": {
        "short_description": "La créature est nimbée d’une aura de feu ou peut la faire surgir à volonté."
      },
      "http://co-drs.org/capacites/couleuvrine/": {
        "short_description": "L’Arquebusier obtient une couleuvrine, un petit canon portatif qui nécessite la "
                             "mise en place d’un trépied."
      },
      "http://co-drs.org/capacites/coup-de-bouclier/": {
        "short_description": "Le chevalier peut effectuer à chaque tour une attaque au bouclier avec un d12 au "
                             "lieu du d20 (action gratuite) qui inflige [1d4 + Mod. de FOR] DM.",
      },
      "http://co-drs.org/capacites/course-des-airs/": {
        "short_description": "Le Moine défie les lois de la pesanteur et peut se déplacer sur des surfaces qui "
                             "ne devraient pas supporter son poids."
      },
      "http://co-drs.org/capacites/course-du-vent/": {
        "short_description": "Le Moine se déplace à une vitesse surhumaine."
      },
      "http://co-drs.org/capacites/cri-de-guerre/": {
        "short_description": "Une fois par combat, le Barbare pousse un hurlement qui effraie ses adversaires."
      },
      "http://co-drs.org/capacites/critique-brutal/": {
        "short_description": "Les DM du demi-orque sont multipliés par 3 lorsqu’il obtient une réussite critique "
                             "sur une attaque au contact.",
      },
      "http://co-drs.org/capacites/croc-en-jambe/": {
        "short_description": "Lorsqu’il obtient un score de 17 à 20 sur son d20 en attaque au contact, le Voleur "
                             "fait chuter son adversaire en plus de lui infliger des DM normaux."
      },
      "http://co-drs.org/capacites/dans-le-mille/": {
        "short_description": "Pour une attaque à distance, le Rôdeur peut choisir d’utiliser 1d12 en attaque. "
                             "Si l’attaque est réussie, il ajoute 2d6 aux DM."
      },
      "http://co-drs.org/capacites/danse-irresistible/": {
        "short_description": "Le barde joue une gigue endiablée aux effets magiques. S’il réussit un test "
                             "d’attaque magique, la créature qu’il cible se met à danser."
      },
      "http://co-drs.org/capacites/debrouillard/": {
        "short_description": "Le Barde obtient un bonus de +5 à tous ses tests de survie en nature et aux tests "
                             "de profession et d’artisanat."
      },
      "http://co-drs.org/capacites/dechainement-d-acier/": {
        "short_description": "Le Barbare parcourt 10 mètres en ligne droite et porte une attaque à chaque "
                             "adversaire sur son passage."
      },
      "http://co-drs.org/capacites/dedoublement/": {
        "short_description":  "L’Ensorceleur cré un double translucide de la cible qui passe sous son "
                              "contrôle (attaque magique). Il "
                              "possède les mêmes Caractéristiques que l’original, "
                              "la moitié de ses PV et tous les DM qu’il inflige sont divisés par "
                              "deux. Une créature ne peut être dédoublée qu’une fois par "
                              "combat et le double disparaît si ses PV tombent à 0.",
        "range": Range(value=20, unit="m"),
        "duration": Duration(value="5+[CHA]", unit="tr"),
      },
      "http://co-drs.org/capacites/defaut-dans-la-cuirasse/": {
        "short_description": "L’Arquebusier passe un tour complet à analyser le point faible de son adversaire "
                             "et à viser."
      },
      "http://co-drs.org/capacites/defier-la-mort/": {
        "short_description": "Lorsque le Barbare subit des DM d’une attaque qui devrait l’amener à 0 PV, il peut "
                             "réaliser un test de CON difficulté 10. En cas de réussite, il conserve 1 PV."
      },
      "http://co-drs.org/capacites/deguisement/": {
        "short_description": "Ce sort permet au Barde de prendre l’apparence de n’importe quelle créature de "
                             "taille à peu près équivalente."
      },
      "http://co-drs.org/capacites/delivrance/": {
        "short_description": "En touchant sa cible, le Prêtre annule les pénalités infligées par les sorts, "
                             "les malédictions, la pétrification et les effets de capacités spéciales."
      },
      "http://co-drs.org/capacites/deluge-de-coups/": {
        "short_description": "A son tour, le Moine peut effectuer 2 attaques à mains nues sur des cibles de son "
                             "choix ou 2 attaques avec une arme."
      },
      "http://co-drs.org/capacites/demolition/": {
        "short_description": "L’Arquebusier peut préparer un explosif qui lui permet de démolir facilement des "
                             "structures."
      },
      "http://co-drs.org/capacites/dentelles-et-rapiere/": {
        "short_description": "Le Barde ne met pas d’armure, cela ne sied point en société. Sa seule armure est "
                             "la dentelle, sa seule défense, la rapière."
      },
      "http://co-drs.org/capacites/deplacement-magique/": {
        "short_description": "La créature possède une magie qui lui permet de se téléporter."
      },
      "http://co-drs.org/capacites/dernier-rempart/": {
        "short_description": "Le Guerrier effectue uniquement une attaque au contact durant ce tour et bénéficie "
                             "d’une attaque supplémentaire contre tout ennemi qui se déplace à son contact."
      },
      "http://co-drs.org/capacites/desarmer/": {
        "short_description": "Le Guerrier réalise une attaque au contact et sa victime doit faire un test "
                             "d’attaque opposé. S'il réussi, l’arme de son adversaire tombe au sol."
      },
      "http://co-drs.org/capacites/desintegration/": {
        "short_description": "Le Magicien projette un rayon mortel qui annule la cohésion de la matière, ne "
                             "laissant derrière lui qu’un amas de poussière que la cible soit une créature "
                             "ou un objet.",
        "range": Range(value=20, unit="m"),
        "attack": Attack(
          atype='magical',
          range=Range(value=30, unit="m"),
          damages=Damage(
            base=[],
            other=[Mod(die=6, count=5),
                   Mod(mtype="+", target="INT")],
          ),
          critical=RangeSet([20])
        ),
        "special_property": [
          "Petit objet: attaque -5",
          "Objet magique: insensible",
          "Impossible sur objet > 50 Kg"
          ]


      },
      "http://co-drs.org/capacites/destruction-des-morts-vivants/": {
        "short_description": "Le Prêtre peut faire un test de SAG difficulté 13. S’il réussit, tous les "
                             "morts-vivants en vue subissent 2d6 points de DM."
      },
      "http://co-drs.org/capacites/detecter-les-pieges/": {
        "short_description": "En réussissant un test d’INT difficulté 10, le Voleur peut détecter et contourner "
                             "les pièges.",
      },
      "http://co-drs.org/capacites/detection-de-l-invisible/": {
        "short_description": "L’Ensorceleur détecte les créatures invisibles ou cachées et détecte si un sort "
                             "de Clairvoyance affecte l’endroit.",
        "duration": Duration(value="5+[CHA]", unit="tr"),
        "range": Range(value=30, unit="m"),
        "special_property": ["Détecte créature invisible ou cachée",
                             "Detecte sort de clairvoyance",
                             "Vue normale si aveuglé"]
      },
      "http://co-drs.org/capacites/detection-de-la-magie/": {
        "short_description": "Le Magicien se concentre et détecte la présence "
                             "de toute inscription et de tout objet magique situé dans la pièce "
                             "où il se trouve. Ce sort permet aussi d’analyser les propriétés "
                             "d’un objet magique au prix de 2 heures d’étude et de 100 pa de "
                             "poudre d’argent.",
        "area": Area(value=15, unit="m"),
      },
      "http://co-drs.org/capacites/devorer/": {
        "short_description": "Lorsque la créature réussit une attaque (15-20), elle saisit sa proie entre ses "
                             "crocs ou ses griffes et lui inflige immédiatement une attaque supplémentaire."
      },
      "http://co-drs.org/capacites/dexterite-heroique/": {
        "short_description": "Le personnage augmente son score de DEX de +2 et il peut désormais lancer deux d20 "
                             "à chaque fois qu’un test de DEX lui est demandé, et conserver le meilleur résultat."
      },
      "http://co-drs.org/capacites/discretion/": {
        "short_description": "Quand il essaie de passer inaperçu, le Voleur bénéficie d’un bonus de +2 à son test "
                             "de DEX pour chaque rang acquis dans cette voie."
      },
      "http://co-drs.org/capacites/disparition/": {
        "short_description": "La créature devient invisible et peut se déplacer de 20 mètres."
      },
      "http://co-drs.org/capacites/doigts-agiles/": {
        "short_description": "Le Voleur reçoit un bonus de +2 pour tous ses tests de DEX liés à la précision : "
                             "crocheter une serrure, désamorcer un piège, pickpocket…",
      },
      "http://co-drs.org/capacites/domination/": {
        "short_description": "En réussissant un test d’Attaque magique, l’Ensorceleur prend contrôle de son esprit "
                             "pendant [1d4 + Mod. CHA] minutes."
      },
      "http://co-drs.org/capacites/don-occulte/": {
        "short_description": "Le joueur choisit une capacité de rang 1 ou 2 de n’importe quelle voie "
                             "d’Ensorceleur."
      },
      "http://co-drs.org/capacites/double-attaque/": {
        "short_description": "Le Guerrier peut tenter deux attaques au contact durant ce tour avec un malus de -2."
      },
      "http://co-drs.org/capacites/double-peine/": {
        "short_description": "Si les deux armes du personnage atteignent la cible lors d’un même tour, le "
                             "personnage ajoute +1d6 DM à l’une des deux attaques selon son choix."
      },
      "http://co-drs.org/capacites/dressage/": {
        "short_description": "Le Rôdeur a dressé l’ours, il peut lui faire faire des numéros comme marcher sur "
                             "les pattes avant ou porter un objet en équilibre sur son museau."
      },
      "http://co-drs.org/capacites/dur-a-cuire/": {
        "short_description": "Le Guerrier reçoit un bonus de +5 à tous ses tests de CON. De plus, lorsqu’il tombe "
                             "à 0 PV, il peut continuer à agir pendant un ultime tour avant de tomber inconscient."
      },
      "http://co-drs.org/capacites/ecuyer/": {
        "short_description": "Le Chevalier dispose d’un écuyer à son service. Il est absolument loyal à son maître "
                             "et lui sert de serviteur."
      },
      "http://co-drs.org/capacites/eduque/": {
        "short_description": "Le Chevalier sait lire et écrire, il gagne +1 par rang dans la voie à tous les "
                             "tests d’INT et de CHA.",
      },
      "http://co-drs.org/capacites/elixir-de-guerison/": {
        "short_description": "Le Forgesort peut préparer un élixir qui soigne [3d6 + Mod. d’INT] PV ou un "
                             "empoisonnement.",
        "special_property": ["Soigne: 3d6 + [INT] PV",
                             "Soigne un empoisonnement"]
      },
      "http://co-drs.org/capacites/elixirs-magique/": {
        "short_description": "Le Forgesort peut préparer une potion d’Invisibilité, de Vol, de Respiration "
                             "aquatique, de Flou ou de Hâte.",
      },
      "http://co-drs.org/capacites/embuscade/": {
        "short_description": "En quelques minutes, le Rôdeur peut cacher tous ses compagnons dans n’importe quel "
                             "environnement naturel."
      },
      "http://co-drs.org/capacites/embuscade-2/": {
        "short_description": "Au premier tour de combat, si l’environnement permet à la créature de se dissimuler, "
                             "la cible doit faire un test de SAG difficulté [15 + Mod. de DEX] ou être Surprise."
      },
      "http://co-drs.org/capacites/empathie-animale/": {
        "short_description": "Le Rôdeur peut parler aux animaux. Il peut également communiquer avec son compagnon "
                             "animal par télépathie et le guérir à distance en dépensant ses propres PV."
      },
      "http://co-drs.org/capacites/emporter-dans-les-airs/": {
        "short_description": "La créature peut emporter dans les airs une victime agrippée de taille inférieure à "
                             "la sienne au prix d’une action de mouvement."
      },
      "http://co-drs.org/capacites/encaisser-un-coup/": {
        "short_description": "Le chevalier se place de façon à dévier un coup sur son armure."
      },
      "http://co-drs.org/capacites/enchainement/": {
        "short_description": "Chaque fois que le Barbare réduit un adversaire à 0 PV avec une attaque de contact, "
                             "il bénéficie d’une action d’attaque gratuite sur un autre adversaire au contact."
      },
      "http://co-drs.org/capacites/endurant/": {
        "short_description": "Pour chaque Rang dans cette Voie, le Rôdeur obtient un bonus de +2 sur tous ses "
                             "tests de CON destinés à la survie en milieu naturel."
      },
      "http://co-drs.org/capacites/endurer/": {
        "short_description": "Le Forgesort est habitué aux travaux et à la chaleur de la forge."
      },
      "http://co-drs.org/capacites/enfant-de-la-foret/": {
        "short_description": "Le joueur choisit une capacité de rang 1 de n’importe quelle voie de Druide ou de "
                             "Rôdeur."
      },
      "http://co-drs.org/capacites/ennemi-jure/": {
        "short_description": "Après avoir tué une créature, le Rôdeur peut décider que tous ceux de sa race sont "
                             "devenus des ennemis jurés."
      },
      "http://co-drs.org/capacites/enrager/": {
        "short_description": "Lorsqu’elle reçoit un coup critique ou si ses PV passent sous la moitié, la "
                             "créature devient enragée."
      },
      "http://co-drs.org/capacites/ensevelissement/": {
        "short_description": "Une fois par combat, si le Nécromancien réussit un test d’attaque magique, le sol "
                             "s’ouvre sous les pieds d’une cible de taille moyenne et l’enterre vivante."
      },
      "http://co-drs.org/capacites/esquive/": {
        "short_description": "Le Voleur est très vif et bénéficie d’un bonus de +1 par rang dans cette voie à sa "
                             "DEF et à tous ses tests de DEX destinés à esquiver."
      },
      "http://co-drs.org/capacites/esquive-acrobatique/": {
        "short_description": "Une fois par tour, le Barde peut réaliser une esquive. En cas de réussite, le Barde "
                             "ne subit aucun DM."
      },
      "http://co-drs.org/capacites/esquive-de-la-magie/": {
        "short_description": "À chaque fois qu’un sort le prend pour cible, le Voleur peut effectuer un test de "
                             "DEX en opposition au test d’attaque magique du sort et échapper au sort."
      },
      "http://co-drs.org/capacites/esquive-du-singe/": {
        "short_description": "Pour chaque Rang dans cette Voie, le Moine gagne +1 en DEF et à tous ses tests de "
                             "DEX pour effectuer des acrobaties."
      },
      "http://co-drs.org/capacites/esquive-fatale/": {
        "short_description": "Une fois par combat, le duelliste peut esquiver une attaque qui devait le toucher "
                             "et s’arranger pour que celle-ci affecte un autre adversaire à son contact."
      },
      "http://co-drs.org/capacites/exemplaire/": {
        "short_description": "Une fois par tour, le Chevalier permet à un allié qui combat le même adversaire "
                             "que lui de relancer le d20 d’un test d’attaque, s’il s’agissait d’un d’échec."
      },
      "http://co-drs.org/capacites/expertise/": {
        "short_description": "Au choix, soit le personnage obtient un bonus de +5 sur les tests d’une "
                             "caractéristique, soit il obtient un bonus de +10 sur les tests d’une compétence."
      },
      "http://co-drs.org/capacites/explosion-finale/": {
        "short_description": "Lorsqu’elle trépasse, la créature explose violemment en infligeant [NC] d6 DM de "
                             "feu dans un rayon qui dépend de sa taille."
      },
      "http://co-drs.org/capacites/exsangue/": {
        "short_description": "Lorsque le nécromant tombe à 0 PV, il peut peut "
                             "continuer à agir mais avec un malus. Une attaque réussie lui "
                             "infligeant au moins 1 point de DM l’achèvera.",
        "skill": [Mod(label="Test", mtype="-", count=2)]
      },
      "http://co-drs.org/capacites/familier/": {
        "short_description": "Le personnage choisit un petit animal. Il peut utiliser les sens de son familier et "
                             "communiquer avec lui à distance illimitée."
      },
      "http://co-drs.org/capacites/fauchage/": {
        "short_description": "Sur 15 à 20 au test d’attaque, si l’attaque est réussie, la victime doit réussir au "
                             "choix un test de FOR ou de DEX ou être Renversée."
      },
      "http://co-drs.org/capacites/feindre-la-mort/": {
        "short_description": "Une fois par combat, le Voleur peut feindre la mort après avoir reçu une blessure. "
                             "Il peut ainsi passer pour mort aussi longtemps qu’il le souhaite."
      },
      "http://co-drs.org/capacites/feinte/": {
        "short_description": "Le Barde effectue une attaque fictive pour déséquilibrer son adversaire et réaliser "
                             "ensuite une attaque mortelle."
      },
      "http://co-drs.org/capacites/feu-gregeois/": {
        "short_description": "Le Forgesort lance la fiole et le contenu explose "
                             "en projetant du feu.",
        "attack": Attack(
          atype='magical',
          area=Area(value=3, unit="m"),
          range=Range(value=10, unit="m"),
          damages=Damage(
            base=[],
            other=[Mod(die=6, count=1, target="feu", 
            label="(par rang dans la voie)")],
          ),
          critical=RangeSet([20])
        ),
        "special_property": ["Test DEX > 10 + [INT]: DM / 2",
                             "Réussite automatique"]
      },
      "http://co-drs.org/capacites/feu-nourri/": {
        "short_description": "Lorsqu’il utilise le Tir de barrage, l’Arquebusier peut affecter jusqu’à [1 + Mod. "
                             "de DEX] cibles différentes dans le même tour."
      },
      "http://co-drs.org/capacites/fidele-monture/": {
        "short_description": "Le Chevalier possède un puissant destrier, c’est un cheval de guerre bien dressé "
                             "qui comprend les ordres simples."
      },
      "http://co-drs.org/capacites/fleche-de-mort/": {
        "short_description": "Le Rôdeur lance deux d20 pour son attaque et conserve le meilleur résultat. Les "
                             "dégâts de la flèche sont doublés."
      },
      "http://co-drs.org/capacites/fleche-enflammee/": {
        "short_description": "Le Magicien lance ce sort choisit une cible à distance. Si son attaque magique "
                             "réussit, la cible encaisse des dégâts et la flèche enflamme ses vêtements le "
                             "tour suivant.",
        "attack": Attack(
          atype='magical',
          range=Range(value=30, unit="m"),
          damages=Damage(
            base=[],
            other=[Mod(die=6, count=1),
                   Mod(mtype="+", target="INT")],
          ),
          critical=RangeSet([20])
        ),
        "special_property": ["DM feu: 1d6 / tr", "Fin sur un résultat de 1 ou 2"]
      },
      "http://co-drs.org/capacites/fleche-sanglante/": {
        "short_description": "L’elfe fait une attaque à distance qui provoque une hémorragie. En plus des DM "
                             "normaux, la flèche produit un effet de saignement."
      },
      "http://co-drs.org/capacites/flou/": {
        "short_description": "Pendant [1d4 + Mod. d’INT] tours, le corps du Magicien devient flou et tous les DM "
                             "des attaques de contact ou à distance qu’il encaisse sont divisés par 2.",
        "duration": Duration(value="1d4+[INT]", unit="tr"),
        "special_property": ["DM attaque contact / 2",
                             "DM attaque distance / 2"]

      },
      "http://co-drs.org/capacites/force-d-ame/": {
        "short_description": "L’elfe est immunisé à la peur et au sommeil magique."
      },
      "http://co-drs.org/capacites/force-de-la-nature/": {
        "short_description": "Le demi-orque gagne un bonus de +5 à tous les tests de FOR et ajoute son "
                             "[Mod. de FOR] à son score total de PV."
      },
      "http://co-drs.org/capacites/force-heroique/": {
        "short_description": "Le personnage augmente sa valeur de FOR de +2 et il peut désormais lancer deux d20 "
                             "à chaque fois qu’un test de FOR lui est demandé et garder le meilleur résultat."
      },
      "http://co-drs.org/capacites/foret-vivante/": {
        "short_description": "La forêt s’éveille dans un rayon d’1 km par rang et devient une alliée du Druide "
                             "pendant les 12 prochaines heures."
      },
      "http://co-drs.org/capacites/forgeron/": {
        "short_description": "Le Forgesort obtient un bonus de +2 par Rang dans la Voie aux tests d’orfèvrerie "
                             "ou de forge."
      },
      "http://co-drs.org/capacites/formation-d-elite/": {
        "short_description": "Le chevalier possède les moyens et la culture nécessaire pour obtenir une formation "
                             "dans n’importe quel domaine qui lui sied."
      },
      "http://co-drs.org/capacites/forme-animale/": {
        "short_description": "Le Druide peut prendre la forme d’un "
                             "animal de sa taille (ou plus petit). Elle conserve "
                             "ses PV et acquiert les Carac. et les capacités naturelles de la "
                             "forme choisie.",
        "special_property": ["Reprendre forme humaine (L)"]
      },
      "http://co-drs.org/capacites/forme-d-arbre/": {
        "short_description": "Une fois par combat, le Druide peut se "
                             "transformer en arbre de petite taille. Il conserve ses "
                             "propres PV. Il peut utiliser les sorts des voies du "
                             "protecteur et des végétaux.",
        "duration": Duration(value="5+[SAG]", unit="tr"),
        "special_property": ["Ne peut pas parler"]
              
      },
      "http://co-drs.org/capacites/forme-etheree/": {
        "short_description": "L'ensorceleur et tout son équipement deviennent "
                             "translucides et intangibles. Ils peuvent passer à travers murs et "
                             "obstacles.",
        "duration": Duration(value="5+[CHA]", unit="tr"),
        "special_property": ["Aucun DM physique subit"]
      },
      "http://co-drs.org/capacites/forme-gazeuse/": {
        "short_description": "Le Magicien prend la consistance d’un gaz. Il se déplace au ras du sol à une "
                             "vitesse de 10 m par tour. Il ne peut utiliser aucune capacité.",
        "special_property": ["Chute ralentie : 10m / tour",
                             "Aucun DM, sauf DM de sort de zone",
                             "Déplacement : 10m / tour"],
        "duration": Duration(value="1d4+[INT]", unit="tr")
      },
      "http://co-drs.org/capacites/fortifiant/": {
        "short_description": "Un breuvage étrange qui guérit et permet de gagner un bonus de +3 "
                             "aux [rang +1] prochains tests de réussite effectués.",
        "duration": Duration(value=12, unit="h"),
        "special_property": ["Test: +3 (rang + 1 prochains tests)",
                             "Soigne: 1d4 + rang PV"]
      },
      "http://co-drs.org/capacites/foudre/": {
        "short_description": "L’Ensorceleur produit un éclair sur une ligne de 10 mètres."
      },
      "http://co-drs.org/capacites/foudres-divines/": {
        "short_description": "La foudre frappe toutes les créatures désignées autour du "
                             "prêtre qui compare son test d'attaque à la DEF de chaque cible.",
        "area": Area(value="10", unit="m"),
        "attack": Attack(
          atype='magical',
          damages=Damage(
            base=[],
            other=[Mod(die=6, count=1),Mod(mtype="+", target="SAG")],
          ),
          critical=RangeSet([20])
        ),
      },
      "http://co-drs.org/capacites/frappe-chirurgicale/": {
        "short_description": "Par sa science de l’escrime, le Voleur augmente de manière permanente ses chances "
                             "de faire des coups critiques."
      },
      "http://co-drs.org/capacites/frappe-des-arcanes/": {
        "short_description": "Le Forgesort frappe le sol de son bâton et provoque une onde dévastatrice dans un "
                             "rayon de 10 m autour de lui."
      },
      "http://co-drs.org/capacites/frappe-lourde/": {
        "short_description": "Le chevalier effectue une attaque au contact avec 1d12 au lieu du d20. Si l’attaque "
                             "est réussie, il ajoute +2d6 aux DM."
      },
      "http://co-drs.org/capacites/fureur-du-dragon/": {
        "short_description": "Une fois par combat, le Moine peut effectuer une attaque tournoyante qui inflige "
                             "automatiquement des dégâts à tous les adversaires au contact et peut les renverser."
      },
      "http://co-drs.org/capacites/furie-du-berserk/": {
        "short_description": "Au lieu de la Rage du berserk, le Barbare peut entrer s’il le souhaite en Furie du "
                             "berserk, qui lui donne +3 en attaque et +2d6 aux DM pour une pénalité en DEF de -6."
      },
      "http://co-drs.org/capacites/gland-de-pouvoir/": {
        "short_description": "Une fois par combat, le Druide peut lancer un gland sur une cible. En cas d’attaque "
                             "magique réussie, la victime se transforme en statue de bois."
      },
      "http://co-drs.org/capacites/gober/": {
        "short_description": "Lorsqu’elle utilise sa capacité Dévorer, la créature peut avaler toute entière une "
                             "cible d’au moins 1 taille en dessous de la sienne."
      },
      "http://co-drs.org/capacites/golem/": {
        "short_description": "Le golem est une créature humanoïde fabriquée par le Forgesort pour lui servir de "
                             "serviteur et de garde du corps."
      },
      "http://co-drs.org/capacites/golem-superieur/": {
        "full_description": "Le Forgesort peut améliorer son golem en choisissant une option parmi : Armure : +5 "
                            "en DEF, Félin : +3 Mod. de DEX, Baliste : portée 20 m, 2d6 DM, Taille : +10 PV et +1 "
                            "Mod. de FOR, Vol : des « sauts » de 40 m en action limitée, Cerveau amélioré : +2 "
                            "Mod. d’INT, SAG, CHA, doué de parole, Puissant : +2 Mod. de FOR, Arme à deux mains : "
                            "+1d8 aux DM au contact, Le joueur peut choisir une option de plus lorsque son "
                            "personnage atteint les niveaux 9, 13 et 17. Les options peuvent êtres choisies "
                            "plusieurs fois et cumulées.",
        "short_description": "Le Forgesort peut améliorer son golem"
      },
      "http://co-drs.org/capacites/grace-elfique/": {
        "short_description": "L’elfe gagne un bonus de +5 en Initiative et à tous les tests de DEX."
      },
      "http://co-drs.org/capacites/grace-elfique-2/": {
        "short_description": "L’elfe gagne +5 à tous les tests de CHA et de déplacement silencieux."
      },
      "http://co-drs.org/capacites/grace-feline/": {
        "short_description": "Le Barde ajoute son Mod. de CHA en DEF et en Initiative (en plus du Mod. habituel "
                             "de DEX)."
      },
      "http://co-drs.org/capacites/grace-feline-2/": {
        "short_description": "Le Voleur possède une démarche et une façon de se déplacer à la fois élégante, "
                             "féline et souple."
      },
      "http://co-drs.org/capacites/grand-felin/": {
        "short_description": "La panthère devient un animal fabuleux, ou est remplacée par un félin plus grand "
                             "(tigre, lion)."
      },
      "http://co-drs.org/capacites/grand-pas/": {
        "short_description": "Le Rôdeur augmente tous ses déplacements de 10 m. Il n’est pas gêné par les "
                             "terrains accidentés et obtient +5 aux tests de natation et d’escalade."
      },
      "http://co-drs.org/capacites/griffes-du-tigre/": {
        "short_description": "Les DM des attaques à mains nues du Moine sont désormais des jets sans limite."
      },
      "http://co-drs.org/capacites/grosse-tete/": {
        "short_description": "Le Forgesort remplace la force brutale par un peu de réflexion."
      },
      "http://co-drs.org/capacites/guerir/": {
        "short_description": "Ce pouvoir annule tous les effets préjudiciables, pénalités, poisons, maladies "
                             "auquel était soumise la cible."
      },
      "http://co-drs.org/capacites/guerison/": {
        "short_description": "Une fois par jour, le Prêtre peut toucher une cible. Elle récupère alors tous ses "
                             "PV et est guérie des poisons, maladies et affaiblissements de Caractéristiques."
      },
      "http://co-drs.org/capacites/haches-et-marteaux/": {
        "short_description": "Le nain gagne un bonus de +1 en attaque et aux DM lorsqu’il utilise une hache ou un "
                             "marteau de guerre."
      },
      "http://co-drs.org/capacites/hate/": {
        "short_description": "Le Magicien voit son métabolisme s’accélérer. A partir du tour suivant, il obtient "
                             "une action supplémentaire par tour.",
        "special_property": ["+1 déplacement ou attaque / tour", "Seulement une action limité / tour"],
        "duration": Duration(value="1d6+[INT]", unit="tr"),
      },
      "http://co-drs.org/capacites/hausser-le-ton/": {
        "short_description": "Lorsqu’il passe sous la moitié de ses PV, le champion gagne un bonus de +5 à ses "
                             "tests d’attaque et +1d6 aux DM et réduit tous les DM subits de 5 points par attaque."
      },
      "http://co-drs.org/capacites/hemorragie/": {
        "short_description": "Si le Nécromancien réussit un test d’attaque magique, la victime saigne à la moindre "
                             "blessure."
      },
      "http://co-drs.org/capacites/hyperconscience/": {
        "short_description": "L’Ensorceleur augmente ses valeurs de SAG et d’INT de +2."
      },
      "http://co-drs.org/capacites/ignorer-la-douleur/": {
        "short_description": "Une fois par combat, le Chevalier peut noter à part les DM subis par une attaque. "
                             "Il n’en subira les effets que lorsque le combat sera terminé."
      },
      "http://co-drs.org/capacites/image-decalee/": {
        "short_description": "Pendant [5 + Mod. de CHA] tours, lorsqu’une attaque le touche, l’Ensorceleur lance "
                             "1d6 : sur 5-6, il ne subit pas les DM."
      },
      "http://co-drs.org/capacites/imitation/": {
        "short_description": "L’ensorceleur peut prendre l’apparence d’une créature de taille proche de la "
                             "sienne (+/- 50cm) qu’il voit au moment de l’incantation.",
        "duration": Duration(value="5+[CHA]", unit="tr"),
        "special_property": ["Fin si touché ou attaqué"]
      },
      "http://co-drs.org/capacites/immortel/": {
        "short_description": "L’elfe n’a besoin que de la moitié du repos, de la nourriture ou de la boisson d’un "
                             "humain normal pour être en pleine forme. Il est immunisé aux poisons et maladies."
      },
      "http://co-drs.org/capacites/immortel-2/": {
        "short_description": "Lorsqu’elle tombe à 0 PV, la créature n’est pas définitivement détruite, elle est "
                             "juste chassée et pourra se reconstituer en 24 heures."
      },
      "http://co-drs.org/capacites/imparable/": {
        "short_description": "Réaliser une attaque en lançant deux d20 et garder le meilleur résultat. Si le "
                             "champion obtient 15-20 au d20 d’un test d’attaque,"
      },
      "http://co-drs.org/capacites/impressionnant/": {
        "short_description": "L’ours permet au Rôdeur de gagner un bonus de +5 à tous ses tests d’intimidation "
                             "lorsque l’animal est à ses cotés."
      },
      "http://co-drs.org/capacites/increvable/": {
        "short_description": "Si vous croyez en avoir fini avec lui… Une fois par combat, lorsqu’il tombe à 0 PV, "
                             "le Rôdeur peut récupérer [3d6 + Mod. de CON] PV au tour suivant."
      },
      "http://co-drs.org/capacites/increvable-2/": {
        "short_description": "Une fois par tour, si le personnage tombe à 0 PV, ce dernier peut effectuer un test "
                             "d’attaque. En cas de réussite, le personnage esquive ou résiste à cette attaque."
      },
      "http://co-drs.org/capacites/injonction/": {
        "short_description": "L’Ensorceleur donne un ordre simple que la victime doit pouvoir comprendre. Il doit "
                             "réussir un test d’attaque magique opposé avec la cible à une portée de 20 mètres."
      },
      "http://co-drs.org/capacites/injonction-mortelle/": {
        "short_description": "Une cible doit réussir un test de CON de difficulté 15 ou tomber à 0 PV. En cas de "
                             "succès, la cible subit tout de même [2d6 + NC] DM."
      },
      "http://co-drs.org/capacites/insignifiant/": {
        "short_description": "Le gnome sait comment échapper aux attaques des grandes créatures comme les géants."
      },
      "http://co-drs.org/capacites/instinct-de-survie/": {
        "short_description": "La créature est passée maître dans l’art de se faufiler et de se mettre à couvert."
      },
      "http://co-drs.org/capacites/intelligence-du-combat/": {
        "short_description": "Le Barde ajoute son Mod. d’INT en Initiative et en DEF en plus de son Mod. de DEX."
      },
      "http://co-drs.org/capacites/intelligence-heroique/": {
        "short_description": "Le personnage augmente sa valeur d’INT de +2 et il peut désormais lancer deux d20 à "
                             "chaque fois qu’un test d’INT lui est demandé et conserver le meilleur résultat."
      },
      "http://co-drs.org/capacites/intercepter/": {
        "short_description": "Une fois par tour, le Chevalier peut encaisser un coup à la place d’un allié à ses "
                             "cotés."
      },
      "http://co-drs.org/capacites/interchangeables/": {
        "short_description": "Tant que la créature et ses alliées sont plus nombreuses que la cible, elles se "
                             "relaient pour esquiver ses attaques et elles obtiennent un bonus de +5 en DEF."
      },
      "http://co-drs.org/capacites/intervention-divine/": {
        "short_description": "Le Prêtre fait appel à son dieu pour changer le cours des événements. Une fois par "
                             "combat, il peut décider qu’un test du MJ ou des joueurs est une réussite ou un échec."
      },
      "http://co-drs.org/capacites/invisibilite/": {
        "short_description": "Le Magicien se rend invisible et personne ne peut plus détecter sa présence ou lui "
                             "porter d’attaque.",
        "duration": Duration(value="1d6+[INT]", unit="min"),
        "special_property": ["Visible si action limité ou attaque"]
      },
      "http://co-drs.org/capacites/invocation-d-un-demon/": {
        "short_description": "Une fois par combat, en sacrifiant 1d6 PV, le Nécromancien invoque un démon à son "
                             "service pour [5 + Mod. d’INT] tours."
      },
      "http://co-drs.org/capacites/invulnerable/": {
        "short_description": "Le Moine ne reçoit que la moitié des DM de toutes les sources «élémentaires» : feu, "
                             "froid, foudre, acide… Il ne subit aucun DM des poisons ou des maladies."
      },
      "http://co-drs.org/capacites/joli-coup/": {
        "short_description": "L’Arquebusier ignore les pénalités normalement appliquées lorsque la cible est à "
                             "couvert (généralement -2 à -5)."
      },
      "http://co-drs.org/capacites/laissez-le-moi/": {
        "short_description": "Le chevalier met un point d’honneur à combattre le leader ennemi. le Chevalier lui "
                             "inflige +1d6 DM par attaque."
      },
      "http://co-drs.org/capacites/lanceur-de-couteau/": {
        "short_description": "Une fois par tour, le Barde peut lancer un couteau gratuitement sur une cible à "
                             "distance (maximum 10 m)."
      },
      "http://co-drs.org/capacites/langage-des-animaux/": {
        "short_description": "Le Druide peut communiquer avec les animaux qui, en général, se comportent avec lui "
                             "de manière amicale. L'échange est primitif et limité à l’intelligence de "
                             "l’animal",
        "skill": [Mod(label="Test", target="Influencer un animal", mtype="+", count=2)]
      },
      "http://co-drs.org/capacites/le-guetteur/": {
        "short_description": "Le Druide reçoit un oiseau de proie comme compagnon animal. Il possède un lien "
                             "télépathique avec lui et peut percevoir par ses sens."
      },
      "http://co-drs.org/capacites/les-sept-vies-du-chat/": {
        "short_description": "Cette capacité ne peut être utilisée que sept fois, et pas plus d’une fois par "
                             "niveau. le Druide peut choisir d’ignorer ce qui a provoqué la mort."
      },
      "http://co-drs.org/capacites/levitation/": {
        "short_description": "En se concentrant, le Moine peut « léviter » à une vitesse de 10 m par tour.",
        "special_property": ["Déplacement: 10 m / tour"]
      },
      "http://co-drs.org/capacites/liberte-d-action/": {
        "short_description": "Le barde est immunisé à la peur et à tous les sorts ou effets magiques qui "
                             "asservissent l’esprit ou le corps."
      },
      "http://co-drs.org/capacites/lien-de-sang/": {
        "short_description": "En réussissant un test d’attaque magique, le Nécromancien tisse un lien avec sa "
                             "victime qui reçoit la moitié des DM reçus par le Nécromancien."
      },
      "http://co-drs.org/capacites/lilliputien/": {
        "short_description": "Le personnage rapetisse jusqu’à devenir plus petit que son familier. La "
                             "transformation dans un sens ou dans l’autre demande 1 tour complet."
      },
      "http://co-drs.org/capacites/loup-parmi-les-loups/": {
        "short_description": "Le personnage gagne +1 aux DM lorsqu’il combat un adversaire humanoïde. Ce bonus "
                             "passe à +2 au rang 4 de la voie."
      },
      "http://co-drs.org/capacites/lumiere/": {
        "short_description": "Le Magicien désigne un objet, lequel produit dès lors de la lumière dans un rayon "
                             "de 20 mètres qui n’émet pas de chaleur."
      },
      "http://co-drs.org/capacites/l-hallali/": {
        "short_description": "Les créatures profitent d’une erreur de leur victime pour lui porter des attaques "
                             "fatales."
      },
      "http://co-drs.org/capacites/magnetisme/": {
        "short_description": "Le Forgesort contrôle le magnétisme autour de lui et gagne un bonus de +5 en DEF et "
                             "divise par 2 les DM de toutes les armes ou projectiles métalliques."
      },
      "http://co-drs.org/capacites/mains-denergie/": {
        "short_description": "Le Moine peut rendre ses mains intangibles. Toutes les attaques à mains nues du "
                             "Moine sont considérées comme magiques."
      },
      "http://co-drs.org/capacites/maitre-de-la-survie/": {
        "short_description": "Le Druide obtient un bonus de +2 par rang dans la voie à tous les tests basés sur "
                             "la survie en milieu naturel."
      },
      "http://co-drs.org/capacites/maitrise-du-ki/": {
        "short_description": "Le Moine utilise son intuition et son empathie avec le monde pour augmenter son "
                             "efficacité en combat. Il ajoute son Mod. de SAG à son Initiative et sa DEF."
      },
      "http://co-drs.org/capacites/malediction/": {
        "short_description": "En cas de succès sur une attaque magique, la victime réalise tous ses tests avec "
                             "deux d20 et garde le résultat le plus faible."
      },
      "http://co-drs.org/capacites/marche-des-plans/": {
        "short_description": "Une fois par jour, le Prêtre peut passer dans une dimension entre les plans "
                             "d’existence où le temps et l’espace sont déformés."
      },
      "http://co-drs.org/capacites/marche-sylvestre/": {
        "short_description": "Le Druide ne subit aucune pénalité de déplacement en terrain difficile et obtient "
                             "un bonus lors d’un combat dans ces conditions.",
        "special_property":["DEF: +2 (terrain difficile)",
                            "Attaque: +2 (terrain difficile)"],
        "duration": Duration(value=24, unit="h")
      },
      "http://co-drs.org/capacites/marteau-spirituel/": {
        "short_description": "Le prêtre lance un un projectile d’énergie prenant la forme de l’arme du Prêtre qui "
                             "va percuter la cible, lui infligeant [1d8 + Mod. de SAG] de DM."
      },
      "http://co-drs.org/capacites/masque-du-predateur/": {
        "short_description": "Lorsqu’il est sous l’effet de ce sort, le Druide prend les traits d’un fauve ou "
                             "d’un loup.",
        "special_property": ["Initiative : +[SAG]",
                             "Vision nocturne (elfe)"],
        "duration": Duration(value="5+[SAG]", unit="tr")
      },
      "http://co-drs.org/capacites/masque-mortuaire/": {
        "short_description": "Le Nécromancien prend l’apparence de la mort. Il est immunisé aux attaques qui "
                             "n’affectent que les vivants et à la plupart des pouvoirs des mort-vivants (de "
                             "plus, ceux-ci le prennent pour l’un des leurs).",
        "defense": [Mod(label="RD", target="rd", count=2)],
        "special_property": ["DM de froid divisé par 2"]
      },
      "http://co-drs.org/capacites/massacrer-la-pietaille/": {
        "short_description": "Le Chevalier ajoute +1d6 aux DM contre la piétaille."
      },
      "http://co-drs.org/capacites/mecanismes/": {
        "short_description": "L’Arquebusier obtient un bonus de +1 par Rang dans cette voie à tous les tests "
                             "visant à réparer ou à comprendre des mécanismes."
      },
      "http://co-drs.org/capacites/meme-pas-mal/": {
        "short_description": "Lorsqu’il subit un coup critique, cela a pour effet de décupler la rage du barbare."
      },
      "http://co-drs.org/capacites/merveille-technologique/": {
        "short_description": "Le gnome sait utiliser les arbalètes quel que soit son profil. Il ajoute son Mod. "
                             "de DEX aux DM qu’il inflige avec ces armes.",
      },
      "http://co-drs.org/capacites/messie/": {
        "short_description": "Une fois par aventure, le Prêtre entre directement en contact avec la puissance "
                             "divine et réalise un miracle."
      },
      "http://co-drs.org/capacites/metal-brulant/": {
        "short_description": "Le Forgesort doit réussir une attaque magique pour faire chauffer un objet "
                             "métallique que sa cible transporte."
      },
      "http://co-drs.org/capacites/metal-hurlant/": {
        "short_description": "Avec une attaque magique réussi, le Forgesort déforme une pièce d’équipement "
                             "métallique portée par sa cible."
      },
      "http://co-drs.org/capacites/mirage/": {
        "short_description": "L’Ensorceleur crée une illusion visuelle et sonore immobile d’une durée de "
                             "[5 + Mod. de CHA] minutes (ou tours si l’illusion est animée).",
        "duration": Duration(value="5+[CHA]", unit="min"),
        "range": Range(value=500, unit="m"),
        "special_property": ["Durée: 5+[CHA] si illusion animée", "Fin si interraction"]
      },
      "http://co-drs.org/capacites/moment-de-perfection/": {
        "short_description": "Une fois par combat, le Moine peut choisir de réussir toutes ses attaques et "
                             "d’esquiver toutes celles qui le prennent pour cible pendant un tour."
      },
      "http://co-drs.org/capacites/monture-fantastique/": {
        "short_description": "Le chevalier obtient une monture volante. Lorsqu’il est en selle, le chevalier peut "
                             "faire attaquer sa monture une fois par tour."
      },
      "http://co-drs.org/capacites/monture-magique/": {
        "short_description": "Le chevalier obtient une monture magique, qui peut apparaître et disparaître depuis "
                             "un autre plan à volonté."
      },
      "http://co-drs.org/capacites/morsure-du-serpent/": {
        "short_description": "Le Moine obtient des DM critiques de 19 à 20 au d20 à mains nues ou avec une arme de "
                             "contact, et sur des résultats de 18 à 20 avec une rapière ou une Vivelame."
      },
      "http://co-drs.org/capacites/mot-de-mort/": {
        "short_description": "Le Nécromancien effectue une attaque magique contre le score max de PV de sa cible "
                             "et la victime doit réussir un test de CON [10 + Mod. d’INT] ou tomber à 0 PV.",
      },
      "http://co-drs.org/capacites/mot-de-pouvoir/": {
        "short_description": "Une fois par combat, le Prêtre peut prononcer un mot avec la voix de son dieu qui "
                             "paralyse ses ennemis de terreur et galvanise tous ses alliés en vue."
      },
      "http://co-drs.org/capacites/mur-de-force/": {
        "short_description": "L’Ensorceleur crée un mur de force indestructible, ou bien une hémisphère centrée "
                             "sur lui-même."
      },
      "http://co-drs.org/capacites/murmures-dans-le-vent/": {
        "short_description": "L’Ensorceleur  chuchote un message d’une dizaine de mots "
                             "qui voyage jusqu’à son destinataire. Elle doit connaître la cible ou la voir et "
                             "peut entendre sa réponse immédiatement.",
        'special_property': ["Portée: 100m / rang dans la voie"]
      },
      "http://co-drs.org/capacites/musique-fascinante/": {
        "short_description": "Le Barde joue de la musique pour fasciner et «contrôler» toutes les créatures de "
                             "son choix dont les PV sont inférieurs ou égaux à [5 + Mod. de CHA] du Barde."
      },
      "http://co-drs.org/capacites/nature-nourriciere/": {
        "short_description": "Si le Rôdeur passe du temps en forêt, il peut trouver de quoi nourrir des personnes "
                             "ou trouver des plantes médicinales qui doivent être utilisées immédiatement."
      },
      "http://co-drs.org/capacites/nuee-d-insectes/": {
        "short_description": "En réussissant une attaque magique, le Druide libère sur sa cible une nuée "
                             "d’insectes volants qui piquent, aveuglent et la suivent."
      },
      "http://co-drs.org/capacites/odorat/": {
        "short_description": "Le loup du Rôdeur détecte les odeurs des animaux et des créatures là où ils sont "
                             "passés et obtient un bonus de +5 aux tests de SAG pour pister et suivre des traces."
      },
      "http://co-drs.org/capacites/ombre-mortelle/": {
        "short_description": "L’ombre de la cible du Nécromancien attaque son propriétaire. L’ombre poursuit sa "
                             "cible partout où elle se réfugie. L'ombre possède la même attaque que la cible mais "
                             "inflige seulement la moitié des DM.",
        "duration": Duration(value="3+[INT]", unit="tr"),
        "range":Range(value=20, unit="m"),
        "special_property": ["Ombre: une attaque / tour"]

      },
      "http://co-drs.org/capacites/ombre-mouvante/": {
        "short_description": "En réussissant un test de DEX difficulté 10, le Voleur peut disparaître dans les "
                             "ombres à son tour et ne réapparaître qu’au tour suivant durant sa phase d’Initiative."
      },
      "http://co-drs.org/capacites/ordre-de-bataille/": {
        "short_description": "Le chevalier donne des ordres tactiques pertinents au cœur de la bataille. Une fois "
                             "par tour, il octroie une action supplémentaire gratuite à un allié en vue."
      },
      "http://co-drs.org/capacites/ouverture-mortelle/": {
        "short_description": "Une fois par combat, le Voleur obtient une réussite critique automatique contre la "
                             "cible de son choix."
      },
      "http://co-drs.org/capacites/pacifisme/": {
        "short_description": "Tant que le Moine n’a réalisé aucune action offensive dans un combat, il bénéficie "
                             "d’un bonus en DEF de +5."
      },
      "http://co-drs.org/capacites/pacte-sanglant/": {
        "short_description": "Par une action gratuite, le Nécromancien sacrifie 1d4 PV et gagne immédiatement +3 "
                             "sur un jet de d20 de son choix ou en DEF contre une attaque."
      },
      "http://co-drs.org/capacites/panthere/": {
        "short_description": "Le Druide apprivoise une panthère qui lui obéit au doigt et à l’œil."
      },
      "http://co-drs.org/capacites/parade-croisee/": {
        "short_description": "Durant un tour complet, le personnage obtient un bonus en DEF égal au rang atteint "
                             "dans la voie. Il ne réalise qu’une attaque à ce tour."
      },
      "http://co-drs.org/capacites/parade-de-projectiles/": {
        "short_description": "Le Moine peut dévier un projectile une fois par tour de combat."
      },
      "http://co-drs.org/capacites/parole-divine/": {
        "short_description": "Pour chaque rang dans cette Voie, le Prêtre obtient un bonus de +2 aux tests de "
                             "CHA visant à convaincre ou convertir son auditoire."
      },
      "http://co-drs.org/capacites/pas-de-loup/": {
        "short_description": "Quand il essaie de passer inaperçu en forêt, le Rôdeur bénéficie d’un bonus de +2 "
                             "par Rang à son test de DEX."
      },
      "http://co-drs.org/capacites/pas-du-vent/": {
        "short_description": "Le Moine peut se déplacer avant et après avoir attaqué. De plus, il gagne +1 par "
                             "rang dans la Voie en Initiative."
      },
      "http://co-drs.org/capacites/passe-muraille/": {
        "short_description": "Le Moine peut rendre son corps intangible temps de passer au travers d’un mur d’une "
                             "épaisseur maximum de [Mod. de SAG] mètres."
      },
      "http://co-drs.org/capacites/pattes-d-araignee/": {
        "short_description": "Le Nécromancien peut se déplacer de 10 m par action de mouvement sur les murs et "
                             "les plafonds. S’il reste immobile, il peut lancer des sorts.",
        "full_description": "Le Nécromancien peut se déplacer de 10 m par action de mouvement sur les murs et "
                            "les plafonds pendant [5 + Mod. d’INT] tours. S’il reste immobile, il peut lancer "
                            "des sorts.",
        "duration": Duration(value="5+[INT]", unit="tr"),
      },
      "http://co-drs.org/capacites/peau-de-fer/": {
        "short_description": "Le Moine gagne un bonus de +2 en DEF."
      },
      "http://co-drs.org/capacites/peau-de-pierre/": {
        "short_description": "Le Barbare est particulièrement endurci, il reçoit un bonus de DEF égal à son Mod. "
                             "de CON."
      },
      "http://co-drs.org/capacites/peau-de-pierre-2/": {
        "short_description": "Le Magicien obtient une réduction des DM égale à [5 + Mod. d’INT] pendant [5+ Mod. "
                             "d’INT] tours ou jusqu’à ce que le sort ait absorbé 40 points de dégâts."
      },
      "http://co-drs.org/capacites/peau-d-acier/": {
        "short_description": "Le Barbare ne sent plus la douleur et ignore les égratignures, il réduit tous les "
                             "DM subits de 3 points."
      },
      "http://co-drs.org/capacites/peau-d-ecorce/": {
        "short_description": "La peau du Druide prend la consistance de l’écorce. Il gagne alors un bonus en "
                             "défense.",
        "special_property": ["DEF: +1 / rang dans la voie"],
        "duration": Duration(value="5+[SAG]", unit="tr")
      },
      "http://co-drs.org/capacites/perception/": {
        "short_description": "Le halfelin obtient un bonus de +5 à tous les tests de perception et de discrétion. "
                             "Il sait utiliser la fronde et peut ajouter son Mod. de DEX aux DM fait par cet arme."
      },
      "http://co-drs.org/capacites/perception-heroique/": {
        "short_description": "Le Rôdeur augmente sa valeur de SAG de +2 et il peut désormais lancer deux d20 à "
                             "chaque fois qu’un test de SAG lui est demandé et conserver le meilleur résultat."
      },
      "http://co-drs.org/capacites/percuter/": {
        "short_description": "Sur une charge réussie, si la victime est d’une taille inférieure à la créature, "
                             "elle est projetée.",
      },
      "http://co-drs.org/capacites/petit-pote/": {
        "short_description": "Le gnome est un compagnon sympathique et difficile à prendre pour quelqu’un de "
                             "dangereux ou de malintentionné. Il gagne un bonus de +5 à tous les tests de CHA."
      },
      "http://co-drs.org/capacites/petit-veinard/": {
        "short_description": "Le halfelin peut relancer un dé de son choix une fois par combat."
      },
      "http://co-drs.org/capacites/peur/": {
        "short_description": "Le Nécromancien effectue un test d’attaque magique contre une cible. Celle-ci doit "
                             "réussir un test de FOR ou de SAG difficulté [10 + Mod. d’INT] ou fuir."
      },
      "http://co-drs.org/capacites/piege-explosif/": {
        "short_description": "il faut un tour complet à l’Arquebusier pour installer un piège qui explose dans un "
                             "rayon de 3 mètres en infligeant 5d6 DM."
      },
      "http://co-drs.org/capacites/piqures-d-insecte/": {
        "short_description": "Lorsqu’il porte une armure lourde, le Chevalier réduit les DM subis par les attaques "
                             "à distances d’un montant égal au rang atteint dans cette voie."
      },
      "http://co-drs.org/capacites/plus-vite-que-son-ombre/": {
        "short_description": "Si son arme à poudre est prête (chargée et tenue en main), l’Arquebusier peut tirer "
                             "avec un bonus de +10 à son Initiative."
      },
      "http://co-drs.org/capacites/poings-de-fer/": {
        "short_description": "Lorsqu’il combat à mains nues, le Moine peut utiliser son score d’attaque à "
                             "distance au lieu de celui d’attaque au contact."
      },
      "http://co-drs.org/capacites/polyvalence/": {
        "short_description": "Le personnage augmente de 2 points la valeur de sa Caractéristique la plus faible, "
                             "ainsi que la valeur d’une autre Caractéristique au choix."
      },
      "http://co-drs.org/capacites/porte-vegetale/": {
        "short_description": "Une fois par jour, le Druide peut pénétrer dans le tronc d’un gros arbre et sortir "
                             "de celui d’un autre arbre appartenant à la même forêt."
      },
      "http://co-drs.org/capacites/porteur-de-poisse/": {
        "short_description": "Toutes les attaques et tous les tests effectués contre le PNJ sont réalisés avec "
                             "deux dés, seul le plus mauvais résultat est pris en compte."
      },
      "http://co-drs.org/capacites/posture-de-combat/": {
        "short_description": "A votre tour, choisissez d’appliquer jusqu’à -1 par rang en attaque, en DEF ou aux"
                             " DM et obtenez l’équivalent en bonus au choix en attaque, en DEF ou aux DM."
      },
      "http://co-drs.org/capacites/potion-magique/": {
        "short_description": "Le Forgesort peut préparer une potion d’Agrandissement, de Forme gazeuse, de "
                             "Protection contre les éléments, d’Armure de mage ou de Chute ralentie."
      },
      "http://co-drs.org/capacites/poudre-puissante/": {
        "short_description": "L’Arquebusier sait préparer lui-même une poudre plus puissante, il ajoute "
                             "+10 mètres à la portée et +2 aux dégâts de toutes ses armes à poudre."
      },
      "http://co-drs.org/capacites/precision/": {
        "short_description": "Le Barde peut utiliser son score d’attaque à distance pour combattre au contact "
                             "lorsqu’il emploie une arme à une main légère."
      },
      "http://co-drs.org/capacites/prescience/": {
        "short_description": "Une fois par combat, à la fin d’un tour, le joueur peut décider que tout ce qui "
                             "s’est passé durant ce tour n’était que la vision d’un futur possible."
      },
      "http://co-drs.org/capacites/pression-mortelle/": {
        "short_description": "Le Moine frappe les points par lesquels circule l’énergie vitale d’une créature "
                             "vivante. En touchant un point précis, il libère ensuite des effets dévastateurs."
      },
      "http://co-drs.org/capacites/prison-vegetale/": {
        "short_description": "Le Druide peut commander à la végétation de pousser et bloquer ses ennemis. "
                             "Entravées, les cibles subissent un malus de -2 en attaque et en DEF."
      },
      "http://co-drs.org/capacites/proche-de-la-nature/": {
        "short_description": "Le Barbare obtient un bonus de +1 par Rang dans la voie aux tests de survie, de "
                             "discrétion ou d’observation en milieu naturel."
      },
      "http://co-drs.org/capacites/projectile-magique/": {
        "short_description": "Le Magicien choisit une cible visible située à moins de 50 mètres. Elle encaisse "
                             "automatiquement 1d4 points de dégâts."
      },
      "http://co-drs.org/capacites/projection/": {
        "short_description": "Sur 15 à 20 au test d’attaque, la victime est projetée et subit +3d6 DM "
                             "supplémentaires. Elle doit réussir un test de CON de difficulté 15 ou être Étourdie."
      },
      "http://co-drs.org/capacites/projection-du-ki/": {
        "short_description": "Le Moine projette une vague de force avec son corps et son esprit."
      },
      "http://co-drs.org/capacites/projection-mentale/": {
        "short_description": "Le Moine entre en méditation et projette son esprit hors de son corps. Celui-ci "
                             "ressemble à un ectoplasme de couleur blanche qui se déplace en volant."
      },
      "http://co-drs.org/capacites/protecteur/": {
        "short_description": "Une fois par tour, s’il est au contact d’un personnage, le golem peut s’interposer "
                             "et subir les DM d’une attaque à sa place."
      },
      "http://co-drs.org/capacites/protection-contre-le-mal/": {
        "short_description": "La cible obtient alors un bonus de +2 en DEF et pour les tests de résistance contre "
                             "les attaques des mort-vivants, démons, élémentaires et créatures conjurées."
      },
      "http://co-drs.org/capacites/protection-contre-les-elements/": {
        "short_description": "Le Magicien retranche à tous les DM de feu, de froid, d’électricité ou d’acide subis "
                             "un montant égal à 2 fois son Rang dans cette Voie.",
        "defense": [Mod(label="RD", target="fire", count=2),
                    Mod(label="RD", target="coldness", count=2),
                    Mod(label="RD", target="lightning", count=2),
                    Mod(label="RD", target="acid", count=2)],
        "duration": Duration(value="5+[INT]", unit="tr")
      },
      "http://co-drs.org/capacites/proteger-un-allie/": {
        "short_description": "Le Guerrier accorde le Mod. de DEF de son bouclier à un compagnon de son choix qui "
                             "se trouve juste à côté de lui."
      },
      "http://co-drs.org/capacites/prouesse/": {
        "short_description": "Le Guerrier réussit souvent des exploits physiques hors-norme. Une fois par tour, "
                             "vous pouvez sacrifier 1d4 PV pour obtenir +5 sur un test de FOR ou de DEX."
      },
      "http://co-drs.org/capacites/provocation/": {
        "short_description": "Le Voleur maîtrise l’art de se rendre désagréable, voire insupportable."
      },
      "http://co-drs.org/capacites/puissance-du-ki/": {
        "short_description": "Le Moine peut choisir d’utiliser 1d12 en attaque au lieu du d20 habituel. Si "
                             "l’attaque est réussie, il ajoute 2d6 aux DM."
      },
      "http://co-drs.org/capacites/putrefaction/": {
        "short_description": "En réussissant un test d’attaque magique, le Nécromancien fait pourrir les chairs de "
                             "sa victime."
      },
      "http://co-drs.org/capacites/rage-du-berserk/": {
        "short_description": "Le Barbare entre dans une rage berserk pour le reste du combat, ce qui le rend "
                             "particulièrement dangereux."
      },
      "http://co-drs.org/capacites/rappel/": {
        "short_description": "Le personnage peut à présent rappeler son familier à son contact par magie."
      },
      "http://co-drs.org/capacites/rappel-a-la-vie/": {
        "short_description": "Une fois par jour, le Prêtre peut rappeler à la vie un personnage décédé. Il doit "
                             "connaître personnellement la personne et posséder une relique lui appartenant."
      },
      "http://co-drs.org/capacites/rayon-affaiblissant/": {
        "short_description": "Le Magicien choisit une cible. Si son attaque magique réussit, le rayon affecte la "
                             "cible qui subit un malus de -2 à ses tests de FOR, d’attaque au contact et de dégâts."
      },
      "http://co-drs.org/capacites/reduction-des-dm/": {
        "short_description": "La créature est peu sensible aux DM provoqués par les armes, le métal rebondi sur "
                             "elle comme un vulgaire morceau de bois ou alors la créature guérit immédiatement."
      },
      "http://co-drs.org/capacites/reflexes-felins/": {
        "short_description": "Le Barbare obtient un bonus de +1 par Rang dans cette voie à son score d’Initiative "
                             "et à tous les tests de DEX destinés à esquiver."
      },
      "http://co-drs.org/capacites/regeneration/": {
        "short_description": "Une fois par jour, La cible touchée par le Druide guérit de 3 PV par tour pendant "
                             "[niveau du Druide + Mod. de SAG] tours."
      },
      "http://co-drs.org/capacites/renvoi-de-sort/": {
        "short_description": "Le Guerrier peut décider de renvoyer un sort qu’il vient d’absorber. Le sort absorbé "
                             "le tour précédent est retourné contre son expéditeur."
      },
      "http://co-drs.org/capacites/repli/": {
        "short_description": "Le Rôdeur se déplace en forêt en s’éloignant de ses ennemis. Le joueur fait un test "
                             "de DEX difficulté 10, en cas de succès, il disparaît de la vue de ses poursuivants."
      },
      "http://co-drs.org/capacites/resistance/": {
        "short_description": "Le nain gagne un bonus de +5 à tous ses tests de CON."
      },
      "http://co-drs.org/capacites/resistance-2/": {
        "short_description": "Le familier obtient une réduction des DM (RD) de 1 point par rang face à tous les "
                             "types de DM."
      },
      "http://co-drs.org/capacites/resistance-a-la-magie/": {
        "short_description": "Le Barbare devient capable de résister à la magie."
      },
      "http://co-drs.org/capacites/resistance-a-la-magie-2/": {
        "short_description": "Chaque fois que le personnage est la cible d’un sort, le joueur lance 1d6. Sur un "
                             "résultat supérieur au rang du sort, il peut en ignorer les effets."
      },
      "http://co-drs.org/capacites/resistance-legendaire/": {
        "short_description": "Le halfelin obtient un bonus de +5 à tous ses tests de CON et un bonus de +5 en DEF "
                             "contre la magie."
      },
      "http://co-drs.org/capacites/resistant/": {
        "short_description": "Le Druide obtient une réduction de DM égal à son [Rang x 2] contre toutes les "
                             "sources de dégâts « naturels »."
      },
      "http://co-drs.org/capacites/respiration-aquatique/": {
        "short_description": "Le Magicien peut respirer sous l’eau pendant 10 minutes.",
        "duration": Duration(value=10, unit="min")
      },
      "http://co-drs.org/capacites/riposte/": {
        "short_description": "Une fois par tour, lorsqu’un adversaire rate une attaque de contact contre le "
                             "Guerrier, le joueur obtient une attaque supplémentaire contre cet adversaire."
      },
      "http://co-drs.org/capacites/riposte-2/": {
        "short_description": "Le champion peut effectuer une attaque en action gratuite contre chaque adversaire "
                             "qui l’attaque à l’exception de celui qu’il a lui-même choisit d’attaquer à son tour."
      },
      "http://co-drs.org/capacites/rituel-de-puissance/": {
        "short_description": "Sur une attaque magique, le Magicien peut utiliser un d12 en attaque au lieu du d20 "
                             "habituel. Si l’attaque est réussie, il ajoute 2d6 aux DM."
      },
      "http://co-drs.org/capacites/robustesse/": {
        "short_description": "Le Guerrier gagne 3 PV supplémentaires au Rang 1, puis 3 PV de plus au Rang 3 de "
                             "cette Voie et enfin 3 PV au Rang 5."
      },
      "http://co-drs.org/capacites/rumeurs-et-legendes/": {
        "short_description": "A force de voyager, le Barde a appris toutes sortes de choses. Il peut essayer de se"
                             " «souvenir» d’une information historique, politique, géographique ou occulte."
      },
      "http://co-drs.org/capacites/rune-de-pouvoir/": {
        "short_description": "Le Forgesort peut lier un sort à un objet par une inscription runique."
      },
      "http://co-drs.org/capacites/rune-de-protection/": {
        "short_description": "Le Forgesort enchante une armure pour 24 h. Celle-ci permet d’ignorer les DM d’une "
                             "attaque une fois par combat."
      },
      "http://co-drs.org/capacites/rune-de-puissance/": {
        "short_description": "Le Forgesort enchante une arme pour 24 h. Celle-ci permet d’infliger les DM maximum "
                             "une fois par combat."
      },
      "http://co-drs.org/capacites/rune-d-energie/": {
        "short_description": "Le forgesort enchante un bijou pour 24 h. Celui-ci permet de relancer un d20 une "
                             "fois par combat sur un test d’attaque, de FOR, DEX ou CON."
      },
      "http://co-drs.org/capacites/runes-de-defense/": {
        "short_description": "Le Forgesort inscrit des runes de protection sur l’ensemble de son équipement et "
                             "parfois jusque sur sa peau. Il obtient un bonus de +1 en DEF par rang dans la voie."
      },
      "http://co-drs.org/capacites/sac-sans-fond/": {
        "short_description": "Le Forgesort possède un sac pour y mettre du matériel. Le sac peut aussi fournir les "
                             "objets qu’il désire de moins de 20 pa, 50 kg, 1m3 ou "
                             "1m de circonférence. Pas plus de 20 pa d’objets créés peuvent exister à la fois. Ils "
                             "disparaissent au bout d’une heure.",
        "special_property": [
            "Le sac pèse 1kg (même plein)",
            "50Kg / rang dans la voie",
            "Ne peut contenir de créature vivante"
        ]
      },
      "http://co-drs.org/capacites/sagesse-heroique/": {
        "short_description": "Le personnage augmente sa valeur de SAG de +2. Il peut désormais lancer deux d20 à "
                             "chaque fois qu’un test de SAG lui est demandé et conserver le meilleur résultat."
      },
      "http://co-drs.org/capacites/saignements/": {
        "short_description": "Du sang s’écoule de la bouche, du nez, des oreilles et même des yeux de la victime."
      },
      "http://co-drs.org/capacites/sanctuaire/": {
        "short_description": "Quand le Prêtre lance ce sort, tous les adversaires qui veulent l’attaquer doivent "
                             "d’abord réussir un test de SAG difficulté 15.",
        "duration": Duration(value="5+[CHA]", unit="tr"),
        "special_property": ["Fin si action d'attaque"]
      },
      "http://co-drs.org/capacites/sang-mordant/": {
        "short_description": "Le sang du Nécromancien se transforme en un acide qui gicle lorsqu’il subit une "
                             "blessure."
      },
      "http://co-drs.org/capacites/sans-peur/": {
        "short_description": "Le Chevalier est immunisé aux attaques de peur et il offre un bonus de [2 + Mod. de "
                             "CHA] à tous ses alliés contre ce type d’effet."
      },
      "http://co-drs.org/capacites/science-du-critique/": {
        "short_description": "Le Guerrier inflige des critiques sur 19-20 (18-20 lorsqu’il emploie une rapière ou "
                             "une Vivelame)."
      },
      "http://co-drs.org/capacites/second-ennemi-jure/": {
        "short_description": "Le Rôdeur choisit une nouvelle race ennemie. Les règles et avantages de la capacité "
                             "Ennemi juré s’appliquent à l’identique."
      },
      "http://co-drs.org/capacites/second-souffle/": {
        "short_description": "Une fois par combat, le Guerrier peut décider de ne pas attaquer lors du tour de "
                             "combat pour reprendre son souffle. Il récupère alors des PV."
      },
      "http://co-drs.org/capacites/sens-affutes/": {
        "short_description": "Le Rôdeur gagne un bonus de +2 à tous ses tests de SAG destinés à simuler la "
                             "perception."
      },
      "http://co-drs.org/capacites/sens-developpes/": {
        "short_description": "Capable de percevoir avec les sens de son familier, le personnage améliore "
                             "grandement la maîtrise de ses sens."
      },
      "http://co-drs.org/capacites/sergent/": {
        "short_description": "Une fois par tour, le sergent peut donner une action supplémentaire à n’importe "
                             "quel allié sous ses ordres à porté de vue."
      },
      "http://co-drs.org/capacites/serviteur-invisible/": {
        "short_description": "Ce sort crée une force invisible. Le serviteur peut effectuer à distance des tâches "
                             "simples."
      },
      "http://co-drs.org/capacites/seul-contre-tous/": {
        "short_description": "Le chevalier sait faire face à de nombreux adversaires, en tentant de profiter "
                             "d’une éventuelle faille dans leur garde."
      },
      "http://co-drs.org/capacites/siphon-des-ames/": {
        "short_description": "Chaque fois qu’une créature meurt à moins de 20 m du Nécromancien, il récupère "
                             "1d6 PV."
      },
      "http://co-drs.org/capacites/soigner/": {
        "short_description": "La créature est capable de soigner 50% des PV totaux de chaque créature qu’elle "
                             "touche une fois par jour."
      },
      "http://co-drs.org/capacites/soins-de-groupe/": {
        "short_description": "Une fois par combat, le Prêtre peut libérer une décharge d’énergie bienfaitrice : "
                             "tous ses compagnons en vue et lui récupèrent [1d8 + niveau du prêtre] PV perdus."
      },
      "http://co-drs.org/capacites/soins-legers/": {
        "short_description": "Le Prêtre peut toucher une cible, qui récupère alors [1d8 + niveau du prêtre] PV "
                             "perdus. Le Prêtre peut utiliser ce sort sur lui-même.",
        'special_property': ["Soigne : 1d8 PV + niveau"]
      },
      "http://co-drs.org/capacites/soins-moderes/": {
        "short_description": "Le Prêtre peut toucher une cible, qui récupère alors [2d8 + niveau du prêtre] PV "
                             "perdus. Le Prêtre peut utiliser ce sort sur lui-même.",
        'special_property': ["Soigne : 2d8 PV + niveau"]
      },
      "http://co-drs.org/capacites/solide-comme-un-roc/": {
        "short_description": "Le nain réduit tous les DM subis de 2 points. Ce bonus est cumulable avec d’autres "
                             "sources de réduction des DM."
      },
      "http://co-drs.org/capacites/sommeil/": {
        "short_description": "Plonge dans l’inconscience des créatures vivantes d’un Niveau inférieur ou égal à la "
                             "moitié du Niveau du personnage.",
        "full_description": "Plonge dans l’inconscience des créatures vivantes pendant [5 + Mod. de CHA] minutes. "
                            "Affecte un nombre de PV égal au test d’attaque magique de l’Ensorceleur dans une "
                            "zone de 10 m de diamètre (portée 20 m). Toutes les cibles doivent être d’un Niveau "
                            "inférieur ou égal à la moitié du Niveau du personnage. Il est possible de les "
                            "réveiller en les giflant (action d’attaque).",
      },
      "http://co-drs.org/capacites/souffle-enflamme/": {
        "short_description": "Le souffle est une attaque de zone affectant toutes les créatures dans un cône. "
                             "L’attaque inflige automatiquement des dégâts."
      },
      "http://co-drs.org/capacites/sous-tension/": {
        "short_description": "L’Ensorceleur se charge d’énergie électrique. Toute créature qui le blesse ou le "
                             "touche reçoit une décharge provoquant 1d6 DM. Il peut également délivrer une décharge "
                             "électrique.",
        "attack": Attack(
          atype='magical',
          name="(décharge)",
          range=Range(value=10, unit="m"),
          damages=Damage(
            base=[],
            other=[Mod(die=6, count=1, target="lightning"), 
                   Mod(mtype="+", target="CHA")],
          ),
          critical=RangeSet([20])
        ),
        "duration": Duration(value="5+[CHA]", unit="tr"),
      },
      "http://co-drs.org/capacites/soutenir/": {
        "short_description": "Tous les alliés de la créature dans un rayon de 20 mètres récupèrent [3d6 + NC] PV. "
                             "Ce pouvoir n’est utilisable que 3 fois par jour."
      },
      "http://co-drs.org/capacites/specialisation/": {
        "short_description": "Lorsque le Guerrier emploie son arme de prédilection, il gagne un bonus de +2 aux "
                             "DM."
      },
      "http://co-drs.org/capacites/sprint/": {
        "short_description": "Une fois par combat, le Voleur peut effectuer un "
                             "déplacement supplémentaire gratuit à n’importe quel moment du tour.",
        "range": Range(value=20, unit="m")
      },
      "http://co-drs.org/capacites/strangulation/": {
        "short_description": "En réussissant un test d’attaque magique, le Nécromancien étouffe une créature "
                             "vivante pourvu qu’il maintienne sa concentration. Elle s'affaiblie alors un peu "
                             "plus chaque tour. Si la victime sort du champ de vision du Nécromancien, le sort "
                             "prend fin.",
        "range": Range(value=20, unit="m"),
        "special_property": ["DM: 1d6 / tour",
                             "Concentration (L)",
                             "Tests (cible): -1 / tr"]
      },
      "http://co-drs.org/capacites/suggestion/": {
        "short_description": "Une fois par jour, le Barde peut suggérer une action à une créature. En cas de "
                             "réussite la créature fera tout son possible pour satisfaire sa demande."
      },
      "http://co-drs.org/capacites/superiorite-elfique/": {
        "short_description": "L’elfe augmente ses valeurs de DEX et SAG de +2."
      },
      "http://co-drs.org/capacites/superiorite-elfique-2/": {
        "short_description": "L’elfe augmente ses valeurs d’INT et de SAG de +2."
      },
      "http://co-drs.org/capacites/surprise/": {
        "short_description": "Le Voleur n’est jamais surpris. Il peut réaliser une Attaque sournoise en utilisant "
                             "une action d’attaque plutôt qu’une action limitée contre un adversaire Surpris."
      },
      "http://co-drs.org/capacites/surveillance/": {
        "short_description": "Le loup est constamment sur ses gardes. Le Rôdeur a donc un temps d’avance quand "
                             "des ennemis essaient de l’attaquer par surprise."
      },
      "http://co-drs.org/capacites/symetrie/": {
        "short_description": "Le personnage n’est plus obligé de manier une arme légère dans sa main secondaire."
      },
      "http://co-drs.org/capacites/talent-pour-la-magie/": {
        "short_description": "Le joueur choisit une capacité de rang 1 de n’importe quelle voie de Magicien ou "
                             "d’Ensorceleur. Il peut utiliser cette capacité en armure sans pénalité."
      },
      "http://co-drs.org/capacites/talent-pour-la-violence/": {
        "short_description": "Le joueur choisit une capacité de rang 1 de n’importe quelle voie de Barbare, de "
                             "Guerrier ou de la voie de l’homme."
      },
      "http://co-drs.org/capacites/tatouages/": {
        "short_description": "Le Barbare possède un tatouage magique qui améliore ses performances physiques."
      },
      "http://co-drs.org/capacites/telekinesie/": {
        "short_description": "L’Ensorceleur peut déplacer dans les airs un objet inerte ou une cible volontaire. Il "
                             "est possible de faire tomber un objet sur une cible surprise qui subit alors des "
                             "dégâts.",
        "duration": Duration(value="5+[CHA]", unit="tr"),
        "range": Range(value="20", unit="m"),
        "special_property": [
            "Poids maximum: 50kg / rang",
            "Déplacement: 10m / tr (mouvement)",
            "DM: 1d6 / 50kg"
          ]
      },
      "http://co-drs.org/capacites/teleportation/": {
        "short_description": "Le Magicien disparaît et réapparaît à un autre endroit.",
        "range": Range(value="10x[INT]", unit="m"),
        "special_property": [
            "Lieu arrivée: en ligne de vue ou parfaitement connu",
          ]

      },
      "http://co-drs.org/capacites/tenacite/": {
        "short_description": "Le nain augmente ses valeurs de CON et de SAG de +2."
      },
      "http://co-drs.org/capacites/tenebres/": {
        "short_description": "Le Nécromancien invoque une zone fixe de ténèbres magiques. Même les créatures "
                             "capables de voir dans le noir sont aveuglées dans cette zone.",
        "area": Area(value=10, unit="m"),
        "duration": Duration(value="5+[INT]", unit="tr")
      },
      "http://co-drs.org/capacites/tir-aveugle/": {
        "short_description": "Le Rôdeur peut attaquer à distance un ennemi qu’il ne voit pas, mais dont il connaît "
                             "l’existence et la direction approximative, comme s’il le voyait."
      },
      "http://co-drs.org/capacites/tir-de-barrage/": {
        "short_description": "L’Arquebusier met en joue une cible sur laquelle il a l’Initiative et attend. Si "
                             "elle se déplace à ce tour, il effectue une attaque à distance."
      },
      "http://co-drs.org/capacites/tir-de-semonce/": {
        "short_description": "Après avoir raté une attaque à distance au tour précédent, l’Arquebusier déclare "
                             "qu’il s’agissait d’un tir de semonce."
      },
      "http://co-drs.org/capacites/tir-double/": {
        "short_description": "L’Arquebusier est capable de tirer avec une pétoire dans chaque main sans pénalité."
      },
      "http://co-drs.org/capacites/tir-mortel/": {
        "short_description": "Pour une attaque à distance, l’Arquebusier peut choisir d’utiliser un d12 pour "
                             "son attaque au lieu du d20 habituel. En cas de réussite, il ajoute +2d6 aux DM."
      },
      "http://co-drs.org/capacites/tir-parabolique/": {
        "short_description": "L’Arquebusier est capable de réaliser un tir à longue distance sans pénalité : il "
                             "double la portée des armes à distance."
      },
      "http://co-drs.org/capacites/tir-precis/": {
        "short_description": "L’Arquebusier ajoute un bonus de +1 aux DM des armes de tir jusqu’à une portée "
                             "de [5 x Mod. de DEX]."
      },
      "http://co-drs.org/capacites/tir-rapide/": {
        "short_description": "Le Rôdeur peut faire 2 attaques à distance pendant ce tour."
      },
      "http://co-drs.org/capacites/touche-a-tout/": {
        "short_description": "Le Barde peut choisir n’importe quelle capacité de Rang 1 à 3 de son choix au sein "
                             "d’un autre Profil de Chroniques Oubliées.",
        "full_description": "Le Barde peut choisir n’importe quelle capacité de Rang 1 à 3 de son choix au sein "
                            "d’un autre Profil de Chroniques Oubliées."
      },
      "http://co-drs.org/capacites/tour-de-force/": {
        "short_description": "Le Barbare peut temporairement décupler ses ressources physiques pour faire usage "
                             "d’une force prodigieuse."
      },
      "http://co-drs.org/capacites/transe-de-guerison/": {
        "short_description": "Une fois après chaque combat, le Moine peut méditer pendant 10 minutes et récupérer "
                             "ainsi [niveau + Mod de SAG] PV."
      },
      "http://co-drs.org/capacites/traquenard/": {
        "short_description": "Le Rôdeur gagne un bonus de +2 en attaque et +2d6 aux DM sur sa première attaque "
                             "contre une créature s’il possède un meilleur score d’Initiative."
      },
      "http://co-drs.org/capacites/tueur-fantasmagorique/": {
        "short_description": "Ce sort invoque les pires terreurs d’une créature vivante et lui fait croire à sa "
                             "propre mort."
      },
      "http://co-drs.org/capacites/vampirisation/": {
        "short_description": "lors d'une attaque magique, la cible subit [1d6 x NC/2] DM et la créature se "
                             "régénère autant de PV que de DM infligés."
      },
      "http://co-drs.org/capacites/versatile/": {
        "short_description": "Le personnage obtient une capacité de rang 1 de n’importe quel Profil au choix du "
                             "joueur ou une capacité de rang 2 d’un profil de la même famille que le sien."
      },
      "http://co-drs.org/capacites/vetements-sacres/": {
        "short_description": "La tenue religieuse traditionnelle du Prêtre remplace une armure et a été bénie à "
                             "cet effet : il obtient un bonus en DEF égal à +1 pour chaque Rang dans cette Voie."
      },
      "http://co-drs.org/capacites/vif-et-alerte/": {
        "short_description": "Le halfelin augmente ses valeurs de DEX et de CON de +2."
      },
      "http://co-drs.org/capacites/vigilance/": {
        "short_description": "Le Barbare possède des sens très affûtés, il est difficile de le surprendre, il "
                             "gagne un bonus de +5 à tous les tests pour détecter les pièges ou les embuscades."
      },
      "http://co-drs.org/capacites/vigueur/": {
        "short_description": "Le Barbare est capable de prouesses physiques extraordinaires, il obtient un bonus "
                             "de +2 par Rang dans la voie aux tests de course, de saut ou d’escalade."
      },
      "http://co-drs.org/capacites/vitalite-debordante/": {
        "short_description": "Le Barbare guérit à une vitesse presque surnaturelle. Tant qu’il lui reste au moins "
                             "1 PV, il récupère 1d6 PV par heure, de nuit comme de jour.",
      },
      "http://co-drs.org/capacites/vitalite-surnaturelle/": {
        "short_description": "La créature guérit à un rythme fantastique, elle récupère 5 PV à la fin de chaque "
                             "tour."
      },
      "http://co-drs.org/capacites/vitesse-du-felin/": {
        "short_description": "Le Druide gagne +1 par rang dans la voie en Initiative et aux tests de course, "
                             "d’escalade ou de saut."
      },
      "http://co-drs.org/capacites/vivacite/": {
        "short_description": "Le Guerrier gagne +3 en Initiative.",
      },
      "http://co-drs.org/capacites/vol/": {
        "short_description": "Le Magicien peut voler et sa vitesse de déplacement est la même qu’au sol.",
        "duration": Duration(value="1d6+[INT]", unit="min")
      },
      "http://co-drs.org/capacites/vol-rapide/": {
        "short_description": "La créature obtient une action de mouvement supplémentaire par tour lorsqu’elle est "
                             "en vol."
      },
      "http://co-drs.org/capacites/zone-de-silence/": {
        "short_description": "Le Barde crée une zone de silence fixe de 5 mètres de diamètre dans laquelle tous "
                             "les sons émis sont annulés."
      },
    },
}
