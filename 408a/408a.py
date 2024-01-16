import time

from 408a.408sorting import BubbleSort
def main():
  try:
    dataI = []
    dataS = []
    with open("prg408a.dat", 'r') as f:
      lines = f.readlines()
      for lcv in range(len(lines)):
        id, score = lines[lcv].split(' ')
        id = int(id)
        score = int(score)
        # Make helper class objects and add to data
        dataI.append(id)
        dataS.append(score)
    pass
    # Your code here
    list = dataS[:]
    list2 = dataS[:]
    list3 = dataS[:]
    list4 = dataS[:]

    start = time.perf_counter
    
    end = time.perf_counter
    print(list)
  except Exception as e:
    print("Error:", e)
  pass


if __name__ == "__main__":
  main()