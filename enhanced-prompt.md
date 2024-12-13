# Enhanced Open Interpreter Prompt

## Initial Validation Steps

```python
# Add these validation checks at the start:
def check_system_requirements():
    """Verify system meets minimum requirements"""
    import psutil
    import shutil
    
    # Check RAM (4GB minimum)
    ram_gb = psutil.virtual_memory().total / (1024**3)
    assert ram_gb >= 4, f"Insufficient RAM: {ram_gb:.1f}GB < 4GB required"
    
    # Check disk space (20GB minimum)
    disk_gb = shutil.disk_usage("/").free / (1024**3)
    assert disk_gb >= 20, f"Insufficient disk space: {disk_gb:.1f}GB < 20GB required"

# Add basic error handling to service checks
def verify_services():
    """Verify essential services are responding"""
    import requests
    from time import sleep
    
    # Check Elasticsearch with retry
    for i in range(3):
        try:
            es_response = requests.get("http://localhost:9200")
            assert es_response.status_code == 200
            break
        except:
            if i == 2:
                raise Exception("Elasticsearch failed to start")
            sleep(10)
    
    # Check txtai with retry
    for i in range(3):
        try:
            txtai_response = requests.get("http://localhost:8080")
            assert txtai_response.status_code == 200
            break
        except:
            if i == 2:
                raise Exception("txtai failed to start")
            sleep(10)
```

## Enhanced Streamlit Interface

```python
# Enhanced app.py with better error handling and UI
import streamlit as st
import requests
import json
from datetime import datetime

# Configure page
st.set_page_config(page_title="AI Search Platform", layout="wide")

# Add CSS for better styling
st.markdown("""
    <style>
    .stAlert {margin-top: 1rem;}
    .search-results {padding: 1rem; border-radius: 0.5rem;}
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("AI-Powered Search Platform")
st.markdown("Search across both Elasticsearch and txtai indexes")

# Search interface
with st.form("search_form"):
    query = st.text_input("Enter your search query:")
    submitted = st.form_submit_button("Search")

if submitted and query:
    try:
        # Create columns for results
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Elasticsearch Results")
            es_response = requests.get(
                "http://localhost:9200/test-index/_search",
                json={"query": {"match": {"content": query}}}
            )
            if es_response.status_code == 200:
                results = es_response.json()
                if results['hits']['hits']:
                    for hit in results['hits']['hits']:
                        st.json(hit['_source'])
                else:
                    st.info("No results found in Elasticsearch")
            else:
                st.error("Error querying Elasticsearch")
        
        with col2:
            st.subheader("txtai Results")
            txtai_response = requests.post(
                "http://localhost:8080/search",
                json={"query": query}
            )
            if txtai_response.status_code == 200:
                results = txtai_response.json()
                if results:
                    st.json(results)
                else:
                    st.info("No results found in txtai")
            else:
                st.error("Error querying txtai")
                
    except Exception as e:
        st.error(f"Error processing search: {str(e)}")

# Add system status indicators
with st.sidebar:
    st.subheader("System Status")
    try:
        es_health = requests.get("http://localhost:9200/_cluster/health").json()
        st.success("Elasticsearch: Connected")
        st.json(es_health)
    except:
        st.error("Elasticsearch: Disconnected")
        
    try:
        txtai_health = requests.get("http://localhost:8080/health").json()
        st.success("txtai: Connected")
        st.json(txtai_health)
    except:
        st.error("txtai: Disconnected")
```

## Additional Test Data

```python
# Add more comprehensive test data
def populate_test_data():
    """Populate systems with test data"""
    import requests
    
    # Elasticsearch test documents
    es_documents = [
        {
            "title": "Python Programming",
            "content": "Python is a versatile programming language.",
            "tags": ["programming", "python"]
        },
        {
            "title": "Data Science",
            "content": "Data science combines statistics and programming.",
            "tags": ["data-science", "analytics"]
        }
    ]
    
    # txtai test documents
    txtai_documents = [
        {
            "id": "1",
            "text": "Python is great for data science and machine learning."
        },
        {
            "id": "2",
            "text": "Statistical analysis is key to understanding data."
        }
    ]
    
    # Index Elasticsearch documents
    for doc in es_documents:
        response = requests.post(
            "http://localhost:9200/test-index/_doc",
            json=doc,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code in [200, 201]
    
    # Index txtai documents
    for doc in txtai_documents:
        response = requests.post(
            "http://localhost:8080/add",
            json=doc,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200
```

These enhancements provide:
1. System requirement validation
2. Better error handling
3. Enhanced UI with status monitoring
4. More comprehensive test data
5. Proper service health checks

Would you like me to add any additional elements or explain any part in more detail?