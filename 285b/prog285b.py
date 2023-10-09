from CL285b import Salesperson

def main():
  try:
    print("Number   code   sales   commission")
    people = []
    with open("data/285b.txt", 'r') as f:
      for line in f:
        ldata = line.split(" ")
        id = int(ldata[0])
        code = int(ldata[1])
        sales = float(ldata[2])
        
        dude = Salesperson(id, code, sales)
        people.append(dude)

    for sp in people:
      sp.calc()
      print(sp)
  except Exception as e:
    print("Error: ", e)


if __name__ == "__main__":
  main()