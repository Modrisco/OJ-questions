one_to_nine_digits =['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
ten_to_twenty_digits =['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
twenty_to_hundred_digits = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
def digit_to_letter(n):
    letter = ''
    if n == 0:
        return one_to_nine_digits[0]
    while n > 0:
        if n > 0 and n < 10:
            letter += one_to_nine_digits[n]
            n -= n
        if n >= 10 and n < 20:
            letter += ten_to_twenty_digits[n - 10]
            n -= n
        if n >= 20 and n < 100:
            a = n // 10
            letter += twenty_to_hundred_digits[a-2]
            n -= a * 10
        if n >= 100 and n < 1000:
            a = n // 100
            if n % 100 == 0:
                letter += one_to_nine_digits[a] + 'Hundred'
            else:
                letter += one_to_nine_digits[a] + 'HundredAnd'
            n -= a * 100
        if n >= 1000 and n < 1000000:
            a = n // 1000
            letter += digit_to_letter(a) + 'Thousand'
            n -= a * 1000
        if n >= 1000000 and n < 1000000000:
            a = n // 1000000
            letter += digit_to_letter(a) + 'Million'
            n -= a * 1000000
        if n >= 1000000000 and n < 1000000000000:
            a = n // 1000000000
            letter += digit_to_letter(a) + 'Billion'
            n -= a * 1000000000
        if n == 1000000000000:
            letter = 'OneTrillion'
            n -= 1000000000000
    return letter
    
total_length = 0
for i in range(1, 1001):
    total_length += len(digit_to_letter(i))
print(total_length)
