"""
URL configuration for Pharmacy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index),
    path('login/',views.login),
    path('user_register/',views.user_register),
    path('doctor_register/',views.doctor_register),
    path('pharmacist_register/',views.pharmacist_register),
    # path('dl',views.dlt),
    # path('ad',views.admin),


    #-------ADmin----------#
    path('admin_view_doctors/',views.admin_view_doctors),
    path('adminHome/',views.adminHome),
    path('approve_doctor/',views.approve_doctor),
    path('reject_doctor/',views.reject_doctor),
    path('admin_view_phar/',views.admin_view_phar),
    path('accept_pharma/',views.accept_pharma),
    path('reject_pharma/',views.reject_pharma),
    path('profit_report/',views.profit_report),
    path('SoldMedicine/',views.SoldMedicine),
    path('adm_viewMedicine/',views.adm_viewMedicine),
    path('adm_viewdetails/',views.adm_viewdetails),
    path('expiredStock/',views.expiredStock),



    #--------Pharmacist--------#
   path('pharmacist_Profile/',views.pharmacist_Profile), 
   path('pharmaHome/',views.pharmaHome), 
   path('update_pharmacist_Profile/',views.update_pharmacist_Profile), 
   path('addmedicine/',views.addmedicine), 
   path('view_medicineDetails/',views.view_medicineDetails), 
   path('Update_Medicine/',views.Update_Medicine), 
   path('view_medicine/',views.view_medicine), 
   path('ph_view_prescription/',views.ph_view_prescription), 
   path('sales_Medicine/',views.sales_Medicine), 
   path('delete_med/',views.delete_med), 
   path('pharmacist_view_orders/',views.pharmacist_view_orders), 
   path("paid_orders_view/",views.paid_orders_view, name="paid_orders"),
    # path("generate-invoice/<int:order_id>/",views.generate_invoice, name="generate_invoice"),
    # path("invoice/<int:invoice_id>/",views.invoice_detail, name="invoice_detail"),
        # path("invoice_details/", views.invoice_details, name="invoice_details"),

    path("invoice_details/",views.invoice_details),


    # path('profit_report/', views.profit_report, name='profit_report'),

    path('pharmacist_view_profit/',views.pharmacist_view_profit, name='pharmacist_view_profit'),


   #----------Doctor---------#
   path('doctorHome/',views.doctorHome), 
   path('DoctorProfile/',views.DoctorProfile), 
   path('update_DoctorProfile/',views.update_DoctorProfile), 
   path('doc_view_bookings/',views.doc_view_bookings), 
   path('accept_bookings/',views.accept_bookings), 
   path('decline_booking/',views.decline_booking), 
   path('accepted_appointments/',views.accepted_appointments), 
   path('accepted_appointments/',views.accepted_appointments), 
   path('prescription_patient/',views.prescription_patient), 
   path('dr_viewMedicine/',views.dr_viewMedicine,name='dr_viewMedicine'), 
   path('dr_viewMedicinedetails/',views.dr_viewMedicinedetails), 



   #---------USER-------------#
   path('userHome/',views.userHome),
   path('book_appoinment/',views.book_appoinment),
   path('view_bookedappointment/',views.view_bookedappointment),
   path('view_prescription/',views.view_prescription),
   path('ph_givenMedicine/',views.ph_givenMedicine),
   path('user_payment_page/',views.user_payment_page),
   path('user_viewMedicine/',views.user_viewMedicine),
   path('user_viewMedicineDetails/',views.user_viewMedicineDetails),
   path('add_to_cart/',views.add_to_cart),
   path('medicine_payment/',views.medicine_payment),
   path('place_order/',views.place_order),
   path('confirmorder/',views.confirmorder),
   path('chat/',views.chat),
   path('UserProfile/',views.UserProfile),
   path('update_userProfile/',views.update_userProfile),
   path('invoice/',views.invoice),





]
