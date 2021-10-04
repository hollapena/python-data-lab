cupcake_invoices=open("CupcakeInvoices.csv")

# def all_invoices(cupcake_invoices):
#     for invoices in cupcake_invoices:
#         print(invoices)

# all_invoices(cupcake_invoices)

# def find_type(cupcake_invoices):
#     for invoices in cupcake_invoices:
#         split_invoices = invoices.split(',')
#         print(split_invoices[2])

# find_type(cupcake_invoices)
   
# def find_customer_total(cupcake_invoices):
#     for invoices in cupcake_invoices:
#          split_invoices = invoices.split(',')
#          new_num1=float(split_invoices[3])
#          new_num2=float(split_invoices[4])
#          total=new_num1*new_num2
#          print(total)

# find_customer_total(cupcake_invoices)

def find_overall_total(cupcake_invoices):
    new_total=0
    for invoices in cupcake_invoices:
        split_invoices=invoices.split(',')
        new_num1=float(split_invoices[3])
        new_num2=float(split_invoices[4])
        customer_total=new_num1*new_num2
        new_total += customer_total
    print(new_total)

find_overall_total(cupcake_invoices)







