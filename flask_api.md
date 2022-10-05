# FLASK API

Документ описывает запросы, которые *адекватно* может обработать API.

### Формат JSON

> Документ может включать в себя параметры ***name*** и ***password***, тип переменных *string*.

### Доступные методы:

- ***GET***

	> Позволяет получить всех пользователей в виде 
	> списка JSON объектов.

	- ID пользователя
	- Имя пользователя
	- Пароль пользователя
	
	**URL: http://localhost:3005/music**
	
	![get_result](get_result.png)

- ***POST***

	> Позволяет добавить пользователя 
	> в базу данных.

	*Принимает строго указанный формат JSON.*
	
	**URL: http://localhost:3005/music**
	
	![get_result](post_result.png)

- ***PUT***

	> Позволяет изменить данные пользователя
	> с указанным ID.

	*Пароль или логин может быть не указан,
	и он не подвергнется изменению*
	
	**URL: http://localhost:3005/music/id**
	
	![get_result](put_result.png)

- ***DELETE***

	> Позволяет удалить пользователя
	> с указанным ID.

	**URL: http://localhost:3005/music/id**
	
	![get_result](delete_result.png)
