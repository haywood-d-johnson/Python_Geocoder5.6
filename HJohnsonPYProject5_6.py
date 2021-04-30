"""
@author: Haywood D. Johnson
@class: ITSE 2359 Advanced Computer Programming
@assignment: Project 5.6 Python – Geocoder
"""

import geocoder

print("Foward lookup using Komoot for Phoenix, Arizona")
g = geocoder.komoot("Phoenix, AZ")
print(g.latlng)
print(g.postal)
print(g.country)
print("\n")

print("Reverse lookup example using Arcgis for Lat 51.5074, Long 0.1278")
g = geocoder.arcgis([51.5074, 0.1278], method="reverse")
print(g.city)
print(g.state)
print(g.country)
print("\n")

print("IP address lookup using 8.8.8.8")
g = geocoder.ip("8.8.8.8")
print(g.ip)
print(g.postal)
print(g.latlng)
print(g.city + ", " + g.state)
print("\n")

print("IP address lookup using me")
g = geocoder.ip("me")
print(g.ip)
print(g.postal)
print(g.latlng)
print(g.city + ", " + g.state)
print("\n")

print("House address lookup using Komoot for 1600 Pennsylvania Avenue NW, Washington D.C.")
g = geocoder.komoot("1600 Pennsylvania Avenue NW, Washington D.C.")
print(g.housenumber)
print(g.postal)
print(g.street)
print(g.city)
print(g.state)
print(g.country)
print("\n")