fuel_consumption_mid = float(input('Enter fuel consumption per 100 km: '))
fuel_consumption_1km = fuel_consumption_mid / 100
fuel = int(input('Enter fuel value: '))
fuel_range = (fuel / fuel_consumption_1km) - 20
print("Fuel range: ", round(fuel_range), 'km')
if fuel_range < 40:
    print('Attention: low fuel!')

