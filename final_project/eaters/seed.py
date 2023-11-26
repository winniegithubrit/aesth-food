# from django.core.management.base import BaseCommand
# from django.contrib.auth.hashers import make_password
# from django.utils.crypto import get_random_string
# from django.utils import timezone
# from yourapp.models import Owner, Restaurant, Menu, User, Order

# class Command(BaseCommand):
#     help = 'Seeding  the database with actual data'

#     def handle(self, *args, **options):
#         # Create owners
#         owner1 = Owner.objects.create(
#             name='Winnie',
#             email='winniejomo18@gmail.com',
#             password=make_password('nathalie'),
#             image='https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGVvcGxlfGVufDB8fDB8fHww',
#         )
#         owner2 = Owner.objects.create(
#             name='Wesley',
#             email='wesleykamau@gmail.com',
#             password=make_password('wess'),
#             image='https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fHBlb3BsZXxlbnwwfHwwfHx8MA%3D%3D',
#         )

#         # Create restaurants
#         restaurant1 = Restaurant.objects.create(
#             owner=owner1,
#             restaurant_name='Petes',
#             contact_number='1234567890',
#             opening_hours='08:00:00',
#             closing_hours='20:00:00',
#             image='https://images.unsplash.com/photo-1590846406792-0adc7f938f1d?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHJlc3RhdXJhbnR8ZW58MHx8MHx8fDA%3D',
#             payment_method='Mpesa',
#         )
#         restaurant2 = Restaurant.objects.create(
#             owner=owner2,
#             restaurant_name='Dominos',
#             contact_number='9876543210',
#             opening_hours='10:00:00',
#             closing_hours='22:00:00',
#             image='https://images.unsplash.com/photo-1615719413546-198b25453f85?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZG9taW5vcyUyMHBpenphfGVufDB8fDB8fHww',
#             payment_method='Mpesa',
#         )

#         # Create menus
#         menu1 = Menu.objects.create(
#             restaurant=restaurant1,
#             menu_name="Spaghetti Bolognese",
#             description="Classic Italian dish with meat sauce",
#             prices=12,
#             image="https://plus.unsplash.com/premium_photo-1664478291780-0c67f5fb15e6?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8c3BhZ2hldHRpJTIwYm9sb2duZXNlfGVufDB8fDB8fHww"
# ,
#         )
#         menu2 = Menu.objects.create(
#             restaurant=restaurant2,
#             menu_name='Chicken Alfredo',
#             description='Creamy pasta with grilled chicken',
#             prices=20,
#             image='https://images.unsplash.com/photo-1612152328178-4a6c83d96429?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2hpY2tlbiUyMHBhc3RhfGVufDB8fDB8fHww',
#         )

#         # Create users
#         user1 = User.objects.create(
#             user_name='Lexxie',
#             email='lexxie234@gmail.com',
#             password=make_password('rpass1'),
#             confirm_password=make_password('rpass1'),
#             type=False,
#             blocked='',
#             activity='Active',
#         )
    
#         # Create orders
#         order1 = Order.objects.create(
#             menu=menu1,
#             total_price=15,
#             order_date_and_time=timezone.now(),
#             address='123 Main St, Cityville',
#             payment_method='Mpesa',
#         )
      

#         self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
