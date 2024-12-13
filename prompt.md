Prompt Document for Open Interpreter

Objective: Set up a lightweight, local AI-powered search platform using Elasticsearch and txtai, integrated with a simple Streamlit app for testing and demonstration purposes.

Instructions for Open Interpreter

1. Install Required Tools
	1.	Ensure Docker and Docker Compose are Installed:

# Update package index
sudo apt update

# Install Docker and Docker Compose
sudo apt install docker.io docker-compose -y

# Start and enable Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
docker --version
docker-compose --version


	2.	Install Python and pip:

sudo apt install python3 python3-pip -y
python3 --version
pip3 --version


	3.	Install Streamlit:

pip install streamlit

2. Create the Project Structure
	1.	Create a directory for the project:

mkdir ai_search_platform && cd ai_search_platform
mkdir -p data/elasticsearch data/txtai logs


	2.	Create a docker-compose.yml file in the project directory:

version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.0
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
      - "9300:9300"
    volumes:
      - ./data/elasticsearch:/usr/share/elasticsearch/data
    restart: always

  txtai:
    image: neuml/txtai:latest
    container_name: txtai
    ports:
      - "8080:8000"
    volumes:
      - ./data/txtai:/data
    restart: always

3. Start the Services
	1.	Launch Elasticsearch and txtai:

docker-compose up -d


	2.	Verify that both services are running:

docker ps


	3.	Test the services:
	•	Elasticsearch:

curl http://localhost:9200


	•	txtai:

curl http://localhost:8080

4. Populate the Databases
	1.	Add test data to Elasticsearch:

curl -X POST "http://localhost:9200/test-index/_doc" -H "Content-Type: application/json" -d '{
  "title": "Test Document",
  "content": "This is a test document for Elasticsearch."
}'


	2.	Add test data to txtai:

curl -X POST "http://localhost:8080/add" -H "Content-Type: application/json" -d '{
  "id": "1",
  "text": "This is a test document for txtai."
}'

5. Create the Streamlit App
	1.	Create a file named app.py in the project directory:

import streamlit as st
import requests

st.title("AI-Powered Search Platform")

query = st.text_input("Enter your search query:")

if query:
    # Elasticsearch query
    es_response = requests.get(
        "http://localhost:9200/test-index/_search",
        json={"query": {"match": {"content": query}}}
    ).json()

    # txtai query
    txtai_response = requests.post(
        "http://localhost:8080/search",
        json={"query": query}
    ).json()

    st.write("### Elasticsearch Results")
    st.json(es_response)

    st.write("### txtai Results")
    st.json(txtai_response)


	2.	Run the Streamlit app:

streamlit run app.py

6. Validate Functionality
	1.	Open the Streamlit app in a browser (the URL will be displayed in the terminal).
	2.	Test queries to ensure both Elasticsearch and txtai return results.
	3.	Verify logs for potential issues:

docker-compose logs elasticsearch
docker-compose logs txtai

7. Cleanup (Optional)

If services need to be stopped or reset:

docker-compose down -v

Expected Deliverables
	1.	Functional local setup with Elasticsearch and txtai running via Docker.
	2.	A working Streamlit app to query both services and display results.
	3.	Test data successfully indexed in Elasticsearch and txtai.
	4.	Verified system functionality through Streamlit.

This prompt ensures everything is set up and operational for a lightweight proof of concept. Let me know if you need further adjustments!