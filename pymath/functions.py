"""
Created by SaturnLang
"""
from math import *

def haversine(lon1: float, lat1: float, lon2: float, lat2: float) ->
float:
  #Convert decimal degrees radians
  lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
  
  #havsersine formula
  dlon = lon1 - lon2
  dlat = lat2 - lat1
  a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
  c = 2* asin(sqrt(a))
  r = 6371 # Radius of earth kilometers
  return c*r
def add(Add,ADD):
  return ADD+Add#add: ADD and Add
def subtract(Subtract,SUBTRACT):
  return Subtract-SUBTRACT #Subtract: Subtract and SUBTRACT
def multiply(Multiply, MUltiply):
  return Multiply * MUltiply#multiply: Multiply and multiply
def divide(Divide, DIvide):
  return Divide/DIvide#divide: Divide and DIvide
def pymath(MAth):
  print(MAth)
def Help():
  print("To Add: pymath(add(number,number)), To Subtract: pymath(subtract(number,number)), To Multiply: pymath(multiply(number,number)), To Divide: pymath(divide(number,number))")
     
