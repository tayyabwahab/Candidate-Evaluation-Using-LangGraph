from langgraph.graph import StateGraph, START, END
from langchain_core.prompts import ChatPromptTemplate
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io
from evaluation import *
from data import data_pdf

def add_nodes(graph: RecruiterAgent) -> RecruiterAgent:
    """
    Add all evaluation nodes to the recruitment workflow graph.
    
    This function configures the StateGraph with all the necessary nodes for the
    candidate evaluation process, including experience categorization, skills evaluation,
    and decision-making nodes.
    
    Args:
        graph (RecruiterAgent): The StateGraph instance to add nodes to.
        
    Returns:
        RecruiterAgent: The updated graph with all nodes added.
        
    """
    
    graph.add_node("Categorize Candidate Experience", CategorizeCandidateExperience)
    graph.add_node("Evaluate Candidate Skills", EvaluateCandidateSkills)
    graph.add_node("Evaluate By Recruiter", EvaluateByRecruiter)
    graph.add_node("Eligible For Interview", EligibleForInterview)
    graph.add_node("Reject Candidate", RejectCandidate)
    return graph

def add_edges(graph: RecruiterAgent) -> RecruiterAgent:
    """
    Configure the workflow edges and conditional routing in the recruitment graph.
    
    This function sets up the flow between different evaluation stages, including
    conditional routing based on candidate experience and skills assessment.
    
    Args:
        graph (RecruiterAgent): The StateGraph instance to add edges to.
        
    Returns:
        RecruiterAgent: The updated graph with all edges and conditional routing configured.
        
    Workflow:
        1. START → Categorize Candidate Experience
        2. Categorize Candidate Experience → Evaluate Candidate Skills
        3. Evaluate Candidate Skills → [Conditional Routing]:
           - To Interview → Eligible For Interview → END
           - To Recruiter → Evaluate By Recruiter → END
           - Rejected → Reject Candidate → END
    """
    
    graph.add_edge(START, "Categorize Candidate Experience")
    graph.add_edge("Categorize Candidate Experience", "Evaluate Candidate Skills")
    
    graph.add_conditional_edges(
        "Evaluate Candidate Skills",
        conditional_edges,
        {
            "To Interview": "Eligible For Interview",
            "To Recruiter": "Evaluate By Recruiter", 
            "Rejected": "Reject Candidate"
        }
    )
    
    # Add edges from conditional destinations to END
    graph.add_edge("Evaluate By Recruiter", END)
    graph.add_edge("Eligible For Interview", END)
    graph.add_edge("Reject Candidate", END)
    return graph

def visualize_graph(graph) -> None:
    """
    Generate and display a visual representation of the recruitment workflow graph.
    
    This function creates a matplotlib visualization of the graph structure,
    showing the flow between different evaluation stages and decision points.
    
    Args:
        graph: The compiled StateGraph instance to visualize.
        
    Returns:
        None: Displays the graph visualization in a matplotlib window.
        
    Raises:
        Exception: If the graph visualization fails, prints an error message.
        
    """
    try:
        # Get the PNG data from the graph
        png_data = graph.get_graph().draw_mermaid_png()
        
        # Create a figure with proper size
        plt.figure(figsize=(14, 10))
        
        # Convert PNG data to image array
        img = mpimg.imread(io.BytesIO(png_data))
        
        # Display the image
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.title('Candidate Evaluation Flow', fontsize=16, pad=20)
        
        # Adjust layout and display
        plt.tight_layout()
        plt.show()
        
        #print("Graph displayed using matplotlib!")
            
    except:
        print("The graph is not created properly")

def display_Summary(summary) -> None:   
    """
    Display a formatted summary of the candidate evaluation results.
    
    This function prints a comprehensive summary of the candidate's evaluation,
    including their experience level, skills match assessment, and final outcome.
    
    Args:
        summary (dict): A dictionary containing the evaluation results with keys:
            - 'match': The skills match assessment (yes/no)
            - 'level_experience': The categorized experience level
            - 'outcome': The final decision or status
            
    Returns:
        None: Prints the summary to the console.
        
    """

    print("\n******* Application Summary**********")
    print(f"Skills Match: {summary['match']}")
    print(f"Experience: {summary['level_experience']}")
    print(f"Outcome: {summary['outcome']}")

def get_details(detail):
    """
    Extract and summarize candidate details using LLM.
    
    This function processes candidate information and creates a summarized
    version that can be used for evaluation purposes.
    
    Args:
        detail (dict): Dictionary containing candidate details with key 'candidate_details'
        
    Returns:
        str: Summarized candidate information
    """
    prompt = ChatPromptTemplate.from_template(
        """
        For the provided details of the candidate, extract the important information that can be used for the evaluation. After extracting all the details, 
        make a summarized paragraph that contains all the details of the candidate regarding its experience, skills and background that can be used later for evaluation of the job.
        
        Candidate Details: {detail}
        """
    )
    
    llm = GetLLM("gemma3:12b")
    chain = prompt | llm
    
    # Invoke the chain with the detail variable
    summary = chain.invoke({"detail": detail["candidate_details"]})
    return summary

if __name__ == "__main__":
    """
    Main execution block for the Recruitment Agency workflow.
    
    This section:
    1. Creates a new StateGraph for candidate evaluation
    2. Configures all nodes and edges
    3. Compiles the graph for execution
    4. Visualizes the workflow structure
    5. Tests the system with sample candidate data
    6. Displays the evaluation results
    
    The workflow evaluates candidates based on:
    - Experience level categorization (Entry/Mid/Senior)
    - Skills assessment for ML Engineer position
    - Conditional routing based on qualifications
    """

    graph = StateGraph(RecruiterAgent)
    graph = add_nodes(graph)
    graph = add_edges(graph)
    evaluate_candidate = graph.compile()
    visualize_graph(evaluate_candidate)
    
    # Test the graph with sample data
    print("\n" + "="*50)
    print("Testing the graph with sample data:")
    print("="*50)

    candidate_details = {"candidate_details": data_pdf()}
    get_details(candidate_details)
    
    #candidate_details = {"candidate_details": "3 years of experience in machine learning and 6 years of experience in deep learning",}
    result = evaluate_candidate.invoke(candidate_details)
    display_Summary(result)
        



