# -*- coding: utf-8 -*-
from cof.properties import *
import config.cofConfig

potions = {
    'magical_level': {
        'mineur': {'use': 1, 'label': 'mineure'},
        'moyen': {'use': 3, 'label': 'moyenne'}
    },
    'weight': Weight(value=0.1, unit='Kg'),
    'cost': lambda item: Cost(
        value=item.way_rank * item.way_rank * config.cofConfig.config['global']['cost']['potions'] * item.use,
        unit=config.cofConfig.config['global']['cost']['unit']).iso()
    if item.use > 0 else
    Cost(
        value=item.way_rank * item.way_rank * config.cofConfig.config['global']['cost']['potions'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'addons': {
        'potion-soins-legers-mineur': {
            "short_description": "La personne qui boit cette potion récupère alors [1d8 + niveau] PV perdus.",
            "full_description": "La personne qui boit cette potion récupère alors [1d8 + niveau] PV perdus."
        },
        'potion-soins-legers-moyen': {
            "short_description": "La personne qui boit cette potion récupère alors [1d8 + niveau] PV perdus.",
            "full_description": "La personne qui boit cette potion récupère alors [1d8 + niveau] PV perdus."
        },
        'potion-soins-moderes-mineur': {
            "short_description": "La personne qui boit cette potion récupère alors [2d8 + niveau] PV perdus.",
            "full_description": "La personne qui boit cette potion récupère alors [2d8 + niveau] PV perdus."
        },
        'potion-soins-moderes-moyen': {
            "short_description": "La personne qui boit cette potion récupère alors [2d8 + niveau] PV perdus.",
            "full_description": "La personne qui boit cette potion récupère alors [2d8 + niveau] PV perdus."
        },
        'potion-delivrance-mineur': {
            "short_description": "La personne qui boit cette potion annule les pénalités infligées par les sorts, "
                                 "les malédictions, la pétrification et les effets de capacités spéciales.",
            "full_description": "La personne qui boit cette potion annule les pénalités infligées par les "
                                "sorts, les malédictions, la pétrification et les effets de capacités spéciales "
                                "(douleur, mutilation, poisons etc.)."
        },
        'potion-delivrance-moyen': {
            "short_description": "La personne qui boit cette potion annule les pénalités infligées par les sorts, "
                                 "les malédictions, la pétrification et les effets de capacités spéciales.",
            "full_description": "La personne qui boit cette potion annule les pénalités infligées par les "
                                "sorts, les malédictions, la pétrification et les effets de capacités spéciales "
                                "(douleur, mutilation, poisons etc.)."
        },
        'potion-detection-de-linvisible-mineur': {
            "short_description": "La personne qui boit cette potion détecte les créatures invisibles ou cachées "
                                 "et si un sort de Clairvoyance affecte l’endroit.",
            "full_description": "Pendant [5 + Mod. de CHA] tours, la personne qui boit cette potion détecte les "
                                "créatures invisibles ou cachées à moins de 30 mètres et détecte si un sort de "
                                "Clairvoyance affecte l’endroit. Aveuglé, ce sort lui permet de voir normalement."
        },
        'potion-detection-de-linvisible-moyen': {
            "short_description": "La personne qui boit cette potion détecte les créatures invisibles ou cachées "
                                 "et si un sort de Clairvoyance affecte l’endroit.",
            "full_description": "Pendant [5 + Mod. de CHA] tours, la personne qui boit cette potion détecte les "
                                "créatures invisibles ou cachées à moins de 30 mètres et détecte si un sort de "
                                "Clairvoyance affecte l’endroit. Aveuglé, ce sort lui permet de voir normalement."
        }, 
        'potion-agrandissement-mineur': {
            "short_description": "La personne qui boit cette potion voit sa taille augmenter de 50% "
                                 "pendant [5 + Mod. d’INT] tours.",
            "full_description": "La personne qui boit cette potion voit sa taille augmenter de "
                                "50% pendant [5 + Mod. d’INT] tours. Il gagne +2 aux DM au contact et aux tests "
                                "de FOR. Pataud, il subit un malus de -2 aux tests de DEX."
        },
        'potion-agrandissement-moyen': {
            "short_description": "La personne qui boit cette potion voit sa taille augmenter de 50% "
                                 "pendant [5 + Mod. d’INT] tours.",
            "full_description": "La personne qui boit cette potion voit sa taille augmenter de "
                                "50% pendant [5 + Mod. d’INT] tours. Elle gagne +2 aux DM au contact et aux tests "
                                "de FOR. Pataud, elle subit un malus de -2 aux tests de DEX."
        },
        'potion-forme-gazeuse-mineur': {
            "short_description": "La personne qui boit cette potion se transforme en gaz. Elle se "
                                 "déplace au ras du sol et ne peut utiliser aucune capacité.",
            "full_description": "La personne qui boit cette potion prend la consistance d’un gaz. Elle se "
                                "déplace au ras du sol (si elle " 
                                "chute, elle le fait au ralenti) à une vitesse de 10 m par tour. elle peut "
                                "s’introduire par les plus petits interstices (comme sous une porte) mais "
                                "ne peut utiliser aucune capacité sous cette forme. Elle ne subit pas non "
                                "plus de DM, à l’exception des sorts de zone occasionnant des DM (comme "
                                "Boule de feu). Le sort a une durée de [1d4 + Mod. d’INT] tours.",
        },
        'potion-forme-gazeuse-moyen': {
            "short_description": "La personne qui boit cette potion se transforme en gaz. Elle se "
                                 "déplace au ras du sol et ne peut utiliser aucune capacité.",
            "full_description": "La personne qui boit cette potion prend la consistance d’un gaz. Elle se "
                                "déplace au ras du sol (si elle " 
                                "chute, elle le fait au ralenti) à une vitesse de 10 m par tour. elle peut "
                                "s’introduire par les plus petits interstices (comme sous une porte) mais "
                                "ne peut utiliser aucune capacité sous cette forme. Elle ne subit pas non "
                                "plus de DM, à l’exception des sorts de zone occasionnant des DM (comme "
                                "Boule de feu). Le sort a une durée de [1d4 + Mod. d’INT] tours.",
        },
        'potion-hate-mineur': {
            "short_description": "La personne qui boit cette potion voit son métabolisme s’accélérer. "
                                 "A partir du tour suivant, elle obtient une action supplémentaire par tour.",
            "full_description": "Pendant [1d6 + Mod. d’INT] tours, la personne qui boit cette potion voit "
                                "son métabolisme s’accélérer. A partir du tour suivant, elle obtient une "
                                "action supplémentaire par tour : soit une attaque normale, soit une "
                                "action de mouvement. En revanche, elle ne peut toujours "
                                "accomplir qu’une seule action limitée par tour.",
        },
        'potion-hate-moyen': {
            "short_description": "La personne qui boit cette potion voit son métabolisme s’accélérer. "
                                 "A partir du tour suivant, elle obtient une action supplémentaire par tour.",
            "full_description": "Pendant [1d6 + Mod. d’INT] tours, la personne qui boit cette potion voit "
                                "son métabolisme s’accélérer. A partir du tour suivant, elle obtient une "
                                "action supplémentaire par tour : soit une attaque normale, soit une "
                                "action de mouvement. En revanche, ellel ne peut toujours "
                                "accomplir qu’une seule action limitée par tour.",
        },
        'potion-protection-contre-les-elements-mineur': {
            "short_description": "La personne qui boit cette potion retranche 2 à tous les DM de feu, de "
                                 "froid, d’électricité ou d’acide subis un montant égal à 2 fois son "
                                 "Rang dans cette Voie.",
            "full_description": "Pendant [5 + Mod. d’INT] tours, la personne qui boit cette potion "
                                "retranche à tous les DM de feu, de froid, d’électricité ou d’acide "
                                "subis un montant égal à 2 fois son Rang dans cette Voie.",
        },
        'potion-protection-contre-les-elements-moyen': {
            "short_description": "La personne qui boit cette potion retranche 2 à tous les DM de feu, de "
                                 "froid, d’électricité ou d’acide subis un montant égal à 2 fois son "
                                 "Rang dans cette Voie.",
            "full_description": "Pendant [5 + Mod. d’INT] tours, la personne qui boit cette potion "
                                "retranche à tous les DM de feu, de froid, d’électricité ou d’acide "
                                "subis un montant égal à 2 fois son Rang dans cette Voie.",
        },
        'potion-respiration-aquatique-mineur': {
            "short_description": "La personne qui boit cette potion peut respirer sous l’eau pendant "
                                 "10 minutes.",
            "full_description": "La personne qui boit cette potion peut respirer sous l’eau pendant "
                                "10 minutes.",
        },
        'potion-respiration-aquatique-moyen': {
            "short_description": "La personne qui boit cette potion peut respirer sous l’eau pendant "
                                 "10 minutes.",
            "full_description": "La personne qui boit cette potion peut respirer sous l’eau pendant "
                                "10 minutes.",
        },   
        'potion-armure-de-mage-mineur': {
            "short_description": "La personne qui boit cette potion fait apparaître un nuage magique "
                                 "argenté qui la protège contre les attaques adverses.",
            "full_description": "La personne qui boit cette potion fait apparaître un nuage magique "
                                "argenté qui la protège contre les attaques adverses. Elle bénéficie "
                                "d’un bonus de +4 à la DEF pour le reste du combat. Si le sort est "
                                "cumulé à une armure physique, le bonus est divisé par 2 (+2 DEF).",
        },   
        'potion-armure-de-mage-moyen': {
            "short_description": "La personne qui boit cette potion fait apparaître un nuage magique "
                                 "argenté qui la protège contre les attaques adverses.",
            "full_description": "La personne qui boit cette potion fait apparaître un nuage magique "
                                "argenté qui la protège contre les attaques adverses. Elle bénéficie "
                                "d’un bonus de +4 à la DEF pour le reste du combat. Si le sort est "
                                "cumulé à une armure physique, le bonus est divisé par 2 (+2 DEF).",
        },   
        'potion-chute-ralentie-mineur': {
            "short_description": "La personne qui boit cette potion voit sa chute ralentie et ne "
                                 "subit aucun dégât jusqu'a 6m de hauteur par rang dans la voie. "
                                 "Au delà, sa chute est réduite d'autant.",
            "full_description": "La personne qui boit cette potion peut chuter de 6 mètres par "
                                "rang dans la Voie sans subir de dégâts. Si la chute est "
                                "supérieure à cette hauteur, elle est réduite d’autant.",
        },
        'potion-chute-ralentie-moyen': {
            "short_description": "La personne qui boit cette potion voit sa chute ralentie et ne "
                                 "subit aucun dégât jusqu'a 6m de hauteur par rang dans la voie. "
                                 "Au delà, sa chute est réduite d'autant.",
            "full_description": "La personne qui boit cette potion peut chuter de 6 mètres par "
                                "rang dans la Voie sans subir de dégâts. Si la chute est "
                                "supérieure à cette hauteur, elle est réduite d’autant.",
        },
        'potion-invisibilite-mineur': {
            "short_description": "La personne qui boit cette potion se rend invisible et personne "
                                 "ne peut plus détecter sa présence ou lui porter d’attaque.",
            "full_description": "La personne qui boit cette potion se rend invisible pendant "
                                "[1d6 + Mod. d’INT] minutes. Une fois invisible, personne ne peut "
                                "plus détecter sa présence ou lui porter d’attaque. Si la personne "
                                "attaque ou utilise une capacité limitée, elle redevient visible.",
        },
        'potion-invisibilite-moyen': {
            "short_description": "La personne qui boit cette potion se rend invisible et personne "
                                 "ne peut plus détecter sa présence ou lui porter d’attaque.",
            "full_description": "La personne qui boit cette potion se rend invisible pendant "
                                "[1d6 + Mod. d’INT] minutes. Une fois invisible, personne ne peut "
                                "plus détecter sa présence ou lui porter d’attaque. Si la personne "
                                "attaque ou utilise une capacité limitée, elle redevient visible.",
        },
        'potion-vol-mineur': {
            "short_description": "La personne qui boit cette potion peut voler. Sa vitesse de "
                                 "déplacement est la même qu’au sol.",
            "full_description": "La personne qui boit cette potion peut voler pendant "
                                "[1d6 + Mod. d’INT] minutes. Sa vitesse de déplacement "
                                "est la même qu’au sol.",
        },
        'potion-vol-moyen': {
            "short_description": "La personne qui boit cette potion peut voler. Sa vitesse de "
                                 "déplacement est la même qu’au sol.",
            "full_description": "La personne qui boit cette potion peut voler pendant "
                                "[1d6 + Mod. d’INT] minutes. Sa vitesse de déplacement "
                                "est la même qu’au sol.",
        },
        'potion-langage-des-animaux-mineur': {
            "short_description": "La personne qui boit cette potion peut communiquer avec les animaux " 
                                 "qui se comportent avec elle de façon amicale, en général. L'échange "
                                 "est primitif et limité à l’intelligence de l’animal.",
            "full_description": "La personne qui boit cette potion peut communiquer avec les animaux "
                                "qui, en général, se comportent avec lui de manière amicale. Il "
                                "gagne un bonus de +2 par rang à tous les tests destinés à "
                                "influencer un animal. La communication reste primitive et "
                                "limitée à l’intelligence de l’animal et à son point de vue "
                                "(prédateur, proie, etc.).",
        },
        'potion-langage-des-animaux-moyen': {
            "short_description": "La personne qui boit cette potion peut communiquer avec les animaux " 
                                 "qui se comportent avec elle de façon amicale, en général. L'échange "
                                 "est primitif et limité à l’intelligence de l’animal.",
            "full_description": "La personne qui boit cette potion peut communiquer avec les animaux "
                                "qui, en général, se comportent avec lui de manière amicale. Il "
                                "gagne un bonus de +2 par rang à tous les tests destinés à "
                                "influencer un animal. La communication reste primitive et "
                                "limitée à l’intelligence de l’animal et à son point de vue "
                                "(prédateur, proie, etc.).",
        },
        'potion-masque-du-predateur-mineur': {
            "short_description": "La personne qui boit cette potion prend les traits d’un fauve ou "
                                 "d’un loup.",
            "full_description": "La personne qui boit cette potion prend les traits d’un fauve ou "
                                "d’un loup. Il gagne son Mod. de SAG en Initiative, en attaque et "
                                "aux DM et peut voir dans la nuit (comme un elfe) pendant "
                                "[5 + Mod. de SAG] tours.",
        },
        'potion-masque-du-predateur-moyen': {
            "short_description": "La personne qui boit cette potion prend les traits d’un fauve ou "
                                 "d’un loup.",
            "full_description": "La personne qui boit cette potion prend les traits d’un fauve ou "
                                "d’un loup. Il gagne son Mod. de SAG en Initiative, en attaque et "
                                "aux DM et peut voir dans la nuit (comme un elfe) pendant "
                                "[5 + Mod. de SAG] tours.",
        },
        'potion-forme-animale-mineur': {
            "short_description": "La personne qui boit cette potion peut prendre la forme d’un "
                                 "animal de sa taille (ou plus petit). Elle conserve "
                                 "ses PV et acquiert les Carac. et les capacités naturelles de la "
                                 "forme choisie.",
            "full_description": "La personne qui boit cette potion peut prendre la forme d’un "
                                "animal d’une taille inférieure ou égale à la sienne. Elle conserve "
                                "ses PV, il acquiert les Carac. et les capacités naturelles de la "
                                "forme choisie (le vol pour un oiseau, la respiration aquatique pour "
                                "le poisson, etc.). Le Druide peut reprendre sa forme humaine lorsqu’"
                                "il le désire (L).",
        },
        'potion-forme-animale-moyen': {
            "short_description": "La personne qui boit cette potion peut prendre la forme d’un "
                                 "animal de sa taille (ou plus petit). Elle conserve "
                                 "ses PV et acquiert les Carac. et les capacités naturelles de la "
                                 "forme choisie.",
            "full_description": "La personne qui boit cette potion peut prendre la forme d’un "
                                "animal d’une taille inférieure ou égale à la sienne. Elle conserve "
                                "ses PV, il acquiert les Carac. et les capacités naturelles de la "
                                "forme choisie (le vol pour un oiseau, la respiration aquatique pour "
                                "le poisson, etc.). Le Druide peut reprendre sa forme humaine lorsqu’"
                                "il le désire (L).",
        },
        'potion-marche-sylvestre-mineur': {
            "short_description": "La personne qui boit cette potion ne subit aucune pénalité de "
                                 "déplacement en terrain difficile et obtient un bonus "
                                 "lors d’un combat dans ces conditions.",
            "full_description": "Non seulement la personne qui boit cette potion ne subit aucune "
                                "pénalité de déplacement en terrain difficile (neige, boue, "
                                "broussailles, pente abrupte, etc.) mais en plus, elle obtient "
                                "un bonus de +2 en attaque et en DEF lors d’un combat dans ces "
                                "conditions. L'effet dure 24H.",
        },
        'potion-marche-sylvestre-moyen': {
            "short_description": "La personne qui boit cette potion ne subit aucune pénalité de "
                                 "déplacement en terrain difficile et obtient un bonus "
                                 "lors d’un combat dans ces conditions.",
            "full_description": "Non seulement la personne qui boit cette potion ne subit aucune "
                                "pénalité de déplacement en terrain difficile (neige, boue, "
                                "broussailles, pente abrupte, etc.) mais en plus, elle obtient "
                                "un bonus de +2 en attaque et en DEF lors d’un combat dans ces "
                                "conditions. L'effet dure 24H.",
        },   
        'potion-forme-darbre-mineur': {
            "short_description": "Une fois par combat, la personne qui boit cette potion peut se "
                                 "transformer en arbre de petite taille. Elle conserve ses "
                                 "propres PV. Elle peut utiliser les sorts des voies du "
                                 "protecteur et des végétaux si elle les connaît.",
            "full_description": "Une fois par combat, la personne qui boit cette potion peut se "
                                "transformer en arbre de petite taille (environ 4 m de hauteur) "
                                "pendant [5 + Mod. de SAG] tours. Il prend les mêmes "
                                "Caractéristiques que l’arbre animé, mais conserve ses propres PV. "
                                "Sous cette forme, il ne peut pas parler mais peut utiliser les "
                                "sorts des voies du protecteur et des végétaux.",
        },
        'potion-forme-darbre-moyen': {
            "short_description": "Une fois par combat, la personne qui boit cette potion peut se "
                                 "transformer en arbre de petite taille. Elle conserve ses "
                                 "propres PV. Elle peut utiliser les sorts des voies du "
                                 "protecteur et des végétaux si elle les connaît.",
            "full_description": "Une fois par combat, la personne qui boit cette potion peut se "
                                "transformer en arbre de petite taille (environ 4 m de hauteur) "
                                "pendant [5 + Mod. de SAG] tours. Il prend les mêmes "
                                "Caractéristiques que l’arbre animé, mais conserve ses propres PV. "
                                "Sous cette forme, il ne peut pas parler mais peut utiliser les "
                                "sorts des voies du protecteur et des végétaux.",
        },
        'potion-peau-decorce-mineur': {
            "short_description": "La peau de la personne qui boit cette potion prend la consistance "
                                 "de l’écorce. Elle gagne alors un bonus en défense.",
            "full_description": "La peau de la personne qui boit cette potion prend la consistance "
                                "de l’écorce. Elle gagne +1 en DEF par rang dans la voie pendant "
                                "[5 + Mod. de SAG] tours.",
        },
        'potion-peau-decorce-moyen': {
            "short_description": "La peau de la personne qui boit cette potion prend la consistance "
                                 "de l’écorce. Elle gagne alors un bonus en défense.",
            "full_description": "La peau de la personne qui boit cette potion prend la consistance "
                                "de l’écorce. Elle gagne +1 en DEF par rang dans la voie pendant "
                                "[5 + Mod. de SAG] tours.",
        },
        'potion-clairvoyance-mineur': {
            "short_description": "La personne qui boit cette potion peut voir et entendre "
                                 "ce qui se passe dans un lieu qu’elle connait, tant qu’elle reste "
                                 "concentrée. Les créatures présentes peuvent se sentir observées.",
            "full_description": "La personne qui boit cette potion peut voir et entendre à distance "
                                "ce qui se passe dans un lieu qu’il connait, tant qu’elle reste "
                                "concentré (action limitée à chaque tour). Les créatures présentes "
                                "ont droit à un test de SAG difficulté [12 + Mod. de CHA] : en cas "
                                "de réussite, elles se sentent observées.",
        },   
        'potion-clairvoyance-moyen': {
            "short_description": "La personne qui boit cette potion peut voir et entendre "
                                 "ce qui se passe dans un lieu qu’elle connait, tant qu’elle reste "
                                 "concentrée. Les créatures présentes peuvent se sentir observées.",
            "full_description": "La personne qui boit cette potion peut voir et entendre à distance "
                                "ce qui se passe dans un lieu qu’il connait, tant qu’elle reste "
                                "concentré (action limitée à chaque tour). Les créatures présentes "
                                "ont droit à un test de SAG difficulté [12 + Mod. de CHA] : en cas "
                                "de réussite, elles se sentent observées.",
        },
        'potion-sous-tension-mineur': {
            "short_description": "En buvant cette potion on se charge d’énergie électrique. "
                                 "Toute créature qui vous blesse ou vous touche reçoit une décharge "
                                 "provoquant 1d6 DM.",
            "full_description": "La personne qui boit cette potion se charge d’énergie électrique pour "
                                "[5 + Mod. de CHA] tours. Toute créature qui la blesse ou la touche "
                                "reçoit une décharge infligeant 1d6 DM. Elle peut également délivrer "
                                "une décharge électrique (attaque magique, portée 10 m) infligeant "
                                "[1d6 + Mod. de CHA] DM.",
        },
        'potion-sous-tension-moyen': {
            "short_description": "En buvant cette potion on se charge d’énergie électrique. "
                                 "Toute créature qui vous blesse ou vous touche reçoit une décharge "
                                 "provoquant 1d6 DM.",
            "full_description": "La personne qui boit cette potion se charge d’énergie électrique pour "
                                "[5 + Mod. de CHA] tours. Toute créature qui la blesse ou la touche "
                                "reçoit une décharge infligeant 1d6 DM. Elle peut également délivrer "
                                "une décharge électrique (attaque magique, portée 10 m) infligeant "
                                "[1d6 + Mod. de CHA] DM.",
        },
        'potion-forme-etheree-mineur': {
            "short_description": "En buvant cette potion, La personne (et son équipement) deviennent "
                                 "translucides et intangibles. Ils peuvent passer à travers murs et "
                                 "obstacles.",
            "full_description": "La personne qui boit cette potion et tout son équipement deviennent "
                                "translucides et intangibles pendant [5 + Mod. de CHA] tours. Sous "
                                "cette forme, elle peut passer à travers murs et obstacles, et ne peut "
                                "subir aucun DM physiques.",
        },
        'potion-forme-etheree-moyen': {
            "short_description": "En buvant cette potion, La personne (et son équipement) deviennent "
                                 "translucides et intangibles. Ils peuvent passer à travers murs et "
                                 "obstacles.",
            "full_description": "La personne qui boit cette potion et tout son équipement deviennent "
                                "translucides et intangibles pendant [5 + Mod. de CHA] tours. Sous "
                                "cette forme, elle peut passer à travers murs et obstacles, et ne peut "
                                "subir aucun DM physiques.",
        },
        'potion-imitation-mineur': {
            "short_description": "La personne qui boit cette potion peut prendre l’apparence d’une "
                                 "créature de taille proche (+/- 50cm) qu’il voit au moment de "
                                 "l’incantation.",
            "full_description": "La personne qui boit cette potion peut prendre l’apparence d’une "
                                "créature de taille proche (+ ou – 50 cm) qu’il voit au moment de "
                                "boire la potion. Durée [5 + Mod. de CHA] minutes. Toucher "
                                "la personne (une attaque ou non) met fin au sort.",
        },   
        'potion-imitation-moyen': {
            "short_description": "La personne qui boit cette potion peut prendre l’apparence d’une "
                                 "créature de taille proche (+/- 50cm) qu’il voit au moment de "
                                 "l’incantation.",
            "full_description": "La personne qui boit cette potion peut prendre l’apparence d’une "
                                "créature de taille proche (+ ou – 50 cm) qu’il voit au moment de "
                                "boire la potion. Durée [5 + Mod. de CHA] minutes. Toucher "
                                "la personne (une attaque ou non) met fin au sort.",
        },   
        'potion-fortifiant-mineur': {
            "short_description": "Un breuvage étrange qui guérit et permet de gagner "
                                 "un bonus aux [rang +1] prochains tests de réussite effectués.",
            "full_description": "Un breuvage étrange qui guérit [1d4 + rang] PV et permet de gagner "
                                "un bonus de +3 aux [rang +1] prochains tests de réussite effectués "
                                "(dans une limite de temps de 12 heures).",
        },
        'potion-fortifiant-moyen': {
            "short_description": "Un breuvage étrange qui guérit et permet de gagner "
                                 "un bonus aux [rang +1] prochains tests de réussite effectués.",
            "full_description": "Un breuvage étrange qui guérit [1d4 + rang] PV et permet de gagner "
                                "un bonus de +3 aux [rang +1] prochains tests de réussite effectués "
                                "(dans une limite de temps de 12 heures).",
        },
        'potion-feu-gregeois-mineur': {
            "short_description": "La personne lance la fiole et le contenu explose "
                                 "en pojetant du feu.",
            "full_description": "La personne qui boit cette potion lance la fiole à une distance "
                                "maximum de 10 m, grâce à une action d’attaque (réussite automatique). "
                                "Le contenu explose dans un rayon de 3 m en infligeant 1d6 DM par "
                                "rang dans la voie. Un test de DEX difficulté [10 + Mod. d’INT] réussi "
                                "permet aux victimes de diviser les DM par 2.",
        },
        'potion-feu-gregeois-moyen': {
            "short_description": "La personne lance la fiole et le contenu explose "
                                 "en pojetant du feu.",
            "full_description": "La personne qui boit cette potion lance la fiole à une distance "
                                "maximum de 10 m, grâce à une action d’attaque (réussite automatique). "
                                "Le contenu explose dans un rayon de 3 m en infligeant 1d6 DM par "
                                "rang dans la voie. Un test de DEX difficulté [10 + Mod. d’INT] réussi "
                                "permet aux victimes de diviser les DM par 2.",
        },
        'potion-elixir-de-guerison-mineur': {
            "short_description": "Un élixir qui soigne [3d6 + Mod. d’INT] PV ou un empoisonnement.",
            "full_description": "Un élixir qui soigne [3d6 + Mod. d’INT] PV ou un empoisonnement.",
        },   
        'potion-elixir-de-guerison-moyen': {
            "short_description": "La personne qui boit cette potion peut préparer un élixir qui soigne "
                                 "[3d6 + Mod. d’INT] PV ou un empoisonnement.",
            "full_description": "La personne qui boit cette potion peut préparer un élixir qui soigne "
                                "[3d6 + Mod. d’INT] PV ou un empoisonnement.",
        },   
        'potion-flou-mineur': {
            "short_description": "Le corps de la personne qui boit cette potion devient flou et "
                                 "tous les DM des attaques de contact ou à distance qu’il "
                                 "encaisse sont divisés par 2.",
            "full_description": "Pendant [1d4 + Mod. d’INT] tours, le corps de la personne qui boit "
                                "cette potion devient flou et tous les DM des attaques de contact ou "
                                "à distance qu’il encaisse sont divisés par 2.",
        },
        'potion-flou-moyen': {
            "short_description": "Le corps de la personne qui boit cette potion devient flou et "
                                 "tous les DM des attaques de contact ou à distance qu’il "
                                 "encaisse sont divisés par 2.",
            "full_description": "Pendant [1d4 + Mod. d’INT] tours, le corps de la personne qui boit "
                                "cette potion devient flou et tous les DM des attaques de contact ou "
                                "à distance qu’il encaisse sont divisés par 2.",
        },
        'potion-aspect-de-la-succube-mineur': {
            "short_description": "La personne qui boit cette potion acquiert une beauté fascinante.",
            "full_description": "La personne qui boit cette potion acquiert une beauté fascinante "
                                "pour [5 + Mod. d’INT] tours. Il gagne un bonus de +5 aux tests de "
                                "CHA ainsi qu’une attaque de contact nécessitant un test d’attaque "
                                "magique et qui inflige [1d4 + Mod. de CHA] DM. Ces DM sont "
                                "transformés en PV, au bénéfice du Nécromancien (sans dépasser "
                                "son score max de PV).",
        },
        'potion-aspect-de-la-succube-moyen': {
            "short_description": "La personne qui boit cette potion acquiert une beauté fascinante.",
            "full_description": "La personne qui boit cette potion acquiert une beauté fascinante "
                                "pour [5 + Mod. d’INT] tours. Il gagne un bonus de +5 aux tests de "
                                "CHA ainsi qu’une attaque de contact nécessitant un test d’attaque "
                                "magique et qui inflige [1d4 + Mod. de CHA] DM. Ces DM sont "
                                "transformés en PV, au bénéfice du Nécromancien (sans dépasser "
                                "son score max de PV).",
        },
        'potion-aspect-du-demon-mineur': {
            "short_description": "Cette potion permet de prendre l’apparence d’un démon.",
            "full_description": "Le Nécromancien prend l’apparence d’un démon pendant [5 + Mod. d’INT] "
                                "tours. Il gagne + 2 en attaque au contact, en DEF et à tous les tests "
                                "physiques (FOR, DEX, CON). Il peut faire deux attaques de griffe à "
                                "1d6+4 DM à chaque tour, en action limitée (une seule en action "
                                "d’attaque). Ne se cumule pas avec l’Aspect de la succube.",
        }, 
        'potion-aspect-du-demon-moyen': {
            "short_description": "Cette potion permet de prendre l’apparence d’un démon.",
            "full_description": "Le Nécromancien prend l’apparence d’un démon pendant [5 + Mod. d’INT] "
                                "tours. Il gagne + 2 en attaque au contact, en DEF et à tous les tests "
                                "physiques (FOR, DEX, CON). Il peut faire deux attaques de griffe à "
                                "1d6+4 DM à chaque tour, en action limitée (une seule en action "
                                "d’attaque). Ne se cumule pas avec l’Aspect de la succube.",
        },   
        'potion-masque-mortuaire-mineur': {
            "short_description": "La personne qui boit cette potion prend l’apparence de la mort. "
                                 "Elle est immunisé aux attaques qui n’affectent que les vivants et "
                                 "à la plupart des pouvoirs des mort-vivants (de plus, ceux-ci la "
                                 "prennent pour l’un des leurs).",
            "full_description": "Pendant [5 + Mod. d’INT] tours, la personne qui boit cette potion "
                                "prend l’apparence de la mort. Elle est immunisé aux attaques qui "
                                "n’affectent que les vivants et à la plupart des pouvoirs des "
                                "mort-vivants (de plus, ceux-ci la prennent pour l’un des leurs). "
                                "Elle retranche 2 points à tous les DM physiques subits et divise "
                                "par deux tous les DM de froid.",
        },
        'potion-masque-mortuaire-moyen': {
            "short_description": "La personne qui boit cette potion prend l’apparence de la mort. "
                                 "Elle est immunisé aux attaques qui n’affectent que les vivants et "
                                 "à la plupart des pouvoirs des mort-vivants (de plus, ceux-ci la "
                                 "prennent pour l’un des leurs).",
            "full_description": "Pendant [5 + Mod. d’INT] tours, la personne qui boit cette potion "
                                "prend l’apparence de la mort. Elle est immunisé aux attaques qui "
                                "n’affectent que les vivants et à la plupart des pouvoirs des "
                                "mort-vivants (de plus, ceux-ci la prennent pour l’un des leurs). "
                                "Elle retranche 2 points à tous les DM physiques subits et divise "
                                "par deux tous les DM de froid.",
        },
        'potion-pattes-daraignee-mineur': {
            "short_description": "La personne qui boit cette potion peut se déplacer de 10 m par "
                                 "action de mouvement sur les murs et les plafonds. S’il reste "
                                 "immobile, il peut lancer des sorts.",
            "full_description": "La personne qui boit cette potion peut se déplacer de 10 m par "
                                "action de mouvement sur les murs et les plafonds pendant "
                                "[5 + Mod. d’INT] tours. S’il reste immobile, il peut "
                                "lancer des sorts.",
        },
        'potion-pattes-daraignee-moyen': {
            "short_description": "La personne qui boit cette potion peut se déplacer de 10 m par "
                                 "action de mouvement sur les murs et les plafonds. S’il reste "
                                 "immobile, il peut lancer des sorts.",
            "full_description": "La personne qui boit cette potion peut se déplacer de 10 m par "
                                "action de mouvement sur les murs et les plafonds pendant "
                                "[5 + Mod. d’INT] tours. S’il reste immobile, il peut "
                                "lancer des sorts.",
        },
        'potion-ailes-celestes-mineur': {
            "short_description": "Des ailes divines poussent dans le dos de la personne qui boit "
                                 "cette potion, qui peut voler à une vitesse équivalente à deux "
                                 "fois son déplacement normal.",
            "full_description": "Des ailes divines poussent dans le dos de la personne qui boit "
                                 "cette potion, qui peut voler à une vitesse équivalente à deux "
                                 "fois son déplacement normal pendant [5 + Mod. de SAG] tours. "
                                 "Rester en vol stationnaire avec les ailes céleste est une "
                                 "action de mouvement.",
        },   
        'potion-ailes-celestes-moyen': {
            "short_description": "Des ailes divines poussent dans le dos de la personne qui boit "
                                 "cette potion, qui peut voler à une vitesse équivalente à deux "
                                 "fois son déplacement normal.",
            "full_description": "Des ailes divines poussent dans le dos de la personne qui boit "
                                 "cette potion, qui peut voler à une vitesse équivalente à deux "
                                 "fois son déplacement normal pendant [5 + Mod. de SAG] tours. "
                                 "Rester en vol stationnaire avec les ailes céleste est une "
                                 "action de mouvement.",
        },   
        'potion-sanctuaire-mineur': {
            "short_description": "Quand la personne boit cette potion, tous les adversaires qui "
                                 "veulent l’attaquer doivent d’abord réussir un test de SAG "
                                 "difficulté 15.",
            "full_description": "Quand la personne boit cette potion, tous les adversaires qui "
                                "veulent l’attaquer doivent d’abord réussir un test de SAG "
                                "difficulté 15. S’ils échouent, ils ne peuvent pas l’attaquer. "
                                "Les effets de ce sort durent [5 + Mod de SAG] tours, mais s’il "
                                "tente la moindre attaque, le sort prend fin immédiatement.",
        },
         'potion-sanctuaire-moyen': {
            "short_description": "Quand la personne boit cette potion, tous les adversaires qui "
                                 "veulent l’attaquer doivent d’abord réussir un test de SAG "
                                 "difficulté 15.",
            "full_description": "Quand la personne boit cette potion, tous les adversaires qui "
                                "veulent l’attaquer doivent d’abord réussir un test de SAG "
                                "difficulté 15. S’ils échouent, ils ne peuvent pas l’attaquer. "
                                "Les effets de ce sort durent [5 + Mod de SAG] tours, mais s’il "
                                "tente la moindre attaque, le sort prend fin immédiatement.",
        }
    }
}
