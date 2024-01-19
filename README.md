# PythonProjectAlgebra

# Project Title

PyFloraPots

# Summary

The work consists of creating a GUI application for monitoring the state of ornamental and/or herb plants planted in containers with integrated sensors for measuring:
- temperature
- soil moisture
- pH value and salinity of the soil
- the level of light reaching the plant.
Vessels from the sensor send measurements to the application via an integrated Bluetooth connection or the values ​​are read from all sensors by simulation by generating them in a separate Python script that will be run every time the user presses the "Sync" button.

## How is it used?

To use the application, the user must log in to the application. The application is not available to anonymous users. After a successful login, the user can view the status of all PyPots with associated plants.
The user can add new PyPots to the application, associate PyPots with plants from the integrated plant database. All application objects should have the possibility of CRUD operations (Create, Read, Update, Delete).
During the first launch, the application has information about the user (first name, last name, username and password), an initial plant database and one PyPot (flower pot with integrated sensors).

## Acknowledgments

The application was made as a final paper while attending the program for Python Developer in Algebra
