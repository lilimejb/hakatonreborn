# Краткая инструкция по использованию
```
Выбирайте категорию блюд, нажимая на интересующее, нажатием кнопок "+" и "-" регулируйте количество и
нажимайте "Добавить в корзину".
Как соберёте все нужные для вас блюда - переходите в корзину и оплачивай заказ.
Номер заказа будет написан после оплаты
Приятного аппетита!
```

#### Для оплаты используйте тестовую карту:<br/>
**Номер** - 1111 1111 1111 1026<br/>
**Дата**  - 12/22<br/>
**CVC**   - 000.<br/>

# Ссылка на бота
## https://t.me/stolovkatest_bot <br/>
# Мои контакты 
## tg-https://t.me/lilimejb <br/>vk-https://vk.com/lilimejb<br/> 

# Баги
В программе присутсвуют баги, которые можно было исправить при наличии большего количества времени

  * ## В корзину можно добавить отрицательное количество товаров
Решение проблемы:<br/>
```py
Изминить в файле handlers/dish_page.py строку 35

if action == "MINUS" and amount > 0:
    amount = int(amount) - 1
```
  * ## При частом нажатии на кнопки бот начинает долго загружаться
Решение проблемы:<br/>
```
Оптимизировать api
```

# Улучшения
Сейчас бот больше похож на версию закрытого бета теста, поэтому есть несколько улучшений которые можно сделать

  * ## Больше способов оплаты

Можно ввести оплату с помощью СБП или с помощью QR-кода на кассе
В первом случае бот будет создавать кнопку с встроенной ссылкой на оплату по СБП
Во втором телеграм будет присылать QR-код с которым можно будет подойти к кассиру и оплатить заказ наличными

  * ## Сделать в боте выбор локации для заказа

На данный момент реализован только заказ в столовой.
Так как у вуза есть ещё 2 предприятия можно сделать выбор места для заказа

 * ## Добавить комбо обед

В столовой университета присутсвуют комбо обеды, которые были добавлены
в базу данных и в api, но пока что не реализованы в самом боте

  * ## Связать бота с iikoapicloud

Так как столовая не предоставила доступа к своим базам в сервисе [iiko](https://iiko.ru/) и к его api - iikocloudapi,
api было написано вручную, что не позволяет сделать большое разнообразие блюд и раскрыть весь потенциал бота

  * ## Сделать бота-приложение

Для меня огромный плюс многих ботов - мало сообщений в чате
хотелось бы реализовать полное избавление от лишних сообщений

