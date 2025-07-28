from db_methods import insert_data
insert_data(5,"Raksh",1234,"rs@gmail.com")

from db_methods import delete_data 
delete_data(75)

from db_methods import update_data
update_data("Rakshu",55)

from db_methods import select_data
result=select_data()
print(result)
