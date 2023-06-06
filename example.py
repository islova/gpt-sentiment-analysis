import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
	messages = [{"role": "user", "content": prompt}]
	response = openai.ChatCompletion.create(
		model=model,
		messages=messages,
		temperature=0.8
	)
	return response.choices[0].message["content"]


sentiments = ["miedo", "alegria", "amor", "enojo", "tristeza"]

sample_text_happiness = '''
	Mi mejor amigo es una persona muy amable y alegre, 
	e igualmente es una persona muy inteligente que busca 
	superarse a si misma razón por la cual quiere estudiar 
	para ser doctor un día y ayudar a la gente que necesite 
	ayuda, soy muy afortunada de tener un tan buen amigo.
'''

sample_text_nostalgia = '''
	Cuando miro al cielo , buscando luz,
	A veces me pierdo , me sumerjo en él,
	Y cuando presiento, que no se que hacer ,
	Busco la paz, me enfoco, surjes tú;

	Entre nubes, estrellas, o el cielo azul,
	Isofacto a mi mente llega el poder,
	Para lograr imaginar, recorrer,
	Mares de placer, sacados de un baúl .

	Nutriendo así, un alma que fugaz se ahoga,
	Cuando anhela y no tiene, cuando sufre,
	Ante la ausencia de esa suave droga,

	Que cuando la fumo, en mi ser produce,
	Latires por mil que firmes derogan,
	Aquello que la distancia introduce.
'''

prompt_classify = f'''
	Con base en los sentimientos dentro de la siguiente lista ```{sentiments}```, 
	genere un string de formato JSON, donde contenga los elementos de la lista
	como llaves y el valor como un booleano dependiendo de si el siguiente texto
	contiene el sentimiento ```{sample_text_nostalgia}```
'''

prompt_generate_single = f'''
	Con base en los sentimientos dentro de la siguiente lista ```{sentiments}```,
	genere un párrafo de máximo 100 palabras, donde se exprese solo uno de los sentimientos.
	Asegurese que el sentimiento elegido no sea mencionado explicitamente.
	Como salida, retorne un string en formato JSON, donde las llaves sean "text" y "sentiment"
	y los valores sean el texto generado y el sentimiento expresado en este.
'''

prompt_generate_multiple = f'''
	Con base en los sentimientos dentro de la siguiente lista ```{sentiments}```,
	genere un párrafo de máximo 100 palabras, donde se expresen dos de los sentimientos.
	Como salida, retorne únicamente un string en formato JSON, donde las llaves sean "text", "sentiment_1" 
	y "sentiment_2" y los valores sean el texto generado y el sentimientos expresado en este.
	Asegurese que el sentimiento elegido no sea mencionado explicitamente.
'''

prompt_1 = '''
	Genere una lista de al menos 20 emociones de segundo nivel relacionadas a la emoción "alegría". La lista
	debe de tener el siguiente formato:
	```
	1. Amor
	2. Alegria
	3. Tristeza
	```
'''

prompt_2 = '''
	Genere una lista de al menos 20 emociones de segundo nivel relacionadas a la emoción "amor". La lista
	debe de tener el siguiente formato:
	```
	1. Amor
	2. Alegria
	3. Tristeza
	```
'''

prompt_3 ='''
	Genere una de emociones de relacionadas a la "euforia".
	Explique por qué estas emociones se relacionan a la euforia.
	Retorne un string en formato JSON donde las llaves sean "sentiments" y "reasoning", donde
	el valor de "sentiments" sea la lista de emociones y "reasoning" sea la explicación realizada.
'''

response = get_completion(prompt_3)
print(response)
