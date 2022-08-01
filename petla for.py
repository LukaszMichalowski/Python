persons=['Elizabeth','Steven','Sebastian','Margaret','Svetlana','Raphael']
domain='mycompany.com'

for person in persons:
    email=person+'@'+domain
    print('email for\t',person,'\tis\t',email)
else:
    print('---end of the list--')
