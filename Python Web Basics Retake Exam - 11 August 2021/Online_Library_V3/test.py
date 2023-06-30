type = '1234567891011121314151617'
print(f'{type if len(type) < 18 else type[:18] + "..."}')
