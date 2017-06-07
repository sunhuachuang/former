# Base Form
class Form:
    name = None

    def __init__(self, obj=None):
        self.is_valid = None
        self.is_submit = False
        self.types = []
        self.obj = obj

    def handle(self, request):
        if self.name is None:
            self.name = self.__class__.__name__.casefold()

        data = request.get(self.name, {})

    def is_submit(self):
        return self.is_submit

    def is_valid(self):
        if self.is_valid is None:
            for child_type in self.types:
                if not child_type.is_valid:
                    self.is_valid = False
                    break
            else:
                self.is_valid = True

        return self.is_valid
