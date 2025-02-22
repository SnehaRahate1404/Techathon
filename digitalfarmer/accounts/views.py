from django.shortcuts import render, redirect
from .models import UserProfile, FarmerProfile
# from labor_panel.models import LabourProfile
# from krushi_kendr_panel.models import KrushiKendraProfile
# from gov_clerk_panel.models import GovernmentClerkProfile
from accounts.models import FarmerProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def user_login(request):
    if request.method == "POST":
        phone = request.POST.get('mobile')
        password = request.POST.get('pass')

        print(f"Phone: {phone}, Password: {password}")  # Debugging

        try:
            user = UserProfile.objects.get(phone=phone)

            # Debugging: Check if user is found
            print(f"User Found: {user}")

            # Check if password matches (assuming passwords are stored in plaintext)
            if user.password == password:  # ⚠️ Consider hashing passwords in the future
                request.session['user_id'] = user.id
                request.session['designation'] = user.identity
                request.session['phone'] = user.phone
                request.session['user_name'] = user.name  # Assuming your User model has 'name'
                request.session['user_location'] = user.location  
                designation = user.identity  # Assuming `identity` stores the designation

                print(f"Designation: {designation}")

                # Redirect based on the user's designation
                if designation == "Farmer":
                    return redirect('farmer_home')
                elif designation == "Labour":
                    return redirect('labor_panel:labor_home')
                elif designation == "Krushi Kendra":
                    return redirect('krushi_kendr_panel:krushi_home')
                elif designation == "gov_clerk":
                    return redirect('gov_clerk_panel:gov_clerk_home')
                elif designation == "Market_clerk":
                    return redirect('market_panel:market_home')

            else:
                messages.error(request, "Invalid credentials")
                return redirect("accounts:user_login")

        except UserProfile.DoesNotExist:
            messages.error(request, "User not found!")
            return redirect("accounts:user_login")

    return render(request, "login.html")

def user_logout(request):
    request.session.flush()  # Clears all session data
    return redirect('accounts:user_login')  # Redirect to login page



def user_registration(request):
    if request.method == "POST":
        from market_panel.models import MarketClerkProfile
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        identity = request.POST.get('identity')  # Get user role
        location = request.POST.get('location')
        password = request.POST.get('pass')

        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('accounts:user_registration')

        # Create user profile
        user = UserProfile.objects.create(
            name=name,
            phone=phone,
            email=email,
            identity=identity,
            location=location,
            password=password  # ⚠️ Consider hashing the password before saving
        )

        # If the user is a labourer, create a LabourProfile
        if identity == "Labour":
            LabourProfile.objects.create(
                user=user,
                wage_per_day=0,  # Default wage, can be updated later
                skills="Not specified",
                experience=0,
                location=location
            )

        if identity == "Krushi Kendra":
            KrushiKendraProfile.objects.create( 
                user=user,
                shop_name="Default Shop Name",  # Owners can update later
                owner_name=name,
                contact_number=phone,
                location=location,
                services_offered="Not specified"
            )
        if identity == "Farmer":
            FarmerProfile.objects.create( 
            user=user,
            land_size=0,  
            crop_type="Not specified",
            experience_years=0
            )
        elif identity == "gov_clerk":
            GovernmentClerkProfile.objects.create(
                user=user,
                department="Not specified",
                office_location=location
            )
        elif identity == "Market_clerk":
            MarketClerkProfile.objects.create(
                user=user,
                market_name="Not specified",
                region=location
            )


        messages.success(request, "Registration Successful!")
        return redirect('accounts:user_login')  # Redirect to login after registration

    return render(request, "registration.html")


