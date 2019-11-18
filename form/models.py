from django.db import models
from django.core.mail import send_mail
import telebot
token='1040941161:AAGRKhQAsHaPsXVQH6nfuaE_Sap-9qnN878'
from telebot import types
bot= telebot.TeleBot(token)

class Form(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    Collage = models.BooleanField(default=False)
    Electronic_design = models.BooleanField(default=False)
    DreamArt = models.BooleanField(default=False)
    Print_no_edit= models.BooleanField(default=False)
    size_of_picture = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        send_mail('New Client', f'{self.telephone}', 'alquilar.cochee@gmail.com', ['alquilar.cochee@gmail.com'])
    
        if (self.Collage):
            self.completed="Коллаж"
        if (self.Electronic_design):
            self.completed="Электронный коллаж"
        if (self.DreamArt):
            self.completed="DreamAr"
        if (self.Print_no_edit):
            self.completed="Собственный дизайн"
    bot.send_message(chat_id='270129913', text="Новый клиент: имя: {} {}, телефон: {}, тип подарка: {}, размер холста: {}".format(self.firstName, self.lastName, self.telephone, self.completed, self.size_of_picture))
    bot.send_message(chat_id='208698986', text="Новый клиент: имя: {} {}, телефон: {}, тип подарка: {}, размер холста: {}".format(self.firstName, self.lastName, self.telephone, self.completed, self.size_of_picture))

            #bot.send_message(chat_id='270129913', text="Новый клиент: имя: {} {}, телефон: {}, тип подарка: {}, размер холста {}".format(self.firstName, self.lastName, self.telephone, self.completed, self.size_of_picture))

    def _str_(self):
        return self.firstName
