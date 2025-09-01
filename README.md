# Candidate-Evaluation-Using-LangGraph

An intelligent recruitment system that automates candidate evaluation using LangGraph workflows and AI-powered assessment. This project demonstrates how to build a sophisticated recruitment pipeline that categorizes candidates, evaluates their skills, and routes them through different evaluation stages based on their qualifications.

## 🚀 Features

- **AI-Powered Candidate Evaluation**: Uses Ollama LLMs to assess candidate experience and skills
- **Intelligent Workflow Routing**: Automatically routes candidates based on experience level and skills match
- **Experience Level Categorization**: Classifies candidates as Entry Level (0-2 years), Mid Level (2-5 years), or Senior (5+ years)
- **Skills Assessment**: Evaluates candidate suitability for Machine Learning Engineer positions
- **Conditional Decision Making**: Smart routing to interviews, recruiter review, or rejection
- **Modular Architecture**: Clean separation of concerns with dedicated modules for different functionalities
- **Docker Support**: Complete containerization with optimized Ollama integration
- **Smart Caching**: Efficient Ollama configuration caching for improved performance
- **PDF Processing**: Automated resume text extraction and processing
- **Robust Error Handling**: Comprehensive error handling and fallback mechanisms

## 🏗️ Architecture

The project follows a modular architecture with four main components:

```
main.py          ← Main entry point and graph orchestration
├── evaluation.py ← AI-powered evaluation functions with smart caching
├── data.py      ← PDF extraction and data processing
└── Dockerfile   ← Container configuration
```

### Workflow Structure

```
START → Categorize Candidate Experience → Evaluate Candidate Skills → [Conditional Routing]
                                                                    ├─ To Interview → Eligible For Interview → END
                                                                    ├─ To Recruiter → Evaluate By Recruiter → END
                                                                    └─ Rejected → Reject Candidate → END
```

## 🛠️ Installation

1. **Create a Virtual Environment**
   ```bash
   virtualenv <Environment name>
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and start Ollama**
   ```bash
   # Install Ollama (follow instructions at https://ollama.ai)
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Start Ollama service
   ollama serve
   ```

4. **Download required models**
   ```bash
   ollama pull gemma3:12b
   ollama pull mistral
   ```

### Option 2: Docker Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tayyabwahab/Candidate-Evaluation-Using-LangGraph.git
   cd "Candidate-Evaluation-Using-LangGraph"
   ```
2. **Install Ollama on host machine**
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ollama serve
   ollama pull gemma3:12b
   ollama pull mistral
   ```

3. **Download and run the Docker Image**
   ```bash
   docker pull tayyabwahab/cand_eval
   docker run cand_eval
   ```

3. **Build and run Docker container**
   You can bulid docker image locally using Dockerfile
   
   ```bash
   # Build the image
   docker build -t cand_eval .
   
   # Run the container
   docker run cand_eval
   ```

## 🚀 Usage

### Local Usage

1. **Run the main application**
   ```bash
   python main.py
   ```

2. **The system will:**
   - Create and visualize the evaluation workflow graph
   - Process candidate data from the provided resume
   - Run the candidate through the evaluation pipeline
   - Display the final evaluation results


### Understanding the Output

The system provides:
- **Experience Level**: Entry/Mid/Senior categorization
- **Skills Match**: Yes/No assessment for ML Engineer role
- **Final Outcome**: Interview selection, recruiter review, or rejection
- **Visual Workflow**: Graph representation of the decision process

## 🔧 Configuration

### LLM Models

The system is designed for local usage and will work any open source LLM via Ollama.
Current flow was tested with two models:
- `gemma3:12b`
- `mistral`

### Customizing Prompts

Modify the prompt templates in `evaluation.py` to adjust:
- Experience level criteria
- Skills assessment criteria
- Evaluation logic

## 📊 Evaluation Criteria

### Experience Levels
- **Entry Level**: 0-2 years of experience
- **Mid Level**: 2-5 years of experience
- **Senior**: 5+ years of experience


### Skills Assessment
- Evaluates suitability for Machine Learning Engineer position
- Considers technical skills, experience relevance, and background
- Provides binary yes/no decision

### Routing Logic
- **Senior + Skills Match**: → Interview
- **Senior + No Skills Match**: → Recruiter Review
- **Other combinations**: → Rejection



## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
