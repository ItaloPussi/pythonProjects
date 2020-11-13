def convertXDecimalToDecimal(x, valuesArray):
        final = 0
        base = x

        # Make the conversion based on hexdecimal -> decimal
        for index, valor in enumerate(valuesArray):
            final +=(base ** index) * int(valor)
        return final    