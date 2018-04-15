import requests
import time

# Change here for the initial CEP
initial_cep = 69000000

# Change here for the final CEP
final_cep = 69899999

base_url = "http://api.postmon.com.br/v1/cep/%s"


def to_csv(json):
    cep = json["cep"]
    estado = json["estado"]
    cidade = json["cidade"]
    bairro = json["bairro"]
    logradouro = json["logradouro"]
    return "%s;%s;%s;%s;%s" % (cep, estado, cidade, bairro, logradouro)


print("CEP range %s - %s" % (initial_cep, final_cep))

for cep in range(initial_cep, final_cep):
    r = requests.get(base_url % (cep))
    if (r is not None) and (r.status_code == 200):
        json = r.json()
        print(to_csv(json))
        time.sleep(2)
