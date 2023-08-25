byte_value = b'r\xc3\xa9sum\xc3\xa9'
print("Исходное байтовое значение:", byte_value)

decoded_string = byte_value.decode('utf-8')
print("Декодированная строка:", decoded_string)

latin1_encoded = decoded_string.encode('latin1')
print("Байтовый вид в кодировке 'Latin1':", latin1_encoded)

decoded_latin1 = latin1_encoded.decode('latin1')
print("Декодированная строка из 'Latin1':", decoded_latin1)
