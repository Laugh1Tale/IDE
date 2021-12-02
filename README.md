# Запуск изображений #

## изображение до: ##

![Getting Started](scale1200.jpg)

## изображение после filter, filter_with_filename: ##
![Getting Started](res.jpg)
block_size = 10, grayscale = 50

## изображение после old_filter: ##
![Getting Started](res1.jpg)
block_size = 10, grayscale = 50

Но т.к. он не исправлен нормального результата не выходит, в остальных случаях результирующее изображение в процессе каждой фильтрации получилось одинаковым, из-за одинаковых параметров фильтрации.

# Profiling #
## old filter: ##

![Getting Started](images/old_filter_profile.jpg)

## filter profile: ##

![Getting Started](images/filter_profile.jpg)

## filter with filename profile: ##

![Getting Started](images/filter_with_filename_profile.jpg)

Как видно по фотографиям выше при запуске старого фильтра(ввод данных в котором отстутствует) на обработку изображения тратится большое количество времени. После запуска исправленного фильтра мы видим, что время работы программы увеличилось, однако замечаем что большая часть времени ушла на ввод данных, а обработка изображения занимает в разы меньше времени. Для объективности тестов мы смотрим результат работы фильтра с уже введенными параметрами, и объективно видим насколько быстрее начало обрабатываться изобраение.

# Doc-тесты #

## функция, к которой написаны doc-тесты: ##
![Getting Started](images/doctests.png)

## результаты doc-тестов: ##
![Getting Started](images/doctests1.png)

1)  49 // 50 = 0;
    0 * 50 = 0;

    0=0✅

2)  50 // 50 = 1;
    1 * 50 = 50;

    50=50✅

3)  51 // 50 = 1;
    1 * 50 = 50;
    
    50=50✅

предполагаемые результаты совпали с фактическими ✅✅✅

# Debug #
## размеры изображения: ##
![Getting Started](images/debug.jpg)
## размеры мозаики: ##
![Getting Started](images/debug1.png)
## градация серого: ##
![Getting Started](images/debug2.png)


Всю необходимую информацию нашли.✅✅✅