from django.contrib import admin


from .models import Comment, Pizza, Topping

admin.site.register(Comment)
admin.site.register(Pizza)
admin.site.register(Topping)