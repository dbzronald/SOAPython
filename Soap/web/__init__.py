#!/usr/bin/env python
import sys

from suds.client import Client

url = "http://localhost:7777/ws/AcademicoWebService?wsdl"
client = Client(url)

print "---------------------------------------------------"
print "               Lista de Estudiantes"
print "---------------------------------------------------"
#Estudiante.
estudiante=client.service.getAllEstudiante()
print estudiante

print "---------------------------------------------------"
print "               Profesor Consultado"
print "---------------------------------------------------"
#Profesor
profe=client.service.getProfesor('031-0001-01').nombre
print profe

print "\n---------------------------------------------------"
print "               Asignatura Consultada"
print "---------------------------------------------------"

#Asignatura
asig=client.service.getAsignatura('ISC-415').nombre
print asig
print "\n---------------------------------------------------"
