# ElevatorProject - OOP

## Problem Statement

Create an algorithm for an OOP exercice based on the concept of "Smart Elevator". We need to implement an elevator controle system using an ***Offline Algorithm***.
In this algorithm, we get all the input before running the program what allow us to
The algorithm receives all the inputs in advance before running the program, which makes it possible to plan the most efficient and fast path without any changements on the running time.

## Sources

- Explanation of the *Destination Dispach* algorithm method on the [Elevatorpedia](https://elevation.fandom.com/wiki/Destination_dispatch) website which is an optimization technique used to install multi-lifts that group passengers to the same destinations to the same lifts and thus reduces waiting times and passengers compared to a standard system where all passengers want to get on or off. And actually eliminates unnecessary stops.

- A study on *"Smart Elevator"* on the [ResearchGate](https://www.researchgate.net/publication/331475872_Smart_Building's_Elevator_with_Intelligent_Control_Algorithm_based_on_Bayesian_Networks) website called *Smart Building’s Elevator with Intelligent Control Algorithm based on Bayesian Networks* which tells about the application of smart elevator control systems based on the *maching learning* algorithm which aims to improve the comfort of multi-site buildings. The algorithm maintains information about the size of the passenger group and their waiting time provided by the purchasing and appointment processing system. The information is then used as the decision-making model and calculation of the elevator path

- A simulation project that simulates a smart [Elevator System Netifly](https://elevator-system.netlify.app/) elevator. The simulator consists of 13 floors and 4 elevators, the quantities can be changed as we wish. Next to each floor is indicated the amount of available elevators calculated according to the algorithm of the simulator. The system knows how to allocate the available elevator closest to the reading floor at any given moment, as well as the *Online* algorithm computes a new path for each new call.
