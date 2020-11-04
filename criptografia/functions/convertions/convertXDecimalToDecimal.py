def convertXDecimalToDecimal(x, valueArray):
        final = 0
        base = x

        for index, valor in enumerate(valueArray):
            final +=pow(base, index) * int(valor)
        return final