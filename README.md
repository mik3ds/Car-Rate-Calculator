# Car Park Rate Generator
An API written in Python that inputs entry and exit times and outputs the appropriate rate.

Requires Python v3.6.5+

## Installation Steps
## Clone repo and navigate to project
```BASH
$ git clone https://github.com/mik3ds/Car-Rate-Calculator.git
$ cd Car-Rate-Calculator
```
### Create new Virtual Environment and activate it
```BASH
$ py -m venv env
```
### Install packages
```BASH
$ pip install -r requirements.txt
```
### Start server
```BASH
$ python main.py
```

If successful, the API will begin listening for POST data on http://0.0.0.0:5000/calculator
### Example Data
##### Input

```BASH
[
    {"entry","2019-12-06 06:30:00.000000"},
    {"exit","2019-12-06 18:30:00.000000"}
]
```
##### Output
```BASH
[
    {"Price","13"},
    {"Rate","Early Bird"}
]
```
### Testing
 - index.html is a simple HTML form that posts data to http://0.0.0.0:5000/calculator for manual testing
 - Running main_test.py will POST test data to the API and confirm that the response received is correct

### Notes

 - The project is written to be customizable. Prices can be edited in the rateGenerator class constructor and the API will still produce the lowest charge the car is valid for.