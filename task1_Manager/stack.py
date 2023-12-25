# Стэк
class Stack():

    def __init__(self):
        """Constructor"""
        self.stack_list: list = []

    # Добавление элемента в стек
    def add_elem(self, new_elem: tuple):
        self.stack_list.append(new_elem)

    # Удаление элмента из стека
    def del_elem(self):
        del self.stack_list[-1]
        return self.stack_list


# Менеджер задач
class TaskManager(object):

    def __init__(self):
        self.task_stack = Stack()
        self.manager_list = self.task_stack.stack_list

    # добавление новой задачи в список дел
    def new_task(self, task: str, priority: int):
        task_record: tuple = (task, priority)
        if len(self.manager_list) == 0:
            self.task_stack.add_elem(task_record)
        match: bool = False
        del_task_index: int = -1
        for i in range(len(self.manager_list)):
            if task_record[0] == self.manager_list[i][0]:
                match = True
                # обновление приоритета задачи, если она уже есть в списке дел
                if task_record[1] != self.manager_list[i][1]:
                    del_task_index = i  # сохранение индекса кортежа (задача, приоритет) для дальнейшего удаления
                    match = False
        if not match:
            self.task_stack.add_elem(task_record)  # добавление задачи, если такой ещё нет в списке дел
        if del_task_index != -1:
            self.manager_list.pop(del_task_index) # удаление кортежа со старым приоритетом задачи

    # удаление верхней задачи из списка дел
    def drop_last_task(self):
        self.manager_list = self.task_stack.del_elem()

    # Форматированный вывод списка дел
    def print(self):
        print("\nРезультат:")
        self.manager_list.sort(key=lambda x: x[1])
        task_dict = {}
        # объединение задач с одинаковыми приоритетами в одну запись
        for i in range(len(self.manager_list)):
            if self.manager_list[i][1] in task_dict.keys() and self.manager_list[i][0] not in task_dict.values():
                old_task: str = task_dict[self.manager_list[i][1]]
                task_dict[self.manager_list[i][1]] = "{old_task}; {new_task}".format(old_task=old_task,
                                                                                     new_task=self.manager_list[i][0])
            else:
                task_dict[self.manager_list[i][1]] = self.manager_list[i][0]
        for priority, task in task_dict.items():
            print("{priority}: {task}".format(priority=priority, task=task))


# Основная программа
if __name__ == '__main__':
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    manager.new_task("поесть", 2)
    manager.print()

    manager.new_task("поесть", 3)
    manager.new_task("сдать дз", 2)
    # manager.drop_last_task()
    manager.print()
