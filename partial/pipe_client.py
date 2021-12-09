from pipeline import Pipeline, soma_um, tira_dez

payload = 100

pipeline = Pipeline(soma_um, tira_dez)

response = pipeline(payload)

print(response)
