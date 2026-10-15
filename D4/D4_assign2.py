#Tuple Example
print("--An Immutable Database Config Guard--")

database_config = ("sql.client-automation.com", 3306, 30)
print(f"Host = {database_config[0]}, Port = {database_config[1]}")
database_config[1] = 2837