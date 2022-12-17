per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = input("Введите сумму -")
tkb = per_cent.get('ТКБ')
skb = per_cent.get('СКБ')
vtb = per_cent.get('ВТБ')
sber = per_cent.get('СБЕР')
b = float(a)
tkb1 = tkb*b/100
skb1 = skb*b/100
vtb1 = vtb*b/100
sber1 = sber*b/100

tkb2 = int(tkb1)
skb2 = int(skb1)
vtb2 = int(vtb1)
sber2 = int(sber1)

c = [tkb2, skb2, vtb2, sber2]
deposit = max(c)
print("Максимальная сумма, которую вы можете заработать", deposit)
