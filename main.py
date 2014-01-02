__author__ = 'rberkes'
from os import walk

def read_words(fp):
    wordarray=[]
    for line in fp:
        l=line.strip().split()
        for word in l:
            wordarray.append(word)
    return wordarray
def build_new_list(flist,f):
    newlist=[]
    for a in flist:
        if a==f:
            pass
        else:
            newlist.append(a)
    return newlist
def remove_repeats(flist,uniques,totals):
    firstTot=0
    firstUnq=0
    secondTot=0
    secondUnq=0
    for af in flist:
        newmaster=[]
        mfp=open('vfiles/'+af,'r')
        master=read_words(mfp)
        nflist=build_new_list(flist,af)
        for word in master:
            FOUND=False
            for f in nflist:
                fp=open('vfiles/'+f,'r')
                complist=read_words(fp)
                for w2 in complist:
                    if w2==word:
                        FOUND=True
                if FOUND:
                    continue
            if not FOUND:
                newmaster.append(word)
        uniques+=len(newmaster)
        totals+=len(master)
        if master[0]==newmaster[0]:
            firstTot+=1
            firstUnq+=1
        else:
            firstTot+=1
        if master[1]==newmaster[1]:
            secondTot+=1
            secondUnq+=1
        else:
            secondTot+=1
        print 'Master file: '+str(af)+" Length: "+str(len(master))+"/"+str(totals)+" Unique:"+str(len(newmaster))+"/"\
        + str(uniques)+" First Word: "+str(firstUnq)+"/"+str(firstTot)+" Second Word: "+str(secondUnq)+"/"+str(secondTot)

      #  print master
      #  print newmaster

    return
flist=[]
for (dirp,dirn,fnames) in walk('vfiles/'):
    flist.extend(fnames)
total_words=0
unique_words=0
remove_repeats(flist,unique_words,total_words)

