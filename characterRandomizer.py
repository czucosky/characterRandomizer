import tkinter as tk
from tkinter import ttk
import random

# Races
raceList = [
    "Aarakocra", "Aasimar", "Bugbear", "Dragonborn", "Dwarf", "Elf",
    "Firbolg", "Genasi", "Gith", "Gnome", "Goblin", "Goliath",
    "Grung", "Half-Elf", "Half-Orc", "Halfling", "Hobgoblin", "Human",
    "Kenku", "Kobold", "Lizardfolk", "Orc", "Tabaxi", "Tiefling",
    "Tortle", "Triton", "Yuan-ti Pureblood"
]

# Backgrounds
backgroundList = [
    "Acolyte", "Anthropologist", "Archaeologist", "Charlatan",
    "City Watch", "Clan Crafter", "Cloistered Scholar", "Courtier",
    "Criminal", "Entertainer", "Faction Agent", "Far Traveler",
    "Folk Hero", "Guild Artisan", "Haunted One", "Hermit", "Inheritor",
    "Knight of the Order", "Mercenary Veteran", "Noble", "Outlander",
    "Sage", "Sailor", "Soldier", "Urban Bounty Hunter", "Urchin",
    "Uthgardt Tribe Member", "Waterdhavian Noble"
]

# Subraces
aasimar = ["Fallen", "Protector", "Scourge"]
dragonborn = ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"]
dwarf = ["Duergar", "Hill", "Mountain"]
elf = ["Drow", "Eladrin", "High", "Sea", "Shadar-kai", "Wood"]
genasi = ["Air", "Earth", "Fire", "Water"]
gith = ["Githyanki", "Githzerai"]
gnome = ["Deep", "Forest", "Rock"]
half_elf = ["Base", "High", "Sea", "Drow", "Wood"]
halfling = ["Ghostwise", "Lightfoot", "Stout"]
tiefling_lineage = ["Asmodeus", "Baalzebul", "Dispater", "Fierna", "Glasya", "Levistus", "Mammon", "Mephistopheles", "Zariel"]
tiefling_variants = ["Devil’s Tongue", "Hellfire", "Winged", "Feral", "Infernal Legacy", "None lmao"]

# Barbarian subclasses
barbarian_subclasses = ["Ancestral Guardian", "Battlerager", "Berserker", "Storm Herald", "Totem Warrior", "Zealot"]

# Bard subclasses
bard_subclasses = ["Glamour", "Lore", "Swords", "Valor", "Whispers"]

# Cleric subclasses
cleric_subclasses = ["Arcana", "Death", "Forge", "Grave", "Knowledge", "Life", "Light", "Nature", "Tempest", "Trickery", "War"]

# Druid subclasses
druid_subclasses = ["Dreams", "Land", "Moon", "Shepherd"]

# Fighter subclasses
fighter_subclasses = ["Arcane Archer", "Battle Master", "Cavalier", "Champion", "Eldritch Knight", "Purple Dragon Knight", "Samurai"]

# Monk subclasses
monk_subclasses = ["Drunken Master", "Four Elements", "Kensei", "Long Death", "Open Hand", "Shadow", "Sun Soul"]

# Paladin subclasses
paladin_subclasses = ["Ancients", "Conquest", "Crown", "Devotion", "Oathbreaker", "Redemption", "Vengeance"]

# Ranger subclasses
ranger_subclasses = ["Beast Master", "Gloom Stalker", "Horizon Walker", "Hunter", "Monster Slayer"]

# Rogue subclasses
rogue_subclasses = ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Scout", "Swashbuckler", "Thief"]

# Sorcerer subclasses
sorcerer_subclasses = ["Divine Soul", "Draconic", "Shadow", "Storm", "Wild Magic"]

# Warlock subclasses
warlock_subclasses = ["Archfey", "Celestial", "Fiend", "Great Old One", "Hexblade", "Undying"]

