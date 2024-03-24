a = input('Digite algo: ')

print('{} é alfabético? '.format(a), a.isalpha())
print('{} é alphanumérico? '.format(a), a.isalnum())
print('{} é só números? '.format(a), a.isnumeric())
print('{} está tudo em maíusculo? '.format(a), a.isupper())

#para uasr o .format, ele sempre tem que vir antes da verificação