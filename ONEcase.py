class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        # Индекс внешнего списка
        self.outer_cursor = 0
        # Индекс внутри текущего подсписка
        self.inner_cursor = 0
        return self

    def __next__(self):
        # Пока мы не прошли все подсписки
        while self.outer_cursor < len(self.list_of_list):
            current_list = self.list_of_list[self.outer_cursor]
            
            # Проверяем, есть ли еще элементы в текущем подсписке
            if self.inner_cursor < len(current_list):
                item = current_list[self.inner_cursor]
                self.inner_cursor += 1
                return item
            
            # Если элементы кончились, переходим к следующему подсписку
            self.outer_cursor += 1
            self.inner_cursor = 0
            
        raise StopIteration
