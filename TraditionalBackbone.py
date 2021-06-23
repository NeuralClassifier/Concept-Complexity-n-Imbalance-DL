#Domain generation 

s = 1
c = 1
while s <= 5:
  c = 1
  while c <= 5:
    
    num_intervals = 2**c
    i = 1
    while i <=5 :

      gap_init = 0
      gap = float(1/num_intervals)
      gap_last = gap
      x = []
      y = []
      cls = '+'
      cnt = 0
      print('Size: ',s,' Complexity: ',c,' Imbalance: ',i)
      while gap_init < 1:
        
        if cls == '+':
          examples = 0
          print('1 class: ',ceil(((5000/32)*2**s)/2**c))
          while examples < ceil(((5000/32)*2**s)/2**c):
            x.append(random.uniform(gap_init,gap_last))
            y.append(1)
            examples+=1
        if cls == '-':
          examples = 0
          print('0 class: ',ceil((((5000/32)*2**s)/2**c)/(32/2**i)))
          while examples < ceil((((5000/32)*2**s)/2**c)/(32/2**i)):
            x.append(random.uniform(gap_init,gap_last))
            y.append(0)
            examples+=1
        

        cnt += 1
        print('cnt%2: ',cnt%2)
        if cnt%2 == 0:
          cls = '+'
        else:
          cls = '-'
        gap_last += gap
        gap_init += gap
      df_name = '/content/'+'size'+str(s)+'_complex'+str(c)+'_imbalance'+str(i)+'.xlsx'
      x=pd.DataFrame(x,columns=['X'])
      y=pd.DataFrame(y,columns=['Y'])
      df=pd.concat([x,y],axis=1)
      df.to_excel(df_name)
      i+=1
    c+=1 
  s+=1
