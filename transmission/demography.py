#proportion of each five year cohort 15-19, 20-24,..., 55-60
age_proportions = [25, 61, 15, 5, 2, 2, 1, 1, 1]

age_cumulative_proportions = []
x = 0
total = sum(age_proportions)

for item in age_proportions:
    x += item
    age_cumulative_proportions.append(x / total)

#gender ratio
#female 59 male 41
gender_proportions = [0.59, 0.41]
