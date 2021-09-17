For both patterns, my script sends only one request to firebase per query.
# film.py
The request url used by this script includes firebase base url, the path pointing to the data(“FILMs”), json suffix, orderBy parameter indexed on “category”, and equalTo parameter set by the user input. 

The response brings a json including only films categorized the same as user input, so no irrelevant data was returned.
##Example:

### Query:
```
python .\film.py family
```
###Request URL:
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
The request url used by this script includes firebase base url, the path pointing to the data, json suffix, orderBy parameter indexed on “actor_name”, and equalTo parameter set by the user input. 

The response brings a json including only the films where the input actor performed, so no irrelevant data was returned.

When there are actors with duplicate name, they will be differentiated by their ids.
##Example:

### Query:
```
python .\actor.py "ed chase"
```
###Request URL:
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