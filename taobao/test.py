from taobao import db
from taobao.models import *

def customer_add(num):
    for i in range(num):
        string="customer_"+str(i)
        cus= Customer(username=string, email=string+"@qq.com", password="123456")
        db.session.add(cus)
    db.session.commit()

def crew_add(num):
    for i in range(num):
        string="crew_"+str(i)
        cus= Crew(username=string, email=string+"@qq.com", password="123456")
        db.session.add(cus)
    db.session.commit()
        

def supplier_add(num):
    for i in range(num):
        string="supplier_"+str(i)
        cus= Supplier(username=string, email=string+"@qq.com", password="123456")
        db.session.add(cus)
    db.session.commit()

def product_add(num):
    for i in range(num):
        string = "product_" + str(i)
        cus = Product(name=string, sort=string, price=500)
        db.session.add(cus)
    db.session.commit()

def supply_add(num):
    for i in range(num):
        cus = Supply(supplier_id=i,product_id=i)
        db.session.add(cus)
    db.session.commit()


count=5
num = input("input 1 to recreate_all()")
if num == "1":
    db.drop_all()
    db.create_all()
    #1
    # input("-------------enter---------")
    #customer_add(count)
    #supplier_add(count)
    #crew_add(count)
    #product_add(count)
    #supply_add(count)


    


