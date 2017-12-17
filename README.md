
### Lambda function that calls AWS Comprehend

This is the code for an AWS lambda function.   The actual lambda function is in a file called "lambda_function.py".  You must also create an AWS API Gateway, which in turn calls the lambda function.


#### Testing


- Use native Postman (give you access to OPTIONS method)
- Takes two parameters (statement and lang)


Example of calling AWS API Gateway (I obfuscated the actual endpoint name): 

```
https://iaq73828402xw8.execute-api.us-east-1.amazonaws.com/prod/detectSentiment01?statement=Now is the time for all good men to come to the aid of their country&lang=en
```


