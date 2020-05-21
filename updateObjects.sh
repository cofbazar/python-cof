#!/bin/bash

case "$1" in
	spell)
		python3 cofCapacitiesUpdate.py && python3 cofDrsSpellsAndMagicalWandsImport.py && cp data/*.json ../../dev/cofbazar.github.io/data/
		;;
	potion)
		python3 cofCapacitiesUpdate.py && python3 cofDrsPotionsImport.py && cp data/*.json ../../dev/cofbazar.github.io/data/
		;;
	weapon|armor|shield|other)
		python3 cofDrsWeaponsArmorsShieldsAndOthersImport.py && cp data/*.json ../../dev/cofbazar.github.io/data/
		;;
	unique)
		python3 cofCapacitiesUpdate.py && python3 cofUniqueImport.py && cp data/*.json ../../dev/cofbazar.github.io/data/
                ;;
	all)
		python3 cofCapacitiesUpdate.py && python3 cofDrsSpellsAndMagicalWandsImport.py && python3 cofDrsPotionsImport.py && python3 cofDrsWeaponsArmorsShieldsAndOthersImport.py && python3 cofUniqueImport.py && cp data/*.json ../../dev/cofbazar.github.io/data/
		;;
	*)
		echo "Usage : $0 spell|potion|weapon|armor|shield|other|unique|all"
		;;
esac
