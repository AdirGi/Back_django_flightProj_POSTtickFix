from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from base.models import Administrator, Airline_Companie, Flight, Product,Customer,Countrie, Ticket, User_Role
from rest_framework import serializers
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from base.serializers import Airline_CompaniesSerializer, FlightsSerializer, ProductSerializer2, UserSerializer, ProductSerializer, CustomerSerializer,CountriesSerializer,AdministratorSerializer,User_RolesSerializer,TicketsSerializer,NoteSerializer
from rest_framework.response import Response
 
 
# from .serializers import NoteSerializer
from base.models import Note,User
 
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
 
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
 
    return Response(routes)
 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    print("innnn")
    user = request.user
    print(user)
    notes = user.note_set.all()
    print(notes)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


# register
@api_view(['POST'])
def addUser(request):
    try:
        User.objects.create_user(
            username=request.data["username"],
            email=request.data["email"],
            password=request.data["password"],
            # is_staff =request.data["is_staff"] ,
            # is_superuser =request.data["is_superuser"] 
            )
        return JsonResponse({"user_is_staff":"created!!!"} )
    except:
        return JsonResponse({"user_is_staff":"not created!!!"} )


 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNote(request):
    print(request.data)
    user = request.user
    Note.objects.create(body=request.data["notebody"],user=user)
    print(user)
    notes = user.note_set.all()
    print(notes)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# ---------------------------------------------------------------------------------------------------------------
def index(req):
    return JsonResponse('hello', safe=False)
 
# desc ,price,prodName,createdTime, _id
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def products(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response(ProductSerializer2().get_Product_by_id(id),status=status.HTTP_200_OK)

        else: 
            return Response(ProductSerializer2().get_Product2()) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})
        # ------------------------------------------
        

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



# ('id','first_name','last_name', 'address', 'phone_no', 'credit_card_no', 'user_id', 'createdTime')
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def customers(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response(CustomerSerializer().get_Customers_by_id(id))
        else: 
            CustomerObj= Customer.objects.all()
            serializer= CustomerSerializer(CustomerObj, many=True)
            print(CustomerObj)
            return Response(serializer.data) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Product.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Product.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Product.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



# ('id','country_name','image')- full CRUDE COMPLET! -NO ALL SERALIZER!!! -Remembr add the difultes to put and post
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def countries(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response(CountriesSerializer().get_Countries_by_id(id))

        else: 
            CountriesObj= Countrie.objects.all()
            serializer= CountriesSerializer(CountriesObj, many=True)
            return Response(serializer.data)


    if request.method == 'POST': #method post add new row
        Countrie.objects.create(country_name =request.data['country_name'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Countrie.objects.get (_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Countrie.objects.get(_id = id)
        temp.country_name =request.data['country_name']
        temp.save()
        return JsonResponse({'PUT': id})



# ('id','status','first_name','last_name','user_id','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def administrators(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response(AdministratorSerializer().get_Administrator_by_id(id))

        else: 
            administratorsObj= Administrator.objects.all()
            serializer= AdministratorSerializer(administratorsObj, many=True)
            return Response(serializer.data)
            # return Response(AdministratorSerializer().get_Administrators(administratorsObj)) #return array as json response

    if request.method == 'POST': #method post add new row
        Countrie.objects.create(country_name =request.data['country_name'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Countrie.objects.get (_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Countrie.objects.get(_id = id)
        temp.country_name =request.data['country_name']
        temp.save()
        return JsonResponse({'PUT': id})



# ('id','status','company_name','country_id','user_id','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def Airline_Companies(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response(Airline_CompaniesSerializer().get_Airline_Company_by_id(id))

        else: 
            AirlineCompaniesOBJ= Airline_Companie.objects.all()
            serializer= Airline_CompaniesSerializer(AirlineCompaniesOBJ, many=True)
            return Response(serializer.data)
            # return Response(Airline_CompaniesSerializer().get_Airline_Companies(CountriesObj)) #return array as json response

    if request.method == 'POST': #method post add new row
        Countrie.objects.create(country_name =request.data['country_name'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Countrie.objects.get (_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Countrie.objects.get(_id = id)
        temp.country_name =request.data['country_name']
        temp.save()
        return JsonResponse({'PUT': id})

# Flight
# ('id','status','airline_company_id','origin_country_id','destination_country_id','departure_time','landing_time','remaining_tickets','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def flights(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response(FlightsSerializer().get_Flights_by_id(id))

        else: 
            FlightsObj= Flight.objects.all()
            serializer= FlightsSerializer(FlightsObj, many=True)
            return Response(serializer.data)

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        Flight.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Flight.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Flight.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})



# ('id','status','role_name','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def User_Roles(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response(User_RolesSerializer().get_User_Role_by_id(id))

        else: 
            User_RolesObj= User_Role.objects.all()
            serializer= User_RolesSerializer(User_RolesObj, many=True)
            return Response(serializer.data)
            # return Response(User_RolesSerializer().get_User_Roles(CountriesObj)) #return array as json response

    if request.method == 'POST': #method post add new row
        print(request.data['desc'])
        desc =request.data['desc']
        User_Role.objects.create(desc=request.data['desc'] ,price=request.data['price'])
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= User_Role.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=User_Role.objects.get(_id = id)
        temp.price =request.data['price']
        temp.desc =request.data['desc']
        temp.save()
 
        return JsonResponse({'PUT': id})


# ('id','status','flight_id','costumer_id','createdTime')
@api_view(['GET','POST','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def Tickets(request,id):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return Response(TicketsSerializer().get_Tickets_by_id(id))

        else: 
            TicketsObj= Ticket.objects.all()
            # serializer= TicketsSerializer(TicketsObj, many=True)
            # return Response(serializer.data)
            return Response(TicketsSerializer().get_Tickets(TicketsObj)) #return array as json response

    if request.method == 'POST': #method post add new row
        idofcustfromtoken= 1 #add data from token
        Ticket.objects.create(flight_id_id= request.data['flight_id'] ,costumer_id = Customer.objects.get(_id = idofcustfromtoken)) #first(): costumer_id return set arry one variable 
        #remove 1 ticket from remaining tickets using flight id 
        return JsonResponse({'POST':"test"})

    if request.method == 'DELETE': #method delete a row
        temp= Ticket.objects.get (_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
        
    if request.method == 'PUT': #method delete a row
        temp=Ticket.objects.get(_id = id)
        temp.country_name =request.data['country_name']
        temp.save()
        return JsonResponse({'PUT': id})



