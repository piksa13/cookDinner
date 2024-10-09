from single_question_chatbot import get_llm_response

my_food_preferences = {
        "dietary_restrictions": "no",
        "favorite_ingredients": ["sun dry tomatoes", "green olives"],
        "experience_level": "intermediate",
        "maximum_spice_level": 3
}

available_spices = ["cumin", "turmeric", "oregano", "paprika"]

prompt = f"""Please suggest a recipe that tries to include 
the following ingredients: 
{my_food_preferences["favorite_ingredients"]}.
The recipe should adhere to the following dietary restrictions:
{my_food_preferences["dietary_restrictions"]}.
The difficulty of the recipe should be: 
{my_food_preferences["experience_level"]}
The maximum spice level on a scale of 10 should be: 
{my_food_preferences["maximum_spice_level"]} 
Provide a two sentence description.
The recipe should include spices from below list:
{available_spices}.
"""
print(get_llm_response(prompt))
