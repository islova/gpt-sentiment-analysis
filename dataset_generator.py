import json
import openai
import os
import time
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('API_KEY')

os.mkdir('data/')


def get_completion(prompt, model="gpt-3.5-turbo", logit_bias=None):
	messages = [{"role": "user", "content": prompt}]
	response = openai.ChatCompletion.create(
		model=model,
		messages=messages,
		temperature=0.7,
		n=128
	)
	return [x.message["content"] for x in response.choices]


sentiments = ["miedo", "alegria", "amor", "enojo", "tristeza", "sorpresa"]

sleep_time = 20

for sentiment in sentiments:
	prompt_generate_single = f'''
	Con base en el siguiente sentimiento ```{sentiment}```,
	genere un párrafo de máximo 50 palabras, donde se exprese solo uno de los sentimientos.
	El texto no debe de contener la palabra ```{sentiment}```.
	El texto no debe de expresar el sentimiento explícitamente.
	Evite ser altamente descriptivo.
	Como salida, asegúrese de retornar un string en formato JSON, donde su llave sea "text"
	y el valor de esta sea el texto generado. No utilice saltos de línea en la salida.
	'''

	response = get_completion(prompt_generate_single)

	file = open(f'./data/{sentiment}.json', mode='w', encoding='utf-8')
	file.write('{\n\t"' + sentiment +'": [\n')
	for choice in response:
		file.write(f'\t\t{choice},\n')
	file.write('\t]\n}')
	file.close()

	print(f'Done with "{sentiment}". Sleeping {sleep_time} seconds...')
	time.sleep(sleep_time)
	print('Continuing...')
