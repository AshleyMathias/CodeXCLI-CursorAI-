from typing_extensions import TypedDict
from openai import OpenAI
from typing import Literal
from langgraph.graph import StateGraph,START,END
from pydantic import BaseModel
import os
import json

client=OpenAI(api_key="api_key")
"""
1. we will classify if the messaeg is coding question or a generic one.
2. we will define  a route query to see which one node to choose the genric one or coding one.
3. if it  is a coding query got ot codingnode and perform the task.
4. if it is a generic one so tell ask my parent node ChatGPT not me i am just a baby.
5. if it is coding node so after genearting repsne check it again and vaidate it if its not the same or expeted so t=sen it back to the llm 
    if the validation goes correct send it to the user
"""

class ClassifyMessageResponse(BaseModel):
    is_coding_question:bool

class CodeAccuracyPercentage(BaseModel):
    accuracy_percentage:str


class State(TypedDict):
    user_prompt:str
    llm_response:None
    accuracy_percentage:str|None
    is_coding_question:bool|None
    command:str



#Take user query:
def ClassifyMessage(state:State):
    query = state['user_prompt']
    SYSTEM_PROMPT = f"""
    You are an expert AI assistant.Your job is to detect if the user's prompt is related to
    coding question or not.
    Return the response in specified JSOn boolean only.

    """
    response =client.beta.chat.completions.parse(
        model="gpt-4.1-nano",
        response_format=ClassifyMessageResponse,
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":query}
        ]
    )
    is_coding_question =response.choices[0].message.parsed.is_coding_question
    state['is_coding_question']=is_coding_question
    return state

#defining the route query after the classification
def route_query(state:State)-> Literal["general_query","coding_query"]:
    is_coding = state["is_coding_question"]
    if is_coding:
        return "coding_query"
    return "general_query"

#getting the general_query function.
def general_query(state:State):
    query=state['user_prompt']
    SYSTEM_PROMPT="""
    You are an expert AI assistant. Your job is to roast the user, using dad jokes on any query the user asks.
    You have to not answer his question or solve the user query.
    example: 
    user:How to get into google without DSA?
    assistant: Well yes obviously you can get in Google without DSA in google just a step in the google with your legs, hahahahaha!.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":query}
        ]
    )
    state["llm_response"]=response.choices[0].message.content
    return state

def coding_query(state: State):
    prompt = state['user_prompt']

    def cmd_controller(command: str) -> str:
        try:
            print(f"Executing: {command}")
            os.system(command)
            return f"Command '{command}' executed successfully."
        except Exception as e:
            return f"Error executing command: {str(e)}"

    available_tools = {
        "cmd_controller": cmd_controller
    }

    SYSTEM_PROMPT = """
        You are a helpful AI Assistant specialized in solving user queries.
        You work on start, plan, action, observe mode.

        Instructions:
        - Always follow the Output JSON Format.
        - Always perform one step at a time and wait for the next input.

        Output JSON Format:
        {
            "step":"string",
            "content":"string",
            "function":"The name of the function of the step is action",
            "input":"The input parameter for the function"
        }

        Available tools:
        - "cmd_controller": takes a Linux command string and executes it.

        Example:
        User: Create a folder named test
        Output: {"step":"plan","content":"The user wants to create a folder"}
        Output: {"step":"action","function":"cmd_controller","input":"mkdir test"}
        Output: {"step":"observe","output":"Folder created"}
        Output: {"step":"output","content":"Folder 'test' was successfully created"}
    """

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.append({"role": "user", "content": prompt})

    output_text = "No valid output generated."  # <-- Default fallback

    while True:
        response = client.chat.completions.create(
            model="gpt-4.1",
            response_format={"type": "json_object"},
            messages=messages
        )

        assistant_msg = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_msg})
        parsed_response = json.loads(assistant_msg)

        step = parsed_response.get("step")

        if step == "plan":
            print(parsed_response.get("content"))
            continue

        if step == "action":
            tool_name = parsed_response.get("function")
            tool_input = parsed_response.get("input")

            print(f"Calling tool: {tool_name}")
            if available_tools.get(tool_name):
                tool_output = available_tools[tool_name](tool_input)
                messages.append({
                    "role": "user",
                    "content": json.dumps({"step": "observe", "output": tool_output})
                })
                continue

        if step == "output":
            output_text = parsed_response.get("content")
            print(output_text)
            break

    state["llm_response"] = output_text
    return state


def coding_validate_query(state:State):
    query=state['user_prompt']
    llm_code=state['llm_response']
    SYSTEM_PROMPT = f"""
        You are expert in calculating accuracy of the code according to the question.
        Return the percentage of accuracy
        User Query:{query}
        Code:{llm_code}
        """
    response = client.beta.chat.completions.parse(
        model="gpt-4.1-mini",
        response_format=CodeAccuracyPercentage,
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":query}
        ]
    )
    state["accuracy_percentage"]=response.choices[0].message.parsed.accuracy_percentage
    return state
    

graph_builder = StateGraph(State)

#building the nodes
graph_builder.add_node("classify_message",ClassifyMessage)
graph_builder.add_node("route_query",route_query)
graph_builder.add_node("general_query",general_query)
graph_builder.add_node("coding_query",coding_query)
graph_builder.add_node("coding_validate_query",coding_validate_query)

#joining the edges of the nodes to start 
graph_builder.add_edge(START,"classify_message")
graph_builder.add_conditional_edges("classify_message",route_query,
                                    {
                                        "coding_query":"coding_query",
                                        "general_query":"general_query"
                                    })
graph_builder.add_edge("general_query",END)
graph_builder.add_edge("coding_query","coding_validate_query")


graph = graph_builder.compile()

def main():
    print("Welcome to your AI assistant! Type 'bye' to exit.")
    while True:
        user = input("-> ")

        if user.lower() in ["bye", "exit", "quit"]:
            print("Goodbye! 👋")
            break

        _state: State = {
            "user_prompt": user,
            "accuracy_percentage": None,
            "is_coding_question": None,
            "llm_response": None,
            "command": None
        }

        try:
            response = graph.invoke(_state)
            print(f"\n Response:\n{response['llm_response']}")
            if response.get("accuracy_percentage"):
                print(f" Accuracy: {response['accuracy_percentage']}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
main()
    







