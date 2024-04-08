# API Endpoints


Official Documentation of the API is readable and downloadable here ---> https://api.mindat.org/schema/redoc/
This is a human-written parsing of the specifics of the API implementation. It may be incorrect and is not part of the official OpenMindat implementation and research. 

## /api-token-auth/

- `POST` referes to a HTTP request method.  
- `https://api.mindat.org/api-token-auth/` is the target URL of this `POST` method.
- I believe this `POST` allows a username and password to be passed to the Mindat Server
- `username`, `password`, and `token` are all type `string` with `readOnly`. 
- This endpoint provides three different ways to create an authentication token:
  - application/x-www-form-urlencoded,
  - multipart/form-data,
  - application/json
 
- The AutToken is defined as a component further down in the .YAML and is as follows:

    AuthToken:
      type: object
      properties:
        username:
          type: string
          writeOnly: true
        password:
          type: string
          writeOnly: true
        token:
          type: string
          readOnly: true
      required:
      - password
      - token
      - username
  
  - `post` is what is allowed for this here and I am not sure if this endpoint has any
  - `AuthToken[]` is important and appears elsewhere in the docs. 

## Other
/countries/
  - get
/countries/{id}/
  - get
/create/
  - post
/dana-8/
  - get
/dana-8/{idtemp}/
  - get
/dana-8/groups/
  - get
/dana-8/subgroups/
  - get
/geomaterials/
  - get
/geomaterials/{id}/
  - get
/geomaterials/{id}/varieties/
  - get
/geomaterials/dict/
  - get
/geomaterials_search/
  - get
/localities/
  - get
/localities/{id}/
  - get
/locality_age/
  - get
/locality_age/{age_id}/
  - get
/locality_status/
  - get
/locality_status/{ls_id}/
  - get
/locality_type/
  - get
/locality_type/{lt_id}/
  - get
/locgeoregion2/
  - get
/locobject/{id}/
  - get
/minerals_ima/
  - get
/minerals_ima/{id}/
  - get
/nickel-strunz-10/
  - get
/nickel-strunz-10/{id}/
  - get
/nickel-strunz-10/classes/
  - get
/nickel-strunz-10/families/
  - get
/nickel-strunz-10/subclasses/
  - get
/photocount/
  - get

