import json
from rest_framework.serializers import ModelSerializer
from base.models import Note
 

from datetime import datetime
from django.contrib.auth.models import User
from django.forms import IntegerField
from rest_framework import serializers
from base.models import Administrator, Airline_Companie, Flight, Product,Customer,Countrie,User_Role,Ticket

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
# ----------------------------------------------------------------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields= ('id','username', 'email')

        
    
    def get_User_name(self,obj):
        return obj.username
         
    def get_User(self,obj):
        return {
            "user_id":obj.id,
            "username":obj.username,
            "email":obj.email
        }

    def get_User_id(self,obj):
        return {
            "user_id":obj.id,
        }
# get_user_by_username(_

    def get_User_by_id(self,id):
        User= User.objects.get(user_id = id)
        return {
            "user_id":User.id,
            "username":User.username,
            "email":User.email
        }

    def get_User_by_username(self,id):
        User= User.objects.get(username = id)
        return {
            "user_id":User.id,
            "username":User.username,
            "email":User.email
        }

# ----------------------------------------------------------------------------------------------------------
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields= ('id','desc', 'price')
        
    
    def get_Product_name(self,obj):
        return obj.desc
         
    def get_Products(self):
        ProductObj= Product.objects.all()
        res=[]
        for obj in ProductObj:
            res.append({
                "prod_id":obj._id,
                "desc":obj.desc,
                "price":obj.price,
                "image": str(obj.image),
                "createdTime":obj.createdTime
              },)   
        return res

