# -*- coding: utf-8 -*-

from cof.properties import *
from cof.utils import string_to_id, get_def_level
from config.cofConfig import config as ccc
from ClusterShell.NodeSet import RangeSet

uniques = {
    'Material': {
        'broche-sagesse+2': {
            'name': "Broche en argent",
            'short_description': "Un magnifique broche en argent représentant une feuille de houx.",
            'full_description': "Un magnifique broche en argent représentant une feuille de houx. Cette broche "
                                "confère un bonus au Mod. de SAG de +2.",
            'category': "quest",
            'special_property': [
                "Mod. SAG: +2",
            ],
            'weight': Weight(value=0.1, unit='Kg'),
            'cost': lambda item: Cost(
                value=18000,
                unit=ccc['global']['cost']['unit']).iso(),
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
        },
        'etoile-d-honneur-en-argent': {
            'name': "Étoile d'honneur, en argent",
            'base_item': lambda item: item.oid,
            'short_description': "L’étoile d'honneur en argent est une décoration qui symbolise le patriotisme de "
                                 "son porteur. Elle comporte des motifs complexes très difficile à reproduire et "
                                 "produit une lumière bleutée lorsque les mots « Pour la gloire d’Arly » sont "
                                 "prononcés en la tenant dans la main.",
            'full_description': "L’étoile d'honneur en argent est une décoration qui symbolise le patriotisme de "
                                "son porteur. Elle accorde un bonus de +2 à tous les tests de CHA face aux "
                                "représentants de l’autorité dans la Principauté d’Arly et +1 avec les citoyens "
                                "ordinaires. Elle comporte des entrelacs complexes qui la rendent très difficile "
                                "à reproduire et un enchantement spécial qui produit une lumière bleutée (couleur "
                                "de la Principauté) lorsque les mots « Pour la gloire d’Arly » sont prononcés en "
                                "la tenant dans la main.",
            'category': "quest",
            'special_property': ["Test (CHA): +2 contre représentant de l'autorité d'Arly ou citoyen ordinaire"],
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le sanctuaire", chapter="Le problème de Twemby", numbering="1")
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'croquis-grossier-homme-gant': {
            'name': "Croquis grossier, du shaman orque",
            'base_item': lambda item: item.oid,
            'short_description': "un croquis grossier, il représente un elfe dont l’une des mains est énorme et "
                                 "émet des rayons ardents.",
            'full_description': "un croquis grossier, il représente un elfe dont l’une des mains est énorme et "
                                "émet des rayons ardents.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Fort Boueux", chapter="La bataille de vireux", numbering="3"
                ),
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'chocolat-elbion': {
            'name': "Chocolat, d'Elbion",
            'base_item': lambda item: item.oid,
            'short_description': "Le chocolat d'Elbion est un met inconnu, mais savoureux. Il accorde un bonus de +2 "
                                 "sur un test au choix du joueur dans un délai de 10 minutes après que le personnage "
                                 "l'ai dégusté.",
            'full_description': "Le chocolat d'Elbion est un met inconnu, mais savoureux. Il accorde un bonus de +2 "
                                "sur un test au choix du joueur dans un délai de 10 minutes après que le personnage "
                                "l'ai dégusté.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Scénarios uniques", title="Retour à clairval", chapter="Une nuit à Clairval", numbering="2")
            ],
            'skill': [Mod(label="Test", count=2, mtype="+")],
            'cost': Cost(value=2.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'costume-sur-mesure-de-albik': {
            'name': "Costume sur mesure, d'Albik",
            'base_item': lambda item: item.oid,
            'short_description': "Un magnifique costume taillé sur mesure par Albik de Clairval.",
            'full_description': "Un magnifique costume taillé sur mesure par Albik de Clairval.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Scénarios uniques", title="Retour à clairval", chapter="Amis pour la vie", numbering="5")
            ],
            'cost': Cost(value=5.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'planche-de-chene': {
            'name': "Planche de chêne",
            'base_item': lambda item: item.oid,
            'short_description': "Une planche bien solide en chêne.",
            'full_description': "Une planche bien solide en chêne.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Fort Boueux", chapter="Voyage dans la boue", numbering="1")
            ],
            'cost': Cost(value=1.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1, unit='Kg'),
            'quantity': 1
        },
        'roue-de-chariot': {
            'name': "Roue de chariot",
            'base_item': lambda item: item.oid,
            'short_description': "Une roue de chariot, bien utile en cas de panne.",
            'full_description': "Une roue de chariot, bien utile en cas de panne.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Fort Boueux", chapter="Voyage dans la boue", numbering="1")
            ],
            'cost': Cost(value=2.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=10, unit='Kg'),
            'quantity': 1
        },
        'scie-a-bois': {
            'name': "Scie a bois",
            'base_item': lambda item: item.oid,
            'short_description': "Une scie à bois manuelle qui viendra à bout de n'importe qu'elle planche "
                                 "moyennant un peu d'huile de coude.",
            'full_description': "Une scie à bois manuelle qui viendra à bout de n'importe qu'elle planche "
                                 "moyennant un peu d'huile de coude.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Fort Boueux", chapter="Voyage dans la boue", numbering="1")
            ],
            'cost': Cost(value=2.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'torque-de-andra-mortemine': {
            'name': "Torque, d'Andra Mortemine",
            'base_item': lambda item: item.oid,
            'short_description': "Un torque en argent gravé d'un motif de poisson.",
            'full_description': "Un torque en argent gravé d'un motif de poisson.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Fort Boueux", chapter="Voyage dans la boue", numbering="1")
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'torque-de-julius-mortemine': {
            'name': "Torque, de Julius Mortemine",
            'base_item': lambda item: item.oid,
            'short_description': "Un torque en argent gravé d'un motif de poisson.",
            'full_description': "Un torque en argent gravé d'un motif de poisson.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le problème de Twemby", numbering="1")
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'stone-morceaux-quartz': {
            'name': "Morceaux de quartz",
            'base_item': lambda item: item.oid,
            'short_description': "Quelques jolis morceaux de quartz. Ces morceaux sont sans grande valeur, sauf "
                                 "pour un collectionneur.",
            'full_description': "Quelques jolis morceaux de quartz. Ces morceaux sont sans grande valeur, sauf "
                                 "pour un collectionneur.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Scénarios uniques", title="Retour à clairval", chapter="Baston chez les Crânes-creux", numbering="4")
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 5
        },
        'stone-ambre': {
            'name': "Ambre",
            'base_item': lambda item: item.oid,
            'short_description': "L'ambre est une résine végétale sécrétée par des conifères il y a des millions "
                                 "d'années et qui s'est fossilisée.",
            'full_description': "L'ambre est une résine végétale sécrétée par des conifères il y a des millions "
                                "d'années et qui s'est fossilisée.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le problème de Twemby", numbering="1"),
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-emeraude': {
            'name': "Émeraude",
            'base_item': lambda item: item.oid,
            'short_description': "L’émeraude est un minéral, dont la couleur verte provient de traces de chrome, "
                                 "de vanadium et parfois de fer. L'émeraude est, avec le diamant, le saphir et le "
                                 "rubis, l'une des quatre pierres précieuses.",
            'full_description': "L’émeraude est un minéral, dont la couleur verte provient de traces de chrome, "
                                 "de vanadium et parfois de fer. L'émeraude est, avec le diamant, le saphir et le "
                                 "rubis, l'une des quatre pierres précieuses.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                ),
            ],
            'cost': Cost(value=150.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-amethyste': {
            'name': "Améthyste",
            'base_item': lambda item: item.oid,
            'short_description': "L'améthyste est une variété de quartz violet dont la teinte est due aux traces "
                                 "de fer. Ce minéral est utilisé en joaillerie et classé comme pierre fine.",
            'full_description': "L'améthyste est une variété de quartz violet dont la teinte est due aux traces "
                                "de fer. Ce minéral est utilisé en joaillerie et classé comme pierre fine.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                ),
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-rubis': {
            'name': "Rubis",
            'base_item': lambda item: item.oid,
            'short_description': "Le rubis est la variété rouge de la famille minérale du corindon. Sa couleur est "
                                 "causée principalement par la présence d'atomes de chrome. Le rubis est une pierre "
                                 "gemme presqu'aussi dure que le diamant.",
            'full_description': "Le rubis est la variété rouge de la famille minérale du corindon. Sa couleur est "
                                "causée principalement par la présence d'atomes de chrome. Le rubis est une pierre "
                                "gemme presqu'aussi dure que le diamant.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Voyage", numbering="2"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-diamant': {
            'name': "Diamant",
            'base_item': lambda item: item.oid,
            'short_description': "Le diamant est un minéral transparent composé de cristaux de carbone pur. Cette "
                                 "pierre précieuse est connue pour être le minéral le plus dur qui soit.",
            'full_description': "Le diamant est un minéral transparent composé de cristaux de carbone pur. Cette "
                                 "pierre précieuse est connue pour être le minéral le plus dur qui soit.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'cost': Cost(value=5000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-alexandrite': {
            'name': "Alexandrite",
            'base_item': lambda item: item.oid,
            'short_description': "L'alexandrite est d'éclat vitreux. Sa couleur change avec l'éclairage : bleu-vert "
                                 "à la lumière du jour, rose-rouge au feu de bois.",
            'full_description': "L'alexandrite est d'éclat vitreux. Sa couleur change avec l'éclairage : bleu-vert "
                                "à la lumière du jour, rose-rouge au feu de bois.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-alexandrite': {
            'name': "Alexandrite rare",
            'base_item': "stone-alexandrite",
            'short_description': "L'alexandrite est d'éclat vitreux. Sa couleur change avec l'éclairage : bleu-vert "
                                 "à la lumière du jour, rose-rouge au feu de bois.",
            'full_description': "L'alexandrite est d'éclat vitreux. Sa couleur change avec l'éclairage : bleu-vert "
                                "à la lumière du jour, rose-rouge au feu de bois.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-agate': {
            'name': "Agate",
            'base_item': lambda item: item.oid,
            'short_description': "L’agate se caractérise par des successions de couleurs ou de tons "
                                 "différents, c'est une pierre fine.",
            'full_description': "L’agate se caractérise par des successions de couleurs ou de tons "
                                 "différents, c'est une pierre fine.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-jaspe': {
            'name': "Jaspe",
            'base_item': lambda item: item.oid,
            'short_description': "Le jaspe peut avoir plusieurs aspects : tacheté, rubané, rouge, à taches rouges "
                                 "sur fond vert, noir, etc.",
            'full_description': "Le jaspe peut avoir plusieurs aspects : tacheté, rubané, rouge, à taches rouges "
                                "sur fond vert, noir, etc.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La Vallée des Songes",
                    chapter="La Vallée des Songes", numbering="2"
                ),
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
         'stone-jade': {
            'name': "Jade",
            'base_item': lambda item: item.oid,
            'short_description': "Le jade est une pierre gemme très dure et tenace généralement de couleur verte.",
            'full_description': "Le jade est une pierre gemme très dure et tenace généralement de couleur verte.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-petit-jaspe': {
            'name': "Petit jaspe",
            'base_item': 'stone-jaspe',
            'short_description': "Le jaspe peut avoir plusieurs aspects : tacheté, rubané, rouge, à taches rouges "
                                 "sur fond vert, noir, etc.",
            'full_description': "Le jaspe peut avoir plusieurs aspects : tacheté, rubané, rouge, à taches rouges "
                                "sur fond vert, noir, etc.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-perle': {
            'name': "Perle",
            'base_item': lambda item: item.oid,
            'short_description': "Une perle est une concrétion calcaire, généralement de couleur blanche, "
                                 "fabriquée par certains mollusques. Quand un objet irritant passe à l'intérieur "
                                 "de la coquille, l'animal réagit en entourant l'objet d'une couche de nacre.",
            'full_description': "Une perle est une concrétion calcaire, généralement de couleur blanche, "
                                 "fabriquée par certains mollusques. Quand un objet irritant passe à l'intérieur "
                                 "de la coquille, l'animal réagit en entourant l'objet d'une couche de nacre.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1"),
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-perle-rare': {
            'name': "Perle rare",
            'base_item': lambda item: item.oid,
            'short_description': "Une perle est une concrétion calcaire, généralement de couleur blanche, "
                                 "fabriquée par certains mollusques. Quand un objet irritant passe à l'intérieur "
                                 "de la coquille, l'animal réagit en entourant l'objet d'une couche de nacre.",
            'full_description': "Une perle est une concrétion calcaire, généralement de couleur blanche, "
                                 "fabriquée par certains mollusques. Quand un objet irritant passe à l'intérieur "
                                 "de la coquille, l'animal réagit en entourant l'objet d'une couche de nacre.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-petite-perle': {
            'name': "Petite perle",
            'base_item': lambda item: item.oid,
            'short_description': "Une perle est une concrétion calcaire, généralement de couleur blanche, "
                                 "fabriquée par certains mollusques. Quand un objet irritant passe à l'intérieur "
                                 "de la coquille, l'animal réagit en entourant l'objet d'une couche de nacre.",
            'full_description': "Une perle est une concrétion calcaire, généralement de couleur blanche, "
                                 "fabriquée par certains mollusques. Quand un objet irritant passe à l'intérieur "
                                 "de la coquille, l'animal réagit en entourant l'objet d'une couche de nacre.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-topaze-orientale': {
            'name': "Topaze orientale",
            'base_item': lambda item: item.oid,
            'short_description': "La topaze est une espèce minérale pouvant contenir des traces de fer, "
                                 "chrome, magnésium et titane.",
            'full_description': "La topaze est une espèce minérale pouvant contenir des traces de fer, "
                                 "chrome, magnésium et titane.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La Vallée des Songes",
                    chapter="La Vallée des Songes", numbering="2"
                )
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-carnelian': {
            'name': "Carnélian",
            'base_item': lambda item: item.oid,
            'short_description': "La carnélian est une variété de calcédoines rouges. Elle est principalement "
                                 "utilisée pour l'orfêvrerie.",
            'full_description': "La carnélian est une variété de calcédoines rouges. Elle est principalement "
                                 "utilisée pour l'orfêvrerie.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La Vallée des Songes",
                    chapter="La Vallée des Songes", numbering="2"
                )
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-hematite': {
            'name': "Hématite",
            'base_item': lambda item: item.oid,
            'short_description': "L’Hématite est une pierre fine sombre et complétement opaque aux reflets "
                                 "argentés. Sa couleur se rapproche du gris acier. Certains spécimens ont "
                                 "une couleur presque noire.",
            'full_description': "L’Hématite est une pierre fine sombre et complétement opaque aux reflets "
                                "argentés. Sa couleur se rapproche du gris acier. Certains spécimens ont "
                                "une couleur presque noire.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La Vallée des Songes",
                    chapter="La Vallée des Songes", numbering="2"
                )
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-citrine': {
            'name': "Citrine",
            'base_item': lambda item: item.oid,
            'short_description': "La citrine est une variété de quartz, dont la couleur jaune est due à la "
                                 "présence d'infimes quantités d'oxydes de fer dans le minéral.",
            'full_description': "La citrine est une variété de quartz, dont la couleur jaune est due à la "
                                "présence d'infimes quantités d'oxydes de fer dans le minéral.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-aigue-marine': {
            'name': "Aigue marine",
            'base_item': lambda item: item.oid,
            'short_description': "L'aigue-marine est une pierre transparente, de couleur bleu clair évoquant "
                                 "l'eau de mer, d'apparence proche de la topaze.",
            'full_description': "L'aigue-marine est une pierre transparente, de couleur bleu clair évoquant "
                                "l'eau de mer, d'apparence proche de la topaze.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-opale': {
            'name': "Opale",
            'base_item': lambda item: item.oid,
            'short_description': "L'opale est une pierre fine très spéciale et, contrairement aux autres minéraux, "
                                 "ses cristaux n'ont pas de forme particulière.",
            'full_description': "L'opale est une pierre fine très spéciale et, contrairement aux autres minéraux, "
                                "ses cristaux n'ont pas de forme particulière.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=2000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-petite-opale': {
            'name': "Petite opale",
            'base_item': "stone-opale",
            'short_description': "L'opale est une pierre fine très spéciale et, contrairement aux autres minéraux, "
                                 "ses cristaux n'ont pas de forme particulière.",
            'full_description': "L'opale est une pierre fine très spéciale et, contrairement aux autres minéraux, "
                                "ses cristaux n'ont pas de forme particulière.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=1000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-chrysoprase': {
            'name': "Chrysoprase",
            'base_item': lambda item: item.oid,
            'short_description': "La chrysoprase est une variété gemme dont la couleur varie du vert pomme au vert "
                                 "foncé.",
            'full_description': "La chrysoprase est une variété gemme dont la couleur varie du vert pomme au vert "
                                "foncé.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-peridot': {
            'name': "Péridot",
            'base_item': lambda item: item.oid,
            'short_description': "Le péridot est une variété gemme de couleur verte qui est considérée comme ayant "
                                 "un pouvoir magique.",
            'full_description': "Le péridot est une variété gemme de couleur verte qui est considérée comme ayant "
                                "un pouvoir magique.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-spinelle': {
            'name': "Spinelle",
            'base_item': lambda item: item.oid,
            'short_description': "Le spinelle est une espèce minérale de couleur rouge. C'est une pierre fine utilisée "
                                 "en joaillerie car elle ressemble au rubis.",
            'full_description': "Le spinelle est une espèce minérale de couleur rouge. C'est une pierre fine utilisée "
                                "en joaillerie car elle ressemble au rubis.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-chrysoberyl': {
            'name': "Chrysobéryl",
            'base_item': lambda item: item.oid,
            'short_description': "Le chrysobéryl est une espèce minérale peut être de différentes couleurs qui sont "
                                 "dues à de petites quantités de fer pour le jaune ou le vert pour la variété connue "
                                 "sous le nom d'alexandrite, qui est verte à la lumière du jour et rouge à la lumière "
                                 "artificielle.",
            'full_description': "Le chrysobéryl est une espèce minérale peut être de différentes couleurs qui sont "
                                "dues à de petites quantités de fer pour le jaune ou le vert pour la variété connue "
                                "sous le nom d'alexandrite, qui est verte à la lumière du jour et rouge à la lumière "
                                "artificielle.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-onyx': {
            'name': "Onyx",
            'base_item': lambda item: item.oid,
            'short_description': "L’onyx est une agate dont les bandes sont circulaires et concentriques.",
            'full_description': "L’onyx est une agate dont les bandes sont circulaires et concentriques.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-topaze': {
            'name': "Topaze",
            'base_item': lambda item: item.oid,
            'short_description': "La topaze est un cristal utilisé en joaillerie, classée comme pierre fine. "
                                 "La topaze se présente en une large variété de couleurs à l'état naturel.",
            'full_description': "La topaze est un cristal utilisé en joaillerie, classée comme pierre fine. "
                                "La topaze se présente en une large variété de couleurs à l'état naturel.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-opale-de-feu': {
            'name': "Opale de feu",
            'base_item': lambda item: item.oid,
            'short_description': "l'opale de feu est une opale, transparente, jaune orange ou rouge, avec ou "
                                 "sans jeux de couleurs.",
            'full_description': "l'opale de feu est une opale, transparente, jaune orange ou rouge, avec ou "
                                 "sans jeux de couleurs.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=1000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-grenat': {
            'name': "Grenat",
            'base_item': lambda item: item.oid,
            'short_description': "Les grenats rassemblent plusieurs minéraux proches et forment un groupe "
                                 "dans lequel on retrouve des gemmes de toutes les couleurs. Les grenats "
                                 "rouges sont les plus célèbres, mais il existe également des grenats verts, "
                                 "oranges, violets et même des grenats bleus.",
            'full_description': "Les grenats rassemblent plusieurs minéraux proches et forment un groupe "
                                "dans lequel on retrouve des gemmes de toutes les couleurs. Les grenats "
                                "rouges sont les plus célèbres, mais il existe également des grenats verts, "
                                "oranges, violets et même des grenats bleus.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-pierre-de-sang': {
            'name': "Pierre de sang",
            'base_item': lambda item: item.oid,
            'short_description': "Une pierre qui donne des éclats de couleur de sang lorsqu’elle est "
                                 "disposée dans un vase rempli d’eau sous la lumière du soleil.",
            'full_description': "Une pierre qui donne des éclats de couleur de sang lorsqu’elle est "
                                 "disposée dans un vase rempli d’eau sous la lumière du soleil.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-saphir': {
            'name': "Saphir",
            'base_item': lambda item: item.oid,
            'short_description': "Le saphir est une pierre précieuse. C'est une variété gemme pouvant "
                                 "présenter de multiples couleurs, sauf la couleur rouge qui désigne "
                                 "alors uniquement le rubis.",
            'full_description': "Le saphir est une pierre précieuse. C'est une variété gemme pouvant "
                                "présenter de multiples couleurs, sauf la couleur rouge qui désigne "
                                "alors uniquement le rubis.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=1000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'stone-quartz': {
            'name': "Quartz",
            'base_item': lambda item: item.oid,
            'short_description': "Le quartz rose se présente en grands cristaux à la fois roses et translucides.",
            'full_description': "Le quartz rose se présente en grands cristaux à la fois roses et translucides.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 5
        },
        'stone-quartz-rose': {
            'name': "Quartz rose",
            'base_item': lambda item: item.oid,
            'short_description': "Le quartz se présente sous la forme ou bien de grands cristaux incolores, "
                                 "colorés ou fumés, ou bien de cristaux microscopiques d'aspect translucide.",
            'full_description': "Le quartz se présente sous la forme ou bien de grands cristaux incolores, "
                                 "colorés ou fumés, ou bien de cristaux microscopiques d'aspect translucide.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 5
        },
        'stone-perle-noire': {
            'name': "Perle noire",
            'base_item': lambda item: item.oid,
            'short_description': "Une perle est une concrétion calcaire, généralement de couleur blanche, "
                                 "fabriquée par certains mollusques. Quand un objet irritant passe à l'intérieur "
                                 "de la coquille, l'animal réagit en entourant l'objet d'une couche de nacre. "
                                 "La perle noire est considérée comme un véritable symbole de sagesse.",
            'full_description': "Une perle est une concrétion calcaire, généralement de couleur blanche, "
                                 "fabriquée par certains mollusques. Quand un objet irritant passe à l'intérieur "
                                 "de la coquille, l'animal réagit en entourant l'objet d'une couche de nacre. "
                                 "La perle noire est considérée comme un véritable symbole de sagesse.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=5000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'quantity': 1
        },
        'pierre-de-mort': {
            'name': "Pierre de Mort",
            'base_item': lambda item: item.oid,
            'short_description': "Une pierre magique qui semble posséder une puissante aura de mort.",
            'full_description': "Une pierre magique qui semble posséder une puissante aura de mort",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'pierre-du-feu': {
            'name': "Pierre du Feu",
            'base_item': lambda item: item.oid,
            'short_description': "Une pierre magique qui semble irradier d'une puissante chaleur.",
            'full_description': "Une pierre magique qui semble irradier d'une puissante chaleur.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'pierre-de-terre': {
            'name': "Pierre de Terre",
            'base_item': lambda item: item.oid,
            'short_description': "Une pierre magique d'où semble s'émananer de fines volutes empoisonnées.",
            'full_description': "Une pierre magique d'où semble s'émananer de fines volutes empoisonnées.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'pierre-d-esprit': {
            'name': "Pierre d'Esprit",
            'base_item': lambda item: item.oid,
            'short_description': "Une pierre magique fascinante dont il est difficile de détourner le regard.",
            'full_description': "Une pierre magique fascinante dont il est difficile de détourner le regard.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'pierre-de-vent': {
            'name': "Pierre de Vent",
            'base_item': lambda item: item.oid,
            'short_description': "Une pierre magique empreinte de tellement de puissance qu'elle semble vibrer.",
            'full_description': "Une pierre magique empreinte de tellement de puissance qu'elle semble vibrer.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'flute-d-amarange': {
            'name': "Flûte, d'Amarange",
            'base_item': lambda item: item.oid,
            'short_description': "Une jolie flûte richement décorée.",
            'full_description': "Une jolie flûte richement décorée.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'flute-de-pan-en-ivoire': {
            'name': "Flûte de pan, en ivoire",
            'base_item': lambda item: item.oid,
            'short_description': "Une jolie flûte de pan en ivoire plaquée de nacre.",
            'full_description': "Une jolie flûte de pan en ivoire plaquée de nacre.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=200.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'peigne-a-cheveux-en-argent': {
            'name': "Peigne à cheveux, en argent",
            'base_item': lambda item: item.oid,
            'short_description': "Un très beau peigne à cheveux en argent.",
            'full_description': "Un très beau peigne à cheveux en argent.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=25.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 5
        },
        'bouteille-en-cristal-avec-verre': {
            'name': "Bouteille et verres, en cristal",
            'base_item': lambda item: item.oid,
            'short_description': "Une bouteille en cristal avec 6 verres assortis.",
            'full_description': "Une bouteille en cristal avec 6 verres assortis.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=800.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.4, unit='Kg'),
        },
        'grimoire-ancien-pantheon-des-dieux': {
            'name': "Grimoire ancien",
            'base_item': lambda item: item.oid,
            'short_description': "Un grimoire ancien présentant le panthéon des dieux en assez mauvais état.",
            'full_description': "Un grimoire ancien présentant le panthéon des dieux en assez mauvais état.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'paire-de-lorgnons': {
            'name': "Paire de lorgnons",
            'base_item': lambda item: item.oid,
            'short_description': "Une paire de lorgnons.",
            'full_description': "Une paire de lorgnons.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'ancien-tableau-aigle': {
            'name': "Tableau ancien",
            'base_item': lambda item: item.oid,
            'short_description': "Il s’agit d’un ancien tableau représentant un aigle.",
            'full_description': "Il s’agit d’un ancien tableau représentant un aigle.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=100.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'luth-d-amarange': {
            'name': "Luth, d'Amarange",
            'base_item': lambda item: item.oid,
            'short_description': "Un luth de très bonne qualité.",
            'full_description': "Un luth de très bonne qualité.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
        },
        'cassette-de-500-pieces-d-argent': {
            'name': "Cassette de pièces, d'argent",
            'base_item': lambda item: item.oid,
            'short_description': "Une cassette contenant 500 pièces d'argent.",
            'full_description': "Une cassette contenant 500 pièces d'argent.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Voyage", numbering="2"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=3.5, unit='Kg'),
            'quantity': 1,
        },
        'cassette-de-450-pieces-d-argent': {
            'name': "Cassette de pièces, d'argent",
            'base_item': lambda item: item.oid,
            'short_description': "Une cassette contenant 450 pièces d'argent.",
            'full_description': "Une cassette contenant 450 pièces d'argent.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=450.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=3.0, unit='Kg'),
            'quantity': 1,
        },
        'cassette-de-50-pieces-d-or': {
            'name': "Cassette de pièces, d'or",
            'base_item': lambda item: item.oid,
            'short_description': "Une cassette contenant 50 pièces d'or.",
            'full_description': "Une cassette contenant 50 pièces d'or.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
            'quantity': 1,
        },
        'cassette-de-275-pieces-d-argent': {
            'name': "Cassette de pièces, d'argent",
            'base_item': lambda item: item.oid,
            'short_description': "Une cassette contenant 275 pièces d'argent.",
            'full_description': "Une cassette contenant 275 pièces d'argent.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Voyage", numbering="2"
                ),
            ],
            'cost': Cost(value=275.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=2, unit='Kg'),
            'quantity': 1,
        },
        'cassette-de-75-pieces-d-argent': {
            'name': "Cassette de pièces, d'argent",
            'base_item': lambda item: item.oid,
            'short_description': "Une cassette contenant 75 pièces d'argent.",
            'full_description': "Une cassette contenant 75 pièces d'argent.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Voyage", numbering="2"
                ),
            ],
            'cost': Cost(value=75.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.5, unit='Kg'),
            'quantity': 1,
        },
        'cassette-de-81-pieces-d-argent': {
            'name': "Cassette de pièces, d'argent",
            'base_item': lambda item: item.oid,
            'short_description': "Une cassette contenant 81 pièces d'argent.",
            'full_description': "Une cassette contenant 81 pièces d'argent.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Voyage", numbering="2"
                ),
            ],
            'cost': Cost(value=81.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.5, unit='Kg'),
            'quantity': 1,
        },
        'tonnelet-de-vin': {
            'name': "Un tonnelet de vin",
            'base_item': lambda item: item.oid,
            'short_description': "Un tonnelet de bon vin des Marches du Piémont.",
            'full_description': "Un tonnelet de bon vin des Marches du Piémont.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Voyage", numbering="2"
                ),
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=5, unit='Kg'),
        },
        'sac-de-pommes': {
            'name': "Un grand sac de pommes",
            'base_item': lambda item: item.oid,
            'short_description': "Un un grand sac rempli de pommes.",
            'full_description': "Un un grand sac rempli de pommes qui ont l'air très appétissantes.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Forêt Sombre", numbering="1"
                ),
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=10, unit='Kg'),
        },
        'bourse-fruits-seches': {
            'name': "Une bourse contenant des fruits séchés",
            'base_item': lambda item: item.oid,
            'short_description': "Une bourse avec des baies pour prendre 5 repas. "
                                 "Un repas nourrit la personne pour 24 heures, guerit les blessures et "
                                 "soigne tout empoisonnement.",
            'full_description': "Une bourse de fruits séchés aux propriétés magiques. Chaque bourse contient "
                                "une quantité suffisante de baies pour prendre 5 repas. Chaque repas nourrit "
                                "la personne pour 24 heures, permet de guérir 3d6 PV et soigne tout "
                                "empoisonnement. Un personnage ne peut bénéficier de cet effet plus d’une fois "
                                "par jour.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Forêt Sombre", numbering="1"
                ),
            ],
            'special_property': [
                "Soigne: 3d6 PV",
                "Soigne: Empoisonnement",
                "Effet: 1 seule fois par jour"
            ],
            'cost': Cost(value=200.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.5, unit='Kg'),
            'quantity': 1,
            'use': 5
            
        },
        'vetements-sombres': {
            'name': "Vêtements sombres",
            'base_item': lambda item: item.oid,
            'short_description': "Des vêtements sombres qui vous permettrons de vous fondre dans les ombres une fois "
                                 "la nuit tombée.",
            'full_description': "Des vêtements sombres qui vous permettrons de vous fondre dans les ombres une fois "
                                 "la nuit tombée.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Voyage", numbering="2"
                ),
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'cost': Cost(value=2.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.2, unit='Kg'),
        },
        'Autorisation-port-arme-capitaine-angus': {
            'name': "Autorisation, du Capitaine Angus",
            'base_item': lambda item: item.oid,
            'short_description': "Cette autorisation du Capitaine Angus contient le message suivant : "
                                 "« Le porteur de cette autorisation ainsi que tous ses compagnons sont "
                                 "autorisés à pouvoir porter des armes en ville de 17h00 à 6h00 et de procéder à "
                                 "une enquête approfondie chez le sieur Emarin Grisant dont on craint la "
                                 "disparition ».",
            'full_description': "Cette autorisation du Capitaine Angus contient le message suivant : "
                                "« Le porteur de cette autorisation ainsi que tous ses compagnons sont "
                                "autorisés à pouvoir porter des armes en ville de 17h00 à 6h00 et de procéder à "
                                "une enquête approfondie chez le sieur Emarin Grisant dont on craint la "
                                "disparition ».",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'recette-tarte-aux-pommes-emarin-grisant': {
            'name': "Tarte aux pommes, d'Emarin Grisant",
            'base_item': lambda item: item.oid,
            'short_description': "Recette de la tarte aux pommes: Faites la pâte avec du beurre, de la farine et "
                                 "de l'eau. Malaxez puis faites-en une boule que vous laisserez reposer au moins "
                                 "une heure. Pendant ce temps épluchez des pommes et coupez les en morceaux. Lorsque "
                                 "la pâte est prête, étalez la dans un moule et disposez les morceaux de pommes "
                                 "dessus. Faites cuire 35 min puis dégustez la tiède !",
            'full_description': "Recette de la tarte aux pommes: Faites la pâte avec du beurre, de la farine et "
                                 "de l'eau. Malaxez puis faites-en une boule que vous laisserez reposer au moins "
                                 "une heure. Pendant ce temps épluchez des pommes et coupez les en morceaux. Lorsque "
                                 "la pâte est prête, étalez la dans un moule et disposez les morceaux de pommes "
                                 "dessus. Faites cuire 35 min puis dégustez la tiède !",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'recette-amphore-de-soin': {
            'name': "Recette amphore de soin",
            'base_item': lambda item: item.oid,
            'short_description': "Sur cette plaquette de cire est gravée (en Uraqi) la methode utilisé par les Uraqi "
                                 "pour produire une amphore de soin. L'ingrédient principal semble être ... du sang humain ...",
            'full_description': "Sur cette plaquette de cire est gravée (en Uraqi) la methode utilisé par les Uraqi "
                                "pour produire une amphore de soin. L'ingrédient principal semble être ... du sang humain ...",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'lettre-secrete-d-emarin-grisant': {
            'name': "Lettre secrète, d'Emarin Grisant",
            'base_item': lambda item: item.oid,
            'short_description': "« Cher collègue, je suis actuellement prisonnier au Pic d’Andalf. Aidez-moi et "
                                 "vous serez récompensé pour votre peine. Attention ! Mes ravisseurs sont doués "
                                 "de pouvoirs magiques. Libérez-moi et leurs richesses seront vôtres si vous savez "
                                 "ne pas trop ébruiter l’affaire. ― Emarin Grisant ».",
            'full_description': "« Cher collègue, je suis actuellement prisonnier au Pic d’Andalf. Aidez-moi et "
                                "vous serez récompensé pour votre peine. Attention ! Mes ravisseurs sont doués "
                                "de pouvoirs magiques. Libérez-moi et leurs richesses seront vôtres si vous savez "
                                "ne pas trop ébruiter l’affaire. ― Emarin Grisant ».",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'lettre-officielle-de-nicolai': {
            'name': "Lettre officielle, de Nicolaï",
            'base_item': lambda item: item.oid,
            'short_description': "Une lette officielle munie du sceau de Nicolaï qui mandate sont possesseur pour "
                                 "escorter la caravane de soutien logistique jusqu'à Flerk.",
            'full_description': "Une lette officielle munie du sceau de Nicolaï qui mandate sont possesseur pour "
                                 "escorter la caravane de soutien logistique jusqu'à Flerk.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="Voyage", numbering="1"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'symbole-beni-d-abalath': {
            'name': "Symbole béni, d'Abalath",
            'base_item': lambda item: item.oid,
            'short_description': "Un symoble béni du culte d’Abalath, le dieu des Secrets et des Complots.",
            'full_description': "Un symoble béni du culte d’Abalath, le dieu des Secrets et des Complots.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'sacs-en-toile': {
            'name': "Sac en toile",
            'base_item': lambda item: item.oid,
            'short_description': "Un sac en toile vide pouvant contenir environ 50 litres.",
            'full_description': "Un sac en toile vide pouvant contenir environ 50 litres.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'quantité': 5
        },
        'carnet-de-compte-de-sifmo': {
            'name': "Carnet de compte, de Sifmo",
            'base_item': lambda item: item.oid,
            'short_description': "Le carnet de Sifmo contient les revenus de ses activités mois par mois : "
                                 "1ère Année : 1er mois: 5000 pa, 2ième mois: 5000 pa, 3ième mois: 5000 pa, "
                                 "4ième mois: 5000 pa, 5ième mois: 5000 pa, 6ième mois: 5000 pa",
            'full_description': "Le carnet de Sifmo contient les revenus de ses activités mois par mois : "
                                 "1ère Année : 1er mois: 5000 pa, 2ième mois: 5000 pa, 3ième mois: 5000 pa, "
                                 "4ième mois: 5000 pa, 5ième mois: 5000 pa, 6ième mois: 5000 pa",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'quantité': 5
        },
        'liasse-de-comptes-d-amarange': {
            'name': "Carnet de compte, d'Amarange",
            'base_item': lambda item: item.oid,
            'short_description': "Une liasse de comptes contenant l’ensemble des opérations. Les sommes en jeux "
                                 "sont hallucinantes et feraient pâlir d’envie un dragon. elles font état de "
                                 "100 000 pa et toutes les grandes villes des Marches sont concernées.",
            'full_description': "Une liasse de comptes contenant l’ensemble des opérations. Les sommes en jeux "
                                "sont hallucinantes et feraient pâlir d’envie un dragon. elles font état de "
                                "100 000 pa et toutes les grandes villes des Marches sont concernées.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'quantité': 5
        },
        'batonnet-metallique': {
            'name': "Bâtonnet métallique, d'Annita de Caurel",
            'base_item': lambda item: item.oid,
            'short_description': "Un bâtonnet métallique qui procure un bonus en attaque et aux dégâts pour les "
                                 "sorts d’électricité lorsqu’il est pointé sur la cible.",
            'full_description': "Un bâtonnet métallique qui procure un bonus de +2 en attaque et +2 aux "
                                "dégâts pour les sorts d’électricité lorsqu’il est pointé sur la cible.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'cost': Cost(value=250.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'special_property': ["Attaque: +2 (sorts de d'électricité)",
                                 "DM: +2 (sorts de d'électricité)"],
            'hands': 1,
        },
        'briquet-magique': {
            'name': "Briquet magique, d'Annita de Caurel",
            'base_item': lambda item: item.oid,
            'short_description': "Un briquet magique qui procure un bonus en attaque et aux dégâts pour les "
                                 "sorts de feu lorsqu’il est pointé sur la cible.",
            'full_description': "Un briquet magique qui procure un bonus de +2 en attaque et +2 aux "
                                "dégâts pour les sorts de feu lorsqu’il est pointé sur la cible.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'cost': Cost(value=250.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'special_property': ["Attaque: +2 (sorts de feu)",
                                 "DM: +2 (sorts de feu)"],
            'hands': 1,
        },
        'materiel-ecriture-parchemin': {
            'name': "Nécessaire à parchemin, composants et encre",
            'base_item': lambda item: item.oid,
            'short_description': "Des composants et une bouteille d'encre pour écrire des parchemeins.",
            'full_description': "Des composants et une bouteille d'encre pour écrire des parchemeins.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'cost': Cost(value=200.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'livre-de-sort': {
            'name': "Livre de sort",
            'base_item': lambda item: item.oid,
            'short_description': "Un livre pour inscrire des sorts",
            'full_description': "Un livre pour inscrire des sorts",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'cost': Cost(value=200.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'boule-de-cristal': {
            'capacity': "http://co-drs.org/capacites/clairvoyance/",
            'name': "Boule de cristal, d'Amarange le Bel",
            'base_item': lambda item: item.oid,
            'short_description': "La personne qui utilise cette boule de cristal peut voir et entendre "
                                 "ce qui se passe dans un lieu qu’il connait, tant qu’il reste "
                                 "concentrée. Les créatures présentes peuvent se sentir observées.",
            'full_description': "La personne qui utilise cette boule de cristal peut voir et entendre à distance "
                                "ce qui se passe dans un lieu qu’il connait, tant qu’il reste concentré (action "
                                "limitée à chaque tour). Les créatures présentes ont droit à un test de SAG "
                                "difficulté [12 + Mod. de CHA] : en cas de réussite, elles se sentent observées.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'weight': Weight(value=0.3, unit='Kg'),
            'special_property': lambda item: item.special_property + ["Utilisation: 3 fois par jour"],
        },
        'gland-de-pouvoir': {
            "capacity": "http://co-drs.org/capacites/gland-de-pouvoir/",
            'name': "Gland de pouvoir",
            'short_description': "Avec une attaque à distance réussie, celui qui lance ce gland transforme la "
                                 "victime en statue de bois. Sous cette forme elle ne peut agir et "
                                 "ne ressent rien. Sa DEF passe à 10 et il obtient une RD de 10. Le sort s’achève "
                                 "dès que la cible perd plus de 10 PV. En cas d'échec, on peut le récupérer "
                                 "avec un test de SAG de 10 ou 20 selon la nature du sol).",
            'full_description': "Une fois par combat, la personne peut lancer un gland sur une cible (portée 10 m). En cas "
                                "d’attaque à distance réussie, la victime se transforme en statue de bois pendant [2d6 + Mod. "
                                "de SAG] tours. Sous cette forme elle ne peut agir et ne ressent rien. Sa DEF passe à 10 "
                                "mais elle gagne une réduction des DM de 10. Le sort s’achève dès que la cible perd "
                                "plus de 10 PV. S'il rate sa cible, il peut être récupéré avec un test de sagesse de difficulté 10 "
                                "ou 20 selon la nature du sol.",
            'category': "quest",
            'base_item': lambda item: item.oid,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'magnum-de-brandy-de-ferrance': {
            'name': "Magnum de brandy, de Ferrance",
            'base_item': lambda item: item.oid,
            'short_description': "Un magnum d'eau-de-vie de vin. Celui-ci provient de la ville de Ferrance, "
                                 "ce qui en fait une bouteille très appréciée par les amateurs de spiritueux.",
            'full_description': "Un magnum d'eau-de-vie de vin. Celui-ci provient de la ville de Ferrance, "
                                 "ce qui en fait une bouteille très appréciée par les amateurs de spiritueux.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(value=20.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.5, unit='Kg'),
        },
        'sac-sans-fond': {
            'capacity': "http://co-drs.org/capacites/sac-sans-fond/",
            'name': "Sac sans fond",
            'base_item': lambda item: item.oid,
            'short_description': "Un sac un sac pour y mettre du matériel. Le sac peut aussi fournir les "
                                 "objets qu’il désire de moins de 20 pa, 50 kg, 1m3 ou "
                                 "1m de circonférence. Pas plus de 20 pa d’objets créés peuvent exister à la fois. Ils "
                                 "disparaissent au bout d’une heure.",
            'full_description': "Un sac dans lequel on peut entreposer 50 kg de matériel par rang dans la voie, "
                                "tandis que le sac semble toujours ne peser qu’un kilo. Le sac ne fonctionne "
                                "pas si on tente d’y mettre une créature vivante. Le sac est de plus capable "
                                "de fournir au Forgesort les objets qu’il désire. Il peut en retirer une "
                                "pelle, une corde, une épée ou tout objet dont la valeur ne dépasse pas 20 pa, "
                                "le poids 50 kg, la circonférence 1 m et le volume 1 m3. Pas plus de 20 pa "
                                "de valeur d’objet créés par le sac sans fond ne peuvent exister simultanément. "
                                "Ces objets ont hélas la propriété de disparaître au bout d’une heure. De ce "
                                "fait, la nourriture magique retirée du sac ne nourrit pas vraiment celui "
                                "qui la consomme.",
            'category': "Magique",
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
        },
        'petit-parchemin-camp-orque-1': {
            'name': "Petit parchemin",
            'base_item': lambda item: item.oid,
            'short_description': "Le message suivant est écrit sur ce petit parchemin : "
                                 "« Tuer le chevalier haut elfe aux cheveux d'argent de retour... ».",
            'full_description': "Le message suivant est écrit sur ce petit parchemin : "
                                "« Tuer le chevalier haut elfe aux cheveux d'argent de retour... ».",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes",
                    chapter="e camp des Crocs-Brisés", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'petit-parchemin-camp-orque-2': {
            'name': "Petit parchemin",
            'base_item': lambda item: item.oid,
            'short_description': "Le message suivant est écrit sur ce petit parchemin : "
                                 "« Envoyez collier oreilles otages cette fois... ».",
            'full_description': "Le message suivant est écrit sur ce petit parchemin : "
                                "« Envoyez collier oreilles otages cette fois... ».",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes",
                    chapter="e camp des Crocs-Brisés", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'manche-de-hache': {
            'name': "Manche de hache",
            'base_item': lambda item: item.oid,
            'short_description': "Un manche de hache bien solide en chêne.",
            'full_description': "Unm anche de hache bien solide en chêne.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="La justices des Elfes",
                         chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'cost': Cost(value=1.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
            'quantity': 1
        },
        'clous': {
            'name': "Clous",
            'base_item': lambda item: item.oid,
            'short_description': "Un lot de 20 clous de bonne qualité.",
            'full_description': "Un lot de 20 clous de bonne qualité.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="La justices des Elfes",
                         chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'cost': Cost(value=1.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.2, unit='Kg'),
            'quantity': 20
        },
        'bracelet-arbre-coeur': {
            'name': "Bracelet, de l'Arbre-Coeur",
            'base_item': lambda item: item.oid,
            'short_description': "Bracelet taillé dans le tronc de l’Arbre-Cœur, un signe que tout elfe reconnaîtra "
                                 "comme la plus haute distinction elfique: Gardiens de l’Arbre sacré.",
            'full_description': "Bracelet taillé dans le tronc de l’Arbre-Cœur, un signe que tout elfe reconnaîtra "
                                 "comme la plus haute distinction elfique: Gardiens de l’Arbre sacré.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'feuilles-de-mandragore': {
            'name': "Feuilles de racine, de mandragore femelle",
            'base_item': lambda item: item.oid,
            'short_description': "Feuilles de racine de mandragore femelle.",
            'full_description': "Les feuilles de racine de mandragore femelle sont de grandes feuilles de forme "
                                "hastée et aux reflets bleus. Elles peuvent être soit mangées (3d6 PV récupérés), "
                                "soit plongées dans de l’eau bouillante. Dans ce cas, il faut recouvrir, les "
                                "laisser infuser, puis découvrir, puis inspirer une grand bouffée des vapeurs "
                                "qui se dégageront. Tous ceux qui inspirent ces effluves se sentiront revigorés "
                                "(1D6 PV récupéré par feuille plongée dans l’eau bouillante, jusqu’à 8 personnages "
                                "peuvent inspirer en même temps).",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'quantity': 3,
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'special_property': ["Soin: 3d6 PV (si mangée)", "Soin: 1d6 PV (si infusée)", "Infusion: 8 personnes max"]
        },
        'lanterne-elfique': {
            'name': "Lanterne elfique",
            'base_item': lambda item: item.oid,
            'short_description': "Une jolie lanterne réhaussée de petites pierres.",
            'full_description': "Une jolie lanterne réhaussée de petites pierres.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=250.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'loupe': {
            'name': "Une loupe",
            'base_item': lambda item: item.oid,
            'short_description': "Une loupe.",
            'full_description': "Une loupe.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'symbole-maudit-d-azazel': {
            'name': "Symbole maudit, d'Azazel",
            'base_item': lambda item: item.oid,
            'short_description': "Le symbole maudit d'Azazel, dieu de la Douleur et de la cruauté.",
            'full_description': "Le symbole maudit d'Azazel, dieu de la Douleur et de la cruauté.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=50.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'petit-coffret-en-platine': {
            'name': "Petit coffret, en platine",
            'base_item': lambda item: item.oid,
            'short_description': "Un petit coffret en platine en très mauvais état.",
            'full_description': "Un petit coffret en platine en très mauvais état.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'tube-a-parchemin-en-ivoire': {
            'name': "Tube à parchemin, en ivoire",
            'base_item': lambda item: item.oid,
            'short_description': "Un tube à parchemin en ivoire gravé.",
            'full_description': "Un tube à parchemin en ivoire gravé.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=75.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1
        },
        'manteau-en-peau-de-chat-sauvage': {
            'name': "Manteau, en peau de chat",
            'base_item': lambda item: item.oid,
            'short_description': "Un manteau en peau de chat sauvage.",
            'full_description': "Un manteau en peau de chat sauvage.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=125.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'fiole-encre-rare': {
            'name': "Fiole d'encre",
            'base_item': lambda item: item.oid,
            'short_description': "Une fiole d'encre rare.",
            'full_description': "Une fiole d'encre rare.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=25.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'collier-maison-eilserv': {
            'name': "Collier, de la maison Eilserv",
            'base_item': lambda item: item.oid,
            'short_description': "Un collier avec un baton cuivré, symbole de la maison Eilserv.",
            'full_description': "Un collier avec un baton cuivré, symbole de la maison Eilserv.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit='pa').iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'symbole-de-maedra': {
            'name': "Symbole, de Maëdra",
            'base_item': lambda item: item.oid,
            'short_description': "Le symbole de Maëdra déesse de l’Obéissance et des Insectes.",
            'full_description': "Le symbole de Maëdra déesse de l’Obéissance et des Insectes.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'collier-maison-kar-lothian': {
            'name': "Collier, de la maison Kar'Lothian",
            'base_item': lambda item: item.oid,
            'short_description': "Un collier avec une rune, symbole de la maison Kar'Lothian.",
            'full_description': "Un collier avec une rune, symbole de la maison Kar'Lothian.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'bouteille-liqueur-orque': {
            'name': "Une bouteille de liqueur",
            'base_item': lambda item: item.oid,
            'short_description': "Une bouteille contenant de la liqueur assez sucrée mais très fruitée.",
            'full_description': "Une bouteille contenant de la liqueur assez sucrée mais très fruitée.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=2.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.75, unit='Kg'),
            'quantity': 1
        },
        'lingot-or': {
            'name': "Un lingot d'or",
            'base_item': lambda item: item.oid,
            'short_description': "Une petite barre d'or.",
            'full_description': "Une petite barre d'or.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1, unit='Kg'),
            'quantity': 1
        },
        'gobelet-electrum': {
            'name': "Un gobelet, en électrum",
            'base_item': lambda item: item.oid,
            'short_description': "Un gobelet en électrum, un alliage composé d'or et d'argent.",
            'full_description': "Un gobelet en électrum, un alliage composé d'or et d'argent.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=25.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1
        },
        'couverts-en-argent': {
            'name': "Couverts, en argent",
            'base_item': lambda item: item.oid,
            'short_description': "Un service de couverts en argent.",
            'full_description': "Un service de couverts en argent.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=25.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'assiette-porcelaine': {
            'name': "Une assiette, en porcelaine",
            'base_item': lambda item: item.oid,
            'short_description': "Une assiette en porcelaine.",
            'full_description': "Une assiette en porcelaine.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=5.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 20
        },
        'mirroir-en-argent': {
            'name': "Un mirroir, en argent",
            'base_item': lambda item: item.oid,
            'short_description': "Un miroir d’argent au cadre plaqué or.",
            'full_description': "Un miroir d’argent au cadre plaqué or.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=350.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.2, unit='Kg'),
        },
        'psyche-en-argent': {
            'name': "Un psyché, en argent",
            'base_item': lambda item: item.oid,
            'short_description': "Un magifique miroir en argent.",
            'full_description': "Un magifique miroir en argent.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=120.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
        },
        'coupe-en-or': {
            'name': "Coupe en or.",
            'base_item': lambda item: item.oid,
            'short_description': "Une coupe en or serties de pierres précieuses.",
            'full_description': "Une coupe en or serties de pierres précieuses.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=700.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.2, unit='Kg'),
            'quantity': 1
        },
        'cassette-platine': {
            'name': "Une cassette , en platine.",
            'base_item': lambda item: item.oid,
            'short_description': "Une jolie petite boite en platine.",
            'full_description': "Une jolie petite boite en platine.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=700.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
    },
    "Bracer": {
    },
    'Potion': {
        'amphore-de-soin': {
            'name': "Petite amphore de soin",
            'base_item': lambda item: item.oid,
            'short_description': "Une petite amphone contenant un liquide qui permet de soigner les "
                                "blessures.",
            'full_description': "Une poterie en forme de petite amphone contenant un liquide qui permet de soigner les "
                                "blessures. La personne qui boit cette potion récupère alors [2d8 + niveau] PV perdus.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=200.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'special_property': ["Soigne: 2d8 PV + niveau"],
            'weight': Weight(value=0.5, unit='Kg'),
            'quantity': 1
        },
        'elixir-de-soin': {
            'name': "Élixir de soin",
            'base_item': lambda item: item.oid,
            'short_description': "Une petite fiole en métal contenant trois gorgées d'un élixir qui permet de soigner "
                                 "les blessures.",
            'full_description': "Une petite fiole en métal contenant trois gorgées d'un élixir qui permet de soigner "
                                "les blessures. Chaque gorgée de cet élixir soigne [1d8+5 PV].",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Scénarios uniques", title="Retour à clairval", chapter="La chasse au gobelin", numbering="3")
            ],
            'use': 3,
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'] * item.use,
                unit=ccc['global']['cost']['unit']).iso(),
            'special_property': ["Soigne: 1d8 + 5 PV"],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1
        },
        'fiole-de-poison': {
            'name': "Fiole de poison",
            'base_item': lambda item: item.oid,
            'short_description': "Une petite fiole en métal contenant une dose de poison à boire ou pour enduire une "
                                 "arme tranchante.",
            'full_description': "Une petite fiole en métal contenant une dose de poison à boire ou pour enduire une "
                                "arme tranchante. La personne qui ingére le poison ou qui reçoit une blessure "
                                "sanglante d'une arme enduite de ce poison se voit infliger 1d8+5 DM.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Scénarios uniques", title="Retour à clairval", chapter="Baston chez les Crânes-creux", numbering="4")
            ],
            'use': 1,
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'] * item.use,
                unit=ccc['global']['cost']['unit']).iso(),
            'special_property': ["DM: 1d8 + 5"],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1
        },
        'pot-acide': {
            'name': "Pot d'acide",
            'base_item': lambda item: item.oid,
            'short_description': "Un pot contenant un acide très puissant qui permet de cibler un ennemi et éclabousse "
                                 "ceux à proximité.",
            'full_description': "Un pot contenant un acide très puissant. Ce pot peut être jeté sur les adversaires "
                                "pour les dissoudre. La créature visée et touchée perd 3d6 PV le premier tour, 2d6 PV "
                                "le second et 1d6 PV au troisième tour. Toutes les créatures éclaboussées (3 mètres de "
                                "diamètre) souffrent de 1d6 points de dégâts au premier tour uniquement.",
            'category': "quest",
            'area': Area(value=3, unit="m"),
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'use': 1,
            'cost': lambda item: Cost(
                value=250,
                unit=ccc['global']['cost']['unit']).iso(),
            'special_property': [
                "DM (creature): 3d6 (1er tour)",
                "DM (creature): 2d6 (2ième tour)",
                "DM (creature): 1d6 (3ième tour)",
                "DM (zone): 1d6 (1er tour)"
            ],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1
        },
        'poison-narcotique': {
            'name': "Poison narcotique",
            'base_item': lambda item: item.oid,
            'short_description': "Un poison violent qui affaibli celui qui l'ingère. Une seule dose de ce poison est "
                                 "nécessaire pour empoisonner jusqu'à 12 personnes.",
            'full_description': "Un poison violent qui affaibli celui qui l'ingère. Une seule dose de ce poison est "
                                "nécessaire pour empoisonner jusqu'à 12 personnes pendant 1 heure.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1"),
            ],
            'use': 1,
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'] * item.use,
                unit=ccc['global']['cost']['unit']).iso(),
            'special_property': ["Effet après 10 min",
                                 "Test CON < 15: Affaibli (1d12)"],
            'quantity': 1,
            'weight': Weight(value=0.1, unit='Kg'),
            'duration': Duration(value=1, unit="h")
        },
        'flacon-de-sang-feu': {
            'name': "Flacon de sang feu",
            'base_item': lambda item: item.oid,
            'short_description': "Un petit flacon une contenant une dose de poison rapide pour enduire une "
                                 "arme tranchante ou pointue.",
            'full_description': "Un petit flacon une contenant une dose de poison rapide pour enduire une "
                                 "arme. La personne qui reçoit une blessure "
                                "sanglante d'une arme enduite de ce poison se voit infliger 2d6 DM s'il rate un "
                                "test de CON de difficulté 10.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'use': 1,
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'] * item.use,
                unit=ccc['global']['cost']['unit']).iso(),
            'special_property': ["DM: 2d6 (si empoisonné)",
                                 "Empoisonné: Test CON < 10"],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 3
        },
        'potion-fort-d-assaut': {
            'name': "Potion de fort d'assaut",
            'base_item': lambda item: item.oid,
            'short_description': "Une potion à enduire sur une arme de contact qui augmente de façon importante les "
                                 "dégâts occasionnés.",
            'full_description': "Une potion à enduire sur une arme de contact qui augmente de +1d6 les"
                                "dégâts occasionnés pendant 10 tours.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'],
                unit=ccc['global']['cost']['unit']).iso(),
            'quantity': 2,
            'special_property': ["DM: +1d6 (arme de contact)"],
            'weight': Weight(value=0.1, unit='Kg'),
            'duration': Duration(value=10, unit="tr")
        },
        'potion-de-force-des-geants': {
            'name': "Potion de force, de géant",
            'base_item': lambda item: item.oid,
            'short_description': "Une fois bue, cette potion procure, pour un petit laps de temps, un bonus "
                                 "à l'attaque et aux dégâts.",
            'full_description': "Une potion à enduire sur une arme de contact qui augmente de +1d6 les"
                                "dégâts occasionnés pendant 10 tours.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'],
                unit=ccc['global']['cost']['unit']).iso(),
            'quantity': 1,
            'special_property': ["Attaque: +2 (contact)", "DM: +2 (contact)"],
            'weight': Weight(value=0.1, unit='Kg'),
            'duration': Duration(value=10, unit="tr")
        },
        'flasque-de-fer-jarraseen': {
            'name': "Flasque de fer",
            'base_item': lambda item: item.oid,
            'short_description': "Une flasque de fer couverte de signes magiques et fermé par un bouchon "
                                 "hermétique en fer.",
            'full_description': "Une flasque de fer couverte de signes magiques et fermé par un bouchon "
                                "hermétique en fer.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': lambda item: Cost(
                value=0.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'huile-etheree': {
            "name": "Huile éthérée",
            'base_item': lambda item: item.oid,
            "capacity": "http://co-drs.org/capacites/forme-etheree/",
            "short_description": "En buvant cette huile, La personne (et son équipement) deviennent "
                                 "translucides et intangibles. Ils peuvent passer à travers murs et "
                                 "obstacles.",
            "full_description": "La personne qui boit cette huile et tout son équipement deviennent "
                                "translucides et intangibles pendant [5 + Mod. de CHA] tours. Sous "
                                "cette forme, elle peut passer à travers murs et obstacles, et ne peut "
                                "subir aucun DM physiques.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1
        },
        'potion-levitation': {
            "capacity": "http://co-drs.org/capacites/levitation/",
            "short_description": "En se concentrant, la personne qui boit cette potion peut « léviter » à "
                                 "une vitesse de 10 m par tour.",
            "full_description": "En se concentrant, la personne qui boit cette potion peut « léviter » à "
                                 "une vitesse de 10 m par tour.",
            'category': "quest",
            'base_item': lambda item: item.oid,
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1
        },
        'potion-vol-coup-double': {
            "name": "Potion de vol, de chez Coup-Double",
            "capacity": "http://co-drs.org/capacites/vol/",
            "short_description": "La personne qui boit cette potion peut voler. Sa vitesse de déplacement est la "
                                 "même qu’au sol. Effet secondaire : le personnage ne peut plus parler pendant toute "
                                 "la durée du vol. Il peut uniquement grogner comme un porc.",
            "full_description": "La personne qui boit cette potion peut voler pendant [1d6 + Mod. d’INT] minutes. "
                                "Sa vitesse de déplacement est la même qu’au sol. Effet secondaire : le personnage "
                                "ne peut plus parler pendant toute la durée du vol. Il peut uniquement grogner "
                                "comme un porc.",
            'category': "quest",
            'base_item': 'potion-vol',
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1,
            'cost': lambda item: Cost(
                value=3500,
                unit=ccc['global']['cost']['unit']).iso(),
        },
        'potion-invisibilite-coup-double': {
            "name": "Potion d'invisibilité, de chez Coup-Double",
            "capacity": "http://co-drs.org/capacites/vol/",
            "short_description": "La personne qui boit cette potion se rend invisible et personne ne peut plus "
                                 "détecter sa présence ou lui porter d’attaque.",
            "full_description": "La personne qui boit cette potion se rend invisible pendant [1d6 + Mod. d’INT] "
                                "minutes. Une fois invisible, personne ne peut plus détecter sa présence ou lui "
                                "porter d’attaque. Si la personne attaque ou utilise une capacité limitée, elle "
                                "redevient visible. Effet secondaire : le personnage dégage le temps de son "
                                "invisibilité une odeur semblable aux flatulences d’un gnome aux intestins très "
                                "contrariés.",
            'category': "quest",
            'base_item': 'potion-invisibilite',
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1,
            'cost': lambda item: Cost(
                value=300,
                unit=ccc['global']['cost']['unit']).iso(),
            'special_property': lambda item: item.special_property + ["Dégage une odeur nauséabonde"]
        },
        'potion-soins-legers-coup-double': {
            "name": "Potion de soins légers, de chez Coup-Double",
            "capacity": "http://co-drs.org/capacites/soins-legers/",
            "short_description": "La personne qui boit cette potion récupère alors [1d8 + niveau] PV perdus. "
                                 "Effet secondaire : tous les poils du personnage (cheveux, barbe, sourcils, "
                                 "avant-bras...) poussent de dix centimètres.",
            "full_description": "La personne qui boit cette potion récupère alors [1d8 + niveau] PV perdus. "
                                "Effet secondaire : tous les poils du personnage (cheveux, barbe, sourcils, "
                                "avant-bras...) poussent de dix centimètres.",
            'category': "quest",
            'base_item': 'potion-soins-legers',
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1,
            'cost': lambda item: Cost(
                value=200,
                unit=ccc['global']['cost']['unit']).iso(),
        },
        'potion-de-resistance-au-feu': {
            'name': "Potion de résistance, au feu",
            'base_item': lambda item: item.oid,
            'short_description': "Une fois bue, cette potion procure, pour un petit laps de temps, un bonus "
                                 "de résistance aux dégats de feu.",
            'full_description': "Une fois bue, cette potion divise par 2 tous les DM de feu reçus pendant "
                                "10 minutes",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'],
                unit=ccc['global']['cost']['unit']).iso(),
            'quantity': 1,
            'weight': Weight(value=0.1, unit='Kg'),
            'duration': Duration(value=10, unit="min"),
            'special_property': [
                "RD: DM feu / 2",
            ],
        },
        'potion-antidote': {
            'name': "Potion d'antidote",
            'base_item': lambda item: item.oid,
            'short_description': "Cette potion peut être ingurgitée pour soigner ou prévenir un empoisonnement.",
            'full_description': "Cette potion peut être ingurgitée pour soigner un empoisonnement ou préventivement. "
                                "Dans ce cas, elle donne un bonus de +5 aux tests de CON pour résister aux poisons "
                                "et divise par deux les effets des poisons (DM ou durée) pendant 10 minutes.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'],
                unit=ccc['global']['cost']['unit']).iso(),
            'quantity': 1,
            'use': 3,
            'weight': Weight(value=0.1, unit='Kg'),
            'duration': Duration(value=10, unit="min"),
            'special_property': [
                "Préventif: +5 test CON",
                "Préventif: DM poison / 2",
                "Préventif: durée poison / 2",
            ],
        },
        'potion-guerison': {
            "name": "Potion, de guérison",
            "capacity": "http://co-drs.org/capacites/guerison/",
            "short_description": "La personne qui boit cette potion récupère tous ses PV. Elle est aussi guérie des "
                                 "poisons, maladies et affaiblissements de Caractéristiques.",
            "full_description": "La personne qui boit cette potion récupère tous ses PV. Elle est aussi guérie des "
                                "poisons, maladies et affaiblissements de Caractéristiques.",
            'category': "quest",
            'base_item': 'potion-guerison',
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'quantity': 1,
        },
        'potion-de-resistance-acide': {
            'name': "Potion de résistance, à l'acide",
            'base_item': lambda item: item.oid,
            'short_description': "Une fois bue, cette potion procure, pour un petit laps de temps, un bonus "
                                 "de résistance aux dégats d'acide.",
            'full_description': "Une fois bue, cette potion divise par 2 tous les DM d'acide' reçus pendant "
                                "10 minutes",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': lambda item: Cost(
                value=ccc['global']['cost']['potions'],
                unit=ccc['global']['cost']['unit']).iso(),
            'quantity': 1,
            'weight': Weight(value=0.1, unit='Kg'),
            'duration': Duration(value=10, unit="min"),
            'special_property': [
                "RD: DM acide / 2",
            ],
        },
    },
    "Spell": {
        'spell-message-lointain': {
            'capacity': "http://co-drs.org/capacites/murmures-dans-le-vent/",
            'name': "Parchemin - Message lointain",
            'short_description': "La personne qui utilise ce parchemin chuchote un message d’une dizaine de mots "
                                 "qui voyage jusqu’à son destinataire. Elle doit connaître la cible ou la voir et "
                                 "peut entendre sa réponse immédiatement.",
            'full_description': "La personne qui utilise ce parchemin chuchote un message d’une dizaine de mots "
                                "qui voyage jusqu’à son destinataire. Elle peut entendre sa réponse immédiatement. "
                                "La portée est de 100 Km et le personnage doit connaître la "
                                "cible ou la voir.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Fort Boueux", chapter="La bataille de vireux", numbering="3")
            ],
            'range': Range(value=100, unit="km"),
            'quantity': 1
        },
        'spell-fleche-enflammee': {
            "capacity": "http://co-drs.org/capacites/fleche-enflammee/",
            'short_description': "La personne qui lance ce sort choisit une cible à distance. Si son attaque magique "
                                 "réussit, la cible encaisse des dégâts et la flèche enflamme ses vêtements le "
                                 "tour suivant.",
            'full_description': "La personne qui lance ce sort choisit une cible située à moins de 30 mètres. Si son"
                                "attaque magique réussit, la cible encaisse [1d6 + Mod. d’INT] DM et la flèche "
                                "enflamme ses vêtements. Chaque tour de combat suivant, le feu inflige 1d6 dégâts "
                                "supplémentaires. Sur un résultat de 1 à 2, les flammes s’éteignent et le sort "
                                "prend fin.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'quantity': 1
        },
        'spell-invisibilite': {
            "capacity": "http://co-drs.org/capacites/invisibilite/",
            'short_description': "La personne qui lance ce sort se rend invisible et personne ne peut plus détecter "
                                 "sa présence ou lui porter d’attaque.",
            'full_description': "La personne qui lance ce sort se rend invisible pendant [1d6 + Mod. d’INT] minutes. "
                                "Une fois invisible, personne ne peut plus détecter sa présence ou lui porter "
                                "d’attaque. Si la personne attaque ou utilise une capacité limitée, elle redevient "
                                "visible.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'quantity': 1
        },
        'spell-telekinesie': {
            "capacity": "http://co-drs.org/capacites/telekinesie/",
            'short_description': "La personne qui lance ce sort peut déplacer dans les airs un objet inerte ou "
                                 "une cible volontaire. Il est possible de faire tomber un objet sur une cible "
                                 "surprise qui subit alors des dégâts.",
            'full_description': "La personne qui lance ce sort peut déplacer dans les airs un objet inerte ou une "
                                "cible volontaire (par exemple elle-même) dont le poids n’excède pas 50 kg par "
                                "Rang, à une portée de 20 m et pendant [5+Mod. de CHA] tours. L’objet peut être "
                                "déplacé de 10 m par tour au prix d’une action de mouvement. Il est possible de "
                                "faire tomber un objet sur une cible surprise (DM 1d6 tous les 50 kg).",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'quantity': 1
        },
        'spell-mirage': {
            "capacity": "http://co-drs.org/capacites/mirage/",
            'short_description': "La personne qui lance ce sort crée une illusion visuelle et sonore immobile. Le "
                                 "volume maximum de l’illusion est de 10 m de coté par rang dans la voie. Divisez "
                                 "ces paramètres par 10 si l’illusion est animée.",
            'full_description': "La personne qui lance ce sort crée une illusion visuelle et sonore immobile d’une "
                                "durée de [5 + Mod. de CHA] minutes (ou tours si l’illusion est animée). Le volume "
                                "maximum de l’illusion est de 10 m de coté par rang dans la voie (portée 500 m). "
                                "Divisez ces paramètres par 10 si l’illusion est animée. Interagir avec l’illusion "
                                "la fait disparaître.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'quantity': 1
        },
        'spell-tenebres': {
            "capacity": "http://co-drs.org/capacites/tenebres/",
            'short_description': "La personne qui lance ce sort invoque une zone fixe de ténèbres magiques. Même "
                                 "les créatures capables de voir dans le noir sont aveuglées dans cette zone.",
            'full_description': "La personne qui lance ce sort invoque une zone fixe de ténèbres magiques, de 10 m "
                                "de diamètre, pour une durée de [5 + Mod. d’INT] tours. Même les créatures capables "
                                "de voir dans le noir sont aveuglées dans cette zone.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'quantity': 1
        },
        'spell-pattes-daraignee': {
            "capacity": "http://co-drs.org/capacites/pattes-d-araignee/",
            "short_description": "La personne qui lance ce sort peut se déplacer de 10 m par "
                                 "action de mouvement sur les murs et les plafonds. S’il reste "
                                 "immobile, il peut lancer des sorts.",
            "full_description": "La personne qui lance ce sort peut se déplacer de 10 m par "
                                "action de mouvement sur les murs et les plafonds pendant "
                                "[5 + Mod. d’INT] tours. S’il reste immobile, il peut "
                                "lancer des sorts.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'quantity': 1
        },
        'spell-strangulation': {
            "capacity": "http://co-drs.org/capacites/strangulation/",
            "short_description": "En réussissant un test d’attaque magique, la personne qui lance ce sort étouffe "
                                 "une créature vivante pourvu qu’elle maintienne sa concentration. Elle s'affaiblie "
                                 "alors un peu plus chaque tour. Si la victime sort du champ de vision du "
                                 "Nécromancien, le sort prend fin.",
            "full_description": "En réussissant un test d’attaque magique (portée 20 m), la personne qui lance ce "
                                "sort étouffe une créature vivante et lui inflige [1d6 + Mod. d’INT] DM par tour "
                                "pendant [rang] tours pourvu qu’il maintienne sa concentration par une action "
                                "limitée. La victime subit un malus égal au nombre de tours d’effet de la "
                                "Strangulation (-1 au premier tour, -2 au second, etc.) à tous ses tests. Si la "
                                "victime sort du champ de vision du Nécromancien, le sort prend fin.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Monastir", numbering="3"
                ),
            ],
            'quantity': 1
        },
        'spell-murmure-dans-le-vent': {
            'capacity': "http://co-drs.org/capacites/murmures-dans-le-vent/",
            'short_description': "La personne qui utilise ce parchemin chuchote un message d’une dizaine de mots "
                                 "qui voyage jusqu’à son destinataire. Elle doit connaître la cible ou la voir et "
                                 "peut entendre sa réponse immédiatement.",
            'full_description': "La personne qui utilise ce parchemin chuchote un message d’une dizaine de mots "
                                "qui voyage jusqu’à son destinataire. Elle peut entendre sa réponse immédiatement. "
                                "La portée est de 100m par rang dans la voie et le personnage doit connaître la "
                                "cible ou la voir.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'quantity': 1
        },
        'spell-asphyxie': {
            'capacity': "http://co-drs.org/capacites/asphyxie/",
            'short_description': "Avec une attaque magique, la personne qui utilise ce parchemin prive la créature "
                                 "ciblée d’air. La victime étouffe progressivement et subit des dégâts à chaque tour.",
            'full_description': "Si la personne qui utilise ce parchemin réussit son test d’attaque magique "
                                "(avec une portée de 20 m), la créature ciblée est privée d’air. La victime "
                                "étouffe progressivement et subit 1d6 DM par tour pendant [1+Mod. d’INT] tours.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'quantity': 1
        },
        'spell-forme-gazeuse': {
            'capacity': "http://co-drs.org/capacites/forme-gazeuse/",
            'short_description': "La personne qui utilise ce parchemin se transforme en gaz. Elle se "
                                 "déplace au ras du sol et ne peut utiliser aucune capacité.",
            'full_description': "La personne qui utilise ce parchemin prend la consistance d’un gaz. Elle se "
                                "déplace au ras du sol (si elle " 
                                "chute, elle le fait au ralenti) à une vitesse de 10 m par tour. elle peut "
                                "s’introduire par les plus petits interstices (comme sous une porte) mais "
                                "ne peut utiliser aucune capacité sous cette forme. Elle ne subit pas non "
                                "plus de DM, à l’exception des sorts de zone occasionnant des DM (comme "
                                "Boule de feu). Le sort a une durée de [1d4 + Mod. d’INT] tours.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'quantity': 1
        },
        'spell-respiration-aquatique': {
            'capacity': "http://co-drs.org/capacites/respiration-aquatique/",
            'short_description': "La personne qui utilise ce parchemin peut respirer sous l’eau pendant "
                                 "10 minutes.",
            'full_description': "La personne qui utilise ce parchemin peut respirer sous l’eau pendant "
                                "10 minutes.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'quantity': 1
        },
        'spell-vol': {
            'capacity': "http://co-drs.org/capacites/vol/",
            'short_description': "La personne qui utilise ce parchemin peut voler. Sa vitesse de "
                                 "déplacement est la même qu’au sol.",
            'full_description': "La personne qui utilise ce parchemin peut voler pendant "
                                "[1d6 + Mod. d’INT] minutes. Sa vitesse de déplacement "
                                "est la même qu’au sol.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'quantity': 1
        },
        'spell-nuees-de-criquets': {
            'capacity': "http://co-drs.org/capacites/nuees-de-criquets/",
            "full_description": "En réussissant un test d’attaque magique (portée 20 m), la personne "
                                "qui utilise ce parchemin libère sur sa cible une nuée de criquet "
                                "affamés qui la dévorent à petit feu pendant [5 + Mod de SAG.] tours. "
                                "La victime subit 2 points de DM par tour et un malus de -3 à toutes "
                                "ses actions. Les DM de zone détruisent la nuée.",
            "short_description": "Sur une attaque magique réussie, la personne qui utilise ce parchemin "
                                 "libère sur sa cible une nuée de criquet affamés qui la dévorent à "
                                 "petit feu.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="Fleck", numbering="2"
                ),
            ],
            'quantity': 1
        },
        'spell-cercle-de-protection': {
            "capacity": "http://co-drs.org/capacites/cercle-de-protection/",
            "full_description": "L'utilisateur de ce parchemin peut tracer un cercle sur le sol pouvant "
                                "contenir 3 personnes. Une fois par tour, lorsqu’un sort prend pour cible "
                                "un personnage situé dans le cercle (par un test d’attaque magique), "
                                "l'utilisateur de ce parchemin fait un test d’attaque magique en opposition "
                                "à celui de l’adversaire. Si le test est réussi, le sort adverse est annulé "
                                "et n’a aucun effet.",
            "short_description": "L'utilisateur de ce parchemin peut tracer un cercle sur le sol pour se "
                                 "protéger des sorts adverses. Une fois par tour, lorsqu’un sort (attaque "
                                 "magique) prend pour cible un personnage situé dans le cercle, l'utilisateur "
                                 "fait un test d’attaque magique en opposition à celui de l’adversaire. En "
                                 "cas de succès le sort adverse n’a aucun effet.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="Fleck", numbering="2"
                ),
            ],
            'quantity': 1
        },
        'spell-arme-argent': {
            "capacity": "http://co-drs.org/capacites/arme-d-argent/",
            "full_description": "Ce miracle crée pour la durée du combat une arme d’argent et de lumière "
                                "que seul l'utilisateur de ce parchemin peut utiliser. Cette arme inflige "
                                "[1d6 + Mod. de SAG] de DM. Contre les démons et les mort-vivants, elle "
                                "offre un bonus de +2 en attaque et ajoute +1d6 aux DM.",
            "short_description": "Ce miracle crée pour la durée du combat une arme d’argent et de lumière "
                                 "que seul l'utilisateur de ce parchemin peut utiliser.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'quantity': 1
        },
        'spell-foudres-divines': {
            "capacity": "http://co-drs.org/capacites/foudres-divines/",
            "full_description": "La foudre frappe toutes les créatures désignées dans un rayon de 10 mètres "
                                "autour de l'utilisateur de ce parchemin et leur inflige [1d6 + Mod. de SAG] "
                                "de DM. L'utilisateur compare son test d’attaque magique à la DEF de chaque "
                                "cible.",
            "short_description": "La foudre frappe toutes les créatures désignées autour de l'utilisateur de "
                                 "ce parchemin.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'quantity': 1
        },
        'spell-teleportation': {
            "capacity": "http://co-drs.org/capacites/teleportation/",
            "full_description": "La personne qui utilise ce parchemin disparaît et réapparaît à un autre endroit "
                                "situé à moins de [INT x 10] mètres. Le lieu d’arrivée doit être soit en ligne de "
                                "vue, soit parfaitement connu par cette personne.",
            "short_description": "La personne qui utilise ce parchemin disparaît et réapparaît à un autre endroit.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'quantity': 1
        },
        'spell-desintegration': {
            "capacity": "http://co-drs.org/capacites/desintegration/",
            "full_description": "La personne qui utilise ce parchemin projette un rayon mortel dont la portée est de "
                                "20 mètres et qui annule la cohésion de la matière, ne laissant derrière lui qu’un "
                                "amas de poussière. Un test d’attaque magique réussi permet de toucher une créature "
                                "et d’infliger [5d6 + Mod. d’INT] DM. Si l'utilisateur vise un objet porté par une "
                                "créature, le jet d’attaque subit un malus de -5. Les objets magiques sont insensibles "
                                "à ce sort, les objets normaux sont réduits en poussière. Aucun objet de plus de 50 kg "
                                "ne peut être affecté par ce sort : inutile donc de tenter de creuser un tunnel par ce "
                                "biais. En revanche, vous pourrez ainsi désintégrer une porte (ou même une pierre dans "
                                "un mur).",
            "short_description": "L'utilisateur projette un rayon mortel qui réduit la matière en un amas de poussière "
                                 "que la cible soit une créature ou un objet.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'quantity': 1
        },
        'spell-detection-de-linvisible': {
            "capacity": "http://co-drs.org/capacites/detection-de-l-invisible/",
            "short_description": "La personne qui utilise ce parchemin détecte les créatures invisibles ou cachées "
                                 "et si un sort de Clairvoyance affecte l’endroit.",
            "full_description": "Pendant [5 + Mod. de CHA] tours, la personne qui utilise ce parchemin détecte les "
                                "créatures invisibles ou cachées à moins de 30 mètres et détecte si un sort de "
                                "Clairvoyance affecte l’endroit. Aveuglé, ce sort lui permet de voir normalement.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=0.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'use': 3
                            
        }, 
        'spell-clairvoyance': {
            "capacity": "http://co-drs.org/capacites/clairvoyance/",
            "short_description": "La personne qui utilise ce parchemin peut voir et entendre "
                                 "ce qui se passe dans un lieu qu’elle connait, tant qu’elle reste "
                                 "concentrée. Les créatures présentes peuvent se sentir observées.",
            "full_description": "La personne qui utilise ce parchemin peut voir et entendre à distance "
                                "ce qui se passe dans un lieu qu’il connait, tant qu’elle reste "
                                "concentré (action limitée à chaque tour). Les créatures présentes "
                                "ont droit à un test de SAG difficulté [12 + Mod. de CHA] : en cas "
                                "de réussite, elles se sentent observées.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=0.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'use': 3
                            
        },
       'spell-main-deployee': {
            "name": "Main déployée (L)",
            'short_description': "Un jet de flamme qui "
                                "touche toutes les créatures au contact dans un arc de 180°.",
            'full_description': "La personne qui lance ce sort à ses mains qui deviennent brûlantes. Un jet de flamme "
                                "affecte toutes les créatures au contact du porteur dans un arc de 180°. Elles subissent "
                                "3d6 DM ou la moitié si elles réussissent un test de DEX difficulté 12.",
            'category': "quest",
             "attack": Attack(
                atype="magical",
                damages=Damage(
                    base=[],
                    other=[Mod(die=6, count=3, target="fire")],
                ),
                critical=RangeSet([20])
            ),
            'special_property': [
                "Utilisable: 3 fois par jour",
                "Test DEX >= 12: DM / 2"
            ],
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'use': 3,
            'cost': lambda item: Cost(
                value=0.0,
                unit=ccc['global']['cost']['unit']).iso(),
        },
        'spell-pointer-du-doigt': {
            "name": "Pointer du doigt (L)",
            "capacity": "http://co-drs.org/capacites/projectile-magique/",
            "short_description": "La personne qui utilise ce parchemin peut cibler une cible qui encaisse alors "
                                 "automatiquement des dégâts.",
            "full_description": "La personne qui utilise ce parchemin choisit une cible visible située à moins de "
                                "50 mètres. Elle encaisse automatiquement 1d4 points de dégâts (pas de test "
                                "d’attaque nécessaire).",
            "range": Range(value=50, unit="m"),
            'category': "quest",
            'special_property': lambda item: [p for p in item.special_property] + [
                "Utilisable: 3 fois par jour",
            ],
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=0.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'use': 3
                            
        },
        'spell-paume-ouverte': {
            "name": "Paume ouverte (L)",
            'short_description': "La personne qui lance ce sort peut immobiliser des personnes ou des monstres.",
            'full_description': "La personne qui lance ce sort peut immobiliser des personnes ou des monstres, la "
                                "créature doit faire un test de SAG difficulté 15 ou être immobilisée pendant 1 tour "
                                "(d12 et pas de déplacement).",
            'category': "quest",
            "duration": Duration(value="1", unit="tr"),
            'special_property': [
                "Utilisable: 3 fois par jour",
                "Immobilisé: d12 au lieu du d20",
                "Test SAG < 15: Immobilisé"
            ],
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=0.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'use': 3,
        },
        'spell-caresse-joue': {
            "capacity": "http://co-drs.org/capacites/peau-de-pierre-2/",
            "name": "Caresse sur la joue (L)",
            'short_description': "La personne qui lance ce sort obtient une réduction des DM pendant plusiuers "
                                 "tours ou jusqu’à ce que le sort ait absorbé un certain nombre de dégâts.",
            'full_description': "La personne qui lance ce sort obtient une réduction des DM égale à [5 + Mod. d’INT] pendant [5+ Mod. "
                                 "d’INT] tours ou jusqu’à ce que le sort ait absorbé 40 points de dégâts.",
            'category': "quest",
            'special_property': lambda item: [p for p in item.special_property] + [
                "Utilisable: 3 fois par jour",
            ],
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'use': 3,
        },
        'spell-cercle-de-la-main': {
            "capacity": "http://co-drs.org/capacites/mur-de-force/",
            "name": "Cercle de la main (L)",
            'short_description': "La personne qui lance ce sort crée un mur de force indestructible (5m haut par 3m de long), ou bien une hémisphère centrée "
                             "sur lui-même (3m de rayon).",
            'full_description': "La personne qui lance ce sort crée un mur de force indestructible (portée 10 m, maximum 5 m de haut "
                                "et 10 m de long), ou bien une hémisphère de 3 m de rayon centrée sur lui-même. Le sort dure "
                                "pendant [5 + Mod. de CHA] tours.",
            'category': "quest",
            'special_property': lambda item: [p for p in item.special_property] + [
                "Utilisable: 3 fois par jour",
            ],
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=0.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'use': 3,
        },
        'spell-coup-de-poing': {
            "capacity": "http://co-drs.org/capacites/boule-de-feu/",
            "name": "Coup de poing (L)",
            'short_description': "Une boule de feu blessant toutes personnes "
                                 "dans la zone d'effet.",
            'full_description': "La personne qui lance ce sort crée un mur de force indestructible (portée 10 m, maximum 5 m de haut "
                                "et 10 m de long), ou bien une hémisphère de 3 m de rayon centrée sur lui-même. Le sort dure "
                                "pendant [5 + Mod. de CHA] tours.",
            'category': "quest",
            'special_property': lambda item: [p for p in item.special_property] + [
                "Utilisable: 3 fois par jour",
            ],
            "attack": Attack(
                atype='magical',
                area=Area(value=6, unit="m"),
                range=Range(value=30, unit="m"),
                damages=Damage(
                    base=[],
                    other=[Mod(die=6, count=6, target="feu"),
                        Mod(target="INT", mtype="+", label="(Échec: DM / 2)")],
                ),
                critical=RangeSet([20])
            ),
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=0.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'use': 3,
        },
    },
    "MagicalWand": {
        'magic-wand-defoliation': {
            'name': "Baguette - Défoliation",
            'base_item': lambda item: item.oid,
            'short_description': "L'utilisateur de cette baguette tue toute végétation ordinaire (non magique) "
                                 "autour de lui ou inflige des dégâts à une créature végétale (pas de sauvegarde).",
            'full_description': "La personne qui utilise cette baguette tue toute végétation ordinaire (non magique) "
                                "dans un rayon de 50 mètres autour d'elle ou inflige 4d6 DM à une "
                                "créature végétale sans aucune sauvegarde.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'area': Area(value=50, unit="m"),
            'cost': lambda item: Cost(value=item.use * ccc['global']['cost']['spells'],
                                      unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1,
            'use': 12,
            'hands': 1,
            'special_property': ["Attaque: 4d6 (créature végétale)"]
        },
        'magic-wand-de-givre': {
            'capacity': "http://co-drs.org/capacites/cone-de-froid/",
            "full_description": "Le cône de affecte toute les créatures dans un cône approximatif de "
                                "20 mètres de long sur 10 mètres de large à son extrémité. Les "
                                "victimes subissent [2d6+Mod d’INT] DM et sont Ralenties pour 1 tour "
                                "si elles ratent un test de CON difficulté 13. Sinon, elles subissent "
                                "seulement la moitié des DM et ne sont pas ralenties. Cette baguette "
                                "contient 10 charges.",
            "short_description": "Un cône de froid sort de la baguette et affecte les créatures "
                                 "prises à l'intérieur.",
            'name': "Baguette - de givre",
            'base_item': lambda item: item.oid,
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': lambda item: Cost(value=item.way_rank * item.way_rank * item.use * ccc['global']['cost']['spells'],
                                      unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'quantity': 1,
            'use': 6,
            'hands': 1,
        },
        'sceptre-de-puissance-ogre-mage': {
            'name': "Sceptre de puissance, d'Ogre-mage",
            'base_item': lambda item: item.oid,
            'short_description': "Ce septre de puissance permet de lancer les sorts de rang 1 par une action de "
                                 "mouvement et ceux de rang 2 par une action d’attaque. Il peut peut être utilisé "
                                 "une fois par jour et par niveau.",
            'full_description': "Ce septre de puissance permet de lancer les sorts de rang 1 par une action de "
                                "mouvement et ceux de rang 2 par une action d’attaque. Il peut peut être utilisé "
                                "une fois par jour et par niveau.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2"
                )
            ],
            'hands': 1,
            'cost': lambda item: Cost(value=100 * ccc['global']['cost']['spells'],
                                      unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
    },
    "Weapon": {
        'arbalete-automatique': {
            'category': 'standard',
            'name': "Arbalète automatique, du forgesort",
            'base_item': 'arbalete-automatique',
            'full_description': "Le forgesort fabrique une arbalète complexe qu'il est le seul à pouvoir "
                                "utiliser. Elle est dotée d'un chargeur de 10 carraux et permet de tirer "
                                "un carreau au prix d'une action de mouvement (il est donc possible de "
                                "tirer plusieurs carreaux par tour). Elle inflige [2d4 + Mod de DEX] DM à "
                                "une portée de 50 mètres. Il faut un tour complet pour la recharger.",
            'short_description': "Arbalète automatique du forgesort.",
            'weight': cof.properties.Weight(value=9.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='ranged',
                damages=Damage(
                    base=[Mod(die=4, count=2, target=['punctured'])],
                    other=[Mod(mtype="+", target="DEX")],
                ),
                range=Range(value=50, unit='m'),
                critical=RangeSet([20])
            ),
            'use': 5,
            'special_property': [
                "Attaque: Action mouvement",
                "Capacité : 10 munitions",
                "Rechargement: 1 tour",
            ],
            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
        },
        'epee-longue-de-kolik': {
            'name': "Épée longue, de Kolik",
            'base_item': lambda item: item.oid,
            'short_description': "Une épée longue de belle facture pourvue d'une lame en laënk et ornée d'un rubis "
                                 "sur le pommeau. Cette lame éclaire dans l'obscurité.",
            'full_description': "Une épée longue de belle facture pourvue d'une lame en laënk et ornée d'un rubis "
                                 "sur le pommeau qui éclaire dans l'obscurité dans un rayon de 3 mètres."
                                " Elle procure un bonus de +1 en attaque et inflige 1d8 de dégâts.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Scénarios uniques", title="Retour à clairval", chapter="Baston chez les Crânes-creux", numbering="4")
            ],
            'cost': Cost(value=500.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'material': 'laenk',
            'special_property': ["Lumière: 3m"],
            'flavor': [Flavor(ftype='laenk', count=1)],
        },
        'tranchoir-a-2-mains-d-ogre': {
            'name': "Tranchoir",
            'base_item': lambda item: item.oid,
            'short_description': "Bien affuté, ce tranchoir permettra de découper en rondelles tous vos ennemis.",
            'full_description': "Bien affuté, ce tranchoir permettra de découper en rondelles tous vos ennemis. "
                                "Il inflige 2d6 DM mais nécessite au minimum une force de 14.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=3, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=6, count=2, target=['sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': ["Force minimum > 14"]
        },
        'dague-sacrificielle': {
            'name': "Dague sacrificielle",
            'base_item': lambda item: item.oid,
            'short_description': "Une dague dont la garde en forme de tête de mort enserre une lame forgée dans "
                                 "un métal noir.",
            'full_description': "Une dague dont la garde en forme de tête de mort enserre une lame forgée dans un "
                                "métal noir. Elle n’octroie aucun bonus magique, mais toute victime d’une blessure "
                                "par cette lame doit réussir un test de CON difficulté 10 ou être Affaibli pendant "
                                "un tour (d12 à tous les tests). Cette dague est clairement d'origine maléfique.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                ),
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=12.0 * ccc['global']['cost']['cold-iron'] + 60.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'material': "gorndar",
            'special_property': ["Test CON <= 10 (si attaque réussie): Affaibli (d12) pendant 1 tour"],
            'flavor': [Flavor(ftype="gorndar", count=1)],
        },
        'epee-courte-de-qualite-en-fer-froid': {
            'name': "Épée courte de qualité, en fer froid",
            'base_item': lambda item: item.oid,
            'short_description': "Une épée courte de qualité pourvue d'une lame en ferd froid.",
            'full_description': "Une épée courte de qualité qui permet d'attaquer avec un bonus "
                                "de +1 et pourvue d'une lame en ferd froid. "
                                "Cette épée inflige 1d6 de dégâts qui sont multipliés par 2 "
                                "contre le fées et les démons.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Scénarios uniques", title="Retour à clairval", chapter="Baston chez les Crânes-creux", numbering="4")
            ],
            'cost': Cost(value=12.0 * ccc['global']['cost']['cold-iron'] + 60.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'material': 'cold-iron',
            'special_property': ["DM: x2 (fées et démons)"],
            'flavor': [Flavor(ftype='cold-iron', count=1)],
        },
        'faucille-magique-en-argent': {
            'name': "Faucille magique, en argent",
            'base_item': lambda item: item.oid,
            'short_description': "Une magnifique faucille en argent gravée de runes druidiques.",
            'full_description': "Une magnifique faucille en argent gravée de runes druidiques. "
                                "Il s’agit d’une faucille magique +1 (DM de base 1d6) qui inflige "
                                "+1d6 DM contre les plantes.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Forêt Sombre", numbering="1"
                ),
            ],
            'cost': Cost(value=12.0 * ccc['global']['cost']['silver'],
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[Mod(mtype="+", count=1, target="magical")]
                ),
                critical=RangeSet([20])
            ),
            'material': 'silver',
            'special_property': ["DM: +1d6 contre les plantes"],
            'flavor': [Flavor(ftype='silver', count=1), Flavor(ftype='magical', count=1)],
        },
        'rapiere-elfique-+1-en-argent': {
            'name': "Rapière elfique +1, en argent",
            'base_item': lambda item: item.oid,
            'short_description': "Une rapière en argent, décorée de magnifiques entrelacs elfiques et d’une garde "
                                 "qui semble faite de dentelle d’acier (mais très solide).",
            'full_description': "Une rapière +1 en argent, décorée de magnifiques entrelacs elfiques et d’une garde "
                                "qui semble faite de dentelle d’acier (mais très solide). Cette arme inflige "
                                "1d6 dégâts qui sont doublé contre les lycanthropes. L'arme ignore également la RD "
                                "d'une telle créature.",
            'category': "quest",
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'cost': Cost(value=12.0 * ccc['global']['cost']['silver'] + 2000.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[Mod(mtype="+", count=1, target="magical")]
                ),
                critical=RangeSet([19,20])
            ),
            'material': 'silver',
            'special_property': ["DM: x2 (sensible à l'argent)", "RD: ignoré (sensible à l'agent)"],
            'flavor': [Flavor(ftype='silver', count=1), Flavor(ftype='magical', count=1)],
        },
        'baton-en-bois-+1-magique': {
            'name': "Bâton +1, en bois noir",
            'base_item': lambda item: item.oid,
            'short_description': "Un bâton magique en simple bois noir rehaussé de deux cercles d’or fin. Ce baton "
                                 "procure un bonus en attaque au contract, aux dégâts mais aussi en attaque magique.",
            'full_description': "Un bâton +1 (bonus en attaque au contact et aux DM, mais aussi en attaque magique) "
                                "en simple bois noir rehaussé de deux cercles d’or fin. Il inflige donc 1d4 +1 DM.",
            'category': "quest",
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'cost': Cost(value=3000.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['blunt'])],
                    other=[Mod(mtype="+", count=1, target="magical")]
                ),
                critical=RangeSet([20])
            ),
            'material': 'wood',
            'special_property': ["Attaque magique: +1"],
            'flavor': [Flavor(ftype='magical', count=1)],
        },
        'baton+2-de-defense': {
            'name': "Bâton +2, de défense",
            'base_item': lambda item: item.oid,
            'short_description': "Un bâton magique +2 en chêne. Ce bâton noueux "
                                 "procure également un bonus de défense.",
            'full_description': "Un bâton magique +2 (bonus en attaque au contact et aux DM) en chêne. Ce bâton noueux "
                                "procure également un bonus de DEF de +2. Il inflige donc 1d4 +2 DM.",
            'category': "quest",
            'magical_level': 2,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=9000.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                mod=2,
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['blunt'])],
                    other=[Mod(mtype="+", count=2, target="magical")]
                ),
                critical=RangeSet([20])
            ),
            'material': 'wood',
            'special_property': ["DEF: +2"],
            'flavor': [Flavor(ftype='magical', count=2)],
        },
        'baton-lance-+1': {
            'name': "Bâton-lance +1",
            'base_item': lambda item: item.oid,
            'short_description': "Un bâton-lance avec une lame en forme de feuille, une arme elfique utilisée "
                                 "par certains guerriers magiciens de ce peuple.",
            'full_description': "Un bâton-lance +1 avec une lame en forme de feuille, une arme elfique utilisée "
                                "par certains guerriers magiciens de ce peuple (DM 1d10 à 2 mains).",
            'category': "quest",
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'cost': Cost(value=3000.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=10, count=1, target=['blunt'])],
                    other=[Mod(mtype="+", count=1, target="magical")]
                ),
                critical=RangeSet([20])
            ),
            'material': 'wood',
            'flavor': [Flavor(ftype='magical', count=1)],
        },
        'hache-en-durium-de-urgashn': {
            'name': "Hâche en durium, d'Urgashn",
            'base_item': lambda item: item.oid,
            'short_description': "La hache en durium d'Urgashn est une arme de qualité qui permet de tailler en "
                                 "pièces même les plus gros durs à cuire.",
            'full_description': "La hache en durium d'Urgashn est une arme de qualité qui permet de tailler en "
                                 "pièces même les plus gros durs à cuire. Elle inflige 2d8 dégâts.",
            'category': "quest",
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'cost': Cost(value=32.0 * ccc['global']['cost']['durium'] + 70.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=3.5, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=8, count=2, target=['sharp'])],
                ),
                critical=RangeSet([20])
            ),
            'material': 'durium',
            'flavor': [Flavor(ftype='quality', count=1), Flavor(ftype='durium', count=1)],
        },
        'francisque+1-de-lancer': {
            'name': "Francisque +1, de lancer",
            'base_item': lambda item: item.oid,
            'short_description': "Cette hache peut être lancée et revient dans la main de "
                                 "son lanceur. Il peut alors ajouter son Mod. de FOR.",
            'full_description': "Cette hache peut être lancée à une portée de 20 mètres et elle "
                                "revient dans la main de son lanceur. Elle inflige 1d6 DM et le "
                                "personnage peut ajouter "
                                "son Mod. de FOR aux DM qu’il inflige lors d’une attaque à distance "
                                "avec cette arme.",
            'category': "quest",
            'range': Range(value=20, unit="m"),
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': Cost(value=8500,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.5, unit='Kg'),
            'hands': 1,
            'special_property': [
                "DM (distance) : +[FOR]",
                "Revient dans la main de son lanceur"],
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['sharp'])],
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=1)],
        },
        'epee-longue-en-durium-de-urgashn': {
            'name': "Épée longue en durium, d'Urgashn",
            'base_item': lambda item: item.oid,
            'short_description': "L'épée en durium d'Urgashn est une arme de qualité qui permet de tailler en "
                                 "pièces même les plus gros durs à cuire.",
            'full_description': "L'épée en durium d'Urgashn est une arme de qualité qui permet de tailler en "
                                "pièces même les plus gros durs à cuire. Elle inflige 1d10 dégâts.",
            'category': "quest",
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'cost': Cost(value=32.0 * ccc['global']['cost']['durium'] + 70.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=3.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=10, count=1, target=['punctured', 'sharp'])],
                ),
                critical=RangeSet([20])
            ),
            'material': 'durium',
            'flavor': [Flavor(ftype='quality', count=1), Flavor(ftype='durium', count=1)],
        },
        'rapiere-+2-de-parade': {
            'name': "Rapière de parade +2, d'Amarange le Bel",
            'base_item': lambda item: item.oid,
            'short_description': "Une rapière spécialement faite pour parer les coups.",
            'full_description': "Une rapière spécialement faite pour parer les coups qui apporte un bonus de +2 "
                                "en défense. Elle est magique et apporte un bonus de +2 en attaque et aux dégâts",
            'category': "quest",
            'magical_level': 4,
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=2,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[Mod(mtype="+", count=2, target="magical")]
                ),
                critical=RangeSet([19,20])
            ),
            'defense': [Mod(label="DEF", count=2, mtype="+")],
            'flavor': [Flavor(ftype='magical', count=2)],
        },
        'rapiere-+2-de-haute-dexterite': {
            'name': "Rapière +2, de haute dextérité",
            'base_item': lambda item: item.oid,
            'short_description': "Une rapière magique qui améliore la dextérité de son porteur.",
            'full_description': "Cette rapière magique de haute dextérité apporte un bonus de +2 a son Mod. de DEX. " 
                                "Elle est magique et apporte un bonus de +2 en attaque et aux dégâts",
            'category': "quest",
            'magical_level': 4,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=2,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[Mod(mtype="+", count=2, target="magical")]
                ),
                critical=RangeSet([19,20])
            ),
            'special_property': ["[DEX] : +2"],
            'flavor': [Flavor(ftype='magical', count=2)],
        },
        'dague-maudite': {
            'category': 'Bazar du bizarre',
            'base_item': 'dague-maudite',
            'name': "Dague maudite",
            'full_description': "Une arme blanche à simple ou double tranchant dont la pointe en forme de losange, "
                                "et de préférence symétrique, améliore le pouvoir de perforation. Cette arme à une "
                                "main inflige 1d4 dégâts. Cette dague possède une lame noire de conception spéciale "
                                "qui se casse dans la blessure en cas de critique. Le morceau libéré s'enfonce "
                                "dans les chairs de la victime en direction de ses organes vitaux et occasionne la "
                                "perte de 1 point de CON par heure. Retirer le fragment de lame demande de réussir "
                                "un test SAG de difficulté 20. Chaque échec provoquant la perte de 1d6 points de CON "
                                "supplémentaire. Ensuite les points sont récupérés au rythme de 1 par jour. Ce type "
                                "de dague est généralement accompagné de poison pour les assassinats, si la lame se "
                                "brise la virulence du poison est augmentée et la difficulté du test de CON "
                                "correspondant au poison est augmenté de +5. Une dague brisée devient inutilisable.",
            'short_description': "Dague dont la lame se casse (critique). Retirer le fragment (test SAG >= 20) "
                                 "permet de récupérer les points perdus (1 / jour). Chaque échec enlève 1d6 points "
                                 "(CON). Si la lame est empoisonnée et se brise: test contre le poison: +5.",
            'weight': Weight(value=0.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'cost': lambda item: Cost(value=1000, unit=ccc['global']['cost']['unit']).iso(),
            'special_property': ["-1 CON / heure (critique)",
                                 "Inutilisable si cassée"]
        },
        'epee-courte-assassin-orque-noir': {
            'name': "Épée courte, d'assassin",
            'base_item': 'epee-courte-assassin-orque-noir',
            'short_description': "Une épée courte spécialement conçue pour les assassins qui inflige des dégâts "
                                 "de poison supplémentaires.",
            'full_description': "Une épée courte spécialement conçue pour les assassins et inflige 1d6 dégâts. La "
                                "lame est en Kröntaâr, un métal corrompu qui provient du cratère de Krön, la "
                                "capitale des orques. Il se dissout dans les blessures et empoisonne le sang de "
                                "la victime en infligeant 1d6 dégâts de poison supplémentaires. Cette arme n’a "
                                "qu’un nombre d’usages limité. Après chaque combat, lancer un d6: sur un résultat "
                                "de 1 à 3, l’arme est trop abîmée pour être encore utilisée.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justice des elfes", chapter="Des ennemis partout", numbering="1"
                )
            ],
            'cost': lambda item: Cost(
                value=6 * ccc['global']['cost']['krontaar'] + 5.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp'])],
                    other=[Mod(mtype="+", die=6, count=1, target="poison")]
                ),
                critical=RangeSet([20])
            ),
            'material': 'krontaar'
        },
        'dague-garde-turquoise': {
            'name': "Dague +1, incrustée de turquoises",
            'base_item': lambda item: item.oid,
            'short_description': "Une superbe dague pourvue d’une garde incrustée de turquoises.",
            'full_description': "Une superbe dague pourvue d’une garde incrustée de turquoises. Elle bénéficie d'un "
                                "bonus d'attaque de +1 et inflige 1d4 +1 dégâts.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2"
                )
            ],
            'cost': Cost(value=2500,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured', 'sharp']),
                          Mod(mtype="+", count=1, target='magical')],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
        },
        'epee-elfique+2': {
            "magical_level": 2,
            'name': "Épée elfique +2",
            'base_item': 'epee-elfique+2',
            'short_description': "Une épée de facture elfique qui permet d'utiliser son bonus de dextérité en "
                                 "attaque ou aux dégâts.",
            'full_description': "Une épée de facture elfique qui possède un bonus à l'attaque de +2 et inflique "
                                "1d8 +2 dégâts. Elle permet en outre d'utiliser son bonus de dextérité en "
                                "attaque ou aux dégâts.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justice des elfes", chapter="Le procès", numbering="3"
                )
            ],
            'cost': lambda item: Cost(
                value=8500,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=2,
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['punctured', 'sharp']),
                          Mod(mtype="+", count=2, target="magical")],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=2)],
            'special_property': ["Attaque ou DM: +[DEX]"]
        },
        'cimeterre-large': {
            'name': "Cimeterre large",
            'base_item': 'cimeterre',
            'short_description': "Un cimeterre est un type de sabre lourd avec une lame courbée.",
            'full_description': "Un cimeterre est un type de sabre lourd avec une lame courbée. Avec sa "
                                "large lame celui-ci inflique 1d8 dégâts.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="Voyage", numbering="1"
                ),
            ],
            'cost': lambda item: Cost(
                value=12,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            )
        },
        'faux': {
            'name': "Faux",
            'base_item': 'faux',
            'short_description': "La faux est formée d'une longue lame effilée et arquée, fixée "
                                 "perpendiculairement sur un manche en bois ou en métal, relativement "
                                 "long.",
            'full_description': "La faux est formée d'une longue lame effilée et arquée, fixée "
                                "sur un manche en bois ou en métal, relativement "
                                "long. Cette faux inflique 1d12 dégâts. Il faut au moins 12 en "
                                "FOR pour manier cette faux.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="Voyage", numbering="1"
                ),
            ],
            'cost': Cost(
                value=10,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=4.0, unit='Kg'),
            'hands': 2,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=12, count=1, target=['punctured', 'sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=3)],
            'special_property': ["Nécessite: FOR > 12"]
        },
        'epee-boutetroll': {
            "magical_level": 2,
            'name': "Boutetroll",
            'base_item': 'epee-boutetroll',
            'short_description': "Cette magnifique épée courte en bronze ressemble à un glaive celtique.",
            'full_description': "Cette magnifique épée courte en bronze ressemble à un glaive celtique. Elle "
                                "possède un bonus à l'attaque de +2 et inflique 1d6 +2 dégâts.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': lambda item: Cost(
                value=8000,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=2,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp']),
                          Mod(mtype="+", count=2, target="magical")],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=2)],
        },
        'epee-boutetroll-kelorn': {
            "magical_level": 2,
            'name': "Boutetroll",
            'base_item': 'epee-boutetroll',
            'short_description': "Cette magnifique épée courte en bronze ressemble à un glaive celtique. Elle "
                                 "s’enflamme si le mot de commande « Kelorn » est prononcé.",
            'full_description': "Cette magnifique épée courte en bronze ressemble à un glaive celtique. Elle possède "
                                "un bonus à l'attaque de +2 et inflique 1d6 +2 dégâts. Elle s’enflamme si le mot de "
                                "commande « Kelorn » (« brûle » en elfe sombre) est prononcé et inflige alors 1d6 DM "
                                "de feu supplémenantaires.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(
                value=32000,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=1.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=2,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['punctured', 'sharp']),
                          Mod(mtype="+", count=2, target="magical")],
                    other=[Mod(mtype="+", count=1, die=6, target="fire", limitation="Nécessite le mot de commande")]
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=2),Flavor(ftype='fire', count=1)],
        },
        'masse-serpent': {
            'name': "Masse serpent",
            'base_item': lambda item: item.oid,
            'short_description': "Cette masse serpent inocule du poison à sa victime à chaque attaque.",
            'full_description': "Cette masse serpent inocule du poison à sa victime à chaque attaque. "
                                "Elle doit faire un test de CON difficulté 12 ou sombrer dans "
                                "l’inconscience immédiatement pour une durée de 1d6 minutes. La masse "
                                "serpent ne prend vie qu’entre les mains d’une prêtresse de Maëdra.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': lambda item: Cost(
                value=100,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=2.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=2,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['blunt'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'special_property': [
                "Test CON < 12: Inconscient",
                "Utilisable: Prêtresse de Maëdra"
            ]
        },
        'masse-destruction-des-morts': {
            'name': "Masse +2, de destruction des morts",
            'base_item': lambda item: item.oid,
            'short_description': "Cette masse magique semble annimée d'une énergie qui se transmets à son "
                                 "porteur lui permettant de faire des dégâts supplémentaires.",
            'full_description': "Cette masse magique semble annimée d'une énergie qui se transmets à son "
                                "porteur lui permettant de faire des dégâts supplémentaires. Elle possede "
                                "un bonus à l'attaque au contact de +2 et inflige 2d6 DM.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=20000,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=2.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=2,
                damages=Damage(
                    base=[Mod(die=6, count=2, target=['blunt'])],
                    other=[Mod(count=2, target='magical', mtype="+")]
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=2)],
            "magical_level": 2,
        },
        'etoile-du-matin+3-de-feu': {
            'name': "Étoile du matin +3, de feu",
            'base_item': lambda item: item.oid,
            'short_description': "L'étoile du matin est une masse d'arme particulière constituée d'une masse lourde, "
                                "présentant généralement des aspérités ou des lames Cette arme est magique avec un "
                                "bonus de +3. Cette arme fait des dégâts supplémentaires de feu.",
            'full_description': "L'étoile du matin est une masse d'arme particulière constituée d'une masse lourde, "
                                "présentant généralement des aspérités ou des lames, accrochée au bout d'un bâton "
                                "plus ou moins long. Elle s'utilise à une main et inflige 1d6 dégâts. Cette arme "
                                "est magique et offre un bonus de +3 en attaque et aux dégats. Cette arme fait des "
                                "dégâts supplémentaires de +1d6 DM de feu.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=50000,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=2.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=3,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['blunt'])],
                    other=[
                        Mod(count=3, target=['magical'], mtype="+"),
                        Mod(die=6, count=1, target='fire', mtype="+"),
                    ]
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=3),Flavor(ftype='fire', count=2)],
            "magical_level": 5,
        },
        'dague-sacrificielle+1': {
            'name': "Dague sacrificielle +1",
            'base_item': "dague-sacrificielle",
            'short_description': "Une dague dont la garde en forme de tête de mort enserre une lame forgée dans "
                                 "un métal noir.",
            'full_description': "Une dague dont la garde en forme de tête de mort enserre une lame forgée dans un "
                                "métal noir. Elle n’octroie aucun bonus magique, mais toute victime d’une blessure "
                                "par cette lame doit réussir un test de CON difficulté 10 ou être Affaibli pendant "
                                "un tour (d12 à tous les tests). Cette dague est clairement d'origine maléfique.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(value=12.0 * ccc['global']['cost']['cold-iron'] + 60.0 + 2000.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=4, count=1, target=['punctured', 'sharp']),
                         Mod(mtype="+", count=1, target="magical")],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=1)],
            "magical_level": 1,
            'material': "gorndar",
            'special_property': ["Test CON <= 10 (si attaque réussie): Affaibli (d12) pendant 1 tour"],
            'flavor': [Flavor(ftype="gorndar", count=1)],
            
        },
        'masse-sanglante+1': {
            'name': "Masse sanglante +1",
            "magical_level": 1,
            'base_item': 'masse-sanglante',
            'short_description': "Cette masse +1 est composée d’un manche de bois noir et d’une tête de mort "
                                "en argent courroné d'un cercle de fer aux pointes acérées.",
            'full_description': "Cette masse +1 est composée d’un manche de bois noir et d’une tête de mort "
                                "en argent. Le crâne est couronné d’un cercle de fer aux pointes acérées. Les "
                                "blessures causées par les pointes produisent un effet de saignement qui "
                                "inflige +1d6 DM de saignement pendant 3 tours. Les DM de saignement de "
                                "plusieurs blessures ne sont pas cumulables.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=2.0, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                mod=1,
                damages=Damage(
                    base=[Mod(die=6, count=1, target=['blunt','punctured']),
                          Mod(mtype="+", count=1, target="magical")],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'flavor': [Flavor(ftype='magical', count=1)],
            'special_property': [
                "Saignement: 1d6 pendant 3 tr",
                "DM saignement non cumulable"
            ]
        },
        'masse-de-fantassin+1': {
            'category': 'quest',
            'base_item': 'masse-fantassin',
            'name': "Masse +1, de fantassin",
            'full_description': "La masse de fantassin est une arme contondante constituée d'une masse lourde "
                                "accrochée au bout d'un long manche permettant de l'utiliser à cheval. Elle "
                                "s'utilise à deux main et inflige 1d8 +1 dégâts mais avec un malus à l'attaque "
                                "de -1 à cause de son long manche. Utilisée sur un cheval, après une action "
                                "de mouvement, cette attaque est sans malus et inflige +1d8 dégats "
                                "supplémentaires.",
            'short_description': "La masse de fantassin est constituée d'un long manche terminé par une lourde "
                                 "masse. Elle montre son potentiel lors de charges (mouvement + attaque) "
                                 "à cheval.",
            'weight': cof.properties.Weight(value=3.0, unit='Kg'),
            'hands': 3,
            'attack': Attack(
                atype='melee',
                mod=-1,
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['blunt'])],
                    other=[Mod(mtype="+", count=1, target="magical" )]
                ),
                critical=RangeSet([20])
            ),
            'cost': Cost(
                value=2000,
                unit=ccc['global']['cost']['unit']).iso(),
            'flavor': [Flavor(ftype='magical', count=1)],
            'special_property': [
                "Charge cheval: une seule main",
                "Charge cheval: pas de malus",
                "Charge cheval: +1d8 DM"
                ]
        },
        'tranchegrand': {
            "magical_level": 2,
            'category': 'quest',
            'base_item': 'tranchegrand',
            'name': "Tranchegrand",
            'full_description': "Une magnifique hache +2 à double tranchant de facture naine, décorée de runes. "
                                "Tranchegrand est une faucheuse de géants : elle inflige +1d6 DM contre les "
                                "créatures de taille grande et +2d6 contre celles de taille énorme ou supérieure!",
            'short_description': "Une magnifique hache à double tranchant de facture naine, décorée de runes "
                                 "spécialement conçue pour tuer de grandes créatures.",
            'weight': cof.properties.Weight(value=3.5, unit='Kg'),
            'hands': 1,
            'attack': Attack(
                atype='melee',
                damages=Damage(
                    base=[Mod(die=8, count=1, target=['sharp'])],
                    other=[]
                ),
                critical=RangeSet([20])
            ),
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'flavor': [Flavor(ftype='magical', count=2)],
            'special_property': [
                "Grande créature: +1d6 DM",
                "Énorme créature: +2d6 DM"]
        },
        
    },
    "Boots": {
        'boots-sprint': {
            "capacity": "http://co-drs.org/capacites/sprint/",
            "name": "Bottes de vitesse",
            "short_description": "Une fois par combat, la personne qui porte ces bottes peut effectuer un "
                                 "déplacement supplémentaire gratuit à n’importe quel moment du tour.",
            "full_description": "Une fois par combat, la personne qui porte ces bottes peut effectuer un déplacement "
                                "supplémentaire gratuit de 20 mètres à n’importe quel moment du tour.",
            "category": "Magique",
            "magical_level": lambda item: item.way_rank,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'boots-course-des-airs': {
            "capacity": "http://co-drs.org/capacites/course-des-airs/",
            "name": "Bottes de course, dans les airs",
            "short_description": "La personne qui porte ces bottes défie les lois de la pesanteur et peut se "
                                 "déplacer sur des surfaces qui ne devraient pas supporter son poids. Il peut "
                                 "se déplacer sur l’eau, la neige, le feuillage des arbres ou courir sur un mur "
                                 "vertical. Il doit commencer et terminer son déplacement sur une surface normale.",
            "full_description": "La personne qui porte ces bottes défie les lois de la pesanteur et peut se "
                                "déplacer sur des surfaces qui ne devraient pas supporter son poids. Il peut "
                                "se déplacer sur l’eau, la neige, le feuillage des arbres ou courir sur un mur "
                                "vertical. Il doit commencer et terminer son déplacement sur une surface normale.",
            'category': "quest",
            "magical_level": lambda item: item.way_rank,
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'boots-marche-des-plans': {
            "capacity": "http://co-drs.org/capacites/marche-des-plans/",
            "name": "Bottes de sept lieues",
            "short_description": "La personne qui porte ces bottes se déplace dans une dimension entre les plans "
                                "d’existence où le paysage défile à toute vitesse. Le lieu de "
                                "sortie n’est cependant pas très précis.",
            "full_description": "La personne qui porte ces bottes peut passer dans une dimension entre les plans "
                                "d’existence où le temps et l’espace sont déformés. Il se déplace dans une sorte "
                                "de brouillard gris où le paysage défile à toute vitesse une fois par jour et "
                                "pour une durée maximale de [3 + Mod. de SAG] tours. Pour chaque tour "
                                "de « Marche des plans », il se déplace en réalité de 10 km. Le lieu de "
                                "sortie n’est cependant pas très précis et le MJ doit déterminer une position "
                                "au hasard autour du point visé (à 1d6 km près).",
            'category': "quest",
            "magical_level": lambda item: item.way_rank,
           'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'bottes-elfique': {
            'name': "Bottes elfique",
            'base_item': lambda item: item.oid,
            'short_description': "Bottes elfiques.",
            'full_description': "Bottes elfiques.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Le procès", numbering="3")
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.2, unit='Kg'),
        },
        'bottes-elfe': {
            'name': "Bottes d'elfe",
            'base_item': 'bottes-elfique',
            'short_description': "Bottes d'elfe.",
            'full_description': "Bottes d'elfe qui apportent un bonus de plus 5 en discretion.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'flavor': [Flavor(ftype='magical', count=1)],
            "magical_level": 1,
            'cost': Cost(value=2000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.2, unit='Kg'),
            'special_property': [
                "Discretion: +5"
            ],
        },
    },
    "Helmet": {
        'helmet-murmure-dans-le-vent': {
            'capacity': "http://co-drs.org/capacites/murmures-dans-le-vent/",
            'short_description': "Ce casque à nasal permet de chuchoter un message d’une dizaine de mots "
                                 "qui voyage jusqu’à son destinataire. Elle doit connaître la cible ou la voir et "
                                 "peut entendre sa réponse immédiatement.",
            'full_description': "La personne qui porte ce casque à nasal chuchote un message d’une dizaine de mots "
                                "qui voyage jusqu’à son destinataire. Elle peut entendre sa réponse immédiatement. "
                                "La portée est de 100m par rang dans la voie et le personnage doit connaître la "
                                "cible ou la voir. Ce casque offre une RD de 6 lorsque l'on subit un coup critique. "
                                "Le port de de ce casque inflige une pénalité de -6 a tous les tests de SAG destinés "
                                "à simuler la perception, détecter un bruit ou une créature cachée, échaper à "
                                "une embuscade, etc.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'skill': [
                Mod(label="Test", target="view", count=6, mtype="-"),
                Mod(label="Test", target="hearing", count=6, mtype="-"),
                Mod(label="Test", target="embuscade", count=6, mtype="-")
                ],
            'defense': [Mod(label="RD", target="rd", count=6, limitation="Seulement contre les critiques")],
            'weight': Weight(value=0.5, unit='Kg'),
        },
        'bandeau-intelligence': {
            'name': lambda item: f"Bandeau, d'intelligence +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"[INT]: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Ce bandeau apporte un bonus au Mod. d'intelligence de la personne qui la porte.",
            'full_description': lambda item: f"Ce bandeau robe apporte un bonus de +{item.magical_level} au Mod. "
                                             "d'intelligence de la personne qui la porte.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'serre-tete-sagesse': {
            'name': lambda item: f"Serre-tête, de sagesse +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"[SAG]: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Ce serre-tête apporte un bonus au Mod. de sagesse de la personne qui la porte.",
            'full_description': lambda item: f"Ce serre-tête robe apporte un bonus de +{item.magical_level} au Mod. "
                                             "de sagesse de la personne qui la porte.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'serre-tete-en-or-parnesir': {
            'name': "Serre-Tête en or",
            'short_description': "Un magnifique serre-tête en or blanc représentant un aigle. Le mot Parnesir "
                                 "est gravé à l’intérieur.",
            'full_description': "Un magnifique serre-tête en or blanc représentant un aigle. Le mot Parnesir "
                                "est gravé à l’intérieur et il faut le faut prononcer pour activer ses pouvoirs. "
                                "Une fois activé et porté, il confère un bonus de +5 aux tests de perception basés "
                                "sur la SAG et un bonus de +2 en attaque et +1 aux DM quand on tire à l’arc en le "
                                "portant. Ces bonus sont cumulables avec d’autres bonus éventuels.",
            'category': "quest",
            'skill': [
                Mod(label="Test", target="perception", count=5, mtype="+")
                ],
            'special_property': [
                "Attaque: +2 (arc)",
                "DM: +2 (arc)",
                "Bonus cumulables d'autres"],
            'weight': Weight(value=0.1, unit='Kg'),
            'cost': lambda item: Cost(
                value=15000,
                unit=ccc['global']['cost']['unit']).iso(),
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
        },
        'heavy-helmet-silver': {
            'base_item': lambda item: f"{item.oid}",
            'flavor': [Flavor(ftype='silver', count=1)],
            'category': 'quest',
            'skill': [
                Mod(label="Test", target="view", count=8, mtype="-"), 
                Mod(label="Test", target="hearing", count=8, mtype="-"),
                Mod(label="Test", target="embuscade", count=8, mtype="-")
                ],
            'defense': [Mod(label="RD", target="rd", count=8, limitation="Seulement contre les critiques")],
            'magical_level': 0,
            'name': "Heaume sculpté, en argent",
            'short_description': "Un heaume sculpté et rehaussé d’argent qui protègera énormément la tête de "
                                 "l'aventurier mais réduira sa perception quasiment à néant.",
            'full_description': "Un heaume magnifiquement sculpté et rehaussé d’argent. Le heaume est l'élément "
                                "indispensable pour compléter une armure de demi-plaques. "
                                "Il offre une RD de 8 lorsque l'on subit un coup critique. Le port de de ce casque "
                                "inflige une pénalité de -8 a tous les tests de SAG destinés à simuler la perception, "
                                "détecter un bruit ou une créature cachée, échaper à une embuscade, etc.",
            'cost': lambda item: cof.properties.Cost(value=300.0,
                                                     unit=ccc['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=2.0, unit='Kg')
        },
        'heaume-de-vision': {
            'base_item': lambda item: f"{item.oid}",
            'category': 'quest',
           'skill': [
                Mod(label="Test", target="view", count=5, mtype="+"), 
                Mod(label="Test", target="hearing", count=5, mtype="+")
                ],
            'magical_level': 0,
            'name': "Heaume, de vision",
            'short_description': "Ce haume de vision, qui porte le symbole du Roi-Sorcier, permet de voir "
                                 "dans le noir la fumée ou la brume et donne un bonus aux tests de détection. "
                                 "Son porteur peut utiliser Détection de l’invisibilité et Clairvoyance 3 "
                                 "fois par jour.",
            'full_description': "L'heaume de vision accorde à son porteur la vision dans le noir (50 mètres) "
                                "et à travers toute sorte de fumée ou de brume et un bonus de +5 à tous les tests de "
                                "détection. Son porteur peut utiliser Détection de l’invisibilité et Clairvoyance "
                                "trois fois par jour. "
                                "Cet objet porte le symbole du Roi-Sorcier.",
            'cost': lambda item: cof.properties.Cost(value=300.0,
                                                     unit=ccc['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            "area": Area(value="50", unit="m"),
            'special_property': [
                "Vision dans le noir, brume et fumée"
            ],
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
        },
        'heaume-maudit-de-vision': {
            'base_item': "heaume-de-vision",
            'category': 'quest',
            'skill': [
                Mod(label="Test", target="view", count=5, mtype="+"), 
                Mod(label="Test", target="hearing", count=5, mtype="+")
                ],
            'magical_level': 0,
            'name': "Heaume maudit, de vision",
            'short_description': "Ce haume maudit de vision, qui porte le symbole du Roi-Sorcier, permet de voir "
                                 "dans le noir la fumée ou la brume et "
                                 "donne un bonus aux tests de détection. Son porteur peut utiliser Détection de "
                                 "l’invisibilité et Clairvoyance 3 fois par jour. Il pervertit "
                                 "progressivement l’esprit déformant la réalité de ce qu’il perçoit pour le rendre "
                                 "maléfique.",
            'full_description': "L'heaume maudit de vision accorde à son porteur la vision dans le noir (50 mètres) "
                                "et à travers toute sorte de fumée ou de brume et un bonus de +5 à tous les tests de "
                                "détection. Son porteur peut utiliser Détection de l’invisibilité et Clairvoyance "
                                "trois fois par jour. Le heaume pervertit progressivement l’esprit du porteur en "
                                "déformant la réalité de ce qu’il perçoit (paroles, vision) pour le rendre maléfique. "
                                "Cet objet porte le symbole du Roi-Sorcier.",
            'cost': lambda item: cof.properties.Cost(value=300.0,
                                                     unit=ccc['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=2.0, unit='Kg'),
            "area": Area(value="50", unit="m"),
            'special_property': [
                "Vision dans le noir, brume et fumée"
            ],
             'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
        },
    },
    "Robe": {
        'robe-charisme': {
            'name': lambda item: f"Robe, de charisme +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"[CHA]: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Cete robe apporte un bonus au Mod. de charisme de la personne qui la porte.",
            'full_description': lambda item: f"Cete robe apporte un bonus de +{item.magical_level} au Mod. de "
                                             "charisme de la personne qui la porte.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
        },
    },
    "Amulet": {
        'amulet-charme': {
            'category': "quest",
            'base_item': lambda item: item.oid,
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Voyage", numbering="1")
            ],
            'name': "Amulette de charme, d'Amarange le Bel",
            'short_description': "Une amulette de charme qui donne à son porteur un bonus pour tous les "
                                 "sorts de charme.",
            'full_description': "Une amulette de charme qui donne à son porteur un bonus pour tous les "
                                "sorts de charme.",
            'cost': Cost(value=500.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'material': 'gold',
            'special_property': ["Attaque: +5 (sort de charme)"]
        },
        'amulet-constitution': {
            'name': lambda item: f"Amulette, de constitution +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"[CON]: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Cete amulette apporte un bonus au Mod. de constitution de la personne qui la porte.",
            'full_description': lambda item: f"Cete amulette apporte un bonus de +{item.magical_level} au Mod. de "
                                             "constitution de la personne qui la porte.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'collier-de-charisme': {
            'base_item': lambda item: f"{item.oid}",
            'name': "Collier de charisme +1",
            'special_property': ["[CHA]: +1"],
            'flavor': [Flavor(ftype='magical', count=1)],
            'short_description': "Un magnifique médaillon d’argent décoré d’un rubis. Ce collier apporte un bonus "
                                 "de +1 au Mod. de Charisme.",
            'full_description': "Un magnifique médaillon d’argent décoré d’un rubis. Ce collier apporte un bonus "
                                "de +1 au Mod. de Charisme.",
            'category': "quest",
            'magical_level': 2,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'talisman-de-protection-contre-le-poison': {
            'base_item': lambda item: f"{item.oid}",
            'name': "Talisman de protection, contre le poison",
            'special_property': ["Immunité: poison"],
            'short_description': "De ce manifique talismant semble se dégager une aura protectrice et bienveillante. "
                                 "Ce talimant procure une immunité totale contre tout type de poison.",
            'full_description': "De ce manifique talismant semble se dégager une aura protectrice et bienveillante. "
                                "Ce talimant procure une immunité totale contre tout type de poison.",
            'category': "quest",
            'cost': lambda item: Cost(
                value=8000,
                unit=ccc['global']['cost']['unit']).iso(),
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'weight': Weight(value=0.1, unit='Kg'),
        },
         'pendentif-aigle': {
            'name': "Pendentif, représentant un aigle",
            'special_property': [
                "Soigne : 1d8 PV + niveau"
                "Utilisable: 3 fois par jour"],
            'short_description': "Ce pendentif représentant un aigle est un fétiche de guérison qui donne la capacité "
                                ": Soins légers.",
            'full_description': "Ce pendentif représentant un aigle est un fétiche de guérison qui donne la capacité"
                                "de rang 1 de la voie du prêtre : Soins légers. Cette capacité est utilisable "
                                "3 fois par jour.",
            'category': "quest",
            'cost': lambda item: Cost(
                value=8000,
                unit=ccc['global']['cost']['unit']).iso(),
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'weight': Weight(value=0.1, unit='Kg'),
        },
    },
    "Gloves": {
        'gloves-dexterite': {
            'name': lambda item: f"Gantelets, de dextérité +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"[DEX]: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Ces gantelets apportent un bonus au Mod. de dextérité de la personne qui les porte.",
            'full_description': lambda item: f"Ces gantelets apportent un bonus de +{item.magical_level} au Mod. de "
                                             "dextérité de la personne qui les porte.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),

        },
        'gloves-force': {
            'name': lambda item: f"Gantelets, de force +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"[FOR]: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Ces gantelets apportent un bonus au Mod. de force de la personne qui les porte.",
            'full_description': lambda item: f"Ces gantelets apportent un bonus de +{item.magical_level} au Mod. de "
                                             "force de la personne qui les porte.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),

        },
        'gloves-einistar': {
            'name': "L’Einistar, le gant de lumière",
            'base_item': lambda item: f"{item.oid}",
            'special_property': [ 
                "Test de Caract. (tous): +2",
                "Permanent: -10% PV (total)"
            ],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level),Flavor(ftype='mythral', count=1)],
            'short_description': "L’Einistar est aussi nommé le Gardien de la cité de Lune et d’Or (Anathazerïn). "
                                 "L’Einistar comporte des sortes de bagues au niveau des phalanges et "
                                "chacune d’entre elles porte une rune. L’Einistar s’adapte à tout type de main droite.",
            'full_description': "L’Einistar, aussi nommé le Gardien de la cité de Lune et d’Or (Anathazerïn), est un gant en "
                                "maille de mithral remontant jusqu’à moitié de l’avant-bras. Le métal dont il est fait renvoie "
                                "des reflets nacrés quand il est en pleine lumière. L’Einistar comporte des sortes de "
                                "bagues au niveau des phalanges. Assez discrètes, elles sont également en mithral et "
                                "chacune d’entre elles porte une rune. L’Einistar s’adapte à tout type de main droite.",
            'magical_level': 4,
            'category': "quest",
            'defense': [Mod(label="DEF", mtype="+", count=2)],
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=(item.magical_level +6) * (item.magical_level +6) * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'material': "mythral",

        },
        'gloves-einistar-mauvais': {
            'name': "L’Einistar, le gant de lumière",
            'base_item': "gloves-einistar",
            'special_property': [ "Permanent: affaibli"
            ],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level),Flavor(ftype='mythral', count=1)],
            'short_description': "L’Einistar est aussi nommé le Gardien de la cité de Lune et d’Or (Anathazerïn). "
                                 "L’Einistar comporte des sortes de bagues au niveau des phalanges et "
                                "chacune d’entre elles porte une rune. L’Einistar s’adapte à tout type de main droite.",
            'full_description': "L’Einistar, aussi nommé le Gardien de la cité de Lune et d’Or (Anathazerïn), est un gant en "
                                "maille de mithral remontant jusqu’à moitié de l’avant-bras. Le métal dont il est fait renvoie "
                                "des reflets nacrés quand il est en pleine lumière. L’Einistar comporte des sortes de "
                                "bagues au niveau des phalanges. Assez discrètes, elles sont également en mithral et "
                                "chacune d’entre elles porte une rune. L’Einistar s’adapte à tout type de main droite.",
            'magical_level': 4,
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'cost': lambda item: Cost(
                value=(item.magical_level +6) * (item.magical_level +6) * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
            'material': "mythral",

        },
    },
    "Belt": {
        'belt-force': {
            'name': lambda item: f"Ceinture de force +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"[FOR]: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Cete ceinture apporte un bonus au Mod. de force de la personne qui la porte.",
            'full_description': lambda item: f"Cete ceinture apporte un bonus de +{item.magical_level} au Mod. de "
                                             "force de la personne qui la porte.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
        'belt-force-geant': {
            'name': "Ceinture de force de géant",
            'base_item': lambda item: f"{item.oid}",
            'special_property': ["[FOR]: +2"],
            'flavor': [Flavor(ftype='magical', count=2)],
            'short_description': "Cete ceinture en bronze décorée d’un large motif de taureau aux yeux "
                                "de rubis apporte un bonus au Mod. de force de la personne qui la porte.",
            'full_description': "Cete ceinture en bronze décorée d’un large motif de taureau aux yeux "
                                "de rubis apporte un bonus de +2 au Mod. de "
                                "force de la personne qui la porte.",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'category': "quest",
            'magical_level': 2,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.1, unit='Kg'),
        },
    },
    "Ring": {
        'protective-gold-ring-+1': {
            'defense': [Mod(label="DEF", target="", mtype="+", count=1)],
            'category': "quest",
            'base_item': lambda item: item.oid,
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Le Sanctuaire", chapter="Le Sanctuaire de Trenner", numbering="3"
                )
            ],
            'name': "Anneau de protection +1, en or",
            'short_description': "Un anneau de protection en or.",
            'full_description': "Un anneau de protection en or qui procure un bonus de +1 en DEF. Le bonus de "
                                "l'anneau de protection ne se cumule pas avec le bonus des capes de protection.",
            'cost': Cost(value=2500.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'material': 'gold',
        },
        'protective-elements': {
            'defense': [
                Mod(label="RD", target="fire", count=5),
                Mod(label="RD", target="lightning", count=5),
                Mod(label="RD", target="coldness", count=5),
                Mod(label="RD", target="acid", count=5),
            ],
            'category': "quest",
            'base_item': lambda item: item.oid,
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'name': "Anneau de résistance, aux éléments",
            'short_description': "Un anneau de résistance aux éléments qui réduit tous les DM de feu, d’électricité, de froid ou d’acide.",
            'full_description': "Un anneau de résistance aux éléments qui réduit de 5 points tous les DM de feu, d’électricité, de froid ou d’acide.",
            'cost': Cost(value=32000.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'puissance-des-arcanes': {
            'category': "quest",
            'base_item': lambda item: item.oid,
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'name': "Anneau de puissance, des arcanes",
            'short_description': "Cet anneau de puissance des arcanes double les effets de sorts de rang 1 et 2, 3 fois par jours.",
            'full_description': "Un large anneau d’or couvert de runes. Cet anneau de puissance des arcanes de rang 1 et 2 double la durée "
                                "ou les DM ou les soins produits par les sorts de rang 1 ou 2, trois fois par jour pour chaque rang)",
            'cost': Cost(value=18000.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'special_property': [
                "Sort: rang 1 ou 2",
                "DM x2 ou soin x2 ou durée x2",
                "Utilisation: 3 fois par jour"
            ]
        },
        'puissance-des-arcanes-forgesort': {
            'category': "quest",
            'base_item': lambda item: item.oid,
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'name': "Anneau de préparation, des arcanes",
            'short_description': "Cet anneau de préparation des arcanes double les effets de 3 potions préparées  pour chaque rang 1 et 2.",
            'full_description': "Un large anneau d’or couvert de runes. Cet anneau de préparation des arcanes permet de préparer 3 "
                                "potions pour les rangs 1 et 2 dont la durée ou les DM ou les soins produits sont doublés.",
            'cost': Cost(value=18000.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'special_property': [
                "Potion: rang 1 ou 2",
                "DM x2 ou soin x2 ou durée x2",
                "Quantité: 3 potions / rang"
            ]
        },
        'anneau-de-marche-sur-l-eau': {
            'special_property': ["Permanent: Marcher sur l'eau"],
            'category': "quest",
            'base_item': lambda item: item.oid,
            'magical_level': 1,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'name': "Anneau de marche, sur l'eau",
            'short_description': "Un anneau qui permet de marcher sur l'eau.",
            'full_description': "Un anneau qui permet de marcher sur l'eau.",
            'cost': Cost(value=2500.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'bague-en-agate-de-manahim': {
            'category': "quest",
            'base_item': lambda item: item.oid,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les Faux Monnayeurs", chapter="Voyage", numbering="2"
                ),
            ],
            'name': "Bague en agate, de Manahim",
            'short_description': "Une bague en agate représentant un serpent qui se mord la queue.",
            'full_description': "Une bague en agate représentant un serpent qui se mord la queue.",
            'cost': Cost(value=50.0,
                         unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg')
        },
        'ring-sous-tension': {
            "capacity": "http://co-drs.org/capacites/sous-tension/",
            "name": "Anneau en fer, de poigne électrique",
            "short_description": "Cet anneau est chargé d’énergie électrique. "
                                 "Toute créature qui vous blesse ou vous touche reçoit une décharge "
                                 "provoquant 1d6 DM.",
            "full_description": "La personne qui utilise le pouvoir de cet anneau (maximum 3 fois par jour)"
                                "se charge d’énergie électrique pour "
                                "[5 + Mod. de CHA] tours. Toute créature qui la blesse ou la touche "
                                "reçoit une décharge infligeant 1d6 DM. Elle peut également délivrer "
                                "une décharge électrique (attaque magique, portée 10 m) infligeant "
                                "[1d6 + Mod. de CHA] DM.",
            'category': "quest",
            "magical_level": lambda item: item.way_rank,
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'special_property': ["Utilisation: 3 fois par jour"]
        },
        'ring-face-orque': {
            "name": "Anneau de face d'orque",
            "short_description": "Cet anneau permet de se transformer en orque pour une durée limitée. On ne peut pas "
                                 "retirer l'anneau avant le temps imparti.",
            "full_description": "Cet anneau permet de se transformer en orque pour une durée de 1d6 heure à chaque "
                                "fois qu’il est enfilé. La personne garde toutes ses Carac. sauf le CHA dont le "
                                "Mod. subit une pénalité de -2 pour toutes les autres races que les orques. "
                                "Le PJ parle l’orque, mais ne sait plus parler le commun. On ne peut pas retirer "
                                "l'anneau avant le temps imparti.",
            'category': "quest",
            "magical_level": 2,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'cost': lambda item: Cost(
                value=1000,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'duration': Duration(unit="h", value="1d6"),
            'special_property': ["[CHA]: -2 (contre autre que orque)",
                                 "Language: orque",
                                 "Ne peut plus parler le commun"]
        },
        'ring-haute-magie': {
            "name": "Anneau de haute magie",
            "short_description": "Ce simple anneau d’argent donne un bonus de à tous les tests d’attaque magique "
                                 "et augmente les DM de tous les sorts.",
            "full_description": "Ce simple anneau d’argent donne un bonus de +2 à tous les tests d’attaque magique "
                                "et augmente de +1d6 les DM de tous les sorts. Ce bonus est particulièrement "
                                "déterminant lorsqu’il s’agit d’un sort qui inflige habituellement de faibles "
                                "DM (comme projectile magique, par exemple).",
            'category': "quest",
            "magical_level": 2,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                )
            ],
            'cost': lambda item: Cost(
                value=18000,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'special_property': [
                "Attaque magique: +2",
                "Sorts: +1d6 DM"
            ]
        },
        'ring-sceau-de-feu': {
            "name": "Sceau de feu",
            "short_description": "Cet anneau d’or décoré d’un beau rubis permet d’apposer une rune de feu "
                                 "qui se ferme.",
            "full_description": "Cet anneau d’or décoré d’un beau rubis permet d’apposer une rune de feu "
                                "une fois par jour sur un objet qui se ferme (coffre, porte) pour une "
                                "durée de 24 eures. Un test de SAG (trouver les pièges) difficulté 15 est "
                                "nécessaire pour remarquer la rune rouge sur l'objet. S’il est ouvert, la "
                                "rune explose et inflige 4d6 DM de Feu dans un rayon de 3 mètres. Un "
                                "test de DEX difficulté 15 permet de diviser les DM par 2.",
            'category': "quest",
            "magical_level": 2,
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            "duration": Duration(value="24", unit="h"),
            "area": Duration(value="3", unit="m"),
            'cost': Cost(
                value=500,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            'special_property': [
                "Detection rune: test SAG >= 15",
                "Ouverture : 4d6 DM de feu",
                "Test DEX >= 15 : DM / 2"
            ]
        },
    },
    "Shield": {
        'bouclier-de-protection-feu-de-karoom': {
            'name': "Bouclier de protection, de Karoom",
            'base_item': lambda item: item.oid,
            'short_description': "Un bouclier qui porte le symbole de Thürdim (Arshran) et protège du feu.",
            'full_description': "Un bouclier qui porte le symbole de Thürdim (Arshran) et protège du feu. "
                                "Il procure une défense de +1 et divise les DM  souffle ou de zone par 2.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Fort Boueux", chapter="La bataille de vireux", numbering="3")
            ],
            'magical_level': 1,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=2, unit='Kg'),
            'hands': 1,
            'defense': [Mod(label="DEF", mtype="+", count=1)],
            'special_property': ["DM feu (souffle, zone) / 2"],
            'flavor': [Flavor(ftype='fire', count=1)],
        },
        'bouclier-a-pointes': {
            'name': "Bouclier à pointes",
            'base_item': lambda item: item.oid,
            'short_description': "Un très ancien bouclier à pointe fabriqué dans un métal d’un gris mat et sombre.",
            'full_description': "Un très ancien bouclier à pointe de l’époque du Roi-Sorcier de Tor-Angul, "
                                "fabriqué dans un métal d’un gris mat et sombre. Bouclier +2 et, si le "
                                "bouclier est utilisé pour attaquer, il inflige 1d8 DM létaux (au lieu de "
                                "1d4 temporaires).",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'magical_level': 2,
            'cost': lambda item: Cost(
                value=item.magical_level * item.magical_level * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=2, unit='Kg'),
            'hands': 1,
            'defense': [Mod(label="DEF", mtype="+", count=2)],
            'special_property': [
                "Attaque bouclier: 1d8",
                "DM du bouclier létaux"],
            'flavor': [Flavor(ftype='magical', count=2)],
        }
    },
    "Bullet": {
        'fleche-de-guerre-elfique': {
            'name': "Flêches de guerre elfique",
            'base_item': lambda item: item.oid,
            'short_description': "Cinq flêches de guerre elfiques qui procurent un petit bonus aux dégâts.",
            'full_description': "Ces flêches de guerre elfiques procurent un petit bonus de +1 aux "
                                "dégâts, mais ne sont utilisables qu'avec un arc long.  Il en "
                                "reste 5 dans ce carqois.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Sanctuaire",
                         chapter="Le Sanctuaire de Trenner", numbering="3")
            ],
            'cost': Cost(
                value=100.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'special_property': ["DM: +1",
                                 "Uniquement avec un arc long"],
            'quantity': 1,
            'use': 5
        },
        'fleche-meutriere': {
            'name': "Flêche meurtrière",
            'base_item': lambda item: item.oid,
            'short_description': "Des flêches meutrières qui infligent d'importants dégâts supplémentaires.",
            'full_description': "Des flêches meutrières qui infligent d'importants dégâts supplémentaires. Il en "
                                "reste 4 dans ce carqois.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(
                value=240.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'special_property': ["DM: +2d6"],
            'quantity': 1,
            'use': 4
        },
        'carreau-meutrier': {
            'name': "Carreau meurtrier",
            'base_item': lambda item: item.oid,
            'short_description': "Des carreaux meutriers qui infligent d'importants dégâts supplémentaires.",
            'full_description': "Des carreaux meutriers qui infligent d'importants dégâts supplémentaires. Il en "
                                "reste 4 dans ce lot.",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(
                value=240.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'special_property': ["DM: +2d6"],
            'quantity': 1,
            'use': 4
        },
        'carreau-poison': {
            'name': "Carreau empoisonné",
            'base_item': lambda item: item.oid,
            'short_description': "Ces carreaux d’arbalète sont enduits de poison. La victime d’une attaque "
                                 "réussie doit résister au poison ou ou sombrer petit à petit dans l’inconscience.",
            'full_description': "Ces carreaux d’arbalète sont enduits de poison. La victime d’une attaque réussie "
                                "doit faire un test de CON difficulté 12 ou sombrer dans l’inconscience en 1d6 "
                                "tours pour une durée de 1d6 minutes",
            'category': "quest",
            'scenario': [
                Scenario(campaign="Anathazerïn", title="Le Pic d'Andalf", chapter="Le sanctuaire", numbering="2")
            ],
            'cost': Cost(
                value=240.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'special_property': ["Inconscient: CON < 12"],
            'quantity': 1,
            "duration": Duration(value="1d6", unit="tr"),
            'use': 4
        },
        'fleche': {
            'name': lambda item: f"Flêche +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"Attaque: +{item.magical_level}",
                                              f"DM: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Ces flêches magiques apportent un bonus à l'attaque et aux dégâts.",
            'full_description': lambda item: f"Ces flêches magiques apportent un bonus à l'attaque et aux dégâts "
                                             f"de +{item.magical_level}. Lot de {item.use} flêches.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'use': 5,
            'cost': lambda item: Cost(
                value=item.use * item.magical_level * item.magical_level * ccc['global']['cost']['bullets'],
                unit=ccc['global']['cost']['unit']).iso(),
            'quantity': 1,
            'weight': Weight(value=0.3, unit='Kg'),
        },
        'bille': {
            'name': lambda item: f"Bille +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"Attaque: +{item.magical_level}",
                                              f"DM: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Ces billes magiques apportent un bonus à l'attaque et aux dégâts.",
            'full_description': lambda item: f"Ces billes magiques apportent un bonus à l'attaque et aux dégâts "
                                             f"de +{item.magical_level}. Lot de {item.use} billes.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'use': 5,
            'cost': lambda item: Cost(
                value=item.use * item.magical_level * item.magical_level * ccc['global']['cost']['bullets'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'quantity': 1
        },
        'carreau': {
            'name': lambda item: f"Carreau +{item.magical_level}",
            'base_item': lambda item: f"{item.oid}",
            'special_property': lambda item: [f"Attaque: +{item.magical_level}",
                                              f"DM: +{item.magical_level}"],
            'flavor': lambda item: [Flavor(ftype='magical', count=item.magical_level)],
            'short_description': "Ces carreaux magiques apportent un bonus à l'attaque et aux dégâts.",
            'full_description': lambda item: f"Ces carreaux magiques apportent un bonus à l'attaque et aux dégâts "
                                             f"de +{item.magical_level}. Lot de {item.use} carreaux.",
            'magical_levels': [1, 2, 3, 4],
            'category': "Magical",
            'magical_level': lambda item: 1 + item.magical_level,
            'use': 5,
            'cost': lambda item: Cost(
                value=item.use * item.magical_level * item.magical_level * ccc['global']['cost']['bullets'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'quantity': 1
        },
        'projectile-silver': {
            'flavors': [
                {"name": "carreau", "label": "Carreaux", "desc1": "Ces carreaux",
                 "desc2": "Le carreau", "desc3": "carreaux"},
                {"name": "fleche", "label": "Flêches", "desc1": "Ces flêches",
                 "desc2": "La flêche", "desc3": "flêches"},
                {"name": "bille", "label": "Billes", "desc1": "Ces billes",
                 "desc2": "La bille", "desc3": "billes"},
            ],
            'name': lambda item, flavor: f"{flavor['label']}, en Argent alchimique",
            'oid': lambda item, flavor: f"{item.oid}-{flavor['name']}-silver",
            'base_item': lambda item, flavor: f"{flavor['name']}",
            'special_property': [f"RD: ignoré (sensible à l'agent)",
                                 f"DM: x2 (sensible à l'argent)"],
            'flavor': [Flavor(ftype='silver', count=1)],
            'short_description':
                lambda item, flavor: f"{flavor['desc1']} doublent les dégâts contre les lycanthropes.",
            'full_description':
                lambda item, flavor: f"{flavor['desc1']} sont en argent et doublent les dégâts contre les "
                                     f"lycanthropes et autres créatures sensibles à l'argent. {flavor['desc2']} "
                                     f"ignore également la RD d'une telle créature. "
                                     f"Lot de {item.use} {flavor['desc3']}.",
            'category': 'Bazar du bizarre',
            'use': 5,
            'cost': lambda item, flavor: Cost(
                value=ccc['global']['cost']['silver'] + item.use * ccc['global']['cost']['bullets'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'quantity': 1
        },
        'projectile-durium': {
            'flavors': [
                {"name": "carreau", "label": "Carreaux", "desc1": "Ces carreaux",
                 "desc2": "Le carreau", "desc3": "carreaux"},
                {"name": "fleche", "label": "Flêches", "desc1": "Ces flêches",
                 "desc2": "La flêche", "desc3": "flêches"},
                {"name": "bille", "label": "Billes", "desc1": "Ces billes",
                 "desc2": "La bille", "desc3": "billes"},
            ],
            'name': lambda item, flavor: f"{flavor['label']}, en durium",
            'oid': lambda item, flavor: f"{item.oid}-{flavor['name']}-durium",
            'base_item': lambda item, flavor: f"{flavor['name']}",
            'special_property': [f"Portée maximum / 2",
                                 f"DM: +2"],
            'flavor': [Flavor(ftype='durium', count=1)],
            'short_description':
                lambda item, flavor: f"{flavor['desc1']} sont en durium, un métal lourd qui limitent leur portée.",
            'full_description':
                lambda item, flavor: f"{flavor['desc1']} sont en durium, un métal bleu sombre, très dur et "
                                     "particulièrement lourd. Les projectiles en durium voient leur portée "
                                     "maximum divisée par deux."
                                     f"Lot de {item.use} {flavor['desc3']}.",
            'category': 'Bazar du bizarre',
            'use': 5,
            'cost': lambda item, flavor: Cost(
                value=ccc['global']['cost']['durium'] + item.use * ccc['global']['cost']['bullets'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'quantity': 1
        },
        'projectile-mythral': {
            'flavors': [
                {"name": "carreau", "label": "Carreaux", "desc1": "Ces carreaux",
                 "desc2": "Le carreau", "desc3": "carreaux"},
                {"name": "fleche", "label": "Flêches", "desc1": "Ces flêches",
                 "desc2": "La flêche", "desc3": "flêches"},
                {"name": "bille", "label": "Billes", "desc1": "Ces billes",
                 "desc2": "La bille", "desc3": "billes"},
            ],
            'name': lambda item, flavor: f"{flavor['label']}, en mythral",
            'oid': lambda item, flavor: f"{item.oid}-{flavor['name']}-mythral",
            'base_item': lambda item, flavor: f"{flavor['name']}",
            'special_property': [f"Portée maximum: +5m"],
            'flavor': [Flavor(ftype='mythral', count=1)],
            'short_description':
                lambda item, flavor: f"{flavor['desc1']} sont en mythral, un très léger qui augmente leur portée.",
            'full_description':
                lambda item, flavor: f"{flavor['desc1']} sont en mythral, un métal très léger de couleur argent. "
                                     "Les projectiles en mythral voient leur portée maximum augmentée de 5 mètres. "
                                     f"Lot de {item.use} {flavor['desc3']}.",
            'category': 'Bazar du bizarre',
            'use': 5,
            'cost': lambda item, flavor: Cost(
                value=ccc['global']['cost']['mythral'] + item.use * ccc['global']['cost']['bullets'],
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'material': "mythral",
            'quantity': 1
        },
        'carreau-explosif-coup-double': {
            'name': "Carreau explosif, de chez Coup-Double",
            'base_item': lambda item: item.oid,
            'short_description': "Un carreau explosif fabriqué à partir d’un champignon très rare et "
                                 "qui explose lorsqu'il touche sa cible.",
            'full_description': "Un carreau explosif fabriqué à partir d’un champignon très rare. Si le carreau "
                                "touche, une explosion se déclenche dans une étrange fumée verdâtre, provoquant "
                                "3d6 DM sur la cible et dans un rayon de 3 mètres autour de l’impact.",
            'category': "quest",
            'area': Area(unit="m", value=3),
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Rejoindre la Thuléa", numbering="2")
            ],
            'cost': Cost(
                value=50.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'quantity': 1,
            'special_property': [f"Explosion: 3d6 DM "],
        },
        'fleche-de-guerre+2': {
            'name': "Flêches de guerre +2",
            'base_item': 'fleche-de-guerre',
            'short_description': "Cinq flêches de guerre qui procurent un bonus aux dégâts.",
            'full_description': "Ces flêches de guerre procurent un bonus de +2 aux "
                                "dégâts, mais ne sont utilisables qu'avec un arc long.  Il en "
                                "reste 5 dans ce carqois.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'cost': Cost(
                value=1000.0,
                unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.3, unit='Kg'),
            'special_property': ["DM: +2",
                                 "Uniquement avec un arc long"],
            'quantity': 1,
            'use': 5,
            'flavor': [Flavor(ftype='magical', count=2)],
        },
    },
    "Armor": {
        'armure-cuir-peau-dragon': {
            'flavors': [
                {"color": "blanc", "magical_level": 3, "age": "juvénile", "rd_count": 0,
                 "rd_target": "coldness", "cost": 500},
                {"color": "blanc", "magical_level": 4, "age": "jeune", "rd_count": 2,
                 "rd_target": "coldness", "cost": 1000},
                {"color": "blanc", "magical_level": 5, "age": "adulte", "rd_count": 5,
                 "rd_target": "coldness", "cost": 5000},
                {"color": "blanc", "magical_level": 6, "age": "ancien", "rd_count": 10,
                 "rd_target": "coldness", "cost": 10000},
                {"color": "rouge", "magical_level": 3, "age": "juvénile", "rd_count": 0,
                 "rd_target": "fire", "cost": 500},
                {"color": "rouge", "magical_level": 4, "age": "jeune", "rd_count": 2,
                 "rd_target": "fire", "cost": 1000},
                {"color": "rouge", "magical_level": 5, "age": "adulte", "rd_count": 5,
                 "rd_target": "fire", "cost": 5000},
                {"color": "rouge", "magical_level": 6, "age": "ancien", "rd_count": 10,
                 "rd_target": "fire", "cost": 10000},
                {"color": "noir", "magical_level": 3, "age": "juvénile", "rd_count": 0,
                 "rd_target": "acid", "cost": 500},
                {"color": "noir", "magical_level": 4, "age": "jeune", "rd_count": 2,
                 "rd_target": "acid", "cost": 1000},
                {"color": "noir", "magical_level": 5, "age": "adulte", "rd_count": 5,
                 "rd_target": "acid", "cost": 5000},
                {"color": "noir", "magical_level": 6, "age": "ancien", "rd_count": 10,
                 "rd_target": "acid", "cost": 10000},
                {"color": "bleu", "magical_level": 3, "age": "juvénile", "rd_count": 0,
                 "rd_target": "lightning", "cost": 500},
                {"color": "bleu", "magical_level": 4, "age": "jeune", "rd_count": 2,
                 "rd_target": "lightning", "cost": 1000},
                {"color": "bleu", "magical_level": 5, "age": "adulte", "rd_count": 5,
                 "rd_target": "lightning", "cost": 5000},
                {"color": "bleu", "magical_level": 6, "age": "ancien", "rd_count": 10,
                 "rd_target": "lightning", "cost": 10000},
            ],
            'name': lambda item, flavor: f"Armure d'écailles, de dragon {flavor['color']} {flavor['age']}.",
            'base_item': lambda item, flavor: f"armure-cuir-peau-dragon-{flavor['color']}",
            'oid': lambda item, flavor: f"armure-cuir-peau-dragon-{flavor['color']}-{string_to_id(flavor['age'])}",
            'full_description': 
                lambda item, flavor: f"Réalisée par un artisant, cette armure a été confectionnée en utilisant toutes "
                                     "les écailles les plus remarquables d'un dragon "
                                     "{flavor['color']} {flavor['age']}. Cette armure de qualité (pénalité "
                                     "d'encombrement réduite de 1) octroie en plus de son bonus de défense "
                                     f"de +{flavor['magical_level']}, une réduction aux dégats élémentaires de "
                                     "correspondants au type du dragon (blanc/froid, rouge/feu, noir/acide ou "
                                     "bleu/électricité) et à son age (juvénile, jeune, adulte ou ancien.",
            'magical_level': lambda item, flavor: 1 + flavor['magical_level'],
            'short_description': 
                lambda item, flavor: f"Une armure de cuir en peau de dragon {flavor['color']} {flavor['age']} qui "
                                     "réduits les dégats élémentaires.",
            'weight': Weight(value=6.0, unit='Kg'),
            'defense': lambda item, flavor: [
                Mod(label="DEF", target="", mtype="+", count=flavor['magical_level']),
                Mod(label="RD", target=flavor['rd_target'], count=flavor['rd_count'])],
            'skill': [Mod(label="Test", target="DEX", count=2, mtype="-")],
            'category': 'Bazar du bizarre',
            'cost': lambda item, flavor: Cost(
                value=flavor["cost"],
                unit=ccc['global']['cost']['unit']).iso(),
            'flavor': lambda item, flavor: [Flavor(ftype=f"dragon-{flavor['color']}",
                                                   count=flavor['magical_level'] - 2)],
        },
        'cuirasse-de-bronze+1': {
            'name': "Cuirasse de bronze +1",
            'base_item': lambda item: item.oid,
            'full_description': "Fait de plusieurs plaques de bronze rigides, cette cuirasse protègera "
                                "par devant votre torse avec le plaston et par derrière votre dos avec "
                                "la dossière. Elle protège donc l'ensemble du "
                                "corps et procure un bonus de DEF +5. Cette armure est magique et offre "
                                "un bonus de DEF de +1 et réduit de 1 les pénalités qu'elle inflige.",
            'short_description': "Cuirrasse faite de plusieurs plaques de bronze rigides qui protègent "
                                 "l'ensemble du corps. Cette armure magique offre un bonus de DEF de +1.",
            'weight': Weight(value=20.0, unit='Kg'),
            'defense': [
                Mod(label="DEF", target="", mtype="+", count=6)
            ],
            'skill': [Mod(label="Test", target="DEX", count=4, mtype="-")],
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'category': 'quest',
            'cost': Cost(
                value=2100,
                unit=ccc['global']['cost']['unit']).iso(),
            'flavor': [Flavor(ftype="drow",count=1)],
            'special_property': ["Utilisable: voleur, barde rôdeur et barbare"],
        },
        'chemise-de-maille-des-elfes-noirs': {
            'name': "Chemise de mailles, des elfes noirs",
            'base_item': "chemise-de-maille-des-elfes-noirs",
            'oid': "chemise-de-maille-des-elfes-noirs",
            'full_description': "Les chemises de maille des elfes noirs sont si légères et souples "
                                "qu’elles sont considérées comme des armures de cuir (pénalité de -2 "
                                "de base). Elles peuvent être portées par les voleurs, les bardes, "
                                "les rôdeurs ou les barbare comme s’il s’agissait d’armure de cuir "
                                "(mais pas par les druides ou forgesorts, qui sont des lanceurs de "
                                "sort).",
            'short_description': "Les chemises de maille des elfes noirs sont si légères et souples "
                                 "qu’elles sont considérées comme des armures de cuir.",
            'weight': Weight(value=6.0, unit='Kg'),
            'defense': [
                Mod(label="DEF", target="", mtype="+", count=4)
            ],
            'skill': [Mod(label="Test", target="DEX", count=2, mtype="-")],
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'category': 'quest',
            'cost': Cost(
                value=115,
                unit=ccc['global']['cost']['unit']).iso(),
            'flavor': [Flavor(ftype="drow",count=1)],
            'special_property': ["Utilisable: voleur, barde rôdeur et barbare"],
        },
        'chemise-de-maille-des-elfes-noirs': {
            'flavors': [
                {"magical_level": 1},
                {"magical_level": 2},
                {"magical_level": 3},
                {"magical_level": 4},
            ],
            'magical_level': lambda item, flavor: flavor['magical_level'],
            'name': lambda item, flavor: f"Chemise de mailles +{flavor['magical_level']}, des elfes noirs",
            'base_item': "chemise-de-maille-des-elfes-noirs",
            'oid': lambda item, flavor: f"chemise-de-maille-des-elfes-noirs+{flavor['magical_level']}",
            'full_description': 
                lambda item, flavor: f"Les chemises de maille des elfes noirs sont si légères et souples "
                                      "qu’elles sont considérées comme des armures de cuir (pénalité de -2 "
                                      "de base). Elles peuvent être portées par les voleurs, les bardes, "
                                      "les rôdeurs ou les barbare comme s’il s’agissait d’armure de cuir "
                                      "(mais pas par les druides ou forgesorts, qui sont des lanceurs de "
                                      "sort). Cette armure est magique et offre un bonus de DEF de "
                                     f"+{flavor['magical_level']} et réduit de {flavor['magical_level']} "
                                      "les pénalités qu'elle inflige.",
            'short_description': 
                lambda item, flavor: f"Les chemises de maille des elfes noirs sont si légères et souples "
                                      "qu’elles sont considérées comme des armures de cuir.",
            'weight': Weight(value=6.0, unit='Kg'),
            'defense': lambda item, flavor: [
                Mod(label="DEF", target="", mtype="+", count=4 + flavor['magical_level'])
            ],
            'skill': lambda item, flavor: [Mod(label="Test", target="DEX", count=2 - flavor['magical_level'], mtype="-")] if 2 - flavor['magical_level'] > 0 else None,
            'scenario': lambda item, magical_level: [
                Scenario(
                    campaign="Anathazerïn", title="La bataille de Fleck", chapter="La vallée de Duïn", numbering="3"
                ),
            ],
            'category': 'quest',
            'cost': lambda item, flavor: Cost(
                value=100 + flavor['magical_level'] * flavor['magical_level'] * ccc['global']['cost']['magical'],
                unit=ccc['global']['cost']['unit']).iso(),
            'flavor': lambda item, flavor: [
                Flavor(ftype="magical",count=flavor['magical_level']),
            ],
            'special_property': ["Utilisable: voleur, barde rôdeur et barbare"],
        },
        'chemise-de-mailles+2-mythral-free-action': {
            'base_item': 'chemise-de-mailles',
            'name': "Chemise de mailles +2, d'action libre en mythral",
            'magical_level': 3,
            'material': 'mythral',
            'full_description': "Fait d'anneaux métalliques entrecroisés, la chemise de mailles est utilisée "
                                "entre des couches de vêtements ou de cuir. Cette armure offre une protection "
                                "modeste pour le haut du corps et permet au son provoqué par les anneaux frottant "
                                "l'un contre l'autre d'être atténué par les couches de vêtements extérieures. Elle "
                                "procure un bonus de DEF +4. Cette armure est magique et offre un bonus de DEF de +2 et réduit "
                                "de 2 les pénalités qu'elle inflige. Cette armure est faite en mythral, un métal très léger de couleur "
                                "argent. Cette armure voit sa pénalité d'armure réduite "
                                "de 2 points. Dans cette armure le personnage ne peut pas être ralenti, immobilisé "
                                "ou paralysé par la magie. Il obtient un bonus de +5 à tous les tests " 
                                "pour résister à ce type d'effet préjudiciable s'il s'agit d'une "
                                "contrainte physique.",
            'short_description': "Armure composée de d'anneaux métalliques qui protège surtout le "
                                 "haut du corps. Cette armure magique offre un bonus de DEF "
                                 "de +2, réduit la pénalité d'armure et dans cette armure on ne peut pas être entravé pas magie.",
            'weight': Weight(value=20.0, unit='Kg'),
            'flavor': [Flavor(ftype='magical', count=2), Flavor(ftype='mythral', count=1), Flavor(ftype='free-action', count=1)],
            'defense': [Mod(label="DEF", mtype="+", count=6)],
            'cost': Cost(
                value=6 * 2 * ccc['global']['cost']['mythral'] + 15,
                unit=ccc['global']['cost']['unit']).iso(),
            'special_property': ["Immunité : ralenti, paralysé, immobilisé par la magie"],
            'skill': [
                Mod(label="Test", target="slowdown-resistance", mtype="+", count="5", limitation="Contraintes physiques uniquement"),
                Mod(label="Test", target="immobilized-resistance", mtype="+", count="5", limitation="Contraintes physiques uniquement"),
                Mod(label="Test", target="paralysed-resistance", mtype="+", count="5", limitation="Contraintes physiques uniquement")
            ],
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'category': 'quest',
        },
        'robe-tissu-elfique': {
            'name': "Robe, en tissu elfique",
            'base_item': "robe-elfique-naesk",
            'full_description': "Cette robe en tissue elfique est faite en fibre de naësk. La naësk est une araignée "
                                "géante dont le fil, une fois débarrassée de de sa substance collante, produit la "
                                "fibre la plus résistante du monde connu. Elle confère un bonus de DEF de +1 et "
                                "n'impose aucun malus pour le lancement des sorts ni de pénalité d'encombrement.",
            'magical_level': 1,
            'short_description': "Cette robe en tissue elfique est faite en fibre de naësk et n'impose aucun malus "
                                 "pour le lancement des sorts ni de pénalité d'encombrement.",
            'weight': Weight(value=0.5, unit='Kg'),
            'defense': [Mod(label="DEF", target="", mtype="+", count=1)],
            'category': 'Bazar du bizarre',
            'cost': lambda item: Cost(
                value=get_def_level(item.defense) * 2 * ccc['global']['cost']['naesk'],
                unit=ccc['global']['cost']['unit']).iso(),
            'flavor': lambda item: [Flavor(ftype=f"naesk", count=item.magical_level)],
        },
        'malandre-elfique': {
            'name': "Malandre, en tissu elfique",
            'base_item': lambda item: item.oid,
            'full_description': "Cette tunique en tissue elfique est constituée de plusieurs couches de tissus en "
                                "fibre de naësk. La naësk est une araignée géante dont le fil, une fois débarrassée "
                                "de de sa substance collante, produit la fibre la plus résistante du monde connu. "
                                "Elle confère un bonus de DEF de +2 et n'impose aucun malus pour le lancement des "
                                "sorts ni de pénalité d'encombrement.",
            'magical_level': 2,
            'short_description': "Cette tunique en tissue elfique est constituée de plusieurs couches de tissus en "
                                 "fibre de naësk. Elle n'impose aucun malus pour le lancement des sorts ni de "
                                 "pénalité d'encombrement.",
            'weight': Weight(value=1.0, unit='Kg'),
            'defense': [Mod(label="DEF", target="", mtype="+", count=2)],
            'category': 'Bazar du bizarre',
            'cost': lambda item: Cost(
                value=get_def_level(item.defense) * 2 * ccc['global']['cost']['naesk'],
                unit=ccc['global']['cost']['unit']).iso(),
            'flavor': lambda item: [Flavor(ftype=f"naesk", count=item.magical_level)],
        },
    },
    "Cloak": {
        'cape-elfique': {
            'name': "Cape elfique",
            'base_item': lambda item: item.oid,
            'short_description': "Cape elfique.",
            'full_description': "Cape elfique.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="La justices des Elfes", chapter="Le procès", numbering="3")
            ],
            'cost': Cost(value=10.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
        },
        'cape-elfique-discretion': {
            'name': "Cape elfique, de discretion",
            'base_item': lambda item: item.oid,
            'short_description': "Cape elfique qui permet de rester discrêt en forêt.",
            'full_description': "Cape elfique qui procure un bonus de discretion de +2 en forêt.",
            'category': "quest",
            'cost': Cost(value=1000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.0, unit='Kg'),
            "special_property": ["Discretion: +2 (en forêt)"]
        },
        'cape-elfe': {
            'name': "Cape d'elfe",
            'base_item': 'cape-elfique',
            'short_description': "Cape d'elfe.",
            'full_description': "Cape d'elfe qui apporte un bonus de plus 5 en discretion.",
            'category': "quest",
            'scenario': [
                Scenario(
                    campaign="Anathazerïn", title="Les jardins de l'Amertume", chapter="Les jardins de Ma'ishar", numbering="2"
                ),
            ],
            'flavor': [Flavor(ftype='magical', count=1)],
            "magical_level": 1,
            'cost': Cost(value=2000.0, unit=ccc['global']['cost']['unit']).iso(),
            'weight': Weight(value=0.2, unit='Kg'),
            'special_property': [
                "Discretion: +5"
            ],
        },
    }
}
#        'x': {
#            'name': "",
#            'base_item': lambda item: item.oid,
#            'short_description': ".",
#            'full_description': ".",
#            'category': "quest",
#            'scenario': Scenario(campaign="Scénarios uniques", title="Retour à clairval", chapter="", numbering=""),
#            'cost': Cost(value=0.0, unit=ccc['global']['cost']['unit']).iso(),
#            'weight': Weight(value=0.0, unit='Kg'),
#            'quantity': 1,
#            'special_property': [],
#        },
