n=float(input('Digite a distância em metros:'))
km=n/1000
hm=n/100
dam=n/10
dm=n*10
cm=n*100
mm=n*1000
print('A medida de {} metros corresponde a:'.format(n))
print('{} quilômetros'.format(km))
print('{} hectômetros'.format(hm))
print('{} decâmetros'.format(dam))
print('{} decímetros'.format(dm))
print('{} centímetros'.format(cm))
print('{} milímetros'.format(mm))
