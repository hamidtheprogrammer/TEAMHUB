# 1 GET /users v1
List all users

## 1.1 Auth rules
- Auth: Required
- Role: Admin

## 1.2 Request body
- not applicable

## 1.3 Response

### 1.3.1 200 Ok
```
{
    users:[
        {
            "id":"string", 
            "username":"string", 
            "email":"string"
            "verified":Bool
        }
    ]
}
```

### 1.3.2 401 Unauthorised
```
{
    message:"Unauthorized"
}
```

# 2 DELETE /user/{id} v1

# 2.1 Auth Rules
- Auth: Required
- Role: Admin

# 2.2 Request body
- not applicable

# 2.3 Response

# 2.3.1 200 OK
```
{
    message: "User successfully deleted"
}
```

### 2.3.2 401 Unauthorised
```
{
    message:"Unauthorized"
}
```
