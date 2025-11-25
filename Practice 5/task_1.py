sea_fish        = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]
for i in range(len(freshwater_fish)):
    freshwater_fish[i] = freshwater_fish[i].lower()

for i in range(len(sea_fish)):
    sea_fish[i] = sea_fish[i].lower()
print(sorted(freshwater_fish+sea_fish))

