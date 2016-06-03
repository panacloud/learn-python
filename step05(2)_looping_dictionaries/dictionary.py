alien_0 = {"speed": "slow", "x_position": 0}
alien_1 = {"speed": "medium", "x_position": 0}
alien_2 = {"speed": "fast", "x_position": 0}
Aliens = [alien_0, alien_1, alien_2]
x_increment = 0

for item in Aliens:
    if item['speed'] == 'slow':
        x_increment = 1
        item['x_position'] = x_increment
        print('slow one')
    elif item['speed'] == 'medium':
        x_increment = 2
        item['x_position'] = x_increment
        print('medium one')
    else:
        x_increment = 3
        item['x_position'] = x_increment
        print('fast one')

print(Aliens)
