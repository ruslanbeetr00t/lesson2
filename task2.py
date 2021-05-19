first_name = 'Ruslan'
last_name = 'Khavrenko'
print(f'Hello {first_name} {last_name}')

#or

first_name = 'Ruslan'
last_name = 'Khavrenko'
s = ('Hello {} {}')
print(s.format (first_name,last_name))

#or
first_name = 'Ruslan'
last_name = 'Khavrenko'
print('Hello {0} {1}'.format(first_name, last_name))

#or
first_name = 'ruslan'
last_name = 'khavrenko'
full_name = first_name.title()+' '+last_name.title()
print('Hello '+ full_name)