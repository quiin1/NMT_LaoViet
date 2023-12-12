vietlao
    # not preprocess

vietlao2
    # Lower case 
    # Remove punctuation 
    # Remove numbers 
    # Remove special characters (need check)
    # Remove whitespace

vietlao3 (preprocess same vietlao2 + remove )
    # Lower case 
    # Remove punctuation 
    # Remove numbers 
    # Remove special characters (need check)
    # Remove whitespace

    # Remove stopwords both (need check)

vietlao4 = vietlao + bible (preprocess same vietlao2)
    # Lower case 
    # Remove punctuation 
    # Remove numbers 
    # Remove special characters (need check)
    # Remove whitespace

Kq chạy KC (BLEU)
    vietlao1    6.99
    vietlao2    17.56
    vietlao3    5.
    vietlao4 lỗi input max length
Kq chạy finetune
    mt5         

