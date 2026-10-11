from task1 import decrypt_text
from task2 import vigenere
from task3 import find_key_vigenere
from task4 import otp

if __name__ == '__main__':

    # task 1
    print("Task 1")
    encrypted_text = ("Єщеу х ещєщ зщхєбожцж б хбиєбожцж джмеуєу, тґ Ґуизж Дщїснаг, лжн хбє б ежджшаг. "
                      "Зжіадус гжцж, їж хіщ жшєж, пж г іуе вшй, — жшґуяух жїуеує")
    k = 23

    result = decrypt_text(encrypted_text, k)

    print(result)
    print(result == "Нема в мене певнішого і вірнішого лоцмана, як Карпо Летючий, хоч він і молодий. "
                    "Посилаю його, то все одно, що й сам їду, — одказав отаман")
    
    # task 2
    print("Task 2")
    task2_encrypted = "Вцмвриґсб клйд, у сиьб ґатсчстизшюх вьізтинщзтеш ізимсажичясй крхьиоаькериґчяв є яіторач уиплмвовхг тіт, іщ де мцяиятї тдфовчсціч ьжо вьізнищі, иомд йян нс чеже гціжиґс ьасаїем адачнтхвякажта. Ця ніца сґіга пвслиназ єоянс яєрлюйічяща сигачми гнжтиетваццу уідщюютиє хгючцй."
    task2_key = "аліса"
    
    task2_result = vigenere(task2_encrypted, task2_key, True)
    
    print(task2_result)
    print(task2_result == "Відкритий ключ, в силу математичних властивостей асиметричних криптоалгоритмів є набором випадкових біт, що не містять інформації про власника, тому він не може служити засобом аутентифікації. Ця вада стала причиною появи ієрархічної системи сертифікації відкритих ключів.")
    
    # task3
    print("Task 3")
    task3_encrypted = "Єхєйеґ дєг нєедквдгп ієшю живґщ щобівррнр Пхщ Фсвюд 1984 меаи. Рєд дєшлієзшю, нґ пяью ш'прегпжн їечвшюяєзл ююаддезждрпупзш шв сюуижщзшз вбої єґ'о рпк єґлєкуз румчєи Оіяєь, єк кх егдтптшіе р жяісфґж лжґйфбіеи оюихґєеїьботяю сжбо-обгяе єцвні. Фдряюя кон яфцн Фсвюдщ ьпвшфсбреш гщлф ижпжшюен бдеєждсмсиюїйен угіесдакґадм, щгх т 2000 дккь, щоюцобш кцгюю юяфдбєб сєодгщтгниь т фіядзшудьа ямюдзгяжпіщж, яфцм юцпвгнр сзщіюжь р ґюжзн."
    task3_hint = "Першим про спрощення"
    
    task3_key = find_key_vigenere(task3_encrypted, task3_hint)
    
    print(task3_key)
    task3_result = vigenere(task3_encrypted, task3_key, True)
    
    print(task3_result)
    
    # task4
    print("Task 4")
    task4_encrypted = "6229382959335367381141471137"
    task4_key = "ода"
    
    task4_result = otp(task4_encrypted, task4_key, True)
    print(task4_result)
    
    # task5
    print("Task 5")
    task5_decrypted = "Ознайомити студентів з підстановочними шифрами відпрацювати навички в"
    task5_key = "Лабораторна робота шифрування"
    
    task5_result = otp(task5_decrypted, task5_key)
    print(task5_result)
    
    # task6
    print("Task 6")
    task6_decrypted = ""
    task6_key = ""
    
    task6_result = otp(task6_decrypted, task6_key, True)
    print(task6_result)

