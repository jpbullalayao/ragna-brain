# APIs

In this section of the library, we explain exactly what an "API" is, demonstrate best practices for building APIs properly, and share relevant concepts that every engineer needs to know in order to become a great API developer.

## What is an API?

In the simplest terms, an **Application Programming Interface (API)** is a service that one would use (a "client", which could also be considered a "developer" if you take a step back further) to gain access to back-end data or functionality. Generally, when a client integrates with an API, they want to either process their own data (ex: save user sign-up info into a database) or do something useful with the data they are accessing (ex: display a user name on a web page).

APIs aren't specific to back-end data and functionality - technically you can also write logic on the front-end that serves as an "API" to whoever is using it as well, however for the purposes of this section, we will assume that we are talking about a back-end API.

## What languages can we expect an API to be written in?
At any start-up or large company that you encounter, their APIs would likely be written in a language that access a database, such as a MySQL or PostgreSQL one.

If you want to learn how to build an API, you can expect to work in one of the following languages / associated frameworks (not all possibilities listed):

1. Python (Django REST Framework)
2. JavaScript (Node.js)
3. Ruby (Ruby on Rails)
4. PHP (Laravel)

There are many more potential languages and frameworks to work in, but these are the technologies I have the most experience and knowledge in to be able to speak to.

## Best Practices for Building APIs

Just like any other a software application, an API should follow specific guidelines (as established by its associated engineering team) to not only make it easy for any developer to work in, but to also allow for any client to easily integrate with. While guidelines will vary on the engineering team, the following guidelines can serve as a good reference for any engineering team that might not otherwise know how to get started with best architecting an API project:

### 1. Use forward slashes in the endpoint path to represent hierarchical relationships between resources/objects

To demonstrate this, let's consider a simplified example of [Amazon](amazon.com). On the back-end of Amazon, we have `Product`s that users can browse through, and for each product, users who have previously bought the product can leave `Review`s on these products. On the back-end, that would mean that there is a database relationship between a `Product` and a `Review`, where a specific record in the `reviews` table will have a foreign key called `product_id` that maps to a record in the `products` table.

Within the context of building an API, how do we use this guideline to define a proper endpoint URL that the Amazon web client can request in order to display all the customer reviews for a given product?

Simply, we can use define following endpoint path:

```
/products/{productId}/reviews
```

### 2. When defining dynamic placeholders in an endpoint path, use camelCase

Good:
```
/messages/{messageId}
```

Bad:
```
/messages/{MessageID}
```

### 3. Use lower-case letters when defining endpoint paths

Good:
```
/users/{userId}/comments
```

Bad:
```
/Users/{userId}/Comments
```


