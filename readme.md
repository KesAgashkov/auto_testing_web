# Проект автоматизированного кроссбраузерного тестирования веб-приложения https://test-stand.gb.ru/
## Основные задачи проекта:
1. Ускорить процесс тестирования веб-приложения
2. Добавить возможность тестирования веб-приложения на различных браузерах 
3. Реализовать тестирование с использованием DDT подхода (для быстрого внесения правок в тестовые сценарии)
4. Реализовать паттерн проектирования Page Object (для упрощения поддержки расширяющегося проекта и понимания кода командой)
5. В тестовом режиме добавить в проект блок тестирования API
6. Реализовать логирование на проекте с обработкой возникающих ошибок (для быстрого решения проблем)
7. Добавить автоматическую отправку отчётов по тестированию на email посредством SMTP протокола
## Результаты проекта:
1. Удалось реализовать класс BasePage с инициализацией драйвера и основными методами драйвера
2. На уровне модуля conftest.py была разработана фикстура с возможностью инициализации необходимого браузера (Chrome или Firefox)
3. В классе OperationsHelper были разработаны основные методы работы с веб-приложением, а также базовые функции тестирования API
4. В целях реализации принципа DDT подхода данные и локаторы были вынесены в отдельные файлы yaml
5. В двух модулях были разработаны тесты GUI и API веб-приложения
6. В модуле send_to_mail была реализована возможность сбора логов по работе проекта, двух отчётов по пройденным тестам и отправки их по завершении тестирования на email

Вся вышеописаная работа позволила существенно сократить время на тестирование API и GUI веб-приложения, а использование паттерна проектирования Page Object, наряду с DDT подходом, позволит более гибко и легко управлять проектом и расширять его по мере необходимости.

# Для запуска проекта необходимо
1. Клонировать проект с github
2. установить весь пакет использованных библиотек (python -m pip install -r requirements.txt)
3. выбрать в файле testdata.yaml нужный браузер (Chrome или Firefox)
4. в модуле send_to_mail указать с какого адреса и куда отправить файлы по завершении тестирования (код mail.ru можно найти в разделе: настройки -> пароль и безопасность -> внешние сервисы (разрешить для использования SMTP) и в паролях для внешних приложений есть код)
5. Для запуска всех тестов и отправки отчётов на email используйте pipeline в командной строке
### pytest .\test_api.py --html-report=report_api.html | pytest .\test_gui.py --html-report=report_gui.html | python .\send_to_mail.py