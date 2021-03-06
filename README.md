# QA_SIMPLE_API
---
## Создание и тестирование приложения для работы с API

В этом Readme будет описан процесс создания приложаения с функциями API и его тестировка.


Начнем по порядку.
Чтобы написать приложения для работы с API, нужно было разобраться как работают его функции. А лучшего обучения, чем практика - не придумать!
Поэтому я реализовал все функции указанные в ТЗ используя библиотеку **request**.

![image](https://user-images.githubusercontent.com/71213226/145867856-542c5809-2e42-42f5-8fdf-6e70420dc145.png)

Код каждой функции вы можете увидеть в директории **API**, я же приведу результаты первоначальной работы (все скриншоты кликабельны!):

Создание новой карточки животного **без фото**:
![image](https://user-images.githubusercontent.com/71213226/145868196-7cb564ba-2880-403e-a0aa-09bf49444403.png)

Получение ключа API:
![image](https://user-images.githubusercontent.com/71213226/145868480-a9fdb22c-22e7-453b-ae95-a2f942abbd60.png)

Получение списка **My_Pets**:
![image](https://user-images.githubusercontent.com/71213226/145868556-6e8ca465-a116-40b1-b367-1126bb465c8c.png)

Создание новой карточки животного:
![image](https://user-images.githubusercontent.com/71213226/145868912-3d526d0a-f0c4-492f-84d0-6bdcf119e7d6.png)

Добавить фото для животного:
![image](https://user-images.githubusercontent.com/71213226/145868963-7dddb7c6-4e11-407d-bf35-c360818a85df.png)

Удалить карточку животного:
![image](https://user-images.githubusercontent.com/71213226/145869171-5a047f0a-cb87-4345-9804-4b73bcea9dd2.png)

Обновить информацию о животном:
![image](https://user-images.githubusercontent.com/71213226/145869231-8fc7ebbd-2ea2-4d85-88fd-8caf1485b267.png)

Каждая из этих функций была проверена мной, и все действия приложения отображаются на сайте.
---

После реализации функций API пришло время протестировать каждую из них.
Для этого я использовал библиотеку **Pytest**, подключив ее так же, как и в прошлом задании:
https://github.com/wwatchenjoy/QA_File_manager

Так как в ТЗ было указано использовать как **фикстуры**, так и **параметризацию**, то я использовал обе возможности.

У нас используется 3 функции POST, поэтому для них и была применена параметризация:
![image](https://user-images.githubusercontent.com/71213226/145870780-a77ccb87-dd79-405b-987f-400d31437512.png)


В параметрах указаны не только положительные, но и отрицательные кейсы, отмеченные как **marks=pytest.mark.xfail**
![image](https://user-images.githubusercontent.com/71213226/145870945-e7807c7d-12c6-4cb6-9057-eef50a81228e.png)

Таким образом, ошибка в тест-кейсе отображается как ожидаемая, что не ломает тестировку.
![image](https://user-images.githubusercontent.com/71213226/145871157-e5a4052e-6516-4258-9dca-706363330431.png)

Так же тест по фикстуре был применен к единственной функции PUT:
![image](https://user-images.githubusercontent.com/71213226/145871287-4134389a-70d7-4e50-b779-15d1eb9417a9.png)

### Итоги
В процессе работы над этим заданием я изучил и самостоятельно создал простые функции API, а также протестировал их несколькими методами.
Всё представленное в репозитории и на скриншотах является рабочим проектом.











