class FindIndex():
    def find_index(self,args,parameter):
        index=[]
        for i in range(len(args)):
            if isinstance(args[i],list):
                for j in range(len(args[i])):
                    if args[i][j] == parameter:
                        index.append([i,j])
            else:
                if args[i] == parameter:
                    index.append(i)
        return index
if __name__ == '__main__':
    l = [1,[2,3],[45,26],9,[1,2,4,4,6,5,2,6,7]]
    index = FindIndex().find_index(l,4)
    print(index)

