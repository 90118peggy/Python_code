
# Introduction

## SIR Model with Vaccination Simulation

This file primarily implements the **SIR model** in Python to simulate the spread of an infectious disease over time in a fixed population and explores the impact of vaccination on disease transmission. 

The SIR model categorizes the population into three groups: **Susceptible (S)**, **Infected (I)**, and **Recovered (R)**, and uses specific mathematical formulas to simulate how the numbers in these groups change over time. Additionally, it incorporates vaccination strategies and compares the impact of different vaccination policies, including the number of people vaccinated daily (`injected_n`) and the days required for the vaccine to take effect (`T`).

## UI surface


This script allows users to input their current 3D coordinates and find the nearest restaurant from a predefined list of restaurant locations in a 3D space. The program utilizes linear algebra functions for inner product and distance calculations and provides a graphical representation of the user's position and restaurants using `matplotlib`.

### Features
- **Inner Product Calculation**: Computes the inner product of two vectors.
- **Distance Calculation**: Computes the distance between two vectors using the formula based on inner products.
- **Interactive User Input**: Takes user input for coordinates using a simple GUI built with `tkinter`.
- **3D Visualization**: Displays the user and restaurant locations in a 3D scatter plot.
- **Nearest Restaurant Algorithm**: Determines the nearest restaurant based on the user’s position, excluding restaurants visited on previous days.

## PNG figure input Python

This Python script processes an image by dividing it into smaller sections, analyzing pixel color information to identify specific blue points, and visualizing data related to oscillatory behavior. The workflow consists of two main parts:

1. **Image Cutting and Saving**: 
   - The script first divides an image into 825 smaller parts, saves each segment as a separate image, and stores them in a directory.
   
2. **Blue Point Detection and Oscillation Graph Plotting**:
   - The script analyzes each small image to detect blue points using color range filtering in the HSV color space, collects the y-coordinates of these points, and then plots them to visualize the oscillation pattern.
   - Additionally, it calculates and prints the peaks during a stable oscillation phase between specific time intervals.
