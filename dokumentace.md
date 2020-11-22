# Úkol č. 1 - zobrazení
Program slouží k vykreslení zvoleného zobrazení želví grafikou. Uživatel vybere přísliušné zobrazení z nabídky, poté zadá souřadnice bodu a měřítko. Zvolit si může i vlastní poloměr. Výsledkem je vykreslená síť s body. 

## Uživatelské vstupy
### Výběr zobrazení
Pro volení jednoho z nabízených zobrazení zadejte jeho zkratku.
- Marinovo zobrazení (válcové): `Ma`
- Postelovo zobrazení (azimutální): `Po`
- Ptolemainovo zobrazení (kuželové): `Pt`

### Poloměr Země
Program umožňuje si zvolit vlasntí poloměr Země, který uživatel zadá (v km), ale je možno použít i defaultní nastavení pro Zemi (tj. 6371.11 km) zadáním nuly.

### Měřítko
Uživatel zadá měřítko, které chce použít pro výpočet zobrazení. Pro měřítko např. 1 : 50 000 0000 zadejde `50000000`. Opět je možnost použít defaultní měřítko zadáním nuly, tj. 1 : 120 000 000.

### Souřadnice bodů
Program se ptá uživatele opakovaně na body, které chce zobrazit. Nejdříve se zadá zeměpišná šířka, poté výška. Použít se mohou jak celá, tak desetinná čísla. Vždy po zadání vstupů program vypíše přepočtené souřadnice daného bodu a ptá se dál na další body. Smyčka se přeruší zadání souřadnice `(0,0)`.


## Výstup programu
Program vykreslí zobrazení, které spočítá s uživatelskými vstupy. Využívána je knihovna turtle. 


- *používaná verze pythonu: 3.8.5* 
- *kompletní zadání úkolu:* [zde](https://github.com/xtompok/uvod-do-prg_20/tree/ed6ca4dcef3594d045f6fe55b69f6ab2acbdff2c/du01)