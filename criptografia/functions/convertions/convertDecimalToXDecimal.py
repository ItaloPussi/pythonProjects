def convertDecimalToXDecimal(x, value):
        valores = []
        base = x
        while value>=base:
            valores.append(value % base)
            value = value // base
        valores.append(value)

        return valores