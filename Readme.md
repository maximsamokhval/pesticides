# База данных активных веществ Евросоюза

## Сборка

Для запуска выполнить команду 

``` cmd
    docker-compose up -d 
```

В переменных окружения [docker-compose.yml](docker-compose.yml) прописать корректные данные

```yml

environment:
    ENDPOINT: URI
    ENDPOINT_LOGIN: login 
    ENDPOINT_PASSWORD: pass

```


## FrontEnd

- [Bootstrap Table](https://bootstrap-table.com/) 
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)


## BackEnd:

- Python 3.11
- Flask==3.0.0