# 1 POST auth/register  V1
Creates a new account

## 1.1 Auth rules
- Auth: Not required
- Role: any

## 1.2 Request body

```
{
    "username":"string (required)",
    "email":"string (required, valid email)",
    "password":"string (required, minimum length = 8)"
}
```

## 1.3 Response

### 1.3.1 201 created

```
{
    "id":"uuid",
    "username":"string",
    "email":"string",
    "role":"admin"|"user",
    "verified":bool,
    "teams":[],
    
}
```

## 1.4 Error response

### 1.4.1 400 Bad request

```
{
    "error":"malformed request(bad json)"
}
```

### 1.4.2 409 Conflict

```
{
    "error":"Email already exists"
}
```

### 1.4.3 422 Validation error

```
{
    "error":"validation error"
}
```

## 1.5 Side effects

- Sends verification email (http://client-base-url/verify-account/{id}/{token})


# 2 POST auth/verify-token/{token}  V1
This endpoint is either used to reset password or verify account, if the tokenType is set to password and password is provided in the body, it will verify that the password token matches the above token in url and update password, however, if tokenType is verification, it will check that url token matches account verification token and verify acccount.

NOTE: Password token is generated upon clicking reset password, an email containing a url with the token is sent from the server which provides a page to the user to create a new password, Once submitted, password is sent along side url token. However, account verification mail is sent upon registration, the link takes the user to a page which triggers account verification on the server.

For this project, email sending is intentionally stubbed due to domain verification requirements.In development mode, verification tokens are returned in the API response for testing purposes. In production, this service would integrate with a transactional email provider

## 2.1 Auth rules
- Auth: Not required
- Role: any

## 2.2 Request body

```
{
    "id":"str",
    "tokenType":"password" | "verification"
    "password":"string (required, minimum length = 8)"| null
}
```

## 2.3 Response

### 2.3.1 200 OK

```
{
    "error":"Password reset successful" | "verification successful"
}
```

## 2.4 Error response

### 2.4.1 422 Validation error

```
{
    "error":"validation error(Invalid Token | Password too short)"
}
```

### 2.4.2 404 not found

```
{
    "error":"user not found"
}
```

# 3 POST auth/login V1

## 3.1 Auth rules
- Auth: not required
- role: any

## 3.2 Request body

```
{
    "email":"string(valid email address)",
    "password":"string"
}
```

## 3.3 Response

```
{
    "id":"uuid",
    "username":"string",
    "email":"string",
    "role":"admin"|"user",
    "verified":bool,
    "teams":[],
    
}
```

## 3.4 Error Response

### 3.4.1 401 not authorized

```
{
    "error":"Invalid credentials"
}
```

# 4 POST auth/reset-password V1
Reset password

## 4.1 Auth rules
- Auth: not required
- Role: any

## 4.2 Request body

```
{
    "email":"string(valid email)"
}
```

## 4.3 Response

### 4.3.1 200 OK

```
{
    "message":"success"
}
```

## 4.4 Error response

### 4.4.1 404 not found

```
{
    "error":"user not found"
}
```

## 4.5 Side effect
- Sends password reset link (http://client-base-url/reset-password/{id}/{token})