# Wizard subclasses
wizard_subclasses = ["Abjuration", "Bladesinging", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy"]

# Function to randomize character
def randomize():
    classList = []
    baseRace = random.choice(raceList)
    background = random.choice(backgroundList)
    strength = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    dexterity = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    constitution = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    intelligence = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    wisdom = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    charisma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

    match baseRace:
        case "Aarakocra":
            dexterity += 2
            wisdom += 1
        case "Aasimar":
            charisma += 2
            subRace = random.choice(aasimar)
            match subRace:
                case "Fallen":
                    strength += 1
                case "Protector":
                    wisdom += 1
                case "Scourge":
                    constitution += 1
            baseRace += " - " + subRace
        case "Bugbear":
            strength += 2
            dexterity += 1
        case "Dragonborn":
            strength += 2
            charisma += 1
            subRace = random.choice(dragonborn)
            baseRace += " - " + subRace
        case "Dwarf":
            constitution += 2
            subRace = random.choice(dwarf)
            match subRace:
                case "Duergar":
                    strength += 1
                case "Hill":
                    wisdom += 1
                case "Mountain":
                    strength += 2
            baseRace += " - " + subRace
        case "Elf":
            dexterity += 2
            subRace = random.choice(elf)
            match subRace:
                case "Drow":
                    charisma += 1
                case "Eladrin":
                    charisma += 1
                case "High":
                    intelligence += 1
                case "Sea":
                    constitution += 1
                case "Shadar-kai":
                    constitution += 1
                case "Wood":
                    wisdom += 1
            baseRace += " - " + subRace
        case "Firbolg":
            strength += 1
            wisdom += 2
        case "Genasi":
            constitution += 2
            subRace = random.choice(genasi)
            match subRace:
                case "Air":
                    dexterity += 1
                case "Earth":
                    strength += 1
                case "Fire":
                    intelligence += 1
                case "Water":
                    wisdom += 1
            baseRace += " - " + subRace
        case "Gith":
            intelligence += 1
            subRace = random.choice(gith)
            match subRace:
                case "Githyanki":
                    strength += 2
                case "Githzerai":
                    wisdom += 2
            baseRace += " - " + subRace
        case "Gnome":
            intelligence += 2
            subRace = random.choice(gnome)
            match subRace:
                case "Deep":
                    dexterity += 1
                case "Forest":
                    dexterity += 1
                case "Rock":
                    constitution += 1
            baseRace += " - " + subRace
        case "Goblin":
            dexterity += 2
            constitution += 1
        case "Goliath":
            strength += 2
            constitution += 1
        case "Grung":
            dexterity += 2
            constitution += 1
        case "Half-Elf":
            charisma += 2
            subRace = random.choice(half_elf)
            match subRace:
                case "Base":
                    strength += 1
                    dexterity += 1
                case "High":
                    intelligence += 1
                    dexterity += 1
                case "Sea":
                    constitution += 1
                    dexterity += 1
                case "Drow":
                    charisma += 1
                    dexterity += 1
                case "Wood":
                    wisdom += 1
                    dexterity += 1
            baseRace += " - " + subRace
        case "Half-Orc":
            strength += 2
            constitution += 1
        case "Halfling":
            dexterity += 2
            subRace = random.choice(halfling)
            match subRace:
                case "Ghostwise":
                    wisdom += 1
                case "Lightfoot":
                    charisma += 1
                case "Stout":
                    constitution += 1
            baseRace += " - " + subRace
        case "Hobgoblin":
            constitution += 2
            intelligence += 1
        case "Human":
            strength += 1
            dexterity += 1
            constitution += 1
            intelligence += 1
            wisdom += 1
            charisma += 1
        case "Kenku":
            dexterity += 2
            wisdom += 1
        case "Kobold":
            dexterity += 2
            strength -= 2
        case "Lizardfolk":
            constitution += 2
            wisdom += 1
        case "Orc":
            strength += 2
            constitution += 1
            intelligence -= 2
        case "Tabaxi":
            dexterity += 2
            charisma += 1
        case "Tiefling":
            charisma += 2
            subRace = random.choice(tiefling_lineage)
            variant = random.choice(tiefling_variants)
            match subRace:
                case "Asmodeus":
                    intelligence += 1
                case "Baalzebul":
                    intelligence += 1
                case "Dispater":
                    dexterity += 1
                case "Fierna":
                    wisdom += 1
                case "Glasya":
                    dexterity += 1
                case "Levistus":
                    constitution += 1
                case "Mammon":
                    intelligence += 1
                case "Mephistopheles":
                    intelligence += 1
                case "Zariel":
                    strength += 1
            baseRace += " - " + subRace + " - " + variant
        case "Tortle":
            strength += 2
            wisdom += 1
        case "Triton":
            strength += 1
            constitution += 1
            charisma += 1
        case "Yuan-ti Pureblood":
            charisma += 2
            intelligence += 1

    if strength >= 13:
        classList.extend(["Barbarian","Fighter"])
        if charisma >= 13:
            classList.append("Paladin")

    if dexterity >= 13:
        if "Fighter" not in classList:
            classList.extend(["Fighter", "Rogue"])
        else:
            classList.append("Rogue")
        if wisdom >= 13:
            classList.extend(["Ranger", "Monk"])

    if intelligence >= 13:
        classList.append("Wizard")

    if wisdom >= 13:
        classList.extend(["Cleric", "Druid"])

    if charisma >= 13:
        classList.extend(["Bard", "Sorcerer", "Wizard"])

#or strength+dexterity+constitution+intelligence+wisdom+charisma < 65 if needed
    if not classList:
        return randomize()

    randomClass = random.choice(classList)
    match randomClass:
        case "Barbarian":
            subClass = random.choice(barbarian_subclasses)
        case "Bard":
            subClass = random.choice(bard_subclasses)
        case "Cleric":
            subClass = random.choice(cleric_subclasses)
        case "Druid":
            subClass = random.choice(druid_subclasses)
        case "Fighter":
            subClass = random.choice(fighter_subclasses)
        case "Monk":
            subClass = random.choice(monk_subclasses)
        case "Paladin":
            subClass = random.choice(paladin_subclasses)
        case "Ranger":
            subClass = random.choice(ranger_subclasses)
        case "Rogue":
            subClass = random.choice(rogue_subclasses)
        case "Sorcerer":
            subClass = random.choice(sorcerer_subclasses)
        case "Warlock":
            subClass = random.choice(warlock_subclasses)
        case "Wizard":
            subClass = random.choice(wizard_subclasses)

    result = (
        f"Race: {baseRace}\n"
        f"Class: {subClass} {randomClass}\n"
        f"Background: {background}\n"
        f"Skills:\n"
        f"Strength: {strength}\n"
        f"Dexterity: {dexterity}\n"
        f"Constitution: {constitution}\n"
        f"Intelligence: {intelligence}\n"
        f"Wisdom: {wisdom}\n"
        f"Charisma: {charisma}"
    )

    return result

def generate_character():
    result = randomize()
    result_var.set(result)

# Set up the GUI
root = tk.Tk()
root.title("Character Generator")

# Layout
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Title
title_label = ttk.Label(frame, text="Random Character Generator", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Button to generate character
generate_button = ttk.Button(frame, text="Generate Character", command=generate_character)
generate_button.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Text area to display results
result_var = tk.StringVar()
result_text = ttk.Label(frame, textvariable=result_var, font=("Arial", 12))
result_text.grid(row=2, column=0, columnspan=2)

# Start the GUI loop
root.mainloop()
