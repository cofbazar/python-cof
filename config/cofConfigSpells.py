# -*- coding: utf-8 -*-

from cof.properties import *
import config.cofConfig

spells = {
    'magical_level': {
        'mineur': [1, 2, 3, 4, 5, 6],
    },
    'use': 1,
    'weight': Weight(value=0.1, unit='Kg'),
    'cost': lambda item: Cost(
        value=item.way_rank * item.way_rank * config.cofConfig.config['global']['cost']['spells'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'addons': {
        'spell-forme-etheree': {
            "short_description": "La personne qui utilise ce sort (et son équipement) deviennent "
                                 "translucides et intangibles. Ils peuvent passer à travers murs et "
                                 "obstacles.",
            "full_description": "La personne qui utilise ce sort et tout son équipement deviennent "
                                "translucides et intangibles pendant [5 + Mod. de CHA] tours. Sous "
                                "cette forme, elle peut passer à travers murs et obstacles, et ne peut "
                                "subir aucun DM physiques.",
        },
        'spell-6eme-sens': {
            "short_description": "La personne qui utilise ce sort sait toujours légèrement en avance "
                                 "ce qui va arriver.",
            "full_description": "La personne qui utilise ce sort sait toujours légèrement en avance "
                                "ce qui va arriver. "
                                "Elle gagne un bonus de +1 par Rang dans la Voie en Initiative et en "
                                "DEF, ainsi qu’un bonus de +2 par Rang à tous les tests pour éviter "
                                "d’être surprise.",
        },
        'spell-amitie': {
            "short_description": "Si la personne qui utilise ce sort réussie un test d’Attaque magique "
                                 "contre le score max de PV d'une cible humanoïde, celle-ci se comporte "
                                 "comme un ami de longue date tant qu’elle n’est pas attaquée.",
            "full_description": "Si La personne qui utilise ce sort réussit un test d’Attaque magique "
                                "(portée 10 m) contre le score max de PV d’une cible humanoïde, celle-ci "
                                "se comporte comme un ami de longue date tant qu’elle n’est pas attaquée. "
                                "Elle peut résister au sort avec un test de SAG difficulté [12 + Mod. "
                                "de CHA], renouvelable une fois par jour.",
        },
        'spell-dedoublement': {
            "short_description": "Ce sort cré un double translucide de la cible qui passe sous son "
                                 "contrôle (attaque magique). Il "
                                 "possède les mêmes Caractéristiques que l’original, "
                                 "la moitié de ses PV et tous les DM qu’il inflige sont divisés par "
                                 "deux. Une créature ne peut être dédoublée qu’une fois par "
                                 "combat et le double disparaît si ses PV tombent à 0.",
            "full_description": "Sur une Attaque magique réussie (portée 20 m), la personne qui utilise "
                                "ce sort cré un double translucide de la cible pendant [5 + Mod. de CHA] "
                                "tours. Le double est sous son contrôle. Il possède les mêmes "
                                "Caractéristiques que l’original mais seulement la moitié de ses PV et "
                                "tous les DM qu’il inflige sont divisés par deux. Il disparaît si ses "
                                "PV tombent à 0. Une créature ne peut être dédoublée qu’une fois par "
                                "combat.",
        },
        'spell-arme-dansante': {
            "short_description": "Le sort cré une lame d’énergie lumineuse. Dès le premier tour, la "
                                 "personne qui utilise ce sort peut lui ordonner d’attaquer une cible "
                                 "de son choix (action gratuite).",
            "full_description": "Le sort cré une lame d’énergie lumineuse pendant [5 + Mod. de CHA] "
                                "tours. Dès le premier tour, la personne qui utilise ce sort peut lui "
                                "ordonner d’attaquer une cible de son choix (action gratuite, portée 20 m). "
                                "L’attaque magique de la lame = attaque magique de la personne qui "
                                "utilise ce sort, [1d8 + Mod de CHA] DM.",
        },
        'spell-agrandissement': {
            "short_description": "La personne qui utilise ce sort voit sa taille ou celle d'une cible "
                                 " volontaire (au contact) augmenter de 50%.",
            "full_description": "La personne qui utilise ce sort voit sa taille augmenter de "
                                "50% pendant [5 + Mod. d’INT] tours. Elle gagne +2 aux DM au contact "
                                "et aux tests de FOR. Pataud, elle subit un malus de -2 aux tests de DEX."
        },
        'spell-boule-de-feu': {
            "short_description": "La personne qui utilise ce sort lance une boule de feu qui inflige "
                                 "des dégâts à toutes "
                                 "personnes (y compris ses alliés) se trouvant dans la zone d'effet.",
            "full_description": "La personne qui utilise ce sort choisit une cible située à moins de "
                                "30 mètres. Il fait "
                                "un test d’attaque magique et le compare à la DEF de tous les "
                                "personnages (y compris le Magicien et ses compagnons) se trouvant "
                                "dans un rayon de 6 mètres autour de la cible. Chaque victime pour "
                                "laquelle le test est un succès encaisse [4d6 + Mod. d’INT] de DM "
                                "et doit effectuer un test de DEX difficulté 10 + Mod. d’INT du "
                                "Magicien pour ne subir que la moitié des DM. Quand le test "
                                "d’attaque est un échec, la cible subit automatiquement la moitié "
                                "des DM (pas besoin de faire le test de DEX).",
        },
        'spell-arme-enflammee': {
            "short_description": "La personne qui lance ce sort peut enflammer une arme qui infige alors "
                                 "des dégâts supplémentaires de feu.",
            "full_description": "La personne qui lance ce sort  peut enflammer une arme pour "
                                "[5 + Mod. d’INT] tours. Celle-ci inflige +1D6 DM de feu.",
        },
        'spell-armure-de-mage': {
            "short_description": "La personne qui lance ce sort fait apparaître un nuage magique "
                                 "argenté qui la protège contre les attaques adverses.",
            "full_description": "La personne qui lance ce sort fait apparaître un nuage magique "
                                "argenté qui la protège contre les attaques adverses. Elle bénéficie "
                                "d’un bonus de +4 à la DEF pour le reste du combat. Si le sort est "
                                "cumulé à une armure physique, le bonus est divisé par 2 (+2 DEF).",
        },   
        'spell-detection-de-la-magie': {
            "short_description": "La personne qui lance ce sort se concentre et détecte la présence "
                                 "de toute inscription et de tout objet magique situé dans la pièce "
                                 "où elle se trouve. Ce sort permet aussi d’analyser les propriétés "
                                 "d’un objet magique au prix de 2 heures d’étude et de 100 pa de "
                                 "poudre d’argent.",
            "full_description": "La personne qui lance ce sort se concentre et détecte la présence "
                                "de toute inscription et de tout objet magique situé dans la pièce "
                                "où il se trouve (ou dans les 15 mètres autour de lui). Ce sort "
                                "permet aussi d’analyser les propriétés d’un objet magique au prix "
                                "de 2 heures d’étude et de 100 pa de poudre d’argent.",
        },
         'spell-aspect-de-la-succube': {
            "short_description": "La personne qui lance ce sort acquiert une beauté fascinante.",
            "full_description": "La personne qui lance ce sort acquiert une beauté fascinante "
                                "pour [5 + Mod. d’INT] tours. Elle gagne un bonus de +5 aux tests de "
                                "CHA ainsi qu’une attaque de contact nécessitant un test d’attaque "
                                "magique et qui inflige [1d4 + Mod. de CHA] DM. Ces DM sont "
                                "transformés en PV, au bénéfice du Nécromancien (sans dépasser "
                                "son score max de PV).",
        },
        'spell-baiser-du-vampire': {
            "short_description": "La personne qui lance ce sort fait une attaque infligeant des "
                                 "dégâts qui lui permettent de récupèrer autant de PV.",
            "full_description": "Ce sort nécessite la réussite d’un test d’attaque magique "
                                "(portée 50 m). La cible subit [1d8+Mod. d’INT] DM et la personne "
                                "qui a lancée ce sort récupère autant de PV (sans dépasser son "
                                "score max de PV).",
        },
        'spell-animation-des-morts': {
            "short_description": "La personne qui lance ce sort anime (1 par rang) le cadavre d’un humanoïde "
                                 "de taille moyenne, décédé depuis moins d’une heure. Le zombi "
                                 "comprend les ordres: Attaquer, Suivre, Garder et Pas bouger. Il "
                                 "se déplace 2 fois moins vite, perd 1 PV/min et à 0 PV tombe en "
                                 "poussière.",
            "full_description": "La personne qui lance ce sort anime le cadavre "
                                "d’un humanoïde de taille moyenne, décédé depuis moins d’une "
                                "heure. Le zombi comprend les ordres « Attaquer », « Suivre »,"
                                " « Garder » et « Pas bouger ». Zombie : Init 8, DEF 10, PV 12,"
                                " Att +3, DM 1d6+1, se déplace à 50% de la vitesse normale. Le "
                                "zombi se dégrade et perd 1PV par minute. La personne peut "
                                "contrôler un zombi par rang. Un zombi détruit tombe en poussière.",
        },
        'spell-exsangue': {
            "short_description": "Lorsque la personne qui a lancée ce sort tombe à 0 PV, elle peut "
                                 "continuer à agir mais avec un malus. Une attaque réussie lui "
                                 "infligeant au moins 1 point de DM l’achèvera.",
            "full_description": "Lorsque la personne qui a lancée ce sort tombe à 0 PV, elle peut "
                                "continuer à agir mais avec un malus de -2 à tous ses tests. Une "
                                "nouvelle attaque réussie infligeant au moins 1 point de DM finira "
                                "par l’achever !",
        },
        'spell-ombre-mortelle': {
            "short_description": "L’ombre de la cible touché par ce sort attaque son propriétaire. L’ombre poursuit sa "
                                 "cible partout où elle se réfugie. L'ombre possède la même attaque que la cible mais "
                                 "inflige seulement la moitié des DM.",
            "full_description": "L’ombre de la cible touché par ce sort attaque son propriétaire "
                                "pendant [3 + Mod. d’INT] tours (portée 20 m). L’ombre poursuit "
                                "sa cible partout où elle se réfugie. Ombre : 1 attaque par tour, "
                                "att = att de la cible, DM = DM de la cible divisés par 2.",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
        },
        'spell-ailes-celestes': {
            "short_description": "Des ailes divines poussent dans le dos de la personne qui lance le sort. "
                                 "Elle peut alors voler à une vitesse équivalente de deux "
                                 "fois son déplacement normal.",
            "full_description": "Des ailes divines poussent dans le dos de la personne qui lance le sort. "
                                 "Elle peut alors voler à une vitesse équivalente de deux "
                                 "fois son déplacement normal pendant [5 + Mod. de SAG] tours. "
                                 "Rester en vol stationnaire avec les ailes céleste est une "
                                 "action de mouvement.",
        },   
        'spell-benediction': {
            "short_description": "La personne qui lance le sort entonne un chant pour encourager ses "
                                "compagnons en vue. Ceux-ci (ainsi qu'elle-même) bénéficient d’un bonus.",
            "full_description": "La personne qui lance le sort entonne un chant pour encourager ses "
                                "compagnons en vue. Ceux-ci (ainsi qu'elle-même) bénéficient d’un bonus "
                                "de +1 à tous leurs tests de Caractéristique et d’attaque pendant "
                                "[3 + Mod. de SAG] tours.",
        },
        'spell-guerison': {
            "short_description": "La personne qui lance le sort peut toucher une cible qui récupère alors "
                                 "tous ses PV. Elle est aussi guérie des poisons, maladies et affaiblissements "
                                 "de Caractéristiques.",
            "full_description": "La personne qui lance le sort peut toucher une cible qui récupère alors "
                                 "tous ses PV. Elle est aussi guérie des poisons, maladies et affaiblissements "
                                 "de Caractéristiques.",
        },
        'spell-delivrance': {
            "short_description": "La personne lance ce sort annule les pénalités infligées par les sorts, "
                                 "les malédictions, la pétrification et les effets de capacités spéciales.",
            "full_description": "La personne lance ce sort annule les pénalités infligées par les "
                                "sorts, les malédictions, la pétrification et les effets de capacités spéciales "
                                "(douleur, mutilation, poisons etc.)."
        },
        'spell-animation-dun-arbre': {
            "short_description": "La personne lance ce sort peut animer un arbre en le touchant.",
            "full_description": "La personne lance ce sort peut animer un arbre en le touchant. Il "
                                "combat pendant [niveau de la personne] tours.",
        },
    },
}
