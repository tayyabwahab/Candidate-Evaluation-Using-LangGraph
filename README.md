# Candidate-Evaluation-Using-LangGraph

An intelligent recruitment system that automates candidate evaluation using LangGraph workflows and AI-powered assessment. This project demonstrates how to build a sophisticated recruitment pipeline that categorizes candidates, evaluates their skills, and routes them through different evaluation stages based on their qualifications.

## 🚀 Features

- **AI-Powered Candidate Evaluation**: Uses Ollama LLMs to assess candidate experience and skills
- **Intelligent Workflow Routing**: Automatically routes candidates based on experience level and skills match
- **Experience Level Categorization**: Classifies candidates as Entry Level (0-2 years), Mid Level (2-5 years), or Senior (5+ years)
- **Skills Assessment**: Evaluates candidate suitability for Machine Learning Engineer positions
- **Conditional Decision Making**: Smart routing to interviews, recruiter review, or rejection
- **Modular Architecture**: Clean separation of concerns with dedicated modules for different functionalities

## 🏗️ Architecture

The project follows a modular architecture with three main components:

```
main.py          ← Main entry point and graph orchestration
└── evaluation.py ← AI-powered evaluation functions
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

3. **Download required models**
   ```bash
   ollama pull gemma3:12b
   ollama pull mistral
   ```

## 🚀 Usage

### Basic Usage

1. **Run the main application**
   ```bash
   python main.py
   ```

2. **The system will:**
   - Create and visualize the recruitment workflow graph
   - Process candidate data from `data.py`
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
Current setting works with the following details that can be changed according to requirements:
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

## 🙏 Acknowledgments

- **LangGraph** for the workflow orchestration framework
- **LangChain** for the LLM integration capabilities
- **Ollama** for providing local LLM capabilities
- **Matplotlib** for graph visualization