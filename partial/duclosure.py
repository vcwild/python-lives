def pipeline(*funcs):
    def inner(data, funcs=funcs):
        result = data

        for f in funcs:
            result = f(result)

        return result

    return inner
