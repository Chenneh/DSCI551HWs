For both patterns, my script sends only one request to firebase per query.

The request url used by this script includes firebase base url, the path pointing to the data(“FILMs”/"ACTORs"), json suffix, "orderBy" parameter indexed on (“category”/"actor_name"), and "equalTo" parameter set by the user input. 

The response brings a json including only relevant data because the irrelvant data was filtered out based on the "orderBy" and "equalTo" parameter sent with the request. For film.py, the "orderBy" parameter will be a "category". For actor.py, the "orderBy" parameter will be an "actor_name". Both "category" and "actor_name" are set to be the indices for the database. 

# film.py

## Database Structure:
![film_database](film_database.PNG)
## Example:

### Query:
```
python .\film.py family
```
### Request URL:
```
https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com/FILMs.json?orderBy="category"&equalTo="family"
```
### URL Componenet
```
Firebase base url: https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com
Path: FILMs
Json suffix: .json
orderBy parameter: orderBy="category"
equalTo parameter: equalTo="family"
```
The request's response only includes  all the family films, and no other kind of films' info will be returned

# actor.py
When there are actors with duplicate name, they will be differentiated by their ids.

## Database Structure:
![actor_database](actor_database.PNG)

## Example:

### Query:
```
python .\actor.py "ed chase"
```
### Request URL:
```
https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com/ACTORs.json?orderBy="actor_name"&equalTo="ed chase"
```
### URL Componenet
```
Firebase base url: https://dsci551-hw1-52ec5-default-rtdb.firebaseio.com
Path: ACTORs
Json suffix: .json
orderBy parameter: orderBy="actor_name"
equalTo parameter: equalTo="ed chase"
```
The request's response only includes the info films that Ed Chase performed in, and no other films' info was returned.