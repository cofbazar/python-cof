# -*- coding: utf-8 -*-
from cof.properties import *
import config.cofConfig

materials = {
    'cost': lambda item: Cost(
        value=item.magical_level * item.magical_level * config.cofConfig.config['global']['cost']['magical'],
        unit=config.cofConfig.config['global']['cost']['unit']).iso(),
    'addons': {
        'briquet-a-silex': {
            'base_item': 'briquet-a-silex',
            'category': 'Standard',
            'full_description': "Un briquet est une petite pièce d’acier dont on se sert pour créer par "
                                "percussion avec un silex une étincelle.",
            'short_description': "Un briquet à silex qui permet de faire du feu quand il ne fait pas trop de vent.",
            'weight': cof.properties.Weight(value=0.1, unit='Kg')
        },
        'carquois': {
            'base_item': 'carquois',
            'category': 'Standard',
            'full_description': "Un carquois est un étui qui sert à ranger des flèches d'arc ou des carreaux "
                                "d'arbalète. Il peut être porté sur l'archer (à la ceinture ou sur le dos), sur "
                                "l'arc ou posé au sol. Il contient 20 flêches ou 20 carreaux.",
            'short_description': "Un carquois pour ranger des flèches d'arc ou des carreaux d'arbalète.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'quantity': 20,
        },
        'corde-15m-': {
            'name': 'Une corde',
            'base_item': 'corde-15m-',
            'category': 'Standard',
            'full_description': "Une solide corde de 15m qui permettra de ficeler même le plus costaud des méchants. ",
            'short_description': "Une solide corde de 15m qui permettra de ficeler même le plus costaud des méchants.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'range': Range(value=15, unit="m"),
            'quantity': 1,
        },
        'couverture': {
            'base_item': 'couverture',
            'category': 'Standard',
            'full_description': "Une couverture bien épaisse qui tient chaud lorsque l'on dort à la belle étoile.",
            'short_description': "Une couverture bien épaisse qui tient chaud lorsque l'on dort à la belle étoile.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg')
        },
        'grappin': {
            'base_item': 'grappin',
            'category': 'Standard',
            'full_description': "Un grappin est un outil composé de plusieurs crochets, généralement attaché à une "
                                "corde ou autre filin. Il permettra de venir à bout de n'importe "
                                "quelle falaise du moment que l'on ai pas le vertige. Ce grappin fait 15m de long.",
            'short_description': "Un grappin d'une longueur de 15m composé de plusieurs crochets qui permettra "
                                 "de venir à bout de n'importe quelle falaise du moment que l'on ai pas le vertige.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'range': Range(value=15, unit="m"),
            'quantity': 1,
        },
        'huile': {
            'base_item': 'huile',
            'category': 'Standard',
            'full_description': "Une bouteille d'huile. L'huile s'enflamme lorsque qu'elle est au contacte du "
                                "feu.",
            'short_description': "Une bouteille d'huile",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'quantity': 1,
        },
        'lanterne-a-huile': {
            'base_item': 'lanterne-a-huile',
            'category': 'Standard',
            'full_description': "Une lanterne à huile est une lampe dont le combustible est de la graisse animale, "
                                "de l'huile végétale, de l'huile de baleine ou encore de l'huile minérale. La "
                                "flamme est protégée par des parois translucides.",
            'short_description': "Une lanterne à huile dont la flamme est protégée par des parois translucides.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg')
        },
        'materiel-decriture': {
            'base_item': 'materiel-decriture',
            'category': 'Standard',
            'full_description': "Une plume, une fiole d'encre et un rouleau de papier. Vous êtes paré pour écrire "
                                "votre premier roman.",
            'short_description': "Une plume, une fiole d'encre et un rouleau de papier.",
            'weight': cof.properties.Weight(value=0.5, unit='Kg')
        },
        'outils-de-crochetage': {
            'base_item': 'outils-de-crochetage',
            'category': 'Standard',
            'full_description': "Cet étuit comprend l'ensemble des outils nécessaires pour crocher n'importe "
                                "quelle serrure. Elle contient un passepartout, des crochets, des tendeurs, "
                                "des racleurs et des demi-diamants de plusieurs tailles.",
            'short_description': "Outils nécessaires pour crocher n'importe quelle serrure.",
            'weight': cof.properties.Weight(value=0.5, unit='Kg')
        },
        'potion-de-soin': {
            'base_item': 'potion-de-soin',
            'category': 'Standard',
            'full_description': "Une petite potion de soin qui permet de restaurer 1d8 PV.",
            'short_description': "Une petite potion de soin.",
            'weight': cof.properties.Weight(value=0.1, unit='Kg'),
            'special_property': ["Soigne : 1d8 PV"],
            'quantity': 1,
        },
        'ration': {
            'base_item': 'ration',
            'category': 'Standard',
            'full_description': "Tous les aliments nécessaires pour subvenir aux besoins de son corps pendant "
                                "1 semaine. Avec quelques unes de ces rations en poche, vous êtes sûr de ne "
                                "jamais avoir faim lorsque vous partez à l'aventure.",
            'short_description': "Aliments nécessaires pour subvenir aux besoins de son corps pendant 1 semaine. ",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'quantity': 7,
        },
        'sac-a-dos': {
            'base_item': 'sac-a-dos',
            'category': 'Standard',
            'full_description': "Un grand sac à dos qui permettra à n'importe quel aventurier de stocker le "
                                "nécessaire pour faire un long voyage.",
            'short_description': "Un grand sac à dos.",
            'weight': cof.properties.Weight(value=0.5, unit='Kg')
        },
        'torches': {
            'base_item': 'torches',
            'category': 'Standard',
            'full_description': "Un bâton que l’on enflamme à une extrémité pour pouvoir éclairer. Ce lot "
                                "comporte 3 torches qui permettent chacune de s'éclairer pendant 1 heure dans un "
                                "rayon de 10m",
            'short_description': "Une torche est Un bâton que l’on enflamme à une extrémité pour pouvoir éclairer.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'quantity': 3,
            'area': Area(value=10, unit="m"),
            'duration': Duration(value=1, unit="h")
        }
    },
    'others': {
        'outre': {
            'name': "Une outre",
            'base_item': 'outre',
            'category': 'Standard',
            'full_description': "Une outre est un sac en peau, cousu par un bout et dont toutes les coutures sont "
                                "soigneusement bouchées avec de la poix, de manière que l’on peut y renfermer des "
                                "liquides, ou le gonfler d’air.",
            'short_description': "Une outre est un sac en peau que l'on peut remplir de liquide ou que l'on peut "
                                 "glonfler d'air.",
            'weight': cof.properties.Weight(value=0.3, unit='Kg'),
            'cost': lambda item: cof.properties.Cost(value=1.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'quantity': 1,
        },
        'gamelle': {
            'name': "Une gamelle",
            'base_item': 'gamelle',
            'category': 'Standard',
            'full_description': "Une gamelle est un récipient, généralement métallique, destiné à préparer, "
                                "transporter ou manger des aliments lors de circonstances où il n'est pas envisageable "
                                "d'employer les ustensiles habituellement utilisés au foyer.",
            'short_description': "Une gamelle est un récipient, généralement métallique, destiné à préparer, "
                                 "transporter ou manger des aliments lorsque l'on part à l'aventure.",
            'weight': cof.properties.Weight(value=0.1, unit='Kg'),
            'cost': lambda item: cof.properties.Cost(value=1.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
        },
        'leather-skinn': {
            'name': "Peau d'animal",
            'base_item': 'leather-skin',
            'category': 'Cofbazar',
            'full_description': "Une peau d'animal qui peut servir à fabriquer des couvertures ou des habits bien "
                                "chauds.",
            'short_description': "Une peau d'animal qui peut servir à fabriquer des couvertures ou des habits bien "
                                 "chauds.",
            'weight': cof.properties.Weight(value=1.0, unit='Kg'),
            'cost': lambda item: cof.properties.Cost(value=10.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'quantity': 1,
        },
        'pnoulpe': {
            'name': "Pnoulpe",
            'base_item': 'pnoulpe',
            'category': 'Bazar du bizarre',
            'short_description': "Un petit poulpe, qui permet de transformer l'eau en mélange respirable. A placer "
                                 "sur ses voies respiratoires.",
            'full_description': "Le Pnoulpe est une variété de petit poulpe qui à la particularité de transformer "
                                "l'eau en mélange respirable et inversement en quantité suffisante pour assurer la "
                                "survie d'un être humain en milieu aquatique. En pratique, on place le corps mou de "
                                "couleur rouge sur les voies respiratoires, les tentacules enserrant la tête puis on "
                                "se dépêche d'enter dans l'eau pour ne pas asphyxier. Les habitants de la cité de "
                                "Calio ont chacun le leur (une telle créature vit environ 10 ans) et les élèvent. "
                                "On trouve cependant peu de ceux-ci à la vente pour 2 raisons. D'une part la "
                                "production est très peu supérieure aux besoins de Calio et d'autre part le liquide "
                                "qui permet de maintenir le Pnoulpe en état de léthargie a un coût de fabrication "
                                "très élevé. Le Pnoulpe est vendue dans un coffret de bois étanche empli d'un "
                                "liquide qui permet de le conserver en léthargie pendant 1 mois au maximum "
                                "(15x15x30cm), poids 5Kg). Dès que la boîte est ouverte, il faut mettre le Pnoulpe "
                                "à l'eau, la boîte et le liquide ne sont plus utilisables.",
            'cost': lambda item: cof.properties.Cost(value=500.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=5.0, unit='Kg'),
            'quantity': 1,
        },
        'dowser-s-wand': {
            'base_item': 'dowser-s-wand',
            'category': 'Bazar du bizarre',
            'name': "Baguette de sourcier",
            'short_description': "La baguette de sourcier permet d'indiquer la direction de la plus proche source "
                                 "d'eau en surface.",
            'full_description': "Le sourcier est un des nombreux arbres magique du Wahalith, ses branches taillées "
                                "de façon appropriée ont la particularité d'indiquer la direction de la plus proche "
                                "source d'eau en surface et ce quel que soit la distance. Le bois nécesite d'être "
                                "relativement frais et malgré un traitement spécial perd ses propriétés en 2 mois.",
            'cost': lambda item: cof.properties.Cost(value=200.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.1, unit='Kg')
        },
        'true-dowser-s-wand': {
            'base_item': 'true-dowser-s-wand',
            'category': 'Bazar du bizarre',
            'name': "Baguette de vrai sourcier",
            'short_description': "La baguette de vrai sourcier permet d'indiquer la direction de la plus proche source "
                                 "d'eau en surface. Son effet est permanent.",
            'full_description': "Le sourcier est un des nombreux arbres magique du Wahalith, ses branches taillées "
                                "de façon appropriée ont la particularité d'indiquer la direction de la plus proche "
                                "source d'eau en surface et ce quel que soit la distance. Il existe une méthode "
                                "particulièrement longue et complexe pour obtenir une baguette aux propriétés "
                                "permanentes qui s'utilise uniquement avec le rameau le plus élévé d'un Sourcier, "
                                "cela rend l'objet beaucoup plus rare et cher",
            'cost': lambda item: cof.properties.Cost(value=2000.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.1, unit='Kg')
        },
        'ardent-fragment': {
            'base_item': 'ardent-fragment',
            'category': 'Bazar du bizarre',
            'material': 'phospharium',
            'flavor': [Flavor(ftype='phospharium', count=1)],
            'name': "Fragment ardent",
            'short_description': "Petit morceau de Phospharium de la taille d'un zippo qui s'enflamme au contact "
                                 "de l'air.",
            'full_description': "Il s'agit d'un pavé de métal de la taille d'un zippo qui contient un petit morceau "
                                "de Phospharium, le métal qui s'enflamme par réaction alchimique au contact de l'air. "
                                "Lorsque l'on ouvre le couvercle, le fragment chauffe et s'enflamme, lorsqu'on le "
                                "ferme, privé d'air il s'éteint. L'ensemble a cependant tendance à vite devenir "
                                "brûlant.",
            'cost': lambda item: cof.properties.Cost(value=50.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.1, unit='Kg')
        },
        'ardent-torch': {
            'name': "Torche ardente",
            'base_item': 'ardent-torch',
            'material': 'phospharium',
            'flavor': [Flavor(ftype='phospharium', count=1)],
            'category': 'Bazar du bizarre',
            'short_description': "Une torche en phospharium qui éclaire lorsque l'on enlève le capuchon de "
                                 "protection.",
            'full_description': "Un manche en métal avec une gaine en cuir et à l'extrémité un morceau de cylindre "
                                "de Phospharium de 10cm environ recouvert d'un capuchon gainé de cuir lui aussi. "
                                "Une fois le capuchon retiré, l'objet donne une lueur équivalente à une torche "
                                "normale (soit environ 12m de diamètre).",
            'cost': lambda item: cof.properties.Cost(value=200.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'area': Area(value=12, unit="m"),
            'weight': cof.properties.Weight(value=0.5, unit='Kg')
        },
        'cosse-de-psalifere': {
            'name': "Cosse de psalifère",
            'base_item': 'cosse-de-psalifere',
            'category': 'Bazar du bizarre',
            'short_description': "La cosse de psalifère permet de créer une zone de brouillard épais lorsqu'elle est "
                                 "jetée à terre ou tirée avec une flèche.",
            'full_description': "La cosse de psalifère sèche ressemble à un gros haricot sec de 2cm de diamètre. Son "
                                "coeur renferme une énorme quantité de spores noires que la fermentation fait monter "
                                "en pression. Dans la nature, la cosse fini par exploser projetant ses spores en un "
                                "large nuage de brouillard noir qui se dissipe au gré du vent. Lorsqu'elles sont "
                                "récoltées, les cosses sont traitées de façon à arrêter le porcessus de fermentation "
                                "juste avant l'instant cruciale, elle n'explosent alors qu'en cas de choc assez "
                                "violent. Lorsque la cosse est jetée par terre ou tirée avec une flèche, elle explose "
                                "en projetant un nuage de brouillard noir de 6m qui plonge la zone dans les ténèbres. "
                                "Au deuxième tour, la zone atteind 18m de diamètre et correspond à un brouillard "
                                "épais. Ensuite le brouillard se dissipe progressivement, mais si l'air est calme, "
                                "il peut durer jusqu'à 5 min.",
            'cost': lambda item: cof.properties.Cost(value=50.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.0, unit='Kg'),
            'quantity': 1,
        },
        'graine-d-amour': {
            'name': "Graine d'amour",
            'base_item': 'graine-d-amour',
            'category': 'Bazar du bizarre',
            'short_description': "La graine d'amour rend stérile celui ou celle qui l'ingère.",
            'full_description': "Celui ou celle qui ingère cette graine est stérile pendant les 24h suivantes "
                                "(latence 1h).",
            'cost': lambda item: cof.properties.Cost(value=5.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.0, unit='Kg'),
            'quantity': 1,
        },
        'chope-en-hybberium': {
            'name': "Chope en Hybberium",
            'base_item': 'chope-en-hybberium',
            'material': 'hybberium',
            'flavor': [Flavor(ftype='hybberium', count=1)],
            'category': 'Bazar du bizarre',
            'short_description': "Chope en Hybberium qui reste fraîche en toute occasion.",
            'full_description': "Cette simple chope en métal, en bois, en ivoire et autre terre cuite, possède un "
                                "fond doublé en Hybberium protégé par un capuchon de cuir. Lorsque ce dernier est "
                                "retiré, l'action glaciale de l'Hybberium ne tarde pas à se faire sentir et permet "
                                "à votre bière d'être bien fraîche même en plein désert. Un must pour tout nain qui "
                                "se respecte.",
            'cost': lambda item: cof.properties.Cost(value=100.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.2, unit='Kg')
        },
        'tasse-en-phospharium': {
            'base_item': 'tasse-en-phospharium',
            'category': 'Bazar du bizarre',
            'material': 'phospharium',
            'flavor': [Flavor(ftype='phospharium', count=1)],
            'name': "Tasse en Phospharium",
            'short_description': "Une tasse en phospharium qui reste chaude en toute occasion.",
            'full_description': "Cette simple tasse en métal, en bois, en ivoire et autre terre cuite, possède un "
                                "fond doublé en Phospharium protégé par un capuchon de cuir. Lorsque ce dernier est "
                                "retiré, l'action chauffante du Phospharium ne tarde pas à se faire sentir et permet "
                                "à votre thé d'être bien chaud même en plein milieu de la banquise. Les elfes en "
                                "raffolent.",
            'cost': lambda item: cof.properties.Cost(value=100.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.2, unit='Kg')
        },
        'casserole-en-phospharium': {
            'material': 'phospharium',
            'flavor': [Flavor(ftype='phospharium', count=1)],
            'base_item': 'casserole-en-phospharium',
            'category': 'Bazar du bizarre',
            'name': "Casserole en Phospharium",
            'short_description': "Casserole en Phospharium pour manger un repas cuit même en terre hostile.",
            'full_description': "Cette simple casserole en métal, en bois, en ivoire et autre terre cuite, possède un "
                                "fond doublé en Phospharium protégé par un capuchon de cuir. Lorsque ce dernier est "
                                "retiré, l'action chauffante du Phospharium ne tarde pas à se faire sentir. Plus "
                                "qu'un simple gadget, c'est la solution pour manger cuit sans révéler votre position "
                                "en terre hostile par un feu de camp.",
            'cost': lambda item: cof.properties.Cost(value=250.0,
                                                     unit=config.cofConfig.config['global']['cost']['unit']).iso(),
            'weight': cof.properties.Weight(value=0.4, unit='Kg')
        },

    }

}
