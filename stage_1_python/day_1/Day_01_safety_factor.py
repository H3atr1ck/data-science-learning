material = 'ЖС6К'
ultimate_strength = 646 # Данные взял из открытого источника
stress = float(input('Введите напряжение, МПа: '))
if stress <= 0:
    print('Введено неверное напряжение, запас прочности посчитать нельзя. Напряжение должно быть > 0')
else:
    safety_factor = ultimate_strength / stress
    print(f'Материал {material}: запас прочности {safety_factor:.2f}')