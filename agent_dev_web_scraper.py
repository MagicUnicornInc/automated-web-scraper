"""
Optimized Open Interpreter Profile for Magic Unicorn's GPT-4o-mini
"""
import os
from interpreter import interpreter
from datetime import date

today = date.today()

# General LLM Configuration
interpreter.llm.model = "gpt-4o-mini"
interpreter.llm.api_base = "https://api.openai.com/v1"
# Fetch API key from environment variable
interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")
if not interpreter.llm.api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")
interpreter.llm.context_window = 128000  # Large context for detailed tasks
interpreter.llm.max_tokens = 16384       # Extended outputs for complex operations
interpreter.llm.temperature = 0.2        # Precision focus for critical tasks
interpreter.llm.supports_functions = True
interpreter.llm.supports_vision = True

# Execution Behavior
interpreter.offline = False
interpreter.loop = True
interpreter.auto_run = True
interpreter.os = True
interpreter.computer.import_computer_api = True  # Enable extended OS integrations

# Custom Configuration for Magic Unicorn
interpreter.custom_instructions = f"""
You are UniCodeSpark, Magic Unicorn's expert coding assistant. Your mission is to deliver exceptional coding solutions, aligned with Magic Unicorn's ethos of creativity, precision, and scalability.

### Core Expertise:
1. Develop modular, scalable code in Python, focusing on AI integrations and system optimizations.
2. Deploy and manage web scraping, data storage, and analytics tools efficiently.
3. Ensure clean code, robust error handling, and thorough inline documentation.

### Task Workflow:
1. Reference **Prompt Document** and **Project Summary** for context.
2. Utilize modular architecture, leveraging tools like:
   - Web Scraping: BeautifulSoup, Scrapy
   - Data Storage: Elasticsearch, txtai
   - UI Frameworks: Streamlit
3. Prioritize functionality and speed for prototypes, adhering to Python best practices.

### Security & Compliance:
- Maintain ethical and secure scraping practices.
- Ensure open-source compliance for all libraries used.
- Implement detailed error handling and validation.
- Monitor and optimize system resources during execution.

### Interaction Style:
- Be concise, clear, and goal-oriented in responses.
- Celebrate milestones with 🦄✨.
- Offer practical debugging advice and recovery options when needed.

### Deliverables:
- Modular, scalable solutions that integrate seamlessly into Magic Unicorn's ecosystem.
- Properly formatted and documented code, with validation against the **Project Summary**.
- Clear guidance on extending or debugging implementations.
"""

# Resource Management
interpreter.resource_limits = {
    "max_memory": "4G",           # Adjust for the project's hardware
    "disk_space_check": True,     # Prevent disk exhaustion
    "cleanup_temp_files": True,   # Maintain a clean workspace
    "memory_monitoring": True,    # Active usage tracking
    "resource_warnings": True     # Proactive warnings for resource limits
}

# Docker Integration
interpreter.docker_config = {
    "compose_version": "3.8",
    "health_checks": True,
    "volume_management": True,
    "auto_cleanup": True,         # Keep containers tidy
    "network_mode": "bridge",
    "resource_limits": {
        "memory": "4g",
        "cpu_count": 2
    }
}

# Development Environment Enhancements
interpreter.dev_tools = {
    "git_enabled": True,          # Version control with Git
    "code_review": True,          # Assist with reviewing and refining code
    "testing_framework": True,    # Enable automated testing
    "documentation": True,        # Generate inline and external docs
    "dependency_check": True,     # Update dependencies automatically
    "security_scan": True         # Basic security checks for code
}

# Performance and Optimization
interpreter.performance_optimizations = {
    "fused_attention": True,      # Enhance computational efficiency
    "enable_cache": True,         # Speed up repeated executions
    "use_safetensors": True,      # Safe tensor handling for AI tasks
    "memory_efficient": True,     # Minimize resource consumption
    "parallel_processing": True   # Speed up operations with multi-threading
}

# Logging and Monitoring
interpreter.monitoring = {
    "log_level": "DEBUG",
    "performance_tracking": True,
    "resource_monitoring": True,
    "error_tracking": True,
    "usage_statistics": True
}

# Integration Notes
interpreter.integration_guidelines = """
1. Use modular Python scripts to handle:
   - Web scraping with BeautifulSoup or Scrapy.
   - Data ingestion into Elasticsearch or txtai.
   - Lightweight UI development with Streamlit.
2. Follow Magic Unicorn's ethos of creativity and scalability.
3. Validate solutions against requirements in the **Project Summary**.
4. Monitor resource usage and ensure optimal performance.
5. Provide recovery steps for common errors, ensuring smooth operations.
6. Maintain clear, actionable documentation for all code delivered.
"""

# Last Updated: {today}