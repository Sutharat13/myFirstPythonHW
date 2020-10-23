from zeep import Client
from lxml import rtree
client = Client('http://www.pttor.com/oilPrice.asmx?WSDL')
resoult = client.service.CurrentOilPrice(Language="en")
root = etree.formstring(result)
n = len(root)
name = ['none']
price = [0]

def menu1():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 28 + "Welcome to the program" + " " * 28 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)


def menu2():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 37 + "Menu" + " " * 37 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 24 + "1.Gasoline 95   ราคา 29.16 BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "2.Gasoline 91   ราคา 25.30 BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "3.Gassohol 91   ราคา 21.68 BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "4.Gassohol E20  ราคา 20.2  BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "5.Gassohol 95   ราคา 21.0  BATH" + " " * 23 + "#")
    print("#" + " " * 24 + "6.Diesel        ราคา 21.1  BATH" + " " * 23 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)


def menu3():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 33 + "ชนิดการคำนวน" + " " * 34 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 33 + "1.ลิตรเป็นเงิน" + " " * 34 + "#")
    print("#" + " " * 33 + "2.เงินเป็นลิตร" + " " * 34 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)


def menu4():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 31 + "กรุณาใส่ค่าการคำนวน" + " " * 31 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)


def menu5():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 30 + "ออกจากโปรแกรมหรือไม่" + " " * 30 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 31 + "1. ออกจากโปรแกรม" + " " * 31 + "#")
    print("#" + " " * 31 + "2. เริ่มรันใหม่อีกครั้ง" + " " * 31 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)


while True:

    menu1()
    a = input(">>>>กดปุ่มใดๆเพื่อทำรายการ<<<<")

    a = 0
    while not(a in [1, 2, 3, 4, 5, 6]):
        menu2()
        b = input("เลือกเชื้อเพลิง :")
        if b.isnumeric():
            a = int(b)

        else:
            a = 0

    c = 0
    while not(c in [1, 2]):
        menu3()
        d = input("เลือกชนิดการคำนวนข้อมูล :")

        if d.isnumeric():
            c = int(d)
        else:
            c = 0

    e = 0
    while not(e):
        menu4()
        f = input("กรุณาใส่ค่าการคำนวน :")

        if f.isnumeric():
            e = float(f)
        else:
            e = 0
        f = float(f)
        if d == '1':
            if b == '1':
                e = f * 29.16
                print("จำนวนเงินที่ได้ = {}".format(e), "บาท")
            elif b == '2':
                e = f * 25.30
                print("จำนวนเงินที่ได้ = {}".format(e), "บาท")
            elif b == '3':
                e = f * 21.68
                print("จำนวนเงินที่ได้ = {}".format(e), "บาท")
            elif b == '4':
                e = f * 20.2
                print("จำนวนเงินที่ได้ = {}".format(e), "บาท")
            elif b == '5':
                e = f * 21.0
                print("จำนวนเงินที่ได้ = {}".format(e), "บาท")
            else:
                e = f * 21.1
                print("จำนวนเงินที่ได้ = {}".format(e), "บาท")

        if d == '2':
            if b == '1':
                e = f / 29.16
                print("จำนวนลิตรที่ได้ = {}".format(e), "ลิตร")
            elif b == '2':
                e = f / 25.30
                print("จำนวนลิตรที่ได้ = {}".format(e), "ลิตร")
            elif b == '3':
                e = f / 21.68
                print("จำนวนลิตรที่ได้ = {}".format(e), "ลิตร")
            elif b == '4':
                e = f / 20.2
                print("จำนวนลิตรที่ได้ = {}".format(e), "ลิตร")
            elif b == '5':
                e = f / 21.0
                print("จำนวนลิตรที่ได้ = {}".format(e), "ลิตร")
            else:
                e = f / 21.1
                print("จำนวนลิตรที่ได้ = {}".format(e), "ลิตร")
    g = input(">>>>>>>กดปุ่มใดๆเพื่อทำรายการต่อ<<<<<<<")

    a = 0
    while not(a in [1, 2]):
        menu5()
        b = input("เลือกออกจากโปรแกรม :")
        if b.isnumeric():
            a = int(b)
        else:
            a = 0
    if a == 1:
        break