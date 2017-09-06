# TODOS

* [X] Add a RESTful, read-only API to allow consumers to retrieve Questions with Answers as JSON (no need to retrieve Answers on their own). The response should include Answers inside their Question as well as include the id and name of the Question and Answer users
* [X] questions in ui
* [X] validate headers with api_key
* [X] rate limit till 100 requests
* [X] API requests on a per-Tenant basis
* [X] login as user
* [X] register as user
* [X] create tenent api_key (uuid) on register
* [X] aggregating answers and question from different field
* [X] filtering questions on user and private basis
* [ ] Allow adding a query parameter to the API request to select only Questions that contain the query term(s). Return an appropriate HTML status code if no results are found
* [ ] tests
* [X] models added for creating dummy data
* [X] Tenant API request counts for all Tenants | present in @validate_api custom @decorator that attaches to every api
* [ ] Track API request counts per Tenant | done aggregate tenent count


