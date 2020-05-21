# -*- coding: utf-8 -*-

import cof.properties

inns = {
    'split': {
        'banquet': {
            'banquet': {
                "name": "Banquet",
                "short_description": "Un banquet simple mais copieux.",
                "full_description": "Un banquet simple mais copieux.",
                'cost': cof.properties.Cost(value=10, unit='pa').iso()
            },
            'banquet somptueux': {
                "name": "Banquet somptueux",
                "short_description": "Un banquet somptueux avec plein de mets exquis.",
                "full_description": "Un banquet somptueux avec plein de mets exquis qui ravirait n'importe quel "
                                    "convive.",
                'cost': cof.properties.Cost(value=30, unit='pa').iso()
            },
            'banquet exotique': {
                "name": "Banquet exotique",
                "short_description": "Un banquet avec des mets exotiques.",
                "full_description": "Un banquet avec des mets exotiques. Le repas rêvé pour épater n'importe quel"
                                    "bourgeois ayant de l'argent plein les poches.",
                'cost': cof.properties.Cost(value=60, unit='pa').iso()
            },
            'banquet royal': {
                "name": "Banquet royal",
                "short_description": "Un banquet digne d'une cour royale.",
                "full_description": "Un banquet digne d'une cour royale. Idéal pour amadouer n'importe quel "
                                    "monarque.",
                'cost': cof.properties.Cost(value=100, unit='pa').iso()
            },
        },
        'cervoise-biere': {
            'cervoise': {
                "name": "Cervoise",
                "short_description": "Une pinte de cervoise.",
                "full_description": "Une pinte de cervoise."
            },
            'biere': {
                "name": "Bière",
                "short_description": "Une pinte de bière.",
                "full_description": "Une pinte de bière."
            }
        },
        'cidre-lait': {
            'cidre': {
                "name": "Cidre",
                "short_description": "Un verre de cidre.",
                "full_description": "Un verre de cidre"
            },
            'lait': {
                "name": "Lait",
                "short_description": "Un verre de lait",
                "full_description": "Un verre de lait de chèvre."
            }
        },
        'hydromel-vin': {
            'hydromel': {
                "name": "Hydromel",
                "short_description": "Un verre d'hydromel",
                "full_description": "Un verre d'hydromel"
            },
            'vin': {
                "name": "Vin",
                "short_description": "Un verre de vin quelconque.",
                "full_description": "Un verre de vin quelqconque qui étanchera la soif de n'importe quel "
                                    "aventurier à la fin d'une bonne journée."
            }
        },
        'nuit-chambre-de-4-': {
            'nuit-chambre-de-4-modeste': {
                "name": "Nuit (chambre pour 4 personnes)",
                "short_description": "Une nuit dans une chambre modeste pour 4 personnes.",
                "full_description": "Une nuit dans une chambre modeste pour 4 personnes.",
                'cost': cof.properties.Cost(value=1, unit='pa').iso()
            },
            'nuit-chambre-de-4-confortable': {
                "name": "Nuit (chambre confortable pour 4 personnes)",
                "short_description": "Une nuit dans une chambre confortable pour 4 personnes.",
                "full_description": "Une nuit dans une chambre confortable pour 4 personnes.",
                'cost': cof.properties.Cost(value=2, unit='pa').iso()
            }
        },
        'nuit-chambre-individuelle-': {
            'nuit-chambre-individuelle-modeste': {
                "name": "Nuit (chambre individuelle)",
                "short_description": "Une nuit dans une chambre individuelle modeste.",
                "full_description": "Une nuit dans une chambre individuelle modeste.",
                'cost': cof.properties.Cost(value=2, unit='pa').iso()
            },
            'nuit-chambre-individuelle-confortable': {
                "name": "Nuit (chambre individuelle confortable)",
                "short_description": "Une nuit dans une chambre individuelle confortable.",
                "full_description": "Une nuit dans une chambre individuelle confortable.",
                'cost': cof.properties.Cost(value=5, unit='pa').iso()
            }
        },
        'nuit-dortoir-': {
            'nuit-dortoir-modeste': {
                "name": "Nuit (dortoir)",
                "short_description": "Une nuit dans un dortoir modeste.",
                "full_description": "Une nuit dans un dortoir modeste.",
                'cost': cof.properties.Cost(value=5, unit='pc').iso()
            },
            'nuit-dortoir-confortable': {
                "name": "Nuit (dortoir confortable)",
                "short_description": "Une nuit dans un dortoir confortable.",
                "full_description": "Une nuit dans un dortoir confortable.",
                'cost': cof.properties.Cost(value=10, unit='pc').iso()
            }
        },
        'nuit-suite-': {
            'nuit-suite': {
                "name": "Nuit (suite)",
                "short_description": "Une nuit dans une suite.",
                "full_description": "Une nuit dans une suite.",
                'cost': cof.properties.Cost(value=10, unit='pa').iso()
            },
            'nuit-suite-luxueuse': {
                "name": "Nuit (suite luxueuse)",
                "short_description": "Une nuit dans une suite luxueuse.",
                "full_description": "Une nuit dans une suite luxueuse.",
                'cost': cof.properties.Cost(value=50, unit='pa').iso()
            }
        },
        'grand-cru': {
            'grand-cru': {
                "name": "Grand cru",
                "short_description": "Une bouteille d'un grand cru.",
                "full_description": "Une bouteille d'un grand cru.",
                'cost': cof.properties.Cost(value=5, unit='pa').iso(),
                'weight': cof.properties.Weight(value=1.0, unit='Kg')
            },
            'grand-cru-superieur': {
                "name": "Grand cru supérieur",
                "short_description": "Une bouteille d'un grand cru supérieur.",
                "full_description": "Une bouteille d'un grand cru supérieur.",
                'cost': cof.properties.Cost(value=20, unit='pa').iso(),
                'weight': cof.properties.Weight(value=1.0, unit='Kg')
            },
            'grand-cru-classe': {
                "name": "Grand cru classé",
                "short_description": "Une bouteille d'un grand cru classé.",
                "full_description": "Une bouteille d'un grand cru classé.",
                'cost': cof.properties.Cost(value=50, unit='pa').iso(),
                'weight': cof.properties.Weight(value=1.0, unit='Kg')
            },
        },
    },
    'addons': {
        'bon-repas': {
            'full_description': "Un bon repas copieux avec des pommes de terre et du pain.",
            'short_description': "Un bon repas copieux."
        },
        'repas-avec-viande': {
            'full_description': "Un repas avec une bonne tranche de viande.",
            'short_description': "Un repas avec une bonne tranche de viande."
        },
        'soupe-et-pain': {
            'full_description': "Une bonne soupe de légumes servie avec du pain.",
            'short_description': "Une soupe de légumes avec du pain.",
        }
    }
}
