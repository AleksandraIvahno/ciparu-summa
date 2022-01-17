teksts = input("Ievadiet skaitli:")
def countnumbers (teksts): 
  summa = 0
  for simbols in teksts:
    summa = summa + int(simbols)
  print(summa)
  return summa
countnumbers (teksts)