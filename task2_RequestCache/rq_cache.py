class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}

    @property
    # возврат самого старого элемента
    def cache(self):
        return next(iter(self.cache_dict))

    @cache.setter
    # добавление нового элемента
    def cache(self, new_elem):
        if len(self.cache_dict) >= self.capacity:
            oldest_key = next(iter(self.cache_dict))
            del self.cache_dict[oldest_key]  # удаление самого старого элемента
        self.cache_dict[new_elem[0]] = new_elem[1]  # добавляение нового элемента

    # вывод словаря
    def print_cache(self):
        print("\nLRU Cache:")
        for key, value in self.cache_dict.items():
            print("{key} : {value}".format(key=key, value=value))
        print()

    # получение значения по ключу из словаря
    def get(self, key):
        return self.cache_dict.get(key)


if __name__ == '__main__':
    # Создаём экземпляр класса LRU Cache с capacity = 3
    cache = LRUCache(3)

    # Добавляем элементы в кэш
    cache.cache = ("key1", "value1")
    cache.cache = ("key2", "value2")
    cache.cache = ("key3", "value3")

    # # Выводим текущий кэш
    cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

    # Получаем значение по ключу
    print(cache.get("key2"))  # value2

    # Добавляем новый элемент, превышающий лимит capacity
    cache.cache = ("key4", "value4")

    # Выводим обновлённый кэш
    cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
