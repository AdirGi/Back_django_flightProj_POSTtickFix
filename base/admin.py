from django.contrib import admin
from .models import Product,Customer,Countrie,Administrator,Airline_Companie,Flight,User_Role,Ticket,Profile

# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Countrie)
admin.site.register(Administrator)
admin.site.register(Airline_Companie)
admin.site.register(Flight)
admin.site.register(User_Role)
admin.site.register(Ticket)
admin.site.register(Profile)

