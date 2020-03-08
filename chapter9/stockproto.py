"""
stockproto.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


shares = input("Enter quantity of shares: ")
entry = input("Enter price per share: ")
exit_num = input("Enter future exit price per share: ")
print("Cost to get in: $%f" % (int(shares) * float(entry)))
print("Exit: $%f" % (int(shares) * float(exit_num)))
profit = ((int(shares) * float(exit_num)) - (int(shares) * float(entry)))
print("Profit: $%f" % profit)
