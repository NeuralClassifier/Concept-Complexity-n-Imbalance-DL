#Gaussian Backbone (including overlap)
#s=5, c=2

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
  return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)



i=1
while i <= 5:
  print('We are at i = ', i)
  
  if i==1:
    
    #V1
    
    X1 = get_truncated_normal(mean=0.125, sd=0.024, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.024, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.024, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.024, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(78)
    y2 = np.zeros(78)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(78)
    y4 = np.zeros(78)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V1/figs/hist/GausBackbone_hist_s5c2_v1i1.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    plt.savefig('/content/V1/figs/dist/GausBackbone_distplot_s5c2_v1i1.pdf')
    plt.rcParams.update({'font.size': 18})
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v1 = pd.concat([X,Y],axis=1)
    print(bd_v1)
    #bd_v1.to_excel('/content/V1/GausBackbone_s5c2_v1i1.xlsx')


    #V2
    
    X1 = get_truncated_normal(mean=0.125, sd=0.048, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.048, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.048, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.048, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(78)
    y2 = np.zeros(78)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(78)
    y4 = np.zeros(78)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V2/figs/hist/GausBackbone_hist_s5c2_v2i1.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    plt.savefig('/content/V2/figs/dist/GausBackbone_distplot_s5c2_v2i1.pdf')
    plt.rcParams.update({'font.size': 18})
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v2 = pd.concat([X,Y],axis=1)
    print(bd_v2)
    #bd_v2.to_excel('/content/V2/GausBackbone_s5c2_v2i1.xlsx')


    #V3
    
    X1 = get_truncated_normal(mean=0.125, sd=0.06, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.06, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.06, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.06, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(78)
    y2 = np.zeros(78)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(78)
    y4 = np.zeros(78)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V3/figs/hist/GausBackbone_hist_s5c2_v3i1.pdf')
    plt.rcParams.update({'font.size': 18})
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    plt.savefig('/content/V3/figs/dist/GausBackbone_distplot_s5c2_v3i1.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v3 = pd.concat([X,Y],axis=1)
    print(bd_v3)
    #bd_v3.to_excel('/content/V3/GausBackbone_s5c2_v3i1.xlsx')


    #V4
    
    X1 = get_truncated_normal(mean=0.125, sd=0.08, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.08, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.08, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.08, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(78)
    y2 = np.zeros(78)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(78)
    y4 = np.zeros(78)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V4/figs/hist/GausBackbone_hist_s5c2_v4i1.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    plt.savefig('/content/V4/figs/dist/GausBackbone_distplot_s5c2_v4i1.pdf')
    plt.rcParams.update({'font.size': 18})
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v4 = pd.concat([X,Y],axis=1)
    print(bd_v4)
    #bd_v4.to_excel('/content/V4/GausBackbone_s5c2_v4i1.xlsx')

    #V5
    
    X1 = get_truncated_normal(mean=0.125, sd=0.12, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.12, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.12, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.12, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(78)
    y2 = np.zeros(78)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(78)
    y4 = np.zeros(78)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V5/figs/hist/GausBackbone_hist_s5c2_v5i1.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    plt.savefig('/content/V5/figs/dist/GausBackbone_distplot_s5c2_v5i1.pdf')
    plt.rcParams.update({'font.size': 18})
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v5 = pd.concat([X,Y],axis=1)
    print(bd_v5)
    #bd_v5.to_excel('/content/V5/GausBackbone_s5c2_v5i1.xlsx')



  #i=2

  if i==2:
  
    #V1
    
    X1 = get_truncated_normal(mean=0.125, sd=0.024, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.024, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.024, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.024, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(156)
    y2 = np.zeros(156)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(156)
    y4 = np.zeros(156)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V1/figs/hist/GausBackbone_hist_s5c2_v1i2.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V1/figs/dist/GausBackbone_distplot_s5c2_v1i2.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v1 = pd.concat([X,Y],axis=1)
    print(bd_v1)
    #bd_v1.to_excel('/content/V1/GausBackbone_s5c2_v1i2.xlsx')


    #V2
    
    X1 = get_truncated_normal(mean=0.125, sd=0.048, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.048, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.048, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.048, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(156)
    y2 = np.zeros(156)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(156)
    y4 = np.zeros(156)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V2/figs/hist/GausBackbone_hist_s5c2_v2i2.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V2/figs/dist/GausBackbone_distplot_s5c2_v2i2.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v2 = pd.concat([X,Y],axis=1)
    print(bd_v2)
    #bd_v2.to_excel('/content/V2/GausBackbone_s5c2_v2i2.xlsx')


    #V3
    
    X1 = get_truncated_normal(mean=0.125, sd=0.06, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.06, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.06, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.06, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(156)
    y2 = np.zeros(156)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(156)
    y4 = np.zeros(156)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V3/figs/hist/GausBackbone_hist_s5c2_v3i2.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V3/figs/dist/GausBackbone_distplot_s5c2_v3i2.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v3 = pd.concat([X,Y],axis=1)
    print(bd_v3)
    #bd_v3.to_excel('/content/V3/GausBackbone_s5c2_v3i2.xlsx')


    #V4
    
    X1 = get_truncated_normal(mean=0.125, sd=0.08, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.08, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.08, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.08, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(156)
    y2 = np.zeros(156)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(156)
    y4 = np.zeros(156)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V4/figs/hist/GausBackbone_hist_s5c2_v4i2.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V4/figs/dist/GausBackbone_distplot_s5c2_v4i2.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v4 = pd.concat([X,Y],axis=1)
    print(bd_v4)
    #bd_v4.to_excel('/content/V4/GausBackbone_s5c2_v4i2.xlsx')

    #V5
    
    X1 = get_truncated_normal(mean=0.125, sd=0.12, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.12, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.12, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.12, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(156)
    y2 = np.zeros(156)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(156)
    y4 = np.zeros(156)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V5/figs/hist/GausBackbone_hist_s5c2_v5i2.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V5/figs/dist/GausBackbone_distplot_s5c2_v5i2.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v5 = pd.concat([X,Y],axis=1)
    print(bd_v5)
    #bd_v5.to_excel('/content/V5/GausBackbone_s5c2_v5i2.xlsx')


  #i=3

  if i==3:
  
    #V1
    
    X1 = get_truncated_normal(mean=0.125, sd=0.024, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.024, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.024, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.024, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(313)
    y2 = np.zeros(313)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(313)
    y4 = np.zeros(313)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V1/figs/hist/GausBackbone_hist_s5c2_v1i3.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V1/figs/dist/GausBackbone_distplot_s5c2_v1i3.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v1 = pd.concat([X,Y],axis=1)
    print(bd_v1)
    #bd_v1.to_excel('/content/V1/GausBackbone_s5c2_v1i3.xlsx')


    #V2
    
    X1 = get_truncated_normal(mean=0.125, sd=0.048, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.048, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.048, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.048, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(313)
    y2 = np.zeros(313)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(313)
    y4 = np.zeros(313)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V2/figs/hist/GausBackbone_hist_s5c2_v2i3.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V2/figs/dist/GausBackbone_distplot_s5c2_v2i3.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v2 = pd.concat([X,Y],axis=1)
    print(bd_v2)
    #bd_v2.to_excel('/content/V2/GausBackbone_s5c2_v2i3.xlsx')


    #V3
    
    X1 = get_truncated_normal(mean=0.125, sd=0.06, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.06, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.06, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.06, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(313)
    y2 = np.zeros(313)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(313)
    y4 = np.zeros(313)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V3/figs/hist/GausBackbone_hist_s5c2_v3i3.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V3/figs/dist/GausBackbone_distplot_s5c2_v3i3.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v3 = pd.concat([X,Y],axis=1)
    print(bd_v3)
    #bd_v3.to_excel('/content/V3/GausBackbone_s5c2_v3i3.xlsx')


    #V4
    
    X1 = get_truncated_normal(mean=0.125, sd=0.08, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.08, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.08, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.08, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(313)
    y2 = np.zeros(313)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(313)
    y4 = np.zeros(313)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V4/figs/hist/GausBackbone_hist_s5c2_v4i3.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V4/figs/dist/GausBackbone_distplot_s5c2_v4i3.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v4 = pd.concat([X,Y],axis=1)
    print(bd_v4)
    #bd_v4.to_excel('/content/V4/GausBackbone_s5c2_v4i3.xlsx')

    #V5
    
    X1 = get_truncated_normal(mean=0.125, sd=0.12, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.12, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.12, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.12, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(313)
    y2 = np.zeros(313)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(313)
    y4 = np.zeros(313)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V5/figs/hist/GausBackbone_hist_s5c2_v5i3.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V5/figs/dist/GausBackbone_distplot_s5c2_v5i3.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v5 = pd.concat([X,Y],axis=1)
    print(bd_v5)
    #bd_v5.to_excel('/content/V5/GausBackbone_s5c2_v5i3.xlsx')


  #i=4

  if i==4:
  
    #V1
    
    X1 = get_truncated_normal(mean=0.125, sd=0.024, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.024, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.024, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.024, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(625)
    y2 = np.zeros(625)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(625)
    y4 = np.zeros(625)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V1/figs/hist/GausBackbone_hist_s5c2_v1i4.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V1/figs/dist/GausBackbone_distplot_s5c2_v1i4.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v1 = pd.concat([X,Y],axis=1)
    print(bd_v1)
    #bd_v1.to_excel('/content/V1/GausBackbone_s5c2_v1i4.xlsx')


    #V2
    
    X1 = get_truncated_normal(mean=0.125, sd=0.048, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.048, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.048, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.048, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(625)
    y2 = np.zeros(625)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(625)
    y4 = np.zeros(625)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V2/figs/hist/GausBackbone_hist_s5c2_v2i4.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V2/figs/dist/GausBackbone_distplot_s5c2_v2i4.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v2 = pd.concat([X,Y],axis=1)
    print(bd_v2)
    #bd_v2.to_excel('/content/V2/GausBackbone_s5c2_v2i4.xlsx')


    #V3
    
    X1 = get_truncated_normal(mean=0.125, sd=0.06, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.06, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.06, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.06, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(625)
    y2 = np.zeros(625)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(625)
    y4 = np.zeros(625)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V3/figs/hist/GausBackbone_hist_s5c2_v3i4.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V3/figs/dist/GausBackbone_distplot_s5c2_v3i4.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v3 = pd.concat([X,Y],axis=1)
    print(bd_v3)
    #bd_v3.to_excel('/content/V3/GausBackbone_s5c2_v3i4.xlsx')


    #V4
    
    X1 = get_truncated_normal(mean=0.125, sd=0.08, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.08, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.08, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.08, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(625)
    y2 = np.zeros(625)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(625)
    y4 = np.zeros(625)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V4/figs/hist/GausBackbone_hist_s5c2_v4i4.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V4/figs/dist/GausBackbone_distplot_s5c2_v4i4.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v4 = pd.concat([X,Y],axis=1)
    print(bd_v4)
    #bd_v4.to_excel('/content/V4/GausBackbone_s5c2_v4i4.xlsx')

    #V5
    
    X1 = get_truncated_normal(mean=0.125, sd=0.12, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.12, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.12, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.12, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(625)
    y2 = np.zeros(625)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(625)
    y4 = np.zeros(625)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V5/figs/hist/GausBackbone_hist_s5c2_v5i4.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V5/figs/dist/GausBackbone_distplot_s5c2_v5i4.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v5 = pd.concat([X,Y],axis=1)
    print(bd_v5)
    #bd_v5.to_excel('/content/V5/GausBackbone_s5c2_v5i4.xlsx')

  #i=5

  if i==5:
  
    #V1
    
    X1 = get_truncated_normal(mean=0.125, sd=0.024, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.024, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.024, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.024, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(1250)
    y2 = np.zeros(1250)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(1250)
    y4 = np.zeros(1250)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V1/figs/hist/GausBackbone_hist_s5c2_v1i5.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V1/figs/dist/GausBackbone_distplot_s5c2_v1i5.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v1 = pd.concat([X,Y],axis=1)
    print(bd_v1)
    #bd_v1.to_excel('/content/V1/GausBackbone_s5c2_v1i5.xlsx')


    #V2
    
    X1 = get_truncated_normal(mean=0.125, sd=0.048, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.048, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.048, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.048, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(1250)
    y2 = np.zeros(1250)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(1250)
    y4 = np.zeros(1250)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V2/figs/hist/GausBackbone_hist_s5c2_v2i5.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V2/figs/dist/GausBackbone_distplot_s5c2_v2i5.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v2 = pd.concat([X,Y],axis=1)
    print(bd_v2)
    #bd_v2.to_excel('/content/V2/GausBackbone_s5c2_v2i5.xlsx')


    #V3
    
    X1 = get_truncated_normal(mean=0.125, sd=0.06, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.06, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.06, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.06, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(1250)
    y2 = np.zeros(1250)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(1250)
    y4 = np.zeros(1250)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V3/figs/hist/GausBackbone_hist_s5c2_v3i5.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V3/figs/dist/GausBackbone_distplot_s5c2_v3i5.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v3 = pd.concat([X,Y],axis=1)
    print(bd_v3)
    #bd_v3.to_excel('/content/V3/GausBackbone_s5c2_v3i5.xlsx')


    #V4
    
    X1 = get_truncated_normal(mean=0.125, sd=0.08, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.08, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.08, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.08, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(1250)
    y2 = np.zeros(1250)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(1250)
    y4 = np.zeros(1250)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V4/figs/hist/GausBackbone_hist_s5c2_v4i5.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V4/figs/dist/GausBackbone_distplot_s5c2_v4i5.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v4 = pd.concat([X,Y],axis=1)
    print(bd_v4)
    #bd_v4.to_excel('/content/V4/GausBackbone_s5c2_v4i5.xlsx')

    #V5
    
    X1 = get_truncated_normal(mean=0.125, sd=0.12, low=0, upp=0.375)
    X2 = get_truncated_normal(mean=0.375, sd=0.12, low=0.125, upp=0.625)
    X3 = get_truncated_normal(mean=0.625, sd=0.12, low=0.375, upp=0.875)
    X4 = get_truncated_normal(mean=0.875, sd=0.12, low=0.625, upp=1)

    X1 = X1.rvs(1250)
    y1 = np.ones(1250)
    X2 = X2.rvs(1250)
    y2 = np.zeros(1250)
    X3 = X3.rvs(1250)
    y3 = np.ones(1250)
    X4 = X4.rvs(1250)
    y4 = np.zeros(1250)

    plt.scatter(X1,y1)
    plt.scatter(X2,y2)
    plt.scatter(X3,y3)
    plt.scatter(X4,y4)

    fig, ax = plt.subplots(1, sharex=True)
    ax.hist(X1, color='black', ec="skyblue")
    ax.hist(X2, color='fuchsia', ec="skyblue")
    ax.hist(X3, color='black', ec="skyblue")
    ax.hist(X4, color='fuchsia', ec="skyblue")
    #plt.savefig('/content/V5/figs/hist/GausBackbone_hist_s5c2_v5i5.pdf')
    plt.show()    

    sns.distplot(X1, color='black')
    sns.distplot(X2, color='fuchsia')
    sns.distplot(X3, color='black')
    sns.distplot(X4, color='fuchsia')
    #plt.savefig('/content/V5/figs/dist/GausBackbone_distplot_s5c2_v5i5.pdf')
    plt.show()

    X = np.hstack((X1,X2,X3,X4))
    Y = np.hstack((y1,y2,y3,y4))

    X = pd.DataFrame(X,columns=['X'])
    Y = pd.DataFrame(Y,columns=['Y'])
    bd_v5 = pd.concat([X,Y],axis=1)
    print(bd_v5)
    #bd_v5.to_excel('/content/V5/GausBackbone_s5c2_v5i5.xlsx')

    

  


  i+=1
