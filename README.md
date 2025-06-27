# Minutes of Meeting Generator
Discover our MOM (Minutes of Meeting) Generator, a powerful tool for converting .txt and .mp4 files into multi-language meeting minutes. Leveraging React's Carbon UI and RAG implementation, we provide a streamlined, accessible solution for global teams to enhance meeting productivity and communication.

This repository contains all you need to get started and contribute to the project.

## Index

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
      - [Clone the Repository](#clone-the-repository)
      - [Backend Setup](#backend-setup)
      - [FastAPI Server](#start-the-fastapi-server)
      - [Frontend Setup](#frontend-setup)
      - [Start React Application](#start-the-react-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)



## Introduction

The **Minutes of Meeting (MOM) Generator** is a web application designed to automate the creation of meeting minutes from uploaded files. This project supports processing both text and video inputs and can generate minutes in multiple languages, including English, Spanish, Japanese, Portuguese, and French. It leverages FastAPI for the backend and React with Carbon Design System components for a responsive frontend interface. With the integration of Retrieval-Augmented Generation (RAG), the users can inquire and receive answers in English, Spanish, Japanese, French, and Portuguese, making the meeting outcomes accessible to a wider audience.

![MOM Workflow](MOM%20Workflow.png)


## Features

- **File Upload**: Support for `.txt` and `.mp4` file uploads.
- **Progress Bar**: To view the exact status of the MOM Generation.
- **Multi-language Support**: Generates minutes in English, Spanish, Japanese, Portuguese, and French.
- **Modern UI**: Utilizes Carbon Design System for a clean, professional user interface.
- **Retrieval-Augmented Generation (RAG)**: By integrating the RAG feature, our platform not only makes MOMs more accessible but also ensures that every participant has the opportunity to fully understand and engage with the meeting content. It empowers users to explore meeting content deeply, ask targeted questions, and receive instant, accurate answers. This not only improves content accessibility but also promotes a more inclusive and collaborative meeting culture. 

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher

### Installation

### **Backend Setup**
- **Clone the Repository**
   ```sh
   git clone https://github.ibm.com/Shashanka-B-R/Minutes-of-meeting.git
   ```
   
- **Create and Activate a Virtual Environment in backend folder**
    ```sh
    cd backend
    python3 -m venv env
    source env/bin/activate
    ```
    
- **Install Requirements**
    ```sh
    pip install -r requirements.txt
    ```
        
- **Environment Variables**
  Create a .env file with BAM API key:
  ```sh
  GENAI_KEY='YOUR BAM API KEY'
  GENAI_API='https://bam-api.res.ibm.com'
  ```

- **Start the FastAPI Server**

   ```sh
   uvicorn main:app --reload
   ```

### **Frontend Setup**

- In a new terminal, navigate to the frontend directory.

  ```sh
  cd ../frontend
  ```
  
- Install the necessary npm packages.

  ```sh
  npm install
  ```
  
- **Start the React Application**
   ```sh
   npm start
   ```

## Usage
- **Upload a File:** From the main UI, upload a .txt or .mp4 file.
- **Select Languages:** Choose the desired languages for the minutes.
- **Generate and View:** Upload the file and hit the `Generate` button.
- **Seach Query:** Whether you're seeking clarity on a particular point or wish to review what was said by a specific person, this feature provides direct access to the information you need, ensuring no detail goes unnoticed.
