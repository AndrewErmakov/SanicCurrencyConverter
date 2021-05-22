<h1 align="center"> 
  SanicCurrencyConverter
</h1>

## What is it?
API for receiving and converting currency rates. 

## How to start ?
First, we need to upload the project to our local machine. To do this, in the command console, enter: 
```sh
git clone https://github.com/AndrewErmakov/SanicCurrencyConverter.git
```

To run a project in Docker, you need to create an image, enter in cmd:

```sh
docker build -t sanic-currency-converter .
```

Based on this image, you need to run the container, enter in cmd:

```sh
docker run --rm --name converter -p 5000:5000 sanic-currency-converter
```

**We started the server, great!**


# Getting the currency rate against the ruble

To determine currency rate is used get-request type:

<code>
GET /api/course/<currency>
</code>

 
  **where <code>currency</code> - currency code in the format ISO 4217**
  
  
The result is data in the json format with two entries with keys

```json
{
   "currency": <string>,
    "rub_course": <float>
}
```
  
**Examples**

  
1. In order to get the dollar rate against the ruble, you need to go to 
<code>
GET /api/course/USD
</code>

The result of the request will be json data 
 
```json
{
   "currency": USD,
    "rub_course": 71.662
}
```
The HTTP status code will be 200 in this case.

  
2. If the get request is for a currency (invalid) that does not match the code in the format ISO 4217, then result of the request will be:
  ```json
{
   "success": False,
}
```
  
  The HTTP status code will be 421 in this case.

  
# Transfer of a certain amount of one currency to another 

To transfer a certain amount of one currency to another, a post-request get-request type:
<code>
POST /api/convert
</code>
  
Json data arrives on the server.
  ```json
{
   "from_currency": <string>,
    "to_currency": <string>,
    "amount": <float>
}
```
*Value of amount must be above zero*.
  
**Examples**
1. Let the json data come to the server *(valid data)*:

```json
{
   "from_currency": "USD",
    "to_currency": "RUB",
    "amount": 134.65
}
  ```
  The answer to this request is json data:
  ```json
{
   "currency": "RUB",
    "amount": 9643.59
}
  ```
The HTTP status code will be 200 in this case.

2. Let the json data come to the server *(invalid data - one of the currencies does not match the code in the format ISO 4217)*:

  ```json
{
   "from_currency": "USB",
    "to_currency": "RUB",
    "amount": 134.65
}
```
   
The answer to this request is:
   
```json
{
   "success": False,
}
```
  
The HTTP status code will be 421 in this case.
  
3. Let the json data come to the server *(invalid data - value of amount less than zero)*:

  ```json
{
   "from_currency": "USD",
    "to_currency": "RUB",
    "amount": -134.65
}
```

The answer to this request is:
   
```json
{
   "success": False,
}
```

The HTTP status code will be 421 in this case.
