from langchain_groq import ChatGroq
from service import get_species, get_pokemon
from langchain.chains import LLMChain,ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router import MultiPromptChain

llm = ChatGroq(api_key="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",model="meta-llama/llama-4-scout-17b-16e-instruct")

def pokemon_route(question):
    name = question.split()[-1].strip("?")
    data = get_pokemon(name)
    if "erro" in data:
        return data["erro"]
    return f"O Pokémon {data['nome']} tem {data['altura']} m de altura, pesa {data['peso']} kg e possui os tipos: {', '.join(data['tipos'])}."

def species_route(question):
    name = question.split()[-1].strip("?")
    data = get_species(name)
    if "erro" in data:
        return data["erro"]
    return f"A espécie de {data['nome']} é descrita assim: {data['descricao']}"

def fallback_route(question):
    return "Desculpe, não entendi sua pergunta. Pode reformular?"

class PromptFactory():
    # Exemplos de templates que definem os tipos de perguntas
    pokemon_template = """Você é um especialista em Pokémon. \
    Responda a perguntas sobre Pokémon, como suas características, tipos e evolução. \
    Pergunta: {input}"""

    species_template = """Você é um especialista em espécies de Pokémon. \
    Responda a perguntas sobre a descrição de espécies de Pokémon. \
    Pergunta: {input}"""

    prompt_infos = [
        {
            'name': 'pokemon',
            'description': 'Boa para perguntas sobre características de Pokémon',
            'prompt_template': pokemon_template
        },
        {
            'name': 'especie',
            'description': 'Boa para perguntas sobre a descrição de espécies de Pokémon',
            'prompt_template': species_template
        }
    ]

def generate_destination_chains():
    """
    Cria a lista de chains com diferentes templates.
    """
    prompt_factory = PromptFactory()
    destination_chains = {}
    for p_info in prompt_factory.prompt_infos:
        name = p_info['name']
        prompt_template = p_info['prompt_template']
        chain = LLMChain(
            llm=llm, 
            prompt=PromptTemplate(template=prompt_template, input_variables=['input']))
        destination_chains[name] = chain
    default_chain = ConversationChain(llm=llm, output_key="text")
    return prompt_factory.prompt_infos, destination_chains, default_chain

def generate_router_chain(prompt_infos, destination_chains, default_chain):
    """
    Cria o RouterChain usando as informações dos prompts.
    """
    destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
    destinations_str = '\n'.join(destinations)
    router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
    router_prompt = PromptTemplate(
        template=router_template,
        input_variables=['input'],
        output_parser=RouterOutputParser()
    )
    router_chain = LLMRouterChain.from_llm(llm, router_prompt)
    return MultiPromptChain(
        router_chain=router_chain,
        destination_chains=destination_chains,
        default_chain=default_chain,
        verbose=True
    )