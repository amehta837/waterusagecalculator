from datetime import date
gallons = 0.0

def helping_strategy(target_choice):
  if target_choice == 1:
    needHelp = input("Type y for strategies to help with water consumption: ")
    if needHelp == "y":
      print("\n\nInstall Low-Flow Fixtures: Modern showerheads use 2.5 gallons per minute; older models can use 5–10 gallons per minute.\n\nTake Shorter Showers: Reducing shower time can significantly cut water use.")
  elif target_choice == 2:
    needHelp = input("Type y for strategies to help with water consumption: ")
    if needHelp == "y":
      print("\n\nAvoid Baths: Baths typically consume more water than showers.")
  elif target_choice == 3:
    needHelp = input("\nType y for strategies to help with water consumption: ")
    if needHelp == "y":
      print("\n\nUpgrade to Low-Flow Toilets: Low-flow toilets use 1.6 gallons per flush; older models can use up to 6 gallons.")
  elif target_choice == 4:
    needHelp = input("Type y for strategies to help with water consumption: ")
    if needHelp == "y":
      print("\n\nUse a dishwasher. Modern dishwashers use 3–5 gallons per load, while handwashing can use 10–20 gallons.")
  elif target_choice == 5:
    needHelp = input("Type y for strategies to help with water consumption: ")
    if needHelp == "y":
      print("\n\nWash Full Loads: Only run the dishwasher with a full load to maximize water efficiency.")
  elif target_choice == 6:
    needHelp = input("Type y for strategies to help with water consumption: ")
    if needHelp == "y":
      print("\n\nUse Efficient Washing Machines: Newer washing machines use 15–40 gallons per load; older models can use more.\n\nWash Full Loads: Only run the washing machine with a full load to maximize water efficiency.")
  elif target_choice == 7:
    needHelp = input("Type y for strategies to help with water consumption: ")
    if needHelp == "y":
      print("\n\nWater During Cooler Times: Watering in the early morning or late evening reduces evaporation.\n\nUse Efficient Irrigation Systems: Implementing drip irrigation systems can reduce water wastage.")

def dailylogfun(display=False, amount=""):
  global money
  global gallons
  def graphfun(dates, usage_per_date_list, money_list):
    import matplotlib.pyplot as plt
    import numpy as np

    xpoints = np.array(dates)
    ypoints = np.array(usage_per_date_list)

    plt.plot(xpoints, ypoints, marker='o')
    plt.xlabel("Date")
    plt.ylabel("Water Usage (gallons)")
    plt.title("Daily Water Usage")
    plt.grid(True)

    # Annotate money values on the graph
    for i, txt in enumerate(money_list):
      plt.annotate(f"${txt}", (xpoints[i], ypoints[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.show()
      
  if display:
    with open("dailyusage.txt", "r") as file:
      lines = file.readlines()
      for line in lines:
        print(line.strip())
    
    # Extract dates, usage values, and money values for the graph
    dates = []
    usage_per_date_list = []
    money_list = []
    for line in lines:
      parts = line.strip().split("\t")
      if len(parts) >= 3:
        dates.append(parts[0])  # Date
        usage = parts[1].split(" ")[0]  # Extract the numeric part of "X gallons"
        money = parts[2].replace("$", "")  # Extract the dollar amount
        usage_per_date_list.append(float(usage))
        money_list.append(money)
    
    # Call graphfun with extracted data
    graphfun(dates, usage_per_date_list, money_list)
    return

  today = str(date.today())
  
  # Read existing entries
  try:
    with open("dailyusage.txt", "r") as file:
      lines = file.readlines()
  except FileNotFoundError:
    lines = []

  # Check if we already have an entry for today
  updated = False
  new_lines = []
  for line in lines:
    if today in line:
      # Update existing entry for today
      entry = f"{today}\t{gallons} gallons\t${amount}"
      new_lines.append(entry + "\n")
      updated = True
    else:
      new_lines.append(line)

  # Add new entry if none exists for today
  if not updated:
    entry = f"{today}\t{gallons} gallons\t${amount}"
    new_lines.append(entry + "\n")

  # Write back all entries
  with open("dailyusage.txt", "w") as file:
    file.writelines(new_lines)

while True:
  print("")
  choice = int(input("Enter your recent activity: \n(enter any other number get total water bill) \n1. Showering\n2. Bathing\n3. Toilet flushing\n4. Hand-Washing Dishes\n5. Dishwasher\n6. Laundry\n7. Garden Watering\n8. View daily log\n"))
  print("")
  
  if choice == 1:
    gallons += 15.8
    print("Total gallons so far: " + str(gallons))
  elif choice == 2:
    gallons += 20.2
    print("Total gallons so far: " + str(gallons))
  elif choice == 3:
    gallons += 33.1
    print("Total gallons so far: " + str(gallons))
  elif choice == 4:
    gallons += 20
    print("Total gallons so far: " + str(gallons))
  elif choice == 5:
    gallons += 6
    print("Total gallons so far: " + str(gallons))
  elif choice == 6:
    gallons += 25
    print("Total gallons so far: " + str(gallons))
  elif choice == 7:
    minutes = float(input("Enter number of minutes watering: "))
    gallons = minutes * 8
    print("Total gallons so far: " + str(gallons))
  elif choice == 8:
    dailylogfun(display=True)
  money = str(round(gallons*0.005, 2))
  if money.index(money[-1]) == 1 + money.index("."):
    money += "0"
  dailylogfun(amount=money)
  print("")
  print("")
  if choice != 8:
    print("Your water bill is: " + "$" + money)
    print("")
    print("")
  if choice != 8:
    helping_strategy(choice)