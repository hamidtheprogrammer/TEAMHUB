# 1 POST /teams

# 1.1 Auth rules
- Auth: Required
- Role: Admin

# 1.2 Request body
```
{
    "name":"string"
}
```

# 1.3 Response

# 1.3.1 201 Created
```
{
    "id":int
    "name":"string"
    "projects":list
    "users":list
}
```