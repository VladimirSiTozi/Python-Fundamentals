my_dict= {'Toyota': {'corola': [1976, 1978, 1982, 2012], 'supra': {'color': 'red', 'year': [2000, 1993]}, 'prius': 1985},
          'WV': ['golf', 'polo', 'passat']}

print(f"Toyota model {my_dict['Toyota']}{my_dict['Toyota']['corola']}")

print(my_dict['Toyota']['supra']['color'])
print(my_dict['Toyota']['supra']['year'])


for year in my_dict['Toyota']['corola']:
    print(year)