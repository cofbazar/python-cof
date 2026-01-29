# -*- coding: utf-8 -*-

import cof.properties
import config.cofConfig

magicwands = {
    'magical_level': {
        'mineur': {
            'way_rank_list': [1, 2, 3, 4, 5],
            'use': 5
        },
    },
    'weight': cof.properties.Weight(value=0.1, unit='Kg'),
    'cost': lambda item: cof.properties.Cost(
        value=item.way_rank * item.way_rank * config.cofConfig.config['global']['cost']['spells'] * item.use,
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'addons': {
        'magic-wand-forme-etheree': {
            "short_description": "L'utilisateur de cette baguette (et son équipement) deviennent "
                                 "translucides et intangibles. Ils peuvent passer à travers murs et "
                                 "obstacles.",
            "full_description": "L'utilisateur de cette baguette et tout son équipement deviennent "
                                "translucides et intangibles pendant [5 + Mod. de CHA] tours. Sous "
                                "cette forme, elle peut passer à travers murs et obstacles, et ne peut "
                                "subir aucun DM physiques.",
        },
        'magic-wand-6eme-sens': {
            "short_description": "L'utilisateur de cette baguette sait un peu en avance "
                                 "ce qui va arriver.",
            "full_description": "L'utilisateur de cette baguette sait toujours légèrement en avance "
                                "ce qui va arriver. "
                                "Elle gagne un bonus de +1 par Rang dans la Voie en Initiative et en "
                                "DEF, ainsi qu’un bonus de +2 par Rang à tous les tests pour éviter "
                                "d’être surprise.",
        },
        'magic-wand-amitie': {
            "short_description": "Si l'utilisateur de cette baguette réussie une attaque magique "
                                 "contre le score max de PV d'une cible humanoïde, celle-ci se comporte "
                                 "comme un ami de longue date tant qu’elle n’est pas attaquée.",
            "full_description": "Si La personne qui utilise cette baguette réussit un test d’Attaque magique "
                                "(portée 10 m) contre le score max de PV d’une cible humanoïde, celle-ci "
                                "se comporte comme un ami de longue date tant qu’elle n’est pas attaquée. "
                                "Elle peut résister au sort avec un test de SAG difficulté [12 + Mod. "
                                "de CHA], renouvelable une fois par jour.",
        },
        'magic-wand-dedoublement': {
            "short_description": "Cette baguette crée un double translucide de la cible (attaque magique). "
                                 "Le double est controlé, possède les mêmes Caractéristiques que l’original, "
                                 "la moitié des PV et les DM qu’il inflige sont divisés par "
                                 "deux. Il disparaît si ses PV tombent à 0. Une créature ne peut être "
                                 "dédoublée qu’une fois par combat.",
            "full_description": "Sur une attaque magique réussie (portée 20 m), la personne qui utilise "
                                "cette baguette crée un double translucide de la cible pendant [5 + Mod. de CHA] "
                                "tours. Le double est sous son contrôle. Il possède les mêmes "
                                "Caractéristiques que l’original mais seulement la moitié de ses PV et "
                                "tous les DM qu’il inflige sont divisés par deux. Il disparaît si ses "
                                "PV tombent à 0. Une créature ne peut être dédoublée qu’une fois par "
                                "combat.",
        },
        'magic-wand-arme-dansante': {
            "short_description": "Cette baguette crée une lame d’énergie lumineuse. Dès le premier tour, la "
                                 "personne qui utilise cette baguette peut lui ordonner d’attaquer une cible "
                                 "de son choix (action gratuite).",
            "full_description": "Cette baguette crée une lame d’énergie lumineuse pendant [5 + Mod. de CHA] "
                                "tours. Dès le premier tour, la personne qui utilise cette baguette peut lui "
                                "ordonner d’attaquer une cible de son choix (action gratuite, portée 20 m). "
                                "L’attaque magique de la lame = attaque magique de la personne qui "
                                "utilise cette baguette, [1d8 + Mod de CHA] DM.",
        },
        'magic-wand-agrandissement': {
            "short_description": "L'utilisateur de cette baguette voit sa taille ou celle d'une cible "
                                 " volontaire (au contact) augmenter de 50%.",
            "full_description": "L'utilisateur de cette baguette voit sa taille augmenter de "
                                "50% pendant [5 + Mod. d’INT] tours. Elle gagne +2 aux DM au contact "
                                "et aux tests de FOR. Pataud, elle subit un malus de -2 aux tests de DEX."
        },
        'magic-wand-boule-de-feu': {
            "short_description": "Cette baguette lance une boule de feu qui inflige "
                                 "des dégâts à toutes "
                                 "personnes se trouvant dans la zone d'effet.",
            "full_description": "L'utilisateur de cette baguette choisit une cible située à moins de "
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
        'magic-wand-arme-enflammee': {
            "short_description": "L'utilisateur de cette baguette peut enflammer une arme qui infige alors "
                                 "des dégâts supplémentaires de feu.",
            "full_description": "L'utilisateur de cette baguette  peut enflammer une arme pour "
                                "[5 + Mod. d’INT] tours. Celle-ci inflige +1D6 DM de feu.",
        },
        'magic-wand-armure-de-mage': {
            "short_description": "L'utilisateur de cette baguette fait apparaître un nuage magique "
                                 "argenté qui la protège contre les attaques adverses.",
            "full_description": "L'utilisateur de cette baguette fait apparaître un nuage magique "
                                "argenté qui la protège contre les attaques adverses. Elle bénéficie "
                                "d’un bonus de +4 à la DEF pour le reste du combat. Si le sort est "
                                "cumulé à une armure physique, le bonus est divisé par 2 (+2 DEF).",
        },   
        'magic-wand-detection-de-la-magie': {
            "short_description": "L'utilisateur de cette baguette se concentre et détecte la présence "
                                 "de toute inscription et de tout objet magique situé dans la pièce "
                                 "où il se trouve. cette baguette permet aussi d’analyser les propriétés "
                                 "d’un objet magique au prix de 2 heures d’étude et de 100 pa de "
                                 "poudre d’argent.",
            "full_description": "L'utilisateur de cette baguette se concentre et détecte la présence "
                                "de toute inscription et de tout objet magique situé dans la pièce "
                                "où il se trouve (ou dans les 15 mètres autour de lui). cette baguette "
                                "permet aussi d’analyser les propriétés d’un objet magique au prix "
                                "de 2 heures d’étude et de 100 pa de poudre d’argent.",
        },
         'magic-wand-aspect-de-la-succube': {
            "short_description": "L'utilisateur de cette baguette acquiert une beauté fascinante.",
            "full_description": "L'utilisateur de cette baguette acquiert une beauté fascinante "
                                "pour [5 + Mod. d’INT] tours. Il gagne un bonus de +5 aux tests de "
                                "CHA ainsi qu’une attaque de contact nécessitant un test d’attaque "
                                "magique et qui inflige [1d4 + Mod. de CHA] DM. Ces DM sont "
                                "transformés en PV, au bénéfice du Nécromancien (sans dépasser "
                                "son score max de PV).",
        },
        'magic-wand-baiser-du-vampire': {
            "short_description": "L'utilisateur de cette baguette fait une attaque infligeant des "
                                 "dégâts qui lui permettent de récupèrer autant de PV.",
            "full_description": "Cette baguette nécessite la réussite d’un test d’attaque magique "
                                "(portée 50 m). La cible subit [1d8+Mod. d’INT] DM et la personne "
                                "qui a utilisée cette baguette récupère autant de PV (sans dépasser son "
                                "score max de PV).",
        },
        'magic-wand-animation-des-morts': {
            "short_description": "Cette baguette anime (1 par rang) le cadavre d’un humanoïde "
                                 "de taille moyenne, décédé depuis moins d’une heure. Le zombi "
                                 "comprend les ordres: Attaquer, Suivre, Garder et Pas bouger. Il "
                                 "se déplace 2 fois moins vite, perd 1 PV/min et à 0 PV tombe en "
                                 "poussière.",
            "full_description": "L'utilisateur de cette baguette anime le cadavre "
                                "d’un humanoïde de taille moyenne, décédé depuis moins d’une "
                                "heure. Le zombi comprend les ordres « Attaquer », « Suivre »,"
                                " « Garder » et « Pas bouger ». Zombie : Init 8, DEF 10, PV 12,"
                                " Att +3, DM 1d6+1, se déplace à 50% de la vitesse normale. Le "
                                "zombi se dégrade et perd 1PV par minute. La personne peut "
                                "contrôler un zombi par rang. Un zombi détruit tombe en poussière.",
        },
        'magic-wand-exsangue': {
            "short_description": "Lorsque l'utilisateur de cette baguette tombe à 0 PV, il peut "
                                 "continuer à agir mais avec un malus. Une attaque réussie lui "
                                 "infligeant au moins 1 point de DM l’achèvera.",
            "full_description": "Lorsque l'utilisateur de cette baguette tombe à 0 PV, il peut "
                                "continuer à agir mais avec un malus de -2 à tous ses tests. Une "
                                "nouvelle attaque réussie infligeant au moins 1 point de DM finira "
                                "par l’achever !",
        },
        'magic-wand-ombre-mortelle': {
            "short_description": "L’ombre de la cible touché par cette baguette attaque son propriétaire. L’ombre poursuit sa "
                                 "cible partout où elle se réfugie. L'ombre possède la même attaque que la cible mais "
                                 "inflige seulement la moitié des DM.",
            "full_description": "L’ombre de la cible touché par cette baguette attaque son propriétaire "
                                "pendant [3 + Mod. d’INT] tours (portée 20 m). L’ombre poursuit "
                                "sa cible partout où elle se réfugie. Ombre : 1 attaque par tour, "
                                "att = att de la cible, DM = DM de la cible divisés par 2.",
        },
        'magic-wand-ailes-celestes': {
            "short_description": "Des ailes divines poussent dans le dos de L'utilisateur de cette baguette. "
                                 "Il peut alors voler à une vitesse équivalente de deux "
                                 "fois son déplacement normal.",
            "full_description": "Des ailes divines poussent dans le dos de L'utilisateur de cette baguette. "
                                 "Il peut alors voler à une vitesse équivalente de deux "
                                 "fois son déplacement normal pendant [5 + Mod. de SAG] tours. "
                                 "Rester en vol stationnaire avec les ailes céleste est une "
                                 "action de mouvement.",
        },   
        'magic-wand-benediction': {
            "short_description": "L'utilisateur de cette bagette entonne un chant pour encourager ses "
                                "compagnons en vue. Ceux-ci (ainsi que lui-même) bénéficient d’un bonus.",
            "full_description": "L'utilisateur de cette baguette entonne un chant pour encourager ses "
                                "compagnons en vue. Ceux-ci (ainsi que lui-même) bénéficient d’un bonus "
                                "de +1 à tous leurs tests de Caractéristique et d’attaque pendant "
                                "[3 + Mod. de SAG] tours.",
        },
        'magic-wand-guerison': {
            "short_description": "L'utilisateur de cette baguette peut toucher une cible qui récupère alors "
                                 "tous ses PV. Il est aussi guéri des poisons, maladies et affaiblissements "
                                 "de Caractéristiques.",
            "full_description": "L'utilisateur de cette baguette peut toucher une cible qui récupère alors "
                                 "tous ses PV. Il est aussi guéri des poisons, maladies et affaiblissements "
                                 "de Caractéristiques.",
        },
        'magic-wand-delivrance': {
            "short_description": "L'utilisateur de cette baguette annule les pénalités infligées par les sorts, "
                                 "les malédictions, la pétrification et les effets de capacités spéciales.",
            "full_description": "L'utilisateur de cette baguette annule les pénalités infligées par les "
                                "sorts, les malédictions, la pétrification et les effets de capacités spéciales "
                                "(douleur, mutilation, poisons etc.)."
        },
        'magic-wand-animation-dun-arbre': {
            "short_description": "L'utilisateur de cette baguette peut animer un arbre en le touchant.",
            "full_description": "L'utilisateur de cette baguette peut animer un arbre en le touchant. Il "
                                "combat pendant [niveau de la personne] tours.",
        },
    },
    'quest-magic-wands': []
}
