def arabicTOroman(num):
    arabic = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    
    result = ""
    
    if num < 5000 and num > 0 and isinstance(num,int):
        for i in range(len(arabic)-1,-1,-1):
            while(num >= arabic[i]):
                result += roman[i]
                num -= arabic[i]
    else:
        return "Wrong Input"
            
    return result
