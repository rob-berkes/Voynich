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
def print_unique_positions(master,newl):
    count=0
    for a in master:
        if a in newl:
            print 'Position: '+str(count)
        count+=1
def word_count_to_file(TotList,UnqList,WORDSTOCOUNT):
    ofile=open('output.csv','w')
    print 'file opened, now writing...'
    for a in range(0,WORDSTOCOUNT):
        ofile.write(str(a)+','+str(UnqList[a])+','+str(TotList[a])+','+str(round(float(UnqList[a])/float(TotList[a]),4))+'\n')
    ofile.close()
    print 'all done!'
    return

def print_words_report(TotList,UnqList,WORDSTOCOUNT):
    for a in range(0,WORDSTOCOUNT):
        print "Word Number: "+str(a)+" Total Words: "+str(TotList[a])+" Unique Words: "+str(UnqList[a])+" "\
        +" Unique Percent: "+str(round(float(UnqList[a])/float(TotList[a]),4))
    return
def remove_repeats(flist,uniques,totals):
    firstTot=0
    firstUnq=0
    secondTot=0
    secondUnq=0
    WORDSTOCOUNT=200
    Tot_List=[]
    Unq_List=[]
    for a in range(0,WORDSTOCOUNT):
        Tot_List.append(0)
        Unq_List.append(0)
    f2list=['f65r']
    for af in flist:
        newmaster=[]
        try:
            mfp=open('vfiles/'+af,'r')
        except IOError:
            mfp=open('nonplants/'+af,'r')
        master=read_words(mfp)
        nflist=build_new_list(flist,af)
        complist=[]
        for f in nflist:
            try:
                fp=open('vfiles/'+f,'r')
            except IOError:
                fp=open('nonplants/'+f,'r')
            complist+=read_words(fp)
        for word in master:
            FOUND=False
            for w2 in complist:
                if w2==word:
                    FOUND=True
                    continue
            if not FOUND:
                newmaster.append(word)
        uniques+=len(newmaster)
        totals+=len(master)
        if len(master)<WORDSTOCOUNT:
            print af
            print 'above file is less than word count at '+str(len(master))
        for b in range(0,WORDSTOCOUNT):
            try:
                if master[b] in newmaster:
                    Tot_List[b]+=1
                    Unq_List[b]+=1
                elif b<len(master):
                    Tot_List[b]+=1
                elif b>=len(master):
                    continue
            except IndexError:
                continue
        print 'Master file: '+str(af)+" Length: "+str(len(master))+"/"+str(totals)+" Unique:"+str(len(newmaster))+"/"\
        + str(uniques)+" First Word: "+str(firstUnq)+"/"+str(firstTot)+" Second Word: "+str(secondUnq)+"/"+str(secondTot)

    print_words_report(Tot_List,Unq_List,WORDSTOCOUNT)
    word_count_to_file(Tot_List,Unq_List,WORDSTOCOUNT)
      #  print_unique_positions(master,newmaster)
      #2  print master
      #  print newmaster

    return
flist=[]
for (dirp,dirn,fnames) in walk('vfiles/'):
    flist.extend(fnames)
#for (dirp,dirn,fnames) in walk('nonplants/'):
#    flist.extend(fnames)
total_words=0
unique_words=0
remove_repeats(flist,unique_words,total_words)

