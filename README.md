# Application - Github List

The purpose of this application is to allow users to fetch user and repositories data from github via a REST api.


##### Hosted at "http://apigit-guilhermebastos.heroku.com" the API has 5 endpoints.

##### Swagger: https://apigit-guilhermebastos.herokuapp.com/api_doc/

##### That can be known as showed in the resources below:
>----/apigithub
>
>----------------/user/
>
>----------------/users/
>
>----------------/repos/
>
>----------------/users-repos/
>
>----------------/users-repos-populate/

- ### /apigithub/user/
> This resource retrieves a user and returns its username, github url and github id.
> It must be called through GET method using application/json in the body.

HTTP body application/json example:
>{
>	"username":"cavalcantegb"
>}

- ### /apigithub/users/
> This resource lists users and returns them with pagination.
> It must be called through GET method using application/json in the body.

HTTP body application/json example:
>{
>	"page":1,
>   "per_page":3
>}

- ### /apigithub/repos/
> This resource provides the repos from a specific user.
> It must be called through GET method using application/json in the body.

HTTP body application/json example:
>{
>	"username":"cavalcantegb"
>}

- ### /apigithub/user-repos/
> This resource retrieves from our database all users and their github repos.
> This resource must be called through GET method.
> It will accept an array of users as shown below in the example.

- ### /apigithub/user-repos-populate/
> This resource receives a list of users and save them in the database with their respectives
> repositories.
> This resource must be called through POST method using application/json in the body.
> It will accept an array of users as shown below in the example.

HTTP body application/json example:
>{
>	"users" : [
>               {"user":"cavalcantegb"}
>             ]
>}
