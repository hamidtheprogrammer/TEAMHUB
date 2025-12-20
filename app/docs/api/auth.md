# POST api/v1/register  V1
Creates a new account

## Auth rules
- Auth: Not required
- Role: any

## Request body

```
{
    "username":"string (required)",
    "email":"string (required, valid email)",
    "password":"string (required, minimum length = 8)"
}
```

## Response

### 201 created

```
{
    "id":"uuid",
    "username":"string",
    "email":"string",
    "createdAt":Date
}
```

## Error response

### 400 Bad request

```
{
    "error":"malformed request(bad json)"
}
```

### 409 Conflict

```
{
    "error":"Email already exists"
}
```

### 422 Validation error

```
{
    "error":"validation error"
}
```

## Side effects

- Sends verification email