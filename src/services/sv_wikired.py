import markovify
import json


class Wikired:
    def __init__(self):
        self.__ukranian_model = markovify.Text.from_json(self.__read_model('ukranian.json'))
        self.__wikired_model = markovify.Text.from_json(self.__read_model('wikired.json'))

    def __read_model(self, model_name: str):
        with open(model_name) as file:
            return json.loads(file.read())

    async def ukranian(self):
        try:
            return self.__ukranian_model.make_short_sentence(280)
        except Exception as e:
            print(e)

    async def wikired(self):
        try:
            return self.__wikired_model.make_short_sentence(280)
        except Exception as e:
            print(e)
        pass

    def __create_model(self):
        messages = []
        with open('ukranian.txt', 'r', encoding='utf-8') as file:
            for message in file:
                messages.append(message.replace('\n', ''))
        model = markovify.NewlineText(messages, state_size=3).compile()
        json_data = model.to_json()
        with open('../../ukranian.json', 'w') as export_file:
            export_file.write(json.dumps(json_data))

        print(model.make_short_sentence(280))

    def __parse_telegram_json(self):
        with open('ChatExport_2021-01-05/result.json', 'r', encoding='utf-8') as file:
            file_content = file.read()
            data = json.loads(file_content)
            with open('ukranian.txt', 'w', encoding='utf-8') as export_file:
                for message in data['messages']:
                    if message['text'] != '' and type(message['text']) != list:
                        print(message['text'])
                        export_file.write(message['text'] + "\n")
