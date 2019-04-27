for r in range(4):
    for c in range(4):
        print("out["+str((r+(4*c))*8+7)+":"+str((r+(4*c))*8)+"]=state["+str(r)+"]["+str(c)+"];")