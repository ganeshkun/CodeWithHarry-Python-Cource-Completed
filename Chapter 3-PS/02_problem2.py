letter =  '''
         Dear <|Name|>,
         You are selected!
         <|Date|>
'''

print(letter.replace("<|Name|>", "John").replace("<|Date|>", "2026-07-28"))