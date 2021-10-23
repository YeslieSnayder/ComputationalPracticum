# Description

This is the task for Computational Practicum.

The program allows user to see the graph of the solution of the equation $y=C_2e^{x^2}-x^2-1$ with opportunity to change initial conditions, range and number of grid steps.

For calculating new exact solution the program use the following formula to calculate the constant $C_2$: $C_2=(y+x^2+1)e^{-x^2}$

The user can change parameters of the equation and visibility of the corresponding solutions.
After changing any value, user should push the button `Update`.

Also, user can change any of the parameters without filling all of them.
If you want to change only 1 parameter, just fill only this form and push `Update` button.
The application will update only this parameter and display the new graph.

## Page 1

On the first page user can see the graph on which the following solutions are presented:

- Exact solution;
- Approximate solution using Euler's method;
- Approximate solution using Improved Euler's method;
- Approximate solution using Runge Kutta method.

Parameters:
- `x0` - starting point for x;
- `y0` - solution for starting point;
- `X` - endpoint for x;
- `steps` - the number of steps between `x0` and `X`.

## Page 2

There are local truncation errors (LTE) of each method.

## Page 3

There are changing LTE of each approximation method depending on the given step.

It calculates the maximum local error on the range $[x0, X]$ for each number of steps on the range $[n0, N]$ with step 1.

- `n0` - starting number of steps
- `N` - end number of steps

## Tests

The program has tests of functionality.

They are located in the **tests** directory.

## Libraries

Required **Python** version: `3.8` or above.

# Installation

1. Clone repo: `git clone https://github.com/YeslieSnayder/ComputationalPracticum.git`
2. Open the directory: `cd ComputationalPracticum/`
3. Install requirements: `pip install -r requirements.txt`
4. Open the directory of application: `cd app/`
5. Launch the application on the current directory: `python3 .`