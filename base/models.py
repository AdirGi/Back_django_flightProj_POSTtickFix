

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Note(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    body = models.TextField() 
    desc = models.CharField(max_length=50,null=True,blank=True)
 
 
class Profile(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    desc = models.CharField(max_length=50,null=True,blank=True)
    
# -----------------------------------------------------------------------------------------------------

class Product(models.Model):
    status=models.BooleanField(default=True)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
    
    def __str__(self):
     	return self.desc 

# -----------------------------------------------------------------------------------------------------

class Customer(models.Model):
    status=models.BooleanField(default=True)
    _id=models.AutoField(primary_key=True,editable=False)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    phone_no = models.CharField(max_length=50,null=True,blank=True)
    credit_card_no = models.CharField(max_length=50,null=True,blank=True)
    user_id =models.ForeignKey(User,related_name="costumer_id",on_delete=models.SET_NULL,null=True)#unicue
    
    createdTime=models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
     	return self.first_name

# -----------------------------------------------------------------------------------------------------


class Countrie(models.Model):
    status=models.BooleanField(default=True)
    country_name = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    _id=models.AutoField(primary_key=True,editable=False)
    

    def __str__(self):
     	return str(self._id)
        # '%s %s' % (self.country_name, self.last_name)
# -----------------------------------------------------------------------------------------------------
class Administrator(models.Model):
    status=models.BooleanField(default=True)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return self.first_name

# -----------------------------------------------------------------------------------------------------



class Airline_Companie(models.Model):
    status=models.BooleanField(default=True)
    company_name = models.CharField(max_length=50,null=True,blank=True)
    country_id =models.ForeignKey(Countrie,on_delete=models.SET_NULL,null=True)
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return self.company_name

# -----------------------------------------------------------------------------------------------------


class Flight(models.Model):
    status =models.BooleanField(default=True)
    user_id =models.ForeignKey(User,on_delete=models.SET_NULL,null=True) 
    airline_company_id =models.ForeignKey(Airline_Companie,related_name='airline_company_id',on_delete=models.SET_NULL,null=True)
    origin_country_id =models.ForeignKey(Countrie,related_name='origin_country_id',on_delete=models.SET_NULL,null=True)
    destination_country_id = models.ForeignKey(Countrie,related_name='destination_country_id',on_delete=models.SET_NULL,null=True)      #models.ForeignKey(origin_country_id,on_delete=models.SET_NULL,null=True) #make erorr ask eyal
    departure_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    landing_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    remaining_tickets = models.IntegerField(null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)

    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return str(self._id)

# -----------------------------------------------------------------------------------------------------

class User_Role(models.Model):
    status=models.BooleanField(default=True)
    role_name = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):  
     	return self.role_name


# -----------------------------------------------------------------------------------------------------

class Ticket(models.Model):
    # dont forget to make those FK uniqu becuse 1 costumer (traveler) can have 1 tiket 
    status=models.BooleanField(default=True)
    flight_id=models.ForeignKey(Flight,related_name='flight_id',on_delete=models.SET_NULL,null=True)#uniqu ,related_name='flight_id'
    costumer_id =models.ForeignKey(Customer,related_name='costumer_id',on_delete=models.SET_NULL,null=True)#uniqu ,related_name='costumer_id'
    
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
     	return str(self._id)