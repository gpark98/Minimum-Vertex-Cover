'''
Function for writing results
'''

def write_results(file,method,max_time,random_seed,V,time_update,vertex_cover_update,k):

    if method == 'BnB':

        name_file = file+'_'+method + '_' + str(max_time)
    else:
        name_file = file+'_'+method + '_' + str(max_time)+'_'+str(random_seed)

    file = open(name_file+'.sol','w')

    file.write('{:d}\n'.format(int(k)))

    for v in V[:-1]:

        file.write('{:d},'.format(int(v)))

    file.write('{:d}'.format(int(V[-1])))

    file.close()

    file = open(name_file+'.trace','w')

    for i in range(len(time_update)):

        file.write('{:.05f},{:d}\n'.format(float(time_update[i]),int(vertex_cover_update[i])))

    file.close()

