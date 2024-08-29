# Software Engineering Idea Processor

## 🚀 Overview

The Software Engineering Idea Processor is an innovative multi-agent AI system that transforms high-level project ideas into detailed software specifications and code structures. Built using CrewAI and Streamlit, this application leverages a team of specialized AI agents to break down, design, and implement software projects based on user input.

## 🛠 Technologies Used

- [CrewAI](https://github.com/crewAIInc/crewAI)
- [Streamlit](https://streamlit.io/)
- [OpenAI GPT-4](https://openai.com/gpt-4)
- [Langchain](https://github.com/langchain-ai/langchain)
- [Serper API](https://serper.dev/)
- Docker
- Google Cloud Run

## 📋 Prerequisites

- Python 3.10+
- OpenAI API key
- Serper API key
- Langtrace API key (for metrics)
- Docker (for containerization and deployment)
- Google Cloud account (for deployment to Google Cloud Run)

## 🏗 Project Structure

```
.
├── app/
|   ├── config/
│           ├── agents.yaml
│           |── tasks.yaml
│   ├── __init__.py
│   ├── crew.py
│   ├── main.py
│   |── streamer.py
│   |── streamlit_app.py
│   |── utils.py
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
```

## 🤖 Multi-Agent Architecture

### AI Agents

The system uses several specialized AI agents:

- **Manager**: Oversees the project and coordinates other agents.
- **UI/UX Engineer**: Selects appropriate design templates and interactive elements.
- **Frontend Engineer**: Develops React-based frontend code.
- **Backend Engineer**: Creates TypeScript and Express-based backend structure.
- **Writer Agent**: Organizes and outputs the final code structure.

### Tasks

- **Idea Expansion**: Breaks down and expands on initial project ideas.
- **UI/UX Design**: Searches for and selects the best visual design and interactive elements.
- **Frontend Development**: Implements React-based frontend code.
- **Backend Architecture**: Creates TypeScript and Express-based backend structure.
- **Code Organization**: Compiles and organizes all generated code into a coherent project structure.

### 🔧 Configuration

Agent and task configurations are stored in YAML files:

- `config/agents.yaml`: Defines agent roles, goals, and backstories.
- `config/tasks.yaml`: Specifies tasks for each agent.


## 🚀 Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/software-engineering-idea-processor.git
   cd software-engineering-idea-processor
   ```
2. Setup a virtual environment

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SERPER_API_KEY=your_serper_api_key
   LANGTRACE_API_KEY=your_langtrace_api_key
   DEBUG=True
   ```

## 🖥 Running the Application

### Local Streamlit Run

1. Run the Streamlit app:
   ```
   cd app
   
   streamlit run streamlit_app.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

### Local Docker Run

1. Build and run the Docker container:
   ```
   docker-compose up --build
   ```

2. Access the application at `http://localhost:8501`.

### Deployment to Google Cloud Run

1. Install and set up the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).

2. Authenticate with Google Cloud:
   ```
   gcloud auth login
   ```

3. Set your project ID:
   ```
   gcloud config set project YOUR_PROJECT_ID
   ```

4. Build and push the Docker image to Google Container Registry:
   ```
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/software-engineering-idea-processor
   ```

5. Deploy to Google Cloud Run:
   ```
   gcloud run deploy software-engineering-idea-processor \
     --image gcr.io/YOUR_PROJECT_ID/software-engineering-idea-processor \
     --platform managed \
     --region YOUR_PREFERRED_REGION \
     --allow-unauthenticated \
     --set-env-vars="OPENAI_API_KEY=your_key,SERPER_API_KEY=your_key,LANGTRACE_API_KEY=your_key"
   ```

6. Access your deployed application using the URL provided by Google Cloud Run.


## 📊 Metrics

Click the "View metrics on Langtrace" button in the Streamlit sidebar to access detailed performance metrics.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgements

- The CrewAI and Streamlit communities for their excellent tools and documentation.

## 🆘 Troubleshooting

If you encounter any issues during setup or deployment, please check the following:

1. Ensure all required API keys are correctly set in your environment variables.
2. For Docker-related issues, make sure Docker is installed and running on your system.
3. For Google Cloud Run deployment issues, verify that you have the necessary permissions and that your Google Cloud SDK is properly configured.

If problems persist, please open an issue on the GitHub repository with a detailed description of the problem and any relevant error messages.