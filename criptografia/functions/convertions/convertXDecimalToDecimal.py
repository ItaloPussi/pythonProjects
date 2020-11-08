def convertXDecimalToDecimal(x, valueArray):
        final = 0
        base = x

        for index, valor in enumerate(valueArray):
            final +=(base ** index) * int(valor)
        return final