# Hotel

This project explores the **Hotel Bookings Dataset** to extract actionable business insights.  
Using **SQL, Python (pandas, matplotlib)**, and **data visualization techniques**, the project answers key business questions about customer behavior, hotel performance, seasonality, and booking channels.


## Key Insights
- **City Hotels** dominate in total bookings, but **Resort Hotels** have **longer average stays**.
- **Cancellation rates** are notably higher for City Hotels.
- **Summer months** (especially [insert peak month]) see the highest booking volumes.
- **Online Travel Agencies** are the primary source of bookings, representing a key partnership opportunity.
- Guests come predominantly from [Top 3 countries].

## Try the App

https://chvh7vulwjyxfvg98qg82c.streamlit.app/

- Takes booking details (like lead time, deposit type, customer type, etc.)
- Uses a logistic regression model to predict cancellation
- If risk is high, it suggests actions like:
  - Offer a 5% discount
  - Add free breakfast
  - Allow late check-out
