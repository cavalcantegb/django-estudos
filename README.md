# Application - Github List

The purpose of this application is to allow users to fetch user and repositories data from github via a REST api.


##### Hosted at "http://apigithub-guilhermebastos.heroku.com" the API has 5 endpoints.

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