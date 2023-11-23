# Chaabi Assignment 2023
This Repository contains the code for custom gpt . Which can generate the answers from the given context. Here we have used a CSV file as source for context. which can be found [here](https://github.com/rahim-khan-iitg/custom-gpt-backend/tree/master/data). 

<b>This Project is divided into 2 section <i>Backend</i> and <i>Frontend</i> . This Repo contains the Backend part and frontend can be found [here](https://github.com/rahim-khan-iitg/custom-gpt-frontend) 

<b>Deployed version of the app can be accessed [here](https://custom-gpt-five.vercel.app/)</b>

## Setup with Docker
for the setup docker should be installed on the machine. follow the given steps to setup the docker image on the local machine
- step 1
```
# pull the image from docker hub
docker pull rahimkhaniitg/custom-gpt:2.0
```
- step 2
```
# run the image
docker container run  -d -p 5000:5000  rahimkhaniitg/custom-gpt:2.0
```
- step 3
```
# access the endpoint for chat
http://localhost:5000/chat
# access the endpoint for query
http://localhost:5000/query

```
- step 4 \
make a post request to the endpoints with json
```
{"question":<type your question here>}

```
## Local setup without Docker

- step 1
```
# clone the repo
git clone https://github.com/rahim-khan-iitg/custom-gpt-backend

# change the directory
cd custom-gpt-backend

```
- step 2
```
# install the requirements.txt
pip install -r requirements.txt

```
- step 3
```
# install the src package
pip install --no-cache-dir .

```
- step 4 \
now make a ```.env``` file for the api key and environment variables. specify these entries.
```
HUGGINGFACE_API_TOKEN="YOUR HUGGINGFACE API HERE"
HUGGINGFACE_LLM_REPO_ID="LLM MODEL HERE"
HUGGINGFACE_EMBEDDING_REPO_ID="EMBEDDING MODEL NAME HERE"
QDRANT_URL="QDRANT API URL HERE"
QDRANT_API_KEY="QDRANT API KEY HERE"

```
<i>for LLM I have used ```google/flan-t5-xxl``` and for embedding model I have used ```sentence-transformers/paraphrase-multilingual-mpnet-base-v2```</i>

- step 5 \
make vector embedding and store them . run the command given below and we have 2 choices here chroma and qdrant both can be used 
```
python src\pipelines\data_loading_pipeline.py
```
here you will be asked for the chroma or qdrant for chroma type chroma and hit enter it will make the vector embeddings and save them in the local folder. \
if you choose qdrant you will be asked to enter the collection name . Enter the collection name and hit enter. now data will be saved in the qdrant cloud \
by default it will use qdrant as vector database . if you want to use chroma as database you have to uncomment the retriver1 for chroma and comment out the retriever1 of qdrant in the file src/pipelines/chat_pipelines.py class QueryModel 

- step 6 \
Now we are in the state of running our application
```
# run the app
python app.py

```
this command will run the server at 5000 port now you can access the ```http://localhost:5000/``` and HTML page showing hello will shown. it indicates that our app is working. \
now we can access the endpoints  ```http://localhost:5000/chat``` for chat without context and ```http://localhost:5000/query``` for querying the data we have stored in the database.
- step 7 \
now we can make post request to our endpoints
```
{"question":<type your question here>}

```

<i>Other than that i have deployed the same container on Azure container service these endpoints can be accessed via the links given below and also i forgot to mention this app is made using flask </i>\
[https://custom.ambitiousfield-446dccee.centralindia.azurecontainerapps.io/query](https://custom.ambitiousfield-446dccee.centralindia.azurecontainerapps.io/query) \
[https://custom.ambitiousfield-446dccee.centralindia.azurecontainerapps.io/chat](https://custom.ambitiousfield-446dccee.centralindia.azurecontainerapps.io/chat)