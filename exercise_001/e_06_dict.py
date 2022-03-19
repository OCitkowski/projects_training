alien_0 = {}
alien_0['color'] = 'green'

# alen_0 = {'color': 'green', 'points': 5}
# print(f" {alen_0}")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# print(f'{alien_0}')
alien_0['x_position'] = 444
alien_0['z_position'] = 87.5
# del alien_0['color']
# print(f"{alien_0}")
pointss = alien_0.get('clll', 'no points')
# print(f"{pointss}")

for key, val in alien_0.items():
    print(f"key = {key},     val =  {val}")
print(f'**********************')
for name in alien_0:
    print(f"{name} // {alien_0[name]}")
print(f'**********************')


