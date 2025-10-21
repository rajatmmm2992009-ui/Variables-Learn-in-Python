# Shopping Card System

product1_name = "Laptop"
product1_price = 500000
product1_quantity = 2

product2_name = "Keyboard"
product2_price = 100000
product2_quantity = 2

product3_name = "Mouse"
product3_price = 100000
product3_quantity = 2

total1 = product1_price * product1_quantity
total2 = product2_price * product2_quantity
total3 = product3_price * product3_quantity

subtotal = total1 + total2 + total3
gst = 0.18
final_amount = subtotal + gst

print("Shopping Card System")
print("=" * 30)
print(f"{product1_name} ({product1_quantity}) - Rs.{total1}")
print(f"{product2_name} ({product2_quantity}) - Rs.{total2}")
print(f"{product3_name} ({product3_quantity}) - Rs.{total3}")
print("=" * 30)
print("Subtotal;", subtotal)
print("GST (18%):", gst)
print("Final_Amount:", final_amount)


    