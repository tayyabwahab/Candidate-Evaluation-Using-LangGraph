# Recruitment Agency using LangGraph

An intelligent recruitment system that automates candidate evaluation using LangGraph workflows and AI-powered assessment. This project demonstrates how to build a sophisticated recruitment pipeline that categorizes candidates, evaluates their skills, and routes them through different evaluation stages based on their qualifications.

## 🚀 Features

- **AI-Powered Candidate Evaluation**: Uses Ollama LLMs to assess candidate experience and skills
- **Intelligent Workflow Routing**: Automatically routes candidates based on experience level and skills match
- **Experience Level Categorization**: Classifies candidates as Entry Level (0-2 years), Mid Level (2-5 years), or Senior (5+ years)
- **Skills Assessment**: Evaluates candidate suitability for Machine Learning Engineer positions
- **Conditional Decision Making**: Smart routing to interviews, recruiter review, or rejection
- **Visual Workflow Representation**: Matplotlib-based visualization of the recruitment workflow
- **Modular Architecture**: Clean separation of concerns with dedicated modules for different functionalities

## 🏗️ Architecture

The project follows a modular architecture with three main components:

```
main.py          ← Main entry point and graph orchestration
├── evaluation.py ← AI-powered evaluation functions
└── data.py      ← Data extraction and processing
```

### Workflow Structure

```
START → Categorize Candidate Experience → Evaluate Candidate Skills → [Conditional Routing]
                                                                    ├─ To Interview → Eligible For Interview → END
                                                                    ├─ To Recruiter → Evaluate By Recruiter → END
                                                                    └─ Rejected → Reject Candidate → END
```

## 📋 Prerequisites

- **Python 3.8+** (recommended 3.10+)
- **Ollama** installed and running locally
- **Sufficient RAM** for LLM operations (4GB+ recommended)
- **Git** for cloning the repository

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Recruitment Agency using LangGraph"
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and start Ollama**
   ```bash
   # Install Ollama (follow instructions at https://ollama.ai)
   # Start Ollama service
   ollama serve
   ```

4. **Download required models**
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

### Customizing Candidate Data

Modify the `data.py` file to provide different candidate information:

```python
def data_pdf():
    return "Your candidate details here"
```

### Understanding the Output

The system provides:
- **Experience Level**: Entry/Mid/Senior categorization
- **Skills Match**: Yes/No assessment for ML Engineer role
- **Final Outcome**: Interview selection, recruiter review, or rejection
- **Visual Workflow**: Graph representation of the decision process

## 🔧 Configuration

### LLM Models

The system uses different Ollama models for different tasks:

- **Experience Categorization**: `gemma3:12b`
- **Skills Evaluation**: `gemma3:12b`
- **Default Model**: `mistral`

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

## 🧪 Testing

### Sample Test Cases

1. **Senior Candidate with Skills**
   ```python
   candidate_details = "6 years ML experience, strong Python skills"
   # Expected: Interview
   ```

2. **Senior Candidate without Skills**
   ```python
   candidate_details = "7 years unrelated experience"
   # Expected: Recruiter Review
   ```

3. **Junior Candidate**
   ```python
   candidate_details = "1 year basic programming"
   # Expected: Rejection
   ```

## 🔍 Troubleshooting

### Common Issues

1. **"Invalid template" error**
   - Ensure proper template variable usage
   - Check ChatPromptTemplate syntax

2. **Ollama connection issues**
   - Verify Ollama is running: `ollama serve`
   - Check model availability: `ollama list`

3. **Import errors**
   - Install all requirements: `pip install -r requirements.txt`
   - Check Python version compatibility

4. **Graph visualization issues**
   - Ensure matplotlib is properly installed
   - Check for PNG generation errors

### Debug Mode

Enable debug output by modifying the evaluation functions to include more print statements.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangGraph** for the workflow orchestration framework
- **LangChain** for the LLM integration capabilities
- **Ollama** for providing local LLM capabilities
- **Matplotlib** for graph visualization

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the code documentation

---

**Built with ❤️ using LangGraph and AI-powered recruitment automation** 