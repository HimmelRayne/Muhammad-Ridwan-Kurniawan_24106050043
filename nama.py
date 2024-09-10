Name = str(input('Nama: '))
hobi = str(input('Hobi Kamu: '))
umur = int(input('Tahun Lahir: '))
jarak = float(input('Jarak Rumah ke UIN (KM): '))
print('- - - - - - - - - - - - -')
print('Hallo, ',Name)
print('Kamu suka ',hobi , ' ya? Hebat!')
print('Umur Kamu ' , 2024 - umur , ' tahun')
if jarak * 2 < 10.0:
    print('Pulang pergi ' , jarak * 2 , 'KM? Cukup dekat ya!')
if jarak * 2 > 10.0:
    print('Pulang pergi ' , jarak * 2 , 'KM? Jauh juga. . .')