# Movie Ticket Booking Systems

movie_name = "Rajat Singhaniya"
movie_time = "12:00"
screen_number = 3
ticket_price = 250
seats_available = 45

customer_name = "Rajat"
number_of_tickets = 3
seat_numbers = "F5, F6, F7"

total_cost = ticket_price * number_of_tickets
gst_amount= total_cost * 0.12
convenience_fee = 30
final_amount = total_cost + gst_amount + convenience_fee
seats_available -= number_of_tickets

print("Movie Tickets")
print("=" * 30)
print(f"Movie: {movie_name}")
print(f"Time: {movie_time}")
print(f"Customer: {customer_name}")
print(f"Tickets: {number_of_tickets} | Seats: {seat_numbers}")
print(f"Base Price: Rs.{total_cost}")
print(f"GST (12%): Rs.{gst_amount:.2f}")
print(f"Convenience Fee: Rs.{convenience_fee}")
print(f"Total_Amount: Rs.{final_amount:.2f}")
print(f"Remaining Seats: {seats_available}")

