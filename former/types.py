from error import Error
from label import Label
from widget import Widget


class FormType:
    label = Label()
    widget = Widget()
    error = Error()

    def __init__(self, options={}):
        self.label = Label()
        self.widget = Widget()
        self.error = Error()
        self.previous_data = options.get('previous_data')
        self.data = None

    def set_data(self, data):
        self.data = data

    def label(self):
        return self.label

    def widget(self):
        return self.widget

    def error(self):
        return self.error

    def is_valid(self):
        return self.error.is_valid()

# Text Fields
# TextType
# TextareaType
# EmailType
# IntegerType
# MoneyType
# NumberType
# PasswordType
# PercentType
# SearchType
# UrlType
# RangeType

# Choice Fields
# ChoiceType
# EntityType
# CountryType
# LanguageType
# LocaleType
# TimezoneType
# CurrencyType

# Date and Time Fields
# DateType
# DateIntervalType
# DateTimeType
# TimeType
# BirthdayType

# Other Fields
# CheckboxType
# FileType
# RadioType

# Field Groups
# CollectionType
# RepeatedType

# Hidden Fields
# HiddenType

# Buttons
# ButtonType
# ResetType
# SubmitType
