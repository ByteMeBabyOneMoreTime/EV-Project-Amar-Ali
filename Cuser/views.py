from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db import IntegrityError
from .models import Role, Customer
from Services.models import Service, Payment, Perks

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url="login") 
def register_customer(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        name = request.POST.get("name", "").strip()
        
        # Basic validation
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("register_customer")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect("register_customer")

        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("register_customer")

        try:
            # Create user and role
            customer_user = User.objects.create_user(username=username, email=email, password=password)
            customer_user.first_name = name
            customer_user.save()
            Role.objects.create(user=customer_user, role="Customer")

            messages.success(request, "Customer registered successfully.")
            return redirect("add_customer_details", user_id=customer_user.id)

        except IntegrityError:
            messages.error(request, "An error occurred while creating the user. Please try again.")
        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")

    template = "dashboard/register_customer.html"
    return render(request, template)


@login_required(login_url="login") 
def add_customer_details(request, user_id):
    customer_user = get_object_or_404(User, id=user_id)

    # Ensure the user has the 'Customer' role
    if not Role.objects.filter(user=customer_user, role="Customer").exists():
        messages.error(request, "User must have the role of Customer.")
        return redirect("register_customer")  # Redirect to an appropriate page

    if request.method == "POST":
        gender = request.POST.get("gender", "").strip()
        father_name = request.POST.get("father_name", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        aadhar_number = request.POST.get("aadhar_number", "").strip()
        address = request.POST.get("address", "").strip()

        # Validate required fields
        if not all([gender, father_name, phone_number, aadhar_number, address]):
            messages.error(request, "All fields are required.")
            return render(request, "dashboard/customer_details.html", {"customer_user": customer_user})

        # Validate phone number
        if not phone_number.isdigit() or len(phone_number) != 10:
            messages.error(request, "Invalid phone number. It must be 10 digits.")
            return render(request, "dashboard/customer_details.html", {"customer_user": customer_user})

        # Validate Aadhar number
        if not aadhar_number.isdigit() or len(aadhar_number) != 12:
            messages.error(request, "Invalid Aadhar number. It must be 12 digits.")
            return render(request, "dashboard/customer_details.html", {"customer_user": customer_user})

        # Ensure phone number is unique
        if Customer.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "This phone number is already registered.")
            return render(request, "dashboard/customer_details.html", {"customer_user": customer_user})

        # Ensure Aadhar number is unique
        if Customer.objects.filter(aadhar_number=aadhar_number).exists():
            messages.error(request, "This Aadhar number is already registered.")
            return render(request, "dashboard/customer_details.html", {"customer_user": customer_user})

        try:
            # Create the customer entry
            Customer.objects.create(
                user=customer_user,
                gender=gender,
                father_name=father_name,
                phone_number=phone_number,
                aadhar_number=aadhar_number,
                address=address,
                created_by=request.user
            )
            messages.success(request, "Customer details added successfully.")
            return redirect("select_service", user_id=customer_user.id)

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    template = "dashboard/customer_details.html"
    return render(request, template, {"customer_user": customer_user})


@login_required(login_url="login") 
def select_service(request, user_id):
    customer_user = get_object_or_404(User, id=user_id)
    services = Service.objects.all()

    if request.method == "POST":
        service_id = request.POST.get("service", "").strip()
        method = request.POST.get("payment_method", "").strip()  # Fix: Use correct key
        payment_id = request.POST.get("online_payment_id", "").strip()  # Fix: Use correct key

        if not service_id:
            messages.error(request, "Please select a service.")
            return render(request, "dashboard/select_service.html", {"customer_user": customer_user, "services": services})

        if method == "Online" and not payment_id:
            messages.error(request, "Payment ID is required for online payments.")
            return render(request, "dashboard/select_service.html", {"customer_user": customer_user, "services": services})

        # Ensure the payment ID is unique if the method is online
        if method == "Online" and Payment.objects.filter(online_payment_id=payment_id).exists():
            messages.error(request, "This payment ID has already been used.")
            return render(request, "dashboard/select_service.html", {"customer_user": customer_user, "services": services})

        try:
            selected_service = get_object_or_404(Service, id=service_id)

            Payment.objects.create(
                user=customer_user,
                service=selected_service,
                method=method,  # Fix: Now correctly fetching the method
                online_payment_id=payment_id if method == "Online" else None  # Only store if online
            )

            messages.success(request, "Payment successful. Redirecting...")
            return redirect("payment_success", user_id=user_id)

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    return render(request, "dashboard/select_service.html", {"customer_user": customer_user, "services": services})


@login_required(login_url="login") 
def payment_success(request, user_id):
    try:
        customer_user = get_object_or_404(User, id=user_id)
        messages.success(request, "Payment was successful! Thank you for your purchase.")
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect("select_service", user_id=user_id)

    template = "dashboard/payment_success.html"
    return render(request, template, {"customer_user": customer_user})


def clogin(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_superuser or Role.objects.get(user=request.user).role == "Employee":
                return redirect('/admin')
            else:
                return redirect('profile')
            
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if Role.objects.get(user=user).role == "Employee":
                return redirect('/admin')
            elif user.is_superuser:
                return redirect('/admin')
            else:
                return redirect("profile")
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'pages/login.html')

@login_required(login_url="login")   
def clogout(request):
    logout(request)
    return redirect('homepage')

@login_required(login_url="login")
def customer_page(request):
    user = request.user

    try:
        user_customer_details = Customer.objects.get(user=user)
    except ObjectDoesNotExist:
        user_customer_details = None

    user_payement_details = Payment.objects.filter(user=user)
    last_payement = user_payement_details.first()
    package = last_payement.service.name
    perks = Perks.objects.filter(service=last_payement.service)
    

    if last_payement:
        package_days_left = last_payement.days_until_default()
        need_for_recharge = last_payement.is_defaulter()
    else:
        package_days_left = 0
        need_for_recharge = True

    username = f"{user.first_name} {user.last_name}"
    lastlogin = user.last_login
    created = user.date_joined

    if user_customer_details:
        userid = user_customer_details.generated_id
        user_gender = user_customer_details.gender
        user_fathers_name = user_customer_details.father_name
        user_phonenumber = user_customer_details.phone_number
        user_aadharnumber = user_customer_details.aadhar_number
        user_address = user_customer_details.address
        agent_name = user_customer_details.created_by.username
    else:
        userid = None
        user_gender = None
        user_fathers_name = None
        user_phonenumber = None
        user_aadharnumber = None
        user_address = None
        agent_name = None

    context = {
        'username': username,
        'lastlogin': lastlogin,
        'created': created,
        'userid': userid,
        'user_gender': user_gender,
        'user_fathers_name': user_fathers_name,
        'user_phonenumber': user_phonenumber,
        'user_aadharnumber': user_aadharnumber,
        'user_address': user_address,
        'agent_name': agent_name,
        'packagedaysleft': package_days_left,
        'needforrecharge': need_for_recharge,
        'allpayments': user_payement_details,
        'package' : package,
        'perks' : perks
        
    }

    return render(request, 'pages/profile.html', context)