# ---------------------------------------------------------------------------------------------------------
class ProductSerializer2(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields= ('id','image','desc', 'price')
    
    def get_Product_name(self,obj):
        return obj.desc
    
    def get_Product2(self):
        ProductObj= Product.objects.all()
        res=[]
        for obj in ProductObj:
            res.append({
                "prod_id":obj._id,
                "status": str(obj.status),
                "desc":obj.desc,
                "price":obj.price,
                "image": str(obj.image),
                "createdTime":obj.createdTime
              },)   
        return res
        
         
    def get_Product_by_id(self,id):
        product= Product.objects.get(_id = id)
        return {
            "id": product._id,
            "status": str(product.status),
            "image": str(product.image), 
            "desc": product.desc,
            "price": product.price,
            "createdTime":product.createdTime
        }

    def get_all_products(self):
        res=[] #create an empty list
        for productObj in Product.objects.all(): 
            res.append(self.get_Product2(productObj))
        return res

# ----------------------------------------------------------------------------------------------------------
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        # fields= ('id','first_name','last_name', 'address', 'phone_no', 'credit_card_no', 'user_id', 'createdTime')
        fields= '__all__'
    def get_Customers_name(self,obj):
        return obj.user_id
         
    def get_Customers(self,objec):
        res=[]
        for i in objec:
            res.append({
                
            "id": i._id,
            "status": str(i.status),
            "first_name": i.first_name,
            "last_name": i.last_name,
            "address": i.address,
            "phone_no": i.phone_no,
            "first_name": i.first_name,
            "credit_card_no": i.credit_card_no,
            "user_id":(i.user_id_id), #!!!----not serelayzable whithout "str"----!!!!  make sure you fix it
            "createdTime": i.createdTime
            },)   
        return res


    def get_Customers_by_id(self,id):
        customer= Customer.objects.get(_id = id)
        return {
     
            "id": customer._id,
            "status": str(customer.status),
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "address": customer.address,
            "phone_no": customer.phone_no,
            "first_name": customer.first_name,
            "credit_card_no": customer.credit_card_no,
            "user_id":(customer.user_id_id), #!!!----not serelayzable whithout "str"----!!!!  make sure you fix it
            "createdTime": customer.createdTime
          
        }

    def get_Customers_by_username(self,id):
        customer= Customer.objects.get(user_id_id = id)
        return {
     
            "id": customer._id,
            "status": str(customer.status),
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "address": customer.address,
            "phone_no": customer.phone_no,
            "first_name": customer.first_name,
            "credit_card_no": customer.credit_card_no,
            "user_id":(customer.user_id_id), #!!!----not serelayzable whithout "str"----!!!!  make sure you fix it
            "createdTime": customer.createdTime
          
        }

# ----------------------------------------------------------------------------------------------------------
class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Countrie
        fields= '__all__'
        # fields= ('id','country_name','image')
    
    def get_Countries_name(self,obj):
        return obj.desc
    
    def get_Countries_id(self,obj):
        return obj._id
         
    def get_Countries(self,objec):
        res=[]
        for i in objec:
            res.append({
                
            "id": i._id,
            "status": str(i.status),
            "country_name": i.country_name,
            "image": str(i.image),
            },)   
        return res

    


    def get_Countries_by_id(self,id):
        country= Countrie.objects.get(_id = id)
        return {
            "id": country._id,
            "status": str(country.status),
            "country_name": country.country_name,
            "image": str(country.image),
            }

# ----------------------------------------------------------------------------------------------------------
class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:

        model =Administrator
        fields= '__all__'
        # fields= ('id','status','first_name','last_name','user_id','createdTi')
    
    def get_Administrators_name(self,obj):
        return obj.desc
         
    def get_Administrators(self,objec):
        res=[]
        for i in objec:
            res.append({
                
            "id": i._id,
            "status": str(i.status),
            "first_name": i.first_name,
            "last_name": str(i.last_name),
            "user_id": str(i.user_id),
            "createdTime": i.createdTime,
          
            },)   
        return res


    def get_Administrator_by_id(self,id):
        country= Administrator.objects.get(_id = id)
        return {
            "id": country._id,
            "status": str(country.status),
            "first_name": country.first_name,
            "last_name": str(country.last_name),
            "user_id": str(country.user_id),
            "createdTime": country.createdTime,
            
            }

# ----------------------------------------------------------------------------------------------------------
class Airline_CompaniesSerializer(serializers.ModelSerializer):
    class Meta:

        model =Airline_Companie
        fields= '__all__'
        # fields= ('id','status','company_name','country_id','user_id','createdTime')
    
    def get_Airline_Companie_name(self,obj):
        return obj.company_name
    
    def get_Airline_Companie_id(self,obj):
        return obj._id
         
    def get_Airline_Companies(self,objec):
        res=[]
        for i in objec:
            res.append({
            # ('id','status','company_name','country_id','user_id','createdTime')
            "id": i._id,
            "status": str(i.status),
           
            "company_name": str(i.company_name),
            "country_id": str(i.country_id),
            "user_id": str(i.user_id),
            "createdTime": i.createdTime,
          
            },)   
        return res

    def get_Airline_Company_by_id(self,id):
        country= Airline_Companie.objects.get(_id = id)
        # ('id','status','company_name','country_id','user_id','createdTime')
        return {
            "id": country._id,
            "status": str(country.status),
            "company_name": str(country.company_name),
            "country_id": str(country.country_id),
            "user_id": str(country.user_id),
            "createdTime": country.createdTime,
            }

    def get_Airline_Company_by_name(self,name):
        company= Airline_Companie.objects.get(company_name = name)
        return {
     
            "id": company._id,
            "status": str(company.status),
            "company_name": str(company.company_name),
            "country_id": str(company.country_id),
            "user_id": str(company.user_id),
            "createdTime": company.createdTime,
        }

    def add_new_Airline_Company(self,obj):
        # ('id','status','company_name','country_id','user_id','createdTime')
        return {
            "id": obj._id,
            "status": str(obj.status),
            "company_name": str(obj.company_name),
            "country_id": str(obj.country_id),
            "user_id": str(obj.user_id),
            "createdTime": obj.createdTime,
            
            }

# ----------------------------------------------------------------------------------------------------------
class FlightsSerializer(serializers.ModelSerializer):
    airline_company_id= Airline_CompaniesSerializer()
    origin_country_id= CountriesSerializer()
    destination_country_id= CountriesSerializer()
    class Meta:
        model =Flight
        fields= '__all__'
        # fields= ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
        # depth=1


    def get_Flights_name(self,obj):
        return obj.company_name

    def get_Flights_id(self,obj):
        return obj.id
         
    def get_Flights(self,objec):
        res=[]
        for i in objec:
            # print((i.origin_country_id).country_name)
            res.append({
            # ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
            "id": i._id,
            "status": str(i.status),
            "airline_company_id": (i.airline_company_id).company_name,
            "origin_country_id": (i.origin_country_id).country_name,
            "destination_country_id": (i.destination_country_id).country_name,
            "landing_time": i.landing_time,
            "remaining_tickets": i.remaining_tickets,
            "createdTime": i.createdTime,
            },)   
        return res


    def get_Flights_by_id(self,id):
        country= Flight.objects.get(_id = id)
       # ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
        return {
            "id": country._id,
            "status": str(country.status),
            "airline_company_id":Airline_CompaniesSerializer().get_Airline_Companie_id(country.airline_company_id),
            "origin_country_id": CountriesSerializer().get_Countries_id(country.origin_country_id),
            "destination_country_id": CountriesSerializer().get_Countries_id(country.destination_country_id),
            "departure_time": country.departure_time,
            "landing_time": country.landing_time,
            "remaining_tickets": country.remaining_tickets,
            "createdTime": country.createdTime,
            
            }

    def get_flights_by_airline_id(self,airline_company_id):
        country= Flight.objects.get(airline_company_id = airline_company_id)
       # ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
        return {
            "id": country._id,
            "status": str(country.status),
            "airline_company_id":Airline_CompaniesSerializer().get_Airline_Companie_id(country.airline_company_id),
            "origin_country_id": CountriesSerializer().get_Countries_id(country.origin_country_id),
            "destination_country_id": CountriesSerializer().get_Countries_id(country.destination_country_id),
            "departure_time": country.departure_time,
            "landing_time": country.landing_time,
            "remaining_tickets": country.remaining_tickets,
            "createdTime": country.createdTime,
            
            }

# 2 fuctions dont finishd
    def get_arrival_flights_next_12_h_by_departure(self,id):
        Flight= Flight.objects.get(destination_country_id = id)
        if Flight.landing_time >= datetime.now()+12:
       # ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
            return {
                "id": Flight._id,
                "status": str(Flight.status),
                "airline_company_id":Airline_CompaniesSerializer().get_Airline_Companie_id(Flight.airline_company_id),
                "origin_country_id": CountriesSerializer().get_Countries_id(Flight.origin_country_id),
                "destination_country_id": CountriesSerializer().get_Countries_id(Flight.destination_country_id),
                "departure_time": Flight.departure_time,
                "landing_time": Flight.landing_time,
                "remaining_tickets": Flight.remaining_tickets,
                "createdTime": Flight.createdTime,

                }
        else:return {"no":"flights"}

    def get_departure_flights_next_12_h(self,origin_country_id):
        Flight= Flight.objects.get(origin_country_id = origin_country_id)
        if Flight.landing_time >= datetime.now()-12:
       # ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
            return {
                "id": Flight._id,
                "status": str(Flight.status),
                "airline_company_id":Flight.airline_company_id,
                "origin_country_id": Flight.origin_country_id,
                "destination_country_id": Flight.destination_country_id,
                "departure_time": Flight.departure_time,
                "landing_time": Flight.landing_time,
                "remaining_tickets": Flight.remaining_tickets,
                "createdTime": Flight.createdTime,

                }

        else:return {"no":"flights"}


# get_flights_by_parameters
    def get_Flights_by_parameters(self,id,origin_country_id,destination_country_id):
        country= Flight.objects.filter(_id = id , origin_country_id = origin_country_id , destination_country_id = destination_country_id)
       # ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
        return {
            "id": country._id,
            "status": str(country.status),
            "airline_company_id":Airline_CompaniesSerializer().get_Airline_Companie_id(country.airline_company_id),
            "origin_country_id": CountriesSerializer().get_Countries_id(country.origin_country_id),
            "destination_country_id": CountriesSerializer().get_Countries_id(country.destination_country_id),
            "departure_time": country.departure_time,
            "landing_time": country.landing_time,
            "remaining_tickets": country.remaining_tickets,
            "createdTime": country.createdTime,
            
            }

# ----------------------------------------------------------------------------------------------------------
class User_RolesSerializer(serializers.ModelSerializer):
    class Meta:

        model =User_Role
        fields= '__all__'
        # fields= ('id','status','first_name','last_name','user_id','createdTi')
    
    def get_User_Roles_name(self,obj):
        return obj.desc
         
    def get_User_Roles(self,objec):
        res=[]
        for i in objec:
            res.append({

                # ('id','status','role_name','createdTime')
                
            "id": i._id,
            "status": str(i.status),
            "role_name": i.role_name,
            # "last_name": str(i.last_name),
            "createdTime": i.createdTime,
          
            },)   
        return res


    def get_User_Role_by_id(self,id):
        country= User_Role.objects.get(_id = id)
        return {
            "id": country._id,
            "status": str(country.status),
            "first_name": country.role_name,
            "createdTime": country.createdTime,
            
            }

# ----------------------------------------------------------------------------------------------------------
class TicketsSerializer(serializers.ModelSerializer):
    class Meta:

        model =Ticket
        fields= '__all__'
        # fields= ('id','status','flight_id','costumer_id','createdTime')

    def get_Tickets_name(self,obj):
        return obj.company_name
         
    def get_Tickets(self,objec):
        res=[]
        for i in objec:
            print(i._id,"--------------------------------------------")
            res.append({
            # ('id','status','flight_id','costumer_id','createdTime')
            "id": i._id,
            "status": str(i.status),
            "flight_id": str(i.flight_id),
            "costumer_id": str(i.costumer_id),
            "createdTime": i.createdTime,
        
            },)   
        return res


    def get_Tickets_by_id(self,id):
        country= Ticket.objects.get(_id = id)
       # ('id','status','flight_id','costumer_id','createdTime')
        print(country.flight_id)
        print("-----------------------------------------")
        return {
            "id": country._id,
            "status": str(country.status),
            "flight_id": str(country.flight_id),
            "costumer_id": str(country.costumer_id),
            "createdTime": country.createdTime,
            
            }


    # get_tickets_by_customer(_customer_id bigint)
    def get_Tickets_by_customer_id(self,id):
        # ('id','status','flight_id','costumer_id','createdTime')
        Tickets= Ticket.objects.filter(costumer_id = id)#not set as unicue in models.py
        res=[]
        for i in Tickets:
            res.append({
            "id": i._id,
            "status": str(i.status),
            "flight_id": str(i.flight_id),
            "costumer_id": str(i.costumer_id),
            "createdTime": i.createdTime,
            },)
        print("-----------------------------------------")
        return 

  