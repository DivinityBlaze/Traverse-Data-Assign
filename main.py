# Read the survey data file
survey_file = open('data/survey-results.txt', 'r')

# Read the number data file
number_file = open('data/number-data.txt', 'r')

# Read the age data file
age_file = open('data/age-data.txt', 'r')


# Analyze and print survey data
yes = 0
no = 0
maybe = 0
for line in survey_file:
    if 'Yes' in line:
        yes += 1
    elif 'Maybe' in line:
        maybe += 1
    elif 'No' in line:
        no += 1
print("Expected Results: Yes (", yes , "), No (", no , "), Maybe (", maybe, "),")


# Analyze and print age data
below18 = 0
b18_35 = 0
b_36_65 = 0
above_65 = 0
for age in age_file:
    if int(age) < 18:
        below18 += 1
    elif 18 <= int(age) <= 35:
        b18_35 += 1
    elif 36 <= int(age) <= 65:
        b_36_65 += 1
    else:
        above_65 += 1
print("Age Distribution: Under 18 (", below18 , "), 18 to 35 (", b18_35 , "), 36 to 65 (", b_36_65 , "), Above 65 (", above_65 ,")")


# Analyze and print number data
even = 0
odd = 0
for data in number_file:
    if int(data) % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number Properties: Even (", even , ") Odd (" , odd , ")")