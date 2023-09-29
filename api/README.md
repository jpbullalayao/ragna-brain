# APIs

In this section of the library, we explain exactly what an "API" is, demonstrate best practices for building APIs properly, and share relevant concepts that every engineer needs to know in order to become a great API developer.

## What is an API?

In the simplest terms, an **Application Programming Interface (API)** is a service that one would use (a "client", which could also be considered a "developer" if you take a step back further) to gain access to back-end data or functionality. Generally, when a client integrates with an API, they want to either process their own data (ex: save user sign-up info into a database) or do something useful with the data they are accessing (ex: display a user name on a web page).

APIs aren't specific to back-end data and functionality, as technically you can also write logic on the front-end that serves as an "API" to whoever is using it as well, however for the purposes of this section, we will assume that we are talking about a back-end API.

## What languages can we expect an API to be written in?
At any start-up or large company that you encounter, their APIs would likely be written in a language that access a database, such as a MySQL or PostgreSQL one.

If you want to learn how to build an API, you can expect to work in one of the following languages / associated frameworks (not all possibilities listed):

1. Python (Django REST Framework)
2. JavaScript (Node.js)
3. Ruby (Ruby on Rails)
4. PHP (Laravel)

There are many more potential languages and frameworks to work in, but these are the technologies I have the most experience and knowledge in to be able to speak to.
