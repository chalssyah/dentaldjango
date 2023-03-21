from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']
		
		# send an email
		appointment = "Name: " + your_name + " \nPhone☎: " + your_phone + " \nEmail📩: " + your_email + " \nAddress🎪: " + your_address + " \nSchedule: " + your_schedule + " \nDay: " + your_date + " \nMessage: " + your_message

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			['munkarsamanakir@gmail.com'], # To Email
			)
		
		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message
			})

	else:
		return render(request, 'appointment.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['munkarsamanakir@gmail.com'], # To Email
			)

		return render(request, 'contact.html', {'message_name': message_name})


	else:
		# return the page
		return render(request, 'contact.html', {})
	
