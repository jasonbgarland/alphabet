# Alphabet

Route that can be used to verify if every letter of the alphabet is included in the provided string.

Note: The check is case-insensitive. Numbers, special characters, and whitespace are ignored.

## URL

The route is located at the following url after the base url:

```
/alphabet
```

## Parameters

Alphabet has the following URL parameters:

### string

Description: The string to check  
Type: string  

Example:
```
/alphabet?string=abcdefg
```

## Responses

The alphabet endpoint returns the following responses:

### 200

The response was valid. The return value is a plaintext string.

The output will be true if the provided string has at least one of every character in the alphabet.
```
true
```
The output will be false if the provided string does NOT contain at least one of every character in the alphabet.
```
false
```

### 400

The endpoint will return a 400 response if the `string` parameter is omitted.
This response will be a JSON object as follows:

```json
{
    "Code": "BadRequestError",
    "Message": "Must include string parameter with string to verify",
}
```
