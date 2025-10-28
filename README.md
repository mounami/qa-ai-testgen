# QA AI TestGen 
An AI-driven framework that auto-generates test cases and integrates with Rally for seamless QA coverage.

I’ve built a FastAPI-based backend app called QA-AI-TestGen.
It uses mock Rally data to simulate how an AI system could generate test cases automatically for QA teams.
The app runs locally on my laptop, has multiple endpoints, and serves as a base for integrating real AI logic later.”



## Features

- FastAPI backend with modular structure
- Mock Rally stories for simulation
- Placeholder for AI-based test case generation
- Interactive API docs (Swagger UI)
- Easy setup for local development

## Visit the endpoints
Endpoint	            Method	                Description
    /	                GET	                    Health check & welcome message
    /rally-stories	    GET	                    Returns mock Rally stories
    /generate-testcases	POST	                Simulates AI-generated test cases

## Open your browser:

Main: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs