from django import template
from django.utils import numberformat
register = template.Library()



def spaced_format(value):
    deleni = value / 1000
    zbytek = value % 1000
    str_value = str(value)
    str_deleni = str(deleni)
    str_zbytek_ = str(zbytek)
    str_zbytek = (str_zbytek_[:-1])
    if zbytek == 0:
        
        if value > 10000:
            res = str_deleni.replace("."," ") + "00"
            return res
        if value < 10000:
            res = str_deleni.replace("."," ") + "00"
            return res
    else:
        if value > 9999:
            vysledek = None
            podeleni = str_deleni.replace(".", " ")
            if len(str_value) == 7 and str_value[-3]== "0" and str_value[-4] != "0":
                vysledek=f"{podeleni}0"

            if len(str_value) == 7 and str_value[-3]!= "0" and str_value[-4] != "0":
                vysledek=f"{podeleni}"

            if len(str_value) == 7 and str_value[-3]== "0" and str_value[-4] =="0":
                vysledek=f"{podeleni}00"

            if len(str_value) == 7 and str_value[-3]== "0" and str_value[-4] =="0"and str_value[-5] =="0":
                vysledek=f"{podeleni}000"

            if len(str_value) == 7 and str_value[-3]== "0" and str_value[-4] =="0"and str_value[-5] !="0":
                vysledek=f"{podeleni}00"

            if len(str_value) == 8 and str_value[-3]== "0" and str_value[-4] != "0":
                vysledek=f"{podeleni}0"

            if len(str_value) == 8 and str_value[-3]!= "0" and str_value[-4] != "0":
                vysledek=f"{podeleni}"

            if len(str_value) == 8 and str_value[-3]== "0" and str_value[-4] =="0":
                vysledek=f"{podeleni}00"

            if len(str_value) == 8 and str_value[-3]== "0" and str_value[-4] =="0"and str_value[-5] =="0":
                vysledek=f"{podeleni}000"

            if len(str_value) == 8 and str_value[-3]== "0" and str_value[-4] =="0"and str_value[-5] !="0":
                vysledek=f"{podeleni}00"


            
            if len(str_value) == 9 and str_value[-3]== "0" and str_value[-4] != "0":
                vysledek=f"{podeleni}0"

            if len(str_value) == 9 and str_value[-3]!= "0" and str_value[-4] != "0":
                vysledek=f"{podeleni}"

            if len(str_value) == 9 and str_value[-3]== "0" and str_value[-4] =="0":
                vysledek=f"{podeleni}00"

            if len(str_value) == 9 and str_value[-3]== "0" and str_value[-4] =="0"and str_value[-5] =="0":
                vysledek=f"{podeleni}000"

            if len(str_value) == 9 and str_value[-3]== "0" and str_value[-4] =="0"and str_value[-5] !="0":
                vysledek=f"{podeleni}00"


            
            return vysledek
        if value < 10000:
            vysledek = None
            podeleni = str_deleni.replace(".", " ")

            if len(str_value) == 6 and str_value[-3]== "0" and str_value[-4] != "0":
                vysledek=f"{podeleni}0"

            if len(str_value) == 6 and str_value[-3]!= "0" and str_value[-4] != "0":
                vysledek=f"{podeleni}"

            if len(str_value) == 6 and str_value[-3]== "0" and str_value[-4] =="0":
                vysledek=f"{podeleni}00"

            if len(str_value) == 6 and str_value[-3]== "0" and str_value[-4] =="0"and str_value[-5] =="0":
                vysledek=f"{podeleni}000"

                

            return vysledek

register.filter("spaced_format",spaced_format)

def spaced_format_total(value):
    deleni = value / 1000
    str_value = str(deleni)
    str_value_after = str_value.replace('.',' ')
    return f"{str_value_after}00"
register.filter("spaced_format_total",spaced_format_total)