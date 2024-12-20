import multiprocessing

# 1-misol
def raqamlar_yigindisi(numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"Raqamlar yig'indisi: {total}")


# 2-misol
def royhat_aralashtirish(lst):
    rotated = lst[1:] + lst[:1]
    print(f"Aylangan ro'yxat: {rotated}")


# 3-misol
def minumun_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    print(f"Min: {minimum}, Max: {maximum}")


# 4-misol
def Elementni_qidirish(lst, element):
    found = element in lst
    print(f"Element {element} topildi: {found}")


# 5-misol
def takronlanuvchi_royhat(lst):
    unique = list(set(lst))
    print(f"takronlanuvchielementlar: {unique}")


# 6-misol
def sozlarni_teskari(words):
    tesakri_qil = [word[::-1] for word in words]
    print(f"tesakri_qil: {tesakri_qil}")


# 7-misol
def royhatni_uzunligi(words):
    longest = max(words, key=len)
    print(f"royhati uzunligi: {longest}")


# 8-misol
def a(dct):
    values = list(dct.values())
    b = {value for value in values if values.count(value) > 1}
    print(f"Ikki nusxadagi qiymatlar: {b}")


# 9-misol
def a(dct):
    raqm = sorted([v for v in dct.values() if isinstance(v, (int, float))])
    print(f"sara raqam: {raqm}")


# 10-misol
def ikiga_kopaytirmasi(dct):
    a = {k: (v * 2 if isinstance(v, (int, float)) else v) for k, v in dct.items()}
    print(f"2 kaeasi: {a}")


# 11-misol
def long_short(dct):
    max_key = max(dct, key=dct.get)
    print(f"eng kata va eng kichik: {max_key}")


# 12-misol
def ortacha_arimat(dct):
    a = [v for v in dct.values() if isinstance(v, (int, float))]
    average = sum(a) / len(a) if a else 0
    print(f"ortacha qimat: {average}")


# 13-misol
def ikki_lugat_birlashtirish(d1, d2):
    a = d1.copy()
    for k, v in d2.items():
        a[k] = a.get(k, 0) + v
    print(f"luhat bilashtirish: {a}")


# 14-misol
def eng_uzun_eng_kalt(dct):
    keys = list(dct.keys())
    uzun = max(keys, key=len)
    kalta = min(keys, key=len)
    print(f"eng uzun: {uzun}, eng kalta: {kalta}")


# 15-misol
def string_raqamlar(dct):
    converted = {k: (int(v) if isinstance(v, str) and v.isdigit() else v) for k, v in dct.items()}
    print(f"stiring raqamlar: {converted}")





if __name__ == "__main__":
    dictionary = {"a": 1, "b": "2", "c": "hello", "d": 4}

    processes = [
        multiprocessing.Process(target=raqamlar_yigindisi, args=([21324,453,56],)),
        multiprocessing.Process(target=royhat_aralashtirish, args=([198, 2, 3, 4],)),
        multiprocessing.Process(target=minumun_max, args=([3543,3,6,7],)),
        multiprocessing.Process(target=Elementni_qidirish, args=([7,5,9], 3)),
        multiprocessing.Process(target=takronlanuvchi_royhat, args=([198, 2, 2, 3, 4, 4, 5],)),
        multiprocessing.Process(target=sozlarni_teskari, args=(["husanbo"],)),
        multiprocessing.Process(target=royhatni_uzunligi, args=(["husanbo"],)),
        multiprocessing.Process(target=a, args=({"a": 198, "b": 2, "c": 198, "d": 3},)),
        multiprocessing.Process(target=a, args=(dictionary,)),
        multiprocessing.Process(target=ikiga_kopaytirmasi, args=(dictionary,)),
        multiprocessing.Process(target=long_short, args=({"a": 198, "b": 3, "c": 2},)),
        multiprocessing.Process(target=ortacha_arimat, args=({"a": 67, "b": 6, "c": 9},)),
        multiprocessing.Process(target=ikki_lugat_birlashtirish, args=({"a": 123, "b": 67}, {"b": 54, "c": 3})),
        multiprocessing.Process(target=eng_uzun_eng_kalt, args=({"short": 198, "longest_key": 2},)),
        multiprocessing.Process(target=string_raqamlar, args=(dictionary,)),
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
