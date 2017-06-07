class Label:
    def __init__(self, options={}):
        self.name = options.get('name', '')
        self.class_name = options.get('class', '')
        self.field_name = options.get('field_name', '')

    def __str__(self):
        return '<lable class="{}" for="{}">{}</label>'.format(
            self.class_name, self.field_name, self.name)

    def get_label(self):
        return self.__str__()
