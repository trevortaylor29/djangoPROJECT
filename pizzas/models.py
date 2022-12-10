from django.db import models


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=255)
    image_url = models.URLField()
    def get_image_url(self):
        images = {
            1: "https://www.pngitem.com/pimgs/m/504-5040768_meat-lovers-pizza-hd-png-download.png",
            2: "https://www.pngitem.com/pimgs/m/525-5257824_tropical-hawaiian-pizza-hut-hd-png-download.png",
        
        }
        return images.get(self.id)

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=255)

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=255)
    comment_text = models.TextField()