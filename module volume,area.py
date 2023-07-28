from math import pi
def arearectangle(l,b):
    area=(l*b)
    print (area)
def areasquare(a):
    area=(a*a)
    print(area)
def areacircle(r):
    area1=(pi*r*r)
    area=round(area1)
    print(area)
def areatriangle(a,b):
    area=(0.5*a*b)
    print(area)
def areatrapezoid(a,b,c):
    area=(0.5*(a+b)*c)
    print(area)
def areaellipse(a,b):
    area1=(pi*a*b)
    area=round(area1)
    print(area)
########volume startsss
#
#
#
#
def volcuboid(a,b,c):
    volume=(a*b*c)
    print(volume)
def volcube(a):
    volume=a**3
    print(volume)
def volcylinder(r,h):
    volume=(pi*(r**2)*h)
    print(volume)
def volsphere(r):
    volume=((4/3)*pi*(r**3))
    print(volume)
def volrtcircularcone(r,h):
    vol=((1/3)*pi*(r**2)*h)
    print(vol)