#Colin's Images: Complexity 3

#Class A

#Training Data

c=5
num_intervals = 2**c
gap_init = 0
gap = float(1/num_intervals)
gap_last = gap
x = []
y = []
board_x=[]
board_y=[]
arr=1
total_images = 5000
gen_count = 0
while gen_count < total_images:
  c=5
  num_intervals = 2**c
  gap_init = 0
  gap = float(1/num_intervals)
  gap_last = gap
  x = []
  y = []
  board_x=[]
  board_y=[]
  arr=1
  while arr<=num_intervals+1:
    gap_init = 0
    gap = float(1/num_intervals)
    gap_last = gap
    gap1 = gap_init
    gap2 = gap_last
    x = []
    y = []
    times_end = round(11/2)
    times = random.randint(1,times_end)
    while gap_init <=1:
      x.append(0.1)
    
      gap_last += gap
      gap_init += gap
    
    if arr<11:
      tms = 1
      lst_pxl = []
      while tms <= times:
        pxl = random.randint(0,11)
        if pxl not in lst_pxl:
          x[pxl] = 1
        tms+=1
    if arr>11 and arr<21:

      tms = 1
      lst_pxl = []
      while tms <= times:
        pxl = random.randint(0,11)
        if pxl not in lst_pxl:
          x[pxl] = 1
        tms+=1

      tms = 1
      lst_pxl = []
      while tms <= times:
        pxl = random.randint(11,21)
        if pxl not in lst_pxl:
          x[pxl] = 1
        tms+=1
    
    if arr>21 and arr<=32:
      tms = 1
      lst_pxl = []
      while tms <= times:
        pxl = random.randint(21,32)
        if pxl not in lst_pxl:
          x[pxl] = 1
        tms+=1

    board_x.append(x)
    board_y.append(y)
    arr+=1

  k=np.array(board_x)
  io.imshow(k)
  #plt.xlim([0, 1])
  plt.rcParams.update({'font.size': 18})
  plt.axis('off')
  plt.savefig('/content/A/ColinImageIdeaP1_C3_ClassA_inst'+str(gen_count)+'.png')
  plt.show()
  gen_count += 1


#Class B
c=5
num_intervals = 2**c
gap_init = 0
gap = float(1/num_intervals)
gap_last = gap
x = []
y = []
board_x=[]
board_y=[]
arr=1
total_images = 5000
gen_count = 0
while gen_count < total_images:
  c=5
  num_intervals = 2**c
  gap_init = 0
  gap = float(1/num_intervals)
  gap_last = gap
  x = []
  y = []
  board_x=[]
  board_y=[]
  arr=1
  while arr<=num_intervals+1:
    gap_init = 0
    gap = float(1/num_intervals)
    gap_last = gap
    gap1 = gap_init
    gap2 = gap_last
    x = []
    y = []
    times_end = round(11/2)
    times = random.randint(1,times_end)
    while gap_init <=1:
      x.append(0.1)
    
      gap_last += gap
      gap_init += gap
    tms = 1
    lst_pxl = []
    while tms <= times:
      pxl = random.randint(11,21)
      if pxl not in lst_pxl:
        x[pxl] = 1
      tms+=1
    board_x.append(x)
    board_y.append(y)
    arr+=1

  k=np.array(board_x)
  io.imshow(k)
  #plt.xlim([0, 1])
  plt.rcParams.update({'font.size': 18})
  plt.axis('off')
  plt.savefig('/content/B/ColinImageIdeaP1_C3_ClassB_inst'+str(gen_count)+'.png')
  plt.show()
  gen_count +=1


#Class C
c=5
num_intervals = 2**c
gap_init = 0
gap = float(1/num_intervals)
gap_last = gap
x = []
y = []
board_x=[]
board_y=[]
arr=1
total_images = 5000
gen_count = 0
while gen_count < total_images:
  c=5
  num_intervals = 2**c
  gap_init = 0
  gap = float(1/num_intervals)
  gap_last = gap
  x = []
  y = []
  board_x=[]
  board_y=[]
  arr=1
  while arr<=num_intervals+1:
    gap_init = 0
    gap = float(1/num_intervals)
    gap_last = gap
    gap1 = gap_init
    gap2 = gap_last
    x = []
    y = []
    times_end = round(11/2)
    times = random.randint(1,times_end)
    while gap_init <=1:
      x.append(0.1)
    
      gap_last += gap
      gap_init += gap
    
    if arr<11:
      tms = 1
      lst_pxl = []
      while tms <= times:
        pxl = random.randint(21,32)
        if pxl not in lst_pxl:
          x[pxl] = 1
        tms+=1
    if arr>11 and arr<21:

      tms = 1
      lst_pxl = []
      while tms <= times:
        pxl = random.randint(21,32)
        if pxl not in lst_pxl:
          x[pxl] = 1
        tms+=1

      tms = 1
      lst_pxl = []
      while tms <= times:
        pxl = random.randint(11,21)
        if pxl not in lst_pxl:
          x[pxl] = 1
        tms+=1
    
    if arr>21 and arr<=32:
      tms = 1
      lst_pxl = []
      while tms <= times:
        pxl = random.randint(0,11)
        if pxl not in lst_pxl:
          x[pxl] = 1
        tms+=1

    board_x.append(x)
    board_y.append(y)
    arr+=1

  k=np.array(board_x)
  io.imshow(k)
  #plt.xlim([0, 1])
  plt.rcParams.update({'font.size': 18})
  plt.axis('off')
  plt.savefig('/content/C/ColinImageIdeaP1_C3_ClassC_inst'+str(gen_count)+'.png')
  plt.show()
  gen_count += 1
