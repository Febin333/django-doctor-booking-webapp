from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'
class Bookingform(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'booking_date':DateInput,
        }
        labels={
           'p_name':"Patient name:",
           'p_number':"Patient number:",
           'p_email':"Patient email:",
           'name':"Doctor name:",
           'booking_date':"Booking date:",
        }