wall_length = float(input('Enter wall length: '))
wall_width = float(input('Enter wall width: '))
wall_height = float(input('Enter wall height: ')) + 0.1
room_perimetr = (wall_length + wall_width) * 2
wallpaper_width = float(input('Enter wallpaper width: '))
cloth_quantity = int(round(room_perimetr / wallpaper_width))
wallpaper_length = float(input('Enter wallpaper length: '))
cloth_in_one_roll = int(wallpaper_length / wall_height)
roll_quantity = int(cloth_quantity / cloth_in_one_roll) + 1
print('')
print("You will need", roll_quantity, "wallpaper rolls")