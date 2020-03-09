import requests
import json
from hashlib import sha1


class CryptographyJulioCesar:

    def __init__(self):
        self.token = 'token=enter_token'
        self.url = f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data? \
                    {self.token}'
        self.post = f'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution? \
                    {self.token}'
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.number_solution = 7

    def get_url(self):
        page_url = requests.get(self.url)
        encrypted_text = page_url.text[80:147].lower()
        self.create_file_json(page_url)
        self.descrypt(encrypted_text)

    def create_file_json(self, url):
        with open('answer.json', 'w') as create_file:
            json.dump(url.json(), create_file)

    def update_file_json(self, update_json_args, update_json_key):
        with open('answer.json', 'r+', encoding='utf-8') as read_json:
            context_file = read_json.read()
            context_json = json.loads(context_file)
            context_json.update({update_json_args: update_json_key})
            overwrite_content = json.dumps(context_json)
            read_json.seek(0)
            read_json.write(overwrite_content)

    def descrypt(self, encrypted_text):
        context = ''
        for text in encrypted_text:
            if text in self.alphabet:
                c = self.alphabet.index(text)
                context += self.alphabet[(c - self.number_solution)]
            else:
                context += text

        self.encrypt_sha1(context)
        self.update_file_json('decifrado', context)

    def encrypt_sha1(self, result):
        hash_sha1 = sha1(result.encode('utf-8'))
        encrypt = hash_sha1.hexdigest()
        self.update_file_json('resumo_criptografico', encrypt)

    def post_api(self):
        files = {'answer': open('answer.json', 'rb')}
        response = requests.post(self.post, files=files)
        print(response)


if __name__ == "__main__":
    run = CryptographyJulioCesar()
    run.get_url()
    run.post_api()
