        # Создаем кнопку для выбора категории
        category_button = Button(text='Выбрать категорию')
        category_button.bind(on_press=self.show_categories)
        layout.add_widget(category_button)
