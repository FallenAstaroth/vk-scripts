# Text Faker

Замена значения элементов до их рендеринга на странице.

## Навигация
* [Установка](#Установка)
  * [GitHub](#GitHub)
  * [GreasyFork](#GreasyFork)
* [Использование](#Использование)

## Установка
Для работы скрипта нужно установить расширение [Tampermonkey](https://www.tampermonkey.net/).

### GitHub
1. Копируем содержимое файла [text.faker.js](https://github.com/FallenAstaroth/scammers-scripts/blob/master/VoiceStealer/voice.stealer.js).
2. Нажимаем на иконку Tampermonkey в меню с расширениями.
3. Нажимаем `Create a new script`.
4. Вставляем код из файла [text.faker.js](https://github.com/FallenAstaroth/scammers-scripts/blob/master/VoiceStealer/voice.stealer.js).

### GreasyFork
1. Открываем [страницу со скриптом](https://greasyfork.org/ru/scripts/461584-text-faker).
2. Нажимаем `Установить`.

## Использование
1. Открываем сайт, на котором нужно заменить текст.
2. Кликаем правой кнопкой мышки по тексту, затем `Просмотреть код элемента`.
3. Находим в `html` блок с текстом.
4. Кликаем по нему правой кнопкой мышки, затем `Copy` -> `Copy Selector`.
5. Открываем скрипт в [Tampermonkey](https://www.tampermonkey.net/).
6. Заполняем поле `elements`:
   ```javascript
   const elements = [
        {
            selector: "Первый селектор",
            text: "Текст 1"
        },
        {
            selector: "Второй селектор",
            text: "Текст 2"
        }
    ]
   ```
7. Заменяем ссылку из 7 строки на ссылку нужного сайта:
   ```javascript
   // @match        https://github.com/FallenAstaroth/scammers-scripts
   ```
8. Перезагружаем страницу сайта и видим наши значения вместо стандартных.