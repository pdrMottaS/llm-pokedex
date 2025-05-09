from langchain.agents import initialize_agent, AgentType
from tool import pokemons_tool,types_tool
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatGroq(api_key="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",model="meta-llama/llama-4-scout-17b-16e-instruct")

translation_prompt = PromptTemplate(
    input_variables=["input_text"],
    template="Translate the following text to English:\n\n{input_text}"
)

translation_chain = LLMChain(llm=llm, prompt=translation_prompt)

agent = initialize_agent(
    llm=llm,
    tools=[pokemons_tool,types_tool],
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True,
    agent_kwargs={
        "prefix": (
            "You are a Pokémon expert assistant. Use only the tools provided." 
            "Case the subject is not about pokemon, show a message that question is not about pokemon"
            "Verify and fix pokemon name when it is written wrong"
            "Give short and accurate answers in English."
        )
    }

)

def run_agent_with_translation(user_input):
    translated_input = translation_chain.run(user_input)
    return agent.run(translated_input)