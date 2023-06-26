import json
import openai
import os
import time
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo", logit_bias=None):
	messages = [{"role": "user", "content": prompt}]
	response = openai.ChatCompletion.create(
		model=model,
		messages=messages,
		temperature=0.7,
		n=128
	)
	return [x.message["content"] for x in response.choices]


sentiments = ["miedo", "alegria", "amor", "enojo", "tristeza"]

json_string_template = '''
{
	"text": "X",
	"sentiment": "Y"
}
'''

sleep_time = 20

for sentiment in sentiments:
	prompt_generate_single = f'''
	Con base en el siguiente sentimiento ```{sentiment}```,
	genere un párrafo de máximo 50 palabras, donde se exprese solo uno de los sentimientos.
	El texto no debe de contener la palabra ```{sentiment}```.
	El texto no debe de expresar el sentimiento explícitamente.
	Evite ser altamente descriptivo.
	Como salida, retorne un string en formato JSON que se vea de la siguiente manera 
	```{json_string_template}```, donde se reemplaze ```X``` por el texto generado y
	```Y``` por el sentimiento brindado previamente.
	'''

	response = get_completion(prompt_generate_single)

	file = open(f'{sentiment}.json', 'w')
	file.write('{\n\t"data": [\n')
	for choice in response:
		lines = choice.split('\n')
		file.write(f'\t\t{lines[0]}\n')
		file.write(f'\t\t{lines[1]}\n')
		file.write(f'\t\t{lines[2]}\n')
		file.write(f'\t\t{lines[3]},\n')
	file.write('\t]\n}')
	file.close()

	print(f'Done with "{sentiment}". Sleeping {sleep_time} seconds...')
	time.sleep(sleep_time)
	print('Continuing...')
