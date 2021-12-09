from duclosure import pipeline


def soma_um(param):
    return param + 1


def tira_dez(param):
    return param - 10


payload = 100

pipe = pipeline(soma_um, tira_dez)
res = pipe(payload)

print(res)
