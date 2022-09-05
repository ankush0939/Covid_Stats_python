from covid import Covid
covid = Covid()
print('\n')
for y in covid.get_data():
    cases = covid.get_status_by_country_name(y.get("country"))
    for x in cases:
        print(x,":",cases[x]);
    print('\n')