
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from typing import TypedDict


class RecruiterAgent(TypedDict):
    candidate_details: str
    level_experience: str
    match: str
    resume: str
    outcome: str

def GetLLM(model = "mistral"):
    return OllamaLLM(model=model)

def CategorizeCandidateExperience(graph: RecruiterAgent) -> RecruiterAgent:
    """
    Categorize a candidate's experience level based on their provided details.
    
    This function uses an LLM to analyze candidate information and categorize them
    into one of three experience levels: Entry Level, Mid Level, or Senior.
    
    Args:
        graph (RecruiterAgent): A dictionary containing candidate information with key:
            - 'candidate_details': String describing the candidate's background and experience
            
    Returns:
        RecruiterAgent: Updated state with new key:
            - 'level_experience': The categorized experience level (Entry/Mid/Senior)
            
    Experience Level Criteria:
        - Entry Level: 0-2 years of experience
        - Mid Level: 2-5 years of experience  
        - Senior: 5+ years of experience
        
    """


    print("Categorize the candidate: ")
    prompt = ChatPromptTemplate.from_template(
        """
        Suppose you are an expert recruiter. You are given details of the candidate need to categorize the candidate as 
        Entry Level, Mid Level and Senior. 
        Entry Level: 0-2 years of experience
        Mid Level: 2-5 years of experience
        Senior: 5+ years of experience
        Candidate Details: {candidate_details}
        Your answer will be strictly Entry, Intermediate or Senior without any other text or punctuation.
        """
        )
    llm = GetLLM("gemma3:12b")
    chain = prompt | llm
    #print(state["candidate_details"])
    experience = chain.invoke({"candidate_details": graph["candidate_details"]})
    #print(f"Experience: {experience}")

    return {"level_experience": experience}

def EvaluateCandidateSkills(graph: RecruiterAgent) -> RecruiterAgent:
    """
    Evaluate whether a candidate's skills match the requirements for a Machine Learning Engineer position.
    
    This function assesses the candidate's suitability based on their provided details
    and returns a binary yes/no decision regarding their fit for the ML Engineer role.
    
    Args:
        graph (RecruiterAgent): A dictionary containing candidate information with keys:
            - 'candidate_details': String describing the candidate's background and experience
            
    Returns:
        RecruiterAgent: Updated state with new key:
            - 'match': Binary assessment result ("yes" or "no")

    """


    print("Evaluating experience...")
    prompt = ChatPromptTemplate.from_template(
        """
        Based on the experience of the candidate, evaluate whether the candidate is suitable for the position of Machine Learning Engineer.
        Your answer will be strictly yes or no without any other text or punctuation.
        Candidate Details: {candidate_details}
        """
        )
    llm = GetLLM("gemma3:12b")
    chain = prompt | llm
    match = chain.invoke({"candidate_details": graph["candidate_details"]})
    #print(f"Match: {match}")
    return {"match": match}

def EligibleForInterview(graph: RecruiterAgent) -> RecruiterAgent:
    """
    Mark a candidate as eligible for an interview.
    
    This function is called when a candidate meets all the criteria for the position
    and should proceed to the interview stage.
    
    Args:
        graph (RecruiterAgent): The current candidate evaluation state.
            
    Returns:
        RecruiterAgent: Updated state with new key:
            - 'outcome': Status indicating the candidate is selected for interview

    """


    print("The Candidate is selected for the interview...")
    return {"outcome": "Selected for Interview"}
    #return {"response": "The candidate is good and selected for the interview"}

def EvaluateByRecruiter(graph: RecruiterAgent) -> RecruiterAgent:
    """
    Route a candidate to a recruiter for further evaluation.
    
    This function is called when a candidate has senior-level experience but
    their skills assessment indicates they may need additional review by a human recruiter.
    
    Args:
        graph (RecruiterAgent): The current candidate evaluation state with keys:
            - 'level_experience': The categorized experience level
            
    Returns:
        RecruiterAgent: Updated state with new key:
            - 'outcome': Explanation of why further evaluation is needed

    """


    print("Moved to recruiter for further evaluation...")
    return {"outcome": "The candidate requires further evaluation as its category is " + graph["level_experience"] + " but seems they lack the skills for the role"}
    #return {"response": "The candidate requires further evaluation as its category is " + graph["level_experience"] + " but seems they lack the skills for the role"}

def RejectCandidate(graph: RecruiterAgent) -> RecruiterAgent:
    """
    Reject a candidate who does not meet the minimum requirements.
    
    This function is called when a candidate's experience level and skills assessment
    indicate they are not suitable for the position.
    
    Args:
        graph (RecruiterAgent): The current candidate evaluation state.
            
    Returns:
        RecruiterAgent: Updated state with new key:
            - 'outcome': Explanation of why the candidate was rejected
    """


    print("The candidate skills and experience does not meet the criteria. So the candidate is rejected.")
    return {"outcome": "Rejected because candidate does not meet the minimum requirements of the job description"}
    #return {"response": "The candidate does not meet the minimum requirements of the job description"}

def conditional_edges(graph: RecruiterAgent) -> str:
    """
    Determine the next step in the evaluation workflow based on candidate assessment.
    
    This function implements the decision logic for routing candidates through
    the evaluation process based on their experience level and skills match.
    
    Args:
        graph (RecruiterAgent): The current candidate evaluation state with keys:
            - 'match': Skills assessment result ("yes" or "no")
            - 'level_experience': Categorized experience level
            
    Returns:
        str: The next destination in the workflow:
            - "To Interview": Candidate meets all criteria
            - "To Recruiter": Senior candidate needs human review
            - "Rejected": Candidate does not meet requirements
            
    Routing Logic:
        - Senior + Skills Match: → Interview
        - Senior + No Skills Match: → Recruiter Review
        - Other combinations: → Rejected
    """

    if "yes" in graph["match"].lower() and "senior" in graph["level_experience"].lower():
        return "To Interview"
    elif "no" in graph["match"].lower() and "senior" in graph["level_experience"].lower():
        return "To Recruiter"
    else:
        return "Rejected"

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