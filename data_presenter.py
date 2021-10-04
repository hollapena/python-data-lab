cupcake_invoices=open("CupcakeInvoices.csv")

def all_invoices(cupcake_invoices):
    for invoices in cupcake_invoices:
        print(invoices)

all_invoices(cupcake_invoices)

cupcake_invoices.seek(0,0)

def find_type(cupcake_invoices):
    for invoices in cupcake_invoices:
        split_invoices = invoices.split(',')
        print(split_invoices[2])

find_type(cupcake_invoices)

cupcake_invoices.seek(0,0)
   
def find_customer_total(cupcake_invoices):
    for invoices in cupcake_invoices:
         split_invoices = invoices.split(',')
         new_num1=float(split_invoices[3])
         new_num2=float(split_invoices[4])
         total=new_num1*new_num2
         print(total)

find_customer_total(cupcake_invoices)

cupcake_invoices.seek(0,0)

def find_overall_total(cupcake_invoices):
    new_total=0
    for invoices in cupcake_invoices:
        split_invoices=invoices.split(',')
        new_num1=float(split_invoices[3])
        new_num2=float(split_invoices[4])
        customer_total=new_num1*new_num2
        new_total += customer_total
    rounded_total = round(new_total, 2)
    print(rounded_total)

find_overall_total(cupcake_invoices)

cupcake_invoices.seek(0,0)

def find_income_by_flavor(cupcake_invoices):
    chocolate=0
    vanilla=0
    strawberry=0
    for invoices in cupcake_invoices:
        split_invoices=invoices.split(',')
        if split_invoices[2]=="Chocolate":
            new_num1=float(split_invoices[3])
            new_num2=float(split_invoices[4])
            new_total=new_num1*new_num2
            chocolate += new_total
        if split_invoices[2]=="Vanilla":
            new_num1=float(split_invoices[3])
            new_num2=float(split_invoices[4])
            new_total=new_num1*new_num2
            vanilla += new_total
        if split_invoices[2]=="Strawberry":
            new_num1=float(split_invoices[3])
            new_num2=float(split_invoices[4])
            new_total=new_num1*new_num2
            strawberry += new_total
    new_chocolate=round(chocolate, 2)
    new_vanilla=round(vanilla, 2)
    new_strawberry=round(strawberry, 2)
    return (new_chocolate, new_vanilla, new_strawberry)

flavors=find_income_by_flavor(cupcake_invoices)
chocolate=str(flavors[0])
vanilla=str(flavors[1])
strawberry=str(flavors[2])

import matplotlib.pyplot as plt

flavor=['Strawberry', 'Vanilla', 'Chocolate']
income=[strawberry, vanilla, chocolate]

plt.bar(flavor, income)
plt.title('Company Income by Flavor')
plt.xlabel('Flavor')
plt.ylabel('Income')
plt.show()

cupcake_invoices.close()
