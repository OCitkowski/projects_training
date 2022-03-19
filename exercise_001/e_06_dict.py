alien_0 = {}
alien_0['color'] = 'green'
alien_0['zvert'] = '09_ff'
alien_0['color2'] = 'green'

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
print(f'**********01************')
for name in alien_0:
    print(f"{name} // {alien_0[name]}")
print(f'***********02***********')
for key in sorted(alien_0.keys()):
    print(f' {key}')
print(f'*********03*************')
for val in alien_0.values():
    print(f'***** {val}')
print(f'*********04*************')
my_set = set(alien_0.values())
print(f'{alien_0.values()}')
print(f'{my_set}')
# **********************************6.1**************************
alients = []
for alient_number in range(30):
    new_alient = {'color': 'green', 'points': 100, 'speed': 200}
    alients.append(new_alient)
print(f' total alients = {len(alients)} {alients[0:2]}')

i = len(alients)
while i != 0:
    i -= 1
    if i%2 == 0:
        alients[i]['color'] = 'red'
        alients[i]['speed'] = 55
for alient in alients:
    print(alient)
#*****************************6.2****************************************
my_dict = {}
my_list = [200, 'red', 'low']

i = 5
while i != 0:
    i -= 1
    my_dict[f'alient{i}'] = my_list
print(f'{sorted(my_dict)}')