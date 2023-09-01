from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from keyapp.forms import *
from openpyxl.drawing.image import Image
from openpyxl import load_workbook
import pandas
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "base.html")

def output(request):
    display = Employee.objects.all()
    return render(request, "output.html", {'display': display})

def apply(request):
    return render(request, 'form.html')

def exportdjango(request, employee_id):
    filename = "c:/Users/DELL/Desktop/django project/onetomany/keyapp/resources/template1.xlsx"
    wb = load_workbook(filename)
    response = HttpResponse(content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['content-Disposition'] = 'attachment; filename = "template1.xlsx" '

    filename2 = "c:/Users/DELL/Desktop/django project/onetomany/keyapp/resources/form config.xlsx"
    excel_data_df = pandas.read_excel(filename2, sheet_name='Sheet2', header=None)
    Dict = excel_data_df.to_dict(orient='records')
 
    
    sheet = wb.active
    details = Employee.objects.get(id = employee_id)
    works = Work.objects.get(reg_no_id = employee_id)
    Sal = salary.objects.get(reg_no_id = employee_id)
    sheet[Dict[0][0]] = getattr(details, Dict[0][1])        
    sheet[Dict[1][0]] = getattr(details,Dict[1][1])
    sheet[Dict[2][0]] = getattr(details,Dict[2][1])
    sheet[Dict[3][0]] = getattr(works, Dict[3][1])
    sheet[Dict[6][0]] = getattr(works, Dict[6][1])
    sheet[Dict[4][0]] = getattr(Sal,Dict[4][1])
    sheet[Dict[5][0]] = getattr(Sal, Dict[5][1])
    
    # sheet['C5'] = details.reg_no
    # sheet['C7'] = details.phone
    # sheet['C9'] = details.dob
    # sheet['C11'] = details.address
    # sheet['C14'] = details.email

    # img = Image(getattr(details, Dict[6][1]))
    # img.width = 120
    # img.height = 170
    # sheet.add_image(img, Dict[6][0]) 
    # Sign =Image(getattr(details, Dict[7][1]))
    # Sign.width = 190
    # Sign.height = 70
    # sheet.add_image(Sign, Dict[7][0])

    wb.save(response)
    return response


# def display(request, employee_id):
#     display = Employee.objects.get(id = employee_id)

#     return render(request, "showdetails.html", {'display':display})

# def saving(request):
#     vname = request.POST['name']
#     vreg_no = request.POST['reg_no']
#     vdept = request.POST['dept']
#     vexp = request.POST['exp']
#     vamount = request.POST['amount']
#     vdob = request.POST['dob']
#     vshift = request.POST['shift']
#     eg = Employee(name = vname, reg_no = vreg_no, dob = vdob)
#     eg = Work(reg_no_id = vreg_no, dept = vdept, experience = vexp)
#     eg = salary(reg_no_id = vreg_no, amount = vamount,  shift = vshift)
#     eg.save()
#     return render(request, 'base.html')

def saving(request):
    empform = EmployeeForm()
    workform = WorkForm() 
    salaryform = salaryForm()
    if request.method == 'POST':
        empform = EmployeeForm(request.POST)
        workform == WorkForm(request.POST)
        salaryform = salaryForm(request.POST)
        if empform.is_valid() and workform.is_valid() and salaryform.is_valid():
            empform = empform.save()
            workform.save(reg_no_id =empform.reg_no)
            salaryform.save(reg_no_id =empform.reg_no)
            return HttpResponse("Saved")
    return render(request, 'base.html', {'empform': empform, 'workform':workform, 'salaryform': salaryform}) 
