def convertDecimalToXDecimal(x, value):
        values = []
        base = x
        while value>=base:
            values.append(value % base)

            # Get integer of division
            value = value // base
        values.append(value)

        return values