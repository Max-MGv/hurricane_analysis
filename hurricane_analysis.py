from hurricanes import damages,names, months, deaths, areas_affected, max_sustained_winds, years

# Updating Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def damage_converter(damages):
  updated_damages = []
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion['M'])
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])
  return  updated_damages


# test function by updating damages
converted_damage = damage_converter(damages)
converted_damage_1 = damage_converter(damages)
print(converted_damage)


# Creating a Table
def hurricane_dictionary(names, months, years, max_wind, areas_affected, deaths):
  hurricane_data = {}
  for index in range(34):
    hurricane_data[names[index]] = {names[index]: [months[index], years[index], max_sustained_winds[index], areas_affected[index], deaths[index]]}
  print('---')
  return hurricane_data

# Creating hurricanes dictionary
hurricane_dictionary_names = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths)
print(hurricane_dictionary_names['Cuba I'])


# Organizing by Year
def hurricane_data_organizer_by_year(names, months, years, max_wind, areas_affected, deaths):
  hurricane_data = {}
  for index in range(34):
    hurricane_data[years[index]] = {years[index]: [months[index],["Name:", names[index]], max_sustained_winds[index], areas_affected[index], ["Death:", deaths[index]]]}
  print('---')
  return hurricane_data

# createing a new dictionary hurricanes with year and key
hurricane_dictionary_years = hurricane_data_organizer_by_year(names, months, years, max_sustained_winds, areas_affected, deaths)
print(hurricane_dictionary_years[2003])

# Counting Damaged Areas
def damaged_area_counter(areas_affected):
  damaged_areas = {}
  unique_locations = []
  # for index in range(len(areas_affected)):
  for areas in areas_affected:
    for area in areas:
      if area not in damaged_areas:
        damaged_areas[area] = 0
      if area in damaged_areas:
        damaged_areas[area] += 1
  print('---')  
  return damaged_areas
# storing areas by the number of hurricanes involved in
areas_affected_count = damaged_area_counter(areas_affected)
print(areas_affected_count)


# Calculating Maximum Hurricane Count
def most_affected_area(damaged_areas_dict):
  max_area = ""
  max_area_count = 0
  for key, value in damaged_areas_dict.items():
    if value > max_area_count:
      max_area = key
      max_area_count = value
  print('---')
  return max_area, max_area_count 

# most frequently affected area and the number of hurricanes involved in
most_affected_areas = most_affected_area(areas_affected_count)
print(most_affected_areas)


# Calculating the Deadliest Hurricane
def hurricane_max_death(hurricanes, deaths):
  max_death = 0
  index = 0
  name = ""
  for death in deaths:
      if death > max_death:
        max_death = death
  index = deaths.index(max_death)
  name = hurricanes[index]
  print('---')
  return name, max_death
# highest mortality hurricane and the number of deaths
worst_hurricane = hurricane_max_death(names, deaths)
print(worst_hurricane)

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# Rating Hurricanes by Mortality
def sort_by_mortality_rate(deaths, names):  
  deaths_dict = dict(zip(names, deaths))
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for keys, values in deaths_dict.items():
    if values == 0:
      hurricanes_by_mortality[0] = {keys, values}
    elif values <= 100:
      hurricanes_by_mortality[1] += [keys, values]
    elif values <= 500:
      hurricanes_by_mortality[2] += [keys, values]
    elif values <= 1000:
      hurricanes_by_mortality[3] += [keys, values]
    elif values <= 10000:
      hurricanes_by_mortality[4] += [keys, values]
  print((deaths_dict))

  return hurricanes_by_mortality, print('---')


# dictionary with mortality severity as key
mortality_rate = sort_by_mortality_rate(deaths, names)
print(mortality_rate)
# Calculating Hurricane Maximum Damage
popped_item = converted_damage_1.pop(0)
popped_item = converted_damage_1.pop(1)
popped_item = converted_damage_1.pop(4)
popped_item = converted_damage_1.pop(12)
def most_damaging_hur(converted_damage, names):
  biggest_damage = 0
  index = 0
  for damage in converted_damage:
      if damage > biggest_damage:
        biggest_damage = damage
        index+=1
  index = converted_damage.index(biggest_damage)
  name = names[index]
  return "biggest damage was caused by hurricane {} and it did {}$ damage".format(name, biggest_damage)
# find highest damage inducing hurricane and its total cost
most_damaging = most_damaging_hur(converted_damage_1, names)
print(most_damaging)

# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}